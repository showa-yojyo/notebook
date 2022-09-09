======================================================================
インストール
======================================================================
経験則として NumPy_ 等、PyOpenGL_ の依存パッケージ的なものを先にインストールしておくのがコツ。
もちろん本来の意味では PyOpenGL が依存するパッケージというものはない。
しかし、グラフィックのプログラムを書くのならば、
普通はインストールしていないとマズいというものは存在する。
まずは次の 2 つのパッケージを挙げたい。

* 基礎的なベクトル演算のために NumPy を利用したいので、インストールしておく。関連ノート :doc:`/python-numpy/index` を参照。
* 画像ファイルからテクスチャーを読み込むために Pillow_ をインストールしておく。関連ノート :doc:`/python-pillow` を参照。

.. contents::

PyOpenGL をインストールする
======================================================================
PyOpenGL 本体のインストールは上記関連リンクの非公式インストーラー
(`Python Extension Packages for Windows - Christoph Gohlke`_)
を利用する。著者の当時の環境は Windows 7 64bit なので、選択は次の 2 つとなる。

* :file:`PyOpenGL-3.1.0.win-amd64-py3.4.exe`
* :file:`PyOpenGL-accelerate-3.1.0.win-amd64-py3.4.exe`

以前は GLUT はユーザーが準備することになっていたと記憶するが、
最近のバージョンでは DLL が同時にインストールされるようになっている。

Miniconda_ で Python 環境を管理しているのであれば、
:code:`conda install pyopengl pyopengl-accelerate` してもよい。
ただし、関連する DLL を自前で準備する必要があることを考えると
非公式インストーラー、現在では whl ファイルを
:program:`pip` でインストールするのと手間がそう変わらない。
さらにこの場合 DLL ファイルの設置場所も問題になる。
Miniconda 環境の :file:`Library\\bin` フォルダーに
:file:`freeglut64.dll` を置くことになるだろう。
正しいファイル名が何であるかはモジュール ``OpenGL.platform.win32`` の
関数 :code:`GLUT` の for ループを見ることで理解できる。

アップグレード
----------------------------------------------------------------------
Windows 10 + Python 3.5 環境では下記ファイルを例のサイトから
ダウンロードして :code:`pip install` を実施した。

* :file:`PyOpenGL-3.1.1a1-cp35-none-win_amd64.whl`
* :file:`PyOpenGL_accelerate-3.1.1a1-cp35-none-win_amd64.whl`

Miniconda 利用者ならば :code:`conda update pyopengl pyopengl-accelerate` でよい。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
.. include:: /_include/python-refs-vision.txt
