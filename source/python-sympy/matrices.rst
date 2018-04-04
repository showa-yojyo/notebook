======================================================================
行列
======================================================================
モジュール ``sympy.matrices`` に関するメモを記す。
ここにある機能は、行列を処理するものと、行列に関する数式を処理するものとに分類できる。

.. contents:: ノート目次

.. note::

   紙幅の都合上、出力を一部手で改行した。

   本文中のすべての IPython セッション中のサンプルコードで、
   以下のインポートおよび出力書式設定が済んでいるものとする。

   .. code:: python3

      from sympy.matrices import *
      init_printing(pretty_print=False)

クラス図
======================================================================
行列関連の単純なクラス図を示す。

行列を表現するクラス
----------------------------------------------------------------------
行列オブジェクトの基本単位を表現するためのクラスの論理的な継承関係は次のようになっている。

.. code:: text

   MatrixBase
       MutableDenseMatrix
       ImmutableDenseMatrix

       ImmutableSparseMatrix
       MutableSparseMatrix

* モジュール ``__init__`` で別名が付けられる等されているため、
  クラス名中の Mutable と Dense の部分は省略できる。
  例を挙げると、単に Matrix と書いたとしても、
  実際はクラス MutableDenseMatrix である。

* Mutable と Immutable の違いは Python のプログラマーが思い浮かべるものと同じ。
* Dense と Sparse の違いは疎行列性を意味する。
* MatrixBase のスーパークラスは Python のクラス object である。

行列を構成要素とする数式のためのクラス
----------------------------------------------------------------------
行列オブジェクトを各種演算で構成した数式を表現するためのクラスが多数存在する。
そのクラス群はモジュール ``matrices.expressions`` 以下で定義されており、
それらの継承関係は次のようになっている。
全サブクラスを書き出す必要はまったくないが、何かのために記す。

継承ツリーの右側に関連するフリー関数、行列クラスのメソッド、メモを併記する。

.. code:: text

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

* クラス MatrixExpr のスーパークラスは SymPy のクラス Basic である。

色々な行列の生成方法
======================================================================
まず、行列以外の要素から行列オブジェクトを直接生成する方法を記す。

他のライブラリーの類似機能を利用した経験から言えば、
クラス Matrix のコンストラクターを直接する場合は、
おそらく行列の各成分を細かく指示する場合に限られると思われる。

:code:`Matrix(([[1,0,0], [0,0,0]])`
  入れ子の list は行 (row) を上から下に並べたものとして扱われる。

:code:`Matrix([[1, 2, 3]])`
  上の特別な場合だが、入れ子の中身が list ひとつの場合は行ベクトルと等価な行列となる。

:code:`Matrix([1, 2, 3])`
  入れ子になっていない場合は列ベクトルと等価な行列となる。

:code:`Matrix(2, 3, [1, 2, 3, 4, 5, 6])`
  行列の寸法と成分すべてを行を先に埋める順で指示して生成する。

  * 寸法は行数、列数の順。タテ、ヨコ。

:code:`Matrix(3, 4, lambda i,j: 1 - (i+j) % 2)`
  行列を寸法と添字を引数に取る関数とで生成する。

成分に特徴のある行列を生成する場合は、それに適する関数、メソッドが用意されているので利用する。

* 関数 :code:`eyes` と :code:`zeros` は NumPy_ のそれと同様。
* 関数 :code:`diag` は対角行列の生成であるが、
  より小さい行列を主対角線上に配列するようなこともできる。

基本的な操作
======================================================================
* 要素アクセス

  * 行列の要素ひとつにアクセスするには、
    適切な添え字を用いて :code:`M[i]` や :code:`M[i, j]` とする。
    添字がひとつの場合は、要素を row-major でアクセスする。

  * NumPy の array と同様にスライスもサポートしている。

    * 記法も同様に :code:`M[start:stop:step]` のようにする。
    * 右辺値としてスライスする場合は、元のオブジェクトの一部のコピーとして機能する。
      一方、左辺値としてスライスする場合は、元のオブジェクトのビューのように機能する。

* 行列代数

  * 少なくとも同型の行列同士では加法と乗法が成立する。
    これは標準的な算術演算子 :code:`+`, :code:`-`, :code:`*` で表現する。

* ベクトル演算

  * 例えばメソッド :code:`dot` と :code:`cross` が利用可能になる。
    詳細は後述する。

* 各要素に関数を適用するには、メソッド :code:`applyfunc` を用いる。

