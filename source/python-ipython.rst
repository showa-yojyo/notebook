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

インストール
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
* 例えば Ctrl + A で「キャレットがコマンドライン行の先頭に移動する」等の Emacs 風のキーバインドがなされている。
  これが一番ありがたい変化。この機能があるというだけで私には通常の Python 対話モードから IPython に乗り換える動機になる。

よい変化なので、PyReadline のインストールの状態を保ったまま先に進もう。

テスト
======================================================================
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
TBW

その他
======================================================================
* YouTube で ``IPython`` で検索すると、面白い？ビデオが大量に見つかる。
  ``IPython Windows`` 等もよい。

.. include:: /_include/scipy-refs.txt
.. _PyReadLine: http://ipython.org/pyreadline.html
