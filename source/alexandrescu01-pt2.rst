======================================================================
Modern C++ Design 読書ノート パート 2
======================================================================

読書ノート :doc:`alexandrescu01-pt1` からの続き。

:著者: Andrey Alexandrescu
:訳者: 村上雅章
:出版社: ピアソン・エデュケーション
:ISBN: 4-89471-435-3

.. contents:: ノート目次

第 5 章 汎用のファンクタ
======================================================================

* 「値のセマンティックスを伴ったオブジェクト」という言い回しが頻出する。
  これはオブジェクトがコピー、代入、値による引渡しが完全にサポートされていることを意味する。

* <関数へのポインタをかなり現代風にアレンジしたもの> (p. 105)
* <状態を保存でき、メンバ関数を起動できる> (p. 105) ので、単なる関数ポインタより有利。

----

Command デザインパターンの解説セクション。

* <作業がどのようにして行われるのかを起動側は気にしなくても良い> (p. 106)
* <呼び出しを無期限に延期できる> (p. 107)
* <Command パターンでは、処理を実行するために必要な環境を整えるタイミングが、
  処理を実行するタイミングと異なっています> (p. 107)

* <Command パターンの実装を手作業で行う場合、スケーラビリティに劣ることがあります。
  つまり、小さな機能を持った具体的な Command クラスを数多く記述しなければならず
  （それぞれが、 ``CmdAddUser``, ``CmdDeleteUser``, ``CmdModifyUser`` といった
  アプリケーション中の単一動作を表します）、
  それぞれに特定オブジェクトに対する特定のメンバ関数を単に呼び出すだけの
  ``Execute`` メンバ関数を保持させなければならないのです> (p. 108)
  
  →心当たりありまくり。

----

* <Command パターンにおける ``Command::Execute`` は、C++ におけるユーザ定義演算子
  ``operator()`` となるべきです> (p. 111)
  
  →呼び出しシンタックスを ``operator()`` に統一することで、
  ``Functor`` が他の ``Functor`` を保持できるようになるから。

* クラステンプレート ``Functor`` を、
  戻り値の型が ``ResultType`` で、パラメータリストをタイプリスト ``TList`` で表現する。

* ``Functor`` の定義は一回。Pimpl パターンにより実装を別のクラステンプレート
  ``FunctorImpl`` で行う。
  
* ``FunctorImpl`` を部分特殊化をしまくって、
  引数リストのパラメータ数が十分大きくても対応できるようにしておく。
  
  .. code-block:: c++
  
     // p. 114 より引用
     template <typename R, class TList>
     class FunctorImpl;
     
     template <typename R>
     class FunctorImpl<R, NullType>
     {
     public:
         virtual R operator()() = 0;
         virtual FunctorImpl* Clone() const = 0;
         virtual ~FunctorImpl(){}
     };
     
     template <typename R, typename P1>
     class FunctorImpl<R, TYPELIST_1(P1)>
     {
     public:
         virtual R operator()(P1) = 0;
         virtual FunctorImpl* Clone() const = 0;
         virtual ~FunctorImpl(){}
     };
     
     ...

----

``Functor::operator()`` は ``FunctorImpl::operator()`` へ転送を行う必要がある。

* <``Functor`` の定義内に任意のパラメータ数で全ての ``operator()`` を定義することができる> (p. 115)

  * 第 3 章で紹介した ``TypeAtNonStrict<...>::Result`` を十分な個数だけ ``typedef`` する。

    ``TypeAtNonStrict`` は ``TypeAt`` のゆるゆるバージョン。

  * 力作業で ``operator()`` のオーバーロードをその個数分だけ実装する。

----

``Functor`` オブジェクトの構築に関する考察。

* ``FunctorImpl`` のサブクラス ``FunctorHandler`` を定義して、
* ``Functor`` のコンストラクターで Pimpl メンバーデータにセットする。

----

「メンバ関数へのポインタ」に関する考察。

* C++ では全てのオブジェクトには型があるが、
  ``operator.*`` と ``operator->*`` の結果は何か違うものだ。

----

バインダーに関する考察。ちょっと読みにくいのと、
``BinderFirst`` しか議論していないのが惜しい。
任意の位置のパラメータにバインドするバインダーの話を振らないと。

----

この章の残りの話題は、

* Command パターンの話をしていたので、マクロやらアンドゥ・リドゥの話。
* 「参照の参照」問題回避のため、traits を ``Functor::operator()`` にクッションする。

  .. code-block:: c++

     // 例えば型 Parm1 が組み込み型でない場合、
     // p1 の型は Parm1& となる。
     // const が付いていたら const Parm1& となる。
     R operator()(
         typename TypeTraits<Parm1>::ParameterType p1,
         typename TypeTraits<Parm2>::ParameterType p2)
     {
         return (*spImpl_)(p1, p2);
     }

* <典型的な 32 ビットのシステムの場合、（略）
  メンバ関数へのポインタは 16 バイト> (p. 132) となる。

など。

第 6 章 Singleton の実装
======================================================================
<Singleton デザイン・パターンの実装で「正解」というものは存在しません。
（略）扱っている問題次第で最適なものとなるのです> (p. 137)

----

* <static データ + static 関数 != Singleton> (p. 138)
* <static な関数は virtual にできない> (p. 138)
* <Singleton の実装では、2 番目のインスタンスを生成しないようにしながら、
  オブジェクトの生成と唯一性の管理に集中することになる> (p. 139)

