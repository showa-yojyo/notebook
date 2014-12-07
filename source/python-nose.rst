======================================================================
Nose 利用ノート
======================================================================
.. contents:: ノート目次

.. note::

   * 本稿を読む前に Python_ 本体の ``unittest`` を理解しておくべし。
   * 本稿において、利用した各パッケージのバージョンは次のとおり。

     * Python_ 2.6.6, 2.7.3, 3.4.1
     * Nose_ 1.0.0, 1.1.2, 1.3.3

   * 当ノートでは ``--verbosity`` オプションを多用しているが、
     単にノートを見返すときのわかりやすさを優先するためだけによる。
     実用時には省略することのほうが普通。

関連リンク
======================================================================
Nose_
  パッケージ配布元。

目的
======================================================================

Nose_ 自身は、その目的をドキュメントの冒頭に <nose is nicer testing for python> や <nose extends unittest to make testing easier> と謳っている。
さらに、プログラムの狙いを次の 4 点に絞っている。

  #. テストコードを書くのを簡単に。
  #. テストを走らせるのを簡単に。
  #. テスト環境の構築を簡単に。
  #. やりたいことをやることを簡単に。

そして私が Nose_ を利用する目的は何かというと、主に「走らせるのを簡単に」ではないかと思う。
Python 標準の ``unittest`` だけで単体テストをやろうとすると、TestSuite を集めて TestRunner に渡すコードを書く、
という、これまでよくやってきた作業パターンが億劫に感じられるはずだ。

インストール
======================================================================
他の Python サードパーティー製パッケージ同様に、Nose_ のインストール方法もまた複数存在する。
最近では pip 一択になってきたので、実は特に覚え書きを残すようなトピックでもないのかもしれない。

どの手順でインストールをするにせよ、インストールが成功終了後は、Python 環境は次のように変化している。

* ``Lib/site-packages/nose`` フォルダーが存在する。
  当然その中には py モジュールが含まれている。

* ``Scripts`` フォルダーに実行ファイル :file:`nosetests` が存在する。
  特に Windows の場合、これは exe ファイルである。

方法 1 -- pip 経由でインストール
----------------------------------------------------------------------
インターネットが利用できる環境ではいつも通りコンソールウィンドウで

.. code-block:: console

   $ pip nose

とタイプすればよい。

方法 2 -- setuptools を利用してソースからインストール
----------------------------------------------------------------------
まずは学校・職場・漫画喫茶等に行き、インターネットにアクセス。

自宅環境に `setuptools`_ をインストールしていなかったならば、先に入手すること。
これも持ち帰る。

目的の Nose_ のコード一式（おそらく ``nose-1.0.tar.gz`` のような名前）
を公式サイトからダウンロードして、それを USB メモリか何かに入れて持ち帰る。

解凍した後、次のようにする。

.. code-block:: console

   $ cd nose-1.0.0
   $ python setup.py install

利用方法
======================================================================
:file:`nosetests` と Nose ライブラリー本体の利用方法に分けて理解する。

:file:`nosetests`
----------------------------------------------------------------------
Nose をインストールすると、Python パッケージだけでなく、
:file:`nosetests` というスクリプトか実行ファイルが ``Scripts`` フォルダーにインストールされる。

* これは py ファイルからテストを自動的に発見し、実行することができる便利なツールだ。

* 引数なしで起動すると、おそらくカレントディレクトリーにあるすべての py ファイルから、
  すべてのテストを発見し、片っ端から実行するというはたらきをするのではないだろうか。

* 普通は :file:`nosetests` にコマンドライン引数を指定して利用する。
  次のコマンドライン例は Nose のドキュメントから引用したものだ。
  モジュール名を指定したり、さらにテスト名を指定したり、
  あるいはモジュールフルパスプラステスト名という指定の仕方がサポートされているようだ。

  .. code-block:: console

     $ nosetests test.module
     $ nosetests another.test:TestCase.test_method
     $ nosetests a.test:TestCase
     $ nosetests /path/to/test/file.py:test_function

* ディレクトリーごと指示するやり方もある。その場合、複数パス指定が許される。

  .. code-block:: console

     $ nosetests /path/to/tests /another/path/to/tests

  なので、実は ``-w``, ``--where`` オプションは無用の長物。

* :file:`nosetests` は豊富なコマンドラインオプションを提供している。
* コマンドラインオプションと同等の設定を設定ファイルからも行える。

  * デフォルトの設定ファイルは ``$HOME`` にある :file:`.noserc` または :file:`nose.cfg` だ。
  * 任意の設定ファイルパスをコマンドラインから
    ``--config`` オプションを利用することで指定できる。
  * 設定ファイルの書き方で注意が要るのは、設定項目を
    ``[nosetests]`` セクションに書かねばならないことだ。

    .. code-block:: ini

       [nosetests]
       verbosity=2
       with-doctest=true
       ...

