======================================================================
doc/
======================================================================
NumPy_ のインストールフォルダーの直下 :file:`doc` フォルダにはドキュメンテーション専用の py ファイルが多数ある。

.. contents::

構成
======================================================================
NumPy の開発者はこれらを基に NumPy User Guide を作成していると思われる。
下にファイルとその内容を表にまとめる。array に関するトピックが圧倒的に多い。

============================== ====
ファイル                       内容
============================== ====
basics.py                      array に関する基本的な内容。
broadcasting.py                array の broadcasting rules についての議論。
byteswapping.py                array オブジェクトのメモリレイアウトに関する議論。
constants.py                   NumPy が提供する各種定数に関する文書。
creation.py                    array オブジェクトの生成に関する文書。
glossary.py                    用語集。
howtofind.py                   まだ文書化されていない。
indexing.py                    array オブジェクトの要素を参照する手段に関する議論。
internals.py                   array の実装詳細を説明。
io.py                          まだ文書化されていない。
jargon.py                      まだ文書化されていない。
methods_vs_functions.py        まだ文書化されていない。
misc.py                        IEEE754 浮動小数点数の特殊値、数値計算例外、C 言語インターフェイス等、雑多なメモ。
performance.py                 まだ文書化されていない。
structured_arrays.py           変わった型の array について。
subclassing.py                 ``ndarray`` のサブクラス化に関する文書。
ufuncs.py                      Universal functions に関する文書。
============================== ====

glossary.py
----------------------------------------------------------------------
まず用語集を見るのがよいか。

ファイル :file:`doc/glossary.py` が用語集を docstring の体裁でまとめている。
書式は reStructuredText のようだ。

収録対象は NumPy 独自に使われるものだけでなく、数学、計算機科学、
さらには Python 言語に関係するものにも及ぶ。
ここでは気になる用語に絞ってノートをとる。

along on axis
    行列では axis は二つあるが、縦方向の並びが axis 0 で、横方向の並びが axis 1 だ。
    縦方向の方がインデックスが若いことになっているのは row-major rule によるのだろう。
    array 関連の関数では「axis を引数に取れる」ものが多数ある
    (``sum``, ``var``, ``sort``, ``any``, ``mean``, etc.)

array
    **同種の要素からなる** 配列であることを強調している。
    なお ``ndarray`` のことを単に array と呼ぶ場合が多い。

array_like
    ``ndarray`` に解釈される任意のコンテナーと思ってよいようだ。
    なので ``ndarray`` オブジェクトやスカラーも array_like だ。

broadcast
    array 間の演算は同型が基本だが、若干 shape が異なっていても OK な場合がある。

C order/row-major, Fortran order/column-major
    多次元配列のメモリレイアウトに関する話題をきれいにまとめてある。
    NumPy の array は前者を採用している。
    C 言語がそれを利用していることによる。

    OpenGL は column-major だから、
    PyOpenGL_ のコードを書くときにはその辺の事情を意識しないとだめだろう。

flattened
    array を一次元の shape になるように「折りたたむ」ことができる。

mask, masked array
    OpenGL の ``glColorMask`` の概念みたいなものか。

matrix
    2 次元の ``ndarray`` を何らかの点において最適化した matrix クラスがあるらしい。
    演算経過によって shape が変わるようなことがないことを保証するようだ。

slice
    Python の ``list`` オブジェクトに対するスライスを、
    array でもサポートするという話だ。多次元版スライス。

ufunc
    個々の要素ごとに演算するようなタイプの演算を高速に処理する。
    後で :file:`doc/ufuncs.py` に目を通す程度でいいだろう。

view
    既存の array からスライシング等の操作で別の array を作成することがある。
    この種の操作で新しくできた array は、
    実は参照ベースの proxy オブジェクトであることが多いようだ。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
