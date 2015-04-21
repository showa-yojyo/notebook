======================================================================
ベクトル・行列・座標変換
======================================================================
本稿では前回（:doc:`./renewal`）解説し残した、ベクトル・行列・座標の変換を最近の OpenGL プログラムでどのように実現するかについて記す。
本ノートの序盤では旧式の ``gluPerspective`` や ``gluLookat`` などの関数を用いて、シーン内の頂点に各種座標変換を施していた。
これらを含む各種行列操作用の API が最近の OpenGL では軒並み deprecated 宣言されてしまった。
そのため、これからは全く異なる方式により、すなわちシェーダープログラムに各種座標変換用の行列オブジェクトを「送信」することで変換処理を実現することになる。

.. contents::

方針
======================================================================
本番ではよそのライブラリーを探して、それを利用するのだが、ここでは勉強用に各種行列操作を自作する。
いつものように、NumPy_ という優秀な線形代数機能を有するパッケージを用いて、OpenGL 旧式の行列によるベクトル・座標変換処理を実装する。

シェーダーとのやりとり
======================================================================
頂点シェーダーのコードをこのように書くとする。

.. literalinclude:: /_sample/pyopengl/shaderdemo.py
   :language: python3
   :lines: 26-42

* ``uniform mat4 camera;`` という表現が「4 次正方行列 ``camera`` を扱う」ということを宣言するものだ。
  このオブジェクトの内容を設定するには、「外側」から OpenGL の関数を用いる必要がある。

  .. literalinclude:: /_sample/pyopengl/shaderdemo.py
     :language: python3
     :lines: 79-88

* 関数 ``glGetUniformLocation`` にシェーダーにおける識別子を与えて、行列オブジェクトの「場所」を得る。アドレスのようなものだろう。
* 関数 ``glUniformMatrix4dv`` にその「場所」と行列の全成分を与えることで、行列がシェーダーに反映される。

行列に関する方針を次のようにする。

* 昔で言う ``gluLookat`` および ``gluPerspective``  による座標変換に関する行列をそれぞれ ``camera`` および ``projection`` と呼ぶことにする。
* 今回のサンプルコードではアニメーションの類を実装しないので、行列 ``camera`` の設定はオブジェクト初期化のタイミングで行うのみとし、更新は行わない。
* 行列 ``projection`` の更新はウィンドウリサイズの度に行う。
* 行列は NumPy のクラス ``array`` の shape が (4, 4) のインスタンスとして処理する。
* Python のコード中では、データが OpenGL に渡る寸前ギリギリまでは行列の成分を「教科書の順序」で取り扱うものとする。
  つまり、OpenGL 関数に実引数として渡す際に、内部配列のメモリレイアウトを OpenGL 式 (column-major) に並び替えるものとする。

座標変換を実装する
======================================================================
自作する変換処理は別モジュール ``transform.py`` で定義することにする。
そのモジュールでのインポート部一覧を示す。

.. literalinclude:: /_sample/pyopengl/transform.py
   :language: python3
   :lines: 16-18

いつものモジュール ``numpy`` だけではなく、サブモジュールである ``numpy.linalg`` の機能も用いる。

関数 ``gluPerspective`` を真似る
----------------------------------------------------------------------
OpenGL のリファレンスをそのまま実装すればよい。

.. literalinclude:: /_sample/pyopengl/transform.py
   :language: python3
   :lines: 58-72

この関数は次のように利用すれば機能するだろう。

.. literalinclude:: /_sample/pyopengl/shaderdemo.py
   :language: python3
   :lines: 127-137

ポイントは関数 ``glUniformMatrix4fv`` の第 3 引数を ``GL_TRUE`` とすることだ。
これにより、OpenGL が行列の成分配列の要素の並びを ``np.array`` デフォルトの row-major から column-major にしてくれる。

逆に仮に ``GL_FALSE`` で動作させたいのであれば ``np.array`` オブジェクトを ``.transpose()`` する等の、内部配列の要素入れ替え処理を要する。

関数 ``gluLookAt`` を真似る
----------------------------------------------------------------------
OpenGL のリファレンスをそのまま実装すればよい。

.. literalinclude:: /_sample/pyopengl/transform.py
   :language: python3
   :lines: 36-56

処理の意味はこうだろう。

#. カメラの位置、観測目標点、カメラの姿勢から正規直交基底を計算する。
#. その原点を観測者の位置にオフセットする。

ところでパラメーターの型を ``np.array`` 固定にしたのは設計ミスかもしれない。
NumPy に倣って array-like にするとなおよい。

カメラをシェーダーに設定するにはこのようにする。関数 ``glUniformMatrix4fv`` の第 3 引数を ``GL_TRUE`` とすることを忘れてはならない。

.. literalinclude:: /_sample/pyopengl/shaderdemo.py
   :language: python3
   :lines: 79-88

この座標変換は、

* カメラを (2, 2, 2) に置いて、
* 原点 (0, 0, 0) を向いて、
* カメラ本体の姿勢はベクトル (0, 0, 1) で表現できる、つまり直立している

ので、最終的な絵における x, y, z の各座標軸はそれぞれウィンドウの左下、右下、上方向に向くことになる。

今回の結果の画像を座標変換なし版と併せて再掲する。

.. image:: /_static/pyopengl-vbo.png
   :scale: 100%

.. image:: /_static/pyopengl-shader-transform.png
   :scale: 100%

素直に xy 座標平面上に正多角形を描画するつもりだったが、このアングルでオブジェクトを見ることで初めて、扇型の中心以外の点をすべて間違えて平面 z = 1 上に定義したことに気付く。

.. literalinclude:: /_sample/pyopengl/shaderdemo.py
   :language: python3
   :lines: 90-101
   :emphasize-lines: 10

----

次回（:doc:`./view-navigation`）、トラックボール実装。

.. include:: /_include/pyopengl-refs.txt
