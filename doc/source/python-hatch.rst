======================================================================
Hatch 利用ノート
======================================================================

.. |hatch| replace:: :program:`hatch`
.. |hatch.toml| replace:: :file:`hatch.toml`
.. |mypy| replace:: :program:`mypy`
.. |pip| replace:: :program:`pip`
.. |pyproject.toml| replace:: :file:`pyproject.toml`
.. |pytest| replace:: :program:`pytest`
.. |ruff.toml| replace:: :file:`ruff.toml`

.. contents:: 章見出し
   :local:

概要
======================================================================

   Hatch is a modern, extensible Python project manager.

一言で表現すると確かにこれ以外のものが思いつかない。やれることがたくさんある。

   The high level value proposition of Hatch is that if one adopts all
   functionality then many other tools become unnecessary since there is support
   for everything one might require. Further, if one chooses to use only
   specific features then there are still benefits compared to alternatives.

例えば次の機能を備えている：

* Python 仮想環境管理
* クロスプラットフォーム
* 依存パッケージの導入や更新などの環境
* ビルド構成
* 製品バージョン更新
* テストおよびコード静的解析手順構成
* 成果物の配備

インストール・更新・アンインストール
======================================================================

愛用している仮想環境ツールがインストールコマンドを実装している場合にはそれを使え。
私ならば Miniconda_ であるから、例えば次のようにする：

.. sourcecode:: console
   :caption: 現在の conda 仮想環境に Hatch をインストールする
   :force:

   conda install -c conda-forge hatch

インストール手順の説明は以上だ。Hatch_ の更新、アンインストールの手順は、対応す
る条件におけるインストール手順に合致する手順を選べ。例えば :program:`conda` を
使っているのならば ``conda uninstall hatch`` を走らせる。

.. seealso::

   :doc:`/python-miniconda`

構成・カスタマイズ
======================================================================

Hatch 自身に対する構成
----------------------------------------------------------------------

既定ではファイル :file:`$XDG_CONFIG_HOME/hatch/config.toml` に |hatch| 自身に対
する構成を記述する。新規作成プロジェクトの雛形を構成するファイルでもある。

構成はコマンド ``hatch config show`` で確認可能。

プロジェクトに対する構成
----------------------------------------------------------------------

構成は Python プロジェクトディレクトリーに置かれるファイル |pyproject.toml| また
はファイル |hatch.toml| に指定する。前者を用いる場合、構成区画名は
:samp:`[tool.hatch.{xxxx}]` などのようになる。

当ノートでは |hatch.toml| に記述可能であるものは必ずそちらに記述するものとする。
文字列 ``tool.hatch`` を書かないぶん、区画名が若干短くなる。

使用方法・コツ
======================================================================

以下、ツールが出力する |pyproject.toml| の内容のうち、|hatch| しか認識しないもの
を |hatch.toml| に（適宜整形して）分離することにする。

頻出コマンド一覧
----------------------------------------------------------------------

構成がいったん落ち着くと、ローカルレポジトリーで使う |hatch| コマンドは次くらい
しかない：

``hatch env find``
   プロジェクトの仮想環境が収められているディレクトリーのパスを示す。
``hatch env show``
   定義されている Hatch 環境一覧を出力する。使い勝手が良いのはオプション
   ``--json`` を付けて :program:`jq` にパイプして対象を絞り込むのが見易い。
``hatch env show --internal``
   Hacth 内蔵環境一覧を出力する。既定の依存を調べるのに有用だ。
``hatch fmt --check``
   コードを静的解析する。ファイルを上書きしない。
``hatch fmt --check --sync``
   コード書式整形既定規則が Hatch 側で更新されたときに、プロジェクトの整形ツール
   が参照する規則ファイルにそれを適用する。構成項目 ``config-path`` が示すファイ
   ルを上書きする。
``hatch fmt --formatter``
   コードを書式整形する。コードファイルを上書きする。
``hatch fmt --linter``
   コードを静的解析し、望ましくない記述を可能な限り修正する。コードファイルを上
   書きする。
:samp:`hatch new {project-name} {location}`
   Python プロジェクト `project-name` を構成するディレクトリー群および構成ファイ
   ルをパス `location` に新規作成する。実行頻度はプロジェクト開始時に一度きりだ。
   適当な一時ディレクトリーでこのコマンドを実行して出力を見るがいい。
:samp:`hatch run {env-name:command}`
   環境 `env-name` に入ってからコマンド `command` を走らせる。
