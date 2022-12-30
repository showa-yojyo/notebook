======================================================================
Nose 利用ノート
======================================================================

.. contents:: ノート目次

.. note::

   * 本稿を読む前に Python_ 本体の ``unittest`` を理解しておくべし。
   * 本稿において、利用した各パッケージのバージョンは次のとおり。

     * Python_ 2.6.6, 2.7.3, 3.4.1, 3.5.0, 3.5.2
     * Nose_ 1.0.0, 1.1.2, 1.3.3, 1.3.7

   * 当ノートでは ``--verbosity`` オプションを多用しているが、
     単にノートを見返すときのわかりやすさを優先するためだけによる。
     実用時には省略することのほうが普通。

関連リンク
======================================================================

Nose_
  パッケージ配布元。

目的
======================================================================

Nose_ 自身は、その目的をドキュメントの冒頭に <nose is nicer testing for python>
や <nose extends unittest to make testing easier> と謳っている。さらに、プログラ
ムの狙いを次の 4 点に絞っている。

  #. テストコードを書くのを簡単に。
  #. テストを走らせるのを簡単に。
  #. テスト環境の構築を簡単に。
  #. やりたいことをやることを簡単に。

そして私が Nose_ を利用する目的は何かというと、主に「走らせるのを簡単に」ではな
いかと思う。 Python 標準の ``unittest`` だけで単体テストをやろうとすると、
TestSuite を集めて TestRunner に渡すコードを書くという、これまでよくやってきた作
業パターンが億劫に感じられるはずだ。

インストール
======================================================================

方法については :ref:`python-pkg-proc` で図示したので、そちらを参照して欲しい。イ
ンストールが成功終了後は、Python 環境は次のように変化している。

* :file:`Lib/site-packages/nose` フォルダーが存在する。
  当然その中には py モジュールが含まれている。

* :file:`Scripts` フォルダーに実行ファイル :file:`nosetests` が存在する。特に
  Windows の場合、これは exe ファイルである。

利用方法
======================================================================

:program:`nosetests` と Nose ライブラリー本体の利用方法に分けて理解する。

:program:`nosetests`
----------------------------------------------------------------------

Nose をインストールすると、Python パッケージだけでなく、:program:`nosetests` と
いうスクリプトか実行ファイルが :file:`Scripts` フォルダーにインストールされ
る。

* これは py ファイルからテストを自動的に発見し、実行することができる便利なツール
  だ。
* 引数なしで起動すると、おそらくカレントディレクトリーにあるすべての py ファイル
  から、すべてのテストを発見し、片っ端から実行するというはたらきをするのではない
  だろうか。
* 普通は :program:`nosetests` にコマンドライン引数を指定して利用する。次のコマン
  ドライン例は Nose のドキュメントから引用したものだ。モジュール名を指定したり、
  さらにテスト名を指定したり、あるいはモジュールフルパスプラステスト名という指定
  の仕方がサポートされているようだ。

  .. code:: console

     bash$ nosetests test.module
     bash$ nosetests another.test:TestCase.test_method
     bash$ nosetests a.test:TestCase
     bash$ nosetests /path/to/test/file.py:test_function

* ディレクトリーごと指示するやり方もある。その場合、複数パス指定が許される。

  .. code:: console

     bash$ nosetests /path/to/tests /another/path/to/tests

  なので、実は ``-w``, ``--where`` オプションは無用の長物。

* :program:`nosetests` は豊富なコマンドラインオプションを提供している。
* コマンドラインオプションと同等の設定を設定ファイルからも行える。

  * デフォルトの設定ファイルは ``$HOME`` にある :file:`.noserc` または
    :file:`nose.cfg` だ。
  * 任意の設定ファイルパスをコマンドラインから ``--config`` オプションを利用する
    ことで指定できる。
  * 設定ファイルの書き方で注意が要るのは、設定項目を ``[nosetests]`` セクション
    に書かねばならないことだ。

    .. code:: ini

       [nosetests]
       verbosity=2
       with-doctest=true

* テスト結果の出力書式は、標準の ``unittest`` のそれと基本的には同一。

次に、使えそうなオプションを調べてみよう。

``collect-only`` オプション -- テスト名だけを調べる
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``--collect-only`` オプションでテストを実行せずにテスト名だけを確認できる。

