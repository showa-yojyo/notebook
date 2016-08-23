======================================================================
見本コードを研究する
======================================================================
Matplotlib を手足のように使いこなせるようになるには、
相当時間を要すると前書きで述べた。
ここでは、習うより慣れろの精神で Matplotlib_ ドキュメント内の
`見本コード集 <http://matplotlib.org/examples/>`__ から
いろいろと吸収することを考えてみよう。

.. contents:: ノート目次
   :depth: 3

コードを収集する
======================================================================
公式サイトに付属している見本集の本数は 400 を軽く超える。
これらをブラウザーで閲覧しながら、一個一個の見本コードのページを見ていくのは効率が悪い。
研究に本腰を入れるのならば、これら全てをあらかじめローカルにダウンロードしておくべきだろう。
その方法としては次のどちらかを挙げたい。

* 素直に Matplotlib のリポジトリーを :code:`git clone` してから、
  :file:`examples` ディレクトリーにあるコードにアクセスする。

* とにかく見本コードだけが手許にあれば十分なので、
  :file:`examples` ディレクトリーしかダウンロードせずに済ませる。

PC のディスク残量とインターネットの接続環境に不満がないか、
あるいは既に GitHub にあるリポジトリーのクローンを :code:`pip install -e` していて、
そのソースコードをそのまま利用中であるならば、前者の方法で問題はない。

.. code-block:: console

   $ git clone https://github.com/matplotlib/matplotlib.git
   $ cd matplotlib/examples

そうではなく、資源が乏しかったり、
もうパッケージがあるのにクローンなど作成したくないのであれば、
必要な分だけをダウンロードするだけで済ませる。

Git リポジトリーの特定のディレクトリーのスナップショットを得るのに
古の VCS ツールである :program:`svn` が利用できる。

.. code-block:: console

   $ svn export https://github.com/matplotlib/matplotlib.git/trunk/examples
   $ mv examples mpl-examples
   $ cd mpl-examples

コードを実行する
======================================================================
コマンドプロンプトから実行するか、または IPython のコマンド :code:`%run` を使うことで
見本スクリプトの挙動を確認することができる。
後者の方法のほうがわずかに効率が良い？

後述する、開発陣が利用しているであろう :file:`tests/backend_driver.py` も有用である。

稼働ノート
======================================================================
本節では評者が :file:`examples` にある見本コードを実際に実行した感想を記す。
見本の目的はサブディレクトリーを用いて分類されているので、
本節をそれらに対応した単位に分割して、コードの寸評を述べる。

:file:`animation`
----------------------------------------------------------------------
クラス :code:`matplotlib.animation.FuncAnimation` を利用するコードで構成された見本集。
MPEG ファイルを保存するコードが動かないのが残念だ。

:file:`animate_decay.py`
  動的に減衰波形がプロットされる。

:file:`basic_example.py`
  まず色彩豊かな何かのアニメーションがあり、次に折れ線のアニメーションとなる。
  FuncAnimation と ArtistAnimation を別々に使用。

:file:`basic_example_writer.py`
  先ほどのアニメーションをファイルに出力する見本コードのようだが、
  :code:`animation.writers['ffmpeg']` の処理で実行時例外が発生する。

:file:`bayes_update.py`
  ベータ分布の確率密度関数曲線のプロットのアニメーション例。

  * SciPy_ が必要。
  * メソッド :code:`Axes.axvline` の使い方も習える。

:file:`double_pendulum_animated.py`
  振り子の付いた振り子のアニメーション。肘みたいな動きをする。

  * SciPy_ が必要。常微分方程式を一度解く。

:file:`dynamic_image.py`
  幻想的な色のアニメーション。

  * 関数 :code:`matplotlib.pyplot.imshow` を併用する。

:file:`dynamic_image2.py`
  幻想的な色のアニメーション。上の物と酷似。

  * たまにホワイトアウトするのは :code:`repeat_delay` によるものか。
  * FuncAnimation の代わりに ArtistAnimation を利用する。

:file:`histogram.py`
  ヒストグラムのアニメーション。各ビンの数値が変動する。

  * ヒストグラム本体よりもパスを構成するほうに労力を割いている。
    配列のスライスの活用が素晴らしい。

:file:`moviewriter.py`
  例によって :code:`animation.writers['ffmpeg']` の処理で実行時例外が発生する。

:file:`rain.py`
  雨の降っている地面を眺めているかのようなアニメーション。

  * 乱数は NumPy_ の :code:`np.random.uniform` を利用している。
  * 散布図 (:code:`Axes.scatter`) を応用している。

:file:`random_data.py`
  区分的一次関数のアニメーション。区間以外が動的に変動する。

  * この中でもっとも単純なコードからなる。
  * 乱数は NumPy_ の :code:`np.random.rand` を利用している。

