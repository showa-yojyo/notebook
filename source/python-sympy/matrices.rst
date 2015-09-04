======================================================================
行列
======================================================================
モジュール ``sympy.matrices`` に関するメモを記す。

.. contents:: ノート目次

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

クラス ``MatrixBase``
======================================================================

NumPy インターフェイス
======================================================================


.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
