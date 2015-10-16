======================================================================
インストール
======================================================================
SymPy_ をインストールする前に、オンラインシェルでまずはその機能を試した。
可能性を感じたので、自分の Python_ 環境に SymPy をインストールした。
その過程をここで述べる。

.. contents:: ノート目次

下見する
======================================================================
ブラウザーさえあれば SymPy を自分の Python 環境にインストールすることなく触ってみることが可能だ。
SymPy をインストールするかどうか迷っている場合は、
これらの機能で間に合うかどうかを判断してから決めるのがよさそうだ。

次の手順で SymPy を試すことができる。

#. プロジェクトサイトの右上リンク `Online Shell <http://live.sympy.org/>`_ 先のページを開く。
#. Python インタラクティブシェルで適宜コマンドを入力する。

特製シェルの操作方法はページの右側の柱に記述がある。
これはオンラインドキュメントからも随時表示させることができる。

* Enter キーを単に押すだけでは入力した式が実行されない。
  UI の Evaluate ボタンをクリックすると初めて評価される。

* 画鋲ボタンはセッションの再現をするための URL を生成する優れ物。

* オンラインシェルの Python のバージョンは 2.7.5 なので、
  私の 3.4 環境で動作する SymPy はサポートされているのだろうかという疑問がわく。
  後で試してみたら問題はなかった。

パッケージをインストールする
======================================================================
SymPy のドキュメントによると、ソースからのインストールが推奨手段だそうだ。
そしてそのソースの入手方法は次のいずれかになる。

#. ダウンロードページで配布しているソースの圧縮ファイルを解凍して、
   コマンドラインから ``python setup.py install`` する。

#. Git でレポジトリーをローカルに複製して、以下同文。

私の場合は Git があるのでこちらのやり方のほうが容易だ。
次のようにコマンドラインを入力したところ、うまくインストールできた。

.. code-block:: console

   $ cd ~/devel
   $ git clone git://github.com/sympy/sympy.git
   Cloning into 'sympy'...
   $ cd sympy
   $ git pull origin master
   From git://github.com/sympy/sympy
   * branch            master     -> FETCH_HEAD
   Current branch master is up to date.
   $ pip install -e .
   Obtaining file:///D:/home/yojyo/devel/sympy
     Running setup.py (path:D:/home/yojyo/devel/sympy\setup.py) egg_info for package from file:///D:/home/yojyo/devel/sympy

       no previously-included directories found matching 'doc\_build'
       warning: no files found matching 'TODO'
   Downloading/unpacking mpmath>=0.19 (from sympy==0.7.7.dev)
     Running setup.py (path:D:\Temp\pip_build_work\mpmath\setup.py) egg_info for package mpmath

   Installing collected packages: mpmath, sympy
     Running setup.py install for mpmath

     Running setup.py develop for sympy

       no previously-included directories found matching 'doc\_build'
       warning: no files found matching 'TODO'
       Creating d:\python34\lib\site-packages\sympy.egg-link (link to .)
       Adding sympy 0.7.7.dev to easy-install.pth file
       Installing isympy script to D:\Python34\Scripts

       Installed d:\home\yojyo\devel\sympy
   Successfully installed mpmath sympy
   Cleaning up...

* 公式ドキュメントには ``setupegg.py install`` せよとあるが、私のところでは動かなかった。
  代わりに上記のように pip_ を用いた。

* 依存パッケージに ``mpmath`` というのが見える。
  任意精度浮動小数点演算のための Python パッケージのようだ。

バージョンを確認する
======================================================================
単にバージョンを確認するには、例えば次のようにする。

.. code-block:: console

   $ python -c 'import sympy; print(sympy.__version__)'
   0.7.7.dev

もしくは pip を利用する。こちらの方法のほうが潰しが効くので憶えておくとよいだろう。

.. code-block:: console

   $ pip show sympy
   ---
   Metadata-Version: 1.1
   Name: sympy
   Version: 0.7.7.dev0
   Summary: Computer algebra system (CAS) in Python
   Home-page: http://sympy.org
   Author: SymPy development team
   Author-email: sympy@googlegroups.com
   License: BSD
   Location: d:\home\yojyo\devel\sympy
   Requires: mpmath

単体テストを実施する
======================================================================
せっかくソースごとインストールしたので、開発用のものと思われる単体テストを行う。
私の環境で実施したところ、次のようなレポートが延々と出力されていた。

.. code-block:: console

   $ python -c 'import sympy; sympy.doctest()'
   ============================= test process starts ==============================
   executable:         D:\Python34\python.exe  (3.4.1-final-0) [CPython]
   architecture:       64-bit
   cache:              yes
   ground types:       python
   hash randomization: on (PYTHONHASHSEED=2926718148)

   sympy\assumptions\ask.py[2] ..                                              [OK]
   sympy\assumptions\assume.py[5] .....                                        [OK]
   sympy\assumptions\refine.py[6] ......                                       [OK]
   sympy\assumptions\handlers\calculus.py[2] ..                                [OK]
   -- 略 --
   ===== tests finished: 2926 passed, 1 failed, 6 skipped, in 982.39 seconds ======
   DO *NOT* COMMIT!
   ============================== rst doctests start ==============================
   -- 中断 --

* コンソールに羅列されていく数学用語を見ると、
  身に余る物をインストールしてしまったという気分を感じられる。
* 微分方程式のソルバーのテストに時間がかかるようだ。
* ``rst doctest start`` 以降は時間がなかったので Ctrl + C で中止した。
* ``[OK]`` がほとんどのようだから、全く動作しないということはなさそうに思える。

``isympy`` を実行する
======================================================================
コマンドラインから :file:`bin/isympy` を起動すると、そのまま Python の対話モードが始まる。
IPython_ が利用可能な環境では、IPython のそれが始まる。

* 私の場合は Cygwin のコマンドラインから直接スクリプトを走らせるよりは、
  Windows の「ファイル名を指定して実行」から :file:`python.exe` 経由で
  :file:`isympy` を走らせるとキーバインド等の具合がよい。
  私の場合は下記コマンドラインのようにする。

  .. code-block:: text

     D:\Python35\python.exe "D:\home\yojyo\devel\sympy\bin\isympy" --pretty=no -- --profile=sympy

  私の都合で SymPy 利用時に限り IPython の設定ファイルによる設定を上書きしたいので、
  コマンドライン引数の最後にそれを指定する。
  こう書いておくと、IPython は設定ファイル :file:`$HOME/.ipython/profile_sympy/ipython_config.py` を採用する。
  次の行を編集してある。

  .. code-block:: python3

     c.InteractiveShellApp.pylab_import_all = False

  これの意味を簡単に述べると、
  いつもなら便利な ``from numpy import *`` 等の自動インポートを避けるということだ。
  いかにも NumPy と SymPy で何らかの名前衝突を起こしそうなことは想像に難くない。

  * 関連ノートとして :doc:`/python-ipython` の環境設定の節を参照。
  * 後になって SymPy どころか、``all`` や ``sum`` 等の組み込みの関数の名前をも隠すことが発覚した。

* ConEmu の Predefined Tasks にこのコマンドラインを含めておく。
  :doc:`/python-upgrade` も参照。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