* さらに ``--with-id`` を併用し、テストのインデックスリストも得られる。
* ``--verbosity`` オプションを併用して、テスト名等を明示させるのがコツ。

.. code:: console

   bash$ nosetests --collect-only --with-id --verbosity=2
   #1 A regular test case ... ok
   #2 A very slow test case ... ok
   #3 A test with attribute ... ok
   #4 A test with attribute specific value ... ok
   #5 testattr.test_tags ... ok
   #6 testattr2.test_load_all_images ... ok
   #7 testattr2.test_download_hardcore_images ... ok
   #8 testeven.test_evens(0, 0) ... ok
   #8 testeven.test_evens(1, 3) ... ok
      testeven.test_evens(2, 6) ... ok
      testeven.test_evens(3, 9) ... ok
      testeven.test_evens(4, 12) ... ok
   #9 test_choice (testrandom.TestSequenceFunctions) ... ok
   #10 test_sample (testrandom.TestSequenceFunctions) ... ok
   #11 test_shuffle (testrandom.TestSequenceFunctions) ... ok
   #12 test_default_size (testwidget.WidgetTestCase) ... ok
   #13 test_resize (testwidget.WidgetTestCase) ... ok

   ----------------------------------------------------------------------
   Ran 17 tests in 0.101s

   OK

``attr`` オプション -- 属性を指定することで起動するテストを選択する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

テストケースをいっぱい書いたはいいが、「今はこのテストだけをやりたいンだ」「この
テストは通常はやりたくないンだ」という状況に陥りがち。そんなときには ``--attr``,
``--eval-attr`` オプションの仕組みをうまくテストコードに組み込む。

.. literalinclude:: /_sample/nose/testattr2.py
   :language: python3

.. code:: console

   bash$ nosetests -a '!online' testattr2.py
   bash$ nosetests -A "speed != slow" testattr2.py

* 上のコマンドラインの実行では ``test_download_hardcore_images`` は実行されない。
* 下のコマンドラインの実行では ``test_load_all_images`` は実行されない。

``pdb-failures`` オプション -- テスト失敗時にデバッガーを起動
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``--pdb-failures`` オプションを指定しておくと、テストが FAILURE になった地点で
Python の :program:`pdb` デバッガが起動する。

* 通常使いたいのは ``--pdb`` ではなく ``--pdb-faillures`` のほうだと思う。
* :program:`pdb` はコンソールベースのデバッガ。正直なところ不慣れなツールだが、
  この際慣れておく。

.. code:: console

   bash$ nosetests --pdb-failures testeven.py
   .> d:\home\yojyo\devel\all-note\notebook\source\_sample\nose\testeven.py(13)check_even()
   -> assert val1 % 2 == 0 or val2 % 2 == 0
   (Pdb) l
     8         for i in range(0, 5):
     9             yield check_even, i, i * 3
    10
    11     def check_even(val1, val2):
    12         """Determine if either of numbers is even."""
    13  ->     assert val1 % 2 == 0 or val2 % 2 == 0
   [EOF]
   (Pdb) p val1, val1 % 2, val2 % 2
   (1, 1, 1)
   (Pdb)

エラーの発生とは関係なく、特定の箇所でステップ実行を有効にする方法もある。まずは
ステップ実行したいコードを含むモジュールで
:code:`from nose.tools import set_trace` をする。それから対象コードの直前で
:code:`set_trace()` すればよい。

``with-coverage`` オプション -- コードカバレッジ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``--with-coverage`` オプションでテスト結果と共にコードカバレッジを測定できる。い
つものテスト結果を出力した直後に、カバレッジを出力する。

チューニングの材料になるわけで、いずれ大掛かりなライブラリーを開発するつもりなら
ば、この機能は覚えていて損はない。

この機能を利用するには、別途 coverage_ という別のパッケージが必要だ。インストー
ルは難しくないので、Nose 環境の一部とみなして導入しておくとよさそうだ。

.. code:: console

   bash$ nosetests --with-coverage -v testrandom.py
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

``with-profile`` オプション -- プロファイリング
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   筆者環境では Nose 1.3.3 でこの機能が利用できなくなっている。

``--with-profile`` オプションでテストに関係した全関数に対する呼び出しの回数や時
間の統計を取れる。いつものテスト結果を出力した直後に、プロファイル結果を出力す
る。

