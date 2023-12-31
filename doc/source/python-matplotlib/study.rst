======================================================================
見本コードを研究する
======================================================================

Matplotlib を手足のように使いこなせるようになるには、相当時間を要すると前書きで
述べた。ここでは、習うより慣れろの精神で Matplotlib_ ドキュメント内の
`見本コード集 <http://matplotlib.org/examples/>`__
からいろいろと吸収することを考えてみよう。

.. contents:: ノート目次
   :depth: 3

コードを収集する
======================================================================

公式サイトに付属している見本集の本数は 400 を軽く超える。これらをブラウザーで閲
覧しながら、一個一個の見本コードのページを見ていくのは効率が悪い。研究に本腰を入
れるのならば、これら全てをあらかじめローカルにダウンロードしておくべきだろう。そ
の方法としては次のどちらかを挙げたい。

* 素直に Matplotlib のリポジトリーを ``git clone`` してから、:file:`examples`
  ディレクトリーにあるコードにアクセスする。
* とにかく見本コードだけが手許にあれば十分なので、:file:`examples` ディレクト
  リーしかダウンロードせずに済ませる。

PC のディスク残量とインターネットの接続環境に不満がないか、あるいは既に GitHub
にあるリポジトリーのクローンを :command:`pip install -e` していて、そのソース
コードをそのまま利用中であるならば、前者の方法で問題はない。

.. code:: console

   bash$ git clone https://github.com/matplotlib/matplotlib.git
   bash$ cd matplotlib/examples

そうではなく、資源が乏しかったり、もうパッケージがあるのにクローンなど作成したく
ないのであれば、必要な分だけをダウンロードするだけで済ませる。

Git リポジトリーの特定のディレクトリーのスナップショットを得るのに古の VCS ツー
ルである :program:`svn` が利用できる。

.. code:: console

   bash$ svn export https://github.com/matplotlib/matplotlib.git/trunk/examples
   bash$ mv examples mpl-examples
   bash$ cd mpl-examples

コードを実行する
======================================================================

コマンドプロンプトから実行するか、または IPython のコマンド ``%run`` を使うこと
で見本スクリプトの挙動を確認することができる。後者の方法のほうがわずかに効率が良
い？

後述する、開発陣が利用しているであろう :file:`tests/backend_driver.py` も有用で
ある。

稼働ノート
======================================================================

本節では評者が :file:`examples` にある見本コードを実際に実行した感想を記す。見本
の目的はサブディレクトリーを用いて分類されているので、本節をそれらに対応した単位
に分割して、コードの寸評を述べる。

:file:`animation`
----------------------------------------------------------------------

クラス ``matplotlib.animation.FuncAnimation`` を利用するコードで構成された見
本集。 MPEG ファイルを保存するコードが動かないのが残念だ。

:file:`animate_decay.py`
  動的に減衰波形がプロットされる。
:file:`basic_example.py`
  まず色彩豊かな何かのアニメーションがあり、次に折れ線のアニメーションとなる。
  ``FuncAnimation`` と ``ArtistAnimation`` を別々に使用。
:file:`basic_example_writer.py`
  先ほどのアニメーションをファイルに出力する見本コードのようだが、
  ``animation.writers['ffmpeg']`` の処理で実行時例外が発生する。
:file:`bayes_update.py`
  ベータ分布の確率密度関数曲線のプロットのアニメーション例。

  * SciPy_ が必要。
  * メソッド ``Axes.axvline`` の使い方も習える。

:file:`double_pendulum_animated.py`
  振り子の付いた振り子のアニメーション。肘みたいな動きをする。

  * SciPy_ が必要。常微分方程式を一度解く。

:file:`dynamic_image.py`
  幻想的な色のアニメーション。

  * 関数 ``matplotlib.pyplot.imshow`` を併用する。

:file:`dynamic_image2.py`
  幻想的な色のアニメーション。上の物と酷似。

  * たまにホワイトアウトするのは ``repeat_delay`` によるものか。
  * FuncAnimation の代わりに ArtistAnimation を利用する。

:file:`histogram.py`
  ヒストグラムのアニメーション。各ビンの数値が変動する。

  * ヒストグラム本体よりもパスを構成するほうに労力を割いている。
    配列のスライスの活用が素晴らしい。

:file:`moviewriter.py`
  例によって ``animation.writers['ffmpeg']`` の処理で実行時例外が発生する。

:file:`rain.py`
  雨の降っている地面を眺めているかのようなアニメーション。

  * 乱数は NumPy_ の ``np.random.uniform`` を利用している。
  * 散布図 (``Axes.scatter``) を応用している。

:file:`random_data.py`
  区分的一次関数のアニメーション。区間以外が動的に変動する。

  * この中でもっとも単純なコードからなる。
  * 乱数は NumPy_ の ``np.random.rand`` を利用している。

:file:`simple_3danim.py`
  空間の一部に含まれるいくつかの点のブラウン運動のようなアニメーション。

  * モジュール ``mpl_toolkits.mplot3d.axes3d`` を利用する。
  * モデル部分は 3D データとなり専用のメソッド等を用いる必要があるが、アニメー
    ション部分は 2D だろうが 3D だろうがやることは変わらない。

:file:`simple_anim.py`
  三角関数のプロットのアニメーション。位相が動的に変動する。

  * 関数 ``np.ma.array`` を用いれば、欠損要素を含んでもよい配列オブジェクト
    を生成できる。

:file:`strip_chart_demo.py`
  心電図のようなプロットのアニメーション。

  * 与えられた確率をしきい値として、乱数値またはゼロを評価する関数を構成するとこ
    ろにこのアニメーションの独創性がある。

:file:`subplots.py`
  複数サブプロットがいっせいにアニメーション。

  * クラス ``matplotlib.animation.TimedAnimation`` のサブクラスを実装しても
    よいことを示してもいる。
  * やはり ``Figure.add_subplot`` は使いこなすのが難しい。

:file:`unchained.py`
  モダンアート。

:file:`api`
----------------------------------------------------------------------

ここにあるコードは原則的に ``plt`` の関数呼び出しを厳しく限定していて、
``Figure`` オブジェクトを生成する関数、関数 ``plt.show`` それに関数
``plt.close`` しか利用を認めていない。オブジェクト指向プログラミング風のコー
ドを推奨するということだろう。

:file:`agg_oo.py`
  簡単なプロットを描画して画像ファイルとして保存する。クラス
  ``matplotlib.backends.backend_agg.FigureCanvasAgg`` のデモ。基本。

  * ``Figure``, ``FigureCanvasAgg``/``Axes`` の順にオブジェクトを生成する。最初
    の二つはコンストラクターから直接生成し、最後のものはメソッド
    ``fig.add_subplot`` を用いる。
  * メソッド `canvas.print_figure` の呼び出しで画像ファイルを保存する。拡張子が
    ないが SVG ファイルができる。

:file:`barchart_demo.py`
  棒グラフのデモ。基本。
:file:`bbox_intersect.py`
  クラス ``Bbox`` のデモ。12 本のランダムな線分と矩形が共通点を持つかテストす
  る。

  * 本当なら関数 ``plt.gca`` の戻り値を一時変数に取り、その ``Axes`` オブ
    ジェクトのメソッドでプロットをすることがこのデモディレクトリーの方針に適う。
  * ``Bbox`` のオブジェクトをクラスメソッド ``Bbox.from_bounds`` で生成す
    る。
  * 交点の存在テストには ``Path.intersects_bbox`` を利用したいので、線分を
    ``Path`` オブジェクトとして一時的に生成する。

:file:`collections_demo.py`
  クラス ``LineCollection``, ``PolyCollection``, ``RegularPolyCollection`` と自
  動スケール調整のデモコード。

  * そのまま実行すると例外 ``AttributeError: module 'matplotlib.colors' has no
    attribute 'to_rgba'`` が発生するので、これらの箇所にあるコードを書き換える必
    要がある（クラス ``ColorConverter`` を利用する）。
  * 珍しく ``np.random.RandomState`` を利用している。このクラスは Mersenne
    Twister 乱数生成器を表す。
  * コレクションクラスのキーワード引数の ``transOffset`` には、オブジェクトが所
    属する ``Axes`` の ``.transData`` を指定する。その後にオブジェクトの
    ``.set_transform`` に独自の Transform オブジェクトを指定する。
  * オブジェクトを ``Axes`` に ``.add_collection`` した後にメソッド
    ``.autoscale_view`` を呼び出す。

:file:`colorbar_only.py`
  カラーバーしか図に載せないデモ。応用。
:file:`compound_path.py`
  区分的曲線（ここでは線分だが）のデモ。基本。

  * 曲線の構成は ``Path`` オブジェクトと ``PathPatch`` オブジェクトの二段階構造
    だ。まずデータである ``Path`` を作成してから図表要素である ``PathPatch`` を
    作成する。

  * パッチは ``Axes.add_patch`` で追加する。
  * 最後に ``Axes.autoscale_view`` で描画範囲を適切に設定する。

:file:`custom_projection_example.py`
  ``Axes`` をサブクラス化して、独自の投影クラスを作成するデモ。応用。
:file:`custom_scale_example.py`
  Mercator 図法なプロットを自作するデモ。応用。

  おおまかに言うと ``mpl.scale.ScaleBase`` のサブクラスを適切に実装し、それを関
  数 ``mpl.scale.register_scale`` 呼び出しでクラス自身を与える。その後に
  ``Axes`` を作成して、メソッド ``.set_yscale`` に自作クラスのクラスプロパティー
  ``.name`` を指定する。

:file:`date_demo.py`
  プロット x 軸の目盛ラベルに西暦四桁を描画するデモ。また、ステータスバーに表示
  するマウスポインター位置の座標の表示のカスタマイズもする。モジュール
  ``mpl.dates`` にある各クラスを利用する。

  * メソッド ``Axis.set_major_locator`` で 長目盛の位置決めオブジェクトを指定す
    る。
  * メソッド ``Axis.set_minor_locator`` で 短目盛の位置決めオブジェクトを指定す
    る。
  * メソッド ``Axis.set_major_formatter`` で長目盛のラベル書式オブジェクトを指定
    する。
  * 面白いことに ``Axis.set_xlim`` の値が ``date`` 型オブジェクトだ。
  * プロパティー ``Axis.format_xdata`` にステータスバーの x 座標表示用書式オブ
    ジェクトを指定する。プロパティー ``Axis.format_ydata`` も同様。
  * メソッド ``Figure.autofmt_xdate`` という、日付ラベル回転調整機能がある。

:file:`date_index_formatter.py`
  より細かい日付ラベルのデモ。

  * メソッド ``Axis.set_major_formatter`` の実引数が複雑になっている。自作の関数
    をさらに ``FuncFormatter`` でラップする。

