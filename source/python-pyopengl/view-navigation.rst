======================================================================
回転とズーム
======================================================================
本稿では前回のプログラム（:doc:`./transform`）に、3D モデリングソフトの UI にありがちなビュー処理機能を実装する。
特に、マウスドラッグ風のジェスチャーによる、対象モデルへの回転変換と、カメラのズームイン・ズームアウトを実現する。

.. contents::

方針
======================================================================
* 例によって、前回プログラムのメインクラスに対してサブクラスを定義する。ここでは
  ``ShaderDemoApp`` から ``ViewNavigationDemoApp`` というサブクラスを派生させることとする。

* モデルの回転に関して、次の点を考慮する。

  * 頂点シェーダーを少々変更することで、モデルの回転をサポートする。
    ``uniform mat4`` 変数を新たに追加し、シェーダー外からアクセスする。
  * とりあえず左クリックドラッグ時に動的にビューが回転するようにする。
  * マウスジェスチャーで回転を加算的に表現するのに便利な四元数オブジェクトを導入する。

* カメラのズームに関して、次の点を考慮する。

  * とりあえず右クリックドラッグ時に、動的にカメラのズームを機能させる。
  * 頂点の射影変換が透視変換なので、fovy の値を上下によりズーム率の変更とする。

* マウスジェスチャーを 2 種類実装するという見方ができるので、一連のクラス階層を実装する。

準備
======================================================================
サブクラス ``ViewNavigationDemoApp`` の定義を含むスクリプトを書くこと以外の手順をまとめる。

Quaternion をインストールする
----------------------------------------------------------------------
四元数を自作するとえらいことになるのが目に見えているので、どこかに既にあればそれを拝借するのがよい。
毎度おなじみ pip で調べてみる。

.. code-block:: console

   $ pip search quaternion
   qmath                     - qmath provides a class for deal with quaternion algebra and 3D rotations.
     Root evaluations and Moebius transformations are implemented.
   Quaternion                - Quaternion object manipulation
   quaternion-algebra        - Quaternion algebra for Python.
   quaternionarray           - Python package for fast quaternion arrays math
   mathutils                 - A general math utilities library providing Matrix, Vector, Quaternion, Euler and Color classes, written in C for speed.
   Pyternion                 - Pythonic Quaternion library including Euclidean geometry calculations
   euclid                    - 2D and 3D vector, matrix, quaternion and geometry module
   euclid3                   - 2D and 3D vector, matrix, quaternion and geometry module. updated to python 3.
   pypoints.py               - Classes to represent points, pointsets, anisotropic arrays, and quaternions

私は一番名前の短い ``Quaternion`` をインストールした。Smithsonian Astrophysical Observatory の作品だ。

ポイントをいくつか記す。

* ``np.array`` ベースで実装されている。
* コンストラクターで四元数の全成分を直接指定できるが、その順番がベクトル部、スカラー部なので注意。
* プロパティー ``.transform`` で、四元数に対応する回転行列にアクセスする。
* プロパティー ``.q`` で、四元数の成分にアクセスする。

マウスモーションによるビューの変換を実装する
----------------------------------------------------------------------
以下に示すような機能を持つモジュールを作成する。ここで定義したサブクラスを後述のスクリプトからインポートするのだ。

クラス ``AbstractViewNavigation``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. literalinclude:: /_sample/pyopengl/viewnavigation.py
   :language: python3
   :lines: 1-30

このクラスはマウスドラッグイベントを表現・記録する機能をサブクラスに提供するためだけにある。

* デモクラスの参照を保持する。
* ドラッグ中のビューポートのサイズを保持する。
* ドラッグ開始地点のマウス位置を正規化座標系に変換して保持する。後述。
* 「マウスドラッグ中」イベントを処理するためのメソッドを提供する。サブクラスはこれを必ずオーバーライドする。

  * このメソッドが ``True`` を返すとき、デモクラスにウィンドウを再描画させるように促す。

クラス ``ViewRotate``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
メソッド ``update_mouse_position`` だけを解説する。

.. literalinclude:: /_sample/pyopengl/viewnavigation.py
   :language: python3
   :lines: 41-59

回転に関しては四元数を用いた計算をするため、他の同次座標系表現による線形変換的なコードとは趣が異なる。

* マウスの動きが微小なときには、メソッドが ``False`` を返してウィンドウの再描画をさせない。
* 直前のマウス位置、現在のマウス位置にそれぞれ対応する仮想半球上の変位の回転量を計算する。

  * 自作関数 ``trackball_space`` の戻り値は 3 成分の ``np.array`` なので、4 成分になるよう拡大する。
  * それをそのまま ``Quat`` オブジェクト化する。
  * ``self.app.quat`` をコードに示したような演算により更新する。このへんの数式が気になるが、それについては他の文献を参照。

