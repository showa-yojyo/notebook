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
TBW
