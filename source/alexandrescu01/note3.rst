======================================================================
Modern C++ Design 読書ノート 3/3
======================================================================

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
       // ... VisitParagraph や VisitRasterBitmap を実装 ...
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

* <``DocElementVisitor`` の ``VisitXxx`` メンバ関数名にクラス名が埋め込まれるため、
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
* マルチメソッドという用語は CLOS から借用した (p. 277)

----

C++ におけるポリモフィズムとは何かをまず考える。
関数オーバーロード、関数テンプレートはともに静的なディスパッチメカニズムであり、
仮想メンバ関数呼び出しは動的なディスパッチメカニズムであるとみなせる。

* <``obj.Fun(引数群)`` という呼び出しシンタックスでは、
  引数群よりも ``obj`` に優先的な役割が与えられているのです> (p. 278)

* マルチメソッド、多重ディスパッチとは 
  <関数呼び出しに用いられているオブジェクト群の動的な型に依存して、
  異なった関数にディスパッチするようなメカニズム> (p. 278) のこと。

----

マルチメソッドの必要性について論じる。
ここでは ``Shape`` （のサブクラス）オブジェクト同士の交差部分処理という、
C++ プログラム開発経験者ならまず膝を叩く例が挙げられている。

手許に ``Shape`` への異なるポインターが 2 つあるとして、
それをどのオーバーロードに適用するの？ という問題だ。

----

最初に一番愚直と思われる方法、力任せに dynamic_cast テストをして、
動的な型に見合うオーバーロード関数に引き渡すコードを示している。

.. code-block:: c++

   // pp. 280-281 より一部抜粋（一部だけで雰囲気が思い出せるから）

   void DoHatchArea1(Rectangle&, Rectangle&);
   void DoHatchArea2(Rectangle&, Ellipse&);
   void DoHatchArea3(Rectangle&, Poly&);
   ...

   void DoubleDispatch(Shape& lhs, Shape& rhs)
   {
       if(Rectangle* p1 = dynamic_cast<Rectangle*>(&lhs))
       {
           if(Rectangle* p2 = dynamic_cast<Rectangle*>(&rhs))
               DoHatchArea1(*p1, *p2);
           else if(Ellipse* p2 = dynamic_cast<Ellipse*>(&rhs))
               DoHatchArea2(*p1, *p2);
           else if
               ...
       }
       else if
           ...
   }

* 問題点は明らか。

  * <この実装は、階層中に存在する全クラスを知っていなければならないのです> (p. 281)
  * <``if`` ステートメントの順序が処理に影響を与えてしまう> (p. 281) - 
    <最も下位にあるクラスが最初に判定されるよう、
    ``if`` の判定を「ソートする」> (p. 282) ようでなければ問題が出る。

----

ここから本書らしいアプローチが始まる。
先程の ``DoubleDispatch`` 相当のコードを、クラステンプレート ``StaticDispatcher`` と
クラス ``HatchingExecutor`` に分割して、次のような構造で表現する。

.. code-block:: c++

   // pp. 283-286 から断続的に引用。

   template< /* 略 */ > // 本を読んで。
   class StaticDispatcher
   {
       typedef typename TypesLhs::Head Head;
       typedef typename TypesLhs::Tail Tail;
   public:
       static ResultType Go(BaseLhs& lhs, BaseRhs& rhs, Executor exec)
       {
           if(Head* p1 = dynamic_cast<Head*>(&lhs))
           {
               return StaticDispatcher< NullType, /* 略 */ >::DispatchRhs(*p1, rhs, exec);
           }
           else
           {
               return StaticDispatcher< Tail, /* 略 */ >::Go(/* 略 */);
           }
       }

       template <class SomeLhs>
       static ResultType DispatchRhs(SomeLhs& lhs, BaseRhs& rhs, Executor exec)
       {
           // ここで Head, Tail に対する typedef を「上書き」する。

           if(Head* p2 = dynamic_cast<Head*>(&rhs))
           {
               return exec.Fire(lhs, *p2)
           }
           else
           {
               return StaticDispatcher<NullType, Tail, /* 略 */>::DispatchRhs(/* 略 */);
           }
       }
   };

   // TODO: StaticDispatcher の部分特殊化 1: TypeLhs = NullType で
   // ダミーの static メソッド Go を実装する。

   // TODO: StaticDispatcher の部分特殊化 2: TypeRhs = NullType で
   // ダミーの static メソッド DispatchRhs を実装する。

   class HatchingExecutor
   {
   public:
       void Fire(Rectangle&, Rectangle&);
       void Fire(Rectangle&, Ellipse&);
       ...

       void OnError(Shape&, Shape&);
   };

* ``Go`` から ``Go`` を呼び出す様子は再帰呼び出しに見えるかもしれないが、
  ``StaticDispatcher`` の別な実体化の同名メソッドを呼び出している。
  ``DispatchRhs`` も同様。

* <結果的に、 ``StaticDispatcher`` は、
  2 つのタイプリストと特定のコードから指数に比例した分量のコードを生成するわけです。
  （略）つまり、大きなコードによってコンパイル時間、プログラム・サイズ、
  実行時間の全てに打撃が与えられるのです> (p. 284)