* シェーダーの行列を更新する。メンバーデータ直接変更なので行儀が悪い。
* ``True`` を返すことで、ウィンドウの再描画が発生する。

クラス ``ViewZoom``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
メソッド ``update_mouse_position`` だけを解説する。

.. literalinclude:: /_sample/pyopengl/viewnavigation.py
   :language: python3
   :lines: 68-78

* マウスがドラッグ開始地点から上方向に動いていればズームイン（拡大）、下方向ならばスームアウト（縮小）というふうに振る舞う。
* 個人的な好みにより、fovy 値を 25 度から 125 度に制限している。
* 更新後の fovy を ``self.app`` 側に通知する。
* 無条件に ``True`` を返すことで、ウィンドウの再描画が発生する。

補助関数群を定義する
----------------------------------------------------------------------
マウスカーソル位置のウィンドウ座標からある種の座標系に変換するための関数群を用意する。
マウス位置、およびその変位をウィンドウの形状に依らずに取り扱いたいので、こういうものが要るのだ。

.. literalinclude:: /_sample/pyopengl/viewnavigation.py
   :language: python3
   :lines: 80-96

* 関数 ``nds_coord`` はスクリーン座標から正規化座標系 [-1, 1] x [-1, 1] への写像を求める。ただし y 座標は上方向を正とする。
  ウィンドウのサイズが 0 でない任意の大きさであっても、変換後は座標成分の絶対値が 1 以下になる。

* 関数 ``trackball_space`` はスクリーン座標から仮想的な半球上への写像を求める。
  :doc:`/angel05/note4` 等を参考。

サブクラス ``ViewNavigationDemoApp`` を定義する
======================================================================
サブクラス ``ViewNavigationDemoApp`` の定義を含むスクリプトファイルの全体を示す。

.. literalinclude:: /_sample/pyopengl/viewnavigationdemo.py
   :language: python3

頂点シェーダー
----------------------------------------------------------------------
.. literalinclude:: /_sample/pyopengl/viewnavigationdemo.py
   :language: python3
   :lines: 34-51
   :emphasize-lines: 6,15

プリミティブの全頂点の座標変換を 3 段階に分け、カメラ設定の直前に（式としては ``camera`` の右側だが）回転をはさみこむ。

コンストラクター
----------------------------------------------------------------------
.. literalinclude:: /_sample/pyopengl/viewnavigationdemo.py
   :language: python3
   :lines: 53-64
   :emphasize-lines: 9-

* メンバーデータ ``xxxhandler`` には、マウスドラッグ中にだけ後述のオブジェクトをセットする。
* メンバーデータ ``quat`` は、モデルの回転量を保持する四元数オブジェクトとする。初期値は無回転状態を意図している。
* メンバーデータ ``fovy`` は、透視変換関数の fovy そのものだ。

メソッド ``init_object``
----------------------------------------------------------------------
メソッド ``update_rotation`` を初回時にも利用したいので、このようにしただけだ。

メソッド ``mouse``
----------------------------------------------------------------------
.. literalinclude:: /_sample/pyopengl/viewnavigationdemo.py
   :language: python3
   :lines: 80-93

このような具合に、マウスボタンに対応してドラッグ時にメンバーデータ ``xxxhandler`` にオブジェクトをセットする。

メソッド ``motion``
----------------------------------------------------------------------
.. literalinclude:: /_sample/pyopengl/viewnavigationdemo.py
   :language: python3
   :lines: 95-104

マウスの動きを処理するオブジェクトがセットされていれば、その動きに基づいて回転量やズーム量のような数値をメンバーデータ ``xxxhandler`` に計算させる。
そして、もし何らかの変換が必要となれば、シーンを再描画させる。

メソッド ``resize``
----------------------------------------------------------------------
.. literalinclude:: /_sample/pyopengl/viewnavigationdemo.py
   :language: python3
   :lines: 106-112

ウィンドウのサイズが更新されれば、コールバック関数は射影変換行列を更新するべきである。そのためにメソッド ``update_perspective`` を呼ぶ。

メソッド ``update_perspective``, ``update_rotation``
----------------------------------------------------------------------
.. literalinclude:: /_sample/pyopengl/viewnavigationdemo.py
   :language: python3
   :lines: 114-127

* シェーダーに uniform 変数の行列データを関数 ``glUniformMatrix4fv`` を用いて送る。
* ``self.q.transform`` は普通の 3 次行列なので、OpenGL 用に同次座標変換のための表現に改めてやる。
  一例として、ここでは 4 次の恒等行列を ``np.array`` オブジェクトとして生成し、その左上部分に 3 次行列をスライス代入した。

結果
======================================================================
静止画でわかりづらいが、マウスをドラッグすると押しているボタンによって三角形群がズームしたり回転したりする。

.. image:: /_static/pyopengl-view-navigation.png
   :scale: 100%

.. include:: /_include/pyopengl-refs.txt
