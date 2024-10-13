======================================================================
Pipenv 利用ノート
======================================================================

.. |pip| replace:: :program:`pip`
.. |Pipfile| replace:: :file:`Pipfile`
.. |Pipfile.lock| replace:: :file:`Pipfile.lock`
.. |requirements.txt| replace:: :file:`requirements.txt`

.. contents:: 見出し一覧
   :local:

.. note::

   本記事の前提は次のとおり。

   :Python: 3.12.7
   :Shell: Bash 5.2.21(1)-release

   さらに次を加えておく：

   * Python 本体を含むパッケージ管理を Miniconda_ で行っている
   * 使用者は root でない

概要
======================================================================

Python を用いたプロジェクトに Pipenv_ を導入する手順と、よく用いるコマンドを記す。

Pipenv_ は pip_ と仮想環境を一括して管理する道具であり、Ruby 開発における
Bundler が処理するファイル群と類比するものを導入することで、|pip| が扱えないある
種のバージョン依存関係問題を解決することを目的とする。

導入
======================================================================

インストール
----------------------------------------------------------------------

公式文書の一般的指示とは異なる手順をとる。Miniconda_ を用いているので、次のよう
なコマンドで自分の Python_ 環境に Pipenv_ 本体を導入する：

.. sourcecode:: console
   :caption: Pipenv インストールコマンド例

   conda install conda-forge::pipenv

あらかじめコマンド ``conda search pipenv`` で最新版がどこにあるかを確認しておく
のもコツだ。

.. seealso::

   :doc:`/python-miniconda`

環境設定
----------------------------------------------------------------------

Pipenv_ はコマンドライン補完機能も備えている。これが使えると端末上でのタイピング
の手間が大幅に省けるので、早めに有効にしておきたい。

手順は公式文書の指示に従えばいい。自分の :file:`.bashrc` を編集して次の行を加え
る（インストールした直後ならば端末で直接実行）：

.. sourcecode:: bash
   :caption: Pipenv コマンドライン補完を動作させるコマンド

   eval "$(_PIPENV_COMPLETE=bash_source pipenv)"

コツとしては、テスト ``[ -x $(command -v pipenv) ]`` を入れるとよい。

仮想環境を作る
======================================================================

Python プロジェクトに対して Pipenv_ 仮想環境を用意する手順を述べる。仮想環境が
まったくないところから建造する場合と、Python 標準モジュール venv_ を使用して構築
された環境から Pipenv_ に移行する場合とが考えられる。双方とも説明する。

ゼロから創造する
----------------------------------------------------------------------

Python プロジェクトのディレクトリーを :file:`$PROJECT_DIR` と呼ぶ。仮想環境の初
期化と同時に、必要なサードパーティー製パッケージをインストールするのが標準的だ。
例えばパッケージ :samp:`SOME_PACKAGE` をインストールする場合にはこうする：

.. sourcecode:: console
   :caption: プロジェクトディレクトリーを Pipenv に認識させる

   $ cd $PROJECT_DIR
   $ pipenv install SOME_PACKAGE
   Creating a virtualenv for this project
   Pipfile: PROJECT_DIR/Pipfile
   Using default python from /path/to/python/python3.12
   3.12.7 to create virtualenv...
   （略）
   ✔ Success!
   Locking [dev-packages] dependencies...
   Updated Pipfile.lock!
   To activate this project's virtualenv, run pipenv shell.
   Alternatively, run a command inside the virtualenv with pipenv run.
   Installing dependencies from Pipfile.lock...

事後、次のようになる。

まず、:file:`$PROJECT_DIR` 直下にファイル |Pipfile| および |Pipfile.lock| が出力
される。これらは Ruby 開発でいう :file:`Gemfile` および :file:`Gemfile.lock` に
それぞれ対応する意味を有する。

そして、仮想環境を管理するディレクトリーが :file:`$PROJECT_DIR` 直下ではなく、お
そらく既定では :samp:`$XDG_DATA_HOME/virtualenvs/PROJECT_DIR-{xxxxxxxx}` のよう
なパスにある。

.. tip::

   管理ディレクトリーのパスはコマンド ``pipenv --venv`` を実行することで確かめら
   れる。

既存の環境から乗り換える
----------------------------------------------------------------------

前の説明と同じ名前を使うが、本節では Python 標準モジュール venv_ を使って仮想
環境が :file:`$PROJECT_DIR/.venv` で管理されているところに、今から Pipenv_ を使
うことにすることを仮定する。

普通は何らかのサードパーティー製パッケージが仮想環境にインストールしてあり、その
一覧を :file:`$PROJECT_DIR/requirements.txt` に記録してあるはずだ。この目録ファ
イルから Pipenv_ 仮想環境を構築することが可能だ。次のようにする：

