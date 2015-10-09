======================================================================
Python 移行ノート
======================================================================

私の Windows マシンでの Python のアップグレード作業に必要な手順について記す。
まずは長期に亘り安定して利用してきた 2.6 から、
2.x 台最終版である 2.7 への移行作業を記す。

そして 2014 年夏、Windows 7 の 64 ビット機に Python 3.4 環境を構築する機会が訪れた。

.. contents:: ノート目次

.. note::

   * OS

     * Windows XP Home Edition SP 3
     * Windows 7 Home Premium SP 1
     * Windows 10 Home Edition

   * Python upgrading

     * from 2.6.6 to 2.7.3
     * from 2.7.3 to 3.4.1
     * from 3.4.1 to 3.5.0

2.6 から 2.7 への移行計画
======================================================================
実際のところ、手間をかけて 2.6 から 2.7 へ移行する利点は今のところなさそうに思える。
それは 2.7 での新機能を勉強してから判断すればよい。
とにかく、アップグレード手順を残しておく。

Python 2.6 site-packages の状態を保存
----------------------------------------------------------------------
私の環境では pip_ がインストールされているハズなので、
2.6 環境にインストールしたサードパーティー製パッケージを書き出しておく。

ただし、バージョンは不要なので ``cut`` にて削っておく。

.. code-block:: console

   $ cd D:/Python26/lib/site-packages
   $ pip freeze | cut -d= -f 1 > mypkgs.txt

後ほど :file:`mypkgs.txt` をテキストエディターで編集する。

Python 2.7 本体をインストール
----------------------------------------------------------------------
* Python_ の公式サイトから :file:`python-2.7.3.msi` をダウンロードする。
* 普通に Explorer 上から実行して、Python 2.6 のインストール場所の隣りにインストールする。

Python 2.6 フォルダーから一部のファイルをコピーする
----------------------------------------------------------------------
正直、この作業が必要なのかどうかわかっていない。

* :file:`sitecustomize.py` を 2.6 フォルダーの :file:`site-packages` フォルダーから
  2.7 フォルダーの対応する位置にコピーする。

最初に手動で準備するもの
----------------------------------------------------------------------
* setuptools_: インストーラーを利用する。
  :file:`setuptools-0.6c11.win32-py2.7.exe` のようなファイル名のものをダウンロードページから取得する。

* pip_: :file:`pip.1.1-tar.gz` を入手して、解凍後 :file:`setup.py` を利用する。

  .. code-block:: console

     $ python27 setup.py install

Windows インストーラーを利用するもの
----------------------------------------------------------------------
``pip`` ではインストールできないものを先にインストールしておく。

と言うより、``pip`` でインストールしたいパッケージ X がパッケージ Y に依存しているとして、
Y は Windows インストーラーでインストールするべきものであるとする。
先に Y をインストールしておかないと、
``pip`` で X をインストールする段になって、Y の扱いが怖いことになりそうだから、
ここで述べる手順がある。

私の場合のパッケージ群は次の通り。
インストーラーの拡張子は exe だったり msi だったりするが、
気にしないで構わないだろう。

* PIL_: 公式サイトに 2.7 用のものがある。
* NumPy_: 2.7 OK
* SciPy_: 2.7 OK
* Matplotlib_: 2.7 OK
* Pygame_: 2.7 OK
* Py2exe_: 2.7 OK
* PyQt4_: 2.7 OK
* pysparse: `Python Extension Packages for Windows - Christoph Gohlke`_ を利用させてもらう。

旧環境での pip freeze の出力を利用するもの
----------------------------------------------------------------------
2.6 環境で ``pip freeze`` することで、利用中の ``site-packages`` パッケージが得られる。
これを 2.7 環境の ``pip`` に食わせて様子見とする。

先ほど得た :file:`mypkgs.txt` をテキストエディターで編集する。
PIL, NumPy などのインストーラーモノの行を削除して、このテキストファイルを上書きする。
編集後、おもむろに下記コマンドラインを実行する。
かなり時間がかかることを覚悟することだ。

.. code-block:: console

   $ cd D:/Python27/Scripts
   $ ./pip install -r mypkgs.txt