線形代数的操作
======================================================================
関数 :code:`GramSchmidt(vlist, orthonormal=False)`
  ベクトルの集合を基に直交基底を得る。

  * 引数 :code:`vlist` は同じサイズのベクトルのコレクション。
    断りがないが、線形独立である必要があるはずだ。

  * キーワード引数 :code:`orthonormal` で得られるベクトルの長さを 1 にするかどうかを指定する。

  * 実装を見ると、メソッド :code:`project` を利用していることがわかる。

クラス MatrixBase
======================================================================
このクラスにはメソッドが大量にある。要所に絞って記す。演算子は省略。

プロパティー
----------------------------------------------------------------------
プロパティーのほぼすべてを記す。
下の表のもの以外にも、例えば :code:`.rows` のようにしてオブジェクトの属性を得ることができるものもあるようだが、
コードから拾えないので割愛した。

.. csv-table::
   :delim: @
   :header: プロパティー, 説明
   :widths: 12, 30

   :code:`C`@要素ごとに複素共役をとった行列を返す。
   :code:`D`@Dirac 共役行列を返す。
   :code:`H`@Hermite 共役を返す。
   :code:`T`@転置行列を返す。
   :code:`is_hermitian`@Hermite 行列かどうかを返す。
   :code:`is_lower`@下三角行列かどうかを返す。
   :code:`is_lower_hessenberg`@下 Hessenberg 行列かどうかを返す。
   :code:`is_square`@正方行列かどうかを返す。
   :code:`is_upper`@上三角行列かどうかを返す。
   :code:`is_upper_hessenberg`@上 Hessenberg 行列かどうかを返す。
   :code:`is_zero`@零行列かどうかを返す。
   :code:`shape`@行列の寸法を返す。必ず (r, c) の型をとる。

* :code:`C` はメソッド :code:`conjugate` のエイリアス。

* :code:`D` は結局はモジュール ``sympy.physics.matrices`` の機能を利用している。
  そのときにまた調べよう。

* :code:`H` は :code:`T.C` と同じ。

* :code:`T` はメソッド :code:`transpose` のエイリアス。

* 三角行列判定系のメソッドは for ループを二重にまわして、
  テストに必要な各成分を要素オブジェクトのプロパティー :code:`is_zero` でゼロかどうかをテストしている。

  また、必ずしも正方行列でなくてよい。

要素の物理的な操作
----------------------------------------------------------------------
行や列のデータを物理的に操作するタイプのものを次の表に記す。

.. csv-table::
   :delim: @
   :header: シグニチャー, 説明
   :widths: 16, 30

   :code:`hstack(*args)`@複数の行列を横に連結する。
   :code:`vstack(*args)`@複数の行列を縦に連結する。
   :code:`col_insert(pos, mti)`@行列に列を挿入する。
   :code:`row_insert(pos, mti)`@行列に行を挿入する。
   :code:`col_join(bott)`@行列同士を縦に連結する。
   :code:`row_join(rhs)`@行列同士を横に連結する。
   :code:`permuteBkwd(perm)`@行を指定の置換で入れ替える。
   :code:`permuteFwd(perm)`@行を指定の置換で入れ替える。

* どのメソッドも inplace な振る舞いをしない。
* :code:`hstack`, :code:`vstack` はクラスメソッド。
  余談だが同名のものが NumPy にもある。
* 挿入系メソッドの引数 :code:`mti` は :code:`shape` の縦横の一致を問う。
* 置換系メソッドの核となるのはメソッド :code:`row_swap` である。

部分空間
----------------------------------------------------------------------
部分空間に関するメソッドを下の表に示す。

.. csv-table::
   :delim: @
   :header: シグニチャー, 説明
   :widths: 24, 24

   :code:`columnspace(simplify=False)`@列空間を返す。
   :code:`nullspace(simplify=False)`@零空間を返す。

どちらもメソッド :code:`rref` が重要な働きをする。

乗法
----------------------------------------------------------------------
行列またはベクトルの乗算に関するメソッドを下の表に示す。
行か列のどちらかのサイズを 1 にすれば Matrix を列ベクトル、行ベクトルとして扱える。

.. csv-table::
   :delim: @
   :header: シグニチャー, 説明
   :widths: 16, 36

   :code:`cross(b)`@ベクトルのクロス積、ベクトル積を計算する。
   :code:`dot(b)`@ベクトルのドット積、スカラー積を計算する。
   :code:`multiply(b)`@行列の乗算を行う。
   :code:`multiply_elementwise(b)`@行列の成分ごとの乗算を行う。

