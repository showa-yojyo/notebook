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

:file:`demo_axes_divider.py`
  複数サブプロット、カラーバーの配置方法のデモ。

  * デモコード定義の関数 :code:`get_demo_image` はプロット対象となるデータを
    NumPy の配列オブジェクトとして返す。
    この関数は他のデモコードでも登場する。

  * 最初のサブプロットでは単にデモデータを描画する。
    メソッド :code:`Axes.imshow` でイメージを描画し、
    さらに関数 :code:`plt.colorbar` でカラーバーを付属させる。

  * 次のサブプロットでは、先の処理をより複雑にすることで
    カラーバーの高さをイメージプロットのそれに合わせる。
    クラス SubplotDivider, LocatableAxes, Size と
    メソッド :code:`Figure.add_axes` を使いこなす力量を要求される。

  * 次のサブプロットもやることは同じだが、手続きが簡略化した。
    関数 `make_axes_locatable` をサブプロットに適用して
    レイアウトマネージャーのようなものを利用する。

  * 最後のサブプロットは同じイメージプロットを横一列に並べる。
    つまり、先の例でカラーバーの代わりに元のイメージプロットと同じものを置く。

:file:`demo_axes_grid.py`
  さらに複雑な複数サブプロットの配置方法のデモ。

  * 最初のサブプロット群は田の字に配置するもの。
    クラス ImageGrid に Figure オブジェクトを渡す。

  * 次のサブプロット群も田の字だが、カラーバーをひとつ付属させる。
    横長カラーバーが田の字の上部に出る。
    ImageGrid コンストラクターの後半のキーワード引数がそれを指示する。

  * 次のサブプロット群も田の字だが、カラーバーがそれぞれに付属する。
    ImageGrid の :code:`cbar_mode="each"` がポイントだ。

  * 最後のサブプロット群も田の字。カラーバーも個別。
    ただしカラーバーの範囲をサブプロットごとに変える。

:file:`demo_axes_grid2.py`
  ImageGrid のデモコード。

  * 最初のグループはサブプロットそれぞれにカラーバーを付属させる。
    ImageGrid の引数については以前のデモで理解できるだろう。

  * デモコード定義の関数 :code:`add_inner_title` はサブプロット内にテキストを配置する。
    主にクラス AnchoredText を利用するが、それ以外の機能はあまり馴染みがない。

  * 次のグループはサブプロットにひとつのカラーバーを共有させる。
    ImageGrid の :code:`cbar_mode="single"` がポイントだ。

:file:`demo_axes_hbox_divider.py`
  サブプロットを並べて、それにまたがるようにテキストを入れるデモ？

  * モジュール :code:`mpl_toolkits.axes_grid1.axes_size` にあるクラス
    AxesX, AxesY, Scaled, Fixed を利用してレイアウトマネージャー的な役割がある
    クラス HBoxDivider のオブジェクトを生成する。
    このマネージャーを最初に作った Axes のいずれにも :code:`set_axes_locator` する。

  * テキスト部は実は Axes オブジェクト。
    メソッド :code:`Axes.annotate` でテキスト内容とレイアウト内容を指定する。

:file:`demo_axes_rgb.py`
  モジュール :code:`mpl_toolkits.axes_grid1.axes_rgb` を利用したサブプロットの RGB 分解のデモ。

  * 関数 :code:`make_rgb_axes` でサブプロットから RGB 別のサブプロットを生成する。

  * デモコード内で定義された、画像から RGB 値を分解するコードの処理内容が理解できない。
    謎のスライス。

  * クラス RGBAxes で Figure からサブプロットを内部に 4 つ持つサブプロットを生成する
    サブプロットそれぞれには :code:`.RGB`, :code:`.R`, :code:`.G`, :code:`.B` でアクセスする。

  * この場合にはメソッド :code:`Axes.imshow_rgb` で描画内容生成。

:file:`demo_colorbar_with_inset_locator.py`
  カラーバーを関数 :code:`mpl_toolkits.axes_grid1.inset_locator.inset_axes` で実現するデモ。

  * 関数 :code:`inset_axes` で既存のサブプロットの内側に指定サイズの
    新規サブプロットを作成する。
    それから :code:`plt.colorbar` のキーワード引数 ``cax`` としてそれを指定する。

:file:`demo_edge_colorbar.py`
  クラス AxesGrid のデモ。

  * 最初のグループではカラーバーを 2 個ずつ共有するデモ。下に付く。
    クラス AxesGrid を ImageGrid のように使うが、
    キーワード引数 :code:`cbar_mode="edge"` がポイント。

  * 次のグループではカラーバーを 2 個ずつ共有するデモ。右に付く。

  * ところで :code:`plt.get_cmap("autumn")` 等が気になる。

:file:`demo_imagegrid_aspect.py`
  クラス ImageGrid のデモ。

  * コンストラクターの引数 :code:`aspect=True` でアスペクト比を指定可能な
    オブジェクトを作成することを指示する？

  * アスペクト比自体は :code:`set_aspect` を用いる。

:file:`inset_locator_demo.py`
  モジュール :code:`mpl_toolkits.axes_grid1.inset_locator` のデモ。
  サブプロット内に別のサブプロットを入れる？

  * 関数 :code:`zoomed_inset_axes` で既存のサブプロットから指定倍率を持つ
    新規サブプロットを作成する。

:file:`inset_locator_demo2.py`
  モジュール :code:`mpl_toolkits.axes_grid1.inset_locator` のデモ。
  サブプロット内の一部を拡大して表示する。

  * 関数 :code:`mark_inset` でこれらのサブプロットの位置関係を指定する。

:file:`make_room_for_ylabel_using_axesgrid.py`
  関数 :code:`mpl_toolkits.axes_grid1.axes_divider.make_axes_area_auto_adjustable` その他のデモ。
  サブプロットのマージン？の大きさを自動調整可能にする？

:file:`parasite_simple2.py`
  クラス SubplotHost のデモ？

  * SubplotHost のコンストラクターに Figure オブジェクトと寸法を指定する。
  * あとは何をやりたいのかわからない。

