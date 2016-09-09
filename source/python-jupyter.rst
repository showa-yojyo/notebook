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

     * jupyter_client: 4.3.0
     * jupyter_console: 5.0.0
     * jupyter_core: 4.1.1

関連リンクおよび参考サイト
======================================================================
`Project Jupyter <http://jupyter.org/>`__
  Jupyter 開発サイトのホームページ。

`Jupyter console <https://jupyter-console.readthedocs.io/en/latest/>`__
  Jupyter Console 開発サイトのホームページ。
  中身は開発者向けであり、利用者に対する気の利いた文書のようなものはない。

`The Jupyter notebook <https://jupyter-notebook.readthedocs.io/en/latest/>`__
  Jupyter Notebook 開発サイトのホームページ。

`A Qt Console for Jupyter <https://jupyter.org/qtconsole/stable/>`__
  Jupyter QtConsole 開発サイトのホームページ。

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

設定を理解する
======================================================================

設定ファイルの仕組みを理解する
----------------------------------------------------------------------
コマンドラインツールとして実装されている Jupyter の各サブコマンドには
それぞれ専用の設定ファイルが対応する。
設定ファイル自身は optional なので、
利用者が不要と判断すればわざわざ作成することはない。

例えば後述するサブコマンド :code:`jupyter nbconvert` はそれ専用の
設定ファイルを扱っており、その既定のパスは
:file:`$HOME/.jupyter/jupyter_nbconvert_config.py` である。
このファイルのスケルトンを得るには、次のようにする（一部加工済）。

.. code-block:: console

   $ jupyter nbconvert --generate-config
   Writing default config to: $HOME\.jupyter\jupyter_nbconvert_config.py

* 他のサブコマンドも同様にオプション ``--generate-config`` を指定することで
  そのサブコマンド専用設定ファイルのスケルトンを
  既定のディレクトリーに生成することができるものがある。

* 設定ファイルで指定できる項目はいずれもコマンドライン引数の形でも指定できる。
  同じ項目について、設定ファイルとコマンドラインとで衝突するような値をそれぞれで指定すると、
  コマンドラインでの指定が常に優先されるはずだ。

関連ディレクトリーを理解する
----------------------------------------------------------------------
端末から :program:`jupyter` を次のように実行すると Jupyter が参照する
ディレクトリーをすべて確認できる（一部加工済）：

.. code-block:: console

   $ jupyter --paths
   config:
       $HOME\.jupyter
       D:\Miniconda3\etc\jupyter
       C:\ProgramData\jupyter
   data:
       C:\Users\$USER\AppData\Roaming\jupyter
       D:\Miniconda3\share\jupyter
       C:\ProgramData\jupyter
   runtime:
       C:\Users\$USER\AppData\Roaming\jupyter\runtime

* :program:`jupyter` は上の三種の区分別にディレクトリーを表示するための
  コマンドラインオプションも提供している。

* ``config:`` で列挙されたものは Jupyter のサブコマンドの設定ファイル置き場だ。
  設定ファイルについては、それを扱う個々のサブコマンドのところで述べる。

環境変数を理解する
----------------------------------------------------------------------
Jupyter は先述の関係ディレクトリーの区分に対応する環境変数を規定している。

* :envvar:`JUPYTER_CONFIG_DIR`
* :envvar:`JUPYTER_PATH`
* :envvar:`JUPYTER_RUNTIME_DIR`

環境変数のどれかに何らかのディレクトリーパスを指定すると、
それが対応する区分のものの地点を表すものとして取り扱われる。

サブコマンドを確認する
======================================================================
:program:`jupyter` のサブコマンドを知るには、
この実行ファイルがあるディレクトリーでファイル :file:`jupyter-*.exe` を表示すればよい。
ハイフン以降拡張子以前の文字列がサブコマンド名と合致する。

.. code-block:: console

   $ cd /d/Miniconda3/Scripts
   $ ls jupyter*.exe
   jupyter.exe*             jupyter-nbextension.exe*
   jupyter-console.exe*     jupyter-notebook.exe*
   jupyter-kernelspec.exe*  jupyter-qtconsole.exe*
   jupyter-migrate.exe*     jupyter-serverextension.exe*
   jupyter-nbconvert.exe*   jupyter-trust.exe*

* :code:`jupyter subcommand args` を実行すると、実際には
  :code:`jupyter-subcommand args` を実行することと同じであると考えられる。

* どのサブコマンドもオプション ``--help`` と ``--help-all`` を提供している。
* サブコマンドにはさらにサブコマンドが存在することがある。
  一例を挙げると :code:`jupyter nbextenion list` だ。

