======================================================================
Py2exe 利用ノート
======================================================================

.. contents:: ノート目次

.. note::

   * OS: Windows XP Home Edition SP 3
   * 本稿において、利用した各パッケージのバージョンは次のとおり。

     * Python_: 2.6.6
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
TBW

.. _Python: http://www.python.org/
.. _Py2exe: http://www.py2exe.org/