* <``StaticDispatcher`` は境界条件が発生した場合、
  元々の（キャストしない） ``lhs`` と ``rhs`` を用いて単に
  ``Executor::OnError`` を呼び出します> (p. 286)

.. code-block:: c++

   // p. 286 より。
   typedef StaticDispatcher<HatchingExecutor, Shape,
       TYPELIST_3(Rectangle, Ellipse, Poly)> Dispatcher;

   Shape* p1 = ...;
   Shape* p2 = ...;
   HatchingExecutor exec;
   Dispatcher::Go(*p1, *p2, exec);

* タイプリストに記述するクラスの順序に注意。先程と同様の注意が要る。
  <継承階層で最も下位にあるものをタイプリストの先頭に持ってくることです> (p. 287)

----

次に引数の順序を意識せずに済むように改造していく。対称型マルチメソッド。
``BaseLhs`` と ``BaseRhs`` が同一型かつ
``TypesLhs`` と ``TypesRhs`` が同一型の場合に意味がある。

* <理想的には、追加の ``bool`` テンプレート・パラメータを ``StaticDispatcher`` に引き渡して、
  対称性が選択できるようにするべきでしょう> (p. 289)

  * ``StaticDispatcher`` に ``bool symmetric`` テンプレート引数を追加する。
  * クラス内の private 部分にクラステンプレート ``InvocationTraits`` を定義する。
    これは static メンバー関数 ``DoDispatch`` だけを含む構造体。

    ``DoDispatch`` の内容は単に ``exec.Fire(lhs, rhs);`` のみ。

    * ``InvocationTraits`` の部分特殊化版を定義し、そちらの
      ``DoDispatch`` の内容は ``exec.Fire(rhs, lhs);`` とする。

  * ``StaticDispatcher::DispatchRhs`` の定義で、if ブロック内をこのようにする。

    .. code-block:: c++

       // p. 291 より引用
       enum { swapArgs = symmetric &&
           IndexOf<Head, TypeRhs>::result < IndexOf<BaseLhs, TypesLhs>::result };
       typedef InvocationTraits<swapArgs, BaseLhs, Head>
           CallTraits;
       return CallTraits::DoDispatch(lhs, *p2);

----

型リストから型を探索する効率を対数時間に持っていこうとするのか。

* ``std::type_info::before`` によって <プログラム中における全ての型に対する順序関係が提供されるのです> (p. 291)
* 第 2 章で紹介されたラッパークラス ``TypeInfo`` を利用する。
  <``TypeInfo`` は、値のセマンティックスと演算子 ``operator<`` を提供しています。
  このため、標準コンテナに ``TypeInfo`` オブジェクトを格納することができるのです> (p. 292)

* <特に、ソート済みベクタと二分探索アルゴリズムを組み合わせれば、
  連想コンテナよりも空間的および時間的に優れたものとなる場合もあるのです。
  これは、挿入頻度よりもアクセス頻度の方が多い場合に起こり得ます> (p. 292)

  つまり、コンテナ内容がある時点から固定されるような場合は連想コンテナを採用しないように、か。

* ただし、便宜的に両者のデータ構造を共に「マップ」と呼ぶことにする。(p. 293)

* ``BasicDispatcher``

  * 最終的なディスパッチ先の関数の引数 ``(lhs, rhs)`` ペアの型を ``std::pair<TypeInfo, TypeInfo>`` で表現する。
  * 上記のペア型をキー型とし、
    ``ResultType (*)(BaseLhs&, BaseRhs&)`` 型の関数ポインタを値型とするマップを定義する。
  * そのマップオブジェクトをメンバーデータに持つ。

  * テンプレートメンバー関数 ``Add`` を定義し、マップに関数ポインタを動的に追加できるようにする。
  * ``Go`` は次のようになる。

    .. code-block:: c++

       ResultType Go(BaseLhs& lhs, BaseRhs& rhs)
       {
           MapType::iterator i = callbackMap_.find(
               KeyType(typeid(lhs), typeid(rhs));
           if(i == callbackMap_.end())
           {
               // ... 例外送出
           }
           return (i->second)(lhs, rhs);
       }

  * <継承とともに用いると正しく動作しません> (p. 294)
  * <``BasicDispatcher`` に対して、全てのペアを注意深く登録していかなければならないのです> (p. 295)

----

.. warning::

   次に ``BasicDispatcher`` を利用して ``FnDispatcher`` を定義するのだが、
   もうついていけないのでスキップ。

   ``Trampoline`` という面白い技法を利用してディスパッチを実現する。

----

* <値のセマンティックスは実行時のポリモフィズムとうまく調和できない> (p. 299)

----

static_cast or dynamic_cast という問題。
これまでは dynamic_cast 一丁で押し通してきた理由を解説。

* 仮想継承を伴なうダイアモンド型クラス階層が対象となるとき、
  <仮想基底オブジェクトから導出した型へは static_cast することができない> (p. 302)
* 仮想継承を伴わないダイアモンド型クラス階層が対象となるとき、
  基底クラスが曖昧になるケースがある。

----

<多重ディスパッチと C++ において、特にいやらしかった問題は、
可変引数関数を表現する統一した方法が存在しないということだったのです> (p. 312)

付録 A 最小限のマルチスレッド・ライブラリ
======================================================================
C++ に関する書籍は、マルチスレッドをテーマにした文章が付録になる傾向がある。
本書もその例に漏れない。

* <ユーザは砂時計のカーソルが表示されることを望んでいないため、
  プログラマはマルチスレッド・プログラムを記述しなければならないのです> (p. 317)

* <ライブラリもスレッドを考慮する必要があります。
  こういった機能は、ライブラリが自身のスレッドを用いていない場合であっても、
  組み込んでおかなければならないのです> (p. 317)

----

* <マルチスレッドがシングルプロセッサ・マシンでも必要となる理由は、
  リソースを効果的に使用できるという点があるからです> (p. 318)

* <これらは物理的に独立した機器であるため、同時にリソースを使用することができるのです> (p. 318)

* <非同期実行は、マルチスレッドの実行と比較すると状態遷移の多いプログラムになるという欠点があります> (p. 318)

* <アトミックな操作だと思っていたものがそうではなくなってしまう> (p. 318)
* <マルチスレッドのプログラムは、リソースの共有に大きな問題を抱えている> (p. 319)
* マルチスレッドプログラミングにおける重要な技法のひとつに、同期化オブジェクトがある。

----

``++x`` というステートメントに関する考察を始める。

* こういう (read-modify-write) 操作を RMW 操作と呼ぶ (p. 320)
* マルチプロセッサ環境では、あるプロセッサが変数を更新している間にも、
  別のプロセッサがメモリにアクセスできる。

* <どちらのプロセッサ（スレッド）も、インクリメントができなかったことを検出できない> (p. 320)
* 通常、アトミックなインクリメント・デクリメント操作は OS が C 関数の形式でサポートしている。

ライブラリでアトミック演算をまとめるようだ。

.. code-block:: c++

   template <typename T>
   class SomeThreadingModel
   {
   public:
       typedef int IntType; // int にはプラットフォーム規定整数型名がくる。

       static IntType AtomicAdd(volatile IntType& lval, IntType val);
       ...
   };

* <コピー操作でさえも非アトミックな場合があるため、
  ``AtomicAssign`` 関数も 2 つ必要となるわけです> (p. 321)

----

ミューテックスの話題。

* <マルチスレッド環境下におけるオペレーティング・システムのスケジューラは、
  ある種の同期化オブジェクトを提供しなければならないということが、
  Edgar Dijkstra によって証明されています。
  マルチスレッド・アプリケーションを正しく記述するためには、
  こういったものが必要不可欠なのです> (p. 321)

  とても重要。丸暗記しよう。

* <ミューテックス (mutex) とは、相互排他 (Mutual Exclusive) の略であり、
  同期化用のプリミティブ・オブジェクトの機能を解説するための用語です> (p. 321)

* <たった 1 つのスレッドのみがミューテックスを獲得できるのです> (p. 322)

  獲得は ``Acquire`` で、解放は ``Release`` か。

* コード中の ``mtx.Acquire()`` 呼び出しと ``mtx.Release()`` 呼び出しで囲まれた部分が、
  ``mtx`` オブジェクトに関してアトミックとなる。

  これを利用して <スレッド間で共有させたいリソース毎にミューテックス・オブジェクトを
  1 つ割り当てることになります> (p. 322)

* マルチスレッドプログラミングの教科書にありがちな
  「銀行口座クラスの預金引き出しメソッド実装例」コードあり。

  * <``Lock`` オブジェクトをスタック上に割り当てておけば、例外発生の有無とは関係なく、
    ``Acquire`` と ``Release`` のペアが正しく実行される> (p. 323)

----

* <オブジェクト指向プログラムでは、リソースはオブジェクトになります> (p. 323)
* オブジェクト・レベルのロックと、クラス・レベルのロックがある。

.. code-block:: c++

   template <typename Host>
   class ObjectLevelLockable
   {
   public:
       class Lock
       {
       public:
           Lock(Host&);
           ...
       };
   };

   class BankAccount : public ObjectLevelLockable<BankAccount>
   {
       ...

       void Deposite(/* 略 */)
       {
           Lock(*this);
           // ... 入金トランザクション
       }
       ...
   };

----

<``volatile`` の指定によってコンパイラはある種の最適化を抑止するため、
シングルスレッド・モデルでは指定するべきではないのです> (p. 325)

----

<ポータブルなマルチスレッド・ライブラリとして ACE
(Adaptive Communication Environment) を調査することをお勧めします (Schmidt 2000)> (p. 326)

感想
======================================================================

* 一周読むのに鉛筆片手に 10 時間、
  このノートをとるのに 13 時間近く要した。
  これまで読んできた C++ 関連書籍中「初心者にお勧めできない」度ナンバーワンは間違いなく本書だ。

* コーディング・コンパイル・動作確認を一切しないという不埒な読書姿勢。
* 理解度もかなり低いだろう。
