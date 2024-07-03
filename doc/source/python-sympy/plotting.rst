======================================================================
プロットを利用する
======================================================================

ここでは SymPy_ プロット機能に関する覚え書きを記す。

.. contents:: ノート目次

所感
======================================================================

なぜ便利か。NumPy_/SciPy_ で（数学的な）関数のプロットを作成しようものなら、自分
で関数を評価して「折れ線化」して得られる点列データを Matplotlib_ のプロット関数
に渡す。その折れ線の点列をプロット関数に渡す。ところが SymPy では数式そのものを
プロット関数に渡せばよい。手間がひとつ省ける。

* SymPy でも 2D または 3D のプロットを描ける。
* プロット描画を実現するために Matplotlib が裏で働いている。

  * パッケージをインストールしていない場合は ``TextBackend`` という別の手があ
    る。

* 関数をインポートする形式は :code:`from sympy.plotting import plotxxx` となる。
* 関数 ``plot_implicit`` だけは不等式をも扱える。不等式に対応する等式を表現する
  曲線によって定義される平面上の領域を塗りつぶした図が得られる。
* 3D プロットは描画が重く感じられる。Matplotlib でもこうだったか。
* Matplotlib をラップしているのはわかるが、SymPy は設定ファイル
  :file:`$HOME/.matplotlib/matplotlibrc` を参照しないのか？
* :program:`isympy` でプロットウィンドウを複数出すと、たいていの場合セッションが
  おかしくなる。そして Tk のウィンドウが閉じられなくなる。

  .. todo::

     ここにコンソールの出力をコピーする。

早見表
======================================================================

プロット関数早見表
----------------------------------------------------------------------

手軽にプロットを描くための関数の早見表を下に示す。

======================================== ============================================================================================
関数                                     呼び出しの形
======================================== ============================================================================================
``plot``                                 :code:`plot(expr, range, **kwargs)`
                                         :code:`plot(expr1, expr2, ..., range, **kwargs)`
                                         :code:`plot((expr1, range), (expr2, range), ..., **kwargs)`
``plot_parametric``                      :code:`plot_parametric(expr_x, expr_y, range, **kwargs)`
                                         :code:`plot_parametric((expr1_x, expr1_y), (expr2_x, expr2_y), range, **kwargs)`
                                         :code:`plot_parametric((expr_x, expr_y, range), ..., **kwargs)`
``plot_implicit``                        :code:`plot_implicit(expr)`
                                         :code:`plot_implicit(expr, (xsymbol, xmin, xmax), (ysymbol, ymin, ymax))`
``plot3d``                               :code:`plot3d(expr, range_x, range_y, **kwargs)`
                                         :code:`plot3d(expr1, expr2, range_x, range_y, **kwargs)`
                                         :code:`plot3d((expr1, range_x, range_y), (expr2, range_x, range_y), ..., **kwargs)`
``plot3d_parametric_line``               :code:`plot3d_parametric_line(expr_x, expr_y, expr_z, range, **kwargs)`
                                         :code:`plot3d_parametric_line((expr_x, expr_y, expr_z, range), ..., **kwargs)`
``plot3d_parametric_surface``            :code:`plot3d_parametric_surface(expr_x, expr_y, expr_z, range_u, range_v, **kwargs)`
                                         :code:`plot3d_parametric_surface((expr_x, expr_y, expr_z, range_u, range_v), ..., **kwargs)`
======================================== ============================================================================================

プロット関数引数メモ
----------------------------------------------------------------------

プロット関数の引数の与え方には一貫性があるので、まとめて理解することができる。

* 引数 ``expr`` は SymPy の式オブジェクトである。
* 引数 ``range`` はいずれも :code:`(x, xmin, xmax)` の形式で与える。例えば
  :code:`(x, 0, 10)` のようにする。
* キーワード引数 :code:`**kwargs` は、次の三つに分類できる：

  #. プロット関数自身に関するパラメーター
  #. プロットの見てくれを制御するパラメーター
  #. プロットの種類で決まるパラメーター

プロット関数自身に関するパラメーター
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