----

* デフォルト・コンストラクター、コピー・コンストラクター、代入演算子は
  private に宣言することは承知しているが、これを読むまでデストラクターも
  private にするのを忘れていた。

----

基本を説明してすぐに Singleton オブジェクトの破棄に関する議論が始まる。
これ以降の議論は、デザインパターンの本ではまずお目にかかったことのないものだ。

* <リソース・リークを避ける唯一の正しい手段とは、
  アプリケーションの終了時に Singleton オブジェクトを削除することです。
  問題は、その破棄後に、該当 Singleton に対するアクセスが発生しないようなタイミングを注意深く設定しなければならない点です> (p. 142)

* 次のタイプの実装を Meyers の Singleton と呼ぶことにする。

  .. code-block:: c++
  
     Singleton& Singleton::Instance()
     {
         static Singleton obj;
         return obj;
     }
  
  <Meyers の Singleton は、アプリケーションの終了処理における最も簡単な
  Singleton の破棄手段を提供しています> (p. 143)

----

死んだ参照の議論。
``Keyboard``, ``Display``, ``Log`` という 3 クラスがそれぞれ Singleton な場合で、
``Keyboard`` と ``Display`` のエラーが ``Log`` に報告するような状況を考察する。
この問題を KDL 問題と呼ぶことにする。

* <この 3 つの Singleton を Meyers の Singleton で実装した場合、
  プログラムは正しく動作しないのです> (p. 144)

* <妥当な方法は、Singleton に死んだ参照の検出をさせることです> (p. 144)

  ``Singleton::Instance`` で検出させることで、何らかのエラーハンドリングをする。

----

Phoenix Singleton なる概念を導入する。
デストラクトされたオブジェクトのあったメモリに、
再度オブジェクトをコンストラクトするというものだ。

* ``Singleton::OnDeadReference`` で placement new の機能を利用し、
  ``pInstance_`` に ``Singleton`` オブジェクトを構築する。

* ``atexit`` に破棄関数 ``KillPhoenixSingleton`` を登録する。
  ``KillPhoenixSingleton`` では ``pInstance_`` に対して明示的にデストラクターを呼び出す。
  <``new`` を使用すると（略）コンパイラによる自動破棄が行われなくなるためです> (p. 147)

* ちなみに ``atexit`` にはキズがある。
  <規格では、 ``atexit`` を用いた関数の登録中に他の
  ``atexit`` による登録が発生した場合の定義が行われていない> (p. 147)

----

次の議論は、「Singleton に寿命レベルを導入する」というもの。

* 前節の戦略だと、状態を保持するような Singleton では復活し切れないことは明白。
* KDL 問題は「K, D よりも L のほうが長生きである」ことが表現できれば問題解決だ。

<ここで出てくる寿命の制御というコンセプトは、
Singleton のコンセプトとは独立したものです。
オブジェクトの寿命が長いほど、破棄が後にまわされるのです> (p. 149)

* ``SetLongevity`` 関数の「仕様」は p. 151 のリスト参照。
  ``atexit`` の呼び出しを含むのがポイント。

----

.. warning::

   寿命を指定する Singleton の実装法について数ページにわたる説明があるが、
   読むのが面倒になったのでスキップ。

----

マルチスレッド対応。

<共有されるグローバル・リソースというものは全て、競合条件とスレッドに関連する問題の元凶となり得るのです> (p. 155)

* 今では有名になった手法だが、Doug Schdmit と Tim Harrison が発案した (1996)
  Double-Checked Locking パターンを紹介している。

  .. code-block:: c++
  
     // p. 157 より引用
     Singleton& Singleton::Instance()
     {
         if(!pInstance_)
         {
             Guard myGuard(lock_);
             if(!pInstance_)
             {
                 pInstance_ = new Singleton;
             }
         }
         return *pInstance_;
     }
  
* ただし、ある種のマルチプロセッサではこのパターンが使えない。
  使えるか否かを決定するには <コンパイラのドキュメントを熟読しなければならない> (p. 157)

* <少なくとも、 ``pInstance_`` の次に ``volatile`` 修飾子を置くことです> (p. 157)

----

これまでの分析を総合する。

* ``SingletonHolder`` を 3 つのポリシーに分解する。

  * ``Creator``: ``pInstance_`` の初期化ポリシー。
  * ``Lifetime``: 「通常」「復活アリ」「寿命制御」「無限」の 4 パターンを提供している。
  * ``Threading``: シングルスレッド or マルチスレッド。

  .. code-block:: c++
  
     // p. 160 より引用
     template <
        class T,
        template <class> class CreationPolicy = CreateUsingNew,
        template <class> class LifetimePolicy = DefaultLifetime,
        template <class> class ThreadingModel = SingleThreaded
     >
     class SingletonHolder;


* <インスタンスの型は ``T*`` ではなく ``ThreadingModel<T>::VolatileType*`` です> (p. 160)
  
  →マルチスレッド環境では仇になる、コンパイラによるある種の最適化処理を抑止するため。

* <``SingletonHolder`` が ``DestroySingleton`` を呼び出すことはありません> (p. 161)

* KDL 問題の解として、仮コードを p. 164 に掲載している。

第 7 章 スマート・ポインタ
======================================================================
TBW