:file:`demo_affine_image.py`
  画像に対する affine 変換のデモ。

  * 自作関数 ``get_image`` でダミー画像を生成する。
  * メソッド ``AxesImage.set_transform`` に ``Affine2D`` オブジェクトを指定す
    る。
  * このデモコードにはプロット表示処理がないので、お望みなら自分で書け。

:file:`donut_demo.py`
  同心円の着色に関するデモ。だからドーナツ。

  * これは ``Path`` と ``PathPatch`` のコンビで同心円を辺数の多い多角形で近似す
    ることで定義して、「穴」を塗ったり、または塗らないままにする方法を示してい
    る。

:file:`engineering_formatter.py`
  クラス ``EngFormatter`` のデモ。対数グラフの座標軸ラベルのカスタマイズを示す。

  * このデモでは ``EngFormatter(unit='Hz', places=1)`` というオブジェクトを生成
    する。これにより、目盛ラベルは適当な所で ``Hz``, ``kHz``, ``MHz``, ... とい
    う単位表示になる。数値は小数点以下一位まで見せる。
  * ダミーデータの構成での NumPy の対数関係の関数の使い方が上手なので参考にな
    る。

:file:`filled_step.py`
  残念だが ``AttributeError: Unknown property bottom_margin`` という例外が生じ
  る。可能なら勝手に直したいところだ。

:file:`font_family_rc.py`
  ``rcParams`` の中身を直接変更することでフォントを指定するデモ。

  * コードの一番最初で ``rcParams`` を ``import`` する必要がある。それ以外の
    Matplotlib モジュールの ``import`` 文を書くのは、その変更処理が全部終わって
    からとなる？

:file:`font_file.py`
  クラス ``FontProperties`` のデモ。

  * フォントパスを指定して ``FontProperties`` オブジェクトを生成する。
  * メソッド ``Axes.set_title`` のキーワード引数 ``fontproperties`` にこのオブ
    ジェクトを渡すことで、テキストをこのフォントで描画するようになる。

:file:`histogram_path_demo.py`
  ヒストグラムを ``PathPatch`` オブジェクトを使って描画するデモ。

  * ダミーのヒストグラムデータは ``np.histogram`` で適当に用意する。それからやや
    面倒な配列処理で、各棒の輪郭を定義する。
  * ``Path`` オブジェクトを生成する。今回はクラスメソッドの
    ``.make_compound_path_from_polys`` を利用する。

:file:`image_zcoord.py`
  画像プロットだが、ステータスバーに強引に z 座標を表示するデモ。

  * プロパティー ``Axes.format_coord`` に自作の関数を割り当てる。自作の関数では
    ステータスバーに表示する文字列そのものを戻すようにする。

:file:`joinstyle.py`
  折れ線の折れた部分のスタイル三種のデモ。

  * メソッド ``Axes.plot`` のキーワード引数 ``solid_joinstyle`` に対して文字列
    ``'miter'``, ``'round'``, ``'bevel'`` のいずれかを指定する。

:file:`legend_demo.py`
  凡例のデモ。基本。

  * 関数 ``plt.legend`` で凡例を図に表示する。

:file:`line_with_text.py`
  ``Line2D`` のサブクラスデモ。どのメソッドをオーバーライドすればよいかわかる。
:file:`logo2.py`
  Matplotlib のロゴバナーを生成、表示するデモ。

  * デモというよりアートと呼びたい。

:file:`mathtext_asarray.py`
  クラス ``MathTextParser`` のデモ。

  * 冒頭の関数 ``rc`` 呼び出しが気になる。
  * ``MathTextParser`` オブジェクトをコンストラクターで生成する。
  * メソッド ``.to_png`` で指定した LaTeX の文字列を処理した結果を PNG ファイル
    に保存する。
  * メソッド ``.to_rgba`` で指定した LaTeX の文字列を処理した結果をオブジェクト
    にする。
  * メソッド ``Figure.figimage`` でそれを描画する。呼び出し側が RGB 値を正規化す
    る。

:file:`patch_collection.py`
  主に ``Wedge`` パッチのデモコード。
:file:`power_norm_demo.py`
  2D ヒストグラムで ``PowerNorm`` オブジェクトを渡すデモ。基本。

  * 関数 ``plt.hist2d`` を利用する。見てくれは画像プロットのようだ。このキーワー
    ド引数 ``norm`` にオブジェクト ``PowerNorm(gamma)`` を指定する。``gamma`` は
    適当なスカラー。

:file:`quad_bezier.py`
  二次 Bézier 曲線のデモコード。基本。

  * Path オブジェクトを生成するときに ``Path.CURVE3`` を適宜指示する。

:file:`radar_chart.py`
  レーダーチャートデモ。応用。

  * ``PolarAxes`` のサブクラスとして ``RadarAxes`` を定義する。必要なメンバーを
    オーバーライドする。
  * 関数 ``mpl.projections.register_projection`` にこの ``.name`` を指定する。

:file:`sankey_demo_basics.py`
  クラス ``Sankey`` のデモコード。

  * メソッド ``.add`` で矢印形状を追加できる。形状が確定したら ``.finish`` を呼
    ぶ。この戻り値を介して図式のスタイルを調整する。

:file:`sankey_demo_links.py`
  クラス ``Sankey`` のデモコード。メソッド ``.add`` を駆使して、たいへん長い
  Sankey 図を生成する。
:file:`sankey_demo_old.py`
  クラス ``Sankey`` を利用せず、自力で Sankey 図を描画するデモ。研究。
:file:`sankey_demo_rankine.py`
  クラス ``Sankey`` を利用して Rankine サイクルの図を描くという、かなり実践的な
  デモ。

  * メソッド ``.add`` の引数が複雑なので、何とかしたい。

:file:`scatter_piecharts.py`
  散布図のマーカーが円グラフというふざけたデモコード。

:file:`skewt.py`
  斜交座標系のデモコード。研究。

  * クラス ``XTick``, ``XAxis``, ``Spine``, ``Axes`` からそれぞれのサブクラスを
    定義する。
  * 関数 ``mpl.projections.register_projection`` に ``Axes`` のサブクラスの
    ``.name`` を指定する。

  * プロットデータの生成に ``np.loadtxt`` を使っているのが面白い。

  * メソッド ``Axes.semilogy`` で y 軸が対数寸法になる。
  * メソッド ``Axes.axvline`` は x 一定の線を引くものだが、このデモでは斜めにな
    る。
  * ``ScalarFormatter`` と ``MultipleLocator`` の使用例も見られる。

:file:`span_regions.py`
  クラス ``BrokenBarHCollection`` のデモコード。

  * メソッド ``Axes.axhline`` は y 一定の線を引く。

:file:`two_scales.py`
  プロットの両側に y 軸目盛を付けるデモコード。
:file:`unicode_minus.py`
  マイナス記号差し替えデモ。

  * ``rcParams['axes.unicode_minus'] = False`` とすると、マイナス記号に Unicode
    のそれを使わなくなる。代わりにハイフンになる。

:file:`watermark_image.py`
  図の背景に透かしを入れるデモ。

  * アルファチャンネルありの画像をメソッド ``Figure.figimage`` に渡す。

:file:`watermark_text.py`
  図の背景に透かしを入れるデモ。

  * 単にメソッド ``Figure.text`` の呼び出しでキーワード引数を ``alpha=0.5`` のよ
    うにすればよい。

:file:`axes_grid1`
----------------------------------------------------------------------

モジュール ``mpl_toolkits.axes_grid1`` に関連する見本の集まり。

:file:`demo_axes_divider.py`
  複数サブプロット、カラーバーの配置方法のデモ。

  * デモコード定義の関数 ``get_demo_image`` はプロット対象となるデータを NumPy
    の配列オブジェクトとして返す。この関数は他のデモコードでも登場する。
  * 最初のサブプロットでは単にデモデータを描画する。メソッド ``Axes.imshow`` で
    イメージを描画し、さらに関数 ``plt.colorbar`` でカラーバーを付属させる。
  * 次のサブプロットでは、先の処理をより複雑にすることでカラーバーの高さをイメー
    ジプロットのそれに合わせる。クラス ``SubplotDivider``, ``LocatableAxes``,
    ``Size`` とメソッド ``Figure.add_axes`` を使いこなす力量を要求される。
  * 次のサブプロットもやることは同じだが、手続きが簡略化した。関数
    `make_axes_locatable` をサブプロットに適用してレイアウトマネージャーのような
    ものを利用する。
  * 最後のサブプロットは同じイメージプロットを横一列に並べる。つまり、先の例でカ
    ラーバーの代わりに元のイメージプロットと同じものを置く。

:file:`demo_axes_grid.py`
  さらに複雑な複数サブプロットの配置方法のデモ。

  * 最初のサブプロット群は田の字に配置するもの。クラス ``ImageGrid`` に
    ``Figure`` オブジェクトを渡す。
  * 次のサブプロット群も田の字だが、カラーバーをひとつ付属させる。横長カラーバー
    が田の字の上部に出る。``ImageGrid`` コンストラクターの後半のキーワード引数が
    それを指示する。
  * 次のサブプロット群も田の字だが、カラーバーがそれぞれに付属する。
    ``ImageGrid`` の ``cbar_mode="each"`` がポイントだ。
  * 最後のサブプロット群も田の字。カラーバーも個別。ただしカラーバーの範囲をサブ
    プロットごとに変える。

:file:`demo_axes_grid2.py`
  ``ImageGrid`` のデモコード。

  * 最初のグループはサブプロットそれぞれにカラーバーを付属させる。``ImageGrid``
    の引数については以前のデモで理解できるだろう。
  * デモコード定義の関数 ``add_inner_title`` はサブプロット内にテキストを配置す
    る。主にクラス ``AnchoredText`` を利用するが、それ以外の機能はあまり馴染みが
    ない。
  * 次のグループはサブプロットにひとつのカラーバーを共有させる。``ImageGrid`` の
    ``cbar_mode="single"`` がポイントだ。

:file:`demo_axes_hbox_divider.py`
  サブプロットを並べて、それにまたがるようにテキストを入れるデモ？

  * モジュール ``mpl_toolkits.axes_grid1.axes_size`` にあるクラス ``AxesX``,
    ``AxesY``, ``Scaled``, ``Fixed`` を利用してレイアウトマネージャー的な役割が
    あるクラス ``HBoxDivider`` のオブジェクトを生成する。このマネージャーを最初
    に作った ``Axes`` のいずれにも ``set_axes_locator`` する。
  * テキスト部は実は ``Axes`` オブジェクト。メソッド ``Axes.annotate`` でテキス
    ト内容とレイアウト内容を指定する。