.. sourcecode:: console
   :caption: 旧環境から ``pipenv install`` を実行して新環境を造る

   $ cd $PROJECT_DIR
   $ deactivate
   $ pipenv install -r ./requirements.txt
   Creating a Pipfile for this project...
   Requirements file provided! Importing into Pipfile...
   Pipfile.lock not found, creating...
   Locking [packages] dependencies...
   Building requirements...
   Resolving dependencies...
   ✔ Success!
   Locking [dev-packages] dependencies...
   Updated Pipfile.lock!
   To activate this project's virtualenv, run pipenv shell.
   Alternatively, run a command inside the virtualenv with pipenv run.
   Installing dependencies from Pipfile.lock...

.. tip::

   万が一ファイル |requirements.txt| がない場合には ``pip freeze`` を実行しろ。

紛れがないように旧環境を廃棄しておきたい：

.. sourcecode:: console
   :caption: 旧環境の管理ディレクトリーを廃棄する

   $ rm -rf .venv

.. important::

   これでプロジェクトに出入りするたびにコマンド ``source .venv/bin/activate`` や
   :program:`deactivate` を実行する習慣が廃止できた。

GitHub Actions などの CI/CD 環境が |requirements.txt| をまだ必要とする場合がある
ので、削除したいならばその点を確認してから行え。

仮想環境を作動させる
======================================================================

コマンド単発ならば :samp:`pipenv run {command}` を実行する。依存パッケージが備え
ているスクリプト実行や :program:`make` などの処理をラップ実行する。

実行したいコマンドが複数続く場合には ``pipenv shell`` を実行することで仮想環境に
「入る」ことになる。概念としては venv_ の ``source .venv/bin/activate`` に等し
い。このサブシェルで依存パッケージのスクリプトや :program:`make` を実行する。

|Pipfile| と |Pipfile.lock|
======================================================================

ファイル |Pipfile.lock| は :program:`pip` を用いる Python プロジェクトで使われて
いる |requirements.txt| を洗練させ、最後にロックされたパッケージのハッシュを追跡
するという安全保障上の改良点を加えたものだ。このコマンドを含むロック動作がこの
ファイルを管理する。

依存パッケージを更新する
======================================================================

パッケージ自体とパッケージ管理ファイルを混同しないように、関連コマンドをまとめて
おく：

``pipenv lock``
   ファイル |Pipfile.lock| を生成する。

   これはファイル |Pipfile| の内容に基づいて、|Pipfile.lock| の依存関係すべてを
   最新の解決済みバージョンに更新する。
``pipenv sync``
   |Pipfile.lock| で指定されたパッケージすべてを（依存関係を込めて）仮想環境にイ
   ンストールする。

   |Pipfile.lock| 自体を変更しない。
``pipenv update``
   指定された依存関係と部分依存関係に限って lock を更新する。パッケージをインス
   トールする。
``pipenv upgrade``
   指定された依存関係と部分依存関係に限って lock を更新する。パッケージをインス
   トールすることはしない。

GitHub Actions などの CI/CD 環境が |requirements.txt| を必要とする場合、次のよう
にしてパッケージ一覧を更新することが可能だ（オプションは好みで）：

.. sourcecode:: console
   :caption: Pipenv の情報から |requirements.txt| を更新する

   $ cd $PROJECT_DIR
   $ pipenv requirements --exclude-markers > requirements.txt

ロック
----------------------------------------------------------------------

GitHub Actions などの CI/CD において、次の Pipenv コマンドが実行されないように注
意しろ。これらは :file:`Pipfile.lock` を再構築する：

* ``lock``
* ``update``
* ``upgrade``
* ``uninstall``
* ``install``; ``install --deploy`` は可

操作集
======================================================================

先述のもの以外のコマンド :command:`pipenv` のコマンドラインでの実行例を挙げてい
く。以下、作業ディレクトリーパスはプロジェクトの |Pipfile| などが置かれているの
と同じとする。

サブコマンドなしの操作集
----------------------------------------------------------------------

``pipenv --where``
   このノートでいう :file:`$PROJECT_DIR` の完全パスを出力する。
``pipenv --venv``
   仮想環境を管理するディレクトリーパスを出力する。
``pipenv --envs``
   設定済みの Pipenv_ 環境変数を一覧する。環境変数については後述。
``pipenv --rm``
   仮想環境を消す。
``pipenv --man``
   :command:`pipenv` のマニュアルを出す。なぜか ``man pipenv`` ではダメだ。
``pipenv --support``
   GitHub Issues にバグを報告するときに添える情報を出力する。

