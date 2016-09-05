======================================================================
Jupyter 利用ノート
======================================================================
本稿は Python 製 Web アプリケーション Jupyter_ についての私的なノートだ。

.. contents:: ノート目次
   :depth: 3

.. note::

   本稿執筆時の動作環境は次のとおり。

   * OS: Windows 10 Home (64 bit)
   * Python_: 3.5.2 (64 bit)
   * Jupyter_: 1.0.0

関連リンクおよび参考サイト
======================================================================
`Project Jupyter <http://jupyter.org/>`__
  Jupyter 開発サイトのホームページ。

インストール
======================================================================
:ref:`python-pkg-proc` を参照してインストールすること。
図で示されているところの :program:`conda` を利用するルートになる。

参考までに私の Miniconda 環境で Python 本体しか使えない更地の仮想環境を作成し、
そこに Jupyter をインストールしようとすると、
どのような他の必要パッケージが一緒にインストールされるのかを調べた。
下に端末での入出力を掲載するが、かなりの数のパッケージを必要とすることがわかる。

.. code-block:: console

   $ conda install jupyter
   Fetching package metadata .........
   Solving package specifications: ..........
   Using Anaconda API: https://api.anaconda.org

   Package plan for installation in environment D:\Miniconda3\envs\jupyter-demo:

   The following NEW packages will be INSTALLED:

       _nb_ext_conf:        0.3.0-py35_0
       anaconda-client:     1.5.1-py35_0
       clyent:              1.2.2-py35_0
       colorama:            0.3.7-py35_0
       decorator:           4.0.10-py35_0
       entrypoints:         0.2.2-py35_0
       ipykernel:           4.4.1-py35_0
       ipython:             5.1.0-py35_0
       ipython_genutils:    0.1.0-py35_0
       ipywidgets:          5.2.2-py35_0
       jinja2:              2.8-py35_1
       jpeg:                8d-vc14_0       [vc14]
       jsonschema:          2.5.1-py35_0
       jupyter:             1.0.0-py35_3
       jupyter_client:      4.3.0-py35_0
       jupyter_console:     5.0.0-py35_0
       jupyter_core:        4.1.1-py35_0
       libpng:              1.6.22-vc14_0   [vc14]
       libtiff:             4.0.6-vc14_2    [vc14]
       markupsafe:          0.23-py35_2
       mistune:             0.7.2-py35_0
       nb_anacondacloud:    1.2.0-py35_0
       nb_conda:            2.0.0-py35_0
       nb_conda_kernels:    2.0.0-py35_0
       nbconvert:           4.2.0-py35_0
       nbformat:            4.1.0-py35_0
       nbpresent:           3.0.2-py35_0
       notebook:            4.2.2-py35_0
       openssl:             1.0.2h-vc14_0   [vc14]
       path.py:             8.2.1-py35_0
       pickleshare:         0.7.3-py35_0
       prompt_toolkit:      1.0.3-py35_0
       pygments:            2.1.3-py35_0
       pyqt:                4.11.4-py35_7
       python-dateutil:     2.5.3-py35_0
       pytz:                2016.6.1-py35_0
       pyyaml:              3.11-py35_4
       pyzmq:               15.4.0-py35_0
       qt:                  4.8.7-vc14_9    [vc14]
       qtconsole:           4.2.1-py35_0
       requests:            2.11.1-py35_0
       simplegeneric:       0.8.1-py35_1
       sip:                 4.18-py35_0
       six:                 1.10.0-py35_0
       tornado:             4.4.1-py35_0
       traitlets:           4.2.2-py35_0
       wcwidth:             0.1.7-py35_0
       widgetsnbextension:  1.2.6-py35_0
       win_unicode_console: 0.5-py35_0
       zlib:                1.2.8-vc14_3    [vc14]

   Proceed ([y]/n)? 

* 実際の作業環境ではこれらの被依存パッケージのうちのいくつかはすでに導入が済んでいる。
  ダウンロードとインストールに要する時間は上記のリストから想像するよりは短くなる。

* 同じことを確認するためのコマンドライン入力は
  :code:`conda create --dry-run -n jupyter-demo jupyter` でもよい。

起動する
======================================================================
端末ウィンドウで作業する。適当な作業ディレクトリーに移動してから
:program:`jupyter` を実行する。

.. code-block:: console

   $ jupyter notebook
   [W HH:MM:SS.352 NotebookApp] Unrecognized JSON config file version, assuming version 1
   [I HH:MM:SS.571 NotebookApp] [nb_conda_kernels] enabled, 2 kernels found
   [I HH:MM:SS.905 NotebookApp] [nb_conda] enabled
   [I HH:MM:SS.573 NotebookApp] ✓ nbpresent HTML export ENABLED
   [W HH:MM:SS.575 NotebookApp] ✗ nbpresent PDF export DISABLED: No module named 'nbbrowserpdf'
   [I HH:MM:SS.960 NotebookApp] [nb_anacondacloud] enabled
   [I HH:MM:SS.592 NotebookApp] Serving notebooks from local directory: D:\home\yojyo
   [I HH:MM:SS.592 NotebookApp] 0 active kernels
   [I HH:MM:SS.592 NotebookApp] The Jupyter Notebook is running at: http://localhost:8888/
   [I HH:MM:SS.607 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).

* このログ表示直後に、ウェブブラウザーがアクティブになり、
  そこに Jupyter Notebook のメイン画面（ダッシュボードと呼ばれている）
  を表示し、さらにそこにはこのサービスを起動したディレクトリーにある
  ファイルとサブディレクトリーの一覧を表示するはずだ。

* これはサービスプロセスなので、専用のコンソールウィンドウで実行するのがよいだろう。
  ConEmu の Tasks にコマンドラインを定義しておくか。

* :code:`jupyter notebook` には当然ながらコマンドラインオプションがある。
  利用価値のありそうなものがあれば洗い出しておきたい。

* 起動時ログの警告の類を解決しておきたい。PDF うんぬんは気になる。

終了する
======================================================================
サービスを起動した端末ウィンドウで :kbd:`Ctrl + C` を押すと、サービスが停止する。

.. code-block:: console

   [I HH:MM:SS.570 NotebookApp] Shutting down kernels
   [I HH:MM:SS.298 NotebookApp] Kernel shutdown: f887fdc0-f81c-410c-a941-6820a4b2a5c7
   $ 

ノート
======================================================================
.. todo:: 鋭意調査中。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
.. _Jupyter: http://jupyter.org/