:file:`scatter_hist.py`
  関数 :code:`mpl_toolkits.axes_grid1.make_axes_locatable` のデモ。
  ヒストグラム 2 個と散布図 1 個をウィンドウに表示する。

  * まずは単に散布図を定義し、それを引数にして :code:`make_axes_locatable` を呼ぶ。
    この戻り値オブジェクトのメソッド :code:`append_axes` を呼び出して、
    散布図の上や右に新しくサブプロットを作成する。

  * 棒が横に伸びるヒストグラムを作るには
    :code:`hist` の引数に :code:`orientation='horizontal'` を指定する。

:file:`simple_anchored_artists.py`
  各種図形、特にモジュール :code:`mpl_toolkits.axes_grid1.anchored_artists` にある
  図形要素をサブプロットに配置するデモ。

  * クラス AnchoredText は小さいテキストラベル。
  * クラス AnchoredDrawingArea はサブプロット内の小さな矩形。
    コンテナーとして振る舞う。
    この例では Circle を別途作成し、自身の管理する :code:`add_artist` により含める。
  * クラス AnchoredEllipse はサブプロットに所属する小さな楕円。
  * クラス AnchoredSizeBar はサブプロットに所属する「縮尺を表す線」。

  * 上記のクラスはすべて AnchoredOffsetBox の間接サブクラスである。
    オブジェクトはどれも :code:`Axes.add_artist` に渡すことになる。

:file:`simple_axesgrid.py`
  クラス ImageGrid のデモ。

  * ImageGrid のコンストラクターに Figure オブジェクトと格子の寸法を指定する。
  * ここでは適当に定義した線形データを :code:`imshow` に渡している。

:file:`simple_axesgrid2.py`
  同じくクラス ImageGrid のデモ。
  画像を 3 分割してそれぞれを 3 つの格子それぞれに描画する。

  * ImageGrid の引数で格子間の長さを指定する等する。
  * 画像の分割は単に NumPy の配列をスライスするだけで得られる。

:file:`simple_axisline4.py`
  座標軸の目盛ラベルデモ。
  サブプロットにサインカーブを描き、上辺は円周率単位で、下辺は 1 単位で目盛を付ける。

  * メソッド :code:`Axes.twin` でサブプロット上辺の座標軸を
    表すオブジェクトが得られるので、
    これに対して :code:`set_xticks`, :code:`set_xticklabels` を操作する。

:file:`axisartist`
----------------------------------------------------------------------
モジュール :code:`mpl_toolkits.axisartist` に関連する見本の集まり。

:file:`demo_axisline_style.py`
  プロットの座標軸と枠線の処理方法についての見本。

  * クラス SubplotZero は図の内部にある Axes オブジェクトを生成・操作するメソッドを与える。
    この見本ではオブジェクト :code:`fig` から生成する。

  * 両座標軸ともに正の方向に矢印の矢先を描くために :code:`ax.axis[direction].set_axisline_style("-|>")` する。

:file:`demo_curvelinear_grid.py`
  クラス Subplot, SubplotHost, GridHelperCurveLinear, ParasiteAxesAuxTrans の見本。
  直交座標のプロットと極座標のプロットを描いて、
  それぞれにおいてグリッドや目盛をカスタマイズする。

  * かなり手が込んでいる。

:file:`demo_curvelinear_grid2.py`
  x 軸の目盛間隔が一様でないデモ？

  * 先ほどの見本もそうだが、クラス GridHelperCurveLinear の操作法が面倒そうだ。

:file:`demo_floating_axes.py`
  サブモジュール :code:`mpl_toolkits.axisartist.floating_axes` デモ。
  3 個のサブプロットを生成する。

  * サブプロット全体に affine 変換を施すことができる。
    それにはクラス Affine2D のオブジェクトを生成して適切な変換を定義しておく必要がある。
    それから別のオブジェクトに引き渡す。

  * 直交座標系の棒グラフでは
    :code:`floating_axes.GridHelperCurveLinear` と
    :code:`floating_axes.FloatingSubplot` を上手く使う。

  * バウムクーヘンのような極座標系の散布図では
    FixedLocator, DictFormatter, MaxNLocator の各クラスを利用して、
    座標軸の目盛ラベルをカスタマイズする。

  * 扇型の極座標系の散布図では
    モジュール :code:`mpl_toolkits.axisartist.angle_helper` の機能を上手く使う。

:file:`demo_floating_axis.py`
  極座標？

  * Matplotlib 本体コードで RuntimeWarning が送出される。
    とりあえずサブプロットは表示されるが、この内容で正しいかは知らない。

:file:`demo_parasite_axes2.py`
  密度、温度、速度。何やら座標軸が多い。

  * 関数 :code:`mpl_toolkits.axes_grid1.host_subplot` で生成したオブジェクトから
    メソッド :code:`twinx` を二度呼び出す。

  * このデモはモノクロでわかりにくい。色を変えてみよう。

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

:file:`close_event.py`
  サブプロットのイベントハンドラーの指定方法を示すデモ。基本。

  * このデモではウィンドウを閉じるイベントを扱う。
  * メソッド :code:`Figure.canvas.mpl_connect` を呼び出すことで
    サブプロットの「白い部分」上のイベントハンドラーを指定できる。
    引数にはイベント名を表す文字列と、発動される関数なり関数オブジェクトなりを渡す。

:file:`data_browser.py`
  マウスピック（クリック）およびキー押しイベントのデモ。

  * イベントハンドラーの signature の要件は、引数にイベントオブジェクトを取ることか。
    例えばキーイベントならば :code:`event.key` に、
    マウスピックイベントならば :code:`event.mouseevent` にそれぞれアクセスできる。

  * :code:`Axes.plot` のキーワード引数 :code:`picker=5` にも注意。
    これはマウスピック座標の余裕を指示する値である。CAD によくあるパラメーター。

  * 二点間の距離の平方を計測するのに関数 :code:`np.hypot` を利用する。
    こんな便利なものが存在していたか。

  * スクリプトの最後の if ブロック内に宣言された変数は
    Python 的には全て global 扱いであることに注意。