* 何度か失敗するかもしれないが、成功したものを :file:`mypkgs.txt` から順次削除していき、
  再度 ``pip`` 呼び出しをすればよい。
* ログを取るのもよいだろう。

特殊なもの
----------------------------------------------------------------------
Subversion の Python binding を利用しているため、これをセットアップする。

* http://sourceforge.net/projects/win32svn/files/1.7.6/

* svn-win32-1.7.6-ap24_py27.zip をダウンロード。
  解凍してフォルダーを潜る。下記フォルダーを ``site-packages`` にコピー。

  * libsvn
  * svn_python

2.6 のクリーンナップ
----------------------------------------------------------------------
* Windows のコントロールパネル「プログラムの追加と削除」を利用して、
  Python 2.6 関連のパッケージを全部アンインストールする。

* 念のため、残骸を確認するべし。
  自分で作った設定ファイルやらがある場合、適宜修正を加え 2.7 に引っ越す。

* Python 2.6.6 をアンインストールするのはパッケージを全部片付けてからの最後。

ツールや環境変数の修正
----------------------------------------------------------------------
移行、完全に個人的なメモ。他の人には通用しない作業だ。

.bashrc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
この設定をする理由は、私が Cygwin で ``bash`` をインタラクティブシェルとして利用しており、
そこから Windows 用の Python を呼び出すことが多いことによる。

エイリアス ``python27`` を追加。

.. code-block:: bash

   alias a='alias'
   a python26='D:/Python26/python.exe'
   a python27='D:/Python27/python.exe'

.bash_profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``$PATH`` に Python 関連の記述がある場合は修正する。
設定理由は上述と同じ。

SendToCygwin.ini
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
「Cygwin に送る」というユーティリティがあり、私はこれを偏愛している。
その設定ファイルを更新しておく。

.. code-block:: ini

   *.py =python27 %F ||
   *.pyw =python27 %F ||

環境変数 PATH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``D:\Python26`` を ``D:\Python27`` に置換。

2.7 から 3.4 への移行
======================================================================
Python 自身のメジャーバージョンアップもさることながら、OS も 64 ビット対応のものである。

Python 3.4 本体をインストールする
----------------------------------------------------------------------
次の 2 ステップで十分だ。

* Python_ の公式サイトから :file:`python-3.4.1.amd64.msi` をダウンロードする。
* インストーラーを実行する。
  インストールオプションで pip が含まれるようにすること。

サードパーティー製パッケージのインストール
----------------------------------------------------------------------
インストーラーからインストールするものと、pip でインストールするものに大別して作業することにした。

Windows インストーラーを利用するもの
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
筆者環境では、次のパッケージ群は
`Python Extension Packages for Windows - Christoph Gohlke`_ のビルドを利用した。
わかりやすさのため、インストーラーのファイル名そのものをここに記す。

* :file:`matplotlib-1.3.1.win-amd64-py3.4.exe`
* :file:`numpy-MKL-1.8.2.win-amd64-py3.4.exe`
* :file:`Pillow-2.5.1.win-amd64-py3.4.exe`
* :file:`pygame-1.9.2a0.win-amd64-py3.4.exe`
* :file:`PyOpenGL-3.1.0.win-amd64-py3.4.exe`
* :file:`PyOpenGL-accelerate-3.1.0.win-amd64-py3.4.exe`
* :file:`pyparsing-2.0.2.win-amd64-py3.4.exe`
* :file:`scipy-0.14.0.win-amd64-py3.4.exe`

PyQt5 など、それ以外のパッケージについては、それぞれの公式サイト提供のビルドを利用した。

旧環境での pip freeze の出力を利用するもの
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#. 旧環境 (2.7) の ``pip freeze`` の出力結果をテキストファイルに保存 (:file:`mypkgs.txt`) する。
#. :file:`mypkgs.txt` を編集し、Windows インストーラーでインストールしたパッケージの行を削除する。
#. 前回移行時と同様の手順に従う。

.. code-block:: console

   $ cd D:/Python34/Scripts
   $ ./pip install -r mypkgs.txt

2.7 のクリーンナップ
----------------------------------------------------------------------
前述の 2.6 のクリーンナップと同様。

ツールや環境変数の修正
----------------------------------------------------------------------
SendToCygwin の Windows 7 版が存在しないことを除いて、前述と同様。

環境変数
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
以前は :file:`sitecustomize.py` で行っていたエンコーディング関連の指定を環境変数設定で実現する。
Windows のユーザー環境変数に次のものを指定しておくのが具合がよい。

================ ========================
環境変数         設定値
================ ========================
PYTHONIOENCODING UTF-8
PYTHONPATH       自作モジュールのパス
================ ========================

ドットファイル
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* :file:`.bashrc` の Python 関連のコードを修正。
* :file:`.bash_profile` の Python 関連のコードを修正。

2to3.py 関連
----------------------------------------------------------------------
もっとも面倒な作業は、これまで自分が書いたすべての Python コードを Python 3 仕様に書き改めることだ。
しかし :file:`$PYTHONDIR/Tools/Scripts/2to3.py` で機械的に処理すれば一応は動きそう。

3.4 から 3.5 への以降
======================================================================
OS を Windows 10 にアップグレードしたときには 3.4 環境はビクともしなかった。
なので、今回は OS を変えてから初めての Python のアップグレードになる。

Python 3.5 本体をインストールする
----------------------------------------------------------------------
次の手順を踏む。

#. Python_ の公式サイトから :file:`python-3.5.0-amd64.exe` をダウンロードする。
#. インストーラーを実行する。
   その際は次のような点に気を配りたい。

   * Customize installation を選択する。
   * pip は当然必要だ。
   * Install for all users をオンにして、インストールパスをそれらしい所に設定する。

サードパーティー製パッケージのインストール
----------------------------------------------------------------------
むしろこちらがメインの作業だ。

Windows インストーラーを利用するもの
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
言い換えれば諸事情により pip に頼れないパッケージ群のことだ。
各パッケージの公式サイトおよび
`Python Extension Packages for Windows - Christoph Gohlke`_ が配布するインストーラーに頼る。

* 拡張子が ``exe`` や ``msi`` のファイルは、よくあるインストーラー。
  インストールの順序は任意でよいハズ。

* 拡張子が ``whl`` のファイルについては、これらをダウンロードしておき pip に処理させるもの。
  依存パッケージがあるならば、先にインストールを済ませる必要がある。

コツとしては NumPy_ が一番最初にインストールを済ませるべきものであろう。

* :file:`lxml-3.4.4-cp35-none-win_amd64.whl` (Christoph)
* :file:`matplotlib-1.4.3-cp35-none-win_amd64.whl` (Christoph)
* :file:`numpy‑1.10.0+mkl‑cp35‑none‑win_amd64.whl` (Christoph)
* :file:`pygame-1.9.2a0-cp35-none-win_amd64.whl` (Christoph)
* :file:`PyOpenGL-3.1.1a1-cp35-none-win_amd64.whl` (Christoph)
* :file:`PyOpenGL_accelerate-3.1.1a1-cp35-none-win_amd64.whl` (Christoph)
* :file:`reportlab-3.2.0-cp35-none-win_amd64.whl` (Christoph)
* :file:`scipy-0.16.0-cp35-none-win_amd64.whl` (Christoph)

旧環境での pip freeze の出力を利用するもの
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
インストーラーによる作業がすべて終わってようやく pip が使える。

今回試したらインストーラーではなく pip で済むようになっていたパッケージは次のとおり。

* Pillow (:file:`Pillow-3.0.0-cp35-none-win_amd64.whl`)
* PyOpenGL (:file:`PyOpenGL-3.1.0.tar.gz`): ただしバージョンの関係で上述のインストーラーを採用する。

旧環境のクリーンナップ
----------------------------------------------------------------------
#. Windows のコントロールパネル「プログラムと機能」から 3.4 のパッケージと Python 本体をアンインストールする。
#. :file:`D:\Python34` フォルダーを削除する。
   中に入っている残骸がサードパーティー製パッケージの関連ファイルだけであることを確認できれば、
   そうする。

ツールや環境変数の修正
----------------------------------------------------------------------
3.4 から 3.5 への移行に伴う変更は軽微な修正作業になる。

ドットファイル
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Cygwin bash で作業をするため、主にエイリアスとパスに関わる項目の設定を更新する。

* :file:`.bashrc` の Python 関連のコードを修正。
* :file:`.bash_profile` の Python 関連のコードを修正。