:file:`simple_3danim.py`
  空間の一部に含まれるいくつかの点のブラウン運動のようなアニメーション。

  * モジュール :code:`mpl_toolkits.mplot3d.axes3d` を利用する。
  * モデル部分は 3D データとなり専用のメソッド等を用いる必要があるが、
    アニメーション部分は 2D だろうが 3D だろうがやることは変わらない。

:file:`simple_anim.py`
  三角関数のプロットのアニメーション。位相が動的に変動する。

  * 関数 code:`np.ma.array` を用いれば、
    欠損要素を含んでもよい配列オブジェクトを生成できる。

:file:`strip_chart_demo.py`
  心電図のようなプロットのアニメーション。

  * 与えられた確率をしきい値として、乱数値またはゼロを評価する関数を
    構成するところにこのアニメーションの独創性がある。

:file:`subplots.py`
  複数サブプロットがいっせいにアニメーション。

  * クラス :code:`matplotlib.animation.TimedAnimation` のサブクラスを
    実装してもよいことを示してもいる。

  * やはり :code:`Figure.add_subplot` は使いこなすのが難しい。

:file:`unchained.py`
  モダンアート。

:file:`api`
----------------------------------------------------------------------
.. todo:: 調査する。

:file:`axes_grid1`
----------------------------------------------------------------------
モジュール :code:`mpl_toolkits.axes_grid1` に関連する見本の集まり。

.. todo:: 調査する。

:file:`axisartist`
----------------------------------------------------------------------
モジュール :code:`mpl_toolkits.axisartist` に関連する見本の集まり。

.. todo:: 調査する。

:file:`color`
----------------------------------------------------------------------
色に関係する処理の見本集。

:file:`colormaps_reference.py`
  ``Colormap Vega10 is not recognized`` というエラーが出て完全には動作しない。

  * 動作するものについては、色見本が画面に描かれる。

:file:`color_cycle_default.py`
  現在存在しない :code:`set_facecolor` への参照があるコード。動作しない。

:file:`color_cycle_demo.py`
  RGBY と CMYK とでプロット曲線の色を変えていくデモ。

  * 関数 :code:`plt.rc` の呼び出しでプロット曲線の特性を指定することができる。
  * またはメソッド :code:`Axes.set_prop_cycle` を用いてもよい。

:file:`named_colors.py`
  現在存在しない :code:`BASE_COLORS` への参照があるコード。動作しない。

:file:`event_handling`
----------------------------------------------------------------------
キーボードやマウス操作による対話的な処理をどう実現するかを示す見本集。

.. todo:: 調査する。

:file:`images_contours_and_fields`
----------------------------------------------------------------------

.. todo:: 調査する。

:file:`lines_bars_and_markers`
----------------------------------------------------------------------

.. todo:: 調査する。

:file:`misc`
----------------------------------------------------------------------
雑多なコード例を集積したディレクトリーだろう。

.. todo:: 調査する。

:file:`mplot3d`
----------------------------------------------------------------------
立体的なモデルをウィンドウ上で表現する方法を示す見本集。

.. todo:: 調査する。

:file:`pie_and_polar_charts`
----------------------------------------------------------------------
円グラフと極座標グラフの見本コード集。

:file:`pie_demo_features.py`
  よくある円グラフの見本。

  * 円グラフはメソッド :code:`Axes.pie` で実現する。
  * :code:`Axes.set_aspect('equal')` をしないと、円が円に見えなくなる。
  * 扇型は既定では反時計回りに配列されていく。この振る舞いを変える方法もある。

:file:`polar_bar_demo.py`
  極座標系の中心から棒が伸びるようなグラフの見本。棒というか扇型になる。

  * これは :code:`plt.subplot` の呼び出し時に :code:`projection='polar'` を指定するのが本質的だ。
  * 謎のメソッド :code:`plt.cm.viridis` で「棒」部分の色を決めている。
    これは色の見本コード集のところで学習しよう。

:file:`polar_scatter_demo.py`
  極座標グラフで散布図を実現する見本。

  * これも :code:`plt.subplot` の呼び出し時に :code:`projection='polar'` を指定する。
  * 散布図を実現するのはメソッド :code:`Axes.scatter` だ。
  * サンプルデータは乱数。

:file:`pylab_examples`
----------------------------------------------------------------------

.. todo:: 調査する。

:file:`scales`
----------------------------------------------------------------------
グラフの各軸の目盛寸法を線形的だけではなく、対数的にも設定できる。
詳しくは :code:`matplotlib.pyplot.Axes.set_yscale` 等のヘルプを当たって欲しい。