プロット関数自身に関するパラメーターは全プロット関数の ``**kwargs`` が扱う。その
ようなキーワード引数を次の表に示す：

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   キーワード引数 @ 説明
   ``show``@プロットを表示するかどうかを指定する ``bool`` 値。

プロットの見てくれを制御するパラメーター
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

プロットの見てくれを制御するパラメーターは全プロット関数の ``**kwargs`` が扱う。
そのようなキーワード引数を次の表に示す：

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   キーワード引数 @ 説明
   ``aspect_ratio``@プロットのアスペクト比を例えば :code:`(1.0, 1.0)` のようにするか、または文字列 ``auto`` で指定する。
   ``autoscale``@Matplotlib の :code:`Axes.set_autoscale_on` に渡す ``bool`` 値。
   ``axis``@Matplotlib の :code:`Axes.set_axis_off` を呼ぶかどうかを指定する ``bool`` 値。
   ``axis_center``@プロットの中央の座標を例えば :code:`(0.0, 0.0)` のように指定するか、文字列 ``'center'`` または ``'auto'`` で指定する。
   ``legend``@プロットの凡例を表示するかどうかを指定する ``bool`` 値。
   ``margin``@Matplotlib の :code:`Axes.set_xmargin` と :code:`Axes.set_ymargin` に共通に渡す値。
   ``title``@プロットの表題を文字列で指定する。
   ``xlabel``@x 軸のラベル文字列。
   ``xlim``@x 軸の制限範囲を例えば :code:`(0.0, 10.0)` のようにして指定する。
   ``xscale``@x 軸のスケーリングをどうするか。文字列 ``'linear'`` または ``'log'`` で指定する。
   ``ylabel``@``xlabel`` の y 軸版。
   ``ylim``@``xlim`` の y 軸版。
   ``yscale``@``xscale`` の y 軸版。

プロットの種類で決まるパラメーター
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ここで言うプロットの種類で決まるパラメーターとは、それぞれのプロット関数が処理す
るサンプルデータの種類によって意味を持つものだ。見たらわかるので、例えば「キー
ワード引数 ``surface_color`` は曲面プロット系の関数でのみ有効なパラメーターであ
る」というようなことはいちいち断らずに、下の表でそれらをすべて混ぜて示す。

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   キーワード引数 @ 説明
   ``adaptive``@もし ``False`` を指定するならば、別途 ``nb_of_points`` を指定する必要がある。
   ``depth``@adaptive algorithm の深さを正の整数で指定する。
   ``label``@不明。Matplotlib の折れ線に付与するラベル？
   ``line_color``@プロットする線セグメントの色を指定する。要調査。
   ``nb_of_points``@サンプル点列の個数を整数で指定する。変域から一様にサンプリングされる。
   ``nb_of_points_x``@``nb_of_points`` の曲面プロット系 x 軸版。
   ``nb_of_points_y``@``nb_of_points`` の曲面プロット系 y 軸版。
   ``only_integers``@プロットのサンプリングを整数座標に限るかどうかを指定する ``bool`` 値。
   ``surface_color``@プロットする面パッチの色を指定する。要調査。
   ``steps``@要調査。

.. todo::

   adaptive algorithm というものを調べる。

* ``line_color``, ``surface_color`` の値の与え方は複数ある。両者の違いは次元だけ
  だろうから、以下 ``line_color`` の覚え書きを記す。

  * 差し当たり :code:`line_color=(1.0, 0.0, 0.0)` のように与えると、線の色が赤く
    なることを確認した。
  * または ``float`` 値を返す関数を渡すと動作することは確認した。しかし、浮動小
    数点型の数を返す関数からどのように線の色が決まるのかがわからない。SymPy の実
    装を見ても理解できないのでダメだ。

    .. code:: python3

       plot(sin(x), (x, -pi, pi), adaptive=False, line_color=lambda a: sin(a))

    簡単なサインカーブのプロットで ``line_color`` のはたらきを見ると、何らかの規
    則に基づいて線の色が決まっているらしいことは納得した。

    .. figure:: /_images/sympy-plotting-line-color.png
       :align: center
       :alt: SymPy によるプロット
       :width: 815px
       :height: 615px
       :scale: 50%

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