:file:`figure_axes_enter_leave.py`
  マウスカーソルの移動処理のデモ。Figure と Axes の両方について。

  * イベント名は ``(axes|figure)_(enter|leave)_event`` のような文字列だ。
    Axes についてのイベントハンドラーに渡されるオブジェクトには
    :code:`.inaxes` が、Figure についてのそれには :code:`.canvas` が利用可能。

  * マウスカーソルのある要素に色が塗られる。
    これはメソッド :code:`.patch.set_facecolor` を呼ぶ。

:file:`idle_and_timeout.py`
  アイドルイベントのデモだが、こういうことはしないで代わりに
  :code:`animation` の機能を使うこと。

:file:`keypress_demo.py`
  キー押しイベント処理のデモ。基本。

  * キー :kbd:`x` を押すたびに x 軸ラベルが出たり消えたりするというもの。
  * イベント名は ``key_press_event`` で、ハンドラーでは引数オブジェクトの
    属性値 :code:`.key` を参照する。

  * ラベルの表示処理はメソッド :code:`.set_visible` 等を利用する。

:file:`lasso_demo.py`
  いわゆる投げ縄選択のデモ。

  * そのまま実行すると例外
    ``AttributeError: module 'matplotlib.colors' has no attribute 'to_rgba'``
    が発生するので、これらの箇所にあるコードを書き換える必要がある
    （クラス ColorConverter を利用する）。

  * クラス Lasso を利用する。
  * イベントとしては ``button_press_event`` を使う。

  * 投げ縄を描く際にいろいろと面倒なことをしている。
    特に :code:`Figure.canvas.widgetlock` が絡む処理が曲者。
    ある種のロック操作が含まれる。

:file:`legend_picking.py`
  凡例部分のピックイベント処理デモ。
  凡例の線をピックすると、対応する折れ線（このデモでは折れはないが）の表示状態が切り替わる。

  * イベントとしては ``pick_event`` を使う。

  * 凡例を生成するにはメソッド :code:`Axes.legend` を呼ぶ。
    戻り値が凡例オブジェクト。

  * 凡例内の線にアクセスするには凡例に対するメソッド :code:`get_lines` でよい。
  * 折れ線の表示処理はメソッド :code:`.set_visible` 等を利用する。

:file:`looking_glass.py`
  マウスドラッグを実装するデモ。

  * 詳細は省くが、マウスイベントを 3 種類処理する。

  * 円と線群とが重なり合う部分については、線のほうの見え方を変えたい。
    これには線に対するメソッド :code:`.set_clip_path` を用いる。

:file:`path_editor.py`
  Bézier 曲線の編集デモ。案外面倒なコードになっている。

  * ``draw_event`` というイベントがある。
    キャンバスの描画を自力で行うとでも言うのか。

  * 全体的に FigureCanvas のメソッド呼び出しが重要らしい。
    あまり見かけないものもここでは利用する。

  * 初期状態ではこのパスは閉曲線に見えるが、
    実際には始点終点に対応する制御点（同じ座標だが）が一致しているだけの開曲線だ。

:file:`pick_event_demo.py`
  4 種のサブプロット上におけるピック処理のデモ。基本。

  * ピックイベントの処理は ``pick_event`` という名前になる。

  * 最初のウィンドウでは点プロットと棒グラフをピックするデモ。
    ピックされたオブジェクトが Line2D なのか Rectangle なのか Text なのかで
    イベントオブジェクトから得られる属性情報が異なる。

  * 次のウィンドウも点プロットのピックデモ。
    ピックした座標を得るには :code:`.pickx` 等を用いる。

  * メソッド :code:`Axes.plot` のキーワード引数 ``picker`` に関数を渡す。
    この自作関数ではピック座標とその近傍のプロット点との距離をテストしているらしい。

  * 次のウィンドウでは散布図のピックのデモを行う。
    今度はメソッド  :code:`Axes.scatter` のキーワード引数 ``picker`` には True を指定する。

  * 最後のウィンドウは画像のピックデモ。
    メソッド :code:`Axes.imshow` のキーワード引数 ``picker`` には True を指定する。

:file:`pick_event_demo2.py`
  点をピックすると、それに対応する元データを別ウィンドウで表示するデモ。

  * 元データは :code:`np.random.rand` による。
  * ピックさせるデータは :code:`np.mean` と :code:`np.std` による。
  * ピックハンドラーの引数から得られる :code:`event.ind` には
    どうもプロット点列の配列としてのインデックス（複数）であるようだ。

:file:`pipong.py`
  後述の :file:`pong_gtk.py` が import するモジュール。

:file:`poly_editor.py`
  正多角形の頂点をマウスでドラッグするデモ。

  * :file:`path_editor.py` のデモとコードの構造が同じ。

  * Line2D や Polygon のキーワード引数 :code:`animated=True` が気になる。

  * 角度ゼロ付近の頂点の配置が怪しい。

:file:`pong_gtk.py`
  準備不足なので ``ImportError: No module named 'gobject'`` となる。

:file:`resample.py`
  ビュー範囲を変えるとそれに連動してプロットの標本数を最適化して再描画するデモ？
  こちらの思うようには動作しないようだ。

:file:`test_mouseclicks.py`
  マウスボタンイベント処理のデモ。基本。

  * ダブルクリックかどうかはイベントハンドラーの引数オブジェクトの属性
    :code:`.dblclick` でテストできる。

:file:`timers.py`
  タイマーのデモ。

  * これまでのイベントハンドラーと色合いが異なり、タイマーオブジェクトの生成が必要。
  * コメントアウトのコードも注意。

:file:`trifinder_event_demo.py`
  マウスポインターを含むプロット三角形をハイライトするデモ。面白い。

  * デモデータの構成コードは要研究。
  * クラス Triangulation を利用する。
  * このオブジェクトをプロットするには関数 :code:`plt.triplot` を呼ぶ。
  * 終盤の Polygon オブジェクトは何だろうか。

