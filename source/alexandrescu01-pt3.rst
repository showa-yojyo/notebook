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

