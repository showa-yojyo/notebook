======================================================================
Python Nose 利用ノート
======================================================================

.. note::

   * 本稿を読む前に Python 本体の ``unittest`` を理解しておくべし。
   * このノートをとるに当たって利用した Nose_ のバージョンは 0.11.4 だ。

.. contents:: ノート目次

目的
======================================================================

* Nose_ 自身の目的は、ドキュメントの冒頭に <nose is nicer
  testing for python> や <nose extends unittest to make testing easier>
  と謳われており、さらに次の 4 点に狙いを絞っている。

  #. テストコードを書くのを簡単に。
  #. テストを走らせるのを簡単に。
  #. テスト環境の構築を簡単に。
  #. やりたいことをやることを簡単に。

* そして私が Nose を利用する目的も上のどれかに相当するはずなのだが、
  やはり「走らせるのを簡単に」が主目的だ。
  標準の ``unittest`` だけでやろうとすると、
  TestSuite を集めて TestRunner に渡すコードを書くのが面倒。

インストール
======================================================================
普通のインストール方法はいつものように複数ある。

インストールが終わると、Python 環境は次のように変化しているはず。

* ``Lib/site-packages/nose`` フォルダーが存在する。
  当然その中には py モジュールが含まれている。

* ``Scripts`` フォルダーに実行ファイル ``nosetests`` が存在する。
  特に Windows の場合、これは exe ファイルである。

方法 1 - easy_install 経由でインストール
----------------------------------------------------------------------
インターネットが利用できる環境ではいつも通りコンソールウィンドウで

.. code-block:: text

   $ easy_install nose

とタイプすればよい。

万が一 `easy_install`_ をインストールしていなかったならば、インターネットから入手せよ。

方法 2 - setuptools を利用してソースからインストール
----------------------------------------------------------------------
まずは学校・職場・漫画喫茶等に行き、インターネットにアクセス。

自宅環境に `setuptools`_ をインストールしていなかったならば、先に入手すること。
これも持ち帰る。

目的の Nose_ のコード一式（おそらく ``nose-0.11.4.tar.gz`` のような名前）
を公式サイトからダウンロードして、それを USB メモリか何かに入れて持ち帰る。

解凍した後、次のようにする。

.. code-block:: text

   $ cd nose-0.11.4
   $ python setup.py install

利用方法
======================================================================
``nosetests`` と Nose ライブラリー本体の利用方法に分けて理解する。

``nosetests``
----------------------------------------------------------------------
Nose をインストールすると、Python パッケージだけでなく、
``nosetests`` というスクリプトか実行ファイルが ``Scripts`` フォルダーにインストールされる。

* これは py ファイルからテストを自動的に発見し、実行することができる便利なツールだ。

* 引数なしで起動すると、おそらくカレントディレクトリーにあるすべての py ファイルから、
  すべてのテストを発見し、片っ端から実行するというはたらきをするのではないだろうか。

* 普通は ``nosetests`` にコマンドライン引数を指定して利用する。
  次のコマンドライン例は Nose のドキュメントから引用したものだ。
  モジュール名を指定したり、さらにテスト名を指定したり、
  あるいはモジュールフルパスプラステスト名という指定の仕方がサポートされているようだ。

  .. code-block:: text

     $ nosetests test.module
     $ nosetests another.test:TestCase.test_method
     $ nosetests a.test:TestCase
     $ nosetests /path/to/test/file.py:test_function

* ディレクトリーごと指示するやり方もある。その場合、複数パス指定が許される。

  .. code-block:: text

     $ nosetests /path/to/tests /another/path/to/tests

  なので、実は ``-w, --where`` オプションは無用の長物。

* ``nosetests`` は豊富なコマンドラインオプションを提供している。
* コマンドラインオプションと同等の設定を設定ファイルからも行える。

  * デフォルトの設定ファイルは ``$HOME`` にある ``.noserc`` または ``nose.cfg`` だ。
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

collect-only オプション テスト名だけを調べる
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``--collect-only`` オプションでテストを実行せずにテスト名だけを確認できる。

* さらに ``--with-id`` を併用し、テストのインデックスリストも得られる。
* ``--verbosity`` オプションを併用して、テスト名等を明示させるのがコツ。

.. code-block:: text

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

pdb-failures オプション テスト失敗時にデバッガーを起動
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``--pdb-failures`` オプションを指定しておくと、テストが FAILURE になった地点で
Python の pdb デバッガが起動する。

* 通常使いたいのは ``--pdb`` ではなく ``--pdb-faillures`` のほうだと思う。
* pdb はコンソールベースのデバッガ。正直なところ不慣れなツールだが、この際慣れておく。

.. code-block:: text

   $ nosetests --pdb-failures
   .> d:\home\yojyo\devel\pyunitdemo\testeven.py(6)check_even()
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

with-profile オプション プロファイリング
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``--with-profile`` オプションで、
テストに関係した全関数に対する呼び出しの回数や時間の統計を取れる。
いつものテスト結果を出力した直後に、プロファイル結果を出力する。

.. code-block:: text

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
* ``-V`` または ``--version`` で ``nosetests`` のバージョンを表示。
* ``-v`` または ``--verbosity`` で表示を少々やかましくできる。
  テスト名確認時にはこれを併用するだろう。

* ``-m REGEX`` 系オプションで「テストとみなしたいファイル・ディレクトリー・関数・クラス名にマッチする」
  正規表現を指定できる。
  
  デフォルトで ``(?:^|[\b_\.\-])[Tt]est`` になっていることを押させておけばよい。

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
    全部抽出してリストを作成できたりする。何かの役に立つわけではないがね。

    .. code-block:: text

       $ cd site-packages/jinja2
       $ python -c 'import jinja2; print jinja2.__version__'
       2.5.5
       $ nosetests --collect-only --with-id -v testsuite/*.py
       #56 test_autoescape_autoselect (jinja2.testsuite.api.ExtendedAPITestCase) ... ok
       #57 test_cycler (jinja2.testsuite.api.ExtendedAPITestCase) ... ok
       #58 test_expressions (jinja2.testsuite.api.ExtendedAPITestCase) ... ok
       ... 省略
       #264 test_markup_leaks (jinja2.testsuite.utils.MarkupLeakTestCase) ... ok

       ----------------------------------------------------------------------
       Ran 250 tests in 0.871s
       
       OK

  * Matplotlib_ の ``tests`` フォルダーはテストパッケージの構成になっている。
    nosetests の実験場としては面白い。

  * NumPy_ は Nose をうまく使いこなしているようだ。
    ``import numpy; help(numpy.test)`` してみよう。
    テストの単位をわかりやすく分類する努力を払っているのがわかる。

* 未調査項目

  * 属性指定テスト起動 (``--attr=ATTR``) を調べていない。
  * プラグイン周りを調べていない。
  * ログ設定周りを調べていない。
  * コードカヴァレッジ周りを調べていない。別のプラグインが必要らしい。
  * Windows 環境ゆえ、マルチプロセステストが試せないのは残念。

.. _Nose: http://somethingaboutorange.com/mrl/projects/nose/
.. _easy_install: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _setuptools: http://peak.telecommunity.com/DevCenter/setuptools
.. _py.test: http://codespeak.net/py/current/doc/test.html
.. _Jinja2: http://jinja.pocoo.org/
.. _Matplotlib: http://matplotlib.sourceforge.net/
.. _NumPy: http://scipy.org/NumPy