:file:`viewlims.py`
  Mandelbrot 図形をズームインするデモ。

  * 図形の生成コードは :code:`Mandelbrot.__call__` にあるこの 10 行程度に収まっている。

  * メソッド :code:`Axes.callbacks.connect` でハンドラーを定義する。
    Qt 風に言うと signal を slot に connect する。

  * 素材の選択がある意味不適切な気がする。ズームしても元と変わらない。

:file:`zoom_window.py`
  散布図の拡大図を別ウィンドウで表示するデモ。

  * メソッド :code:`Axes.set_xlim` 等を用いてビューの範囲を更新する。
  * 別ウィンドウは開きっぱなし。

:file:`images_contours_and_fields`
----------------------------------------------------------------------
画像およびベクトル場関連といったところか。

:file:`contourf_log.py`
  グラデーションになっていないが、意図通りか？
  コード量は多くはないが、どのステップの処理も珍しい。

  * 二変数 Gauss 分布関数が :code:`mlab.bivariate_normal` として実装されている。
  * 関数 :code:`plt.contourf` で等高線プロットを描画する。
  * 関数 :code:`plt.colorbar` でカラーバーを図のそばに付属させる。

:file:`image_demo.py`
  ウィンドウに Lovelace 伯爵夫人の画像を表示する見本コード。

  * 画像の読み込みは関数 :code:`plt.imread` で行い、
    戻り値を :code:`plt.imshow` に渡せばよい。

  * :code:`plt.axis('off')` して座標軸を非表示にしておく。

:file:`image_demo_clip_path.py`
  ウィンドウに Grace Hopper 准将の画像を表示する見本コード。

  * 円形にくり抜いてあるが、これは画像オブジェクトのメソッド :code:`set_clip_path` で行う。
    引数のパッチオブジェクトはここでは Circle オブジェクトを採用している。

:file:`interpolation_methods.py`
  色補間 18 種のカタログ。

  * 18 個ものサブプロットオブジェクトを :code:`plt.subplots(3, 6, ...)` で生成している。

  * メソッド :code:`imshow` のキーワード引数 ``interpolation`` に指定する文字列が
    Matplotlib から得られるとよいだろう。

:file:`interpolation_none_vs_nearest.py`
  色補間ナシと最近補間の比較デモ。

  * 補間 ``none`` がよく効くのは大きな画像を小さく表示するときで、
    補間 ``nearest`` がよく効くのは小さな画像を大きく表示するときらしい。

  * Matplotlib 自体の話題ではないのだが、
    スクリプト後半のコメントに PDF を PNG に変換する処理について、
    興味深いことが書かれている。

:file:`pcolormesh_levels.py`
  :code:`Axes.pcolormesh` と :code:`Axes.contourf` の比較デモ。
  メッシュ対点。

  * クラス :code:`mpl.colors.BoundaryNorm` はカラーマップのインデックスを
    離散的な（整数の）区間に基いて生成する。
    このオブジェクトをメッシュプロット関数に渡すので、
    メッシュのほうはモザイクっぽい見栄えになる。
    それに対して、点のほうは曲線的な等高線がくっきりと見える。

  * :code:`plt.tight_layout` を呼び出し、上下のサブプロットの座標軸の目盛ラベルが
    重なり合わぬように、隙間を調整する。

:file:`streamplot_demo_features.py`
  ベクトル場プロットデモ。

  * メソッド :code:`Axes.streamplot` で描画する。
    引数には座標とベクトルを意味する配列を必要とするものがある。

:file:`streamplot_demo_masking.py`
  ベクトル場プロットデモのはず。

  * 実行時に MaskedArrayFutureWarning がスクリプトから送出される。
    これを修正できるくらいに理解を深めたい。

:file:`streamplot_demo_start_points.py`
  不明。

  * ``ValueError: operands could not be broadcast together with shapes (6,) (100,) (6,)`` なる例外が送出される。
    これを修正できるくらいに理解を深めたい。

:file:`lines_bars_and_markers`
----------------------------------------------------------------------
ここには初歩的な見本コードがある。

:file:`barh_demo.py`
  水平棒グラフの見本。

  * 関数 :code:`plt.barh` でデータを描画する。

:file:`fill_demo.py`
  プロット曲線と x 軸とで囲まれた領域に色を塗る単純なデモコード。

  * 単に関数 :code:`plt.fill(x, y)` を呼び出すだけでよい。
    プロット曲線と閉領域の着色を同時に行う。

:file:`fill_demo_features.py`
  複数のプロット曲線と x 軸とで囲まれた領域に色を塗る単純なデモコード。

  * 関数 :code:`plt.fill` の呼び出しが一度で済むことを理解すること。

:file:`line_demo_dash_control.py`
  プロット曲線を破線で描く方法を示す見本。

  * まずは :code:`plt.plot` の引数に文字列 ``--`` を指定して破線にする。
  * これだけでも破線になるが、点描のパターンを :code:`set_dashes` で細かく指定できる。

:file:`line_styles_reference.py`
  プロット曲線の線スタイルのカタログ。

:file:`marker_fillstyle_reference.py`
  マーカースタイルのカタログ。

  * :code:`Line2D.fillStyles` の要素が有効なスタイル。
    これをプロット関数の :code:`fillstyle` として指定する。

  * マーカーはだいたいマルに縦線や横線が入った記号で、
    半円部が別の色で塗られている。

:file:`marker_reference.py`
  マーカースタイルのカタログ。塗りナシと塗りアリの二種類を展示するデモ。

  * マーカーを指示するのに有効な値は
    Line2D.markers, Line2D.filled_markers, Line2D.filled_markers から得られる。
    例えば：

    .. code-block:: ipython

       In [1]: Line2D.filled_markers
       Out[1]: ('o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd')

:file:`scatter_with_legend.py`
  凡例付き散布図のデモ。

  * 散布図のプロット関数は :code:`plt.scatter` だ。
  * 凡例は関数 :code:`plt.legend` を呼び出す。

:file:`misc`
----------------------------------------------------------------------
雑多なコード例を集積したディレクトリーだろう。
すぐに動作しないコードもある。