* テスト結果の出力書式は、標準の ``unittest`` のそれと基本的には同一。

次に、使えそうなオプションを調べてみよう。

collect-only オプション -- テスト名だけを調べる
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``--collect-only`` オプションでテストを実行せずにテスト名だけを確認できる。

* さらに ``--with-id`` を併用し、テストのインデックスリストも得られる。
* ``--verbosity`` オプションを併用して、テスト名等を明示させるのがコツ。

.. code-block:: console

   $ nosetests --collect-only --with-id --verbosity=2
   #1 testeven.test_evens(0, 0) ... ok
   testeven.test_evens(1, 3) ... ok
   testeven.test_evens(2, 6) ... ok
   ---- 省略 ----
   #2 test_choice (testrandom.TestSequenceFunctions) ... ok
   #3 test_sample (testrandom.TestSequenceFunctions) ... ok
   #4 test_shuffle (testrandom.TestSequenceFunctions) ... ok
   #5 test_default_size (testwidget.WidgetTestCase) ... ok
   #6 test_resize (testwidget.WidgetTestCase) ... ok

   ----------------------------------------------------------------------
   Ran 10 tests in 0.070s

   OK

attr オプション -- 属性を指定することで起動するテストを選択する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
テストケースをいっぱい書いたはいいが、
「今はこのテストだけをやりたいンだ」
「このテストは通常はやりたくないンだ」
という状況に陥りがち。
そんなときには ``--attr``, ``--eval-attr``
オプションの仕組みをうまくテストコードに組み込む。

.. literalinclude:: ../sample/nose/testattr2.py
   :language: python3

.. code-block:: console

   $ nosetests -a '!online' tests.py
   $ nosetests -A "speed != slow" tests.py

* 上のコマンドラインの実行では ``test_download_hardcore_images`` は実行されない。
* 下のコマンドラインの実行では ``test_load_all_images`` は実行されない。

pdb-failures オプション -- テスト失敗時にデバッガーを起動
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``--pdb-failures`` オプションを指定しておくと、テストが FAILURE になった地点で
Python の pdb デバッガが起動する。

* 通常使いたいのは ``--pdb`` ではなく ``--pdb-faillures`` のほうだと思う。
* pdb はコンソールベースのデバッガ。正直なところ不慣れなツールだが、この際慣れておく。

.. code-block:: console

   $ nosetests --pdb-failures
   .> d:\home\yojyo\note\sample\nose\testeven.py(6)check_even()
   -> assert n % 2 == 0 or nn % 2 == 0
   (Pdb) l
     1     def test_evens():
     2         for i in range(0, 5):
     3             yield check_even, i, i*3
     4
     5     def check_even(n, nn):
     6  ->     assert n % 2 == 0 or nn % 2 == 0
   [EOF]
   (Pdb) p n, n % 2, nn % 2
   (1, 1, 1)
   (Pdb)

with-coverage オプション -- コードカバレッジ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``--with-coverage`` オプションで、
テスト結果と共にコードカバレッジを測定できる。
いつものテスト結果を出力した直後に、カバレッジを出力する。

チューニングの材料になるわけで、いずれ大掛かりなライブラリーを開発するつもりならば、
この機能は覚えていて損はない。

この機能を利用するには、別途 coverage_ という別のパッケージが必要だ。
インストールは難しくないので、Nose 環境の一部とみなして導入しておくとよさそうだ。

.. code-block:: console

   $ nosetests --with-coverage -v testrandom.py
   test_choice (testrandom.TestSequenceFunctions) ... ok
   test_sample (testrandom.TestSequenceFunctions) ... ok
   test_shuffle (testrandom.TestSequenceFunctions) ... ok

   Name         Stmts   Miss  Cover   Missing
   ------------------------------------------
   ... この行にファイルパスの情報が入るが省略 ...
   testrandom      21      3    86%   25, 30-31
   ----------------------------------------------------------------------
   Ran 3 tests in 0.010s

   OK

with-profile オプション -- プロファイリング
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. note::

   筆者環境では Nose 1.3.3 でこの機能が利用できなくなっている。

``--with-profile`` オプションで、
テストに関係した全関数に対する呼び出しの回数や時間の統計を取れる。
いつものテスト結果を出力した直後に、プロファイル結果を出力する。

