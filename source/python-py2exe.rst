======================================================================
Py2exe 利用ノート
======================================================================

Py2exe に関しては筆者が興味を失っている状態なので、本稿の更新は当分しない予定でいる。
現在、バージョン 0.9.2 のインストーラー（全 Python バージョン対応）が PyPI に置いてある。
64 ビット用のビルドもあるので、その気になれば下記記事を修正する。

.. contents:: ノート目次

.. note::

   * OS: Windows XP Home Edition SP 3
   * 本稿において、利用した各パッケージのバージョンは次のとおり。

     * Python_: 2.6.6, 2.7.3
     * Py2exe_: 0.6.9


関連リンクおよび参考サイト
======================================================================
Py2exe_
  Py2exe ウェブサイト。リリースニュース、ダウンロード、ドキュメントへの各リンクを提供している。

インストール
======================================================================
Windows 用インストーラーによる。
easy_install/pip を利用してのインストールではない。
Py2exe_ のサイトのダウンロードのページから、自分の Python 環境に適合するインストーラーを見つけてダウンロードする。
ファイルは :file:`py2exe-0.6.9.win32-py2.6.exe` のような名前をしている。

EXE ファイルの作成練習
======================================================================

Hello world
----------------------------------------------------------------------
インストール終了後、公式サイトにある Hello world のチュートリアルをやってみるとよい。

hello.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
文字列を標準出力に出力するだけのコード。

.. code-block:: python

   # -*- coding: utf-8 -*-
   #
   # hello.py

   print 'Hello world'

setup.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:file:`hello.py` と同じフォルダーに :file:`setup.py` を作成する。

.. code-block:: python

   # -*- coding: utf-8 -*-
   #
   # setup.py

   from distutils.core import setup
   import py2exe

   setup(console=['hello.py'])

ビルド
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
コンソールウィンドウを開き、下記のようにすることで EXE ファイルができる。

* 本ノートでは Cygwin (bash) 使用。
  ``python26`` とあるのは Windows 用 ``python.exe`` のフルパスの alias だ。
* 配布は :file:`dist` フォルダー全部となる。

.. code-block:: console

   $ python26 setup.py py2exe
   ... 長い出力

   $ cd dist
   $ ./hello.exe
   Hello world
   $

Python 2.6 以降に係わる VC ランタイム問題
----------------------------------------------------------------------
配布物を別の PC で実行することを考えると、
:file:`dist` フォルダー全部でも足りないものがある。
MSVC9 系ランタイム DLL が必要になる。
対象の PC にランタイムがない場合を考慮して、関連 DLL をも配布するケースを考える。

* MSVC 2008 がインストールされていれば話は早いハズ。
  Py2exe_ の Tutorial 内セクション 5.2. "Python 2.6, 2.7, 3.0, 3.1" を一読すれば、
  必要なファイルや作業が理解できる。

* 相手がランタイムを独自にインストールするならば、このセクションの対応は省略できる。

* MSVC 2008 がインストールされていない場合、

  * マニフェストファイルの準備 or 自作が必要。
  * DLL は厳密には 9.0.21022.8 というバージョン。
    システムフォルダー :file:`C:\\WINDOWS\\WinSxS` をチェックする。

仮の措置
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#. :file:`setup.py` のあるフォルダーに以下のファイル群をコピー。

   * :file:`C:\\WINDOWS\\WinSxS\\Manifests\\x86_Microsoft.VC90.CRT_1fc8b3b9a1e18e3b_9.0.21022.8_x-ww_d08d0375.manifest`
   * :file:`C:\\WINDOWS\\WinSxS\\x86_Microsoft.VC90.CRT_1fc8b3b9a1e18e3b_9.0.21022.8_x-ww_d08d0375\\msvc*90.dll`

#. コピー後のマニフェストファイルをリネームし、
   :file:`Microsoft.VC90.CRT.manifest` とする。

#. :file:`setup.py` の内容を修正する。例を示す。

  .. code-block:: python

     # -*- coding: utf-8 -*-
     from distutils.core import setup
     import py2exe
     from glob import glob

     data_files = [("Microsoft.VC90.CRT", 
                    ["Microsoft.VC90.CRT.manifest"] + glob(r'msvc*90.dll'))]

     setup(console=['hello.py'],
           data_files=data_files)

サードパーティ製パッケージを利用した自作プログラムを配布する場合
----------------------------------------------------------------------

PIL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
結論から言うと、何か特殊な処理を :file:`setup.py` に追加する必要はない。

次のコードを考える。コマンドライン引数を画像ファイルとみなし、
ビューワーで開くだけのものだ。エラー処理は実装していない。

.. code-block:: python

   # -*- coding: utf-8 -*-
   import sys
   import Image

   def main(argv):
       img = Image.open(argv[1])
       img.show()

   if __name__ == '__main__':
       main(sys.argv)

この py ファイルを先述の Hello world 同様に EXE 化すると、
:file:`dist` フォルダーの内容にしっかりと PIL のランタイムである
:file:`_imaging.pyd` が含まれている。
これなら配布しても動作しそうだ。

おそらく Py2exe が ``import`` 文をチェックして適宜 DLL を含めてくれるのだろう。

Numpy, Scipy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Py2exe が予想以上に色々な pyd ファイルを同梱してくれるので、正直困る。

ターゲットとなるコードは次のようなものだ。

.. code-block:: python

   # -*- coding: utf-8 -*-
   import numpy as np
   from scipy.spatial import KDTree

   def main():
       # 3D points: (0, 0, 0), (0, 0, 10), (0, 0, 20), ...
       x, y, z = np.mgrid[0:100:10, 0:100:10, 0:100:10]
       points = zip(x.ravel(), y.ravel(), z.ravel())

       # Construct a KDTree.
       tree = KDTree(points)

       # A target point included in [0, 100) * [0, 100) * [0, 100).
       target = np.random.random_sample(3) * 100.
       print "Target: ", target

       # Query for the closest point.
       dist, index = tree.query(target, eps = 0.01)
       print "Closest: ", tree.data[index]
       print "Distance: ", dist

   if __name__ == '__main__':
       main()

``setup.py py2exe`` すると :file:`dist` フォルダーの中身がマッシブになる。
Tcl/Tk 関連のランタイムは本当に必要なのだろうか。

.. code-block:: console

   $ ls -l dist
   合計 24M
   -rwxr-xr-x 1 work ????   72K 8月  24  2010 _ctypes.pyd*
   -rwxr-xr-x 1 work ????  280K 8月  24  2010 _hashlib.pyd*
   -rwxr-xr-x 1 work ????   23K 8月  24  2010 _multiprocessing.pyd*
   -rwxr-xr-x 1 work ????   40K 8月  24  2010 _socket.pyd*
   -rwxr-xr-x 1 work ????  704K 8月  24  2010 _ssl.pyd*
   -rwxr-xr-x 1 work ????   30K 8月  24  2010 _tkinter.pyd*
   -rwxr-xr-x 1 work ????   71K 8月  24  2010 bz2.pyd*
   -rw-r--r-- 1 work ????  8.0M 4月  21 22:28 library.zip
   -rwxr-xr-x 1 work ????   19K 4月  21 22:28 main.exe*
   -rwxr-xr-x 1 work ????  125K 7月  21  2011 numpy.core._sort.pyd*
   -rwxr-xr-x 1 work ????  1.1M 7月  21  2011 numpy.core.multiarray.pyd*
   -rwxr-xr-x 1 work ????  174K 7月  21  2011 numpy.core.scalarmath.pyd*
   -rwxr-xr-x 1 work ????  380K 7月  21  2011 numpy.core.umath.pyd*
   -rwxr-xr-x 1 work ????   48K 7月  21  2011 numpy.fft.fftpack_lite.pyd*
   -rwxr-xr-x 1 work ????   39K 7月  21  2011 numpy.lib._compiled_base.pyd*
   -rwxr-xr-x 1 work ???? 1013K 7月  21  2011 numpy.linalg.lapack_lite.pyd*
   -rwxr-xr-x 1 work ????  494K 7月  21  2011 numpy.random.mtrand.pyd*
   -rwxr-xr-x 1 work ????  150K 8月  24  2010 pyexpat.pyd*
   -rwxr-xr-x 1 work ????  2.1M 8月  24  2010 python26.dll*
   -rwxr-xr-x 1 work ????  1.6M 2月  27 09:48 scipy.sparse.sparsetools._bsr.pyd*
   -rwxr-xr-x 1 work ????  666K 2月  27 09:47 scipy.sparse.sparsetools._coo.pyd*
   -rwxr-xr-x 1 work ????  1.2M 2月  27 09:47 scipy.sparse.sparsetools._csc.pyd*
   -rwxr-xr-x 1 work ????  528K 2月  27 09:48 scipy.sparse.sparsetools._csgraph.pyd*
   -rwxr-xr-x 1 work ????  1.5M 2月  27 09:46 scipy.sparse.sparsetools._csr.pyd*
   -rwxr-xr-x 1 work ????  562K 2月  27 09:48 scipy.sparse.sparsetools._dia.pyd*
   -rwxr-xr-x 1 work ????   46K 2月  27 09:48 scipy.spatial._distance_wrap.pyd*
   -rwxr-xr-x 1 work ????  113K 2月  27 09:48 scipy.spatial.ckdtree.pyd*
   -rwxr-xr-x 1 work ????  576K 2月  27 09:48 scipy.spatial.qhull.pyd*
   -rwxr-xr-x 1 work ????   12K 8月  24  2010 select.pyd*
   -rwxr-xr-x 1 work ????   16K 3月   5 23:19 sgmlop.pyd*
   drwxr-xr-x 1 work ????     0 4月  21 22:28 tcl/
   -rwxr-xr-x 1 work ????  847K 11月  6  2008 tcl85.dll*
   -rwxr-xr-x 1 work ????  1.3M 11月  6  2008 tk85.dll*
   -rwxr-xr-x 1 work ????  572K 8月  24  2010 unicodedata.pyd*
   -rwxr-xr-x 1 work ????   49K 8月  24  2010 w9xpopen.exe*