ConEmu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ConEmu の Settings... > Startup > Tasks の Predefined tasks を更新する。

.. csv-table::
   :delim: @
   :header: Task, Command
   :widths: 12, 88

   {Python}@``D:\Python35\python.exe -i``
   {IPython}@``D:\Python35\Scripts\ipython3.exe``
   {IPython}@``D:\Python35\Scripts\ipython3.exe qtconsole --pylab inline``
   {isympy}@``D:\Python35\python.exe "D:\home\yojyo\devel\sympy\bin\isympy" -- --TerminalIPythonApp.pylab_import_all=False``

残項目
----------------------------------------------------------------------
* IPython_ と Matplotlib_ の連携が何やらおかしい。
  セッション起動時にいきなり次の不具合が発生する。
  もしかるすると IPython のアップグレードで設定項目の何かに変化があったか。

  .. code-block:: text

     Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)]
     Type "copyright", "credits" or "license" for more information.

     IPython 4.0.0 -- An enhanced Interactive Python.
     ?         -> Introduction and overview of IPython's features.
     %quickref -> Quick reference.
     help      -> Python's own help system.
     object?   -> Details about 'object', use 'object??' for extra details.
     [TerminalIPythonApp] WARNING | Eventloop or matplotlib integration failed. Is matplotlib installed?
     ---------------------------------------------------------------------------
     ImportError                               Traceback (most recent call last)
     d:\python35\lib\site-packages\IPython\core\shellapp.py in <lambda>(key)
         217         shell = self.shell
         218         if self.pylab:
     --> 219             enable = lambda key: shell.enable_pylab(key, import_all=self.pylab_import_all)
         220             key = self.pylab
         221         elif self.matplotlib:

     d:\python35\lib\site-packages\IPython\core\interactiveshell.py in enable_pylab(self, gui, import_all, welcome_message)
        3169         from IPython.core.pylabtools import import_pylab
        3170
     -> 3171         gui, backend = self.enable_matplotlib(gui)
        3172
        3173         # We want to prevent the loading of pylab to pollute the user's

     d:\python35\lib\site-packages\IPython\core\interactiveshell.py in enable_matplotlib(self, gui)
        3130                 gui, backend = pt.find_gui_and_backend(self.pylab_gui_select)
        3131
     -> 3132         pt.activate_matplotlib(backend)
        3133         pt.configure_inline_support(self, backend)
        3134

     d:\python35\lib\site-packages\IPython\core\pylabtools.py in activate_matplotlib(backend)
         272     matplotlib.rcParams['backend'] = backend
         273
     --> 274     import matplotlib.pyplot
         275     matplotlib.pyplot.switch_backend(backend)
         276

     d:\python35\lib\site-packages\matplotlib\pyplot.py in <module>()
          25
          26 import matplotlib
     ---> 27 import matplotlib.colorbar
          28 from matplotlib import style
          29 from matplotlib import _pylab_helpers, interactive

     d:\python35\lib\site-packages\matplotlib\colorbar.py in <module>()
          30
          31 import matplotlib as mpl
     ---> 32 import matplotlib.artist as martist
          33 import matplotlib.cbook as cbook
          34 import matplotlib.collections as collections

     d:\python35\lib\site-packages\matplotlib\artist.py in <module>()
          10 import matplotlib.cbook as cbook
          11 from matplotlib import docstring, rcParams
     ---> 12 from .transforms import Bbox, IdentityTransform, TransformedBbox, \
          13                        TransformedPath, Transform
          14 from .path import Path

     d:\python35\lib\site-packages\matplotlib\transforms.py in <module>()
          37 import numpy as np
          38 from numpy import ma
     ---> 39 from matplotlib._path import (affine_transform, count_bboxes_overlapping_bbox,
          40     update_path_extents)
          41 from numpy.linalg import inv

     ImportError: DLL load failed: 指定されたモジュールが見つかりません。

* PyQt5 の Python 3.5 版のインストール

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
.. include:: /_include/python-refs-vision.txt
.. _PyQt4: http://www.riverbankcomputing.com/software/pyqt/intro
.. _Py2exe: http://www.py2exe.org/
.. _Pygame: http://www.pygame.org/