サブコマンド :code:`jupyter console`
======================================================================
このサブコマンドはコンソールアプリケーションのセッションを現在の端末ウィンドウに開始する。

:code:`jupyter console`
  このコマンドを実行すると、その場で IPython のセッションが開始する。
  :doc:`/python-ipython` で習得した物事が全て通用する。

:code:`jupyter console --kernel kernel_name`
  開始するための既定のカーネルを指定する。
  このオプションがないと ``python`` が指定されたものとして振る舞う。

* そういうわけで、Python 以外にも何かカーネルをインストールしないと面白くない。

* オプション ``--generate-config`` を与えると、
  このサブコマンド専用の設定ファイルのスケルトンを
  前述のディレクトリーに生成する。

.. todo:: カーネルを何か入れてから再度サブコマンドを試す。

サブコマンド :code:`jupyter kernelspec`
======================================================================
このサブコマンドは Jupyter のカーネルの詳細を管理するためのものだ。
Jupyter インストール直後にサブコマンド ``list`` を実行するとこのような結果を出力する。

.. code-block:: console

   $ jupyter kernelspec list
   Available kernels:
     python3    D:\Miniconda3\lib\site-packages\ipykernel\resources

* 上記ディレクトリーの中身は Python ロゴが描かれたサイズの異なる PNG ファイル 2 個だ。

.. todo:: これの正体は何だ？

サブコマンド :code:`jupyter migrate`
======================================================================
私はこれを利用する必要はないらしい。
事実、IPython から Jupyter に移行したい資源は何もなかったはずだ。

.. code-block:: console

   $ jupyter migrate
   [JupyterMigrate] Found nothing to migrate.

サブコマンド :code:`jupyter nbconvert`
======================================================================
このサブコマンドを ipynb ファイルから指定する形式のファイルを生成変換するツールとして利用する。
実際にいくつかの用例を試したので、感想を記す。

:code:`jupyter nbconvert helloworld.ipynb`
  ファイル :file:`helloworld.ipynb` から :file:`helloworld.html` を生成する。

* これは Jupyter Notebook 稼働中にブラウザーで目にするものと同じだが、
  これをブラウザー上で編集することはできない。

* ちなみにこのコマンドラインで生成する HTML ファイルはサイズが思いのほか大きくなる。
  見栄えがショボくても気にならないようなときには
  オプション :code:`--template basic` を与えることで
  単純な HTML ファイルを生成させたい。

:code:`jupyter nbconvert --to latex helloworld.ipynb`
  本来ならば LaTeX ファイルを生成するのだが、現在次の例外が発生して失敗する。
  Pandoc というものを準備する必要があるようだ。

  .. code-block:: console

     [NbConvertApp] Converting notebook helloworld.ipynb to latex
     [NbConvertApp] ERROR | Error while converting 'helloworld.ipynb'
     Traceback (most recent call last):
       File "D:\Miniconda3\lib\site-packages\nbconvert\nbconvertapp.py", line 357, in export_single_notebook
         output, resources = self.exporter.from_filename(notebook_filename, resources=resources)

       --- 略 ---

       File "D:\Miniconda3\lib\site-packages\nbconvert\utils\pandoc.py", line 76, in get_pandoc_version
         raise PandocMissing()
     nbconvert.utils.pandoc.PandocMissing: Pandoc wasn't found.
     Please check that pandoc is installed:
     http://pandoc.org/installing.html

* オプション ``--to`` を明示的に指示しないと ``html`` と指定されたものとして振る舞う。
* オプション ``--to`` の受け付ける引数には ``html`` の他に
  ``latex``, ``pdf``, ``markdown``, ``rst`` といった、
  試しがいのある書式が含まれているようだ。

* オプション ``--stdout`` を与えると、指示した変換内容を標準出力に書き出す。
* オプション ``--generate-config`` を与えると、
  このサブコマンド専用の設定ファイルのスケルトンを
  前述のディレクトリーに生成する。

.. todo:: Pandoc とやらを調査する。

サブコマンド :code:`jupyter nbextension`
======================================================================
このサブコマンドは Notebook の拡張を管理するためのものだ。
Jupyter インストール直後にサブコマンド ``list`` を実行するとこのような結果を出力する。

