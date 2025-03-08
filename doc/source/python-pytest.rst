======================================================================
Pytest 利用ノート
======================================================================

.. |pip| replace:: :program:`pip`
.. |pytest| replace:: :program:`pytest`

Python のテストフレームワークとして著名かつ人気のある pytest_ に関するノートだ。

.. contents:: 章見出し
   :local:

概要
======================================================================

   The pytest framework makes it easy to write small, readable tests, and can
   scale to support complex functional testing for applications and libraries.

インストール・更新・アンインストール
======================================================================

複数人で共用するプロジェクトの開発環境に pytest_ をインストールする事例では、そ
のプロジェクトの定める手順に従え。README や :file:`pyproject.toml` を読めば判明
する。

自分が所有する作業用仮想環境に pytest_ をインストールするならば、愛用している仮
想環境ツールがインストールコマンドを実装している場合にはそれを使え。私ならば
Miniconda_ であるから、例えば次のようにする：

.. sourcecode:: console
   :caption: 現在の conda 仮想環境に |pytest| をインストールする
   :force:

   conda install -c conda-forge pytest

仮想環境ツールがインストールコマンドを持っていない場合には、対象仮想環境が有効で
あることを確認してから |pip| を使え：

.. sourcecode:: console
   :caption: 昔ながらの |pip| による |pytest| インストール手順例
   :force:

   pip install pytest

インストール手順の説明は以上だ。pytest_ の更新、アンインストールの手順は、対応す
る条件におけるインストール手順に合致する手順を選べ。例えば :program:`conda` を
使っているのならば ``conda uninstall pytest`` を走らせる、というようにだ。

.. seealso::

   :doc:`/python-miniconda`

構成・カスタマイズ
======================================================================

   Many pytest settings can be set in a `configuration file`, which by
   convention resides in the root directory of your repository.

Pytest_ はプロジェクトごとに構成ファイルを設ける流儀であり、ユーザー構成ファイル
は考えなくてよい。この節の目的は終わった。

何かの過渡期であるようで、ファイル書式が複数ある。プロジェクトのルートディレクト
リーに次のファイルのいずれかが置いてあれば、それが考慮される（この説明は厳密には
正しくないが、理解のためにそう記した）：

* :file:`pytest.ini`
* :file:`pyproject.toml` 内 ``tool.pytest.ini_options`` 区画
* :file:`tox.ini` 内 ``pytest`` 区画
* :file:`setup.cfg` 内 ``tool:pytest`` 区画

今の時代に INI ファイルは書きたくない。私は普通は :file:`pyproject.toml` を用い
る。次のようなコードを与える：

.. sourcecode:: toml
   :caption: :file:`pyproject.toml` における |pytest| 構成記述例
   :force:

   [tool.pytest.ini_options]
   addopts = "--color=yes --showlocals --strict-markers"
   asyncio_mode = "strict"
   doctest_optionflags = [
     "NORMALIZE_WHITESPACE",
     "ELLIPSIS"
   ]
   filterwarnings = [
     "error",
   ]
   log_cli_level = "INFO"
   markers = [
     "slow",
   ]
   minversion = "8.0"
   python_files = [
     "test_*.py",
     "__init__.py",
   ]
   testpaths = "tests"
   tmp_path_retention_policy = "failed"
   xfail_strict = true

オプションの名称と型は ``pytest --help`` から確認可能。

使用方法・コツ
======================================================================

全般
----------------------------------------------------------------------

.. todo::

   * GitHub Actions
   * プロジェクトファイルでの指定例

     * :file:`Pipfile`
     * :file:`pyproject.toml`
     * :file:`hatch.toml`
   * 自作 marks
   * doctest
   * 前回失敗したエラーからテストを再開
   * 報告書
   * ログ
   * プラグイン

他のフレームワークから移行するコツ
----------------------------------------------------------------------

標準テストモジュール ``unittest`` を使って構築したテスト一式がある場合、pytest_
に適合させるための作業は本質的には発生しない。コマンドラインで起点となるパスと
:envvar:`PYTHONPATH` を（上述の構成ファイルに記述する方式が望ましい）適当に指定
すれば |pytest| は動作する。

Nose_ から移行する場合、nose2pytest_ を試せ。初回は学習目的で、敢えて手作業で移
行するのも考えられる（時間的余裕が十分ある場合に限る）。

それでも ``unittest`` ベースのコードを pytest 様式に書き換える場合
----------------------------------------------------------------------

``TestCase`` のサブクラスにテストメソッドがあるだけのテストを書き換えるのは容易
い：

* テストモジュールに ``import pytest`` を加えるのが普通。
* ``self.assertXXXX`` 系メソッド呼び出しをすべて ``assert`` 文に書き直す。それに
  伴い、引数リストを Python 文の形に書き直す。例えば：

  * ``self.assertEqual(x, y)`` → ``assert x == y``
  * ``self.assertIs(x, y)`` → ``assert x is y``
  * ``self.assertIn(x, y)`` → ``assert x in y``
  * ``self.assertRaises(Err, f, args)`` → ``with pytest.raises(Err,
    matches="..."): f(args)`` and more

* サブクラス定義の行を取り払い、インデントを一段浅くする。
* メソッドだったものの第一引数 ``self`` を取り除く。フリー関数に書き直すため。
* メソッド ``setUp`` や ``tearDown`` を実装していたテストクラスでは、この資源管
  理処理を後述するコツのように書き換える。
* ``unittest.mock.{Magic,}Mock`` と ``unittest.mock.patch`` を用いたコードを書き
  直す。例えば pytest 組み込みオブジェクト ``monkeypatch`` を用いたものに書き換
  える。機能の一部は代替不能かもしれない。

テストコードに関するコツ
----------------------------------------------------------------------

テストコードに関するコツを記していくが、以下の事項については既知とする：

* ``pytest.fixture`` の概念と適用方法。例えば組み込み fixture は明示的インポート
  なしで参照可能だ。
* ``pytest.mark``
* ``monkeypatch``

以下のコード例では通常 ``import pytest`` を必要とする。

資源の初期化と解放を管理する fixture では ``yield`` を使え
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

初期化と解放の両方が必要な fixture では ``return`` ではなく ``yield`` で資源
を呼び出し元に引き渡せ。

.. sourcecode:: python
   :caption: RAII 実装例
   :force:

   @pytest.fixture
   def resource(args):
       res = acquire_resoure(args)
       yield res
       release_resource(res)

専用 context manager がある場合には、上の関数定義が ``with`` ブロックになり、最
後の文が ``yield res`` になるだけだ。本質的には同じこととなる。

テストディレクトリーに :file:`conftest.py` を置け
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ファイル :file:`conftest.py` を用意し、テストモジュールのテスト関数がよく用いる
fixture 関数定義をここで行え。さらに、テストモジュールが階層を形成している場合に
はサブディレクトリーにもファイル :file:`conftest.py` を置くことが有利である場合
がある。サブディレクトリーにあるテスト機能に特化するように fixture をこのファイ
ルで上書きすることが可能だ。

標準ストリームの内容を扱うのに ``capsys`` を使え
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

組み込み fixture である ``capsys`` から ``sys.stdout`` and/or ``sys.stderr`` の
内容と同じものを読み取ることが可能だ。これは標準出力に対してしか出力しない機能を
テストするときや、エラー出力をテストするときに有用だ。要点は：

* この fixture は pytest_ 組み込みであるため、テスト関数の引数リストに即列挙可能
  だ。
* ``capsys.readouterr()`` は標準出力と標準エラー出力の内容と同じ文字列の対を返
  す。それぞれを参照するには ``out``, ``err`` を指定する。

.. sourcecode:: python
   :caption: ``capsys`` 利用例
   :force:

   def test_dump(capsys):
       dump(["C808DA", "12", "1389"])
       actual = capsys.readouterr().out.split("\n")
       assert actual[0].startswith("C8/08DA:")

送出される例外の型をテストするだけならば ``pytest.mark.xfail`` を使え
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

テスト関数を ``xfail`` で装飾するだけで済む。その ``raises`` キーワード引数に期
待する例外型を指定しろ。

次の例は関数 ``confdir_home`` が特定の条件下（詳細割愛）で例外
``ConfigNotFoundError`` を送出することを試験するものだ：

.. sourcecode:: python
   :caption: ``mark.xfail`` 利用例
   :force:

   @pytest.mark.xfail(raises=ConfigNotFoundError)
   def test_confdir_home_error(monkeypatch):
       with monkeypatch.context():
           monkeypatch.setattr(os.environ, "get", lambda _: "")
           monkeypatch.setattr(pathlib.Path, "home", lambda: pathlib.Path("/dev/null"))
           confdir_home()

テスト実行結果では当該テストに印 ``x`` がつく。

未完成のテストには ``pytest.mark.skip`` を付けろ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ソフトウェア開発の性質上、テスト関数は完成しているが、本体機能のほうが未完成とい
う場合が普通に生じる。そのような場合には次の例にようにしておけばよい：

.. sourcecode:: python
   :caption: ``mark.skip`` 利用例
   :force:

   @pytest.mark.skip(reason="This feature has been not yet completed")
   def test_feature_not_yet_completed(): ...

実行条件が付くテストには ``pytest.mark.skipif`` を付けろ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

前項の系だが、先行する開発機能があるなど、実行環境次第で成否が決まるテストには
``skipif`` を適用しておくと良さそうだ。

.. sourcecode:: python
   :caption: ``mark.skipif`` 利用例
   :force:

   @pytest.mark.skipif(not check_config(), reason="No configuration provided")
   def test_confdir_home(): ...

データ差し替えテストには ``pytest.mark.parametrize`` を使え
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

テスト対象関数を、実引数だけ変えて何度か呼び出すようなテスト関数があるとする。そ
ういう場合には ``pytest.mark.parametrize`` で decorate すると保守がし易くなる。
そればかりでなく、テストケースの水増しにも有効だ。簡単な例でそれを示す：

.. sourcecode:: python
   :caption: ``mark.parametrize`` 使用前
   :force:

   def test_is_even():
       for i in range(0, 10, 2):
           assert is_even(i)

これを次のように書き換えると、テスト項目数が 1 から 5 に増える：

.. sourcecode:: python
   :caption: ``mark.parametrize`` 使用後
   :force:

   @pytest.mark.parametrize("number", range(0, 10, 2))
   def test_is_even(number):
       assert is_even(number)

まともな decorator なので重ねがけができることに注意：

.. sourcecode:: python
   :caption: ``mark.parametrize`` 重ねがけの実例
   :force:

   @pytest.mark.parametrize(
       "data",
       (
           (0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06),
           b"\x00\x01\x02\x03\x04\x05\x06",
       ),
   )
   @pytest.mark.parametrize(
       "index,length,expected",
       (
           (0, 1, 0x00),
           (1, 1, 0x01),
           (0, 2, 0x0100),
           (6, 2, 0x0006),
           (0, 3, 0x020100),
           (5, 3, 0x000605),
           (6, 3, 0x000006),
       ),
   )
   def test_get_int(data, index, length, expected):
       assert get_int(data, index, length) == expected

一括適用に ``pytestmark`` を指定しろ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

あるテストモジュール（またはテストクラス）が含むテスト関数全てを
``pytest.mark.skip``, ``pytest.mark.xfail``, .etc で適用するには、pytest 組み込
みオブジェクト ``pytestmark`` に値を代入するのが手軽だ：

.. sourcecode:: python
   :caption: ``pytestmark`` 使用例
   :force:

   # In a test module

   from mypackage.config import check_config

   pytestmark = pytest.mark.skipif(
       check_config() is None, reason="No configuration provided"
   )

この右辺自体を複数のテストモジュールで使用したい場合には、それを
:file:`__init__.py` などで別のオブジェクト (e.g. ``requires_config``) に代入して
おき、各モジュールからそれを ``import`` して ``pytestmark = requires_config`` な
どとすればコード量がさらに抑えられるだろう。

知っていると便利なコマンドラインオプション
----------------------------------------------------------------------

重要なオプション設定は構成ファイルに記述するので、ここに挙げるのは実行時にしか指
定することがないオプションとする。

テストを実行しないコマンドを先に挙げる：

``pytest --version``
   |pytest| 本体と、もしあればプラグインのバージョンを出力する。
``pytest --help``
   |pytest| インターフェイス仕様記述を出力する。構成ファイルの項目名を確認するこ
   とも可能だ。
``pytest -q``
   実行結果を許される範囲でコンパクトに出力する。ドットなどが縦横に並んで表示さ
   れ、定型的文言は省かれる。
``pytest --collect-only``
   実行テスト一覧を階層的に表現して出力する。後述する実行コマンドに付加して用い
   る。
``pytest --fixtures``
   使用可能な fixtures 一覧を、その関数 docstring と共に出力する。基本的には組み
   込み、プラグイン、自作の順番に fixtures が並ぶようだ。
``pytest --fixtures-per-test``
   テスト関数それぞれに対して仕込まれる fixtures を一覧する。言い換えると、テス
   ト関数の引数リストに現れる仮引数がすべて示される。この出力にも docstring が使
   われる。
``pytest --markers``
   使用可能な markers 一覧を出力する。

テスト動作を調整するオプションを指定したコマンド：

:samp:`pytest -k {keyword}`
   文字列 `keyword` を部分文字列とする名前のテストに限定して実行する。アルファ
   ベットの大文字小文字は区別しない。実際はもっと高機能だが、とりあえずこれだけ
   憶えておく。文字列を適宜引用符で囲むのがよい。

   利点：テスト対象ファイル名を憶えていなくて済む。
:samp:`pytest -m {marker-spec}`
   テストのうち、その ``@pytest.mark`` が `marker-spec` に合致するものしか実行し
   ない。
``pytest --pdb``
   エラー時または例外 ``KeyboardInterrupt`` が発生した場合に対話型 Python デバッ
   ガーを起動させる。

.. note:: 利用者ノート

   再テスト順序指定オプションやログオプションなど、まだまだ機能がある。

コマンドライン引数
----------------------------------------------------------------------

コマンドライン引数を何も指定しない場合、一般的にコマンド |pytest| は作業ディレク
トリーとその下位にある :file:`test_*.py` または :file:`*_test.py` というファイル
名の全てのテストを実行する。特定のテストを実行するには、例えば次のいずれかのパ
ターンのコマンドを組み立てる：

``pytest tests/``
   ディレクトリー :file:`tests/` およびその下位にあるテストモジュールのテスト全
   てを対象とする。
``pytest tests/test_mod.py``
   モジュール :file:`tests/test_mod.py` にあるテスト全てを対象とする。
``pytest tests/test_mod.py::test_func``
   モジュール :file:`tests/test_mod.py` にあるテスト関数 ``test_func`` を唯一の
   テスト対象とする。
``pytest tests/test_mod.py::test_func[x1,y2]``
   モジュール :file:`tests/test_mod.py` にあるテスト関数 ``test_func`` を唯一の
   テスト対象とし、さらにその引数指定を ``x1,y2`` とする。
``pytest tests/test_mod.py::TestClass``
   モジュール :file:`tests/test_mod.py` にあるテストクラス ``TestClass`` にある
   テスト全てを対象とする。
``pytest tests/test_mod.py::TestClass::test_method``
   モジュール :file:`tests/test_mod.py` にあるテストクラス ``TestClass`` にある
   メソッド ``test_method`` を唯一のテスト対象とする。

.. note:: 利用者ノート

   ツール等を経由して |pytest| を実行する場合、パスを入力するのにファイルパスに
   対するタブ補完が効かずに、面倒である場合があることに注意。そういう場合は前項
   で見たオプション :samp:`-k {keyword}` を用いる。

環境変数
======================================================================

さまざまな環境変数が |pytest| の挙動に影響するが、基本的には利用しない。

:envvar:`CI`, :envvar:`BUILD_NUMBER`
   これらの環境変数は開発者が手動で ``declare`` するものではない。

   どちらかでも設定されていれば、|pytest| は自身が CI 環境で実行されているものと
   して振る舞う。例えば、``pytest.fail`` などの概要情報の出力が端末ウィンドウの
   横幅に切り詰められなくなる。
:envvar:`PYTEST_ADDOPTS`
   構成ファイルのオプション ``addopts`` の環境変数版だ。オプションを構成ファイル
   で指定するのが通例であり、用いない。
:envvar:`PYTEST_VERSION`
   この環境変数は |pytest| 開始時に定義される。テストを実行したのがコマンドライ
   ンからであるのか否かを判定するのに用いられるらしい。
:envvar:`PYTEST_CURRENT_TEST`
   |pytest| はテストを実行する際にこの環境変数を設定する。テストが固まったときに
   この値を参照するようにすることで、どのテストで詰んでいるのかの手がかりが得ら
   れる。

   公式文書では ``psutil.pids()`` の各プロセスに対して ``environ()`` でこの環境
   変数の存在、設定値を確認するという処理例が挙げられている。
:envvar:`PYTEST_DEBUG`
   宣言してから |pytest| を実行するとトレースとデバッグ情報をも出力する。

   出力量が厖大ゆえ、使うのはテスト対象を絞りに絞ってからにしろ。
:envvar:`PYTEST_DEBUG_TEMPROOT`
   一時ファイル系 fixtures が作成する一時ディレクトリーの基点となるパス。

   コマンドラインオプション ``--basetemp`` に相当する。よって使わない。
:envvar:`PYTEST_DISABLE_PLUGIN_AUTOLOAD`
   宣言されている場合に、プラグインの自動ロードが無効になる。明示的に指定された
   プラグインはロードされる。
:envvar:`PYTEST_PLUGINS`
   プラグインとしてロードしたいモジュールを CSV 形式で指定すると、そうなる。
:envvar:`PYTEST_THEME`
   コード出力に使用する :doc:`/python-pygments` スタイルを設定すると、|pytest|
   の出力にそれが反映される。

   こんな凝ったオプションは使わない。
:envvar:`PYTEST_THEME_MODE`
   :envvar:`PYTEST_THEME` を ``dark`` か ``light`` のどちらかに設定する。
:envvar:`PY_COLORS`
   値を ``1`` に設定すると |pytest| は端末出力で色を使う。値を ``0`` に設定する
   とそうはしない（テスト結果記号が地の文字色と同じくなる）。

   .. note::

      |pytest| は環境変数 :envvar:`NO_COLOR` を考慮する。

評価
======================================================================

これから個人開発の Python パッケージには |pytest| をなるべく導入しよう。次の機能
が気に入った：

* テストの「証拠集め」を Python 標準の ``assert`` 一丁で賄う姿勢。
* Fixtures の使い勝手。再利用性がすこぶる良い。
* ``pytest.mark.paramtrize`` でテストケースを大幅に実量以上に見せかけるのが容易
  であること。
* ``pytestmark``

資料集
======================================================================

何しろ人気パッケージであり、インターネットを検索すると高品質の記事がいたるところ
にある。それらをすぐに参照できるようにして整理しておくほうが、私が独りよがりな何
やらを書き殴るよりもはるかに良いだろう。

`pytest documentation`_
   公式文書。全ページに目を通せ。掲載コードを可能な限り検証しろ。紙幅の都合上、
   動作に足りないコード片があるものの、理解できている読者ならば補える。
`Effective Python Testing With pytest <https://realpython.com/pytest-python-testing/>`__
   Real Python 内解説記事。
`Pytest — A beginner Guide <https://medium.com/@ronakchitlangya1997/pytest-a-beginner-guide-f9d4919cd427>`__
   入門記事で ``xfail`` と ``skip`` に触れているものは珍しい。
`Pytest vs Unittest: A Comparison <https://www.browserstack.com/guide/pytest-vs-unittest>`__
   両者を徹底的に比較考量している。長所と短所を列挙し、各項目について双方の性質
   を述べている。記事の造りが堅実であり、すごく参考になる。
`Pytest vs. Unittest: Which Is Better? <https://blog.jetbrains.com/pycharm/2024/03/pytest-vs-unittest/>`__
   こちらも pytest と unittest の比較記事で、コードを示している。
`Pytest: Getting started with automated testing for Python <https://circleci.com/blog/pytest-python-testing/>`__
   CircleCI にある文書。単語 streamline がよく出てくることから、このテストフレー
   ムワークに期待される重要な性質が見えてくる。
`What Is pytest: A Complete pytest Tutorial With Best Practices <https://www.lambdatest.com/learning-hub/pytest-tutorial>`__
   Selenium を使ったアプリケーションのテストを pytest で実施するチュートリアルを
   含む記事（私はまだ試していない）。序盤の統計データも興味深い。

以上のほかにも優等記事が世にあるはずだ。

`I want to use stdin in a pytest test <https://stackoverflow.com/questions/38723140/i-want-to-use-stdin-in-a-pytest-test>`__
   Stack Overflow より。

.. include:: /_include/python-refs-core.txt
.. _pytest documentation: https://docs.pytest.org/en/stable/
.. _nose2pytest: https://github.com/pytest-dev/nose2pytest