Matplotlib
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
わざとらしく NumPy, SciPy 関連を利用しない Matplotlib プログラムを考える。

.. code-block:: python

   # -*- coding: utf-8 -*-
   import matplotlib as mpl
   import matplotlib.pyplot as plt

   def main():
       ax = plt.gca()
       ann = ax.annotate('An annotate', xy=(1.0, 3.0),
       xycoords='data', xytext=(2.0, 2.5), textcoords='data',
       arrowprops=dict(arrowstyle='->'))

       line = ax.plot((1, 2, 3, 4))

       ax.xaxis.grid(True)
       ax.xaxis.set_label('TEST')
       for label in ax.xaxis.get_ticklabels(minor=False):
           label.set_color('red')
           label.set_rotation(-45.)
           label.set_fontsize(16)

       plt.show()

   if __name__ == '__main__':
       main()

面白いことに、MSVC90 ランタイムに関連するエラーメッセージが出る。

.. code-block:: text

   *** finding dlls needed ***
   error: MSVCP90.dll: No such file or directory

ここで、先述の仮の措置を適用した setup.py に書き換えると、ビルドが通る。
そして :file:`dist` の内容がとんでもないことにある。

.. code-block:: console

   $ ls -l dist
   合計 38M
   -rwxr-xr-x 1 work ????   72K 8月  24  2010 _ctypes.pyd*
   -rwxr-xr-x 1 work ????  280K 8月  24  2010 _hashlib.pyd*
   -rwxr-xr-x 1 work ????   23K 8月  24  2010 _multiprocessing.pyd*
   -rwxr-xr-x 1 work ????   40K 8月  24  2010 _socket.pyd*
   -rwxr-xr-x 1 work ????  704K 8月  24  2010 _ssl.pyd*
   -rwxr-xr-x 1 work ????   30K 8月  24  2010 _tkinter.pyd*
   -rwxr-xr-x 1 work ????   71K 8月  24  2010 bz2.pyd*
   -rw-r--r-- 1 work ????   11M 4月  21 22:52 library.zip
   -rwxr-xr-x 1 work ????   20K 4月  21 22:52 main.exe*
   -rwxr-xr-x 1 work ????   19K 10月  6  2011 matplotlib._cntr.pyd*
   -rwxr-xr-x 1 work ????   47K 10月  6  2011 matplotlib._delaunay.pyd*
   -rwxr-xr-x 1 work ????  144K 10月  6  2011 matplotlib._image.pyd*
   -rwxr-xr-x 1 work ????  133K 10月  6  2011 matplotlib._path.pyd*
   -rwxr-xr-x 1 work ????  193K 10月  6  2011 matplotlib._png.pyd*
   -rwxr-xr-x 1 work ????  121K 10月  6  2011 matplotlib._tri.pyd*
   -rwxr-xr-x 1 work ????  211K 10月  6  2011 matplotlib.backends._backend_agg.pyd*
   -rwxr-xr-x 1 work ????  487K 10月  6  2011 matplotlib.ft2font.pyd*
   -rwxr-xr-x 1 work ????   12K 10月  6  2011 matplotlib.nxutils.pyd*
   -rwxr-xr-x 1 work ????   44K 10月  6  2011 matplotlib.ttconv.pyd*
   drwxr-xr-x 1 work ????     0 4月  21 22:52 Microsoft.VC90.CRT/
   -rwxr-xr-x 1 work ????  125K 7月  21  2011 numpy.core._sort.pyd*
   -rwxr-xr-x 1 work ????  1.1M 7月  21  2011 numpy.core.multiarray.pyd*
   -rwxr-xr-x 1 work ????  174K 7月  21  2011 numpy.core.scalarmath.pyd*
   -rwxr-xr-x 1 work ????  380K 7月  21  2011 numpy.core.umath.pyd*
   -rwxr-xr-x 1 work ????   48K 7月  21  2011 numpy.fft.fftpack_lite.pyd*
   -rwxr-xr-x 1 work ????   39K 7月  21  2011 numpy.lib._compiled_base.pyd*
   -rwxr-xr-x 1 work ???? 1013K 7月  21  2011 numpy.linalg.lapack_lite.pyd*
   -rwxr-xr-x 1 work ????  494K 7月  21  2011 numpy.random.mtrand.pyd*
   -rwxr-xr-x 1 work ????  766K 1月  27 08:57 PIL._imaging.pyd*
   -rwxr-xr-x 1 work ????  150K 8月  24  2010 pyexpat.pyd*
   -rwxr-xr-x 1 work ????  5.5M 5月   2  2011 PyQt4.QtGui.pyd*
   -rwxr-xr-x 1 work ????  2.1M 8月  24  2010 python26.dll*
   -rwxr-xr-x 1 work ????  2.2M 3月  21  2011 QtCore4.dll*
   -rwxr-xr-x 1 work ????  7.6M 3月  21  2011 QtGui4.dll*
   -rwxr-xr-x 1 work ????   12K 8月  24  2010 select.pyd*
   -rwxr-xr-x 1 work ????   16K 3月   5 23:19 sgmlop.pyd*
   drwxr-xr-x 1 work ????     0 4月  21 22:42 tcl/
   -rwxr-xr-x 1 work ????  847K 11月  6  2008 tcl85.dll*
   -rwxr-xr-x 1 work ????  1.3M 11月  6  2008 tk85.dll*
   -rwxr-xr-x 1 work ????  572K 8月  24  2010 unicodedata.pyd*
   -rwxr-xr-x 1 work ????   49K 8月  24  2010 w9xpopen.exe*