.. code-block:: console

            4101 function calls (4084 primitive calls) in 0.201 CPU seconds

      Ordered by: cumulative time

      ncalls  tottime  percall  cumtime  percall filename:lineno(function)
         7/1    0.000    0.000    0.201    0.201 d:\python26\lib\site-packages\nose\suite.py:175(__call__)
         7/1    0.002    0.000    0.201    0.201 d:\python26\lib\site-packages\nose\suite.py:196(run)
           1    0.000    0.000    0.200    0.200 d:\python26\lib\unittest.py:463(__call__)
           1    0.000    0.000    0.200    0.200 d:\python26\lib\site-packages\nose\suite.py:70(run)
          25    0.000    0.000    0.121    0.005 d:\python26\lib\site-packages\nose\suite.py:92(_get_tests)
   ...

* ``--profile-sort=SORT`` オプションで、ソート順を何にするかを指定できる。
  オプション自体を指定しない場合は ``cumulative`` がデフォルト扱いとなる。

  なお ``SORT`` に指定する値は Python Standard Library の ``Stats.sort_stats``
  の引数と同じ。

オプションメモ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ``-h`` または ``--help`` でヘルプ表示。
* ``-V`` または ``--version`` で :file:`nosetests` のバージョンを表示。
* ``-v`` または ``--verbosity`` で表示を少々やかましくできる。
  テスト名確認時にはこれを併用するだろう。

* ``-m REGEX`` 系オプションで「テストとみなしたいファイル・ディレクトリー・関数・クラス名にマッチする」
  正規表現を指定できる。

  デフォルトで ``(?:^|[\b_\.\-])[Tt]est`` になっていることを押させておけばよい。

* ``-p`` または ``--plugins`` オプションで、有効なプラグインの一覧を表示。
  ただし出力順が何で決まるのかわからないので、
  適当に ``grep`` や ``sort`` にパイプして見やすくするべし。

ライブラリー
----------------------------------------------------------------------

テストの書き方
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* テストは ``unittest.TestCase`` のサブクラスの形で用意しなくてもよい。
* ただし ``unittest.TestCase`` のサブクラスからはテストを無条件にロードする。
* テスト関数はモジュールの先頭から出現順に走らせる。
* ``TestCase`` サブクラスまたはその他のテストクラスは、
  名前のアルファベット順に走らせる。

* Fixture について

  * どうやら setup/teardown ペアのことを test fixture と呼ぶらしい。
  * Nose はパッケージレベル、モジュールレベル、クラスレベル、関数レベルで
    fixture をサポートしている。

    言い換えれば、これらの各レベルでテストの概念がある。

* テストパッケージ

  * Nose はテストをパッケージの形に編成することを認めている。
  * パッケージレベルでの setup/teardown の概念が存在する。
    それらはいずれも ``__init__.py`` で関数の形で用意しておくと、
    Nose がそれを適切なタイミングで拾ってくれる。

    * setup 関数の名前は次のいずれかとなる：
      ``setup``, ``setup_package``, ``setUp``, ``setUpPackage``

    * teardown 関数の名前は次のいずれかとなる：
      ``teardown``, ``teardown_package``, ``tearDown``, ``tearDownPackage``

* テストモジュール

  * モジュール名がテストっぽいものはテストモジュールである。
  * モジュールレベルでの setup/teardown の概念が存在する。
    それ用の関数名も上述のパッケージのそれから類推できる名前になっている。
  * モジュールのテストが起動するタイミングは、Nose がすべてのテストを集めた後になる。

* テストクラス

  * テストモジュール内に定義されている、次のいずれかの条件を満たすクラスである：

    * ``unittest.TestCase`` のサブクラスすべて - (A)
    * Nose の ``testMatch`` にマッチする名前を持つクラスすべて - (B)

  * (B) タイプのクラスでも ``setUp`` と ``tearDown`` を定義することができ、
    Nose はそれらを (A) タイプのそれのように呼び出すことになる。

  * (B) タイプは (A) タイプよりも以下の点で優遇される：

    * ジェネレーターメソッドを持つことができる。
    * クラスレベルの setup/teardown を定義することができる。
      いずれもクラスメソッドである必要がある。

      * ``setup_class``, ``setupClass``, ``setUpClass``, ``setupAll``, ``setUpAll``
      * ``teardown_class``, ``teardownClass``, ``tearDownClass``, ``teardownAll``, ``tearDownAll``

* テスト関数

  * テストモジュール内に定義されている、
    Nose の ``testMatch`` にマッチする名前を持つ関数がテスト関数となる。

  * 関数にも setup/teardown を適用することができる。
    自分で定義した関数をデコレーター ``with_setup`` を利用して「くっつける」。
    これがたいへん便利だ。

* そして Nose を利用するとジェネレーターをもテストできる。
  自分ではよく使わないので今のところはパス。

nose.tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. note::

   ちょっと利用方法が理解できないものがあるため、後回し。

テストの発見および起動法則
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
さっきも書いたが、それ以外について。

* Nose はテストに見えないディレクトリーかつパッケージでないものは検査しない。

