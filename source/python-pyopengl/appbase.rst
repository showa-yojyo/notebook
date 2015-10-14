======================================================================
クラス ``AppBase`` の実装
======================================================================
単純な PyOpenGL のプログラムは、どれも構造と手続きが似通ったものになる。
このノートではサンプルプログラムを多数書くつもりでいるので、
それらに共通しているプログラミング要素を、
オブジェクト指向プログラミング的着想によってクラスとしてカプセル化しておく。

ただし、歴史的な事情によりそのようなクラスを単一のクラスで表現し切ることは無理があるようだ。
OpenGL 3.0 以前と以後とで、プログラミングの方法論がまるで別物なので、
以前、以後に対応するベースクラスをそれぞれ設計することになる。

本稿では、それらのベースクラスのベースクラス ``AppBase`` を設計する。

.. contents::

.. warning::

   現在、このクラスを利用したすべてのプログラムから次の例外が発生する。
   ``GL_SHADING_LANGUAGE_VERSION`` がいつの間に無効な列挙になったのかわからない。
   鋭意調査中。

   .. code-block:: console

      $ ./textdemo.py
      Traceback (most recent call last):
        File "./textdemo.py", line 72, in <module>
          sys.exit(main(sys.argv))
        File "./textdemo.py", line 69, in main
          app.run(sys.argv)
        File "D:\...\appbase.py", line 72, in run
          self.init_glut(args)
        File "D:\...\appbase.py", line 119, in init_glut
          GL.glGetString(GL.GL_SHADING_LANGUAGE_VERSION).decode()),
        File "GL_accelerate\src\errorchecker.pyx", line 53, in OpenGL_accelerate.errorchecker._ErrorChecker.glCheckError (src\errorchecker.c:1200)
      OpenGL.error.GLError: GLError(
              err = 1280,
              description = b'\x96\xb3\x8c\xf8\x82\xc8\x97\xf1\x8b\x93',
              baseOperation = glGetString,
              cArguments = (GL_SHADING_LANGUAGE_VERSION,)
      )
      freeglut (./textdemo.py): fgInitGL2: fghGenBuffers is NULL

クラス ``AppBase``
======================================================================
先にクラス全景を次に示す。

.. literalinclude:: /_sample/pyopengl/appbase.py
   :language: python3

このクラスの目的は次のとおりだ。

* 新しいサンプルコードを書くときは、このクラスのサブクラスを定義する形にすることで、
  コードの重複を積極的に少なくする。
  特にメソッドのオーバーライドにより、描画や操作の「差分」の実装だけで済むようにする。
* サブクラスでコンテキストバージョンを指定することで、
  そのアプリケーションが deprecated features を採用するかどうかを明示する。
* コンテキスト情報の出力や FPS の表示等、全サンプルコードが利用しがちな機能を提供する。

このクラスの利用方法は後述のページで見ていくことになるので、
このページの残りでは、このクラス自体のポイントを記す。

機能概要
----------------------------------------------------------------------
クラス ``AppBase`` で実装する機能を述べる。

コンテキストバージョン指定機能
  OpenGL のコンテキストバージョンをコンストラクターで指定できる。
  サブクラスから指定することになる。

ウィンドウタイトル設定機能
  ウィンドウタイトルバーに表示するタイトル文字列を指定できる。
  ただし、アスキー文字のみのもよう。

FPS リアルタイム表示機能
  ウィンドウタイトルバーに FPS を表示する。0.25 秒ごとに更新。

ウィンドウサイズ・位置の指定機能
  ウィンドウの初期サイズ、初期表示位置をクラスのコンストラクターで指定できる。

OpenGL サポートバージョン情報表示機能
  ウィンドウ表示までに、次のような情報をコンソールに出力する。

  .. code-block:: text

     Vendor: Intel
     Renderer: Intel(R) HD Graphics
     Version: 3.1.0 - Build 9.17.10.4101
     GLSL: 1.40 - Intel Build 9.17.10.4101

ウィンドウサイズ変更時ビューポート自動更新機能
  ウィンドウサイズ変更時に可能な限り OpenGL のビューポートをウィンドウの全クライアント領域に更新する。

マウスドラッグによるズーム・回転機能
  左ボタンドラッグで描画モデルの回転、右ボタンドラッグでモデルにズームする。
  :doc:`view-navigation` も参照。

透視射影パラメーターの設定機能
  関数 ``gluPerspective`` またはそれと同等のパラメーターを任意に設定可能。

カメラパラメーターの設定機能
  関数 ``gluLookAt`` またはそれと同等のパラメーターを任意に設定可能。

GLSL オブジェクトの管理機能
  プログラムオブジェクトをシェーダーオブジェクトの生成、破棄処理を管理する。
  詳細は :doc:`program-manager` を参照。

アプリケーション終了機能
  Esc キーを押すと、アプリケーションを終了する。

利用方法
----------------------------------------------------------------------
本クラスはオブジェクト化して利用するのではなく、ベースクラスとして利用する。
サブクラスとしてアプリケーションを実装するサンプルのときに記す。

.. include:: /_include/python-refs-vision.txt