.. code:: console

            4101 function calls (4084 primitive calls) in 0.201 CPU seconds

      Ordered by: cumulative time

      ncalls  tottime  percall  cumtime  percall filename:lineno(function)
         7/1    0.000    0.000    0.201    0.201 d:\python26\lib\site-packages\nose\suite.py:175(__call__)
         7/1    0.002    0.000    0.201    0.201 d:\python26\lib\site-packages\nose\suite.py:196(run)
           1    0.000    0.000    0.200    0.200 d:\python26\lib\unittest.py:463(__call__)
           1    0.000    0.000    0.200    0.200 d:\python26\lib\site-packages\nose\suite.py:70(run)
          25    0.000    0.000    0.121    0.005 d:\python26\lib\site-packages\nose\suite.py:92(_get_tests)
   ...

* ``--profile-sort=SORT`` オプションで、ソート順を何にするかを指定できる。オプ
  ション自体を指定しない場合は ``cumulative`` がデフォルト扱いとなる。

  なお ``SORT`` に指定する値は Python Standard Library の ``Stats.sort_stats``
  の引数と同じ。

オプションメモ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``-h`` または ``--help`` でヘルプ表示。
* ``-V`` または ``--version`` で :file:`nosetests` のバージョンを表示。
* ``-v`` または ``--verbosity`` で表示を少々やかましくできる。テスト名確認時には
  これを併用するだろう。
* ``-m REGEX`` 系オプションで「テストとみなしたいファイル・ディレクトリー・関
  数・クラス名にマッチする」正規表現を指定できる。

  デフォルトで :regexp:`(?:^|[\\b_\\.\\-])[Tt]est` になっていることを押させてお
  けばよい。

* ``-p`` または ``--plugins`` オプションで、有効なプラグインの一覧を表示。ただし
  出力順が何で決まるのかわからないので、適当に :program:`grep` や
  :program:`sort` にパイプして見やすくするべし。

ライブラリー
----------------------------------------------------------------------

テストの書き方
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* テストは ``unittest.TestCase`` のサブクラスの形で用意しなくてもよい。
* ただし ``unittest.TestCase`` のサブクラスからはテストを無条件にロードする。
* テスト関数はモジュールの先頭から出現順に走らせる。
* ``TestCase`` サブクラスまたはその他のテストクラスは、名前のアルファベット順に
  走らせる。

* Fixture について

  * どうやら setup/teardown ペアのことを test fixture と呼ぶらしい。
  * Nose はパッケージレベル、モジュールレベル、クラスレベル、関数レベルで
    fixture をサポートしている。言い換えれば、これらの各レベルでテストの概念があ
    る。

* テストパッケージ

  * Nose はテストをパッケージの形に編成することを認めている。
  * パッケージレベルでの setup/teardown の概念が存在する。それらはいずれも
    :file:`__init__.py` で関数の形で用意しておくと、 Nose がそれを適切なタイミン
    グで拾ってくれる。

    * setup 関数の名前は次のいずれかとなる：
      ``setup``, ``setup_package``, ``setUp``, ``setUpPackage``

    * teardown 関数の名前は次のいずれかとなる：
      ``teardown``, ``teardown_package``, ``tearDown``, ``tearDownPackage``

* テストモジュール

  * モジュール名がテストっぽいものはテストモジュールである。
  * モジュールレベルでの setup/teardown の概念が存在する。それ用の関数名も上述の
    パッケージのそれから類推できる名前になっている。
  * モジュールのテストが起動するタイミングは、Nose がすべてのテストを集めた後に
    なる。

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
      * ``teardown_class``, ``teardownClass``, ``tearDownClass``,
        ``teardownAll``, ``tearDownAll``

* テスト関数

  * テストモジュール内に定義されている、Nose の ``testMatch`` にマッチする名前
    を持つ関数がテスト関数となる。
  * 関数にも setup/teardown を適用することができる。自分で定義した関数をデコレー
    ター ``with_setup`` を利用して取り付ける。これがたいへん便利だ。

* そして Nose を利用するとジェネレーターをもテストできる。自分ではよく使わないの
  で今のところはパス。

nose.tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   ちょっと利用方法が理解できないものがあるため、後回し。

テストの発見および起動法則
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

さっきも書いたが、それ以外について。