仮想環境に依存パッケージを追加的にインストールする
----------------------------------------------------------------------

|Pipfile| と |Pipfile.lock| が生成されている仮想環境にさらなるパッケージを加える
には、インストールコマンドをパッケージを指定して実行する：

.. sourcecode:: console
   :caption: パッケージを追加的にインストールする例

   $ pipenv install ANOTHER_PACKAGE
   Installing ANOTHER_PACKAGE...
   Resolving ANOTHER_PACKAGE...
   Added ANOTHER_PACKAGE to Pipfile's [packages] ...
   ✔ Installation Succeeded
   （略）

依存パッケージ集合の依存関係を示す
----------------------------------------------------------------------

コマンド ``pipenv graph`` が基本形で、ここに出力オプションを指定する。

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   フラグ @ 出力
   ``--bare``      @ 最小（おそらく既定）で
   ``--json``      @ JSON で
   ``--json-tree`` @ JSON を入れ子の木で
   ``--reverse``   @ 依存関係を逆にしたグラフで

|Pipfile.lock| から依存パッケージのバージョン情報を直接見るのがわずらわしいので、
このコマンドを利用することでそれを見るということをしがちだ。

依存パッケージのモジュールをテキストエディターで開く
----------------------------------------------------------------------

コマンド ``pipenv open`` を実行すると、モジュール名を指定して Python ファイルを
開く機能がある。意外に便利である可能性がある。

.. sourcecode:: console
   :caption: コマンド ``pipenv open`` 実行例

   $ pipenv open sphinxcontrib.mermaid
   Opening '/path/to/.venv/lib/python3.12/site-packages/sphinxcontrib/mermaid.py' in your EDITOR.

仮想環境から現在未使用のパッケージを消去する
----------------------------------------------------------------------

依存パッケージのバージョン変更や追加削除を繰り返していると、なんらかのパッケージ
がいつの間にか不要になっている場合がある。それを片付けるにはコマンド ``pipenv
clean`` を用いる：

.. sourcecode:: console
   :caption: ``pipenv clean`` 実行例

   $ pipenv clean
   Uninstalling UNUSED_PACKAGE...

依存パッケージをアンインストールする
----------------------------------------------------------------------

依存パッケージをアンインストールするにはコマンド ``pipenv uninstall`` をパッケー
ジ名を指定して実行する。例えば：

.. sourcecode:: console
   :caption: 依存パッケージをアンインストールする例

   $ pipenv uninstall SOME_PACKAGE
   Removed SOME_PACKAGE from Pipfile.
   Building requirements...
   Resolving dependencies...
   ✔ Success!
   Uninstalling SOME_PACKAGE...
   Found existing installation: SOME_PACKAGE x.y.z
   Uninstalling SOME_PACKAGE-x.y.z:
     Successfully uninstalled SOME_PACKAGEa-x.y.z

構成
======================================================================

Pipenv はドットファイルから既定値を読み込むような設計ではないないらしい。ただし、
仮想環境に入るコマンド ``pip run`` と ``pip shell`` は、プロジェクトディレクト
リーにあるファイル :file:`.env` を :command:`source` する。

|Pipfile| の ``[scripts]`` 区画にコマンド定義しておくという手法があるが、ここで
は割愛する。

Pipenv は名前が ``PIPENV_`` から始まる独自の環境変数群を利用する。今のところ、こ
れを明示的に定義したいというものは見つからない（キャッシュパスも既定値が適切）。

運用
======================================================================

* |Pipfile| と |Pipfile.lock| の両方をプロジェクトのバージョン管理ファイル集合に
  加える。
* 作業場では定期的に ``pipenv update`` を行い、依存パッケージを最新に保つように
  努める。
* 依存パッケージを更新したことでプロジェクトのビルドが失敗する場合、
  |Pipfile.lock| を前のバージョンに復元して ``pip sync`` することで依存パッケー
  ジ群を復元可能。
* CI/CD のビルド工程では、ファイル |Pipfile.lock| を変更するようなコマンドを通常
  実行しない。

資料
======================================================================

`Pipenv documentation`_
   公式サイト。インストール方法から基本的な利用方法、応用等が文書化されている。
`venv — Creation of virtual environment`_
   Python 標準の仮想環境モジュール ``venv`` についての文書。このページの API 節
   の直前まで目を通せ。

.. _Python: https://www.python.org/
.. _Miniconda: https://docs.conda.io/en/latest/miniconda.html
.. _pip: https://pip.pypa.io/

.. _venv:
.. _venv — Creation of virtual environment:
   https://docs.python.org/3/library/venv.html

.. _Pipenv:
.. _Pipenv documentation:
   https://pipenv.pypa.io/en/latest/