:file:`scales.py`
  それぞれ異なる Y 軸の目盛寸法の特性のあるサブプロットを 4 つ描画し、
  同一データをプロットする。

  * 寸法の種類は ``linear``, ``log``, ``symlog``, ``logit`` からなる。
    ``symlog`` はプラスマイナス対称であり、
    ``logit`` はクリッピングあり。

  * プロットデータは Gauss 分布 :code:`np.random.normal(0.5, 0.4, 1000)` を
    加工したものとする。これでほぼ線形に分布した点列が得られる。
    この加工の技法にも注目したい。

:file:`shapes_and_collections`
----------------------------------------------------------------------
:file:`artist_reference.py`
  Matplotlib の各種図表要素 (artists) の図解のようなものを描く見本コード。

  * モジュール :code:`mpl.patches` には Circle, Rectangle, Wedge,
    RegularPolygon, Ellipse, Arrow, FancyBboxPatch という図表的要素クラスがある。

  * PatchCollection というクラスでこれらの要素を集約することができる。

  * レイアウトを微調整する関数 :code:`plt.subplots_adjust` を忘れないでおきたい。

:file:`path_patch_demo.py`
  区分的 Bézier 曲線の構成方法の見本。
  :code:`mpl.path.Path`, :code:`mpl.path.PathPatch` の利用法が理解できる。

:file:`scatter_demo.py`
  散布図の見本。

  * この見本コードが散布図を描画するもっとも単純なものだろう。
  * 与える点列データは座標だけでなく大きさと色も指定することができる。
  * 関数 :code:`plt.scatter` による。

:file:`showcase`
----------------------------------------------------------------------
書籍に掲載されていても遜色のないイラスト群。

:file:`bachelors_degrees_by_gender.py`
  アメリカ合衆国における女性の専攻別学位授与率のプロット。

  * 見るべきところは多々あるが、とりわけ目を引くのはサンプルデータの出処である。
    関数 :code:`matplotlib.cbook.get_sample_data` は面白そうだ。

:file:`integral_demo.py`
  典型的な定積分のイラスト。

  * 関数 code:`plt.text` 等 LaTeX 数式を指定できることは学習済み。
  * 求積領域の形状を Polygon を用いて表現する。

:file:`xkcd.py`
  謎のスケッチスタイル適用。

  * 棒グラフはメソッド :code:`Axes.bar` で描画する。

:file:`specialty_plots`
----------------------------------------------------------------------
シェーディング（のようなもの）が関係する画像を生成する見本コード集。

:file:`advanced_hillshading.py`
  3 種類の異なるデモを含むコード。

  * :code:`plt.cm.cupper` という銅の色みを扱うオブジェクトがある。
  * モジュール :code:`mpl.colors` にあるクラス LightSource のオブジェクトが
    メソッド :code:`shade` で色の数値を評価する。
  * メソッド :code:`Figure.colorbar` が色の棒をサブプロットの側に配置する。
  * モジュール :code:`mpl.colors` にあるクラス Normalize のオブジェクトは
    与えらえた数値を指定範囲内に制限する。

:file:`hinton_demo.py`
  Hinton 図のデモコード。
  白と黒でさまざまな大きさの正方形を格子上に描画する。

  * これは面白いから Matplotlib 本体に組み込んでもよいのでは。
  * 関数 :code:`np.ndenumerate` は馴染みがなかった。いつか活用したい。

:file:`topographic_hillshading.py`
  航空写真にありがちな地形に陰影を付けてプロット？するデモコード。

  * LightSource にそのものズバリのメソッド :code:`hillshade` がある。
    この戻り値を :code:`Axes.imshow` に引き渡す。

  * exaggregate (v.): 「誇張する」の意。

:file:`statistics`
----------------------------------------------------------------------

.. todo:: 調査する。

:file:`style_sheets`
----------------------------------------------------------------------
モジュール :code:`mpl.pyplot.style` の見本コード集。

:file:`plot_bmh.py`
  ヒストグラム重ねあわせ。

  * :code:`plt.style.use('bmh')` を適用。
    これは `Bayesian Methods for Hackers` という書籍で用いられているテーマだそうだ。

  * 無意味なデータを生成するのに :code:`np.random.beta` を利用。

:file:`plot_dark_background.py`
  プロットの背景を黒くするだけのデモ。

  * 単に :code:`plt.style.use('dark_background')` するだけで実現できる。
    このとき、通常は黒塗りで描画される図表要素は白色で描画される。

:file:`plot_fivethirtyeight.py`
  特に変わったことはない？

  * :code:`plt.style.context('fivethirtyeight')` を適用。
    この際に with ブロックを用いる。

:file:`plot_ggplot.py`
  サブプロット 4 個

  * スタイルを `R <Bayesian Methods for Hackers>`__ の一般的なパッケージである ggplot 風にするのに
    :code:`plt.style.use('ggplot')` とする。

  * スクリプトの docstring の文言が笑える。いちおう許可は取ってあるのか。
  * 無意味なデータを生成するのに :code:`np.random.normal` と
    :code:`np.random.randint` を利用。

