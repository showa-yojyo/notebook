======================================================================
PyOpenGL 3.x 利用ノート
======================================================================

.. contents:: ノート目次

.. note::

   * OS: Windows XP Home Edition SP 3
   * 本稿執筆にあたり利用した各パッケージのバージョンは次のとおり。

     * Python_: 2.6.6
     * PyOpenGL_: 3.0.2a5
     * NumPy_: 1.6.1
     * PIL_: 1.1.7 (unofficial)

関連リンク
======================================================================
PyOpenGL_ (The Python OpenGL Binding)
  本パッケージ総本山サイト。インストール方法やドキュメント等。

GLUT_ (Nate Robins - OpenGL - GLUT for Win32)
  OpenGL Utility Toolkit (GLUT) の Windows 版バイナリーを配布しているウェブページ。

関連ノート
======================================================================
* :doc:`python-numpy`
* :doc:`python-pil`

インストール
======================================================================
* 経験則として PyOpenGL の依存パッケージ的なものを先にインストールしておくのがコツ。
  もちろん本来の意味では PyOpenGL が依存するパッケージというものはない。
  しかし、グラフィックのプログラムを書くのならば、
  普通はインストールしていないとマズいというものは存在する。

  * 基礎的なベクトル演算のために NumPy_ を利用したいので、インストールしておく。関連ノート参照。
  * 画像ファイルからテクスチャーを読み込むために PIL_ をインストールしておく。これも関連ノート参照。

* GLUT_ をインストールしておく。ただし、システムに存在しない場合に限る。

  * :file:`glut32.dll` が環境変数 ``PATH`` の含むどこかにいれば十分。
  * ない場合は関連リンク先から :file:`glut-3.7.6-bin.zip` をダウンロードする。
    解凍して DLL ファイルを ``C:\WINDOWS\System32`` にぶち込む。
    残りのファイルは処分する。

* PyOpenGL 本体のインストールは `easy_install`_
  またはそれに準じた方法で行えばよい。
  `pip`_ 推奨。

  .. code-block:: console
  
     $ pip install PyOpenGL

ドキュメント
======================================================================
PyOpenGL は Python のラッパーに過ぎない。
OpenGL が一通り使える腕があれば、
必要な勉強は C 言語でのプログラミングとの差分を確認するだけということになる。

* 公式サイトの "PyOpenGL for OpenGL Programmers" という章を読む。

  * PyOpenGL は実行速度については期待できない。

    * プログラミングの柔軟性、利便性、堅牢性を重視しているらしい。
    * 頂点毎の各種演算はアホみたいに遅い。
      よって、せめて配列ベースの演算でコードを書くようにする。

  * PyOpenGL は SIWG ではなく ctypes を利用して実装されている。

  * 一部関数シグニチャーが C 言語版と PyOpenGL 版とで異なる。
    といっても、配列モノの API が Python 風に表現されているだけ。

  * PyOpenGL は OpenGL 操作中でのエラー発生時に例外を送出する。
    プログラマーが手で ``glCheckError`` を書かずにすむというわけだ。

    * デバッグが終わったら ``OpenGL.ERROR_CHECKING = False`` すればよい。

  * PyOpenGL はエラーをログ出力する。
    ``OpenGL.ERROR_LOGING = False`` で無効化。

  * PyOpenGL では、関数の型別サフィックスが省略できる。
    例えば ``glDrawElements{ub|us|ui}`` はいずれも ``glDrawElements`` とできる。

コード
======================================================================
C ではなく Python を利用して OpenGL プログラムを書く利点は、
PyOpenGL_ の API を NumPy_ や PIL_ といった、高品質なサードパーティ製パッケージの
部品と簡単に組み合わせて利用できる点に尽きる。

欠点は何度も言うように実行が遅いことだ。悲しいくらい遅い。
しかし、グラフィックの初学者には遅い方が学習の上ではむしろ好都合ということもあるだろう。

日本語テキストを描画する
----------------------------------------------------------------------
TBW

PNG ファイルからテクスチャーを生成する
----------------------------------------------------------------------
TBW



.. _Python: http://www.python.org/
.. _PyOpenGL: http://pyopengl.sourceforge.net

.. _easy_install: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _pip: http://pypi.python.org/pypi/pip
.. _Python Extension Packages for Windows - Christoph Gohlke: http://www.lfd.uci.edu/~gohlke/pythonlibs/

.. _Numpy: http://scipy.org/NumPy/
.. _PIL: http://www.pythonware.com/products/pil

.. _PyQt: http://www.riverbankcomputing.com/software/pyqt/intro

.. _GLUT: http://user.xmission.com/~nate/glut.html
