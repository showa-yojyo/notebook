======================================================================
インストール
======================================================================
本稿では Matplotlib_ の（ごく限定的な環境向けの）インストール手順を記す。

.. contents::

Matplotlib の依存パッケージと関連パッケージをインストール
======================================================================
Python 環境を Anaconda_ もしくは Miniconda_ で実現しているのであれば、
:ref:`python-pkg-proc` のように作業をすればよく、
この節と次の節は読み飛ばして構わない。
本体が必要とする他のパッケージを自動で察知してインストールを推奨してくれるので、
作業漏れが起こりにくい。

NumPy をインストール
----------------------------------------------------------------------
Matplotlib は NumPy_ を多用しているので、当然これを先にインストールしておく。
→ :doc:`/python-numpy/setup`

Pillow をインストール
----------------------------------------------------------------------
Matplotlib の画像ファイル出力機能の裏に Pillow_ が働いている。
→ :doc:`/python-pillow`

PyParsing をインストール
----------------------------------------------------------------------
必要に応じて PyParsing_ をインストールする。
このパッケージは Matplotlib が TeX 表記を取り扱う際に利用する機能を提供する。

Matplotlib 本体をインストール
======================================================================
Python 2.7.3 環境設定時は公式インストーラーのモジュール群が動作しなかった。
具体的に言うと、簡単なプロットを定義した後に ``matplotlib.pyplot.show()`` すると、
単に白いウィンドウが出て CPU 使用率が 100% になるという挙動だった。

ものの試しに `Python Extension Packages for Windows - Christoph Gohlke`_ で配布している
インストーラーに差し替えてみたら、期待通りの動作をした。

Python 3.4 でも、どうぜ公式サイトでは 64 ビット版のビルドなどしないので、
こちらのインストーラーを利用する。

アップグレード
----------------------------------------------------------------------
Matplotlib をバージョン 1.3.1 から最新版にアップグレードしたときの模様を記す。

VC のコンパイラーを要するような特殊な Python パッケージについては、
これまでは専用のインストーラーに頼っていた。
ところが最近では標準 pip_ で環境に最適なパッケージをダウンロード、
インストールするような仕組みが整備されているようだ。
そういうわけで、今回のアップグレードは pip を利用した。
ただし、NumPy だけは先に最新版にアップグレードしておくほうが無難だ。
公式の NumPy の whl ファイルを参照するようで、これが私の環境にとっては都合が悪い。

.. code:: console

   $ pip install --upgrade matplotlib
   Downloading/unpacking matplotlib from https://pypi.python.org/packages/cp34/m/matplotlib/matplotlib-1.4.3-cp34-none-win_amd64.whl#md5=72e96f66866523cb5974f52038d25242
   Requirement already up-to-date: pytz in d:\python34\lib\site-packages (from matplotlib)
   Requirement already up-to-date: six>=1.4 in d:\python34\lib\site-packages (from matplotlib)
   Requirement already up-to-date: pyparsing>=1.5.6 in d:\python34\lib\site-packages (from matplotlib)
   Requirement already up-to-date: numpy>=1.6 in d:\python34\lib\site-packages (from matplotlib)
   Requirement already up-to-date: python-dateutil in d:\python34\lib\site-packages (from matplotlib)
   Installing collected packages: matplotlib
     Found existing installation: matplotlib 1.4.2
       Uninstalling matplotlib:
         Successfully uninstalled matplotlib
   Successfully installed matplotlib
   Cleaning up...

* :file:`matplotlib-1.4.3-cp34-none-win_amd64.whl` というアーカイブ名から、
  当方の環境 (Python 3.4, Windows 7 64bit) を考慮していることが窺える。

* ``Found existing installation: matplotlib 1.4.2`` とあるが、
  実際には 1.4.3 にアップグレードにされた。

Python 3.5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
理由は忘れたが上記の方法がうまく行かなかったので、
`Python Extension Packages for Windows - Christoph Gohlke`_ が配布するインストーラーに頼った。

* パッケージのビルドに利用している MSVC のバージョンに対応するランタイムが環境に必要なことに注意。
  特に :file:`msvcpxxx.dll` がない可能性がある。

動作確認
======================================================================
Matplotlib の初回インストールまたはアップグレード直後に確認することを記す。

バージョンを確認する
----------------------------------------------------------------------
Matplotlib のモジュールから直接バージョン番号を得ることで確認するには次のようにする。

.. code:: console

   $ python -c 'import matplotlib as mpl; print(mpl.__version__)'
   1.4.3

Anaconda または Miniconda で Python 環境を管理しているのであれば、
コマンドラインで :program:`conda` を用いる。

.. code:: console

   $ conda list matplotlib
   # packages in environment at D:\Miniconda3:
   #
   matplotlib                1.5.1               np111py35_0

もしくは :program:`pip` を用いる。

.. code:: console

   $ pip show matplotlib
   ---
   Metadata-Version: 1.1
   Name: matplotlib
   Version: 1.5.1
   Summary: Python plotting package
   Home-page: http://matplotlib.org
   Author: John D. Hunter, Michael Droettboom
   Author-email: matplotlib-users@python.org
   License: BSD
   Location: d:\miniconda3\lib\site-packages
   Requires: numpy, python-dateutil, pytz, cycler, pyparsing
   Classifiers:
     Development Status :: 5 - Production/Stable
     Intended Audience :: Science/Research
     License :: OSI Approved :: Python Software Foundation License
     Programming Language :: Python
     Programming Language :: Python :: 2
     Programming Language :: Python :: 3
     Topic :: Scientific/Engineering :: Visualization

簡単なプロットを確認する
----------------------------------------------------------------------
次のようなコードを実行してみて、それらしいイメージを目視で確認できたら
Matplotlib のインストールまたはアップグレードが成功したと判断してよい。
ちなみに IPython_ を利用する場合は、デフォルト設定でこのインポート文が省略できて
いきなり :code:`plt` の別名を参照することができて楽だ。

>>> import matplotlib.pyplot as plt
>>> plt.plot(range(4))
>>> plt.show()

環境設定にも依存するが、
基本的には :code:`plt.show()` の実行開始直後に下の画像のような、
プロットを描画するウィンドウが現れる。

.. figure:: /_images/mpl-tkagg.png
   :align: center
   :alt: TkAgg
   :width: 660px
   :height: 553px
   :scale: 50%

ここで Segmentation fault が出るようであれば、
後述するバックエンドを試行錯誤する必要がある。

ドキュメントを確保する
======================================================================
オフラインで学習する必要がある場合は、
公式サイトから PDF ファイルをダウンロードして、ローカルディスクに保存する。
最初のページに "Matplotlib Release 1.4.3" というタイトルと、著者の連名
"John Hunter, Darren Dale, Eric Firing, Michael Droettboom and the matplotlib development team"
が書かれている（途中でページ境界を突き破っている）。

* PDF ファイル全体は 2634 ページに及ぶ。
* 内容はナビゲーションが異なるものの、公式サイトの doc 以下と同じだ。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
.. include:: /_include/python-refs-vision.txt
.. _PyQt: http://www.riverbankcomputing.com/software/pyqt/intro
.. _PyParsing: https://pypi.python.org/pypi/pyparsing