:file:`demo_axes_rgb.py`
  モジュール ``mpl_toolkits.axes_grid1.axes_rgb`` を利用したサブプロットの RGB
  分解のデモ。

  * 関数 ``make_rgb_axes`` でサブプロットから RGB 別のサブプロットを生成する。
  * デモコード内で定義された、画像から RGB 値を分解するコードの処理内容が理解で
    きない。謎のスライス。
  * クラス ``RGBAxes`` で ``Figure`` からサブプロットを内部に 4 つ持つサブプロッ
    トを生成するサブプロットそれぞれには ``.RGB``, ``.R``, ``.G``, ``.B`` でアク
    セスする。
  * この場合にはメソッド ``Axes.imshow_rgb`` で描画内容生成。

:file:`demo_colorbar_with_inset_locator.py`
  カラーバーを関数 ``mpl_toolkits.axes_grid1.inset_locator.inset_axes`` で実現す
  るデモ。

  * 関数 ``inset_axes`` で既存のサブプロットの内側に指定サイズの新規サブプロット
    を作成する。それから ``plt.colorbar`` のキーワード引数 ``cax`` としてそれを
    指定する。

:file:`demo_edge_colorbar.py`
  クラス ``AxesGrid`` のデモ。

  * 最初のグループではカラーバーを二個ずつ共有するデモ。下に付く。クラス
    ``AxesGrid`` を ``ImageGrid`` のように使うが、キーワード引数
    ``cbar_mode="edge"`` がポイント。
  * 次のグループではカラーバーを二個ずつ共有するデモ。右に付く。
  * ところで ``plt.get_cmap("autumn")`` 等が気になる。

:file:`demo_imagegrid_aspect.py`
  クラス ``ImageGrid`` のデモ。

  * コンストラクターの引数 ``aspect=True`` でアスペクト比を指定可能なオブジェク
    トを作成することを指示する？
  * アスペクト比自体は ``set_aspect`` を用いる。

:file:`inset_locator_demo.py`
  モジュール ``mpl_toolkits.axes_grid1.inset_locator`` のデモ。サブプロット内に
  別のサブプロットを入れる？

  * 関数 ``zoomed_inset_axes`` で既存のサブプロットから指定倍率を持つ新規サブプ
    ロットを作成する。

:file:`inset_locator_demo2.py`
  モジュール ``mpl_toolkits.axes_grid1.inset_locator`` のデモ。サブプロット内の
  一部を拡大して表示する。

  * 関数 ``mark_inset`` でこれらのサブプロットの位置関係を指定する。

:file:`make_room_for_ylabel_using_axesgrid.py`
  関数 ``mpl_toolkits.axes_grid1.axes_divider.make_axes_area_auto_adjustable``
  その他のデモ。サブプロットのマージン？の大きさを自動調整可能にする？
:file:`parasite_simple2.py`
  クラス ``SubplotHost`` のデモ？

  * ``SubplotHost`` のコンストラクターに ``Figure`` オブジェクトと寸法を指定す
    る。
  * あとは何をやりたいのかわからない。

:file:`scatter_hist.py`
  関数 ``mpl_toolkits.axes_grid1.make_axes_locatable`` のデモ。ヒストグラム二個
  と散布図一個をウィンドウに表示する。

  * まずは単に散布図を定義し、それを引数にして ``make_axes_locatable`` を呼ぶ。
    この戻り値オブジェクトのメソッド ``append_axes`` を呼び出して、散布図の上や
    右に新しくサブプロットを作成する。
  * 棒が横に伸びるヒストグラムを作るには ``hist`` の引数に
    ``orientation='horizontal'`` を指定する。

:file:`simple_anchored_artists.py`
  各種図形、特にモジュール ``mpl_toolkits.axes_grid1.anchored_artists`` にある図
  形要素をサブプロットに配置するデモ。

  * クラス ``AnchoredText`` は小さいテキストラベル。
  * クラス ``AnchoredDrawingArea`` はサブプロット内の小さな矩形。コンテナーとし
    て振る舞う。この例では ``Circle`` を別途作成し、自身の管理する
    ``add_artist`` により含める。
  * クラス ``AnchoredEllipse`` はサブプロットに所属する小さな楕円。
  * クラス ``AnchoredSizeBar`` はサブプロットに所属する「縮尺を表す線」。
  * 上記のクラスはすべて ``AnchoredOffsetBox`` の間接サブクラスである。オブジェ
    クトはどれも ``Axes.add_artist`` に渡すことになる。

:file:`simple_axesgrid.py`
  クラス ``ImageGrid`` のデモ。

  * ``ImageGrid`` のコンストラクターに ``Figure`` オブジェクトと格子の寸法を指定
    する。
  * ここでは適当に定義した線形データを ``imshow`` に渡している。

:file:`simple_axesgrid2.py`
  同じくクラス ``ImageGrid`` のデモ。画像を三分割してそれぞれを三つの格子それぞ
  れに描画する。

  * ``ImageGrid`` の引数で格子間の長さを指定する等する。
  * 画像の分割は単に NumPy の配列をスライスするだけで得られる。

:file:`simple_axisline4.py`
  座標軸の目盛ラベルデモ。サブプロットにサインカーブを描き、上辺は円周率単位で、
  下辺は 1 単位で目盛を付ける。

  * メソッド ``Axes.twin`` でサブプロット上辺の座標軸を表すオブジェクトが得られ
    るので、これに対して ``set_xticks``, ``set_xticklabels`` を操作する。

:file:`axisartist`
----------------------------------------------------------------------

モジュール ``mpl_toolkits.axisartist`` する見本の集まり。

:file:`demo_axisline_style.py`
  プロットの座標軸と枠線の処理方法についての見本。

  * クラス ``SubplotZero`` は図の内部にある ``Axes`` オブジェクトを生成・操作す
    るメソッドを与える。この見本ではオブジェクト ``fig`` から生成する。
  * 両座標軸ともに正の方向に矢印の矢先を描くために
    ``ax.axis[direction].set_axisline_style("-|>")`` する。

:file:`demo_curvelinear_grid.py`
  クラス ``Subplot``, ``SubplotHost``, ``GridHelperCurveLinear``,
  ``ParasiteAxesAuxTrans`` の見本。直交座標のプロットと極座標のプロットを描い
  て、それぞれにおいてグリッドや目盛をカスタマイズする。

  * かなり手が込んでいる。

:file:`demo_curvelinear_grid2.py`
  x 軸の目盛間隔が一様でないデモ？

  * 先ほどの見本もそうだが、クラス ``GridHelperCurveLinear`` の操作法が面倒そう
    だ。

:file:`demo_floating_axes.py`
  サブモジュール ``mpl_toolkits.axisartist.floating_axes`` デモ。三個のサブプ
  ロットを生成する。

  * サブプロット全体に affine 変換を施すことができる。それにはクラス
    ``Affine2D`` のオブジェクトを生成して適切な変換を定義しておく必要がある。そ
    れから別のオブジェクトに引き渡す。
  * 直交座標系の棒グラフでは ``floating_axes.GridHelperCurveLinear`` と
    ``floating_axes.FloatingSubplot`` を上手く使う。
  * バウムクーヘンのような極座標系の散布図では ``FixedLocator``,
    ``DictFormatter``, ``MaxNLocator`` の各クラスを利用して、座標軸の目盛ラベル
    をカスタマイズする。
  * 扇型の極座標系の散布図ではモジュール ``mpl_toolkits.axisartist.angle_helper``
    の機能を上手く使う。

:file:`demo_floating_axis.py`
  極座標？

  * Matplotlib 本体コードで ``RuntimeWarning`` が送出される。とりあえずサブプ
    ロットは表示されるが、この内容で正しいかは知らない。

:file:`demo_parasite_axes2.py`
  密度、温度、速度。何やら座標軸が多い。

  * 関数 ``mpl_toolkits.axes_grid1.host_subplot`` で生成したオブジェクトからメ
    ソッド ``twinx`` を二度呼び出す。

  * このデモはモノクロでわかりにくい。色を変えてみよう。

:file:`color`
----------------------------------------------------------------------

色に関係する処理の見本集。

:file:`colormaps_reference.py`
  ``Colormap Vega10 is not recognized`` というエラーが出て完全には動作しない。

  * 動作するものについては、色見本が画面に描かれる。

:file:`color_cycle_default.py`
  現在存在しない ``set_facecolor`` への参照があるコード。動作しない。
:file:`color_cycle_demo.py`
  RGBY と CMYK とでプロット曲線の色を変えていくデモ。

  * 関数 ``plt.rc`` の呼び出しでプロット曲線の特性を指定することができる。
  * またはメソッド ``Axes.set_prop_cycle`` を用いてもよい。

:file:`named_colors.py`
  現在存在しない ``BASE_COLORS`` への参照があるコード。動作しない。

:file:`event_handling`
----------------------------------------------------------------------

キーボードやマウス操作による対話的な処理をどう実現するかを示す見本集。

:file:`close_event.py`
  サブプロットのイベントハンドラーの指定方法を示すデモ。基本。

  * このデモではウィンドウを閉じるイベントを扱う。
  * メソッド ``Figure.canvas.mpl_connect`` を呼び出すことでサブプロットの「白い
    部分」上のイベントハンドラーを指定できる。引数にはイベント名を表す文字列と、
    発動される関数なり関数オブジェクトなりを渡す。

:file:`data_browser.py`
  マウスピック（クリック）およびキー押しイベントのデモ。

  * イベントハンドラーの signature の要件は、引数にイベントオブジェクトを取るこ
    とか。例えばキーイベントならば ``event.key`` に、マウスピックイベントならば
    ``event.mouseevent`` にそれぞれアクセスできる。
  * ``Axes.plot`` のキーワード引数 ``picker=5`` にも注意。これはマウスピック座標
    の余裕を指示する値である。CAD によくあるパラメーター。
  * 二点間の距離の平方を計測するのに関数 ``np.hypot`` を利用する。こんな便利なも
    のが存在していたか。
  * スクリプトの最後の if ブロック内に宣言された変数は Python 的には全て
    ``global`` 扱いであることに注意。

:file:`figure_axes_enter_leave.py`
  マウスカーソルの移動処理のデモ。``Figure`` と ``Axes`` の両方について。

  * イベント名は ``(axes|figure)_(enter|leave)_event`` のような文字列
    だ。``Axes`` についてのイベントハンドラーに渡されるオブジェクトには
    ``.inaxes`` が、``Figure`` についてのそれには ``.canvas`` が利用可能。
  * マウスカーソルのある要素に色が塗られる。これはメソッド
    ``.patch.set_facecolor`` を呼ぶ。

:file:`idle_and_timeout.py`
  アイドルイベントのデモだが、こういうことはしないで代わりに ``animation`` の機
  能を使うこと。

