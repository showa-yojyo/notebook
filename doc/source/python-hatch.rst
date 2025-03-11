======================================================================
Hatch 利用ノート
======================================================================

.. |hatch| replace:: :program:`hatch`
.. |hatch.toml| replace:: :file:`hatch.toml`
.. |mypy| replace:: :program:`mypy`
.. |pip| replace:: :program:`pip`
.. |pyproject.toml| replace:: :file:`pyproject.toml`
.. |pytest| replace:: :program:`pytest`

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

.. todo::

   明示的に指定したい項目の構成例を挙げる。

プロジェクトに対する構成
----------------------------------------------------------------------

構成は Python プロジェクトディレクトリーに置かれるファイル |pyproject.toml| また
はファイル |hatch.toml| に指定する。前者を用いる場合、構成区画名は
:samp:`[tool.hatch.{xxxx}]` などのようになる。

当ノートでは |hatch.toml| に記述可能であるものは必ずそちらに記述するものとする。
文字列 ``tool.hatch`` を書かないぶん、区画名が若干短くなる。

.. todo::

   明示的に指定したい項目の構成例を挙げる。

使用方法・コツ
======================================================================

以下、ツールが出力する |pyproject.toml| の内容のうち、|hatch| しか認識しないもの
を |hatch.toml| に（適宜整形して）分離することにする。

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
   内蔵環境と呼ばれるものを出力する。重要なスクリプトを含む環境が揃っている。詳
   しくはビルドおよびテストの節で後述する。

プロジェクトに環境を新規作成する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

環境を定義するには |hatch.toml| に区画 :samp:`[envs.{env-name}]` を設け、そこに
環境 `env-name` を構成する属性を指定する。詳細を記述したら、適当な |hatch| コマ
ンドを実行することによりこの環境が成立する。

TBD: 属性一覧など？

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
   :caption: スクリプト定義例
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

----

.. todo::

   * 継承 ``type``, ``template``
   * ``detached``: インストールを省く
   * ``dependencies`` 後述
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

* 依存のインストールには |pip| が用いられる。
* プロジェクト依存と環境依存がある。

  * プロジェクトなら |pyproject.toml| ``[project]`` 直下の配列 ``dependencies``
  * 環境なら :samp:`envs.{env-name}` それぞれの直下の配列 ``dependencies``
  * プロジェクトには |pyproject.toml| ``[project.optional-dependencies]`` 区画と
    いうものを設けることが可能。内容は :samp:`{name} = [{...}]` の列だと考えられ
    る。この名前は環境区画にある配列 ``features`` が参照する？

* 依存関係は次に ``hatch shell`` や ``hatch run`` を実行したりするときにインス
  トールされる。

  * ``hatch shell`` はシェルが Bash なら :file:`.bashrc` を読み込むことに注意。
    ここで Python のパスを設定していようものなら混乱する。

* 配列 ``extra-dependencies`` は ``dependencies`` の内容をさらに追加するもの。用
  いるならば環境の継承時。

テスト
----------------------------------------------------------------------

* Hatch_ の既定構成では pytest_ を用いる（公式文書の default configuration の記
  述に依存が明記されている）。
* 実行はコマンド ``hatch test`` による。これは ``pytest tests`` に相当する。コマ
  ンドライン引数を指定すればそのまま |pytest| に渡されると考えられる。
* TODO: どの環境が採用されるのか？
* ``hatch test --all`` は互換な環境全てで実行
* オプション ``--include`` や ``--exclude`` で環境を指定
* ``hatch test --cover`` は ``coverage run -m pytest tests`` 相当を実行

ビルド
----------------------------------------------------------------------

* コマンド ``hatch build`` は構成 ``build.targets.sdist`` と
  ``build.targets.wheel`` それぞれに基づいた成果物をビルドする。
* コマンド :samp:`hatch build -t {target}` で個別ビルド。

リリース
----------------------------------------------------------------------

TODO: ``hatch publish``

頻出コマンド一覧
----------------------------------------------------------------------

TBW

不明 or 未定
----------------------------------------------------------------------

.. todo::

   * ``hatch new [OPTIONS] [NAME] [LOCATION]``
   * ``hatch new --init``: このレポジトリーでやってみるか？
   * ``dev-mode``
   * ``skip-install``
   * GitHub Actions ``pypa/hatch@install``
   * Miniconda との連携

   .. code:: console

      hatch run hatch-build:build-all # OK
      hatch run hatch-build:build-sdist # OK
      hatch run hatch-build:build-wheel # OK
      hatch run hatch-static-analysis:format-check # OK
      hatch run hatch-static-analysis:format-fix # OK
      hatch run hatch-static-analysis:lint-check # OK
      hatch run hatch-static-analysis:lint-fix # OK
      #hatch run hatch-test:cov-combine
      #hatch run hatch-test:cov-report
      #hatch run hatch-test:run
      #hatch run hatch-test:run-cov

資料集
======================================================================

Hatch_
   公式。キーボードでページをめくれるのは楽しい。

.. include:: /_include/python-refs-core.txt
.. _mypy: https://mypy.readthedocs.io/en/stable/
.. _Hatch: https://hatch.pypa.io/latest/