* Nose はテストに見えないディレクトリーかつパッケージでないものは検査しない。
* Nose はモジュールを import する際に、そのモジュールがあるディレクトリーパスを
  ``sys.path`` 変数に追加してしまう。モジュールが何かパッケージのものである場
  合、``package.module`` として import されることになる。
* もしあるオブジェクトが属性 ``__test__`` を有し、かつそれが ``True`` と評価しな
  いようなものならば、そのオブジェクトはテストとして集められないし、さらにそのオ
  ブジェクトを含むどんなオブジェクトも集められない。

プラグイン
----------------------------------------------------------------------

Nose のバージョンが上がってから勉強しに行こう。

雑多なメモ
======================================================================

* Further Reading より：

  * Jason Pellerin という人物が作者のようだ。2005 年からコピーライトが発生してい
    る。
  * Nose という名前はどうして付いたのか。作者は discover の同義語を類語辞書で調
    べたようで、短くてマヌケな名前で、なおかつ spy の意味を含まぬものを採用した
    らしい。

    nose は動詞だとクンカクンカするとかいう意味なのでは。

  * Nose は `py.test`_ というテスティングフレームワークにインスパイヤされて作っ
    たとある。以前の py.test はインストールが難しく、unittest ベースでなかった
    とのこと。
  * Nose のライセンスは LGPL とかいうものらしい。バージョン 2 以降ならば、利用者
    が好きなライセンスを選択してよいとか。

* nosetests の変な使い方。

  * 他人様の作ったパッケージのテスト構成を探るのに最適なツールかもしれない。例え
    ば Jinja2_ の ``testsuite`` フォルダーの各ファイルからテストを全部抽出してリ
    ストを作成できたりする。

    .. code:: console

       bash$ cd site-packages/jinja2/
       bash$ python34 -c 'import jinja2; print(jinja2.__version__)'
       2.7.3
       bash$ nosetests --collect-only --with-id -v testsuite/*.py
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

    .. warning::

       最近の Jinja2 のインストールには ``testsuite`` フォルダーがない。

  * Matplotlib_ の :file:`tests` フォルダーはテストパッケージの構成になっている。
    :program:`nosetests` の実験場としては面白い。

  * NumPy_ は Nose をうまく使いこなしているようだ。
    ``import numpy; help(numpy.test)`` してみよう。テストの単位をわかりやすく分
    類する努力を払っているのがわかる。

    例えば線形代数サブパッケージだけテストしたいのならば、Python インタープリ
    ターから次のようにタイプしてみるだけでよい。

    .. code:: pycon

       >>> import numpy as np
       >>> np.linalg.test(verbose=2)
       Running unit tests for numpy.linalg
       NumPy version 1.11.1
       NumPy relaxed strides checking option: False
       NumPy is installed in D:\Miniconda3\lib\site-packages\numpy
       Python version 3.5.2 |Continuum Analytics, Inc.| (default, Jul  5 2016, 11:41:13) [MSC v.1900 64 bit (AMD64)]
       nose version 1.3.7
       test_lapack (test_build.TestF77Mismatch) ... SKIP: Skipping test: test_lapack: Skipping fortran compiler mismatch on non Linux platform
       Check mode='full' FutureWarning. ... ok
       test_linalg.TestBoolPower.test_square ... ok
       test_linalg.TestCond2.test_sq_cases ... ok
       test_linalg.TestCond2.test_stacked_arrays_explicitly ... ok
       test_linalg.TestCondInf.test ... ok
       test_linalg.TestCondSVD.test_sq_cases ... ok
       test_linalg.TestCondSVD.test_stacked_arrays_explicitly ... ok
       test_linalg.TestDet.test_sq_cases ... ok
       ... more results ...
       test_svd_build (test_regression.TestRegression) ... ok
       test_svd_no_uv (test_regression.TestRegression) ... ok

       ----------------------------------------------------------------------
       Ran 134 tests in 17.999s

       OK (SKIP=2)
       <nose.result.TextTestResult run=134 errors=0 failures=0>

* 未調査項目

  * プラグイン周りを調べていない。
  * ログ設定周りを調べていない。
  * Windows 環境ゆえ、マルチプロセステストが試せないのは残念。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
.. _coverage: http://nedbatchelder.com/code/coverage
.. _py.test: http://codespeak.net/py/current/doc/test.html
.. _Jinja2: http://jinja.pocoo.org/