* メソッド :code:`dot` はベクトル同士だけではなく、
  サイズさえ合えば行列対ベクトルでもよい。
  ただし :code:`cross` のほうは本当にベクトル限定。しかも 3 次元のみ。

* メソッド :code:`multiply` は演算子 :code:`*` で実装されている。

* メソッド :code:`multiply_elementwise` は
  関数 :code:`matrix_multiply_elementwise` で実装されている。

ノルム
----------------------------------------------------------------------
ノルムに関係するメソッドを次に示す。

.. csv-table::
   :delim: @
   :header: シグニチャー, 説明
   :widths: 16, 24

   :code:`norm(ord=None)`@行列またはベクトルのノルムを返す。
   :code:`normalized()`@正規化した行列またはノルムを返す。

* ノルムはデフォルトでは行列に対しては Frobenius ノルムを、
  ベクトルに関しては 2-ノルムをそれぞれ返す。

* ノルムの種類に関しては help を参照。いつも使うものは揃っている。

* メソッド :code:`normalized` で用いられるノルムはデフォルトのノルム。

行列式
----------------------------------------------------------------------
行列式に関係するメソッドを次に示す。

.. csv-table::
   :delim: @
   :header: シグニチャー, 説明
   :widths: 16, 44

   :code:`det(method='bareis')`@正方行列の行列式を計算する。
   :code:`det_bareis()`@Baries のアルゴリズムにより行列式を計算する。
   :code:`det_LU_decomposition()`@LU 分解により行列式を計算する。

* :code:`det` は結局は残りのふたつか、
  後述するメソッド :code:`berkowitz_det` のいずれかである。

* Baries のアルゴリズムというのは、Gauss の消去法の拡張版みたいなもので、
  丸め誤差に強いという性質が期待できる。

* LU 分解による行列式の計算は、分解行列の主対角線の成分だけを見ればよいというものだ。
  後述するメソッド :code:`LUdecomposition` も参照。

余因子
----------------------------------------------------------------------
余因子に関係するメソッドを次に示す。

.. csv-table::
   :delim: @
   :header: シグニチャー, 説明
   :widths: 24, 40

   :code:`adjugate(method="berkowitz")`@余因子行列を生成する。
   :code:`cofactor(i, j, method="berkowitz")`@指定成分の符号調整を施した余因子を計算する。
   :code:`cofactorMatrix(method="berkowitz")`@転置を施していない余因子行列を生成する。
   :code:`minorEntry(i, j, method="berkowitz")`@指定成分の符号調整を施していない余因子を計算する。
   :code:`minorMatrix(i, j)`@元の行列から指定行と指定列を削った、一回り小さい行列を生成する。

これらのメソッドの実装は線形の依存関係がある。

まずメソッド :code:`adjugate` は :code:`cofactorMatrix` の転置行列を返す。
その :code:`cofactorMatrix` は単に :code:`cofactor` を成分ごとに計算して、
その値を成分とする行列を生成する。
メソッド :code:`cofactor` は対応する成分の :code:`minorEntry` の戻り値に、
成分の添字から決まる符号を付けるだけだ。
最後にメソッド :code:`minorEntry` は指定成分の :code:`minorMatrix` の行列式を単に返す。

対角行列
----------------------------------------------------------------------
対角行列に関係するメソッドを次に示す。

.. csv-table::
   :delim: @
   :header: シグニチャー, 説明
   :widths: 12, 24

   :code:`diagonalize(...)`@対角化可能な行列を対角化する。
   :code:`is_diagonal()`@行列が対角行列かどうかを返す。
   :code:`is_diagonalizable(...)`@行列が対角化可能かどうかを返す。

* 行列 :code:`M` に対して :math:`D = P\inv M P` とすると、
  メソッド :code:`diagonalize` は :code:`(P, D)` を返す。

* 対角化可能性の判定は、各固有値の多重度をチェックすることでなされる。
  この過程で行列オブジェクトのメンバーデータに中間生成物的なものが残る。
  これをクリアしたい場合に、
  キーワード引数 :code:`clear_subproducts=True` を指定する。

* ちなみに対角行列を生成する機能は関数 :code:`diag` である。

分解
----------------------------------------------------------------------
行列の分解 (decomposition, factorization) に関係するメソッドを次に示す。