:file:`contour_manual.py`
  クラス ContourSet のデモコード。

:file:`font_indexing.py`
  開発者向けコード。
  というより、フォントファイルがなくて動作しない。
  用意すれば動くだろう。

:file:`ftface_props.py`
  開発者向けコード。
  というより、フォントファイルがなくて動作しない。
  用意すれば動くだろう。

:file:`image_thumbnail.py`
  指定ディレクトリーにある全ての PNG ファイルからサムネイル画像を生成するデモコード。
  モジュール :code:`mpl.image` に PIL と似た機能があるようだ。

:file:`longshort.py`
  インターネットから CSV ファイルを取得して、データを読み込み、
  プロットを表示するデモコード。

  * Python 標準ライブラリーの関数 :code:`urllib.request.urlretrieve` でファイルをダウンロードする。
  * 関数 :code:`mpl.mlab.csv2rec` で CSV データをオブジェクト化する。
    それから CSV データを編集する。

  * メソッド :code:`Figure.autofmt_xdate` でラベルの日付文字列を適宜見やすくさせる。

:file:`multiprocess.py`
  Python の :code:`multiprocessing.Process` と :code:`multiprocessing.Pipe` を絡めたデモコード。

  * :code:`matplotlib.use('GtkAgg')` しているが、これが必要なのか。
  * ``ImportError: No module named 'gobject'`` が発生してダメ。

:file:`rasterization_demo.py`
  ビットマップ化関係か？

  * ダミーのメッシュプロットを生成するのに :code:`np.meshgrid` が向いている。
  * ポイントは :code:`Axis.pclormesh` の戻り値オブジェクトに対する
    :code:`set_rasterized(True)` や :code:`set_zorder(-20)` だろう。

  * 最後に関数 :code:`plt.savefig` を呼び出して PDF, EPS, SVG ファイルを出力する。

  * 生成した SVG ファイルを Inkscape で開こうとしたらモッサリしてダメ。
    それ以外のファイルはそれぞれのビューワーで普通に閲覧できた。

:file:`rc_traits.py`
  ``ImportError: No module named 'traits'`` となってダメ。

:file:`rec_groupby_demo.py`
  ``AttributeError: module 'numpy' has no attribute 'string0'`` となってダメ。

:file:`rec_join_demo.py`
  ``AttributeError: module 'numpy' has no attribute 'string0'`` となってダメ。

:file:`sample_data_demo.py`
  ウィンドウに Lovelace 伯爵夫人の画像を表示する見本コード。

  * 関数 :code:`mpl.cbook.get_sample_data` のデモコード。
    あとは :code:`plt.imread` と :code:`plt.imshow` を呼び出す。

:file:`svg_filter_line.py`
  プロットを SVG データ化し、かつ XML コードをそこへ追加するようなデモコード。

  * 関数 :code:`plt.savefig` を BytesIO オブジェクトに対して作用させているのがポイント。

  * Inkscape で開くと、折れ線グラフにドロップシャドウが付いているのが目視できる。
    デモコードの後半部で、このエフェクトフィルターに相当する XML コード片を
    XML オブジェクトツリーに自力で挿入している。

  * UserWarning が発生するので、気になるかもしれない。

:file:`svg_filter_pie.py`
  コードの構造は上記デモコードと同様。円グラフ版。

:file:`tight_bbox_test.py`
  プロットをウィンドウだけでなく、さまざまな形式のファイルに出力するデモコード。

  .. code-block:: ipython

     In [1]: %run ./misc/tight_bbox_test.py
     saving tight_bbox_test.png
     saving tight_bbox_test.pdf
     saving tight_bbox_test.svg
     saving tight_bbox_test.svgz
     saving tight_bbox_test.eps

  * 関数 :code:`plt.savefig` を用いる。
    ファイル形式は最初の引数のパス文字列の拡張子で自動判別されるらしい。

  * 関数呼び出し一発で PDF ファイルにプロットを出力できるのは強力。

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

  * 関数 :code:`plt.text` 等 LaTeX 数式を指定できることは学習済み。
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
統計データに相性の良いプロット各種のデモコード。

:file:`boxplot_color_demo.py`
  箱プロットのデモ。

  * ダミーデータは :code:`np.random.normal` を利用して生成。正規分布。
  * メソッド :code:`Axes.boxplot` によるプロット。
  * キーワード引数 ``notch`` を指定すると、箱の形状が V 字型にえぐれる。

:file:`boxplot_demo.py`
  箱プロットにさまざまなオプションおよび描画スタイルを適用するデモ。

  * ダミーデータは :code:`np.random.lognormal` を利用して生成。正規分布。
  * サブプロットを複数作成して、それぞれでメソッド :code:`Axes.boxplot` を
    さまざまなオプションと共に呼び出す。
    ここでは ``showmeans``, ``showbox``, ``meanline``, ``showcaps``,
    ``notch``, ``bootstrap`` 等のキーワード引数を指定する。

  * 描画用の引数として ``boxprops``, ``flierprops``, ``medianprops`` がある。
    いずれも dict オブジェクトを渡す前提だ。

  * メソッド :code:`Figure.suptitle` で中央寄せの見出しを図に付ける。

:file:`boxplot_vs_violin_demo.py`
  バイオリンプロットと箱プロットの比較デモ。

  * メソッド :code:`Axes.violinplot` によるプロット。
    ここでは :code:`showmeans=False, showmedians=True` としている。
    これは隣のサブプロットに描く箱プロットととの比較をしやすくしているのだろう。

  * バイオリンプロットの一つのデータの形状は、なるほどバイオリンのような輪郭だ。

:file:`bxp_demo.py`
  プロットデータ計算と描画を分けて実現するデモ？

  * デモコードの働きはふたつ上のデモコードと同じ。

  * 関数 :code:`mpl.cbook.boxplot_stats` でサンプルデータから統計データ？を計算しておく。
  * 次にメソッド :code:`Axes.bxp` でこのデータの箱＆ヒゲプロットを描画する。
    このメソッドの引数は :code:`Axes.boxplot` とかなり共通している。

