======================================================================
基本テク
======================================================================

本稿では Matplotlib_ インストール直後にでも実現可能な基本的な操作について記す。
基本の手順は、NumPy_/SciPy_ の機能でデータを生成し、その 2D プロットを
Matplotlib を用いて描画することだ。

.. contents::

.. note::

   特に断らない限り、以降のテキストおよびコード片においては、各種 ``import``
   を次のようにしたものと仮定している。

   .. code:: python3

      import numpy as np
      import scipy as sp
      import matplotlib as mpl
      import matplotlib.pyplot as plt
      from matplotlib import pylab, mlab

基本的な関数・メソッドを押さえる
======================================================================

下の表を見てからヘルプを当たる。

後で見るように、モジュール ``matplotlib.pyplot`` の関数の機能は、ある種の「アク
ティブな」オブジェクトのメソッド呼び出しをするだけに過ぎない。

.. csv-table::
   :delim: @
   :header: 関数, 機能
   :widths: auto

   ``plt.plot(...)``@グラフを描く
   ``plt.hist(...)``@ヒストグラムを描く
   ``plt.show(...)``@イメージを一気に表示
   ``plt.savefig(...)``@イメージをファイルに保存
   ``plt.setp(...)``@プロット線の属性等、描画パラメーターの取得・指定
   ``plt.axis(...)``@ビューポート範囲指定
   ``plt.grid(...)``@グリッド描画をするかしないか指定

IPython_ を利用している場合はおもむろに ``plt?`` とタイプするのもお勧めだ。
Matplotlib の概要がサインカーブのプロットを表示する簡素な例とともにコンソールに
出力する。

Figure と Axes の概念を理解する
======================================================================

Matplotlib には current figure と current axes という概念がある。これを利用し
て、複数個のグラフをワンシーンに定義できるようだ。

.. csv-table::
   :delim: @
   :header: 関数, 機能
   :widths: auto

   ``plt.figure(...)``@指定の figure をカレントにする
   ``plt.subplot(...)``@指定の axes をカレントにする

Figure
  大抵の本にはいくつかの図がしばしばキャプション付きで載っている。Figure という
  語は、それに対応するクラスだと解釈したい。図の一つ一つが Figure のオブジェクト
  になると思えば、個人的にはコードが理解できる。
Axes
  普通は一つの図にグラフ一つを載せるわけだが、同じようなグラフを並べたものを一つ
  の図としたい場合もある。 Axes という語が意味するのが、そのグラフだと解釈すれば
  よいか。

  余談だが MS Word のグラフ API にも Axes というコンセプトがあったと記憶してい
  る。

次の図にふたつの Axes を持たせたひとつの Figure を示す。

.. figure:: /_images/mpl-axes.png
   :align: center
   :alt: Axes デモ
   :width: 815px
   :height: 615px
   :scale: 50%

* ``plt.figure(n)`` で current figure を指定する。
* ``plt.subplot(n0n1n2)`` で current axes を指定する。``n0``, ``n1``, ``n2`` が
  それぞれ縦方向の区画数、横方向の区画数、「どの区画か」を意味する。

  ``n2`` は 1 以上 ``n1 * n2`` 以下の値でなければならない。

* ``plt`` のプロットコマンドはすべて current axes に作用する。

  .. code:: python3

     import matplotlib as mpl
     import matplotlib.pyplot as plt

     # Make figure-1 active and get it.
     fig = plt.figure(1)

     # Split the active figure into 2x1 (2 rows and 1 column)
     # and make axes-1 active.
     plt.subplot(211)

     # ...
     # All plotting commands here are applied to axes-1.

     # Split the active figure into 2x1
     # and make axes-2 active.
     plt.subplot(212)

     # ...
     # All plotting commands here are applied to axes-2.

* Matplotlib は figure/axes を扱うスタイルを二つ提供している。

  * 古典的なステートマシン様式

    ユーザーコードがカレントな figure/axes が何であるかを常に意識して、プロット
    コマンドを呼び出す。コマンドはカレントな figure/axes に対して適用されること
    になる。

  * 状態とオブジェクトとを関連付けて取り扱うオブジェクト指向プログラミング様式

    figure/axes がオブジェクトになっていて、メソッドでプロットコマンドを呼び出
    す。コマンドは対象となるオブジェクトの管理する figure/axes に対して適用され
    ることになる。