.. csv-table::
   :delim: @
   :header: シグニチャー, 説明
   :widths: 12, 36

   :code:`cholesky()`@行列の Cholesky 分解を行う。
   :code:`LDLdecomposition()`@行列の LDL 分解を行う。
   :code:`LUdecomposition(...)`@行列の LU 分解を行う。
   :code:`LUdecomposition_Simple(...)`@行列の LU 分解を単純なアルゴリズムで実装したもの。
   :code:`LUdecompositionFF()`@行列の LU 分解を fraction-free なアルゴリズムで実装したもの。
   :code:`QRdecomposition()`@行列の QR 分解を行う。

Cholesky 分解は :math:`A = L L^\top` なる :code:`L` を計算する。
与える行列が正定値実対象行列である必要がある。

LDL 分解は :math:`A = L D L^\top` を満たす行列を計算してペア :code:`(L, D)` を返す。

* これもまた与える行列が正定値実対象行列である必要がある。
* 行列 :code:`L` は下三角行列であり、対角成分はすべて 1 である。
* 行列 :code:`D` は対角行列である。

LU 分解は :math:`A = LU` というものだ。

* :code:`LUdecomposition` の戻り値は :code:`(L, U, p)` の形である。
  ここで :code:`p` は行の交換情報を表現する list である。
  なぜ行列ではなくリストの形式を返すのかがよくわからない。

* :code:`LUdecomposition_Simple` の戻り値は :code:`(A, p)` の形である。
  ただし :code:`A` は :code:`L` と :code:`U` の合いの子のような行列だ。

* :code:`LUdecompositionFF` は :math:`PA = L D\inv U` を満たす行列の組
  :code:`(P, L, D, U)` を返す。特徴は元の行列がある整域上のものであるとき、
  :code:`L`, :code:`D`, :code:`U` のいずれも同じ整域に属するというものだ。

* QR 分解は行列を :math:`A = QR` の形に分解するアルゴリズムだ。
  行列 :code:`Q` は直交行列で、行列 :code:`R` は上三角行列となる。

ソルバー
----------------------------------------------------------------------
線形連立方程式を解くことに関係するメソッドを次に示す。
基本的には :math:`A \mathbf{x} = \mathbf{b}` に対して、

* :math:`A` が行列オブジェクト自身、
* :math:`\mathbf{x}` が各メソッドの戻り値（の一部）、
* :math:`\mathbf{b}` が各メソッドの最初の引数

に相当する。

.. csv-table::
   :delim: @
   :header: シグニチャー, 説明
   :widths: 20, 30

   :code:`cholesky_solve(rhs)`@Cholesky 分解によるソルバー。
   :code:`diagonal_solve(rhs)`@対角行列を係数とする方程式を解く。
   :code:`gauss_jordan_solve(b, freevar=False)`@Gauss-Jordan 消去法によるソルバー。
   :code:`LDLsolve(rhs)`@LDL 分解によるソルバー。
   :code:`LUsolve(rhs, ...)`@LU 分解によるソルバー。
   :code:`QRsolve(b)`@QR 分解によるソルバー。
   :code:`pinv_solve(B, arbitrary_matrix=None)`@Moore-Penrose の擬逆行列によるソルバー。
   :code:`lower_triangular_solve(rhs)`@下三角行列を係数とする方程式を解く。
   :code:`upper_triangular_solve(rhs)`@上三角行列を係数とする方程式を解く。

* :code:`cholesky_solve`,  :code:`LDLsolve` は係数（自身の行列）が対称行列であるか、
  行数が列数よりも大きい行列であればなんとか動く。

* :code:`diagonal_solve` は対角成分にゼロがあってはならない
  （解を得るときの除算の分母だから）。

* :code:`gauss_jordan_solve` は連立方程式の条件が不足して解が不定個求まる場合に適宜パラメーターを導入する。
  解の行列に加えて、このパラメーターを別途行列にまとめて同時に返す。

* :code:`LUsolve` の利用する分解メソッドは :code:`LUdecomposition_Simple` である。
  その後に前進代入と後退代入を行って解となる行列を返す。

  * 対称行列向け。

* :code:`QRsolve` は :code:`QRdecomposition` の結果から後退代入だけで解が得られる。

  * これは教育目的かつシンボル含みの行列用のメソッドとのこと。

逆行列
----------------------------------------------------------------------
逆行列に関係するメソッドを次に示す。
数値計算の観点から言えば、逆行列の計算は相当なコストがかかるため、
なるべく避けるのが原則だ。
可能な限り先述した分解アルゴリズムやソルバーを利用するのが普通だ。