* 頼みもしないのに PyQt4 関連のランタイムが含まれてしまう。
* インポートした覚えのない NumPy 関連ランタイムが含まれてしまう。
* どさくさ紛れに PIL もいる。

PyOpenGL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
GLUT ベースの簡単なプログラムに対して、Py2exe ビルドを試す。

.. code-block:: python

   # -*- coding: utf-8 -*-
   import sys
   from OpenGL.GL import *
   from OpenGL.GLU import *
   from OpenGL.GLUT import *

   window_title = u"OpenGL Study"
   window_sx, window_sy = 320, 240
   window_x, window_y = 100, 100

   def display():
       glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
       glutSwapBuffers()

   def main(argv):
       glutInit(sys.argv)
       glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
       glutInitWindowSize(window_sx, window_sy)
       glutInitWindowPosition(window_x, window_y)
       glutCreateWindow(window_title)

       glClearColor(0.24, 0.35, 0.64, 1.)
       glEnable(GL_DEPTH_TEST)
       glutDisplayFunc(display)

       glutMainLoop()

   if __name__ == '__main__':
       main(sys.argv)

Hello world のときと同じ設定でビルドすると、次の不審なメッセージが現れる。

.. code-block:: text

   The following modules appear to be missing
   ['OpenGL.GL.GL_EXTENSIONS', 'OpenGL.GL.GL_NUM_EXTENSIONS', 'OpenGL.GL.GL_VERSION
   ', 'OpenGL.platform.CurrentContextIsValid', 'OpenGL.platform.GL', 'OpenGL.platfo
   rm.GLU', 'OpenGL.platform.GLUT', 'OpenGL.platform.GLUT_GUARD_CALLBACKS', 'OpenGL
   .platform.PLATFORM', 'OpenGL.platform.createBaseFunction', 'OpenGL_accelerate',
   'OpenGL_accelerate.arraydatatype', 'OpenGL_accelerate.errorchecker', 'OpenGL_acc
   elerate.latebind', 'OpenGL_accelerate.wrapper']

EXE はビルドできているので、試しに実行するとエラーメッセージが現れる。

.. code-block:: text

   Traceback (most recent call last):
     File "main.py", line 3, in <module>
     File "OpenGL\GL\__init__.pyc", line 3, in <module>
     File "OpenGL\GL\VERSION\GL_1_1.pyc", line 10, in <module>
     File "OpenGL\platform\__init__.pyc", line 35, in <module>
     File "OpenGL\platform\__init__.pyc", line 26, in _load
     File "OpenGL\plugins.pyc", line 14, in load
     File "OpenGL\plugins.pyc", line 28, in importByName
   ImportError: No module named win32

``win32`` というのは ``OpenGL.platform.win32`` モジュールのことと思われる。
試しに ``import OpenGL.platform.win32`` の一行を :file:`main.py` に加えると、
オリジナルのスクリプト、py2exe ビルドおよび成果物の EXE の実行のすべてがうまくいく。

うまくいくが、そうすると Windows 環境でないところで意味のないコードになる。
やはりここは ``setup`` 側で対応したい。
:file:`main.py` を元に戻して、こういうふうにするのはどうだろうか。

.. code-block:: python

   setup(console=['main.py'],
         options={"py2exe":{"includes":["OpenGL.platform.win32"]}})

PyQt4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
拡張子が ``pyw`` のケースに挑戦してみる。

.. code-block:: python

   # -*- coding: utf-8 -*-
   import sys
   from PyQt4 import QtGui, QtCore

   class Example(QtGui.QWidget):

       def __init__(self):
           super(Example, self).__init__()
           self.initUI()

       def initUI(self):
           self.cal = QtGui.QCalendarWidget(self)
           self.cal.setGridVisible(True)
           self.cal.move(20, 20)
           self.connect(self.cal, QtCore.SIGNAL('selectionChanged()'),
               self.showDate)

           self.label = QtGui.QLabel(self)
           date = self.cal.selectedDate()
           self.label.setText(str(date.toPyDate()))
           self.label.move(130, 260)

           self.setWindowTitle('Calendar')
           self.setGeometry(300, 300, 350, 300)

       def showDate(self):
           date = self.cal.selectedDate()
           self.label.setText(str(date.toPyDate()))

   if __name__ == '__main__':
       app = QtGui.QApplication(sys.argv)
       ex = Example()
       ex.show()
       app.exec_()

詳細は省くが :file:`setup.py` の ``setup`` 部分は次のようになる。

.. code-block:: python

   setup(windows=['main.pyw'],
         data_files=data_files)

ビルドして実行する。いきなりエラーメッセージが現れ、ログファイルを見るように言われる。

.. code-block:: text

   Traceback (most recent call last):
     File "main.pyw", line 6, in <module>
     File "PyQt4\QtGui.pyc", line 12, in <module>
     File "PyQt4\QtGui.pyc", line 10, in __load
   ImportError: No module named sip

``sip`` なるモジュールがないという。
これは Py2exe Wiki に解法が書かれていて、例えば次のように書き換えるのがよい。
``options`` キーワード引数をいじるのだ。

.. code-block:: python

   setup(windows=['main.pyw'],
         options={"py2exe":{"includes":["sip"]}},
         data_files=data_files)

ビルド後の :file:`dist` フォルダーはこうなる：

.. code-block:: console

   $ ls -l dist
   合計 21M
   -rwxr-xr-x 1 work ????  71K 8月  24  2010 bz2.pyd*
   -rw-r--r-- 1 work ???? 1.4M 4月  22 22:05 library.zip
   -rwxr-xr-x 1 work ????  20K 4月  22 22:05 main.exe*
   drwxr-xr-x 1 work ????    0 4月  22 21:32 Microsoft.VC90.CRT/
   -rwxr-xr-x 1 work ???? 1.6M 5月   2  2011 PyQt4.QtCore.pyd*
   -rwxr-xr-x 1 work ???? 5.5M 5月   2  2011 PyQt4.QtGui.pyd*
   -rwxr-xr-x 1 work ???? 2.1M 8月  24  2010 python26.dll*
   -rwxr-xr-x 1 work ???? 2.2M 3月  21  2011 QtCore4.dll*
   -rwxr-xr-x 1 work ???? 7.6M 3月  21  2011 QtGui4.dll*
   -rwxr-xr-x 1 work ????  12K 8月  24  2010 select.pyd*
   -rwxr-xr-x 1 work ????  65K 5月   2  2011 sip.pyd*
   -rwxr-xr-x 1 work ???? 572K 8月  24  2010 unicodedata.pyd*
   -rwxr-xr-x 1 work ????  49K 8月  24  2010 w9xpopen.exe*

Pygame
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
実はこれが最も出力ファイルがマッシブとなるようだ。現在調査中。

参考ページ http://www.pygame.org/wiki/Pygame2exe

.. include:: /_include/python-refs-core.txt
.. _Py2exe: http://www.py2exe.org/