:file:`errorbars_and_boxes.py`
  メソッド :code:`Axes.errorbar` のデモ。

  * このデモでは 2 次元のダミーデータを用いる。
  * 四角い部分の描画は PatchCollection オブジェクトによる。

:file:`errorbar_demo.py`
  関数 :code:`plt.errorbar` の使い方を説明する基本的なデモ。

  * キーワード引数 ``xerr`` と ``yerr`` でそれぞれに対応する軸方向の
    アイビームの長さを指定する。

:file:`errorbar_demo_features.py`
  エラー部分の線を対称形にしたり非対称形にしたりするデモ。

  * 上のサブプロットはエラーを y 軸方向に、
    下のサブプロットは x 軸方向にそれぞれ表示する。

  * メソッド :code:`Axies.errorbar` においてエラー量を指定する引数は
    ``xerr``, ``yerr`` である。

  * 意味はないが、下のサブプロットでは y 軸を対数グラフにしている。
    :code:`ax1.set_yscale('log')` による。

:file:`errorbar_limits.py`
  エラー部分のさまざまなスタイル設定のデモ。

  * メソッド :code:`Axies.errorbar` においてキーワード引数
    ``uplims``, ``lolims``, ``xlolims``, ``xuplims`` を用いる。

:file:`histogram_demo_cumulative.py`
  累積的ヒストグラムのデモ。

  * ヒストグラムをプロットする関数は :code:`plt.hist` だ。
    この引数の ``cumulative`` に True を指定すれば累積的になるし、
    -1 を指定すれば逆累積ヒストグラムになる。

:file:`histogram_demo_features.py`
  別のページで説明したので省略。

:file:`histogram_demo_histtypes.py`
  ヒストグラムのデモ。

  * :code:`histtype='stepfilled'` とするとビン同士の間の線がバーの色で塗りつぶされる。
  * 第 2 引数にビンの幅の list オブジェクトを渡すと、ビン間隔が非一様なヒストグラムが描ける。

:file:`histogram_demo_multihist.py`
  複数データを同一のサブプロットに描くデモ。

  :code:`stacked=True` としたり、データそのものが入れ子の配列だったりと
  いろいろなパターンがある。

:file:`multiple_histograms_side_by_side.py`
  複数のヒストグラムを同一サブプロット内で一列に並べるデモ。

:file:`violinplot_demo.py`
  バイオリンプロットのデモ。

  * メソッド :code:`Axes.violinplot` のキーワード引数
    ``showmedians``, ``showextrema``, ``showmeans``,
    ``bw_method`` のデモ。

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
このディレクトリーの見本コード群は
モジュール :file:`basic_units.py` を定義しておき、
それ以外のスクリプトがこれを import するという構造である。

:file:`basic_units.py`
  難しいコードだ。これを理解するのが本題だ。

  * 一般利用者が理解するという目的からすると、
    必要以上に複雑になっている可能性がある。

以下はこのモジュールを応用するデモコードだ。

:file:`annotate_with_units.py`
  距離単位オブジェクトの利用を除けば、注釈矢印のデモコード。
  一方の矢印は単位系を全て :code:`basic_units.cm` で明示し、
  他方はラベル座標の単位系を無次元単位で指定しているというもの。

  * さらに両者の引数 ``textcoords`` の値が異なることに注意。
    前者は ``data`` つまり注釈されるオブジェクトの座標系が適用されるのに対して、
    後者は ``axes fraction`` つまりサブプロット領域の正規化座標系が適用される。

:file:`artist_tests.py`
  Line2D 等が座標変換を扱えることを示すデモコード。

  * メソッド :code:`Axis.set_units` に :code:`basic_units.cm` を引き渡す。

  * Line2D, Rectangle, Text それぞれについて、
    オブジェクトの位置や長さをやはり :code:`basic_units.cm` を用いて指定する。

:file:`bar_demo2.py`
  同一データを座標軸ごとに単位系の異なる複数のサブプロットに描くデモコード。

  * 先頭に :code:`cms = cm * np.arange(0, 10, 2)` というオブジェクトが現れる。
    これをいずれのサブプロットにおいても棒グラフで描く。

  * メソッド :code:`Axes.bar` のキーワード引数 ``xunits`` と ``yunits`` について
    単位オブジェクト :code:`basic_units.cm` や :code:`basic_units.inch` を指定する。

:file:`bar_unit_demo.py`
  棒グラフだが、データは人間の身長の統計のようだ。

  * モデルデータに単位オブジェクトを含める。
  * サブプロットの y 軸にだけ :code:`Axis.set_units` に :code:`basic_units.cm` を引き渡す。
  * あとはメソッド :code:`Axes.autoscale_view` が適宜調整してくれるようだ。

:file:`ellipse_with_units.py`
  同じ形状を定義した上で Ellipse と Arc を比較する。

  * 中心、長径、短径のすべてを :code:`basic_units.cm` で定義する。
  * サブプロットの座標系単位系は明示的に指定しない。

:file:`evans_test.py`
  このデモは :file:`basic_units.py` を必要としない。

  * コードの前半はモジュール :code:`mpl.units` にカスタム単位を登録する方法の見本だ。
    ユーザーがクラスを 2 個書く必要があるようだ。

  * コードの後半は単位のついたデータ量を、
    サブプロットに対しては直接単位系を指定せずにプロットする。

:file:`radian_demo.py`
  :code:`basic_units.radians` と :code:`basic_units.degrees` のデモコード。

  * ふたつサブプロットを用意しておき、
    メソッド :code:`Axes.plot` のキーワード引数 ``xunits`` に
    一方は ``radians`` を、他方には ``degrees`` を指定してプロットする。
    その結果、座標軸の目盛ラベルがそれぞれ違って見える。

:file:`units_sample.py`
  :code:`basic_units.cm` と :code:`basic_units.inch` のデモコード。

  * サブプロットを 4 個用意して、
    それぞれのメソッド :code:`Axes.plot` の呼び出しに対して
    キーワード引数 ``xunits`` および ``yunits`` に考えられる組み合わせで単位を指定する。