.. csv-table::
   :delim: @
   :header: シグニチャー, 説明
   :widths: 12, 20

   :code:`inv(method=None, **kwargs)`@逆行列を計算する。
   :code:`inv_mod(m)`@法を :code:`m` とするときの逆行列を計算する。
   :code:`pinv()`@Moore-Penrose の擬逆行列を計算する。

* :code:`inv` ではキーワード引数 :code:`method` で行列式を計算するアルゴリズムを選択できる。

  * ``'GE'``: Gauss の消去法。デフォルトのアルゴリズム。
  * ``'LU'``: LU 分解。
  * ``'ADJ'``: 余因子行列と行列式を用いて逆行列を得る。

* 面白いのは :code:`inv_mod` だろう。整数論的処理が一部入っていて、
  オイラー関数、余因子行列、行列式を組み合わせて所望の行列を生成する。

Berkowitz のアルゴリズム
----------------------------------------------------------------------
Berkowitz のアルゴリズムと、それに関係するメソッドを次に示す。

.. csv-table::
   :delim: @
   :header: シグニチャー, 説明
   :widths: 16, 24

   :code:`berkowitz()`@Berkowitz のアルゴリズムを実装する。
   :code:`berkowitz_det()`@Berkowitz のアルゴリズムにより行列式を計算する。
   :code:`berkowitz_minors()`@Berkowitz のアルゴリズムにより主小行列を計算する。
   :code:`berkowitz_charpoly(x, simplify)`@Berkowitz のアルゴリズムにより特性多項式を求める。
   :code:`berkowitz_eigenvals(**flags)`@Berkowitz のアルゴリズムにより固有値を計算する。

まずメソッド :code:`berkowitz` の中身について。
`この記事 <https://de.wikipedia.org/wiki/Algorithmus_von_Samuelson-Berkowitz>`_ のアルゴリズムを実装している。

Berkowitz のアルゴリズムを単純に説明すると、
正方行列の対角線に沿って、サイズの小さい順にミニ正方行列を取る。
各ミニ正方行列の特性多項式を求めていくのだが、
あるステップのミニ正方行列の特性多項式を得るのに、
その直前に求めたサイズが一回り小さいミニ正方行列の計算結果を利用できるというものだ。

固有多項式がわければ行列式、行列因子、固有値等が芋づる式にわかるので、
クラス MatrixBase のメソッドの大部分がこのアルゴリズムに頼っている。

特異値
----------------------------------------------------------------------
特異値に関するメソッドを記す。固有値に関するメソッドも参照。

.. csv-table::
   :delim: @
   :header: シグニチャー, 説明
   :widths: 12, 44

   :code:`condition_number()`@行列の条件数、つまり最大特異値と最小特異値の比を返す。
   :code:`singular_values()`@行列の特異値をすべて返す。

* :code:`singular_values` はすべての特異値を list に詰めて返す。
  これらの値が大きい順にソートされている。

微積分
----------------------------------------------------------------------
微積分に関するメソッドを次の表に記す。
実装はすべて想像通りになっている。

.. csv-table::
   :delim: @
   :header: シグニチャー, 説明
   :widths: 12, 36

   :code:`diff(*args)`@各成分を微分して得られる行列を返す。
   :code:`integrate(*args)`@各成分を積分して得られる行列を返す。
   :code:`limit(*args)`@各成分に対して極限をとった行列を返す。

NumPy インターフェイス
======================================================================
モジュール ``sympy.matrices.dense`` には SymPy の行列オブジェクトを
NumPy の :code:`numpy.array` オブジェクトにコンバートするための関数が少々ある。

関数 :code:`list2numpy(l, dtype=object)`
  Python の list オブジェクトを :code:`numpy.array` オブジェクトにコンバートする。

  * 実は SymPy は関係ない。
  * キーワード引数 :code:`dtype=object` が存在するということは、
    リストの要素の型を完全に無視できることを示唆している。

関数 :code:`matrix2numpy(m, dtype=object)`
  SymPy の行列オブジェクトを :code:`numpy.array` オブジェクトにコンバートする。

  * 実装を説明すると、この関数はまず行列のサイズ :code:`m.shape` と
    同じサイズの空の :code:`numpy.array` を生成する。
    次に :code:`m` の各要素を対応する成分にセットして戻すというものだ。