:file:`keypress_demo.py`
  キー押しイベント処理のデモ。基本。

  * キー :kbd:`X` を押すたびに x 軸ラベルが出たり消えたりするというもの。
  * イベント名は ``key_press_event`` で、ハンドラーでは引数オブジェクトの属性値
    ``.key`` を参照する。
  * ラベルの表示処理はメソッド ``.set_visible`` 等を利用する。

:file:`lasso_demo.py`
  いわゆる投げ縄選択のデモ。

  * そのまま実行すると例外 ``AttributeError: module 'matplotlib.colors' has no
    attribute 'to_rgba'`` が発生するので、これらの箇所にあるコードを書き換える必
    要がある（クラス ``ColorConverter`` を利用する）。
  * クラス ``Lasso`` を利用する。
  * イベントとしては ``button_press_event`` を使う。
  * 投げ縄を描く際にいろいろと面倒なことをしている。特に
    ``Figure.canvas.widgetlock`` が絡む処理が曲者。ある種のロック操作が含まれ
    る。

:file:`legend_picking.py`
  凡例部分のピックイベント処理デモ。凡例の線をピックすると、対応する折れ線（この
  デモでは折れはないが）の表示状態が切り替わる。

  * イベントとしては ``pick_event`` を使う。
  * 凡例を生成するにはメソッド ``Axes.legend`` を呼ぶ。戻り値が凡例オブジェク
    ト。
  * 凡例内の線にアクセスするには凡例に対するメソッド ``get_lines`` でよい。
  * 折れ線の表示処理はメソッド ``.set_visible`` 等を利用する。

:file:`looking_glass.py`
  マウスドラッグを実装するデモ。

  * 詳細は省くが、マウスイベントを三種類処理する。
  * 円と線群とが重なり合う部分については、線のほうの見え方を変えたい。これには線
    に対するメソッド ``.set_clip_path`` を用いる。

:file:`path_editor.py`
  Bézier 曲線の編集デモ。案外面倒なコードになっている。

  * ``draw_event`` というイベントがある。キャンバスの描画を自力で行うとでも言う
    のか。
  * 全体的に ``FigureCanvas`` のメソッド呼び出しが重要らしい。あまり見かけないも
    のもここでは利用する。
  * 初期状態ではこのパスは閉曲線に見えるが、実際には始点終点に対応する制御点（同
    じ座標だが）が一致しているだけの開曲線だ。

:file:`pick_event_demo.py`
  四種のサブプロット上におけるピック処理のデモ。基本。

  * ピックイベントの処理は ``pick_event`` という名前になる。
  * 最初のウィンドウでは点プロットと棒グラフをピックするデモ。ピックされたオブ
    ジェクトが ``Line2D`` なのか ``Rectangle`` なのか ``Text`` なのかでイベント
    オブジェクトから得られる属性情報が異なる。
  * 次のウィンドウも点プロットのピックデモ。ピックした座標を得るには ``.pickx``
    等を用いる。
  * メソッド ``Axes.plot`` のキーワード引数 ``picker`` に関数を渡す。この自作関
    数ではピック座標とその近傍のプロット点との距離をテストしているらしい。
  * 次のウィンドウでは散布図のピックのデモを行う。今度はメソッド
    ``Axes.scatter`` のキーワード引数 ``picker`` には True を指定する。
  * 最後のウィンドウは画像のピックデモ。メソッド ``Axes.imshow`` のキーワード引
    数 ``picker`` には True を指定する。

:file:`pick_event_demo2.py`
  点をピックすると、それに対応する元データを別ウィンドウで表示するデモ。

  * 元データは ``np.random.rand`` による。
  * ピックさせるデータは ``np.mean`` と ``np.std`` による。
  * ピックハンドラーの引数から得られる ``event.ind`` にはどうもプロット点列の配
    列としてのインデックス（複数）であるようだ。

:file:`pipong.py`
  後述の :file:`pong_gtk.py` が ``import`` するモジュール。
:file:`poly_editor.py`
  正多角形の頂点をマウスでドラッグするデモ。

  * :file:`path_editor.py` のデモとコードの構造が同じ。
  * ``Line2D`` や ``Polygon`` のキーワード引数 ``animated=True`` が気になる。
  * 角度ゼロ付近の頂点の配置が怪しい。

:file:`pong_gtk.py`
  準備不足なので ``ImportError: No module named 'gobject'`` となる。

:file:`resample.py`
  ビュー範囲を変えるとそれに連動してプロットの標本数を最適化して再描画するデモ？
  こちらの思うようには動作しないようだ。

:file:`test_mouseclicks.py`
  マウスボタンイベント処理のデモ。基本。

  * ダブルクリックかどうかはイベントハンドラーの引数オブジェクトの属性
    ``.dblclick`` でテストできる。

:file:`timers.py`
  タイマーのデモ。

  * これまでのイベントハンドラーと色合いが異なり、タイマーオブジェクトの生成が必
    要。
  * コメントアウトのコードも注意。

:file:`trifinder_event_demo.py`
  マウスポインターを含むプロット三角形をハイライトするデモ。面白い。

  * デモデータの構成コードは要研究。
  * クラス ``Triangulation`` を利用する。
  * このオブジェクトをプロットするには関数 ``plt.triplot`` を呼ぶ。
  * 終盤の ``Polygon`` オブジェクトは何だろうか。

:file:`viewlims.py`
  Mandelbrot 図形をズームインするデモ。

  * 図形の生成コードは ``Mandelbrot.__call__`` にあるこの 10 行程度に収まっている。
  * メソッド ``Axes.callbacks.connect`` でハンドラーを定義する。Qt 風に言うと
    signal を slot に connect する。
  * 素材の選択がある意味不適切な気がする。ズームしても元と変わらない。

:file:`zoom_window.py`
  散布図の拡大図を別ウィンドウで表示するデモ。

  * メソッド ``Axes.set_xlim`` 等を用いてビューの範囲を更新する。
  * 別ウィンドウは開きっぱなし。

:file:`images_contours_and_fields`
----------------------------------------------------------------------

画像およびベクトル場関連といったところか。

:file:`contourf_log.py`
  グラデーションになっていないが、意図通りか？コード量は多くはないが、どのステッ
  プの処理も珍しい。

  * 二変数 Gauss 分布関数が ``mlab.bivariate_normal`` として実装されている。
  * 関数 ``plt.contourf`` で等高線プロットを描画する。
  * 関数 ``plt.colorbar`` でカラーバーを図のそばに付属させる。

:file:`image_demo.py`
  ウィンドウに Lovelace 伯爵夫人の画像を表示する見本コード。

  * 画像の読み込みは関数 ``plt.imread`` で行い、戻り値を ``plt.imshow`` に渡せば
    よい。
  * ``plt.axis('off')`` して座標軸を非表示にしておく。

:file:`image_demo_clip_path.py`
  ウィンドウに Grace Hopper 准将の画像を表示する見本コード。

  * 円形にくり抜いてあるが、これは画像オブジェクトのメソッド ``set_clip_path``
    で行う。引数のパッチオブジェクトはここでは ``Circle`` オブジェクトを採用して
    いる。

:file:`interpolation_methods.py`
  色補間 18 種のカタログ。

  * 18 個ものサブプロットオブジェクトを ``plt.subplots(3, 6, ...)`` で生成してい
    る。
  * メソッド ``imshow`` のキーワード引数 ``interpolation`` に指定する文字列が
    Matplotlib から得られるとよいだろう。

:file:`interpolation_none_vs_nearest.py`
  色補間ナシと最近補間の比較デモ。

  * 補間 ``none`` がよく効くのは大きな画像を小さく表示するときで、
    補間 ``nearest`` がよく効くのは小さな画像を大きく表示するときらしい。
  * Matplotlib 自体の話題ではないのだが、スクリプト後半のコメントに PDF を PNG
    に変換する処理について、興味深いことが書かれている。

:file:`pcolormesh_levels.py`
  ``Axes.pcolormesh`` と ``Axes.contourf`` の比較デモ。メッシュ対点。

  * クラス ``mpl.colors.BoundaryNorm`` はカラーマップのインデックスを離散的な
    （整数の）区間に基いて生成する。このオブジェクトをメッシュプロット関数に渡す
    ので、メッシュのほうはモザイクっぽい見栄えになる。それに対して、点のほうは曲
    線的な等高線がくっきりと見える。
  * ``plt.tight_layout`` を呼び出し、上下のサブプロットの座標軸の目盛ラベルが重
    なり合わぬように、隙間を調整する。

:file:`streamplot_demo_features.py`
  ベクトル場プロットデモ。

  * メソッド ``Axes.streamplot`` で描画する。引数には座標とベクトルを意味する配
    列を必要とするものがある。

:file:`streamplot_demo_masking.py`
  ベクトル場プロットデモのはず。

  * 実行時に ``MaskedArrayFutureWarning`` がスクリプトから送出される。これを修正
    できるくらいに理解を深めたい。

:file:`streamplot_demo_start_points.py`
  不明。

  * ``ValueError: operands could not be broadcast together with shapes (6,)
    (100,) (6,)`` なる例外が送出される。これを修正できるくらいに理解を深めたい。

:file:`lines_bars_and_markers`
----------------------------------------------------------------------

ここには初歩的な見本コードがある。

:file:`barh_demo.py`
  水平棒グラフの見本。

  * 関数 ``plt.barh`` でデータを描画する。

:file:`fill_demo.py`
  プロット曲線と x 軸とで囲まれた領域に色を塗る単純なデモコード。

  * 単に関数 ``plt.fill(x, y)`` を呼び出すだけでよい。プロット曲線と閉領域の着色
    を同時に行う。

:file:`fill_demo_features.py`
  複数のプロット曲線と x 軸とで囲まれた領域に色を塗る単純なデモコード。

  * 関数 ``plt.fill`` の呼び出しが一度で済むことを理解すること。

:file:`line_demo_dash_control.py`
  プロット曲線を破線で描く方法を示す見本。

  * まずは ``plt.plot`` の引数に文字列 ``--`` を指定して破線にする。
  * これだけでも破線になるが、点描のパターンを ``set_dashes`` で細かく指定でき
    る。

:file:`line_styles_reference.py`
  プロット曲線の線スタイルのカタログ。

:file:`marker_fillstyle_reference.py`
  マーカースタイルのカタログ。

  * ``Line2D.fillStyles`` の要素が有効なスタイル。これをプロット関数の
    ``fillstyle`` として指定する。
  * マーカーはだいたいマルに縦線や横線が入った記号で、半円部が別の色で塗られてい
    る。

:file:`marker_reference.py`
  マーカースタイルのカタログ。塗りナシと塗りアリの二種類を展示するデモ。

  * マーカーを指示するのに有効な値は ``Line2D.markers``,
    ``Line2D.filled_markers``, ``Line2D.filled_markers`` から得られる。例えば：

    .. code:: ipython

       In [1]: Line2D.filled_markers
       Out[1]: ('o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd')