テキストを使う
======================================================================

当ノートの目的のひとつに、「数式を含むテキストを表示する」ことがある。そのために
は、事前に単純ななテキスト描画の方法を学習する必要があるだろう。モジュール
``plt`` からテキストに強く関連していそうな機能を表にしてみよう。

.. csv-table::
   :delim: @
   :header: 関数, 機能
   :widths: auto

   ``plt.text(...)``@ビューポート内にテキストを描く
   ``plt.xlabel(...)``@X 軸用キャプション
   ``plt.ylabel(...)``@Y 軸用キャプション
   ``plt.title(...)``@グラフ全体のキャプション

* ``plt.text()`` は指定位置にテキストを描画するコマンドと考える。

テキストプロパティ
----------------------------------------------------------------------

個人的によく使うテキストプロパティを表にまとめておく。各種テキストコマンド関数・
メソッドのキーワード引数として指定するのが一つのやり方。

.. csv-table::
   :delim: :
   :header: キーワード, 意味
   :widths: auto

   ``color``:テキストの色。
   ``family``:テキストのフォント名。フォント名を直接指定するか ``"sans-serif"`` 等の予約名を指定する。
   ``rotation``:テキストの流し込む角度。度単位で直接指定する。
   ``size``:フォントサイズをポイントで指定するか ``"x-large"`` 等の予約名を指定する。
   ``stretch``:0 から 1000 までの値を指定するか ``"condensed"`` 等の予約名を指定する。
   ``style``:``"normal"``, ``"italic"``, ``"oblique"`` から選択。
   ``weight``:0 から 1000 までの値を指定するか ``"bold"`` 等の予約名を指定する。

* テキストの基準位置は ``horizontalalignment``, ``verticalalignment`` キーワード
  引数で指示できる。例えば `x`, `y` 引数をテキストの右下位置としたい場合には次の
  ようにする：

  .. code:: python3

     plt.text(x, y, 'aaaa', verticalalignment='bottom', horizontalalignment='right')

* 複数行テキストの左揃え・中央揃え・右寄せを指定する場合は ``multialignment``
  キーワードを使用する。

日本語のテキストを描画する
----------------------------------------------------------------------

``matplotlib.font_manager.FontProperties`` を明示的に利用する手段を見つけた。

.. literalinclude:: /_sample/mpl/japanese_text.py
   :language: python3

結果のスクリーンショットは次のようなものだ。

.. figure:: /_images/mpl-fontprop.png
   :align: center
   :alt: 御無礼一発です
   :width: 815px
   :height: 615px
   :scale: 50%

ただしフォントパスをハードコードするような手法は可搬性がない。上記の技法を本番で
用いぬことだ。日本語の文字を恒常的に描画させるには、ユーザー設定ファイルでフォン
トを指定するのが自然だ。

* Cygwin ならファイル :file:`$HOME/.matplotlib/matplotlib` を、
* Linux ならファイル :file:`$HOME/.cache/matplotlib/matplotlib`

を開いて次の項目に日本語に対応したフォントを指定することだ：

* ``font.family``
* ``font.sans-serif``: 先頭に加える。

なお、設定ファイルのパスは環境設定のノートで述べるような仕組みで決定されるもの
だ。それは関数 ``mpl.matplotlib_fname`` に対する ``help`` で確認できる。

Artists 関連
======================================================================

* primitives: ``Line2D``, ``Rectangle``, ``Text``, ``AxesImage``, etc.
* containers: ``Axis``, ``Axes``, ``Figure``, etc.

コンテナーを攻略していく。

* ``Axes`` はプロッティングエリア。
* ``Subplot`` は ``Axes`` の特別なもの。コード的にもサブクラスで表現されている。
* ``Patch`` というクラス名は MATLAB から受け継いだ。

* プロパティー一覧は ``matplotlib.artist.getp`` 関数で確認できる。

``Figure`` (``matplotlib.figure.Figure``)
----------------------------------------------------------------------

