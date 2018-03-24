======================================================================
画像ファイルを扱う
======================================================================
本稿では PyOpenGL_ と Pillow_ との連携技についていくつか述べる。
ここに示すプログラムは、クラス ``DeprecatedApp`` を派生することで構築しているので、
先に :doc:`deprecatedapp` を読んでおきたい。

.. contents::

PNG ファイルからテクスチャーを生成する
======================================================================
既存の PNG ファイルから 2 次元テクスチャーデータを生成する方法の一例を示す。

ポイントは Pillow の ``Image`` インスタンスのメソッド ``tostring`` の戻り値を関数 ``glTexImage2D`` に渡すことだ。
アルファチャンネルを含む PNG ファイルからテクスチャーデータを作成する例の、コード全景を示す。

.. literalinclude:: /_sample/pyopengl/texturedemo.py
   :language: python3

以下、ポイントを絞って解説する。

メソッド ``__init__``
----------------------------------------------------------------------
旧式 OpenGL アプリケーション用クラス ``DeprecatedApp`` のサブクラスを定義する。

.. literalinclude:: /_sample/pyopengl/texturedemo.py
   :language: python3
   :lines: 14-18

* 新しいサンプルコードを書くのが面倒なので、
  昔書いたレガシー API を使ったコードをリファクタリングする。
  その都合上、コンテキストバージョンを 1.5 にしたい。
  それ以外はスーパークラスの既定値に従う。

メソッド ``init_gl``
----------------------------------------------------------------------
.. literalinclude:: /_sample/pyopengl/texturedemo.py
   :language: python3
   :lines: 20-25

メソッド ``init_gl`` で ``GL_TEXTURE_2D`` 機能を有効にしておくことを忘れずに。

メソッド ``init_object``
----------------------------------------------------------------------
メソッド ``init_object`` をオーバーライドすることで、描画オブジェクトを定義する。

.. literalinclude:: /_sample/pyopengl/texturedemo.py
   :language: python3
   :lines: 27-53

空間座標・テクスチャー座標・色からなる頂点データをレガシー API で定義する。

メソッド ``init_texture``
----------------------------------------------------------------------
.. literalinclude:: /_sample/pyopengl/texturedemo.py
   :language: python3
   :lines: 55-77

PNG ファイルからテクスチャーを作成している（:doc:`/python-pillow` 参照）。
メソッド ``tostring`` で矩形イメージの RGBA バイト列を得られるということが本質的だ。
イメージのピクセルサイズが OpenGL 的に中途半端なので、
決め打ちだが 256 ピクセル四方にリサイズする。

ファイルパスが私のノート環境から決まる値に決め打ちになっているが、
あくまでも本稿はテクスチャー描画の実現方法に主眼があるので気にしない。

〆に関数 ``glTexImage2D`` 呼び出しにより、テクスチャーデータを OpenGL に渡している。
残りのテクスチャーオプションは、アプリケーションの目的に応じてパラメーターを指定すればよい。

メソッド ``do_render``
----------------------------------------------------------------------
メソッド ``do_render`` をオーバーライドすることで描画処理の中心部分を定義する。
レガシー API のオンパレードなので、説明は省く。

.. literalinclude:: /_sample/pyopengl/texturedemo.py
   :language: python3
   :lines: 79-96

* メソッド ``set_modelview_matrix`` については :doc:`deprecatedapp` を参照。

実行すると以下のようなイメージ (320x240) を得るだろう。

.. figure:: /_images/pyopengl-texture-demo.png
   :align: center
   :alt: イルベロ床
   :width: 328px
   :height: 267px
   :scale: 100%

日本語テキストを描画する
======================================================================
次に Pillow のテキスト描画機能と PyOpenGL のテクスチャー機能を活用したプログラムの例を示す。
当然ながら先述の例とプログラムの構造が同じであることを利用して、
クラス ``TextureDemoApp`` からさらなるサブクラス ``TextDemoApp`` を定義することでコード作業の手間を省く。

.. literalinclude:: /_sample/pyopengl/textdemo.py
   :language: python3

各メソッドの概要は前項のものと同様だが、メソッド ``init_texture`` の最初の処理は説明が必要だ。

テキストを画像化する
----------------------------------------------------------------------
今度は既存の PNG ファイルからではなく、システムフォントからイメージを生成する。
生成処理は別のプログラムでも利用する可能性が高いため、別途関数 ``draw_text`` に定義する。

.. literalinclude:: /_sample/pyopengl/texture.py
   :language: python3

この処理の説明は :doc:`/python-pillow` 参照。

PIL は難しくて、例えばメソッド ``crop`` を素直に ``textsize`` の戻り値で切り落とすと、
境界線が文字に若干かぶるらしく、いやな位置でカットしてしまう。
そこでプラス 16 などという、やってはいけない類の補正を施している。

以上を実行すると、実行結果のスクリーンショットはだいたい次のようなものになる。

.. figure:: /_images/pyopengl-text.png
   :align: center
   :alt: 潔
   :width: 328px
   :height: 267px
   :scale: 100%

Pillow + ``glReadPixels`` によるスクリーンショット取得
======================================================================
ウィンドウに描画されているイメージをファイルに保存できるとたいへん便利なので、
次のような関数を定義しておくとよい。
この関数をクラス ``AppBase`` のキーボードイベントコールバックあたりから呼び出すようにしておくと便利。

.. code-block:: python3

   def capture_screen():
      sx = glutGet(GLUT_WINDOW_WIDTH)
      sy = glutGet(GLUT_WINDOW_HEIGHT)

      pixels = glReadPixels(0, 0, sx, sy, GL_RGBA, GL_UNSIGNED_BYTE)
      img = Image.fromstring("RGBA", (sx, sy), pixels)
      img = img.transpose(Image.FLIP_TOP_BOTTOM)

      filename = input('filename: ')
      img.save(filename)
      print('{} saved'.format(filename))

.. include:: /_include/python-refs-vision.txt