関数 :code:`symarray(prefix, shape)`
  説明するよりも動きを示したほうが早い。

  .. code:: ipython

     In [1]: symarray('ppppp', (3, 3))
     Out[1]: array([[ppppp_0_0, ppppp_0_1, ppppp_0_2],
                    [ppppp_1_0, ppppp_1_1, ppppp_1_2],
                    [ppppp_2_0, ppppp_2_1, ppppp_2_2]], dtype=object)

  * 実際の戻り値は :code:`numpy.array` オブジェクト。
  * 行列の各要素は SymPy の Symbol オブジェクト。
    オブジェクトの :code:`name` が出力に表れている。

演習
======================================================================

Berkowitz のアルゴリズムを検証する
----------------------------------------------------------------------
シンボルベースの 3 次正方行列を定義して、
メソッド :code:`berkowitz` を呼び出して戻り値を得る。
この戻り値から行列のさまざまな属性が得られることを見よう。

.. code:: ipython

   In [1]:M = Matrix(3, 3, symbols('a:3:3')); M
   Out[1]:
   Matrix([[a00, a01, a02],
           [a10, a11, a12],
           [a20, a21, a22]])

   In [2]: Mberk = M.berkowitz(); Mberk
   Out[2]: ((1,),
            (1,
             -a00),
            (1,
             -a00 - a11,
             a00*a11 - a01*a10),
            (1,
             -a00 - a11 - a22,
             a00*a11 - a01*a10 - a02*a20 - a12*a21 - a22*(-a00 - a11),
             -a20*(a00*a02 + a01*a12) - a21*(a02*a10 + a11*a12) - a22*(a00*a11 - a01*a10) + (-a00 - a11)*(-a02*a20 - a12*a21)))

   In [3]: Mcharpoly = M.charpoly().coeffs(); Mcharpoly
   Out[3]: [1,
            -a00 - a11 - a22,
            a00*a11 + a00*a22 - a01*a10 - a02*a20 + a11*a22- a12*a21,
            -a00*a11*a22 + a00*a12*a21 + a01*a10*a22 - a01*a12*a20 - a02*a10*a21+ a02*a11*a20]

   In [4]: all(simplify(i - j) == 0 for i, j in zip(Mcharpoly, Mberk[-1]))
   Out[4]: True

   In [5]: simplify(M.cofactor(2, 2) - Mberk[2][-1])
   Out[5]: 0

   In [6]: simplify(M.det() + Mberk[-1][-1])
   Out[6]: 0

* [1] 全成分を記号とする 3 次正方行列 :code:`M` を定義する。
* [2] メソッド :code:`berkowitz` の戻り値を確認する。
* [3][4] :code:`M` の特性多項式の係数を出力する。
  これは 4 次多項式の係数を降べきの順に並べた list オブジェクトとして得られる。

  次にこの係数と :code:`berkowitz` の戻り値の tuple オブジェクトの末尾の要素とを比較して、
  両者が一致することを見る。

* [5] :code:`M` の対角成分末端（行列の右下）要素の余因子は
  :code:`berkowitz` の戻り値の 2 ステップ目 :code:`Mberk[2]` の末尾の要素に等しい。
  これは同ステップのミニ正方行列の行列式でもある。

* [6] :code:`M` の行列式は :code:`berkowitz` の戻り値の末尾の末尾に符号を考慮したものである。
  符号の決まり方は、特性多項式の次数の偶奇性による。

最後に固有値が特性多項式の解であることを見せて締めたいところだが、
紙幅の都合上、どうしても長い数式をきれいに表示できないため、割愛する。

LU 分解再挑戦
----------------------------------------------------------------------
:doc:`/python-scipy/linear-equations` で LU 分解した行列を SymPy で分解すると結果が異なるのではないか。

.. code:: ipython

   In [1]: A = Matrix([[1, 2, 2], [2, 5, 6], [3, 8, 12]])

   In [1]: L, U, p = A.LUdecomposition()

   In [2]: L
   Out[2]:
   Matrix([
   [1, 0, 0],
   [2, 1, 0],
   [3, 2, 1]])

   In [3]: U
   Out[3]:
   Matrix([
   [1, 2, 2],
   [0, 1, 2],
   [0, 0, 2]])

   In [4]: p
   Out[4]: []

   In [5]: L * U
   Out[5]:
   Matrix([
   [1, 2,  2],
   [2, 5,  6],
   [3, 8, 12]])

* [2][3] 期待しているようなきれいな三角行列が得られている。
* [4] 行の入れ替えはない。

関連ノート
======================================================================
:doc:`/python-numpy/tutorial`
  NumPy の array と SymPy の MatrixBase には共通する機能が多数ある。

:doc:`/python-scipy/linear-equations`
  SciPy の機能で LU 分解をする例を記した。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