``hatch run types:check``
   既定構成では |mypy| が走るはず。
``hatch test``
   単体テストを実施する。

詳しくはサブコマンドごとに節を設けて後述する。

環境
----------------------------------------------------------------------

Hatch_ で言う環境とは、例えば次のような特定の課題を達成するために用意する他から
隔離された作業場くらいの意味に解釈してかまわない：

* コードを整形する
* コードに対して静的解析を行う
* コードをテストする
* 文書をビルドする

ほとんどの |hatch| コマンドは何らかの環境を与えられたものとして機能する。初期構
成であっても、既定で ``default`` という名前の環境が存在する。

プロジェクトにある環境一覧を確認する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

利用可能な環境を確認するには次のコマンドを使え。表形式で得られる：

``hatch env show``
   明示的に構成された環境を出力する。既定では ``default`` と ``types`` の二つの
   環境が存在することが示されるはずだ。
``hatch env show -i``
   内蔵環境と呼ばれるものの構成を出力する。重要なスクリプトを含む環境が揃ってい
   る。詳しくはビルドおよびテストの節で後述する。
:samp:`hatch env show {env-name}`
   環境 `env-name` の構成を出力する。内蔵環境でもかまわない。

.. admonition:: 利用者ノート

   書式オプション ``--json`` を指定し、:program:`jq` などで出力を絞り込むのと見
   通しが良い。

プロジェクトに環境を新規作成する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

環境を定義するには |hatch.toml| に区画 :samp:`[envs.{env-name}]` を設け、そこに
環境 `env-name` を構成する属性を指定する。詳細を記述したら、適当な |hatch| コマ
ンドを実行することによりこの環境が成立する。

環境を特定してコマンド（やスクリプト）を実行するには次のいずれかを実行する：

* :samp:`hatch run {env-name}:{command-or-script}`
* :samp:`hatch env run -e {env-name} {command-or-script}`
* :samp:`hatch -e {env-name} shell` で環境 `env-name` に入ってから、そこで有効な
  コマンド :samp:`hatch run {command-or-script}` を実行する
* シェルの環境変数として :envvar:`HATCH_ENV` を設定したうえでコマンドやスクリプ
  トを実行する

スクリプト
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

区画 :samp:`[envs.{env-name}.scripts]` に :samp:`{script-name} = {script-body}`
の形式で環境固有のスクリプトと呼ばれるコマンドを定義することが可能だ。

.. sourcecode:: toml
   :caption: スクリプト定義例（二番目のものは実践しないこと）
   :force:

   # Suppose the environments [envs.types] and [envs.styles] are properly defined.
   [envs.types.scripts]
   check = "mypy --strict {args:src/my-package}"

   # Scripts can also be defined as an array of strings.
   [envs.style.scripts]
   check = [
     "flake8 .",
     "black --check --diff .",
     "isort --check-only --diff .",
   ]

定義したスクリプトを実行するには、先述のように環境指定のある実行コマンドを実行す
る。この例では ``hatch run types:check`` や ``hatch run style:check`` は有効なス
クリプト呼び出しだ。

定義済みスクリプトを確認するには、コマンド ``hatch env show`` の出力を見ればいい。

.. todo::

   * 継承 ``type``, ``template``
   * ``detached``: インストールを省く
   * 定数を :samp:`[envs.{env-name}.env-vars]` に :samp:`{name} = {value}` の形
     で定義可能。

実例
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``hatch new`` の出力する |pyproject.toml| の時点で環境 ``types`` が定義
済みであり、かつ ``check`` というスクリプトが定義済みだ。次のコードはそれを
|hatch.toml| に移動したものだ：

.. sourcecode:: toml
   :caption: 定義済み環境
   :force:

   [envs.types]
   extra-dependencies = [
     "mypy>=1.0.0",
   ]
   [envs.types.scripts]
   check = "mypy --install-types --non-interactive {args:src/name tests}"

これにより、コマンド ``hatch run types:check`` が機能する。パッケージ mypy_ がイ
ンストールされていない状態で実行すれば、これを |hatch| が環境にインストールして
から |mypy| が走るはずだ。

依存
----------------------------------------------------------------------

本節では依存の基本概念、必要依存と選択的依存について記す。ファイル
|pyproject.toml| に関する、本来 Hatch_ とは独立した仕様にも言及する。

依存 (dependency) の定義は `PEP 508`_ による。