:file:`units_scatter.py`
  散布図の y 軸にだけカスタム単位を適用するデモコード。

  * サンプルデータの単位は :code:`basic_units.secs` とする。
  * メソッド :code:`Axes.scatter` の ``yunits`` は :code:`basic_units.secs` とする。
  * 一番下のサブプロットだけメソッド :code:`Axis.set_units` を呼び出して
    :code:`basic_units.herz` を指定する。

  * NumPy から ``UserWarning: Warning: converting a masked element to nan.`` が生じるが、
    気にしないでおく。

:file:`user_interfaces`
----------------------------------------------------------------------
Matplotlib は wxPython, PyGTK, Tkinter, PyQt4/5 の GUI アプリケーションに直接埋め込む
ことができることを示すデモコードの集まり。
ここでは私の環境で実行できたデモコードをコメントする。

:file:`embedding_in_gtk.py`
  要 GTK につき実行できない。

:file:`embedding_in_gtk2.py`
  要 GTK につき実行できない。

:file:`embedding_in_gtk3.py`
  要 GTK につき実行できない。

:file:`embedding_in_gtk3_panzoom.py`
  要 GTK につき実行できない。

:file:`embedding_in_qt4.py`
  クラス :code:`matplotlib.backends.backend_qt4agg.FigureCanvasQTAgg` のサブクラス化のデモ。

  * PyQt4 だけでなく PyQt5 もインストールされている環境で実行すると
    ``RuntimeError: the PyQt4.QtCore and PyQt5.QtCore modules both wrap the QObject class``
    という例外が発生する。

:file:`embedding_in_qt4_wtoolbar.py`
  クラス :code:`matplotlib.backends.backend_qt4agg.NavigationToolbar2QT` のデモ。
  実行するとツールバーが下部に付いたウィンドウが表示される。

  * PyQt4 だけでなく PyQt5 もインストールされている環境で実行すると
    ``RuntimeError: the PyQt4.QtCore and PyQt5.QtCore modules both wrap the QObject class``
    という例外が発生する。

  * 警告 ``MatplotlibDeprecationWarning: This module has been deprecated in 1.4 ...`` が出現する。

  * クラス FigureCanvasQTAgg をこのデモでも当然利用する。
    このオブジェクトの生成時に Figure オブジェクトを渡す。
    キャンバスは QVBoxLayout に渡す。

  * メソッド :code:`on_draw` でいちいちサブプロットを生成、描画する。

  * キーイベントは :code:`on_key_press` で処理する。
    ただしツールバー自体も処理したいようなので、そちらにもイベントを横流しする。
    例えば :kbd:`s` を押すと、ファイル保存ダイアログボックスが現れる。

:file:`embedding_in_qt5.py`
  クラス :code:`matplotlib.backends.backend_qt5agg.FigureCanvasQTAgg` のサブクラス化のデモ。

  * 最初のモジュールインポート文の感じが :file:`embedding_in_qt4.py` と異なる。

  * サブクラスとして MyMplCanvas, MyStaticMplCanvas, MyDynamicMplCanvas を定義する。
    最初のクラスは残りのもののスーパークラスとする。
    ここで Matplotlib の Figure や Axes オブジェクトを保持し、
    Qt のウィンドウオブジェクトの設定を行う。

  * クラス MyStaticMplCanvas では単純な正弦波をプロットする。

  * クラス MyDynamicMplCanvas では Qt のタイマークラスを用いて
    折れ線プロットのアニメーションを実現する。

  * クラス ApplicationWindow は Qt アプリケーションでよく見られる
    QMainWindow のサブクラス。ウィンドウ部品を手動でレイアウトしたり、
    メニューアイテムを実装したりする。

  * 最後の数行は PyQt アプリケーションにありがちなメイン関数のコードだ。

:file:`embedding_in_tk.py`
  現在 Tk の DLL が壊れているのだろうか、Python ごと落ちる。

:file:`embedding_in_tk2.py`
  現在 Tk の DLL が壊れているのだろうか、Python ごと落ちる。

:file:`embedding_in_tk_canvas.py`
  現在 Tk の DLL が壊れているのだろうか、Python ごと落ちる。

:file:`embedding_in_wx2.py`
  要 wxPython 2.8.12 以上とのことなので実行できない。

:file:`embedding_in_wx3.py`
  要 wxPython 2.8.12 以上とのことなので実行できない。

:file:`embedding_in_wx4.py`
  要 wxPython 2.8.12 以上とのことなので実行できない。

:file:`embedding_in_wx5.py`
  要 wxPython 2.8.12 以上とのことなので実行できない。
  エラーメッセージが他のものと少々異なる。

:file:`embedding_webagg.py`
  簡単なプロットをブラウザーに表示し、
  いつものウィンドウでの簡単な操作に加え、各種フォーマットのファイルをダウンロードすることが
  可能なことを示すデモ。

  * 要 Tornado とのこと。
    実行してみたらファイアーウォールの解除も必要なことがわかる。

  * モジュール :code:`matplotlib.backends.backend_webagg_core` から
    クラスと関数を import する。

  * クラス MyApplication をクラス :code:`tornado.web.Application` のサブクラスとして定義する。
    ここは Tornado を学習しないことには何とも言えない。
    Matplotlib の Figure オブジェクトを関数
    :code:`new_figure_manager_given_figure` に渡す。
    このオブジェクト :code:`figure` が HTML ファイルの対応する部分に埋め込まれる。

  * MyApplication のコンストラクターでクラス FigureManagerWebAgg のクラスメソッド
    :code:`get_static_file_path` を用いる。

  * MyApplication の内部クラス WebSocket が明らかに重要そうなのだが、
    私にはコードの意味がはっきりとわからない。

  * スクリプト実行後に出力される URL をブラウザーに与えればプロットが現れる。

:file:`fourier_demo_wx.py`
  要 wxPython 2.8.12 以上とのことなので実行できない。

:file:`gtk_spreadsheet.py`
  要 GTK につき実行できない。
  エラーメッセージが他のものと少々異なる。

:file:`histogram_demo_canvasagg.py`
  無反応？

