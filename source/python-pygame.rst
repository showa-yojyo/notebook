======================================================================
Pygame 利用ノート
======================================================================

.. contents:: ノート目次

.. note::

   * OS: Windows XP Home Edition SP 3
   * 本稿において、利用した各パッケージのバージョンは次のとおり。

     * Python_: 2.6.6
     * Pygame_: 1.9.1
     * NumPy_: 1.6.1

関連リンクおよび参考サイト
======================================================================
Pygame_
  Pygame ウェブサイト。リリースニュース、ダウンロード、ドキュメントへの各リンクを提供している。
  2012 年現在、あまり活動が活発でないように見受けられる。

関連ノート
======================================================================
:doc:`python-numpy`
  Pygame の一部機能が Numpy_ を利用している。

インストール
======================================================================
事実上 Windows 環境では msi 実行による手段に限られる。
Pygame_ のサイトのダウンロードのページから最新の msi ファイルをダウンロードして、実行するだけでよい。

テスト
----------------------------------------------------------------------
:file:`$PYTHONHOME/site-packages/pygame/tests/__main__.py` をコンソールから実行すると、
とりあえずユニットテストらしきものが始まる。
私の環境では ``font-test`` で進捗が止まってしまう。

.. code-block:: console

   $ python26 __main__.py
   skipping pygame.tests.cdrom_test (tag 'interactive')
   loading pygame.tests.base_test
   loading pygame.tests.blit_test
   loading pygame.tests.bufferproxy_test
   loading pygame.tests.color_test
   loading pygame.tests.cursors_test
   loading pygame.tests.display_test
   loading pygame.tests.draw_test
   loading pygame.tests.event_test
   loading pygame.tests.fastevent_test
   loading pygame.tests.font_test
   Traceback (most recent call last):
     File "__main__.py", line 131, in <module>
       run(*args, **kwds)
     <<略>>
   KeyboardInterrupt

ドキュメント
======================================================================
:file:`$PYTHONHOME/site-packages/pygame/docs/index.html` から読み進めてゆけばよい。

* Readme には本パッケージの概要が記されている。

  * <Pygame requires the Python language and SDL multimedia library> (About): SDL とは何だ？
  * <Best of all the examples directory has many playable small
    programs which can get started playing with the code right away> (Help):
    ``import Numeric`` と書いてあるものに関しては直ちに動作しない。

* Install のページはもう読まなくてよい。
* Tutorials をまずはじっくり読み進めるのがよかろう。

  * Introduction to Pygame:
    紙風船がウィンドウ内をバウンドし続けるプログラムを紹介している。
    自分でコードを実行してみるとよい。

  * Chimp Tutorial, Line by Line:
    ミニウィンドウ内を往復するチンパンジーを殴るゲーム（クソゲー）のプログラミングチュートリアル。
    Pygame のプログラムの骨格や、スプライトオブジェクトの定義方法等を習得できる。
    HTML に書かれているコードと、インストールされている ``chimp.py`` のコードとは若干異なるので注意。

  * Surfarray Introduction: ここが現在の疑問点。
    Numeric とは Numpy_ の前身か。

  * Making Games Tutorial

    * 記事内のリンクが切れまくっている。
    * 最初のチュートリアルは "Hello There" というテキストを描画するだけ。
      これは特に問題ない。
    * 次はテニスゲームの実装チュートリアル。
      ``ball.png`` と ``bat.png`` を自分で用意する必要があるようだが、
      実際にコードを作ってみると、ゲーム博物館に展示されていそうな古い画面が出た。

      .. image:: /_static/pygame-pong.png
         :alt: Basic Pong
         :scale: 50%

    * 一部コードを修正しないと動作しなかったと思うが、
      実行時にすぐに気付くし、修正も容易だったと記憶しているのでここには記さない。

    * ``#self.offcourt()`` の部分を自分なりに実装するとよい。

* Reference は Pygame 各 API の説明。

PyOpenGL との連携
======================================================================
:file:`$PYTHONHOME/site-packages/pygame/examples/glcube.py` を見れば理解できる。

* GLUT ベースのプログラムでは ``glutDisplayFunc`` で描画コールバックを設定するところを、
  Pygame ベースのプログラムではイベントループの内部から再描画する。
* ``pygame.display.set_mode`` の引数を OpenGL 対応にするべく、それ用の値を OR する。
* フレームバッファの入れ替え ``glutSwapBuffers`` は ``pygame.display.flip`` に相当するようだ。

.. warning::

   テキスト描画できると思ったらできないので、調査意欲が失せた。

.. _Python: http://www.python.org/
.. _Pygame: http://www.pygame.org/
.. _Numpy: http://scipy.org/NumPy/
.. _PyOpenGL: http://pyopengl.sourceforge.net/