* ``Figure`` オブジェクトが "current axes" を管理している。
* ``Figure`` は（グラフのものではない）自身の座標系を持っていて、矩形の左下と右
  上がそれぞれ ``(0, 0)``, ``(1, 1)`` となっている。

  変な例だが、画像全体に対角線を一本引くにはこうする。キーワード引数
  ``transform`` の値がいかにもな感じがするだろう。

  .. literalinclude:: /_sample/mpl/diagonal.py
     :language: python3

  結果は次のスクリーンショットのようなものとなる：

  .. figure:: /_images/mpl-figcs.png
     :align: center
     :alt: 対角線
     :width: 815px
     :height: 615px
     :scale: 50%

``Axes`` (``matplotlib.axes.Axes``)
----------------------------------------------------------------------

``Axes`` オブジェクトが図形・テキスト・目盛・グリッド・ラベル各オブジェクトを管
理する。まずコンテナーメンバーのうち、馴染みのあるものだけ表にまとめておく。

.. csv-table::
   :delim: @
   :header: メンバー名, 内容物
   :widths: auto

   ``lines``@ ``plot`` 等で作成した ``Line2D`` オブジェクト。
   ``patches``@ 各種 ``Patch`` オブジェクト。``Ellipse``, ``Polygon``, etc.
   ``texts``@ ``text`` や ``annotate`` で作成した各種テキスト。

非コンテナーメンバーも少しだけ押さえておく。

.. csv-table::
   :delim: @
   :header: メンバー名, オブジェクト
   :widths: auto

   ``patch`` @ ``Axes`` の背景用 ``Rectangle`` オブジェクト。
   ``xaxis`` @ ``XAxis`` オブジェクト。
   ``yaxis`` @ ``YAxis`` オブジェクト。

``Axis`` (``matplotlib.axis.Axis``)
----------------------------------------------------------------------

グラフの目盛、グリッド、目盛に付けるラベル等を管理する。``Axes`` オブジェクトの
``xaxis`` および ``yaxis`` メンバーでアクセスできる。

使用頻度の高いものだけ表にしておく。

.. csv-table::
   :delim: @
   :header: メソッド, 機能
   :widths: auto

   ``get_major_ticks`` @ 目盛 (``matplotlib.ticker.Ticker``) オブジェクトを返す。
   ``grid`` @ グリッド線を描画するしないを指示。

.. code:: python3

   import matplotlib.pyplot as plt
   ax = plt.gca()

   # Modify the tickers for Y axis.
   for tick in ax.yaxis.get_major_ticks():
       tick.tick1On = False   # Hide tickers on left side.
       tick.tick2On = True    # Show tickers on right side.
       tick.label1On = False  # Hide labels on left side.
       tick.label2On = True   # Show labels on right side.

バックエンド
======================================================================

バックエンドとは、グラフを何が何へ出力するのかを指す概念であると思う。これは公式
のドキュメントの記述が完璧なので、何か気になることができたら、素直にそちらを当た
るのがよい。

ユーザーインターフェイスバックエンドとハードコピーバックエンドの二種類があり、前
者はウィンドウ、後者はファイル形式とおおまかに考えられる。それぞれ
``plt.show()`` と ``plt.savefig()`` の振る舞いに影響する。

ここではコードでのバックエンド設定方法を述べる。設定ファイルによる設定方法は
:doc:`config` を参照。

ユーザーインターフェイスバックエンド
----------------------------------------------------------------------

例えば PyQt5 の UI でグラフをウィンドウに表示する場合、次のようにするとそうな
る。

.. code:: python3

   import matplotlib as mpl
   mpl.use('Qt5Agg')

なお ``mpl.use`` 関数を呼び出すタイミングは、最初の ``import matplotlib`` の直後
がベストのようだ。IPython_ のセッションであらかじめ ``matplotlib.plt`` 等がイン
ポートされていて、同関数が呼び出せない状況に陥っているというのがありがちだ。

上記のコードが機能するには、環境に PyQt5 がインストール済みである必要がある。
:doc:`/python-pyqt5` 参照。

.. figure:: /_images/mpl-qt5agg.png
   :align: center
   :alt: Qt5Agg
   :width: 648px
   :height: 559px
   :scale: 50%

ハードコピーバックエンド
----------------------------------------------------------------------

ハードコピーバックエンドのカスタマイズはこのノートの目的の一つ。``backend`` の値
を ``PS``, ``PDF``, ``PNG``, ``SVG`` のどれかにしておくと、その名前の形式のファ
イルを作成することができる。コードで実現するには、次のような手順にしておけばよ
い。

