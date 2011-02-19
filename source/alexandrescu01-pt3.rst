======================================================================
Modern C++ Design 読書ノート 3/3
======================================================================

:doc:`alexandrescu01-pt2` からの続き。

:著者: Andrey Alexandrescu
:訳者: 村上雅章
:出版社: ピアソン・エデュケーション
:ISBN: 4-89471-435-3

.. contents:: ノート目次

第 9 章 Abstract Factory
======================================================================

<もしも、 ``ConventionalDialog`` 中では ``FunkyButton`` を使用させたくないのであれば、
Abstract Factory デザイン・パターンを使用することによって ``FunkyDialog`` 中でのみ
``FunkyButton`` が使用されるように保証することができます> (p. 231)

----

<ゲーム中に登場する全てのオブジェクトを生成する関数を 1 ヶ所に集めておくのが良いでしょう> (p. 232)

.. code-block:: c++

   class AbstractEnemyFactory
   {
   public:
       virtual Soldier* MakeSoldier() = 0;
       virtual Monster* MakeMonster() = 0;
       virtual SuperMonster* MakeSuperMonster() = 0;
   };
   
   class EasyLevelEnemyFactory : public AbstractEnemyFactory
   {
       ...
   };
   class DieHardLevelEnemyFactory : public AbstractEnemyFactory
   {
       ...
   };

* <Abstract Factory の主な欠点は、それが型と強く結びついている点です。
  （略）Abstract Factory の基底クラスは、
  生成を行う全ての抽象的な成果物を知っていなければならないのです> (p. 234)

* <型の安全性を取るか、それとも低依存性を取るかという古典的なジレンマが、
  C++ ではしばしば発生するわけです> (p. 234)

----

ここからジェネリックな Abstract Factory の設計に入る。

構造は、以前取り扱った ``GenScatterHierarchy`` と、
ファクトリーユニットなるクラステンプレートの群を合体させたようなもの。

.. code-block:: c++

   // p. 235 より引用。
   template <class T>
   class AbstractFactoryUnit
   {
   public:
       virtual T* DoCreate(Type2Type<T>) = 0;
       virtual ~AbstractFactoryUnit() {}
   };
   
   template
   <
       class TList,
       template <class> class Unit = AbstractFactoryUnit
   >
   class AbstractFactory : public GenScatterHierarchy<TList, Unit>
   {
   public:
       typedef TList ProductList;
       template <class T> T* Create()
       {
           Unit<T>& unit = *this;
           return unit.DoCreate(Type2Type<T>());
       }
   };

   // p. 236
   typedef AbstractFactory
   <
      TYPELIST_3(Soldier, Monster, SuperMonster)
   >
   AbstractEnemyFactory;

* <``Type2Type`` は、オーバーロード関数の曖昧さを無くすという目的のみを持った単純なテンプレート> (p. 235)
  <``AbstractFactoryUnit`` の実体が同じ継承階層にいくつも現れることになる> (p. 235) ので、
  ``DoCreate`` にこの引数が要る。

* ``AbstractFactory::Create`` は、<生成要求を適切な基底クラスへと振り分けるディスパッチャ> (p. 236) となる。

----

``AbstractFactory`` は固まったので、次は ``ConcreteFactory`` を設計する。

* ``ConcreteFactory`` だけでなく、concrete な ``AbstractFactoryUnit`` も必要。
* ``ConcreteFactory`` はクラステンプレート ``GenLinearHierarchy`` から導出する。
  何をしたいのかと言うと、Factory Unit のクラス継承を直列させたいわけだ。

.. code-block:: c++

   // p. 238 より引用
   template <class ConcreteProduct, class Base>
   class OpNewFactoryUnit : public Base // Base は多分 AbstractFactoryUnit<ConcreteProduct>
   {
       ...

   public:
       // この AbstractProduct を typedef するのがちょっと頭を使う。
       ConcreteProduct* DoCreate(Type2Type<AbstractProduct>)
       {
           return new ConcreteProduct;
       }
   };
   
   // p. 239
   template
   <
       class AbstractFact,
       template <class, class> class Creator = OpNewFactoryUnit,
       class TList = typename AbstractFact::ProductList
   >
   class ConcreteFactory
       : public GenLinearHierarchy< ... >
   {
       ...
   };

----

Prototype バージョンを設計する。

* テンプレートクラス ``PrototypeFactoryUnit`` を定義する。
  ``DoCreate`` の実装では、何かオブジェクトを参照しておいて、そこからクローン作成。

* 先程の ``ConcreteFactory`` がそのまま利用できる。

  .. code-block:: c++
  
     typedef ConcreteFactory
     <
         AbstractEnemyFactory,
         PrototypeFactoryUnit
     >
     EnemyFactory;

* <Abstract Factory デザイン・パターンを手作業で実装して、
  こういった利点全てを満足するようなものを作る手間を考えてみてください> (p. 244)
  
  →大変なことはよく理解した。

第 10 章 Visitor
======================================================================

* メリット：クラス階層や既存コードを再コンパイルせずに、仮想関数を追加できる。
* デメリット：<階層の末端にクラスを追加した場合、
  階層や全ての既存のコードの再コンパイルが必要になる> (p. 249)

----

* <機能拡張は、新たなクラスを追加するか、
  新たな仮想メンバ関数を追加するかのいずれかによって実現できます> (p. 249)

* <新たなクラスの追加は簡単であり、新たな仮想メンバ関数の追加は難しい> (p. 250)

* 従って、こういう場合の裏に対しては、Visitor が役に立つ。

ここから架空の文書エディターを開発する場合を考察していく。

.. code-block:: c++

   // pp. 250-251 引用一部略
   class DocStats // 文書の統計情報
   {
   public:
       void AddChars(xxxx); // 文字数
       void AddWords(xxxx); // 単語数
       void AddImages(xxxx); // 画像数
       ...
       
       void Display(); // 統計情報表示
   };
   
   class DocElement;
       class Paragraph;
       class RasterBitmap;
 
   class DocElement
   {
   public:
       // DocElement が Paragraph だったら AddChars や AddWords を利用するし、
       // RasterBitmap だったら AddImages を利用して、統計をとる。
       virtual void UpdateStats(DocStats& statistics) = 0;
   };

いくつか欠点がある。

* <``DocStats`` を修正する度に、 ``DocElement`` 階層全体を再コンパイルする必要がある> (p. 251)
* <統計情報の収集を行う実際の処理が、 ``UpdateStats`` の実装全体に散りばめられます> (p. 251)
* その他

発想を変えて、 ``UpdateStats`` を ``DocStats`` に移動させてみると、
<今度は ``DocStats`` が、処理対象となる具体的な ``DocElement`` に依存することになります> (p. 252)

.. code-block:: c++

   // p. 252 より引用一部略
   void DocStats::UpdateStats(DocElement& elem)
   {
       if(Paragraph* p = dynamic_cast<Paragraph*>(&elem))
       {
           // Paragraph の統計収集...
       }
       else if(dynamic_cast<RasterBitmap*>(&elem))
       {
           // RasterBitmap の統計収集...
       }
       else ...
   }

ここで Visitor の導入となる。
まずはデザインパターンの教科書通りのインターフェイスを持つクラスを書いてみる。

.. code-block:: c++

   // p. 253 より
   // まず Visitor の抽象基底クラス
   class DocElementVisitor
   {
   public:
       virtual void VisitParagraph(Paragraph&) = 0;
       virtual void VisitRasterBitmap(RasterBitmap&) = 0;
       ...
   };
   
   // DocElement::Visit を宣言。
   
   class DocElement
   {
   public:
       virtual void Accept(DocElementVisitor&) = 0;
       ...
   };
   
   void Paragraph::Accept(DocElementVisitor& v)
   {
       v.VisitParagraph(*this);
   }
   // RasterBitmap も同様。
   
   // そして DocStats は DocElementVisitor を実装する。
   
   class DocStats : public DocElementVisitor
   {
       ... VisitParagraph や VisitRasterBitmap を実装 ...
   };

* ``VisitXXXX`` は ``XXXX`` の public な部分しかアクセスできない。
* 新たな操作を追加する場合、
  ``DocElementVisitor`` から新たなクラスを導出するだけでよい。
  p. 254 の ``IncrementFontSize`` の例を見るといい。

----

オーバーロードについて解説あり。

* 各 ``VisitXXXX`` の関数名は単に ``Visit`` とすることができる。
* ``DocElementVisitor::Visit(DocElement&)`` もアイディアとしてはアリ。

----

非循環式 Visitor という、魅惑的なタイトル。

* <``DocElementVisitor`` の ``VisitXxx メンバ関数名にクラス名が埋め込まれるため、
  ``DocElementVisitor`` のクラス定義をコンパイルする際には、
  ``DocElement`` 階層に存在する全ての具体的なクラスに関する知識（少なくとも名前）が必要になります> (p. 257)

* <循環依存は、保守上のボトルネックになる> (p. 257)

* ``DocElement`` 階層にサブクラスを追加するときに必要な作業を列挙している。
  <こういった作業は面倒くさい> (p. 258)

* Robert Martin (1996) 考案による dynamic_cast を用いた変形 Visitor パターン。

  * ``DocElementVisitor`` に ``VisitXxxx`` を宣言しない。
  * ``XxxxVisitor`` は ``DocElementVisitor`` を継承しないで、
    ``VisitXxxx`` を純粋仮想関数として宣言する。
  
  * ``DocElement`` のサブクラス ``Xxxx::Accept`` 関数にて、
    引数の ``DocElementVisitor`` を ``XxxxVisitor`` に dynamic_cast するテストを加える。
    
    .. code-block:: c++
    
       // p. 259 より引用
       void Paragraph::Accept(DocElementVisitor& v)
       {
           if(ParagraphVisitor* p = dynamic_cast<ParagraphVisitor*>(&v))
           {
               p->VisitParagraph(*this);
           }
           ...
       }

  * 具体的な Visitor クラスの定義は、例えば次のようになる。
  
    .. code-block:: c++
    
       // p. 260 より引用。
       class DocStats :
           public DocElementVisitor,
           public ParagraphVisitor,
           public RasterBitmapVisitor
       {
           ...

           // VisitXxxx をこのクラスで実装する。
           void VisitParagraph(Paragraph&);
           void VisitRasterBitmap(RasterBitmap&);
       };

* 非循環式 Visitor パターンは循環依存をなくす代わりに、
  <``DocElement`` をルートに持つ被訪問階層のクラス群と、
  具体的な被訪問クラス毎に対応する訪問クラス ``XxxVisitor`` 群という
  2 つの並列したクラス群を保守しなければならなくなります> (p. 261)

* <高名な GoF の Ralph Gamma ですら、
  Visitor がボトム 10 パターンの中のかなり下の方に位置付けられると言っているのです (Vlissides 1999)>
  (p. 262)

----

ここでジェネリック化の議論に入る。

* <できるだけ多くのコードをライブラリに収納するようにするのです> (p. 262)
* 最初に非循環式 Visitor を実装し、その後 <標準とも言える> (p. 262) GoF 版 Visitor を実装する流れ。

非循環式。

* ``BaseVisitor`` - 先の例の ``DocElementVisitor`` と同じ。
* ``Visitor`` - ``XxxxVisitor`` 用。クラステンプレートとして宣言。

  .. code-block:: c++
  
     // p. 263
     template <class T, typename R = void>
     class Visitor
     {
     public:
         typedef R ReturnType;
         virtual ReturnType Visit(T&) = 0;
     };

* ``BaseVisitable`` - ``Accept`` するクラスの基底クラスとして利用するためのクラステンプレート。

  * ``Visitor`` 同様に ``Accept`` の戻り値がテンプレート引数になる。
  * ユーザーが ``Accept`` を実装をするための補助的なマクロ ``DEFINE_VISITABLE()`` と補助関数
    ``AcceptImpl(T&, BaseVisitor&)`` を用意する。
    
    * <場合によっては ``DEFINE_VISITABLE()`` マクロを用いるのではなく、
      自分で ``Accept`` を実装する必要が出てくる> (p. 268) が、問題ない。

----

続いて循環式。dynamic_cast を用いないために高速に動作する。

* ``CyclicVisitor`` ではタイプリストを利用する。

  * ``GenScatterHierarchy<TList, 略>`` から継承する。
  * ``Visit`` メンバ関数テンプレートは ``Visitor`` を用いて実装する。
    ``CyclicVisitor`` は ``TList`` 中の各型 ``T`` について、
    クラス ``Visitor<T>`` の派生クラスであるからできる芸当。

* マクロ ``DEFINE_CYCLIC_VISITABLE()`` を提供する。

循環式の場合、ユーザーコードが圧倒的に少なくて済むようだ。

.. code-block:: c++

   // pp. 270-271 より引用
   typedef CyclicVisitor
   <
       void, // 戻り値
       TYPELIST_3(DocElement, Paragraph, RasterBitmap)
   >
   MyVisitor;
   
   class DocElement
   {
   public:
       virtual void Visit(MyVisitor&) = 0;
   };
   
   class Paragraph : public DocElement
   {
   public:
       DEFINE_CYCLIC_VISITABLE(MyVisitor);
   };

第 11 章 マルチメソッド
======================================================================
TBW
