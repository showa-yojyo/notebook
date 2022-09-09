======================================================================
IPython 利用ノート
======================================================================
本稿は IPython_ に関する個人的な覚え書きである。
NumPy_, SciPy_, Matplotlib_ のドキュメントを読んでいるとこのツールの名前が頻繁に出てくる。
無視するのはもったいない気がするので調査する。

.. contents:: ノート目次

.. note::

   * OS

     * Windows 7 Home Premium x64 SP1
     * Windows 10 Home x64

   * 本稿において、利用した各パッケージのバージョンは次のとおり。

     * Python_ 3.4.1, 3.5.0, 3.5.2, 3.6.6
     * IPython_ 3.0.0, 4.0.0, 5.0.0, 6.4.0
     * PyReadline_ 2.0, 2.1, n/a
     * Nose_ 1.3.4, 1.3.7
     * PyQt_ v5.3.1 for Python v3.4 (x64), n/a for Python v3.5 (x64), 4.11.4
     * PyZMQ_ 14.5.0, 14.7.0, TODO

.. note::

   本稿では文字列 ``%PYTHONDIR%`` を :file:`python.exe` が存在するディレクトリーのパスを意味する
   環境変数のようなものを表現するものであることにする。
   例えば、正規の Python 3.5 インストーラーを用いて D ドライブ直下にインストールした環境では
   この値は :file:`D:\\Python35` であり、
   Miniconda の 3.5 インストーラーを用いて D ドライブ直下にインストールした環境では
   この値は :file:`D:\\Miniconda3` である。

IPython とは何か
======================================================================
ドキュメントによると <IPython is meant to work as a drop-in replacement
for the standard interactive interpreter> だそうだ。
標準の Python インタープリターの上位版のようなモノだ。

インストールから初回起動まで
======================================================================
次の条件を初回条件と呼ぶことにする。

* Python がインストール済みである。
* :program:`conda` または :program:`pip` の実行ファイルのあるフォルダーに PATH が通っている。

これを満たす環境において、
:ref:`python-pkg-proc` に示したようにすると IPython をインストールできる。

次に :program:`conda` によるインストール手続きの例を示す。

.. code:: console

   $ conda install ipython
   Fetching package metadata: ....
   Solving package specifications: .........

   Package plan for installation in environment D:\Miniconda3:

   The following packages will be downloaded:

       package                    |            build
       ---------------------------|-----------------
       vs2015_runtime-14.0.25123  |                0         1.9 MB
       colorama-0.3.7             |           py35_0          19 KB
       conda-env-2.5.2            |           py35_0          67 KB
       decorator-4.0.10           |           py35_0          12 KB
       ipython_genutils-0.1.0     |           py35_0          33 KB
       menuinst-1.4.1             |           py35_0         107 KB
       path.py-8.2.1              |           py35_0          47 KB
       pycosat-0.6.1              |           py35_1          80 KB
       pygments-2.1.3             |           py35_0         1.3 MB
       pyyaml-3.11                |           py35_4         169 KB
       requests-2.10.0            |           py35_0         656 KB
       ruamel_yaml-0.11.14        |           py35_0         217 KB
       setuptools-23.0.0          |           py35_0         692 KB
       simplegeneric-0.8.1        |           py35_1           7 KB
       six-1.10.0                 |           py35_0           8 KB
       wcwidth-0.1.7              |           py35_0          21 KB
       win_unicode_console-0.5    |           py35_0          27 KB
       conda-4.1.11               |           py35_0         247 KB
       pickleshare-0.7.3          |           py35_0           8 KB
       pip-8.1.2                  |           py35_0         1.6 MB
       prompt_toolkit-1.0.3       |           py35_0         308 KB
       traitlets-4.2.2            |           py35_0         113 KB
       ipython-5.0.0              |           py35_0         1.0 MB
       ------------------------------------------------------------
                                              Total:         8.6 MB

   The following NEW packages will be INSTALLED:

       colorama:            0.3.7-py35_0
       conda:               4.1.11-py35_0
       conda-env:           2.5.2-py35_0
       decorator:           4.0.10-py35_0
       ipython:             5.0.0-py35_0
       ipython_genutils:    0.1.0-py35_0
       menuinst:            1.4.1-py35_0
       path.py:             8.2.1-py35_0
       pickleshare:         0.7.3-py35_0
       pip:                 8.1.2-py35_0
       prompt_toolkit:      1.0.3-py35_0
       pycosat:             0.6.1-py35_1
       pygments:            2.1.3-py35_0
       pyyaml:              3.11-py35_4
       requests:            2.10.0-py35_0
       ruamel_yaml:         0.11.14-py35_0
       setuptools:          23.0.0-py35_0
       simplegeneric:       0.8.1-py35_1
       six:                 1.10.0-py35_0
       traitlets:           4.2.2-py35_0
       vs2015_runtime:      14.0.25123-0
       wcwidth:             0.1.7-py35_0
       wheel:               0.29.0-py35_0
       win_unicode_console: 0.5-py35_0

   Proceed ([y]/n)?

初回起動
----------------------------------------------------------------------
:file:`%PYTHONDIR%\\Scripts\\ipython3.exe` を起動するだけでよい。
Windows の「ファイル名を指定して実行」で同実行ファイルを指定すると、
コンソールウィンドウが出現する。

私の環境でのスタートアップ時の出力を記す。

.. code:: ipython

   WARNING: Readline services not available or not loaded.
   WARNING: Proper color support under MS Windows requires the pyreadline library.
   You can find it at:
   http://ipython.org/pyreadline.html

   Defaulting color scheme to 'NoColor'
   Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:45:13) [MSC v.1600 64 bit (AMD64)]
   Type "copyright", "credits" or "license" for more information.

   IPython 3.0.0 -- An enhanced Interactive Python.
   ?         -> Introduction and overview of IPython's features.
   %quickref -> Quick reference.
   help      -> Python's own help system.
   object?   -> Details about 'object', use 'object??' for extra details.

   In [1]:

* WARNING のメッセージが気になるので、ここから攻める。指示に従い
  pyreadline なるパッケージをインストールしよう。

PyReadline をインストール
----------------------------------------------------------------------

.. note::

   このパッケージは IPython 5.0.0 では依存関係がなくなっているようだ。

名前からして Python 版 readline と思われるパッケージを :program:`pip` でインストールして、
再度 IPython を起動したい。

.. code:: console

   $ pip install pyreadline
   Downloading/unpacking pyreadline
     Running setup.py (path:D:\cygwin64\tmp\pip_build_work\pyreadline\setup.py) egg_info for package pyreadline

       package init file 'pyreadline\configuration\__init__.py' not found (or not a regular file)
   Installing collected packages: pyreadline
     Running setup.py install for pyreadline
       package init file 'pyreadline\configuration\__init__.py' not found (or not a regular file)

   Successfully installed pyreadline
   Cleaning up...

インストール後 :program:`ipython` を起動すると次の変化が見られた。

* WARNING メッセージが表示されなくなった。
* ``In [1]:``, ``Out [1]:`` 等のプロンプト文字列に色がついた。
* 例えば :kbd:`Ctrl + A` （以下 Emacs 風に表記する。これは :kbd:`C-a` と表記することになる）で
  「キャレットがコマンドライン行の先頭に移動する」等の Emacs 風のキーバインドがなされている。
  これが一番ありがたい変化。
  この機能があるというだけで私には通常の Python 対話モードから IPython に乗り換える動機になる。

よい変化なので、PyReadline のインストールの状態を保ったまま先に進もう。

テスト
----------------------------------------------------------------------
ここで IPython の動作確認テストを行いたい。

IPython 3.0.0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
公式ドキュメントに従い、初回条件で :program:`iptest` を実行すると以下のようになった。

.. code:: console

   $ iptest3
   Traceback (most recent call last):
     File "D:\Python34\lib\runpy.py", line 170, in _run_module_as_main
       "__main__", mod_spec)
     File "D:\Python34\lib\runpy.py", line 85, in _run_code
       exec(code, run_globals)
     File "D:\Python34\Scripts\iptest3.exe\__main__.py", line 5, in <module>
     File "D:\Python34\lib\site-packages\IPython\testing\iptestcontroller.py", line 20, in <module>
       import requests
   ImportError: No module named 'requests'

* モジュール ``requests`` を別途インストールする必要がありそうだ。

  * インストールしたが、今度は ``ImportError: you need to have pywin32 installed for this to work``
    なるエラーが。

結論としては、これは面倒そうなので諦めた。

IPython 4.0.0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
一連の自動テストが実行された。エラーがボロボロと現れる。

.. code:: console

   $ iptest3

   Test group: core
   ............................
   省略
   ______________________________________________________________________
   Test suite completed for system with the following information:
   IPython version: 4.0.0
   IPython commit : f534027 (installation)
   IPython package: d:\python35\lib\site-packages\IPython
   Python version : 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)]
   sys.executable : d:\python35\python.exe
   Platform       : Windows-10.0.10240

   Tools and libraries available at test time:
      matplotlib pygments sqlite3

   Status: ERROR - 1 out of 7 test groups failed (core). Took 125.286s.

   You may wish to rerun these, with:
     iptest core

IPython 5.0.0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Conda で IPython をインストールしたところ、:file:`Scripts` に :program:`iptest3` がないようだ。
開発版では当然存在する。

環境設定
======================================================================
IPython の挙動を次の各項目により制御できるはずなので、本章ではそれらを調べていこう。

* 環境変数
* 設定ファイル
* コマンドライン引数

環境変数による設定
----------------------------------------------------------------------
IPython 固有の環境変数としては :envvar:`IPYTHON_DIR` ただひとつしかない？
これはユーザー設定データ、履歴、拡張モジュールを格納するディレクトリーのパスを
表現する環境変数だろう。
デフォルトでは :file:`~/.ipython` であり、
通常の利用状況ではこの値をわざわざ変更することはなさそうだ。

結論としては、環境変数のことは意識しない。

設定ファイルによる設定
----------------------------------------------------------------------
ドキュメントによると、IPython のセッティングを指定する方法の基本として
:file:`~/.ipython/profile_default` ディレクトリー以下の py ファイルで
プログラムを書くことがあるようだ。

.. code:: console

   $ ipython3 profile create
   [ProfileCreate] Generating default config file: 'D:/home/yojyo/.ipython/profile_default/ipython_config.py'

これでテンプレファイル :file:`ipython_config.py` ができあがった。
テキストエディターでこれを開き、有効にしたい箇所のコメントアウトを解除するとよさそうだ。

.. code:: python3

   c.InteractiveShellApp.pylab = 'auto'

これぐらいやっておくと、NumPy や Matplotlib の構成要素のインポートを自動的に行なってくれる。
例えば :code:`import numpy as np` しなくても :code:`np.arange(10)` のようなコードが通じる。
さらに、下記の項目を有効にすると :code:`np.` すら不要になる。

.. code:: python3

   c.InteractiveShellApp.pylab_import_all = True

一見タイプの手間が省けて便利なようだが、たまにこれらのパッケージの識別子の名前と
Python 組み込みのオブジェクトの識別子がカブるようなもの
(e.g. :code:`all`, :code:`any`, etc.) があると事態が少々複雑になる。
個人的には全インポートは無効にしておき、
NumPy や Matplotlib のモジュールとしてのインポートだけに留めておきたい。

敢えて NumPy と Matplotlib の自動インポートを抑制した状況でセッションを開きたい場合は
名前付きプロファイルを生成して、設定ファイルの対応項目を False にする。
そして、IPython 起動時に ``--profile`` コマンドラインオプションで設定名を指示する。

.. code:: console

   $ ipython3 profile create sympy
   $ edit ~/.ipython/profile_sympy/ipython_config.py
   $ ipython3 --profile=sympy

コマンドライン引数による設定
----------------------------------------------------------------------
* IPython のすべての設定可能な値はコマンドラインパラメーターから構成できる。

  * 通常は次の形式で指定する： :code:`ipython --ClassName.attribute=value`
  * ただし頻繁に用いられるオプションは短い別名形式が用意してある。
    例えば :code:`ipython --matplotlib` など。

    * そのようなオプションの一覧は :code:`ipython help` の
      Options のセクションで確認できる。

* コマンドラインで指定したオプションは、設定ファイルのそれを上書きする。

今のところ、特に毎回指定したくなるコマンドライン引数はなさそうだ。

使い勝手を試す
======================================================================
IPython コンソールウィンドウでの各種機能をひと通り試していこう。

* 単に ``?`` を入力することで IPython に関するちょっとしたドキュメントが出力する。
  10 ページ弱で終了する。

* :code:`%quickref` で *Quick Reference Card* なるドキュメントが出力する。
  こちらはページ数が多め。

* 引数なしの :code:`help()` で対話的ヘルプモードになる。

  * 通常の :code:`help(X)` では、普通の Python コンソール同様の機能 X に関する
    ヘルプが出力することを確認した。

* :code:`X?` で IPython スタイルの機能 X に関するヘルプが出力することを確認した。

  * :code:`X??` で詳細な情報が出力されるとのことだが、あまり変わらない？

* タイプが面倒に感じたら、即タブキーを押す。残り文字列が補完されて便利。

  * 補完されるのは識別子、Python キーワード。なんとファイルパスも補完対象。

* :code:`%pdoc X` で機能 X の docstring が出力することを確認した。
* :code:`%pfile X` でモジュール X のテキスト的な内容が出力することを確認した。
* :code:`%timeit` と :code:`%%timeit` を試した。
* :code:`%lsmagic` で利用可能なマジックの一覧と
  :code:`%automagic` スイッチの ON/OFF 状況が出力することを確認した。
* :code:`%history` でコマンド入力の履歴が出力することを確認した。

  * 詳しくは後述する。

* :code:`!X` でシステムシェルコマンド X を実行できることを確認した。

マジック機能のメモがたくさんできるがしょうがない。
`Built-in magic commands <http://ipython.org/ipython-doc/stable/interactive/magics.html>`__
を眺めて使えそうなものを試そう。

* :code:`%who`, :code:`%whos` で自分が定義した識別子のリストを出力できる。
  後者は利用回数も確認できてたいへん便利。

* 履歴機能操作は readline に強く依存することに留意するべし。

  * :kbd:`C-r` で Bash でいうところの reverse-i-search 機能が使える。
    すなわち、過去のコマンド入力をインクリメンタルサーチする。
  * :kbd:`C-p`, :kbd:`C-n`, 上矢印または下矢印キーで入力履歴を一個ずつ移動できる。

* 履歴リストについて。

  * オプション :code:`-n` を常に指定して、履歴番号を表示するようにしたい。
    この番号情報を基に :code:`%recall` することになるはずだから。

  * 例えば :code:`%history -g print` のようにすると履歴の :program:`grep` が行える。
    オプション :code:`-g` を指定するときには、
    同じコマンド入力が重複して出力されないように、
    オプション :code:`-u` も併せて指定することも許される。

  * オプション :code:`-l` で直近の数コマンドだけを表示できる。

  * オプション :code:`-o` と :code:`-p` を同時に指定すると、
    履歴の表示が doctest の書式で出力される。
    このテキストをこのノートにそのまま貼り付けて、
    サンプルコードのメモ作業を楽にすることもできる。

* TBW: 自動インデントの空白文字数調整
* ログ機能について。

  * :code:`%logstart` でセッションログを保存できる。
    コンソールでの入出力を適宜テキストファイルに保存するものだ。

* TBW: :code:`%alias`
* Input caching system: IPython が記憶しているユーザーのコンソールでの入力を再利用できる。

  * :code:`_i` で 1 つ前の入力を得られる。
  * :code:`_ii` で 2 つ前の入力を得られる。
  * :code:`_iii` で 3 つ前の入力を得られる。
  * リスト :code:`In`, :code:`_ih` でプロンプト番号を添字にして入力を得られる。
  * 実は :code:`_i5` やら :code:`_i100` やらからも（もし存在すれば）入力を得られる。

* Output caching system: 上記の機能の出力バージョン。

  * :code:`_` で 1 つ前の出力を得られる。通常の Python コンソールと同じ。
  * :code:`__` で 2 つ前の出力を得られる。
  * :code:`___` で 3 つ前の出力を得られる。
  * 辞書 :code:`Out`, :code:`_oh` でプロンプト番号をキーにして出力を得られる。

* ディレクトリー移動履歴も管理している。

  * リスト :code:`_dh` に作業ディレクトリーをユーザーが訪問した順に保存する。
  * コマンド :code:`%cd X` を実行すれば、作業ディレクトリーを X に移動する。
  * コマンド :code:`%dhist` を実行すれば、作業ディレクトリーを訪問順に一覧できる。

* スクリプトを IPython のセッションから起動できる。
  次のコード片は自作のスクリプトを :code:`%run` コマンドにより起動した様子を再現したものだ。

  .. code:: ipython

     In [1]: %run ~/bin/listmanager.py remove showa_yojyo bot zzz
     0-15: Wait...
     0-15: OK:
     zzz

  * スクリプトのファイル名の拡張子は省略可能のようだ。

  * オプション :code:`-t` で実行時間を測定する。
    コマンドラインでいうところの ``time python commands`` のようなものだ。
    例を示す。

    .. code:: ipython

       In [1]: %run -t ./bin/mjscore.py -F --today
       集計期間           2016/09/01 00:40 - 2016/09/01 02:13
       ...

       IPython CPU timings (estimated):
         User   :       1.20 s.
         System :       0.00 s.
       Wall time:       1.19 s.

  * オプション :code:`-d` で対象を pdb の支配下で実行する。
    ブレイクポイント等のデバッガーオプションも同時に指定できる。

  * オプション :code:`-p [profile options]` でプロファイルをとれる。
    というより、コマンド :code:`%prun` のラッパーだと思われる。

  * オプション :code:`-m module_name` で指定モジュールをスクリプトとして実行する。
    コマンドラインでいうところの ``python -m module`` の
    Python コード限定版という感じだ。

* :code:`%prun`, :code:`%%prun` はプロファイラー付きでコードを実行する。
  コマンドラインで ``python -m cProfile [options] file`` を実行するのに近い。

* 複数行に亘る関数の定義のコーディングは IPython ウィンドウ内で行うよりも、
  常用しているテキストエディターで行えるほうが効率的だ。
  コマンド :code:`%edit` はそれを実現する。このコマンドを実行すると、
  デフォルトでは :program:`notepad` が開く。ここでコードを書いて保存して閉じる。
  すると IPython のセッションにその内容が伝わる。
  エディターで定義した関数を呼び出すことができる。

  .. code:: ipython

     In [2]: %edit
     IPython will make a temporary file named: D:\Temp\ipython_edit_3cn_y47j\ipython_edit_osmxydqq.py
     Editing... done. Executing edited code...
     Out[2]: 'def need_to_be_in_love():\n\tpass\n'

     In [3]: need_to_be_in_love()

     In [4]:

  :program:`notepad` では逆にテキスト編集の効率が落ちるはずなので、オプション
  ``TerminalInteractiveShell.editor`` で馴染みのテキストエディターを指定する。

  .. code:: python3

     # Set the editor used by IPython (default to $EDITOR/vi/notepad).
     c.TerminalInteractiveShell.editor = 'D:/Program Files/xyzzy/xyzzy.exe'

* クリップボードの内容を Python のコードとして評価することができる。

  * キーボードで :kbd:`C-S-v` を押すと、
    クリップボードに保存されている Python コードを即時評価する。

  * コマンド :code:`%paste` を実行すると、
    いったんクリップボードの内容を画面にエコーしてから、コード内容を評価する。

  * 代わりにコマンド :code:`%cpaste` を実行すると、
    まずはクリップボードに保存されている Python コードの編集モードになる。
    次にユーザーが :code:`--` という行を入力すると編集終了となり、
    そこに書かれたコードが最終的に評価される。

* 作業内容のリセット機能がある。

  * コマンド :code:`%reset` でセッションの各種状態
    （ユーザー定義のオブジェクト、入力履歴、出力履歴、ディレクトリー移動履歴）
    をクリアすることができる。

    * 異色なのは :code:`%reset array` だろう。
      NumPy の配列オブジェクトをすべて削除するというものだ。

  * コマンド :code:`%reset_selective` を用いれば、
    クリアしたいユーザー定義のオブジェクトを正規表現で指定できる。

.. todo::

   * Windows だと :code:`!` コマンドが使えてもあまりうれしくない。
     Cygwin のコマンドを使いたいので設定可能か調べる。単に
     ``/bin`` に :envvar:`PATH` を通すだけかもしれない。
   * Output caching system の :code:`_<n>` の有効な *n* を知りたい場合は？

Qt コンソールを試す
======================================================================
.. warning::

   本節の記述は現時点では公式に deprecated 扱いされている。
   Jupyter とやらを利用するようにとのことだ。

PyQt_ と PyZMQ_ が利用可能であれば、IPython を PyQt ウィンドウで再現できる。
私の環境では PyQt はインストールが済んでいるものの、PyZMQ が入っていなかった。
本節では PyZMQ のインストール作業から記す。

PyZMQ をインストールする
----------------------------------------------------------------------
PyZMQ_ が何であるのかを理解するのは後回しにして、まずはインストールだ。
IPython のドキュメントにあるように、素直に :program:`pip` でインストールできる。

.. code:: console

   $ pip install pyzmq
   Downloading/unpacking pyzmq
   Installing collected packages: pyzmq
   Successfully installed pyzmq
   Cleaning up...
   $ pip list | grep -i pyzmq
   pyzmq (14.5.0)

Qt コンソールを起動する（シンプル）
----------------------------------------------------------------------
Windows の「ファイル名を指定して実行」で次のように指定する。

.. code:: text

   %PYTHONDIR%\Scripts\ipython3.exe qtconsole

一旦真っ黒なウィンドウが表示され、次に Qt ウィンドウが表示される。
後者がコンソールとなる。
通常の IPython のように使えるだけでなく、
よく見ると便利なコマンドを起動するメニューがウィンドウ上部に備えられている。

Qt コンソールを起動する（プロットインライン）
----------------------------------------------------------------------
Matplotlib のプロット図をインラインに Qt コンソール内に描画させる。
この機能が Qt コンソールの目玉であると思われる。
まずは IPython を次のようなコマンドライン引数を指定して起動する。ドキュメントには
:code:`qtconsole --matplotlib inline` と指定すると記されているが、私の環境ではダメだった。

.. code:: text

   %PYTHONDIR%\Scripts\ipython3.exe qtconsole --pylab=inline

試しに Matplotlib を内部的に利用した NetworkX のメソッドを経由して描画してみよう。

.. figure:: /_images/ipython-qtconsole-inline.png
   :align: center
   :alt: IPython Qt Console
   :width: 614px
   :height: 602px
   :scale: 50%

インラインでグラフを描画できて何がうれしいのかと言うと、
このコンソールウィンドウを保存できるからだ。
ファイルメニューの Save を選択すると、
コンソールでの入出力を HTML と画像とに分けてファイルとして保存できる。

その他
======================================================================
* YouTube で ``IPython`` で検索すると、面白いビデオが大量に見つかる。
  ``IPython Windows`` 等もよい。

* ConEmu ユーザーならば、当然 IPython をタブ化できるようにしておくのが筋だろう。
  ところで Qt コンソールウィンドウはタブ化できないのだろうか。
  「元ウィンドウ」はタブ化できる。

* このノートをだいたい書き終わったあとに気づいたが、オライリーの
  `Python によるデータ分析入門 <http://www.oreilly.co.jp/books/9784873116556/>`__ という本が
  IPython を紹介するのに一章分紙幅を割いている。たいへんまとまっていて便利だ。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
.. _PyReadLine: http://ipython.org/pyreadline.html
.. _PyZMQ: http://zeromq.github.io/pyzmq/
.. _PyQt: http://www.riverbankcomputing.co.uk/software/pyqt/