* Nose はモジュールを import する際に、そのモジュールがあるディレクトリーパスを
  ``sys.path`` 変数に追加してしまう。モジュールが何かパッケージのものである場合、
  ``package.module`` として import されることになる。

* もしあるオブジェクトが属性 ``__test__`` を有し、かつそれが ``True``
  と評価しないようなものならば、そのオブジェクトはテストとして集められないし、
  さらにそのオブジェクトを含むどんなオブジェクトも集められない。

プラグイン
----------------------------------------------------------------------
Nose のバージョンが上がってから勉強しに行こう。

雑多なメモ
======================================================================
* Further Reading より：

  * Jason Pellerin という人物が作者のようだ。
    2005 年からコピーライトが発生している。

  * Nose という名前はどうして付いたのか。
    作者は discover の同義語を類語辞書で調べたようで、
    短くてマヌケな名前で、なおかつ spy の意味を含まぬものを採用したらしい。

    nose は動詞だとクンカクンカするとかいう意味なのでは。

  * Nose は `py.test`_ というテスティングフレームワークにインスパイヤされて作ったとある。
    以前の py.test はインストールが難しく、
    unittest ベースでなかったとのこと。

  * Nose のライセンスは LGPL とかいうものらしい。
    バージョン 2 以降ならば、利用者が好きなライセンスを選択してよいとか。

* nosetests の変な使い方。

  * 他人様の作ったパッケージのテスト構成を探るのに最適なツールかもしれない。
    例えば Jinja2_ の ``testsuite`` フォルダーの各ファイルからテストを
    全部抽出してリストを作成できたりする。

    .. code-block:: console

       $ cd site-packages/jinja2/
       $ python34 -c 'import jinja2; print(jinja2.__version__)'
       2.7.3
       $ nosetests --collect-only --with-id -v testsuite/*.py
       #1 Failure: TypeError (find_all_tests() missing 1 required positional argument: 'suite') ... ok
       #2 test_autoescape_autoselect (jinja2.testsuite.api.ExtendedAPITestCase) ... ok
       #3 test_cycler (jinja2.testsuite.api.ExtendedAPITestCase) ... ok
       #4 test_expressions (jinja2.testsuite.api.ExtendedAPITestCase) ... ok
       #5 test_finalizer (jinja2.testsuite.api.ExtendedAPITestCase) ... ok
       ... 省略 ...
       #311 test_markup_leaks (jinja2.testsuite.utils.MarkupLeakTestCase) ... ok

       ----------------------------------------------------------------------
       Ran 311 tests in 0.139s

       OK

  * Matplotlib_ の ``tests`` フォルダーはテストパッケージの構成になっている。
    :file:`nosetests` の実験場としては面白い。

  * NumPy_ は Nose をうまく使いこなしているようだ。
    ``import numpy; help(numpy.test)`` してみよう。
    テストの単位をわかりやすく分類する努力を払っているのがわかる。

    例えば線形代数サブパッケージだけテストしたいのならば、
    Python インタープリターから次のようにタイプしてみるだけでよい。

    .. code-block:: pycon

       >>> import numpy
       >>> numpy.linalg.test(verbose=2)
       Running unit tests for numpy.linalg
       NumPy version 1.8.2
       NumPy is installed in D:\Python34\lib\site-packages\numpy
       Python version 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:45:13) [MSC v.1600 64 bit (AMD64)]
       nose version 1.3.3
       test_lapack (test_build.TestF77Mismatch) ... SKIP: Skipping test: test_lapack: Skipping fortran compiler mismatch on non Linux platform
       Check mode='full' FutureWarning. ... ok
       test_linalg.TestBoolPower.test_square ... ok
       test_linalg.TestCond2.test_sq_cases ... ok
       test_linalg.TestCondInf.test ... ok
       test_linalg.TestCondSVD.test_sq_cases ... ok
       ... 省略 ...
       Ticket 627. ... ok
       test_svd_no_uv (test_regression.TestRegression) ... ok

       ----------------------------------------------------------------------
       Ran 118 tests in 42.034s

       OK (SKIP=2)
       <nose.result.TextTestResult run=118 errors=0 failures=0>

* 未調査項目

  * プラグイン周りを調べていない。
  * ログ設定周りを調べていない。
  * Windows 環境ゆえ、マルチプロセステストが試せないのは残念。

.. _Python: http://www.python.org/
.. _Nose: http://somethingaboutorange.com/mrl/projects/nose/
.. _easy_install: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _setuptools: http://peak.telecommunity.com/DevCenter/setuptools
.. _coverage: http://nedbatchelder.com/code/coverage
.. _py.test: http://codespeak.net/py/current/doc/test.html
.. _Jinja2: http://jinja.pocoo.org/
.. _Matplotlib: http://matplotlib.sourceforge.net/
.. _NumPy: http://scipy.org/NumPy