:file:`scatter_with_legend.py`
  凡例付き散布図のデモ。

  * 散布図のプロット関数は ``plt.scatter`` だ。
  * 凡例は関数 ``plt.legend`` を呼び出す。

:file:`misc`
----------------------------------------------------------------------

雑多なコード例を集積したディレクトリーだろう。すぐに動作しないコードもある。

:file:`contour_manual.py`
  クラス ``ContourSet`` のデモコード。
:file:`font_indexing.py`
  開発者向けコード。というより、フォントファイルがなくて動作しない。用意すれば動
  くだろう。
:file:`ftface_props.py`
  開発者向けコード。というより、フォントファイルがなくて動作しない。用意すれば動
  くだろう。
:file:`image_thumbnail.py`
  指定ディレクトリーにある全ての PNG ファイルからサムネイル画像を生成するデモ
  コード。モジュール ``mpl.image`` に PIL と似た機能があるようだ。
:file:`longshort.py`
  インターネットから CSV ファイルを取得して、データを読み込み、プロットを表示す
  るデモコード。

  * Python 標準ライブラリーの関数 ``urllib.request.urlretrieve`` でファイルをダ
    ウンロードする。
  * 関数 ``mpl.mlab.csv2rec`` で CSV データをオブジェクト化する。それから CSV
    データを編集する。
  * メソッド ``Figure.autofmt_xdate`` でラベルの日付文字列を適宜見やすくさせる。

:file:`multiprocess.py`
  Python の ``multiprocessing.Process`` と ``multiprocessing.Pipe`` を絡めたデモ
  コード。

  * ``matplotlib.use('GtkAgg')`` しているが、これが必要なのか。
  * ``ImportError: No module named 'gobject'`` が発生してダメ。

:file:`rasterization_demo.py`
  ビットマップ化関係か？

  * ダミーのメッシュプロットを生成するのに ``np.meshgrid`` が向いている。
  * ポイントは ``Axis.pclormesh`` の戻り値オブジェクトに対する
    ``set_rasterized(True)`` や ``set_zorder(-20)`` だろう。
  * 最後に関数 ``plt.savefig`` を呼び出して PDF, EPS, SVG ファイルを出力する。
  * 生成した SVG ファイルを Inkscape で開こうとしたらモッサリしてダメ。それ以外
    のファイルはそれぞれのビューワーで普通に閲覧できた。

:file:`rc_traits.py`
  ``ImportError: No module named 'traits'`` となってダメ。
:file:`rec_groupby_demo.py`
  ``AttributeError: module 'numpy' has no attribute 'string0'`` となってダメ。
:file:`rec_join_demo.py`
  ``AttributeError: module 'numpy' has no attribute 'string0'`` となってダメ。
:file:`sample_data_demo.py`
  ウィンドウに Lovelace 伯爵夫人の画像を表示する見本コード。

  * 関数 ``mpl.cbook.get_sample_data`` のデモコード。あとは ``plt.imread`` と
    ``plt.imshow`` を呼び出す。

:file:`svg_filter_line.py`
  プロットを SVG データ化し、かつ XML コードをそこへ追加するようなデモコード。

  * 関数 ``plt.savefig`` を ``BytesIO`` オブジェクトに対して作用させているのがポ
    イント。
  * Inkscape で開くと、折れ線グラフにドロップシャドウが付いているのが目視でき
    る。デモコードの後半部で、このエフェクトフィルターに相当する XML コード片を
    XML オブジェクトツリーに自力で挿入している。
  * ``UserWarning`` が発生するので、気になるかもしれない。

:file:`svg_filter_pie.py`
  コードの構造は上記デモコードと同様。円グラフ版。
:file:`tight_bbox_test.py`
  プロットをウィンドウだけでなく、さまざまな形式のファイルに出力するデモコード。

  .. code:: ipython

     In [1]: %run ./misc/tight_bbox_test.py
     saving tight_bbox_test.png
     saving tight_bbox_test.pdf
     saving tight_bbox_test.svg
     saving tight_bbox_test.svgz
     saving tight_bbox_test.eps

  * 関数 ``plt.savefig`` を用いる。ファイル形式は最初の引数のパス文字列の拡張子
    で自動判別されるらしい。
  * 関数呼び出し一発で PDF ファイルにプロットを出力できるのは強力。

:file:`mplot3d`
----------------------------------------------------------------------

立体的なモデルをウィンドウ上で表現する方法を示す見本集。

:file:`2dcollections3d_demo.py`
  プロット空間内にプロット曲線と散布図を描くデモ。基本。

  * 明示的な ``import`` 文 ``from mpl_toolkits.mplot3d import Axes3D`` が必要。
    この他のデモでも、コード中に明確に 3D 系クラスなり関数なりが出て来ない場合に
    はこのようなダミーの ``import`` 文を必要とする。
  * メソッド ``Figure.gca`` のキーワード引数が ``projection='3d'`` 必要。この戻
    り値のオブジェクトの型が ``Axes3D`` なのだろう。
  * メソッド ``Axes.plot`` にも ``Axes.scatter`` にもキーワード引数 ``zdir`` を
    指定する。この例ではサンプルデータは平面的なので、その平面の法線方向の座標成
    分を指示する。この事はこの他のデモコードすべてのプロット系メソッドに言える。
  * メソッド ``Axes3D.set_xlim3d`` 等でプロット空間の座標成分ごとの範囲を指定す
    る。
  * メソッド ``Axes3D.view_init`` でカメラの位置と姿勢を指示する。引数の与え方が
    難しそうだ。

:file:`bars3d_demo.py`
  平面的棒グラフを奥行き方向に配列するデモ。基本。

  * メソッド ``Figure.add_subplot`` のキーワード引数が ``projection='3d'`` 必
    要。

:file:`contour3d_demo.py`
  関数 ``axes3d.get_test_data`` を利用してプロット空間内に等高線図を描くデモ。基
  本。

  * メソッド ``Axes.contour`` に三次元分の点列を渡す。
  * メソッド ``ContourSet.clabel`` で等高線にラベルする。

:file:`contour3d_demo2.py`
  その等高線をリボン化するデモ。

  * メソッド ``Axes.contour`` のキーワード引数 ``extend3d=True`` とすることで、
    描画される等高線は高さ方向に幅広くなる。

:file:`contour3d_demo3.py`
  その等高線データをプロット曲面とその射影を等高線図として表現するデモ。

  * 曲面プロットはメソッド ``plot_surface`` による。三次元分の点列を渡す。
  * メソッド ``Axes.contour`` を ``zdir`` を各座標成分ごとに呼び出すことで、等高
    線プロットを各座標平面に射影する。このときキーワード引数 ``offset`` を指定し
    て、若干浮かせる。

:file:`contourf3d_demo.py`
  隣接する等高線同士でその対応する「高さ」部分を塗るデモ。基本。

  * メソッド ``Axes.contourf`` を用いる。

:file:`contourf3d_demo2.py`
  その等高線データをプロット曲面とその射影を等高線図として表現するデモ。塗りアリ
  版。

  * メソッド ``Axes.contourf`` を用いる。

:file:`custom_shaded_3d_surface.py`
  これは高級。

  * オブジェクト ``np.s_`` は配列の添字からなる ``tuple`` オブジェクトを生成する
    もの。
  * ここでクラス ``LightSource`` のコンストラクターに与えている実引数はそれぞれ
    方位角と仰角を指定する。
  * このオブジェクトについてメソッド ``shade`` を呼ぶことで色データ ``rgb`` を算
    出する。座標成分 z しか必要としない？
  * それから ``Axes.plot_surface`` を呼び出す。キーワード引数 ``facecolors`` に
    今得た RGB データを指定する。自分で色を与えるので ``shade=False`` とするのだ
    ろう。

:file:`hist3d_demo.py`
  3D 棒グラフのデモコード。基本。

  * 関数 ``np.histogram2d`` でヒストグラムデータを作成する。
  * さらに 16 本の棒の位置を決める配列を ``np.meshgdi`` 等で決める。
  * メソッド ``Axes.bar3d`` で棒グラフを描画する。注目したいのはキーワード引数
    ``zsort='average'`` で、この影響でビューをグリグリ回転させると、ある棒の辺と
    隣の棒の面との前後関係の描画が乱れることがある。

:file:`lines3d_demo.py`
  3D 曲線のデモコード。基本。

  * メソッド ``Axes.plot`` に三次元分の点列を渡す。

:file:`lorenz_attractor.py`
  Lorenz attractor を描画するデモ。

  * 点列を生成するコードはさすがに凝っているが、描画コードはたいへん基本的。

:file:`mixed_subplots_demo.py`
  同一 Figure に 2D の ``Axes`` と 3D の ``Axes`` を掲載するデモコード。

  * 二度目のメソッド ``Figure.add_subplot`` の呼び出しには、キーワード引数
    ``projection='3d'`` を指定する。

:file:`offset_demo.py`
  テキストをオフセットして描画するデモらしいが、見てもよくわからない。

  * メソッド ``Axes.plot_surface`` の x 軸と y 軸データの値が ``+ 1e5`` されてい
    る。これが要点らしい。

:file:`pathpatch3d_demo.py`
  テキストをプロット空間内に描画するデモ。これは参考用だ。

  * モジュール ``mpl_toolkits.mplot3d.art3d`` に関数 ``pathpatch_2d_to_3d`` というのがある。
  * ちなみに実行時間がけっこう長い。裏で LaTeX が起動する。

:file:`polys3d_demo.py`
  平面的折れ線グラフ（を輪郭とする多角形）を奥行き方向に配列するデモ。基本。

  * そのまま実行すると例外 ``AttributeError: module 'matplotlib.colors' has no
    attribute 'to_rgba'`` が発生するので、これらの箇所にあるコードを書き換える必
    要がある（クラス ``ColorConverter`` を利用する）。
  * メソッド ``Axes.add_collection3d`` をキーワード引数 ``zdir`` の指定と共に呼
    ぶ。ステンドグラス的な多角形は ``PolyCollection`` でよい。

:file:`quiver3d_demo.py`
  箙プロットのデモ。基本。

  * ``AttributeError: Unknown property normalize`` という例外が出るので、
    ``norm=True`` に修正する。
  * データとなるベクトル群の全始点を関数 ``np.meshgrid`` で一気に作成する。
  * メソッド ``Axes.quiver`` で箙プロットを描画する。

:file:`rotate_axes3d_demo.py`
  謎。

  * ``plt.show()`` が抜けているので補足したが、それでも謎。

:file:`scatter3d_demo.py`
  散布図デモ。基本。

  * メソッド ``Axes.scatter`` に三次元分の点列を渡す。