Hatch_ にはプロジェクトや環境が依存するパッケージを指定する機能がある。プロジェ
クトならファイル |pyproject.toml| にある区画 ``[project]`` 直下の配列
``dependencies`` で、環境ならファイル |hatch.toml| にある環境定義区画
:samp:`envs.{env-name}` 直下の配列 ``dependencies`` でそれぞれ指定する。それぞれ
依存先パッケージを `PEP 440`_ 方式で指定する。

依存先パッケージのインストールには |pip| が用いられる。

依存先パッケージは ``hatch shell`` や ``hatch run`` を実行したりするときに必要に
応じて |hatch| がインストールする。

必要依存
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

例えば、プロジェクトが開発している対象がサードパーティー製パッケージ
:doc:`Click </python-click>` を使用しているとする。そのバージョンが 8.1 あるいは
それと互換なバージョンであることを指定する場合、次のように指定することが可能だ：

.. sourcecode:: toml
   :caption: プロジェクト依存パッケージ指定例
   :force:

   [project]
   dependencies = [
     "click~=8.1",
   ]

この設定により、コマンド :samp:`pip install {project-name}` を実行してプロジェク
ト `project-name` 本体をインストールすると、Click もインストールされ、そのバー
ジョンは 8.1 と互換性がある。ここまでの説明は |Hatch| とは関係ない。

プロジェクトが必要とする依存とは別に、Hatch_ 環境が要求する依存を指定することが
可能だ。構成ファイルの環境区画 :samp:`[envs.{env-name}]` に上記の要領で配列
``dependencies`` を与えればよい。

.. sourcecode:: toml
   :caption: 環境依存パッケージ指定例
   :force:

   [envs.docs]
   dependencies = [
     "mkdocs~=1.6"
   ]

このように指定することで、例えば `some-script` というスクリプトが定義されていれ
ば、コマンド :samp:`hatch run docs:{some-script}` 実行時など、環境 ``docs`` に入
るときに依存パッケージが必要に応じてインストールされる。

選択的依存
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

必須ではなく、選択的に依存するパッケージという概念もある。指定方法は、区画
``[project.optional-dependencies]`` で :samp:`{option-name} = {dependencies}` を
与えるものだ。別の項目が参照するものであることに注意。

.. sourcecode:: toml
   :caption: ``optional-dependencies`` 構成例（実践的でない）
   :force:

   [project.optional-dependencies]
   checker = [
     "mypy",
     "ruff",
   ]

この設定により、コマンド :samp:`pip install {project-name}[dev]` を実行するとプ
ロジェクト `project-name` 本体と共に ``dev`` が指定するパッケージも併せてインス
トールされる。以上に述べたことは |Hatch| とは関係ない。

環境が上記の選択的依存を参照することがある。配列 ``features`` で選択的依存を名前
で指定する。

.. sourcecode:: toml
   :caption: ``features`` 構成例
   :force:

   [envs.nightly]
   features = [
     "checker",
   ]

この状況では、環境 ``nightly`` に |hatch| が入るときに、選択的依存 ``checker``
指定のパッケージ群が必要に応じてインストールされる。

その他
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. todo::

   * 値の文字列の書式規則
   * 値に書ける ``{args}`` などの説明

コード整形および静的解析
----------------------------------------------------------------------

コード整形や静的解析はコマンド ``hatch fmt`` に専用オプションを指定して行う。裏
では Ruff_ が走る。

コマンド ``hatch fmt`` の挙動のうち、主要なものは四つある。この一つ一つを内蔵環
境 ``hatch-static-analysis`` のスクリプトそれぞれが指定している。定義はおおまか
には次のようなものだ：

.. sourcecode:: toml
   :caption: ``env.hatch-static-analysis.scripts``
   :force:

   [envs.hatch-static-analysis.scripts]
   format-check = "ruff format --check --diff {args:.}"
   format-fix = "ruff format {args:.}"
   lint-check = "ruff check {args:.}"
   lint-fix = "ruff check --fix {args:.}"

コマンド ``hatch fmt`` を

* オプションなしで実行するとスクリプト ``lint-fix`` と ``format-fix`` が走る。
* オプション ``--check`` を付けると ``lint-check`` や ``format-check`` が走る。
* オプション ``-l``/``--linter`` を付けるとスクリプト ``lint-fix`` が走る。
* オプション ``-f``/``--formatter`` を付けるとスクリプト ``format-fix`` が走る。

.. admonition:: 利用者ノート

   打鍵効率を考慮して、定義コマンド (e.g. ``ruff check``) を端末に直接入力する場
   合もある。

