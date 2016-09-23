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

`IPython kernels for other languages <https://github.com/ipython/ipython/wiki/IPython-kernels-for-other-languages>`__
  カーネル一覧。
  どうやら一般的にカーネルごとにインストール方法が異なるらしい。

Pandoc_
  Notebook ファイルを LaTeX やさらには PDF 形式に変換するのにこれが必要になる。

Jupyter の概要を把握する
======================================================================
IPython と Jupyter Notebook がどのように作用し合うかをまとめた、
次の文書を読むと良い：

* `How IPython and Jupyter Notebook work <http://jupyter.readthedocs.io/en/latest/architecture/how_jupyter_ipython_work.html>`__

Terminal IPython
----------------------------------------------------------------------
* 承知しているが IPython とは REPL モデルの端末である。

The IPython Kernel
----------------------------------------------------------------------
* IPython Kernel は分離したプロセスであって、
  ユーザーコードを走らせたり補完を計算するようなことについての責任がある。

* Notebook や Qt コンソールのようなフロントエンドは
  ZeroMQ ソケッツを使って送信される JSON メッセージを用いて
  IPython Kernel とやりとりをする。

* 最初の図式。
  Terminal IPython と IPython Kernel との共通部分が実行部ということか。
  Terminal IPython には JSON も ZeroMQ も関係がなく、
  IPython Kernel には標準入出力のどちらも関係しない。

* 新しい言語を支援するには、
  その言語でのカーネルを開発することで可能になるのだが、
  この事をより実践的にするために開発陣は IPython を洗練している。

* 二番目の図式は別の言語のカーネルを実装するふたつの方法を表現している？
  ラッパー式とネイティブ式があることは理解できる。
  対象言語の実行と通信とを両方とも実装する方式は後者に相当する。

* octave_kernel や bash_kernel はラッパー式で、
  IJulia や IHaskell はネイティブ式だ。

Notebooks
----------------------------------------------------------------------
* Notebook も IPython Kernel のフロントエンドの一つであるが、
  ある特別なことをする。

* ユーザーコードを走らせることに加えて、
  Notebook 専用の書式の編集可能な文書に
  コード、出力、Markdown テキストを保存する。

* ユーザーが保存するときに、ブラウザーからサーバーに文書データが送信されて、
  ディスクに拡張子 ``.ipynb`` の JSON ファイルとして保存する。

* カーネルではなくサーバーが Notebook データの保存や読み込みを行う。
  そのため、編集したいノートの言語カーネルをユーザーが持っていなくても編集は可能である。

Exporting notebooks to other formats
----------------------------------------------------------------------
* Nbconvert についての概要。
  後述する :code:`jupyter nbconvert` の覚え書きで見ていく。

* ウェブ上の ``ipynb`` ファイルの URL を指定すると
  HTML に変換してそのままブラウザーで閲覧できる
  `nbviewer <http://nbviewer.jupyter.org/>`__ というサービスがある。

IPython.parallel
----------------------------------------------------------------------
IPython は IPython.parallel という名の平行計算フレームワークを含む。
多数の個々のエンジンを制御することができる、
上に述べた IPython Kernel の拡張版である。

Jupyter をインストールする
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

  単に :program:`ipython` を起動するのとは異なり、このサブコマンドでは
  Python のプロセスが 2 個起動する。
  後述するサブコマンドにもこのような挙動のものがある。
  なぜこのようになるかを説明できるようにしておくこと。

* コマンドラインオプション ``--existing`` はこのことと関係する？

:code:`jupyter console --kernel kernel_name`
  開始するための既定のカーネルを指定する。
  このオプションがないと ``python`` が指定されたものとして振る舞う。

* そういうわけで、Python 以外にも何かカーネルをインストールしないと面白くない。

* オプション ``--generate-config`` を与えると、
  このサブコマンド専用の設定ファイル :file:`jupyter_console_config.py` のスケルトンを
  前述のディレクトリーに生成する。

bash_kernel_ をインストールして（次の節参照）コンソールを
起動してみたところ、謎の例外が発生した。

.. code-block:: console

   $ jupyter console --kernel=bash
   Traceback (most recent call last):
     File "D:\Miniconda3\lib\runpy.py", line 184, in _run_module_as_main
       "__main__", mod_spec)
     File "D:\Miniconda3\lib\runpy.py", line 85, in _run_code
       exec(code, run_globals)
     File "D:\Miniconda3\lib\site-packages\bash_kernel\__main__.py", line 3, in <module>
       IPKernelApp.launch_instance(kernel_class=BashKernel)
     File "D:\Miniconda3\lib\site-packages\traitlets\config\application.py", line 595, in launch_instance
       app.initialize(argv)
     File "<decorator-gen-121>", line 2, in initialize
     File "D:\Miniconda3\lib\site-packages\traitlets\config\application.py", line 74, in catch_config_error
       return method(app, *args, **kwargs)
     File "D:\Miniconda3\lib\site-packages\ipykernel\kernelapp.py", line 454, in initialize
       self.init_kernel()
     File "D:\Miniconda3\lib\site-packages\ipykernel\kernelapp.py", line 365, in init_kernel
       user_ns=self.user_ns,
     File "D:\Miniconda3\lib\site-packages\traitlets\config\configurable.py", line 412, in instance
       inst = cls(*args, **kwargs)
     File "D:\Miniconda3\lib\site-packages\bash_kernel\kernel.py", line 46, in __init__
       self._start_bash()
     File "D:\Miniconda3\lib\site-packages\bash_kernel\kernel.py", line 55, in _start_bash
       self.bashwrapper = replwrap.bash()
     File "D:\Miniconda3\lib\site-packages\pexpect\replwrap.py", line 110, in bash
       child = pexpect.spawn(command, ['--rcfile', bashrc], echo=False,
   AttributeError: module 'pexpect' has no attribute 'spawn'

他所製のモジュールで困ったことになっているようだ。

サブコマンド :code:`jupyter kernelspec`
======================================================================
このサブコマンドは Jupyter のカーネルの詳細を管理するためのものだ。
Jupyter インストール直後にサブコマンド ``list`` を実行するとこのような結果を出力する。

.. code-block:: console

   $ jupyter kernelspec list
   Available kernels:
     python3    D:\Miniconda3\lib\site-packages\ipykernel\resources

* 上記ディレクトリーの中身は Python ロゴが描かれたサイズの異なる PNG ファイル 2 個だ。

なお、
bash_kernel_ を Python 環境にインストールし、
それから Jupyter 環境にインストールし、最後に本サブコマンドを実行すると
次のようになる（一部加工済）：

.. code-block:: console

   $ pip install bash_kernel
   Collecting bash_kernel
     Downloading bash_kernel-0.4.1-py2.py3-none-any.whl
   Collecting pexpect>=3.3 (from bash_kernel)
     Downloading pexpect-4.2.1-py2.py3-none-any.whl (55kB)
       100% |笆遺毎笆遺毎笆遺毎笆遺毎笆遺毎笆遺毎笆遺毎笆遺毎笆遺毎笆遺毎笆遺毎笆遺毎笆遺毎笆遺毎笆遺毎笆遺毎| 61kB 140kB/s
   Collecting ptyprocess>=0.5 (from pexpect>=3.3->bash_kernel)
     Downloading ptyprocess-0.5.1-py2.py3-none-any.whl
   Installing collected packages: ptyprocess, pexpect, bash-kernel
   Successfully installed bash-kernel-0.4.1 pexpect-4.2.1 ptyprocess-0.5.1

   $ python -m bash_kernel.install
   Installing IPython kernel spec

   $ jupyter kernelspec list
   Available kernels:
     python3    D:\Miniconda3\lib\site-packages\ipykernel\resources
     bash       $APPDATA\Roaming\jupyter\kernels\bash

サブコマンド :code:`jupyter migrate`
======================================================================
私はこれを利用する必要はないらしい。
事実、IPython から Jupyter に移行したい資源は何もなかったはずだ。

.. code-block:: console

   $ jupyter migrate
   [JupyterMigrate] Found nothing to migrate.

サブコマンド :code:`jupyter nbconvert`
======================================================================
このサブコマンドを ipynb ファイルから
HTML, LaTeX, PDF, Markdown, reStructuredText といった、
指定する形式のファイルを生成変換するツールとして利用する。

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
  このサブコマンドが動作する事前条件の一つに Pandoc_ が利用可能であることがある。
  正常に動作すれば、次のようにファイル拡張子が ``.tex`` のものが生成される：

  .. code-block:: console

     $ jupyter nbconvert --to=latex helloworld.ipynb
     [NbConvertApp] Converting notebook helloworld.ipynb to latex
     [NbConvertApp] Writing 18947 bytes to helloworld.tex

  Pandoc が利用可能でなければ次のように失敗する：

  .. code-block:: console

     $ jupyter nbconvert --to=latex helloworld.ipynb
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
  このサブコマンド専用の設定ファイル :file:`jupyter_nbconvert_console.py` のスケルトンを
  前述のディレクトリーに生成する。

端末からのコマンドライン入力だけでなく、
例えば IPython のセッションから本サブコマンドの機能をモジュールの形で
参照、利用することも可能だ。

.. code-block:: ipython

   In [1]: import nbconvert

   In [2]: nbconvert.export_latex?
   Signature: nbconvert.export_latex(nb, **kw)
   Docstring:
   Export a notebook object to latex format

   nb : :class:`~nbformat.NotebookNode`
       The notebook to export.
   config : config (optional, keyword arg)
       User configuration instance.
   resources : dict (optional, keyword arg)
       Resources used in the conversion process.

   Returns
   -------
   tuple
       output : str
           Jinja 2 output.  This is the resulting converted notebook.
       resources : dictionary
           Dictionary of resources used prior to and during the conversion
           process.
       exporter_instance : Exporter
           Instance of the Exporter class used to export the document.  Useful
           to caller because it provides a 'file_extension' property which
           specifies what extension the output should be saved as.
   File:      d:\miniconda3\lib\site-packages\nbconvert\exporters\export.py
   Type:      function

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
  このサブコマンド専用の設定ファイル :file:`jupyter_notebook_console.py` のスケルトンを
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

ダッシュボードを理解する
----------------------------------------------------------------------
ファイラーの UI になっているように見えて、事実そのとおりに振る舞う。
とは言え、最初のうちはここでは基本的に次の行動しかしないはずだ：

* ファイルを作成する
* ファイルを編集する
* ファイルを削除する
* ディレクトリーを移動する

いずれも直接的な方法で実現できるので、ここで特筆することはない。

文書の編集について
----------------------------------------------------------------------
ダッシュボードから Notebook アイコンのファイルを作成または編集をするように操作すると、
ブラウザーでその文書が開かれて編集可能となる。
少々操作方法にクセのようなものがあるので、初心者は次のことをするとよい：

* 可能ならば出来合いの ``ipynb`` 文書を開きたい。
  それを基にして UI の操作方法や文書の修正方法を習得するのが効率が良い。

* 何はともあれ、メニューから次の項目を選択して内容を確認したい：

  :menuselection:`Help --> User Interface Tour`
    画面上に小さなダイアログボックスが表示され、ちょっとした UI に関する註釈が記されている。
    矢印キーの右で次にジャンプする。吹き出しの示す位置もジャンプする。
    これを一巡すれば、ごく基本的な UI の意味は習得できることになる。

  :menuselection:`Help --> Keyboard Shortcuts`
    ショートカットキーの一覧をポップアップ表示する。
    これを見ると、このエディターには Edit モードと Command モードの概念があることが理解できる。
    ここにあるコマンドを眺めることと、エディターが REPL モデルで設計されていることを総合することで、
    Jupyter Notebook エディターの仕組みも見えてくるだろう。

テキスト部分の書式は Markdown で行い、
各種コード処理の書式は IPython の流儀で行えばよい。
これらを行うノート内の単位領域をセルと呼ぶ。
セルの種類を切り替えるには、例えばツールバーのドロップダウンリストを使えば可能だ。

* セルの左端が水色だったり黄緑色だったりするが、これはモードによって変わる。

* セルの評価方法だが、まずは :kbd:`Shift - Enter`: を押せば十分だろう。
  評価コマンドには色々な変種がある。

* セルの挿入、移動、削除は重要なので早く習得することだ。
  編集を繰り返すうちに Python セルのプロンプト番号が文書の時系列順から乱れてくるということが
  起こりがちだ。これをソートするには :guilabel:`Cell` や :guilabel:`Kernel` の
  サブメニューアイテムを上手く指示する他ない。
  出力内容をクリアしてから、再度全セルを評価するような処理ならば何でもよい。
  場合によってはカーネルの再起動まである。

文書の編集を終了する
----------------------------------------------------------------------
単にブラウザー（のタブ）を閉じればよいというわけではない。
次のどちらかの方法で編集を終える：

* 文書のメニューで :menuselection:`File --> Close and Halt` を選択する
* ダッシュボードの :guilabel:`Running` タブにある
  :guilabel:`Notebooks` の下から対象文書の :guilabel:`Shutdown` ボタンを押す

なお、必要に応じて文書の保存を行っておくことを忘れてはならない。

文書をダウンロードする
----------------------------------------------------------------------
メニュー項目 :menuselection:`File --> Download as` のいずれかを選択すると、
現在編集中の文書を指定の書式にエクスポートをしてダウンロードする。
サブメニューに現れる各書式の意味を記す。

:guilabel:`Notebook (.ipynb)`
  原稿ファイルそのものをダウンロードする。

:guilabel:`Python (.py)`
  Python コードとして変換したものをダウンロードする。
  ファイル内容のうち、
  IPython のプロンプト部分は Python のコードとしてそのまま表現され、
  それ以外のテキストはコメントアウトされた ``.py`` ファイルとしてエクスポートされる。

:guilabel:`HTML (.html)`
  今ブラウザーで見えている HTML ファイルそのものをダウンロードする。
  CSS や JavaScript などの外付けのファイルのようなものはなく、
  そういった類のテキストはすべて ``.html`` ファイルに埋め込まれている。

  * ブラウザーの提供する「名前を付けて保存...」機能により
    得られる HTML ファイルと同等のものを得ることになる。

:guilabel:`Markdown (.md)`
  Markdown 形式にエクスポートされたファイルをダウンロードする。
  ファイル内容のうち、
  Markdown 部分はそのままに、
  それ以外のテキストは適切なコードブロックに収まるようにエクスポートされる。

  * この形式のファイルを GitHub のリポジトリーに格納することで、
    他の人には読み取り専用として扱わせるのに便利と思うかもしれないが、
    実際には GitHub も ``.ipynb`` ビューワーを提供しているのでそれには及ばない。

:guilabel:`reST (.rst)`
  reStructuredText 形式にエクスポートされたファイルをダウンロードする。
  エクスポートの方針は ``.md`` のときとたいへん似ている。

  * これは本稿のように Sphinx で管理する文書のページの基にすることができそうだ。

:guilabel:`PDF via LaTeX (.pdf)`
  いったん ``.tex`` ファイルに変換してから ``.pdf`` ファイルに変換したものをダウンロードする。

  * 文書内容が前述の :code:`jupyter nbconvert --to pdf` でも成功するものである必要がある。
    さもなくば HTTP 500 エラーのレポート画面を目にすることになる。
    例えば日本語で書かれた文書を既定のテンプレートで出力しようとしていたり、
    インターネット上の URL により参照される画像を含んでいたりするものはまず失敗するだろう。

  * 某チュートリアルの ``.ipynb`` ファイルでテストしたところ、
    目次ツリー付きの素晴らしい PDF ファイルが生成された。

:guilabel:`Presentation (.html)`
  要調査。

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
  このサブコマンド専用の設定ファイル :file:`jupyter_qtconsole_config.py` のスケルトンを
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

* GitHub を検索すると実践的な ``ipynb`` ファイルが多数見つかるだろう。
  それを含むリポジトリーを clone して、ローカルで編集や書式変換の研究材料にするのもよい。

* GitHub も ``ipynb`` ビューワーを提供しているが、たまに不発する。

* Jupyter Notebook のサービス実行用と ipynb ファイルの実行用の両方がそれぞれ
  Python のプロセスを管理する。
  プアな環境だと Python プロセスによるメモリ食いが気になる。

* :program:`jupyter` の利用可能な「サブコマンド」の集合が文書化されていない？

* Pandoc は Windows ではすぐにインストールできる。
  Graphviz や Git と同じようにして環境変数 :envvar:`PATH` を参照させることで
  サブコマンドから :program:`pandoc` にアクセス可能にしておく。

* 問題になりそうなのは :code:`jupyter nbconvert` で直接 PDF ファイルを
  生成する場合だ。「原稿」に日本語文字を使うことが多いはずなので、
  既定の後処理では中間生成物の ``tex`` ファイルから PDF に変換するのに失敗する。
  単に処理がエラーコードを返す等して失敗する場合と、
  PDF ファイルは生成したものの、日本語文字がまったく印字できていない等して
  失敗する場合が考えられる。

  * この件は LaTeX についてかなり詳しくないと解決できなそうなので、保留。

  * 日本語に対応するべく LaTeX のテンプレートを自作し、
    そこで指定する文書クラスに ``pandoc`` と指定する作戦まであるようだ。
    私は結局文字が出ずに失敗したが。

* GitHub の Gist に ``ipynb`` ファイルを作成すると、
  一応 Jupyter Notebook 風のレンダリングをしてくれる。
  ただ、LaTeX コードのレンダリングがローカルでの見栄えに比べて少々異なる。

  なお、Jupyter 公式による `Jupyter Notebook Viewer <http://nbviewer.jupyter.org/>`__
  というサービスもある。こちらの見栄えは期待通りだ。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
.. _Jupyter: http://jupyter.org/
.. _Pandoc: http://pandoc.org/
.. _bash_kernel: https://github.com/takluyver/bash_kernel
