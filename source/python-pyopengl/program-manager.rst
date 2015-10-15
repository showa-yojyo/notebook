======================================================================
シェーダープログラム管理クラス
======================================================================
GLSL プログラムオブジェクトとシェーダーオブジェクトの生成と破棄の管理方法はワンパターンなので、
この機能をカプセル化した管理クラス ``ProgramManager`` を作成しておき、
アプリケーションクラス ``AppBase`` にオブジェクトを保持させて用いるようにする。

.. contents::

.. warning::

   現在、私の環境ではこのクラスを利用したすべてのプログラムから次の例外が発生する。
   グラフィックドライバーがダメになったため、
   サポートする機能が OpenGL 1.1 までに落ち込んでしまったことにより、
   シェーダーが存在していないかのように扱われる。

   .. code-block:: console

      $ ./shaderdemo.py
      Traceback (most recent call last):
        File "./shaderdemo.py", line 213, in <module>
          sys.exit(main(sys.argv))
        File "./shaderdemo.py", line 210, in main
          app.run(sys.argv)
        File "D:\...\appbase.py", line 73, in run
          self.init_program()
        File "D:\...\modernapp.py", line 40, in init_program
          self.program_manager.setup(shader_sources)
        File "D:\...\program_manager.py", line 28, in setup
          shader = GL.glCreateShader(shader_type)
        File "D:\Python35\lib\site-packages\OpenGL\platform\baseplatform.py", line 407, in __call__
          self.__name__, self.__name__,
      OpenGL.error.NullFunctionError: Attempt to call an undefined function glCreateShader, check for bool(glCreateShader) before calling
      freeglut (./source/_sample/pyopengl/shaderdemo.py): OpenGL >2.1 context requested but wglCreateContextAttribsARB is not available! Falling back to legacy context creation
      freeglut (./source/_sample/pyopengl/shaderdemo.py): fgInitGL2: fghGenBuffers is NULL

クラス ``ProgramManager``
======================================================================
次に挙げるようなコードを書いておく。
部分的には PyOpenGL の某モジュールにも同様のコード片がある。

.. literalinclude:: /_sample/pyopengl/program_manager.py
   :language: python3

メンバーデータの説明
======================================================================
``program_id``
  関数 ``glCreateProgram`` の戻り値をここに保持する。
  アプリケーションは、GLSL 構成要素にアクセスするときにはこの値を参照することになる。

``shader_sources``
  これは辞書オブジェクトで、そのキーは関数 ``glCreateShader`` の引数であり、
  値はその戻り値と一緒に関数 ``glShaderSource`` に与える引数（プログラムコード）のペアを想定している。

``shader_ids``
  これも辞書オブジェクトで、そのキーは先程の辞書と同じものであり、
  値は先程の関数 ``glCreateShader`` の戻り値（シェーダープログラム識別子）である。

メソッドの説明
======================================================================
アプリケーションはメソッド ``setup`` と ``cleanup`` をその初期化処理と後始末処理にて呼び出す。

.. include:: /_include/python-refs-vision.txt