:file:`subplot3d_demo.py`
  曲面プロットデモ。基本。

  * メソッド ``Axes.plot_wireframe`` で曲面をワイヤーフレームで描画する。

:file:`surface3d_demo.py`
  曲面プロットデモ。基本。

  * ``Axes.zaxis`` にアクセスできることに注意。

:file:`surface3d_demo2.py`
  曲面プロットデモ。基本。
:file:`surface3d_demo3.py`
  曲面プロットにおいて面の各マスに色を指定するデモ。

  * メソッド ``Axes.plot_surface`` のキーワード引数 ``facecolors`` に色値からな
    る二次元配列を渡す。

:file:`surface3d_radial_demo.py`
  曲面プロットデモ。基本。

  * メソッド ``Axes.plot_surface`` は極座標は知らないので、そのような点データを
    呼び出し側で直交座標系に変換する必要がある。

:file:`text3d_demo.py`
  テキストデモ。基本。

  * メソッド ``Axes.text`` と ``Axes.text2D`` とがある。
  * キーワード引数 ``zdir`` にはベクトルを表す配列を渡すこともできる。

:file:`tricontour3d_demo.py`
  ``Triangulation`` および ``plt.tricontour`` のデモコード。曲面 tessellation に
  よる描画。3D CAD でよく見かける手法に似ている。

  * ある円周からクラス ``Triangulation`` を利用して三角形格子を得る。オブジェク
    ト ``triang.triangles`` は点列の添字三つ組の配列である。
  * メソッド ``Triangulation.set_mask`` で要らない三角形を指定？
  * 関数 ``plt.tricontour`` で tessellation をプロットする。ここで
    ``Triangulation`` オブジェクトと点列の z 成分配列を指定する。

:file:`tricontourf3d_demo.py`
  ``Triangulation`` および ``plt.tricontourf`` のデモコード。上のと同じ。
:file:`trisurf3d_demo.py`
  ``Axes.plot_trisurf`` のデモコード。

  * おそらく ``Axes.plot_trisurf`` に渡す点列データに何かの制約があると思われ
    る。そうでないと tessellate できない。
  * 引数に x, y, z および ``Triangulation`` オブジェクトを渡す方法と、
    ``Triangulation`` および z を渡す方法が許される。

:file:`trisurf3d_demo2.py`
  変わった曲面のデモ。
:file:`wire3d_animation_demo.py`
  ワイヤーフレーム曲面のアニメーションデモ。

  * ``MatplotlibDeprecationWarning`` が発生するが、気にしない。
  * 関数 ``plt.pause`` を利用。これがマズい。

:file:`wire3d_demo.py`
  ワイヤーフレーム曲面デモ。基本。
:file:`wire3d_zero_stride.py`
  ワイヤーフレーム曲面デモ。基本。

  * 曲面プロット系メソッドのキーワード引数 ``rstride`` や ``cstride`` にゼロを指
    定すると、曲面上の x または y の値が一定の曲線しか描かれない。

:file:`pie_and_polar_charts`
----------------------------------------------------------------------

円グラフと極座標グラフの見本コード集。

:file:`pie_demo_features.py`
  よくある円グラフの見本。

  * 円グラフはメソッド ``Axes.pie`` で実現する。
  * ``Axes.set_aspect('equal')`` をしないと、円が円に見えなくなる。
  * 扇型は既定では反時計回りに配列されていく。この振る舞いを変える方法もある。

:file:`polar_bar_demo.py`
  極座標系の中心から棒が伸びるようなグラフの見本。棒というか扇型になる。

  * これは ``plt.subplot`` の呼び出し時に ``projection='polar'`` を指定するのが
    本質的だ。
  * 謎のメソッド ``plt.cm.viridis`` で「棒」部分の色を決めている。これは色の見本
    コード集のところで学習しよう。

:file:`polar_scatter_demo.py`
  極座標グラフで散布図を実現する見本。

  * これも ``plt.subplot`` の呼び出し時に ``projection='polar'`` を指定する。
  * 散布図を実現するのはメソッド ``Axes.scatter`` だ。
  * サンプルデータは乱数。

:file:`pylab_examples`
----------------------------------------------------------------------

.. todo::

   調査する。

:file:`scales`
----------------------------------------------------------------------

グラフの各軸の目盛寸法を線形的だけではなく、対数的にも設定できる。詳しくは
``matplotlib.pyplot.Axes.set_yscale`` 等のヘルプを当たって欲しい。

:file:`scales.py`
  それぞれ異なる Y 軸の目盛寸法の特性のあるサブプロットを四つ描画し、同一データ
  をプロットする。

  * 寸法の種類は ``linear``, ``log``, ``symlog``, ``logit`` からなる。
    ``symlog`` はプラスマイナス対称であり、``logit`` はクリッピングあり。
  * プロットデータは Gauss 分布 ``np.random.normal(0.5, 0.4, 1000)`` を加工した
    ものとする。これでほぼ線形に分布した点列が得られる。この加工の技法にも注目し
    たい。

:file:`shapes_and_collections`
----------------------------------------------------------------------

:file:`artist_reference.py`
  Matplotlib の各種図表要素 (artists) の図解のようなものを描く見本コード。

  * モジュール ``mpl.patches`` には ``Circle``, ``Rectangle``, ``Wedge``,
    ``RegularPolygon``, ``Ellipse``, ``Arrow``, ``FancyBboxPatch`` という図表的
    要素クラスがある。
  * ``PatchCollection`` というクラスでこれらの要素を集約することができる。
  * レイアウトを微調整する関数 ``plt.subplots_adjust`` を忘れないでおきたい。

:file:`path_patch_demo.py`
  区分的 Bézier 曲線の構成方法の見本。``mpl.path.Path``, ``mpl.path.PathPatch``
  の利用法が理解できる。

:file:`scatter_demo.py`
  散布図の見本。

  * この見本コードが散布図を描画するもっとも単純なものだろう。
  * 与える点列データは座標だけでなく大きさと色も指定することができる。
  * 関数 ``plt.scatter`` による。

:file:`showcase`
----------------------------------------------------------------------

書籍に掲載されていても遜色のないイラスト群。

:file:`bachelors_degrees_by_gender.py`
  アメリカ合衆国における女性の専攻別学位授与率のプロット。

  * 見るべきところは多々あるが、とりわけ目を引くのはサンプルデータの出処である。
    関数 ``matplotlib.cbook.get_sample_data`` は面白そうだ。

:file:`integral_demo.py`
  典型的な定積分のイラスト。

  * 関数 ``plt.text`` 等 LaTeX 数式を指定できることは学習済み。
  * 求積領域の形状を ``Polygon`` を用いて表現する。

:file:`xkcd.py`
  謎のスケッチスタイル適用。

  * 棒グラフはメソッド ``Axes.bar`` で描画する。

:file:`specialty_plots`
----------------------------------------------------------------------

シェーディング（のようなもの）が関係する画像を生成する見本コード集。

:file:`advanced_hillshading.py`
  三種類の異なるデモを含むコード。

  * ``plt.cm.cupper`` という銅の色みを扱うオブジェクトがある。
  * モジュール ``mpl.colors`` にあるクラス ``LightSource`` のオブジェクトがメ
    ソッド ``shade`` で色の数値を評価する。
  * メソッド ``Figure.colorbar`` が色の棒をサブプロットの側に配置する。
  * モジュール ``mpl.colors`` にあるクラス ``Normalize`` のオブジェクトは与えら
    えた数値を指定範囲内に制限する。

:file:`hinton_demo.py`
  Hinton 図のデモコード。白と黒でさまざまな大きさの正方形を格子上に描画する。

  * これは面白いから Matplotlib 本体に組み込んでもよいのでは。
  * 関数 ``np.ndenumerate`` は馴染みがなかった。いつか活用したい。

:file:`topographic_hillshading.py`
  航空写真にありがちな地形に陰影を付けてプロット？するデモコード。

  * ``LightSource`` にそのものズバリのメソッド ``hillshade`` がある。この戻り値
    を ``Axes.imshow`` に引き渡す。
  * exaggregate (v.): 「誇張する」の意。

:file:`statistics`
----------------------------------------------------------------------

統計データに相性の良いプロット各種のデモコード。

:file:`boxplot_color_demo.py`
  箱プロットのデモ。

  * ダミーデータは ``np.random.normal`` を利用して生成。正規分布。
  * メソッド ``Axes.boxplot`` によるプロット。
  * キーワード引数 ``notch`` を指定すると、箱の形状が V 字型にえぐれる。

:file:`boxplot_demo.py`
  箱プロットにさまざまなオプションおよび描画スタイルを適用するデモ。

  * ダミーデータは ``np.random.lognormal`` を利用して生成。正規分布。
  * サブプロットを複数作成して、それぞれでメソッド ``Axes.boxplot`` をさまざまな
    オプションと共に呼び出す。ここでは ``showmeans``, ``showbox``, ``meanline``,
    ``showcaps``, ``notch``, ``bootstrap`` 等のキーワード引数を指定する。
  * 描画用の引数として ``boxprops``, ``flierprops``, ``medianprops`` がある。い
    ずれも ``dict`` オブジェクトを渡す前提だ。
  * メソッド ``Figure.suptitle`` で中央寄せの見出しを図に付ける。

:file:`boxplot_vs_violin_demo.py`
  バイオリンプロットと箱プロットの比較デモ。

  * メソッド ``Axes.violinplot`` によるプロット。ここでは ``showmeans=False,
    showmedians=True`` としている。これは隣のサブプロットに描く箱プロットととの
    比較をしやすくしているのだろう。
  * バイオリンプロットの一つのデータの形状は、なるほどバイオリンのような輪郭だ。

:file:`bxp_demo.py`
  プロットデータ計算と描画を分けて実現するデモ？

  * デモコードの働きは二つ上のデモコードと同じ。
  * 関数 ``mpl.cbook.boxplot_stats`` でサンプルデータから統計データ？を計算して
    おく。
  * 次にメソッド ``Axes.bxp`` でこのデータの箱＆ヒゲプロットを描画する。
    このメソッドの引数は ``Axes.boxplot`` とかなり共通している。

:file:`errorbars_and_boxes.py`
  メソッド ``Axes.errorbar`` のデモ。

  * このデモでは二次元のダミーデータを用いる。
  * 四角い部分の描画は ``PatchCollection`` オブジェクトによる。

:file:`errorbar_demo.py`
  関数 ``plt.errorbar`` の使い方を説明する基本的なデモ。

  * キーワード引数 ``xerr`` と ``yerr`` でそれぞれに対応する軸方向のアイビームの
    長さを指定する。