.. code:: python3

   import matplotlib as mpl
   mpl.use('PDF')  # We want the image as PDF file.

   # ... Here come plotting commands.

   plt.savefig('output')  # File output.pdf will be saved.

ヒストグラムを描く
======================================================================

ノートを整理していたら未使用のスクリプトを発見したので、説明なしにここにコードを
記す。

.. literalinclude:: /_sample/mpl/histogram.py
   :language: python3

最終的な描画結果は次のようなものとなる。乱数次第で分布が変化するので注意。

.. figure:: /_images/mpl-histogram.png
   :align: center
   :alt: ヒストグラム
   :width: 815px
   :height: 615px
   :scale: 50%

曲線を描く
======================================================================

曲線とは言っても実際は折れ線だ。

多項式
----------------------------------------------------------------------

実数 :math:`x` の多項式 :math:`f(x)` について :math:`y = f(x)` のグラフを描きた
い。次の容量で曲線を定義する。

#. プロットする :math:`x` のサンプル点を関数 ``numpy.arange`` で適宜準備する。や
   り方を忘れていたら :doc:`/python-numpy/index` を参照。
#. 多項式 :math:`f` を関数 ``numpy.poly1d`` の戻り値で表現する。
#. 評価する変数を関数 ``np.linspace`` で用意する。
#. プロットする値を ``np.array`` オブジェクトに対する broadcasting を利用して一
   気に得る。

なお、サンプルコードではさらに曲線に対して接線を引いた。``f`` の一次導関数を
``f.deriv()`` で得られることを利用する。

.. literalinclude:: /_sample/mpl/polynomial.py
   :language: python3

描画結果は次のようなものとなる。

.. figure:: /_images/mpl-polynomial.png
   :align: center
   :alt: 多項式をプロット
   :width: 815px
   :height: 615px
   :scale: 50%

Bézier 曲線
----------------------------------------------------------------------

本当は B-Spline 曲線を描画したいのだが、調べてみると Matplotlib では Bézier 曲線
が限界のようだ。

手順はこういう感じのようだ：

#. クラス ``matplotlib.path.Path`` のオブジェクトを作成する。この引数とし
   て、Bézier 曲線の制御点リストと「打点命令」のリストを渡す。
#. そのパスオブジェクトを引数として、クラス ``matplotlib.patches.PathPatch`` の
   オブジェクトを作成する。
#. そのパッチオブジェクトを対象の ``axes`` オブジェクトに ``add_patch`` する。

Matplotlib は制御点列を与えて Bézier 曲線を定義する流儀のようだ。

まずは簡単な例を。最小の手間で二次の Bézier 曲線（単なる放物線）を定義することを
考える。``CURVE3`` というタイプの曲線は、制御点を三つ与えることで二次の Bézier
曲線を表現できる。``CURVE3`` ベースの Bézier 曲線の特徴は次のとおり：

* 最初と最後の制御点は、放物線の始点と終点にそれぞれ一致する。
* 中間の制御点は、放物線の両端点それぞれの接線の交点と一致する。
* よって、出来上がりの曲線形状が把握できる。

``Path`` オブジェクト構築は次のようになる：

.. literalinclude:: /_sample/mpl/bezier.py
   :language: python3
   :lines: 1-25

もうひとつ例を。ドロー系アプリでもよく見かける 3 次の Bézier 曲線を定義する。

* ``CURVE4`` 命令で制御点を指示する。
* 最初と最後の制御点は、曲線の始点と終点にそれぞれ一致する。
* 最初の制御点とその次の制御点を結ぶ直線が、曲線の始点での接線に一致する。また、
  最後の制御点とその前の制御点を結ぶ直線が、曲線の終点での接線に一致する。
* 曲線全体は、制御点列からなる多角形の内部に位置する。

``Path`` オブジェクト構築は次のようになる：

.. literalinclude:: /_sample/mpl/bezier.py
   :language: python3
   :lines: 27-

最終的な描画結果は次のようなものとなる：

.. figure:: /_images/mpl-bezier.png
   :align: center
   :alt: Bézier 曲線をプロット
   :width: 815px
   :height: 615px
   :scale: 50%

.. include:: /_include/python-refs-sci.txt
