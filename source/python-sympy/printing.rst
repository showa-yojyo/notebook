======================================================================
出力
======================================================================
SymPy オブジェクトのテキストファイルやコンソールへの出力について記す。

.. contents:: ノート目次

.. note::

   本文中のすべての IPython セッション中のサンプルコードで、
   以下のインポートおよび出力書式設定が済んでいるものとする。

   .. code-block:: python3

      from sympy.printing import *

Pretty Print
======================================================================
大げさに言えば、オブジェクトをアスキーアートとして出力する一連の仕組みだ。
先に要点を挙げる：

* 個人的に SymPy のこれは肌に合わないので、常に無効にしておきたい。
  IPython コンソールのセッションでオブジェクトの出力がアスキーアート化されているようならば、
  :code:`init_printing(pretty_print=False)` を実行することで、即時に無効化できる。

* 明示的にアスキーアートを出力するには関数 :code:`pretty_print` を呼び出す。

* 関数 :code:`pretty_print` には別名 :code:`pprint` が定義されているので、
  コンソール上の作業時には別名のほうを主にタイプするはずだ。

* この機能に頼るぐらいならば、IPython ではなく Jupyter で作業するだろう。
  そちらは最初から LaTeX 出力がオンになっているはずだ。

LaTeX
======================================================================
オブジェクトを TeX コードとして出力するときの要点を挙げると次のようなものになるだろう：

* 関数 :code:`latex` または :code:`print_latex` を呼び出すと
  オブジェクトを表現する TeX コードを得ることができる。

* 関数 :code:`latex` または :code:`print_latex` の挙動を調整するための
  ``fold_func_brackets``, ``mat_str``, ``mat_delim`` などのキーワード引数があるので、
  これを上手に使う。

* ただし過信はできない。出力結果を何かの文書に流用するのであれば、
  最終的にはテキストエディターで細部を手動編集することになる。

オブジェクトを TeX 形式の文字列に変換するには関数 :code:`latex` を用いる。
ただし、それを標準出力等に出力するには関数 :code:`print_latex` を使うのが
タイプ量の点でわずかに楽だ。

両者の引数リストは同一だ。そのキーワード引数の中で有用なものをいくつか記す。

* ``fold_func_brackets=True`` を指定すると、数学関数呼び出しのカッコを可能な限り省略する。
  例えば三角関数を多く含む式に対して適用すると効果がわかりやすい：

  .. code-block:: ipython

     In [1]: from sympy import cos, sin

     In [2]: from sympy.abc import x

     In [3]: f = sin(x)**2 + cos(x)**2

     In [4]: print_latex(f)
     \sin^{2}{\left (x \right )} + \cos^{2}{\left (x \right )}

     In [4]: print_latex(f, fold_func_brackets=True)
     \sin^{2} {x} + \cos^{2} {x}

  個人的にはまだ中括弧を削れるとは思うのだが、実用には堪える。

* ``mat_str`` は行列の環境名を指定するキーワード引数だ。
  例えば ``mat_str=pmatrix`` を指定すると、式に含まれる行列に対応する TeX コードが
  ``\begin{pmatrix}`` と ``\end{pmatrix}`` で囲まれるようになる。
  ただしその場合には行列のカッコを SymPy が別途補うので、
  さらに ``mat_delim`` キーワード引数を空文字列等に指定することでそれを無効化する。

  .. code-block:: ipython

     In [1]: from sympy import Matrix

     In [2]: A = Matrix([[1, 2], [3, 4]]); A
     Out[2]:
     Matrix([
     [1, 2],
     [3, 4]])

     In [3]: print_latex(A)
     \left[\begin{matrix}1 & 2\\3 & 4\end{matrix}\right]

     In [4]: print_latex(A, mat_str='pmatrix')
     \left[\begin{pmatrix}1 & 2\\3 & 4\end{pmatrix}\right]

     In [5]: print_latex(A, mat_str='pmatrix', mat_delim=None)
     \begin{pmatrix}1 & 2\\3 & 4\end{pmatrix}

  [4] と [5] の MathJax によるレンダリングを次に示す
  （画像上の右クリックメニュー :menuselection:`Show Math As --> Tex Commands`
  でソース TeX コードが確認できる）：

  .. math::

     \left[\begin{pmatrix}1 & 2\\3 & 4\end{pmatrix}\right]

  .. math::

     \begin{pmatrix}1 & 2\\3 & 4\end{pmatrix}

実際には :code:`print_latex` の出力結果をそのままコピー＆ペーストして済むということは
ほとんどないだろう。テキストエディターに出力結果テキストを展開して、
手動で括弧を間引いたり、スペースを補ったり、コマンドを一部自作のマクロに置き換えたりすることになる。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt

