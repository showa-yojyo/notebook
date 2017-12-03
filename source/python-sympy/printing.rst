======================================================================
出力
======================================================================
SymPy オブジェクトを表現するいろいろな方法について記す。

.. contents:: ノート目次

.. note::

   本文中のすべての IPython セッション中のサンプルコードで、
   以下のインポートおよび出力書式設定が済んでいるものとする。

   .. code-block:: python3

      from sympy import cos, sin
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

LatexPrinter をカスタマイズする
----------------------------------------------------------------------
ここでは 関数 :code:`latex` による SymPy オブジェクトの一部の出力文字列を変更する方法を記す。
例を挙げる。外微分周りの表示で以下の二点を目的としたカスタマイズ手順を説明する。

* 座標成分が太字になるのを回避したい。
* 外微分演算子を自作のマクロに置き換えたい。

ここでは正攻法とはとても言えない方法を採っている。
いずれ改良案を考えたい。

#. 必要なクラスをインポートする。

   .. literalinclude:: /_sample/sympy/extp.py
      :language: python3
      :lines: 6-7

#. 対応する SymPy オブジェクトの型に従い、カスタムメソッドを実装する。

   今回の例だと対象となるのは BaseScalerField と Differential だ。
   このときは名前が ``_print_BaseScalarField`` および ``_print_Differential``
   というメソッドを適当なスコープで実装する。

   コード例を以下に示す：

   .. literalinclude:: /_sample/sympy/extp.py
      :language: python3
      :lines: 11-21

   実装の必要に応じてインポート文を追加する（この場合は Symbol を含める）。
   実装例は LatexPrinter のソースコードを手本にすればよい。

   一般にクラス CLASSNAME の LaTeX 出力を書き換える場合には
   メソッド ``_print_CLASSNAME`` を実装する。

#. LatexPrinter 本来のメソッドをカスタムメソッドで置き換える。

   Python 組み込み関数 :code:`setattr` を活用する：

   .. literalinclude:: /_sample/sympy/extp.py
      :language: python3
      :lines: 23-24

ここまでできれば、既定の :code:`latex` や :code:`print_latex` をそのまま呼び出すことで、
カスタムメソッドが SymPy の出力システムから呼び出される。

オブジェクト指向プログラミング言語のライブラリー設計だと、
何か ``set_latex_printer`` のようなインターフェイスが存在して、
そこに LatexPrinter のサブクラスを設定できて然るべきなのだが、
LatexPrinter に関してはそのようなものは提供されていない。

なお、正攻法で行くのならば、LatexPrinter をサブクラスして、
自分用の関数 :code:`latex` と :code:`print_latex` を実装するのが妥当と思われる。

実装例
----------------------------------------------------------------------
これまでに説明してきた方法を一つにまとめたスクリプトおよびその実行結果を以下に示す。

.. literalinclude:: /_sample/sympy/extp.py
   :language: python3
   :lines: 5-

このコードの途中の 2 行をコメントアウトすることによって得られる出力は次のようなものだが::

   - 3 \boldsymbol{\mathrm{x}}^{2} \boldsymbol{\mathrm{y}} \mathrm{d}z + \boldsymbol{\mathrm{x}}^{2} \boldsymbol{\mathrm{z}} b \mathrm{d}y + \boldsymbol{\mathrm{x}} \boldsymbol{\mathrm{y}} \boldsymbol{\mathrm{z}} a \mathrm{d}x
   d(- 3 \boldsymbol{\mathrm{x}}^{2} \boldsymbol{\mathrm{y}} \mathrm{d}z + \boldsymbol{\mathrm{x}}^{2} \boldsymbol{\mathrm{z}} b \mathrm{d}y + \boldsymbol{\mathrm{x}} \boldsymbol{\mathrm{y}} \boldsymbol{\mathrm{z}} a \mathrm{d}x)
   - \boldsymbol{\mathrm{x}}^{2} b - 3 \boldsymbol{\mathrm{x}}^{2}
   \boldsymbol{\mathrm{x}} \boldsymbol{\mathrm{y}} a + 6 \boldsymbol{\mathrm{x}} \boldsymbol{\mathrm{y}}
   - \boldsymbol{\mathrm{x}} \boldsymbol{\mathrm{z}} a + 2 \boldsymbol{\mathrm{x}} \boldsymbol{\mathrm{z}} b

カスタム版を適用した出力は次のようになる::

   - 3 x^{2} y \dd z + x^{2} z b \dd y + x y z a \dd x
   \dd(- 3 x^{2} y \dd z + x^{2} z b \dd y + x y z a \dd x)
   - x^{2} b - 3 x^{2}
   x y a + 6 x y
   - x z a + 2 x z b

画像出力
======================================================================
オブジェクトを文字列として出力する以外に、画像として出力する方法もある。
関数 :code:`preview` はそのような画像生成と出力の両方を行なうことができる。

PNG 出力
----------------------------------------------------------------------
キーワード引数 ``output=png`` を指定するか、あるいはこのキーワード引数を省略すると、
SymPy オブジェクトに相当する数式が描画された PNG 画像を生成して
適当なビューワープログラムでそれを表示する。

* Pyglet パッケージが動作環境にない場合には、呼び出し側が明示的に
  キーワード引数 ``viewer`` を追加で指定する必要がある。

  例えば Windows 上での実行において「ペイント」を起動させるには次のようにする：

  .. code:: ipython

     In [1]: preview(cos(x)**2 + sin**2(x), viewer='mspaint')

  このようにすると、対応する数式が描かれている PNG ファイルを開いた状態の
  「ペイント」ウィンドウがデスクトップに現れる。

* 数式が描画された PNG 画像をファイルに保存することもできる。
  キーワード引数 ``viewer='file'`` に加えて、キーワード引数 ``filename`` を指定し、
  保存先のファイルパスを指定する必要がある：

  .. code:: ipython

     In [1]: preview(cos(x)**2 + sin(x)**2, viewer='file', filename='preview.png')

* また、画像をメモリに保存する機能もある。
  これには BytesIO オブジェクトをあらかじめ生成しておき、
  キーワード引数 ``viewer='BytesIO'`` に加えてキーワード引数 ``outputbuffer`` を指定し、
  そのオブジェクトをその引数に設定する必要がある。
  利用予定がないので詳細を割愛する。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt

