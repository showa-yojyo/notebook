======================================================================
IPython 利用ノート
======================================================================
本稿は IPython_ に関する個人的な覚え書きである。NumPy_, SciPy_, Matplotlib_ のドキュメントを読んでいるとこのツールの名前が頻繁に出てくる。
無視するのはもったいない気がするので調査する。

.. contents:: ノート目次

.. note::

   * OS は Windows 7 Home Premium SP 1 を使用している。
   * 本稿において、利用した各パッケージのバージョンは次のとおり。

     * Python_ 3.4.1
     * IPython_ 3.0.0
     * PyReadline_ 2.0
     * Nose_ 1.3.4

IPython とは何か
======================================================================
ドキュメントによると <IPython is meant to work as a drop-in replacement
for the standard interactive interpreter> だそうだ。Python コンソールの上位機種のような扱いでよい。

インストールから初回起動まで
======================================================================
次の条件を初回条件と呼ぶことにする。

* Python がインストール済みである。
* pip の実行ファイルのあるフォルダーに PATH が通っている。
  私の場合は ``D:/Python34/Scripts`` である。

これを満たす環境において、IPython をインストールする方法を記す。

pip によるインストール
----------------------------------------------------------------------
IPython をインストールするもっとも単純な方法は、おそらく pip によるものだろう。
コンソールウィンドウで次のようにタイプすればよい。速やかに終了するはずだ。

.. code-block:: console

   $ pip ipython
   Downloading/unpacking ipython
   Installing collected packages: ipython
   Successfully installed ipython
   Cleaning up...

ドキュメントによるとオプショナルな依存パッケージがいくつかあるようだ。
場合により別途利用者がインストールすることになる。

初回起動
----------------------------------------------------------------------
``D:\Python34\Scripts\ipython3.exe`` を起動するだけでよい。
Windows の「ファイル名を指定して実行」で同実行ファイルを指定すると、コンソールウィンドウが出現する。

私の環境でのスタートアップ時の出力を記す。

.. code-block:: text

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
  ``pyreadline`` なるパッケージをインストールしよう。

PyReadline をインストール
----------------------------------------------------------------------
名前からして Python 版 readline と思われるパッケージを pip でインストールして、再度 IPython を起動したい。

.. code-block:: console

   $ pip install pyreadline
   Downloading/unpacking pyreadline
     Running setup.py (path:D:\cygwin64\tmp\pip_build_work\pyreadline\setup.py) egg_info for package pyreadline

       package init file 'pyreadline\configuration\__init__.py' not found (or not a regular file)
   Installing collected packages: pyreadline
     Running setup.py install for pyreadline
       package init file 'pyreadline\configuration\__init__.py' not found (or not a regular file)

   Successfully installed pyreadline
   Cleaning up...

インストール後 ``ipython`` を起動すると次の変化が見られた。

* WARNING メッセージが表示されなくなった。
* ``In [1]:``, ``Out [1]:`` 等のプロンプト文字列に色がついた。
* 例えば Ctrl + A （以下 Emacs 風に表記する。これは C-a と表記することになる）で
  「キャレットがコマンドライン行の先頭に移動する」等の Emacs 風のキーバインドがなされている。
  これが一番ありがたい変化。この機能があるというだけで私には通常の Python 対話モードから IPython に乗り換える動機になる。

よい変化なので、PyReadline のインストールの状態を保ったまま先に進もう。

テスト
----------------------------------------------------------------------
ここで IPython の動作確認テストを行いたい。
公式ドキュメントに従い、初回条件で ``iptest`` を実行すると以下のようになった。

.. code-block:: console

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

環境設定
======================================================================
IPython の挙動を次の各項目により制御できるはずなので、本章ではそれらを調べていこう。

* 環境変数
* 設定ファイル
* コマンドライン引数

環境変数による設定
----------------------------------------------------------------------
IPython 固有の環境変数としては :envvar:`IPYTHON_DIR` ただひとつしかない？
これはユーザー設定データ、履歴、拡張モジュールを格納するディレクトリーのパスを表現する環境変数だろう。
デフォルトでは ``~/.ipython`` であり、通常の利用状況ではこの値をわざわざ変更することはなさそうだ。

結論としては、環境変数のことは意識しない。

設定ファイルによる設定
----------------------------------------------------------------------
ドキュメントによると、IPython のセッティングを指定する方法の基本として
:file:`~/.ipython/profile_default` ディレクトリー以下の py ファイルでプログラムを書くことがあるようだ。

.. code-block:: console

   $ ipython3 profile create
   [ProfileCreate] Generating default config file: 'D:/home/yojyo/.ipython/profile_default/ipython_config.py'

これでテンプレファイル :file:`ipython_config.py` ができあがった。
テキストエディターでこれを開き、有効にしたい箇所のコメントアウトを解除するとよさそうだ。

.. code-block:: python3

   c.InteractiveShellApp.pylab = 'auto'
   c.InteractiveShellApp.pylab_import_all = True
   c.TerminalIPythonApp.pylab = 'auto'
   c.TerminalIPythonApp.pylab_import_all = True

これぐらいやっておくと、NumPy や Matplotlib の構成要素のインポートを自動的に行なってくれる。
例えば ``import numpy as np`` しなくても ``np.arange(10)`` のようなコードが通じる。
さらに、モジュール名を書かずに ``arange(10)`` と書いても通じる。

このトピックは深く掘り下げて理解を深めるのがよいように思える。

コマンドライン引数による設定
----------------------------------------------------------------------
* IPython のすべての設定可能な値はコマンドラインパラメーターから構成できる。

  * 通常は次の形式で指定する： ``ipython --ClassName.attribute=value``
  * ただし頻繁に用いられるオプションは短い別名形式が用意してある。
    例えば ``ipython --matplotlib`` など。

    * そのようなオプションの一覧は ``ipython help`` の Options のセクションで確認できる。

* コマンドラインで指定したオプションは、設定ファイルのそれを上書きする。

今のところ、特に毎回指定したくなるコマンドライン引数はなさそうだ。

使い勝手を試す
======================================================================
IPython コンソールウィンドウでの各種機能をひと通り試していこう。

* 単に ``?`` を入力することで IPython に関するちょっとしたドキュメントが出力する。10 ページ弱で終了する。
* ``%quickref`` で *Quick Reference Card* なるドキュメントが出力する。こちらはページ数が多め。
* 引数なしの ``help()`` で対話的ヘルプモードになる。

  * 通常の ``help(X)`` では、普通の Python コンソール同様の機能 X に関するヘルプが出力することを確認した。

* ``X?`` で IPython スタイルの機能 X に関するヘルプが出力することを確認した。

  * ``X??`` で詳細な情報が出力されるとのことだが、あまり変わらない？

* タイプが面倒に感じたら、即タブキーを押す。残り文字列が補間されて便利。

  * 補間されるのは識別子、Python キーワード。なんとファイルパスも補間対象。

* ``%pdoc X`` で機能 X の docstring が出力することを確認した。
* ``%pfile X`` でモジュール X のテキスト的な内容が出力することを確認した。
* ``%timeit`` と ``%%timeit`` を試した。
* ``%lsmagic`` で利用可能なマジックの一覧と ``automagic`` スイッチの ON/OFF 状況が出力することを確認した。
* ``%history`` でコマンド入力の履歴が出力することを確認した。
* ``!X`` でシステムシェルコマンド X を実行できることを確認した。

マジック機能のメモがたくさんできるがしょうがない。
`Built-in magic commands <http://ipython.org/ipython-doc/stable/interactive/magics.html>`_
を眺めて使えそうなものを試そう。

* ``%who``, ``%whos`` で自分が定義した識別子のリストを出力できる。後者は利用回数も確認できてたいへん便利。

.. todo::

   以下を調査する。

   * タブキー補間。Emacs の dabbrev-expand 程度のものを期待したいが、できるか？
   * デフォルトでは ``%history`` の履歴リストが長い。Bash でいうところの $HISTSIZE 的なものがあるか調べる。
   * Windows だと ``!`` コマンドが使えてもあまりうれしくない。Cygwin のコマンドを使いたいので設定可能か調べる。単に
     ``/bin`` に PATH を通すだけかもしれない。

* 履歴機能操作は readline に強く依存することに留意するべし。

  * C-r で Bash でいうところの reverse-i-search 機能が使える。すなわち、過去のコマンド入力をインクリメンタルサーチする。
  * C-p, C-n, 上矢印または下矢印キーで入力履歴を一個ずつ移動できる。

* 例えば ``%hist -g print`` のようにすると履歴の grep が行える。
* TBW: 自動インデントの空白文字数調整
* ログ機能について。

  * ``%logstart`` でセッションログを保存できる。コンソールでの入出力を適宜テキストファイルに保存するものだ。

* TBW: ``%alias``
* Input caching system: IPython が記憶しているユーザーのコンソールでの入力を再利用できる。

  * ``_i`` で 1 つ前の入力を得られる。
  * ``_ii`` で 2 つ前の入力を得られる。
  * ``_iii`` で 3 つ前の入力を得られる。
  * リスト ``In``, ``_ih`` でプロンプト番号を添字にして入力を得られる。
  * 実は ``_i5`` やら ``_i100`` やらからも（もし存在すれば）入力を得られる。

* Output caching system: 上記の機能の出力バージョン。

  * ``_`` で 1 つ前の出力を得られる。通常の Python コンソールと同じ。
  * ``__`` で 2 つ前の出力を得られる。
  * ``___`` で 3 つ前の出力を得られる。
  * 辞書 ``Out``, ``_oh`` でプロンプト番号をキーにして出力を得られる。

* ディレクトリー移動履歴も管理している。

  * リスト ``_dh`` に作業ディレクトリーをユーザーが訪問した順に保存する。
  * コマンド ``%cd X`` を実行すれば、作業ディレクトリーを X に移動する。
  * コマンド ``%dhist`` を実行すれば、作業ディレクトリーを訪問順に一覧できる。

その他
======================================================================
* YouTube で ``IPython`` で検索すると、面白いビデオが大量に見つかる。
  ``IPython Windows`` 等もよい。

* ConEmu ユーザーならば、当然 IPython3 をタブ化できるようにしておくのが筋だろう。

.. include:: /_include/scipy-refs.txt
.. _PyReadLine: http://ipython.org/pyreadline.html
