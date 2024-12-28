======================================================================
doc/
======================================================================

NumPy_ のインストールフォルダーの直下 :file:`doc` フォルダにはドキュメンテーショ
ン専用の py ファイルが多数ある。

.. contents::

構成
======================================================================

NumPy の開発者はこれらを基に NumPy User Guide を作成していると思われる。下にファ
イルとその内容を表にまとめる。array に関するトピックが圧倒的に多い。

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   ファイル | 内容
   :file:`basics.py` | ``array`` に関する基本的な内容。
   :file:`broadcasting.py` | ``array`` の broadcasting rules についての議論。
   :file:`byteswapping.py` | ``array`` オブジェクトのメモリレイアウトに関する議論。
   :file:`constants.py` | NumPy が提供する各種定数に関する文書。
   :file:`creation.py` | ``array`` オブジェクトの生成に関する文書。
   :file:`glossary.py`| 用語集。
   :file:`howtofind.py` | まだ文書化されていない。
   :file:`indexing.py` | ``array`` オブジェクトの要素を参照する手段に関する議論。
   :file:`internals.py` | ``array`` の実装詳細を説明。
   :file:`io.py` | まだ文書化されていない。
   :file:`jargon.py` | まだ文書化されていない。
   :file:`methods_vs_functions.py` | まだ文書化されていない。
   :file:`misc.py` | IEEE754 浮動小数点数の特殊値、数値計算例外、C 言語インターフェイス等、雑多なメモ。
   :file:`performance.py` | まだ文書化されていない。
   :file:`structured_arrays.py` | 変わった型の ``array`` について。
   :file:`subclassing.py` | ``ndarray`` のサブクラス化に関する文書。
   :file:`ufuncs.py` | Universal functions に関する文書。

:file:`glossary.py`
----------------------------------------------------------------------

まず用語集を見るのがよいか。

ファイル :file:`doc/glossary.py` が用語集を docstring の体裁でまとめている。書式
は reStructuredText のようだ。

収録対象は NumPy 独自に使われるものだけでなく、数学、計算機科学、さらには Python
言語に関係するものにも及ぶ。ここでは気になる用語に絞ってノートをとる。

along on axis
    行列では axis は二つあるが、縦方向の並びが axis 0 で、横方向の並びが axis 1 だ。
    縦方向の方がインデックスが若いことになっているのは row-major rule によるのだろう。
    ``array`` 関連の関数では「axis を引数に取れる」ものが多数ある
    (``sum``, ``var``, ``sort``, ``any``, ``mean``, etc.)
array
    **同種の要素からなる** 配列であることを強調している。
    なお ``ndarray`` のことを単に ``array`` と呼ぶ場合が多い。
array_like
    ``ndarray`` に解釈される任意のコンテナーと思ってよいようだ。なので
    ``ndarray`` オブジェクトやスカラーも array_like だ。
broadcast
    ``array`` 間の演算は同型が基本だが、若干 shape が異なっていても OK な場合が
    ある。
C order/row-major, Fortran order/column-major
    多次元配列のメモリレイアウトに関する話題をきれいにまとめてある。NumPy の
    ``array`` は前者を採用している。 C 言語がそれを利用していることによる。

    OpenGL は column-major だから、PyOpenGL_ のコードを書くときにはその辺の事情
    を意識しないとだめだろう。
flattened
    ``array`` を一次元の shape になるように「折りたたむ」ことができる。
mask, masked array
    OpenGL の ``glColorMask`` の概念みたいなものか。
matrix
    二次元の ``ndarray`` を何らかの点において最適化した matrix クラスがあるらし
    い。演算経過によって shape が変わるようなことがないことを保証するようだ。
slice
    Python の ``list`` オブジェクトに対するスライスを、``array`` でもサポートす
    るという話だ。多次元版スライス。
ufunc
    個々の要素ごとに演算するようなタイプの演算を高速に処理する。後で
    :file:`doc/ufuncs.py` に目を通す程度でいいだろう。
view
    既存の ``array`` からスライシング等の操作で別の ``array`` を作成することがあ
    る。この種の操作で新しくできた ``array`` は、実は参照ベースの proxy オブジェ
    クトであることが多いようだ。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
.. include:: /_include/python-refs-vision.txt