:file:`errorbar_demo_features.py`
  エラー部分の線を対称形にしたり非対称形にしたりするデモ。

  * 上のサブプロットはエラーを y 軸方向に、下のサブプロットは x 軸方向にそれぞれ
    表示する。
  * メソッド ``Axies.errorbar`` においてエラー量を指定する引数は ``xerr``,
    ``yerr`` である。
  * 意味はないが、下のサブプロットでは y 軸を対数グラフにしている。
    ``ax1.set_yscale('log')`` による。

:file:`errorbar_limits.py`
  エラー部分のさまざまなスタイル設定のデモ。

  * メソッド ``Axies.errorbar`` においてキーワード引数 ``uplims``, ``lolims``,
    ``xlolims``, ``xuplims`` を用いる。

:file:`histogram_demo_cumulative.py`
  累積的ヒストグラムのデモ。

  * ヒストグラムをプロットする関数は ``plt.hist`` だ。この引数の ``cumulative``
    に ``True`` を指定すれば累積的になるし、``-1`` を指定すれば逆累積ヒストグラ
    ムになる。

:file:`histogram_demo_features.py`
  別のページで説明したので省略。
:file:`histogram_demo_histtypes.py`
  ヒストグラムのデモ。

  * ``histtype='stepfilled'`` とするとビン同士の間の線がバーの色で塗りつぶされ
    る。
  * 第 2 引数にビンの幅の ``list`` オブジェクトを渡すと、ビン間隔が非一様なヒス
    トグラムが描ける。

:file:`histogram_demo_multihist.py`
  複数データを同一のサブプロットに描くデモ。

  ``stacked=True`` としたり、データそのものが入れ子の配列だったりといろいろなパ
  ターンがある。

:file:`multiple_histograms_side_by_side.py`
  複数のヒストグラムを同一サブプロット内で一列に並べるデモ。
:file:`violinplot_demo.py`
  バイオリンプロットのデモ。

  * メソッド ``Axes.violinplot`` のキーワード引数 ``showmedians``,
    ``showextrema``, ``showmeans``, ``bw_method`` のデモ。

:file:`style_sheets`
----------------------------------------------------------------------
モジュール ``mpl.pyplot.style`` の見本コード集。

:file:`plot_bmh.py`
  ヒストグラム重ねあわせ。

  * ``plt.style.use('bmh')`` を適用。これは `Bayesian Methods for Hackers` とい
    う書籍で用いられているテーマだそうだ。
  * 無意味なデータを生成するのに ``np.random.beta`` を利用。

:file:`plot_dark_background.py`
  プロットの背景を黒くするだけのデモ。

  * 単に ``plt.style.use('dark_background')`` するだけで実現できる。このとき、通
    常は黒塗りで描画される図表要素は白色で描画される。

:file:`plot_fivethirtyeight.py`
  特に変わったことはない？

  * ``plt.style.context('fivethirtyeight')`` を適用。この際に ``with`` ブロック
    を用いる。

:file:`plot_ggplot.py`
  サブプロット四個。

  * スタイルを `R <Bayesian Methods for Hackers>`__ の一般的なパッケージである
    :program:`ggplot` 風にするのに ``plt.style.use('ggplot')`` とする。
  * スクリプトの docstring の文言が笑える。いちおう許可は取ってあるのか。
  * 無意味なデータを生成するのに ``np.random.normal`` と ``np.random.randint``
    を利用。

:file:`plot_grayscale.py`
  サブプロット二個でグレースケール。

  * ``plt.style.use('grayscale')`` でよい。

:file:`subplots_axes_and_figures`
----------------------------------------------------------------------

:file:`fahrenheit_celsius_scales.py`
  一つのサブプロットに二種類の目盛を割り当てる見本。

  * メソッド ``Axes.twinx`` でもう一つの ``Axes`` を生成する。これと元の
    ``Axes`` を使い分けて華氏と摂氏の目盛を左右の Y 軸に描画する。
  * メソッド ``Axes.callbacks.connect`` の呼び出しは何だろう。

:file:`subplot_demo.py`
  サブプロットを二個同一ウィンドウに描画する見本。

  * ここでは関数 ``plt.subplot`` を ``(nrows, ncols, plot_number)`` 形式で呼び出
    す。オブジェクト指向的ではなく、状態機械的な手続きで各サブプロットの特性を操
    作する。

:file:`tests`
----------------------------------------------------------------------

:file:`backend_driver.py`
  見本ディレクトリー配下にあるかなりの数の見本スクリプトを、コマンドラインから指
  定されたバックエンドを用いて実行するためのスクリプトである。

  IPython セッションからの実行例を次に示そう。途中で :kbd:`Ctrl` + :kbd:`C` して
  中断した。

  .. code:: ipython

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

  * コマンドラインオプション ``-b`` でバックエンドを指定できる。
  * コマンドラインオプション ``-d`` でテスト対象とするサブディレクトリーを指定で
    きる。ただし、一部のディレクトリーにはサンプルコードの漏れがあると思われる。

:file:`text_labels_and_annotations`
----------------------------------------------------------------------

:file:`autowrap_demo.py`
  関数 ``plt.text`` のデモ。

  * この関数のキーワード引数はクラス ``Text`` の特性と対応している。例えば、キー
    ワード引数 ``wrap=True`` と指定することで、長いテキストを自動的に折り返して
    くれる。

:file:`rainbow_text.py`
  テキストの部分だけを着色するデモ。かなりの工夫をすることになるようだ。

  * ``mpl.transforms.offset_copy`` なる関数までも動員する。

:file:`text_demo_fontdict.py`
  テキストを入力とする Matplotlib の各種関数にはキーワード引数 ``fontdict`` があ
  り、利用するフォントの各情報を ``dict`` オブジェクトに詰め込める。
:file:`unicode_demo.py`
  テキストを入力とする Matplotlib の各種関数は Unicode を当然のように受け付け
  る。

:file:`ticks_and_spines`
----------------------------------------------------------------------

:file:`spines_demo.py`
  ``Axes`` は既定で四辺すべてに枠線が引かれるが、これを辺ごとに設定できることを
  示すデモ。

  * 私の見たところ ``ax1.spines['top'].set_visible(False)`` が効いていない。

:file:`spines_demo_bounds.py`
  さらに辺の一部だけに枠線を引くこともできる。

  * ``ax.spines['left'].set_bounds(-1, 1)`` がそれを実現する。

:file:`spines_demo_dropped.py`
  ``Axes`` の枠線を既定の位置からオフセットするようにずらすやり方を示すデモ。

  * ``ax.spines['left'].set_position(('outward', 10))`` のようにする。
  * プロット用ダミーデータとして乱数 ``np.random.uniform`` を利用。

:file:`ticklabels_demo_rotation.py`
  目盛のラベル文字を決めるデモ。

  * メソッド ``Axis.set_major_formatter`` 等を使う。さらにクラス
    ``FuncFormatter`` の利用と自作の書式設定関数の作成が必要となる。
  * メソッド ``Axis.set_major_locator`` で目盛ラベルの出現に制約をつける。

:file:`tick_labels_from_values.py`
  目盛のラベルを決めるデモ。

  * 関数 ``plt.xticks`` の二番目の引数として、ラベル文字列からなる ``list`` オブ
    ジェクトを引き渡すことで指定できる。

:file:`units`
----------------------------------------------------------------------

このディレクトリーの見本コード群はモジュール :file:`basic_units.py` を定義してお
き、それ以外のスクリプトがこれを ``import`` するという構造である。

:file:`basic_units.py`
  難しいコードだ。これを理解するのが本題だ。

  * 一般利用者が理解するという目的からすると、必要以上に複雑になっている可能性が
    ある。

以下はこのモジュールを応用するデモコードだ。

:file:`annotate_with_units.py`
  距離単位オブジェクトの利用を除けば、注釈矢印のデモコード。一方の矢印は単位系を
  全て ``basic_units.cm`` で明示し、他方はラベル座標の単位系を無次元単位で指定し
  ているというもの。

  * さらに両者の引数 ``textcoords`` の値が異なることに注意。前者は ``data`` つま
    り注釈されるオブジェクトの座標系が適用されるのに対して、後者は ``axes
    fraction`` つまりサブプロット領域の正規化座標系が適用される。

:file:`artist_tests.py`
  ``Line2D`` 等が座標変換を扱えることを示すデモコード。

  * メソッド ``Axis.set_units`` に ``basic_units.cm`` を引き渡す。
  * ``Line2D``, ``Rectangle``, ``Text`` それぞれについて、オブジェクトの位置や長
    さをやはり ``basic_units.cm`` を用いて指定する。

:file:`bar_demo2.py`
  同一データを座標軸ごとに単位系の異なる複数のサブプロットに描くデモコード。

  * 先頭に ``cms = cm * np.arange(0, 10, 2)`` というオブジェクトが現れる。これを
    いずれのサブプロットにおいても棒グラフで描く。
  * メソッド ``Axes.bar`` のキーワード引数 ``xunits`` と ``yunits`` について単位
    オブジェクト ``basic_units.cm`` や ``basic_units.inch`` を指定する。

:file:`bar_unit_demo.py`
  棒グラフだが、データは人間の身長の統計のようだ。

  * モデルデータに単位オブジェクトを含める。
  * サブプロットの y 軸にだけ ``Axis.set_units`` に ``basic_units.cm`` を引き渡す。
  * あとはメソッド ``Axes.autoscale_view`` が適宜調整してくれるようだ。

:file:`ellipse_with_units.py`
  同じ形状を定義した上で ``Ellipse`` と ``Arc`` を比較する。

  * 中心、長径、短径のすべてを ``basic_units.cm`` で定義する。
  * サブプロットの座標系単位系は明示的に指定しない。

:file:`evans_test.py`
  このデモは :file:`basic_units.py` を必要としない。

  * コードの前半はモジュール ``mpl.units`` にカスタム単位を登録する方法の見本
    だ。ユーザーがクラスを二個書く必要があるようだ。
  * コードの後半は単位のついたデータ量を、サブプロットに対しては直接単位系を指定
    せずにプロットする。

:file:`radian_demo.py`
  ``basic_units.radians`` と ``basic_units.degrees`` のデモコード。

  * 二つサブプロットを用意しておき、メソッド ``Axes.plot`` のキーワード引数
    ``xunits`` に一方は ``radians`` を、他方には ``degrees`` を指定してプロット
    する。その結果、座標軸の目盛ラベルがそれぞれ違って見える。

:file:`units_sample.py`
  ``basic_units.cm`` と ``basic_units.inch`` のデモコード。

  * サブプロットを四個用意して、それぞれのメソッド ``Axes.plot`` の呼び出しに対
    してキーワード引数 ``xunits`` および ``yunits`` に考えられる組み合わせで単位
    を指定する。

