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
