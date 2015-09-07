======================================================================
行列
======================================================================
モジュール ``sympy.matrices`` に関するメモを記す。
ここにある機能は、行列を処理するものと、行列に関する数式を処理するものとに分類できる。

.. contents:: ノート目次

.. note::

   本文中のすべての IPython セッション中のサンプルコードで、
   以下のインポートおよび出力書式設定が済んでいるものとする。

   .. code-block:: python3

      from sympy.matrices import *
      init_printing(use_unicode=False, pretty_print=False)

クラス図
======================================================================
行列関連の単純なクラス図を示す。

行列を表現するクラス
----------------------------------------------------------------------
行列オブジェクトの基本単位を表現するためのクラスの論理的な継承関係は次のようになっている。

.. code-block:: text

   MatrixBase
       MutableDenseMatrix
       ImmutableDenseMatrix

       ImmutableSparseMatrix
       MutableSparseMatrix

* モジュール ``__init__`` で別名が付けられる等されているため、
  クラス名中の ``Mutable`` と ``Dense`` の部分は省略できる。
  例を挙げると、単に ``Matrix`` と書いたとしても、
  実際はクラス ``MutableDenseMatrix`` である。

* Mutable と Immutable の違いは Python のプログラマーが思い浮かべるものと同じ。
* Dense と Sparse の違いは疎行列性を意味する。
* ``MatrixBase`` のスーパークラスは Python のクラス ``object`` である。

行列を構成要素とする数式のためのクラス
----------------------------------------------------------------------
行列オブジェクトを各種演算で構成した数式を表現するためのクラスが多数存在する。
そのクラス群はモジュール ``matrices.expressions`` 以下で定義されており、
それらの継承関係は次のようになっている。
全サブクラスを書き出す必要はまったくないが、何かのために記す。

継承ツリーの右側に関連するフリー関数、行列クラスのメソッド、メモを併記する。

.. code-block:: text

   MatrixExpr
       MatrixSymbol                    シンボル（記号）としての行列

       Identity
       ZeroMatrix

       MatAdd                          加法
       MatMul                          乗法
       MatPow                          M ** n
           Inverse                     M ** -1, M.inverse(), M.I

       Transpose                       transpose(M), M.T
       Adjoint                         adjoint(M)

       Trace                           trace(M)
       DiagonalMatrix
       DiagonalOf

       Determinant                     det(M)

       DFT                             離散 Fourier 変換の行列表現
           IDFT                        逆離散 Fourier 変換の行列表現

       MatrixSlice                     M[start:stop:step, ...]

       HadamardProduct                 hadamard_product(M, ...)

       FunctionMatrix                  ラムダ式による行列生成

       Factorization
           LofLU                       lu(M)
               LofCholesky
           UofLU                       lu(M)
               UofCholesky

           QofQR                       qr(M)
           RofQR                       qr(M)

           EigenVectors                eig(M)
           EigenValues                 eig(M)

           UofSVD                      svd(M)
           SofSVD                      svd(M)
           VofSVD                      svd(M)

       BlockMatrix                     blockcut(M, rsize, csize)
           BlockDiagMatrix

* クラス ``MatrixExpr`` のスーパークラスは SymPy のクラス ``Basic`` である。

色々な行列の生成方法
======================================================================
まず、行列以外の要素から行列オブジェクトを直接生成する方法を記す。

他のライブラリーの類似機能を利用した経験から言えば、
クラス ``Matrix`` のコンストラクターを直接する場合は、
おそらく行列の各成分を細かく指示する場合に限られると思われる。