:file:`units_scatter.py`
  散布図の y 軸にだけカスタム単位を適用するデモコード。

  * サンプルデータの単位は ``basic_units.secs`` とする。
  * メソッド ``Axes.scatter`` の ``yunits`` は ``basic_units.secs`` とする。
  * 一番下のサブプロットだけメソッド ``Axis.set_units`` を呼び出して
    ``basic_units.herz`` を指定する。
  * NumPy から ``UserWarning: Warning: converting a masked element to nan.`` が
    生じるが、気にしないでおく。

:file:`user_interfaces`
----------------------------------------------------------------------

Matplotlib は wxPython, PyGTK, Tkinter, PyQt4/5 の GUI アプリケーションに直接埋
め込むことができることを示すデモコードの集まり。ここでは私の環境で実行できたデモ
コードをコメントする。

:file:`embedding_in_gtk.py`
  要 GTK につき実行できない。
:file:`embedding_in_gtk2.py`
  要 GTK につき実行できない。
:file:`embedding_in_gtk3.py`
  要 GTK につき実行できない。
:file:`embedding_in_gtk3_panzoom.py`
  要 GTK につき実行できない。
:file:`embedding_in_qt4.py`
  クラス ``matplotlib.backends.backend_qt4agg.FigureCanvasQTAgg`` のサブクラス化
  のデモ。

  * PyQt4 だけでなく PyQt5 もインストールされている環境で実行すると
    ``RuntimeError: the PyQt4.QtCore and PyQt5.QtCore modules both wrap the
    QObject class`` という例外が発生する。

:file:`embedding_in_qt4_wtoolbar.py`
  クラス ``matplotlib.backends.backend_qt4agg.NavigationToolbar2QT`` のデモ。実
  行するとツールバーが下部に付いたウィンドウが表示される。

  * PyQt4 だけでなく PyQt5 もインストールされている環境で実行すると
    ``RuntimeError: the PyQt4.QtCore and PyQt5.QtCore modules both wrap the
    QObject class`` という例外が発生する。
  * 警告 ``MatplotlibDeprecationWarning: This module has been deprecated in 1.4
    ...`` が出現する。
  * クラス ``FigureCanvasQTAgg`` をこのデモでも当然利用する。このオブジェクトの
    生成時に ``Figure`` オブジェクトを渡す。キャンバスは ``QVBoxLayout`` に渡
    す。
  * メソッド ``on_draw`` でいちいちサブプロットを生成、描画する。
  * キーイベントは ``on_key_press`` で処理する。ただしツールバー自体も処理したい
    ようなので、そちらにもイベントを横流しする。例えば :kbd:`S` を押すと、ファイ
    ル保存ダイアログボックスが現れる。

:file:`embedding_in_qt5.py`
  クラス ``matplotlib.backends.backend_qt5agg.FigureCanvasQTAgg`` のサブクラス化
  のデモ。

  * 最初のモジュールインポート文の感じが :file:`embedding_in_qt4.py` と異なる。
  * サブクラスとして ``MyMplCanvas``, ``MyStaticMplCanvas``,
    ``MyDynamicMplCanvas`` を定義する。最初のクラスは残りのもののスーパークラス
    とする。ここで Matplotlib の ``Figure`` や ``Axes`` オブジェクトを保持し、
    Qt のウィンドウオブジェクトの設定を行う。
  * クラス ``MyStaticMplCanvas`` では単純な正弦波をプロットする。
  * クラス ``MyDynamicMplCanvas`` では Qt のタイマークラスを用いて折れ線プロット
    のアニメーションを実現する。
  * クラス ``ApplicationWindow`` は Qt アプリケーションでよく見られる
    ``QMainWindow`` のサブクラス。ウィンドウ部品を手動でレイアウトしたり、メ
    ニューアイテムを実装したりする。
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
  要 wxPython 2.8.12 以上とのことなので実行できない。エラーメッセージが他のもの
  と少々異なる。
:file:`embedding_webagg.py`
  簡単なプロットをブラウザーに表示し、いつものウィンドウでの簡単な操作に加え、各
  種フォーマットのファイルをダウンロードすることが可能なことを示すデモ。

  * 要 Tornado とのこと。実行してみたらファイアーウォールの解除も必要なことがわ
    かる。
  * モジュール ``matplotlib.backends.backend_webagg_core`` からクラスと関数を
    ``import`` する。
  * クラス ``MyApplication`` をクラス ``tornado.web.Application`` のサブクラスと
    して定義する。ここは Tornado を学習しないことには何とも言えない。Matplotlib
    の ``Figure`` オブジェクトを関数 ``new_figure_manager_given_figure`` に渡
    す。このオブジェクト ``figure`` が HTML ファイルの対応する部分に埋め込まれ
    る。
  * ``MyApplication`` のコンストラクターでクラス ``FigureManagerWebAgg`` のクラスメ
    ソッド ``get_static_file_path`` を用いる。
  * ``MyApplication`` の内部クラス ``WebSocket`` が明らかに重要そうなのだが、私
    にはコードの意味がはっきりとわからない。
  * スクリプト実行後に出力される URL をブラウザーに与えればプロットが現れる。

:file:`fourier_demo_wx.py`
  要 wxPython 2.8.12 以上とのことなので実行できない。
:file:`gtk_spreadsheet.py`
  要 GTK につき実行できない。エラーメッセージが他のものと少々異なる。
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
  SVG ファイルにヒストグラムを出力し、そこにある凡例の棒をクリックするとプロット
  上の対応する棒の表示状態が切り替わるというデモ。SVG ファイルに JavaScript を埋
  め込むので、動作確認にはそれなりのブラウザーが必要。

  * プロット部品に対してメソッド ``.set_gid`` を呼び出すことで SVG 要素用の ID
    を適宜割り振っていく。
  * 関数 ``plt.savefig`` にキーワード引数 ``format="svg"`` を指定することでファ
    イル風オブジェクトにプロットの内容を SVG 形式で出力する。
  * 後半は Python 標準ライブラリーにあるクラス ``xml.etree.ElementTree`` の機能
    を利用。 SVG 要素としてのパッチ要素にイベントハンドラーを属性値として設定す
    る。
  * JavaScript のコードテンプレートを here string で書いて（デモなので）実引数を
    与える。関数 ``json.dumps`` はこういう使い方もするのか。
  * 最後に ``ElementTree`` オブジェクトを生成して直ちにメソッド ``write`` を用い
    てSVG ファイルを保存する。

:file:`svg_tooltip.py`
  SVG ファイルに図形を含むプロットを出力し、そこにある図形の上にマウスポインター
  を重ねるとツールチップが出現するというデモ。デモ :file:`svg_histogram.py` と共
  通するところが多い。
:file:`toolmanager.py`
  要 GTK につき実行できない。
:file:`wxcursor_demo.py`
  要 wxPython 2.8.12 以上とのことなので実行できない。

:file:`widgets`
----------------------------------------------------------------------

ウィンドウ部品のデモコード一式。GUI の学習はここから始めてよい。

:file:`buttons.py`
  プッシュボタンのデモ。ボタンを押すたびに波形の振動数が増減する。

  * ここでは関数 ``plt.axes`` をボタンを配置する空間を確保するものとして利用して
    いる。戻り値を ``Button`` コンストラクターの引数に使う。
  * メソッド ``Button.on_clicked`` に押された時に呼び出される振る舞いを指定す
    る。
  * 関数 ``plt.draw`` でサブプロットを更新描画する。

:file:`check_buttons.py`
  チェックボックスのデモ。チェックボックスに対応する波形の表示が切り替わる。

  * スペース確保とイベントハンドラー周りのコードは前回同様。
  * クラス ``CheckButtons`` のコンストラクターには場所とラベルに加えて初期状態も
    指定する。
  * プロットオブジェクトには ``visible`` のような属性があって、これを関連メソッ
    ドで操作する。また、生成時にもキーワード引数で初期値を指示できる。

:file:`cursor.py`
  マウスカーソルの位置に追従してサブプロット上にクロスヘアを描くデモ。

  * ``AttributeError: Unknown property facecolor`` という例外が生じるので、これ
    を引き起こすコードを削除しておく。
  * クラス ``Cursor`` のコンストラクターを適当に呼び出すだけでよい。

:file:`lasso_selector_demo.py`
  このデモは期待通りに動作しない。投げ縄選択で水玉を囲むデモだと思われる。
:file:`menu.py`
  メニューのデモ。

  * ``AttributeError: module 'matplotlib.colors' has no attribute 'to_rgba'`` 例
    外が生じる。これを解決するために、クラス ``colors.ColorConverter`` のオブ
    ジェクトを導入しておく。
  * コードがたいへん込み入っている。未知のクラスを相当利用したデモコードだ。
  * クラス ``MenuItem`` を ``artist.Artist`` のサブクラスとしてここで実装してい
    る。それ以外のユーザー定義クラスは全てが ``object`` からのサブクラスだ。
  * イベントハンドラーの定義はメソッド ``fig.canvas.mpl_connect`` から行う。

:file:`multicursor.py`
  マウスカーソルの位置に追従して二つのサブプロット上に縦線を描くデモ。

  * クラス ``MultiCursor`` の最初の引数に ``fig.canvas`` を指定する。次の引数に
    は対象のサブプロットを含む ``list`` または ``tuple`` を指定する。

:file:`radio_buttons.py`
  ラジオボタンのデモ。各項目に対応する波形の描画スタイルが切り替わる。

  * クラス ``RadioButtons`` を使うコードの構造は ``Button`` や ``CheckButtons``
    とよく似る。
  * ``AttributeError: Unknown property facecolor`` という例外が生じるので、
    これを引き起こすコードを削除しておく。

:file:`rectangle_selector.py`
  マウスによる矩形領域選択のデモ。

  * クラス ``RectangleSelector`` を用いる。
  * イベントハンドラーの指定がこれまでと異なる。まず ``RectangleSelector`` コン
    ストラクターの引数に一個、次に関数 ``plt.connect`` を呼び出してもう一個、と
    いう感じだ。前者のハンドラーはマウス操作のコールバックとして、後者のハンド
    ラーはキー操作のコールバックとして指定する。

:file:`slider_demo.py`
  ``Slider`` と ``RadioButtons`` のデモ。

  * ``AttributeError: Unknown property facecolor`` という例外が生じるので、これ
    を引き起こすコードを削除しておく。
  * クラス ``Slider`` の使い方はこれまでの widget と大体同じ。イベントハンドラー
    は ``on_changed`` となる。

:file:`span_selector.py`
  サブプロット上の横幅をマウスで選択するデモ。

  * クラス ``SpanSelector`` を用いる。
  * ``AttributeError: Unknown property facecolor`` という例外が生じるので、
    これを引き起こすコードを削除しておく。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
