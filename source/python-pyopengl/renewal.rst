======================================================================
OpenGL 3.x スタイルに書き換える
======================================================================
今までのサンプルは古い OpenGL の仕様に基づいたコードなので、いずれ無用の存在になる（私のノートはこういうパターンがけっこう多い）。
全てを忘れて最新バージョンの OpenGL が推奨する様式でコードを書くことにしたい。
残念ながら私の環境は OpenGL 3.1 までの機能しかサポートしていないので、今後ここに記すコードはせいぜい 3.1 程度の新しさとなる。

本稿では :doc:`./buffer-object` のコードを OpenGL 3.1 の API で再実装したらどうなるかを見ていく。

.. contents::

サンプルコード全体
======================================================================
最初にコードの全体を示す。先に :doc:`./buffer-object` のコード全体と比較しながら読んでもよいし、本稿を単体でのみ読んでもよいだろう。

.. literalinclude:: /_sample/pyopengl/shaderdemo.py
   :language: python3

表示されるグラフィックは次のようなものだ。座標変換をかけたことにより、オブジェクトの定義にミスがあったことがわかる。

.. image:: /_static/pyopengl-shader-transform.png
   :scale: 100%

今回の実装方針は次のとおりだ。

* 私の環境が許す限り、新しい OpenGL の API を用いる。私の環境では OpenGL 3.1 が上限。
* シェーダー言語も許す限り新しい書式で実装する。私の環境では ``#version 330`` が上限。
* 描画するオブジェクトは先述のサンプルのものを再利用する。
* 座標変換を導入する。

座標変換については次回説明する予定だ。→ :doc:`./transform`

ポイント解説
======================================================================
今までのサンプルからの相違点に絞ってコメントを記していきたい。

インポート
----------------------------------------------------------------------
* OpenGL 3.1 を志向しているので、GLU はお役御免となった。
* ``from transform`` から始まる行については、次回解説予定。→ :doc:`./transform`

シェーダープログラム
----------------------------------------------------------------------
:doc:`./shader` のものとは明らかに書き方が変わった。

.. literalinclude:: /_sample/pyopengl/shaderdemo.py
   :language: python3
   :lines: 26-42

* コンテキストバージョンを 2.1 から 3.1 に上げると、シェーダーソースの書き出しを ``#version 330`` のようにバージョンの宣言をしないと、実行時にエラーが発生するようになった。
* ``uniform`` 関連の説明は後述する予定。→ :doc:`./transform`
* ``layout(location=0) in vec4 ...`` の行の宣言により、Python コードからシェーダーに何らかの 4 次元ベクトルデータを引き渡すこと示す。

  * 関数呼び出し ``glVertexAttribPointer(0, 4, ...)`` で、頂点シェーダー内 location = 0 のデータに 4 次元ベクトルデータをセットする。
  * 関数呼び出し ``glEnableVertexAttribArray(0)`` で、このやりとりを有効にするという手続きになるのだろう。

* ``gl_Position`` はシェーダーの予約語ならぬ予約オブジェクトであり、これが描画頂点の最終的な位置を表現する？
* ``out vec4 ...`` の行が、この頂点シェーダーの出力を宣言する。

.. literalinclude:: /_sample/pyopengl/shaderdemo.py
   :language: python3
   :lines: 44-54

* 頂点シェーダーの出力がフラグメントシェーダーの入力となる。
* 最新バージョンの GLSL では ``gl_FragColor`` が廃止されたらしいので、本シェーダーの出力を ``out ...`` の行で別途宣言する。

クラス ``ShaderDemoApp``
----------------------------------------------------------------------
スケルトンクラス ``GLAppBase`` のサブクラスを定義する。

.. literalinclude:: /_sample/pyopengl/shaderdemo.py
   :language: python3
   :lines: 56-69

コンテキストバージョンは、コンストラクターに明示的に指示のない限り、本稿の意図通りに 3.1 とする。

メソッド ``init_object``
----------------------------------------------------------------------
:doc:`./buffer-object` で書いたものと前半部はほぼ同じなので説明はしない。ここでは後半を説明する。

.. literalinclude:: /_sample/pyopengl/shaderdemo.py
   :language: python3
   :lines: 106-125

* 頂点配列オブジェクトを新たに導入する。関数 ``glGenVertexArrays``, ``glBindVertexArray`` を用いる。
* 旧式の関数 ``glVertexPointer``, ``glColorPointer`` の代わりに現代的な ``glVertexAttribPointer`` を用いる。
* 以前メソッド ``do_render`` で呼び出していた ``glEnableClientState`` の代わるものとして、関数 ``glEnableVertexAttribArray`` を導入する。

書かずもがなだが、本コードでは VBO を動的に切り替えるようなことはしないため、VertexAttrib 系関数の呼び出しを初期化メソッドで済ませている。
仮に複数種類の VAO なり VBO なりを用意して、何か動的に切り替えるのであれば、バインド関数の呼び出しを伴った上で、VertexAttrib 系関数の呼び出しをメソッド ``do_render`` に配置するかもしれない。

メソッド ``cleanup``, ``destroy_vbo``
----------------------------------------------------------------------
.. literalinclude:: /_sample/pyopengl/shaderdemo.py
   :language: python3
   :lines: 144-163

* 関数 ``glDisableVertexAttribArray`` により、VBO を効かなくする。
* 関数 ``glBindBuffer`` で ``0`` を指定して VBO を効かなくしてから、関数 ``glDeleteBuffers`` により、VBO を片付ける。
* 関数 ``glBindVertexArray`` で ``0`` を指定して VAO を効かなくしてから、関数 ``glDeleteVertexArrays`` を用いて VAO を片付ける。

一点注意。関数 ``glDeleteXXXs`` の第 2 引数は array-like を要求するので、困ったことに関数
``glGenXXXs`` で「一個だけ」名前を生成したときには、ここに示したように無理矢理 array-like オブジェクトを作る必要がある。

.. include:: /_include/pyopengl-refs.txt