``Matrix(([[1,0,0], [0,0,0]])``
  入れ子の ``list`` は行 (row) を上から下に並べたものとして扱われる。

``Matrix([[1, 2, 3]])``
  上の特別な場合だが、入れ子の中身が ``list`` ひとつの場合は行ベクトルと等価な行列となる。

``Matrix([1, 2, 3])``
  入れ子になっていない場合は列ベクトルと等価な行列となる。

``Matrix(2, 3, [1, 2, 3, 4, 5, 6])``
  行列の寸法と成分すべてを行を先に埋める順で指示して生成する。

  * 寸法は行数、列数の順。タテ、ヨコ。

``Matrix(3, 4, lambda i,j: 1 - (i+j) % 2)``
  行列を寸法と添字を引数に取る関数とで生成する。

成分に特徴のある行列を生成する場合は、それに適する関数、メソッドが用意されているので利用する。

* 関数 ``eyes`` と ``zeros`` は NumPy_ のそれと同様。
* 関数 ``diag`` は対角行列の生成であるが、より小さい行列を主対角線上に配列するようなこともできる。

基本的な操作
======================================================================
* 要素アクセス

  * 行列の要素ひとつにアクセスするには、適切な添え字を用いて ``M[i]`` や ``M[i, j]`` とする。
    添字がひとつの場合は、要素を row-major でアクセスする。

  * NumPy の ``array`` と同様にスライスもサポートしている。

    * 記法も同様に ``M[start:stop:step]`` のようにする。
    * 右辺値としてスライスする場合は、元のオブジェクトの一部のコピーとして機能する。
      一方、左辺値としてスライスする場合は、元のオブジェクトのビューのように機能する。

* 行列代数

  * 少なくとも同型の行列同士では加法と乗法が成立する。
    これは標準的な算術演算子 ``+``, ``-``, ``*`` で表現する。

* ベクトル演算

  * 行か列のどちらかのサイズを 1 にすれば ``Matrix`` を列ベクトル、行ベクトルとして扱える。
    例えばメソッド ``dot`` と ``cross`` が利用可能になる。

    * 一応断っておくと ``dot`` はサイズが合えば行列とベクトルとに作用できる。
    * ただし ``cross`` のほうは本当にベクトル限定。しかも 3 次元のみ。

* 各要素に関数を適用するには、メソッド ``applyfunc`` を用いる。

線形代数的操作
======================================================================
メソッド ``det(method="bareis")``
  行列式を求める。

  * キーワード引数 ``method`` で行列式を計算するアルゴリズムを選択できる。
    おそらく利用しない。

メソッド ``inv(method=None, **kwargs)``
  逆行列を求める。

  * キーワード引数 ``method`` で行列式を計算するアルゴリズムを選択できる。

    * ``'GE'``: Gauss の消去法。デフォルトのアルゴリズム。
    * ``'LU'``: LU 分解。
    * ``'ADJ'``: 余因子行列と行列式を用いて逆行列を得る。

メソッド ``QRdecomposition()``
  行列を QR 分解する。

メソッド ``LUsolve(self, rhs, iszerofunc=_iszero)``
  一次連立方程式 :math:`A \mathbf{x} = \mathbf{b}` を解く。

関数 ``GramSchmidt(vlist, orthonormal=False)``
  ベクトルの集合を基に直交基底を得る。

  * 引数 ``vlist`` は同じサイズのベクトルのコレクション。
    断りがないが、線形独立である必要があるはずだ。

  * キーワード引数 ``orthonormal`` で得られるベクトルの長さを 1 にするかどうかを指定する。

  * 実装を見ると、メソッド ``project`` を利用していることがわかる。

クラス ``MatrixBase``
======================================================================
このクラスにはメソッドが大量にある。要所に絞って記す。演算子は省略。

プロパティー
----------------------------------------------------------------------
プロパティーのほぼすべてを記す。
下の表のもの以外にも、例えば ``.rows`` のようにしてオブジェクトの属性を得ることができるものもあるようだが、
コードから拾えないので割愛した。

.. csv-table::
   :delim: :
   :header: プロパティー, 説明

   ``C``:要素ごとに複素共役をとった行列を返す。
   ``D``:Dirac 共役行列を返す。
   ``H``:Hermite 共役を返す。
   ``T``:転置行列を返す。
   ``is_hermitian``:Hermite 行列かどうかを返す。
   ``is_lower``:下三角行列かどうかを返す。
   ``is_lower_hessenberg``:下 Hessenberg 行列かどうかを返す。
   ``is_square``:正方行列かどうかを返す。
   ``is_upper``:上三角行列かどうかを返す。
   ``is_upper_hessenberg``:上 Hessenberg 行列かどうかを返す。
   ``is_zero``:零行列かどうかを返す。
   ``shape``:行列の寸法を返す。必ず (r, c) の型をとる。

* ``C`` はメソッド ``conjugate`` のエイリアス。

* ``D`` は結局はモジュール ``sympy.physics.matrices`` の機能を利用している。
  そのときにまた調べよう。

* ``H`` は ``T.C`` と同じ。

* ``T`` はメソッド ``transpose`` のエイリアス。

* 三角行列判定系のメソッドは for ループを二重にまわして、
  テストに必要な各成分を要素オブジェクトのプロパティー ``is_zero`` でゼロかどうかをテストしている。

  また、必ずしも正方行列でなくてよい。

要素の物理的な操作
----------------------------------------------------------------------
行や列のデータを物理的に操作するタイプのものを次の表に記す。

.. csv-table::
   :delim: :
   :header: シグニチャー, 説明

   ``hstack(*args)``:複数の行列を横に連結する。
   ``vstack(*args)``:複数の行列を縦に連結する。
   ``col_insert(pos, mti)``:行列に列を挿入する。
   ``row_insert(pos, mti)``:行列に行を挿入する。
   ``col_join(bott)``:行列同士を縦に連結する。
   ``row_join(rhs)``:行列同士を横に連結する。
   ``permuteBkwd(perm)``:行を指定の置換で入れ替える。
   ``permuteFwd(perm)``:行を指定の置換で入れ替える。

* どのメソッドも inplace な振る舞いをしない。
* ``hstack``, ``vstack`` はクラスメソッド。余談だが同名のものが NumPy にもある。
* 挿入系メソッドの引数 ``mti`` は ``shape`` の縦横の一致を問う。
* 置換系メソッドの核となるのはメソッド ``row_swap`` である。

部分空間
----------------------------------------------------------------------
部分空間に関するメソッドを下の表に示す。

.. csv-table::
   :delim: :
   :header: シグニチャー, 説明

   ``columnspace(simplify=False)``:列空間を返す。
   ``nullspace(simplify=False)``:零空間を返す。

どちらもメソッド ``rref`` が重要な働きをする。

乗法
----------------------------------------------------------------------
行列またはベクトルの乗算に関するメソッドを下の表に示す。

.. csv-table::
   :delim: :
   :header: シグニチャー, 説明

   ``cross(b)``:ベクトルのクロス積、ベクトル積を計算する。
   ``dot(b)``:ベクトルのドット積、スカラー積を計算する。
   ``multiply(b)``:行列の乗算を行う。
   ``multiply_elementwise(b)``:行列の成分ごとの乗算を行う。

* メソッド ``dot`` はベクトル同士だけではなく、
  サイズさえ合えば行列対ベクトルでもよい。

* メソッド ``multiply`` は演算子 ``*`` で実装されている。

* メソッド ``multiply_elementwise`` は関数 ``matrix_multiply_elementwise`` で実装されている。

ノルム
----------------------------------------------------------------------
ノルムに関係するメソッドを次に示す。

.. csv-table::
   :delim: :
   :header: シグニチャー, 説明

   ``norm(ord=None)``:行列またはベクトルのノルムを返す。
   ``normalized()``:正規化した行列またはノルムを返す。

* ノルムはデフォルトでは行列に対しては Frobenius ノルムを、
  ベクトルに関しては 2-ノルムをそれぞれ返す。

* ノルムの種類に関しては help を参照。いつも使うものは揃っている。

* メソッド ``normalized`` で用いられるノルムはデフォルトのノルム。

行列式
----------------------------------------------------------------------
行列式に関係するメソッドを次に示す。

.. csv-table::
   :delim: :
   :header: シグニチャー, 説明

   ``det(method='bareis')``:TBW
   ``det_bareis()``:TBW
   ``det_LU_decomposition()``:TBW

余因子
----------------------------------------------------------------------
余因子に関係するメソッドを次に示す。

.. csv-table::
   :delim: :
   :header: シグニチャー, 説明

   ``adjugate(...)``:TBW
   ``cofactor(i, j, ...)``:TBW
   ``cofactorMatrix(...)``:TBW
   ``minorEntry(i, j, ...)``:TBW
   ``minorMatrix(i, j)``:TBW

対角行列
----------------------------------------------------------------------
対角行列に関係するメソッドを次に示す。

.. csv-table::
   :delim: :
   :header: シグニチャー, 説明

   ``diagonalize(...)``:TBW
   ``is_diagonal()``:TBW

分解
----------------------------------------------------------------------
行列の分解 (decomposition, factorization) に関係するメソッドを次に示す。

.. csv-table::
   :delim: :
   :header: シグニチャー, 説明

   ``cholesky()``:TBW
   ``LDLdecomposition()``:TBW
   ``LUdecomposition(...)``:TBW
   ``LUdecomposition_Simple(...)``:TBW
   ``LUdecompositionFF(...)``:TBW
   ``QRdecomposition()``:TBW

ソルバー
----------------------------------------------------------------------
線形連立方程式を解くことに関係するメソッドを次に示す。

.. csv-table::
   :delim: :
   :header: シグニチャー, 説明

   ``cholesky_solve(rhs)``:TBW
   ``diagonal_solve(rhs)``:TBW
   ``gauss_jordan_solve(b, freevar=False)``:TBW
   ``LDLsolve(rhs)``:TBW
   ``LUsolve(rhs, ...)``:TBW
   ``QRsolve(b)``:TBW
   ``pinv_solve(B, arbitrary_matrix=None)``:TBW
   ``lower_triangular_solve(rhs)``:TBW
   ``upper_triangular_solve(rhs)``:TBW

逆行列
----------------------------------------------------------------------
逆行列に関係するメソッドを次に示す。

.. csv-table::
   :delim: :
   :header: シグニチャー, 説明

   ``inv(method=None, **kwargs)``:TBW
   ``inv_mod(m)``:TBW
   ``pinv()``:TBW
   ``pinv_solve(B, arbitrary_matrix=None)``:TBW

Berkowitz のアルゴリズム
----------------------------------------------------------------------
Berkowitz のアルゴリズムと、それに関係するメソッドを次に示す。

.. csv-table::
   :delim: :
   :header: シグニチャー, 説明

   ``berkowitz()``:TBW
   ``berkowitz_det()``:TBW
   ``berkowitz_minors()``:TBW
   ``berkowitz_charpoly(x, simplify)``:TBW
   ``berkowitz_eigenvals(**flags)``:TBW

特異値
----------------------------------------------------------------------
特異値に関するメソッドを記す。固有値に関するメソッドも参照。

.. csv-table::
   :delim: :
   :header: シグニチャー, 説明

   ``condition_number()``:行列の条件数、つまり最大特異値と最小特異値の比を返す。
   ``singular_values()``:行列の特異値をすべて返す。

微積分
----------------------------------------------------------------------
微積分に関するメソッドを次の表に記す。
実装はすべて想像通りになっている。

.. csv-table::
   :delim: :
   :header: シグニチャー, 説明

   ``diff(*args)``:各成分を微分して得られる行列を返す。
   ``integrate(*args)``:各成分を積分して得られる行列を返す。
   ``limit(*args)``:各成分に対して極限をとった行列を返す。

NumPy インターフェイス
======================================================================
モジュール ``sympy.matrices.dense`` には SymPy の行列オブジェクトを
NumPy の ``numpy.array`` オブジェクトにコンバートするための関数が少々ある。

関数 ``list2numpy(l, dtype=object)``
  Python の ``list`` オブジェクトを ``numpy.array`` オブジェクトにコンバートする。

  * 実は SymPy は関係ない。
  * キーワード引数 ``dtype=object`` が存在するということは、
    リストの要素の型を完全に無視できることを示唆している。

関数 ``matrix2numpy(m, dtype=object)``
  SymPy の行列オブジェクトを ``numpy.array`` オブジェクトにコンバートする。

  * 実装を説明すると、この関数はまず行列のサイズ ``m.shape`` と同じサイズの空の ``numpy.array`` を生成する。
    次に ``m`` の各要素を対応する成分にセットして戻すというものだ。

関数 ``symarray(prefix, shape)``
  説明するよりも動きを示したほうが早い。

  .. code-block:: ipython

     In [1]: symarray('ppppp', (3, 3))
     Out[1]: array([[ppppp_0_0, ppppp_0_1, ppppp_0_2],
                    [ppppp_1_0, ppppp_1_1, ppppp_1_2],
                    [ppppp_2_0, ppppp_2_1, ppppp_2_2]], dtype=object)

  * 実際の戻り値は ``numpy.array`` オブジェクト。
  * 行列の各要素は SymPy の ```Symbol`` オブジェクト。
    オブジェクトの ``name`` が出力に表れている。

演習
======================================================================

関連ノート
======================================================================
* :doc:`/python-numpy/tutorial`

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