.. seealso::

   Ruff_ そのものについては :doc:`/python-ruff` に記す。

構成項目 ``config-path``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ruff_ に対する Hatch_ 独自の既定構成がある。整形初心者はそのまま用いればよい。独
自に構成する場合にはファイル |ruff.toml| をプロジェクトの基点ディレクトリーに置
いて内容を埋めろ。

Hatch_ が推奨する構成ファイルの配置構成は次のとおり：

#. 環境 ``envs.hatch-static-analysis`` に ``config-path = "ruff_defaults.toml"``
   を記す。
#. ファイル |ruff.toml| を置く。先頭に ``extend = "ruff_defaults.toml"`` を記す。
   残りの部分でプロジェクト固有の構成を与える。
#. ファイル :file:`ruff_defaults.toml` を下で述べるコマンドを実行して生成する。

Hatch_ を更新すると Ruff_ 周りの既定値も更新されることがある。それを反映させるた
めに、更新後にコマンド ``hatch fmt --check --sync`` を一度実行する必要がある。こ
うすると ``config_path`` 値として指示した Ruff_ 構成ファイルが上書きさせる。

Hatch_ 既定構成をいっさい採用せず、完全に自分の構成を与えたい場合には環境
``envs.hatch-static-analysis`` に ``config-path = "none"`` を記せ。もちろん
オプション ``--sync`` もいっさい使うな。

テスト
----------------------------------------------------------------------

既定構成で単体テストを容易に行えるというのが Hatch_ の利点の一つだ。既定構成では
テストコマンドは内蔵環境 ``hatch-test`` で次のように定義されているとされる：

.. sourcecode:: toml
   :caption: 既定テストコマンド
   :force:

   [envs.hatch-test.scripts]
   run = "pytest{env:HATCH_TEST_ARGS:} {args}"
   run-cov = "coverage run -m pytest{env:HATCH_TEST_ARGS:} {args}"
   cov-combine = "coverage combine"
   cov-report = "coverage report"

スクリプト ``run`` はコマンド ``hatch test`` の動作を指定する。フラグ指定を何も
しないときのコマンドと考えればよい。

スクリプト ``run-cov`` は ``hatch test --cover`` および ``hatch test
--cover-quiet`` の動作を指定する。

スクリプト ``cov-combine`` もスクリプト ``cov-report`` も、コード網羅度を計測す
るオプションを使う場合の、テストコマンドの実行が完了した後にこの順番で実行され
る。なお、フラグ ``--cover-quiet`` で計測する場合は呼び出されない。

これらの定義に出てくる ``{args}`` はコマンドライン引数を対応コマンドの末尾に追加
することで |pytest| に引数をそのまま渡すことが可能であることを示す。既定引数を指
定するには環境 ``[envs.hatch-test]`` の配列 ``default-args`` だけを上書き定義す
ればいい。

この構成 ``[envs.hatch-test.scripts]`` 全体を構成ファイルで再定義することが可能。

.. todo::

   * そもそも :program:`coverage` を私が理解していない。
   * ``hatch test --all`` は互換な環境全てで実行

.. seealso::

   Pytest_ については :doc:`/python-pytest` に記す。

環境選択
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

環境には ``matrix`` という属性を有する場合がある。内蔵環境 ``envs.hatch-test``
であり得る組み合わせ全てがテストの対象となる。テストの順序は見てくれと一致すると
は限らず、|hatch| をインストールした Python のバージョンをまず優先する。互換でな
い環境に対しては |hatch| はテストを飛ばすことを告げる。

コマンド ``hatch env show -i`` で Matrices 区画を見ろ。環境 ``hatch-test`` の
``Envs`` として選択可能なものが一覧になっている。