.. code-block:: console

   $ jupyter nbextension list
   Known nbextensions:
     config dir: D:\Miniconda3\etc\jupyter\nbconfig
       notebook section
         nb_conda/main enabled
         - Validating: ok
         nbpresent/js/nbpresent.min enabled
         - Validating: ok
         jupyter-js-widgets/extension enabled
         - Validating: ok
         nb_anacondacloud/main enabled
         - Validating: ok
       tree section
         nb_conda/tree enabled
         - Validating: ok

サブコマンド :code:`jupyter notebook`
======================================================================
このサブコマンドは Jupyter Notebook を管理するものだ。
通常実行することで Tornado ベースの HTTP サーバーを起動し、
Notebook クライアントが利用可能になる。

:code:`jupyter notebook`
  Jupyter Notepad を起動する。
  同時にダッシュボードページをブラウザーで開く。
  次節で詳しく述べる。

:code:`jupyter notebook --no-browser`
  Jupyter Notepad を起動するが、ブラウザーでダッシュボードページを開かない。
  つまり、開きたい ipynb ファイルがあれば利用者がそれに対応するアドレスに、
  好きな手段によりアクセスする。

* オプション ``--generate-config`` を与えると、
  このサブコマンド専用の設定ファイルのスケルトンを
  前述のディレクトリーに生成する。

Jupyter Notebook を起動する
----------------------------------------------------------------------
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
  下にコマンドラインの一例を記す。好みで ConEmu に対するアイコンやタブ名を指定するのもよい。

  .. code-block:: text

     D:\Miniconda3\Scripts\jupyter.exe notebook -new_console:d:D:\home\yojyo\jupyter

* :code:`jupyter notebook` には当然ながらコマンドラインオプションがある。
  利用価値のありそうなものがあれば洗い出しておきたい。

* 起動時ログの警告の類を解決しておきたい。PDF うんぬんは気になる。

Jupyter Notebook を終了する
----------------------------------------------------------------------
サービスを起動した端末ウィンドウで :kbd:`Ctrl + C` を押すと、サービスが停止する。

.. code-block:: console

   [I HH:MM:SS.570 NotebookApp] Shutting down kernels
   [I HH:MM:SS.298 NotebookApp] Kernel shutdown: f887fdc0-f81c-410c-a941-6820a4b2a5c7
   $ 

サブコマンド :code:`jupyter qtconsole`
======================================================================
このサブコマンドは Jupyter QtConsole アプリケーション、
すなわち Qt ベースのコンソール風アプリケーションを起動する。
Qt ウィンドウで実現された IPython セッションと表現すれば適当だろうか。
下の図は Jupyter QtConsole を起動し、たまたま手許にある
Matplotlib のデモコードを一つ実行したときの画面だ。

.. figure:: /_static/jupyter-qtconsole.png
   :align: center
   :alt: Jupyter QtConsole
   :scale: 50%

   Jupyter QtConsole

:code:`jupyter qtconsole`
  Jupyter QtConsole を起動する。

* 何か既視感があると思ったが、これは :doc:`/python-ipython` で調査した
  :code:`ipython qtconsole` の挙動と酷似している。
  確認のために久しぶりに :code:`ipython qtconsole` してみたら、
  ウィンドウタイトルが :guilabel:`Jupyter QtConsole` となっていた。
  つまり、両者は同一のアプリケーションなのだろう。

* オプション ``--generate-config`` を与えると、
  このサブコマンド専用の設定ファイルのスケルトンを
  前述のディレクトリーに生成する。

サブコマンド :code:`jupyter serverextension`
======================================================================
Jupyter インストール直後にサブコマンド ``list`` を実行するとこのような結果を出力する。

.. code-block:: console

  $ jupyter serverextension list
  config dir: D:\Miniconda3\etc\jupyter
      nb_anacondacloud enabled
      - Validating...
        nb_anacondacloud  ok
      nb_conda enabled
      - Validating...
        nb_conda  ok
      nbpresent enabled
      - Validating...
        nbpresent  ok

* この情報は Jupyter Notebook のダッシュボードでも形を変えて確認できそうだ。

サブコマンド :code:`jupyter trust`
======================================================================
.. todo:: 調査する。

ノート
======================================================================
Jupyter の一連の機能を利用して気付いた点や思い付き等を記す。

* YouTube で検索すると Jupyter の基礎的な利用法をコーチするビデオが多数見つかるだろう。

* Jupyter Notebook のサービス実行用と ipynb ファイルの実行用の両方がそれぞれ
  Python のプロセスを管理する。
  プアな環境だと Python プロセスによるメモリ食いが気になる。

* :program:`jupyter` の利用可能な「サブコマンド」の集合が文書化されていない？

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
.. _Jupyter: http://jupyter.org/