:file:`plot_grayscale.py`
  サブプロット 2 個でグレースケール。

  * :code:`plt.style.use('grayscale')` でよい。

:file:`subplots_axes_and_figures`
----------------------------------------------------------------------
:file:`fahrenheit_celsius_scales.py`
  一つのサブプロットに二種類の目盛を割り当てる見本。

  * メソッド :code:`Axes.twinx` でもう一つの Axes を生成する。
    これと元の Axes を使い分けて華氏と摂氏の目盛を左右の Y 軸に描画する。

  * メソッド :code:`Axes.callbacks.connect` の呼び出しは何だろう。

:file:`subplot_demo.py`
  サブプロットを 2 個同一ウィンドウに描画する見本。

  * ここでは関数 :code:`plt.subplot` を `(nrows, ncols, plot_number)` 形式で呼び出す。
    オブジェクト指向的ではなく、
    状態機械的な手続きで各サブプロットの特性を操作する。

:file:`tests`
----------------------------------------------------------------------
:file:`backend_driver.py`
  見本ディレクトリー配下にあるかなりの数の見本スクリプトを、
  コマンドラインから指定されたバックエンドを用いて実行するためのスクリプトである。

  IPython セッションからの実行例を次に示そう。途中で :kbd:`Ctrl-C` して中断した。

  .. code-block:: ipython

     In [1]: %run ./backend_driver.py -bqt5agg
      ..\pylab_examples files not tested: agg_buffer.py, agg_buffer_to_array.py, ...
      ..\api files not tested: compound_path.py, demo_affine_image.py, ...
      ..\units files not tested: artist_tests.py, bar_unit_demo.py, basic_units.py, ...
      ..\mplot3d files not tested: contour3d_demo3.py, contourf3d_demo2.py, ...
      testing qt5agg
           driving ..\pylab_examples\accented_text.py
      9.067790508270264 0
              driving ..\pylab_examples\alignment_test.py
      QObject::~QObject: Timers cannot be stopped from another thread

  * コマンドラインオプション :code:`-b` でバックエンドを指定できる。
  * コマンドラインオプション :code:`-d` でテスト対象とするサブディレクトリーを指定できる。
    ただし、一部のディレクトリーにはサンプルコードの漏れがあると思われる。

:file:`text_labels_and_annotations`
----------------------------------------------------------------------
:file:`autowrap_demo.py`
  関数 :code:`plt.text` のデモ。

  * この関数のキーワード引数はクラス Text の特性と対応している。
    例えば、キーワード引数 :code:`wrap=True` と指定することで、
    長いテキストを自動的に折り返してくれる。

:file:`rainbow_text.py`
  テキストの部分だけを着色するデモ。かなりの工夫をすることになるようだ。

  * :code:`mpl.transforms.offset_copy` なる関数までも動員する。

:file:`text_demo_fontdict.py`
  テキストを入力とする Matplotlib の各種関数には
  キーワード引数 ``fontdict`` があり、
  利用するフォントの各情報を dict オブジェクトに詰め込める。

:file:`unicode_demo.py`
  テキストを入力とする Matplotlib の各種関数は Unicode を当然のように受け付ける。

:file:`ticks_and_spines`
----------------------------------------------------------------------
:file:`spines_demo.py`
  Axes は既定で四辺すべてに枠線が引かれるが、これを辺ごとに設定できることを示すデモ。

  * 私の見たところ :code:`ax1.spines['top'].set_visible(False)` が効いていない。

:file:`spines_demo_bounds.py`
  さらに辺の一部だけに枠線を引くこともできる。

  * :code:`ax.spines['left'].set_bounds(-1, 1)` がそれを実現する。

:file:`spines_demo_dropped.py`
  Axes の枠線を既定の位置からオフセットするようにずらすやり方を示すデモ。

  * :code:`ax.spines['left'].set_position(('outward', 10))` のようにする。
  * プロット用ダミーデータとして乱数 :code:`np.random.uniform` を利用。

:file:`ticklabels_demo_rotation.py`
  目盛のラベル文字を決めるデモ。

  * メソッド :code:`Axis.set_major_formatter` 等を使う。
    さらにクラス FuncFormatter の利用と自作の書式設定関数の作成が必要となる。

  * メソッド :code:`Axis.set_major_locator` で目盛ラベルの出現に制約をつける。

:file:`tick_labels_from_values.py`
  目盛のラベルを決めるデモ。

  * 関数 :code:`plt.xticks` の 2 番目の引数として、
    ラベル文字列からなる list オブジェクトを引き渡すことで指定できる。

:file:`units`
----------------------------------------------------------------------

.. todo:: 調査する。

:file:`user_interfaces`
----------------------------------------------------------------------

.. todo:: 調査する。

:file:`widgets`
----------------------------------------------------------------------

.. todo:: 調査する。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