このサブ環境を指定してテストコマンドを実施することが可能であり、それにはオプショ
ン :samp:`-i {env-spec}` を使う。Python のバージョンだけ指定すれば十分な場合には
オプション :samp:`-py {python-version}`` も使える。例えばコマンド ``hatch test
-i python=3.13`` や ``hatch test -py 3.13`` はどちらも環境 ``hatch-test.py3.13``
でのみテストを実施する。

反対に、オプション :samp:`-x {env-spec}` を指定すると、テストコマンドは
`env-spec` でのテストを飛ばす。

コマンド ``hatch new`` が生成する構成ではテスト対象 Python バージョンが多過ぎる
場合、次のように ``matrix`` の定義を上書きしろ：

.. sourcecode:: toml
   :caption: ``envs-hatch-test.matrix`` の構成を簡略化する例
   :force:

   [[envs.hatch-test.matrix]]
   # The version that matches the interpreter on which Hatch runs.
   python = ["3.13"]

ビルド
----------------------------------------------------------------------

コマンド ``hatch build`` について記す。ビルドに関する構成は内蔵環境
``envs.hatch-build`` にあり、ビルドコマンドの実装はスクリプト群
``envs.hatch-build.scripts`` が規定する。

``hatch build -t sdist``
   スクリプト ``build-sdist`` が走る。既定はおそらく ``python -m build --sdist
   {args}``.
``hatch build -t wheel``
   スクリプト ``build-wheel`` が走る。既定はおそらく ``python -m build --wheel
   {args}``.
``hatch build``
   スクリプト ``build-all`` が走る。既定はおそらく ``python -m build {args}``.

どの場合でもフラグオプション ``-c``/``--clean`` をつければ、既存の成果物をまず消
去してからビルドする。環境変数 :envvar:`HATCH_BUILD_CLEAN` も使える。

使う機会はほとんどないが、コマンド ``build`` の代わりに ``clean`` を使うと、
|hatch| は対象成果物の消去のみを行う。

ビルドシステム
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

構成ファイル |pyproject.toml| で次の記述が必須だ：

.. sourcecode:: toml
   :caption: ``[build-system]`` 定義
   :force:

   [build-system]
   requires = ["hatchling"]
   build-backend = "hatchling.build"

その他
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

次のような機能があるが、当面は上述の基本機能だけで十分だ。

* 環境 ``envs.hatch-build`` の配列 ``dependencies`` を上書き可能。
* 構成 ``[envs.hatch-build.env-vars]`` で定数を定義可能。
* 構成 :samp:`[build.targets.{targ-name}]` でビルド対象 `targ-name` を構成する。

  * 配列 ``include``, ``exclude`` でビルド対象の Python ファイルをパターンで選択
    可能。
  * 配列 ``artifacts`` で成果物ファイルをパターンで指定可能。
  * 配列 ``dependencies`` が利用可能。
* ビルドフック

リリース
----------------------------------------------------------------------

コマンド ``hatch publish`` は自作成果物をレジストリーに公開する場合に活用する。

Bash 端末におけるタブ補完
----------------------------------------------------------------------

Bash の対話的モードでの起動時読み込みシェルスクリプトファイルに次のようなコード
を書いておけば十分だ：

.. sourcecode:: bash

   [ -x "$(command -v hatch)" ] && eval "$(_HATCH_COMPLETE=bash_source hatch)"

GitHub Actions
----------------------------------------------------------------------

ワークフローファイルの ``jobs`` の ``steps`` に次のように書け：

.. sourcecode:: yaml

   jobs:
     run:
       # ...
       steps:

       - name: Install Hatch
         uses: pypa/hatch@install

通常は ``install`` の部分を適当な固定コミット ID に置き換える。

Visual Studio Code は Hatch を認識する
----------------------------------------------------------------------

Visual Studio Code の Python 拡張は Hatch がパスにさえあれば、関連した便宜を図
るように振る舞う：

   Hatch environments are now discovered and activated by default, similar to
   other common environments, such as Venv, Conda, and Poetry. Furthermore, in
   the case of Hatch, where an explicit environment identifier is not
   registered, the extension is able to determine the environment type (Hatch)
   from the environment locator. <https://code.visualstudio.com/updates/v1_88>

VS Code のステータスバーにある :guilabel:`Select Interpreter` をクリックし、
:guilabel:`Hatch` と記されている Python を選んでからデバッグなりなんなりしろ。

資料集
======================================================================

Hatch_
   公式。キーボードでページをめくれるのは楽しい。
`PEP 508 Dependency specification for Python Software Packages`_
   依存の意味をこの文書で規定されるように解釈する。
`Install Hatch Action pypa/hatch <https://github.com/pypa/hatch/tree/install>`__
   GitHub Actions ワークフロー用アクション。

.. include:: /_include/python-refs-core.txt
.. _mypy: https://mypy.readthedocs.io/en/stable/
.. _Hatch: https://hatch.pypa.io/latest/
.. _PEP 440: https://www.python.org/dev/peps/pep-0440/
.. _PEP 508:
.. _PEP 508 Dependency specification for Python Software Packages:
   https://peps.python.org/pep-0508/
.. _Ruff: https://docs.astral.sh/ruff/