:file:`interactive.py`
  要 GTK につき実行できない。

:file:`interactive2.py`
  要 GTK につき実行できない。

:file:`lineprops_dialog_gtk.py`
  要 GTK につき実行できない。

:file:`mathtext_wx.py`
  要 wxPython 2.8.12 以上とのことなので実行できない。

:file:`mpl_with_glade.py`
  要 GTK につき実行できない。

:file:`mpl_with_glade_316.py`
  要 GTK につき実行できない。

:file:`pylab_with_gtk.py`
  要 GTK につき実行できない。

:file:`rec_edit_gtk_custom.py`
  要 GTK につき実行できない。

:file:`rec_edit_gtk_simple.py`
  要 GTK につき実行できない。

:file:`svg_histogram.py`
  SVG ファイルにヒストグラムを出力し、そこにある凡例の棒をクリックすると
  プロット上の対応する棒の表示状態が切り替わるというデモ。
  SVG ファイルに JavaScript を埋め込むので、動作確認にはそれなりのブラウザーが必要。

  * プロット部品に対してメソッド :code:`.set_gid` を呼び出すことで
    SVG 要素用の ID を適宜割り振っていく。

  * 関数 :code:`plt.savefig` にキーワード引数 :code:`format="svg"` を指定することで
    ファイル風オブジェクトにプロットの内容を SVG 形式で出力する。

  * 後半は Python 標準ライブラリーにあるクラス :code:`xml.etree.ElementTree` の機能を利用。
    SVG 要素としてのパッチ要素にイベントハンドラーを属性値として設定する。

  * JavaScript のコードテンプレートを here string で書いて（デモなので）実引数を与える。
    関数 :code:`json.dumps` はこういう使い方もするのか。

  * 最後に ElementTree オブジェクトを生成して
    直ちにメソッド :code:`write` を用いて SVG ファイルを保存する。

:file:`svg_tooltip.py`
  SVG ファイルに図形を含むプロットを出力し、
  そこにある図形の上にマウスポインターを重ねるとツールチップが出現するというデモ。
  デモ :file:`svg_histogram.py` と共通するところが多い。

:file:`toolmanager.py`
  要 GTK につき実行できない。

:file:`wxcursor_demo.py`
  要 wxPython 2.8.12 以上とのことなので実行できない。

:file:`widgets`
----------------------------------------------------------------------
ウィンドウ部品のデモコード一式。GUI の学習はここから始めてよい。

:file:`buttons.py`
  プッシュボタンのデモ。ボタンを押すたびに波形の振動数が増減する。

  * ここでは関数 :code:`plt.axes` をボタンを配置する空間を確保するものとして利用している。
    戻り値を Button コンストラクターの引数に使う。

  * メソッド :code:`Button.on_clicked` に押された時に呼び出される振る舞いを指定する。

  * 関数 :code:`plt.draw` でサブプロットを更新描画する。

:file:`check_buttons.py`
  チェックボックスのデモ。チェックボックスに対応する波形の表示が切り替わる。

  * スペース確保とイベントハンドラー周りのコードは前回同様。

  * クラス CheckButtons のコンストラクターには場所とラベルに加えて初期状態も指定する。

  * プロットオブジェクトには:code:`visible` のような属性があって、
    これを関連メソッドで操作する。また、生成時にもキーワード引数で初期値を指示できる。

:file:`cursor.py`
  マウスカーソルの位置に追従してサブプロット上にクロスヘアを描くデモ。

  * ``AttributeError: Unknown property facecolor`` という例外が生じるので、
    これを引き起こすコードを削除しておく。

  * クラス Cursor のコンストラクターを適当に呼び出すだけでよい。

:file:`lasso_selector_demo.py`
  このデモは期待通りに動作しない。投げ縄選択で水玉を囲むデモだと思われる。

:file:`menu.py`
  メニューのデモ。

  * ``AttributeError: module 'matplotlib.colors' has no attribute 'to_rgba'`` 例外が生じる。
    これを解決するために、クラス :code:`colors.ColorConverter` のオブジェクトを導入しておく。

  * コードがたいへん込み入っている。未知のクラスを相当利用したデモコードだ。

  * クラス MenuItem を :code:`artist.Artist` のサブクラスとしてここで実装している。
    それ以外のユーザー定義クラスは全てが object からのサブクラスだ。

  * イベントハンドラーの定義はメソッド :code:`fig.canvas.mpl_connect` から行う。

:file:`multicursor.py`
  マウスカーソルの位置に追従してふたつのサブプロット上に縦線を描くデモ。

  * クラス MultiCursor の最初の引数に :code:`fig.canvas` を指定する。
    次の引数には対象のサブプロットを含む list または tuple を指定する。

:file:`radio_buttons.py`
  ラジオボタンのデモ。各項目に対応する波形の描画スタイルが切り替わる。

  * クラス RadioButtons を使うコードの構造は Button や CheckButtons とよく似る。

  * ``AttributeError: Unknown property facecolor`` という例外が生じるので、
    これを引き起こすコードを削除しておく。

:file:`rectangle_selector.py`
  マウスによる矩形領域選択のデモ。

  * クラス RectangleSelector を用いる。

  * イベントハンドラーの指定がこれまでと異なる。
    まず RectangleSelector コンストラクターの引数に一個、
    次に関数 :code:`plt.connect` を呼び出してもう一個、という感じだ。
    前者のハンドラーはマウス操作のコールバックとして、
    後者のハンドラーはキー操作のコールバックとして指定する。

:file:`slider_demo.py`
  Slider と RadioButtons のデモ。

  * ``AttributeError: Unknown property facecolor`` という例外が生じるので、
    これを引き起こすコードを削除しておく。

  * クラス Slider の使い方はこれまでの widget と大体同じ。
    イベントハンドラーは :code:`on_changed` となる。

:file:`span_selector.py`
  サブプロット上の横幅をマウスで選択するデモ。

  * クラス SpanSelector を用いる。

  * ``AttributeError: Unknown property facecolor`` という例外が生じるので、
    これを引き起こすコードを削除しておく。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
