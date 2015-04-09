======================================================================
画像ファイルを扱う
======================================================================
本稿では PyOpenGL_ と Pillow_ との連携技についていくつか述べる。

ここに示すプログラムは、いずれも前述のクラスを派生することで構築している。

.. contents::

PNG ファイルからテクスチャーを生成する
======================================================================
既存の PNG ファイルから 2 次元テクスチャーデータを生成する方法の一例を示す。

ポイントは Pillow の ``Image`` インスタンスのメソッド ``tostring`` の戻り値を関数 ``glTexImage2D`` に渡すことだ。
アルファチャンネルを含む PNG ファイルからテクスチャーデータを作成する例の、コード全景を示す。

.. literalinclude:: /_sample/pyopengl/texturedemo.py
   :language: python3

以下、ポイントを絞って解説する。

各種初期設定をする
----------------------------------------------------------------------
スケルトンクラス ``GLAppBase`` のサブクラスを定義する。

.. literalinclude:: /_sample/pyopengl/texturedemo.py
   :language: python3
   :lines: 15-29

* 新しいサンプルコードを書くのが面倒なので、レガシー API を使うのだが、その都合上、コンテキストバージョンを 1.5 にしたい。それ以外はスーパークラスの既定値に従う。
* メソッド ``init_gl`` で ``GL_TEXTURE_2D`` 機能を有効にしておくことを忘れずに。

描画オブジェクトを定義する
----------------------------------------------------------------------
メソッド ``init_object`` をオーバーライドすることで、描画オブジェクトを定義する。ここではテクスチャー、図形の順に処理する。

.. literalinclude:: /_sample/pyopengl/texturedemo.py
   :language: python3
   :lines: 31-37

PNG ファイルからテクスチャーを作成している（:doc:`/python-pillow` 参照）。メソッド
``tostring`` で矩形イメージの RGBA バイト列を得られるということが本質的だ。
イメージのピクセルサイズが OpenGL 的に中途半端なので、決め打ちだが 256 ピクセル四方にリサイズする。

ファイルパスが私のノート環境から決まる値に決め打ちになっているが、あくまでも本稿はテクスチャー描画の実現方法に主眼があるので気にしない。

テクスチャーパラメーターを設定する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. literalinclude:: /_sample/pyopengl/texturedemo.py
   :language: python3
   :lines: 39-46

関数 ``glTexImage2D`` 呼び出しにより、テクスチャーデータを OpenGL に渡している。
残りのテクスチャーオプションは、アプリケーションの目的に応じてパラメーターを指定すればよい。

頂点データを定義する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
最後に空間座標・テクスチャー座標・色からなる頂点データをレガシー API で定義する。

.. literalinclude:: /_sample/pyopengl/texturedemo.py
   :language: python3
   :lines: 48-71

これで描画の準備がほぼ整った。残りは描画メソッド本体で行う。

描画する
----------------------------------------------------------------------
メソッド ``do_render`` をオーバーライドすることで描画処理の中心部分を定義する。レガシー API のオンパレードなので、説明は省く。

.. literalinclude:: /_sample/pyopengl/texturedemo.py
   :language: python3
   :lines: 84-105

実行すると以下のようなイメージ (320x240) を得るだろう。

.. image:: /_static/illvelo-texture.png
   :scale: 50%

日本語テキストを描画する
======================================================================
次に Pillow のテキスト描画機能と PyOpenGL のテクスチャー機能を活用したプログラムの例を示す。
当然ながら先述の例とプログラムの構造が同じであることを利用して、クラス
``TextureDemoApp`` からさらなるサブクラス ``TextDemoApp`` を定義することでコード作業の手間を省く。

.. literalinclude:: /_sample/pyopengl/textdemo.py
   :language: python3

描画オブジェクトを定義する
----------------------------------------------------------------------
前項同様、メソッド ``init_object`` をオーバーライドすることで、描画オブジェクトを定義する。処理の流れはこのようになっている。

#. テキストからイメージをメモリに生成する。
#. 前項同様、OpenGL にテクスチャーパラメーターの設定をする。
#. 前項同様、頂点データを定義する。

テクスチャーパラメーターを設定する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
説明を省く。

テキストを画像化する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. literalinclude:: /_sample/pyopengl/textdemo.py
   :language: python3
   :lines: 34-37

今度は既存の PNG ファイルからではなく、システムフォントからイメージを生成する。
生成処理は別のプログラムでも利用する可能性が高いため、別途関数に定義する。

.. literalinclude:: /_sample/pyopengl/textdemo.py
   :language: python3
   :lines: 13-29

この処理の説明は :doc:`/python-pillow` 参照。

頂点データを定義する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
またしてもレガシー API によってしまったが、頂点データの定義コードである。これはテクスチャー処理そのものだ。

.. literalinclude:: /_sample/pyopengl/textdemo.py
   :language: python3
   :lines: 47-69

描画する
----------------------------------------------------------------------
メソッド ``do_render`` をオーバーライドする。前のサンプルとの本質的な違いはほとんどない。せいぜいカメラや描画形状
``GL_TRIANGLES`` と ``GL_POLYGON`` の違いに過ぎない。

.. literalinclude:: /_sample/pyopengl/textdemo.py
   :language: python3
   :lines: 71-92

以上を実行すると、実行結果のスクリーンショットはだいたい次のようなものになる。

.. image:: /_static/pyopengl-text.png
   :scale: 50%

Pillow + glReadPixels によるスクリーンショット取得
======================================================================
ウィンドウに描画されているイメージをファイルに保存できるとたいへん便利なので、次のような関数を定義しておくとよい。
この関数をキーボードイベントコールバックあたりから呼び出すようにしておくと便利。

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

.. include:: /_include/pyopengl-refs.txt
