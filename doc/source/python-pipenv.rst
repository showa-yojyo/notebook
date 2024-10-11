======================================================================
Pipenv 利用ノート
======================================================================

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

.. todo::

   TBW

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
まったくないところから建造する場合と、Python 標準モジュール ``venv`` を使用して
構築された環境から Pipenv_ に移行する場合とが考えられる。双方とも説明する。

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

まず、:file:`$PROJECT_DIR` 直下にテキストファイル :file:`Pipfile` および
:file:`Pipfile.lock` が出力される。これらは Ruby 開発でいう :file:`Gemfile` およ
び :file:`Gemfile.lock` にそれぞれ対応する意味を有する。

そして、仮想環境を管理するディレクトリーが :file:`$PROJECT_DIR` 直下ではなく、お
そらく既定では :samp:`$XDG_DATA_HOME/virtualenvs/PROJECT_DIR-{xxxxxxxx}` のよう
なパスにある。

.. tip::

   管理ディレクトリーのパスはコマンド ``pipenv --venv`` を実行することで確かめら
   れる。

既存の環境から乗り換える
----------------------------------------------------------------------

前の説明と同じ名前を使うが、本節では Python 標準モジュール ``venv`` を使って仮想
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

   万が一ファイル :file:`requirements.txt` がない場合には ``pip freeze`` を実行
   しろ。

紛れがないように旧環境を廃棄しておきたい：

.. sourcecode:: console
   :caption: 旧環境の管理ディレクトリーを廃棄する

   $ rm -rf .venv

GitHub Actions などの CI/CD 環境が :file:`requirements.txt` を必要とする場合があ
るので、削除したいならばその点を確認してから行え。

仮想環境にあるパッケージを更新する
======================================================================

.. todo::

   ``pip update`` 関連のメモ

GitHub Actions などの CI/CD 環境が :file:`requirements.txt` を必要とする場合、次
のようにしてパッケージ一覧を更新することが可能だ（オプションは好みで）：

.. sourcecode:: console
   :caption: Pipenv の情報から :file:`requirements.txt` を更新する

   $ pipenv requirements --exclude-markers > requirements.txt

操作集
======================================================================

.. todo::

   インストールと更新以外のコマンド事例集

資料
======================================================================

`Pipenv documentation`_
   公式サイト。インストール方法から基本的な利用方法、応用等が文書化されている。

.. _Python: https://www.python.org/
.. _Miniconda: https://docs.conda.io/en/latest/miniconda.html
.. _pip: https://pip.pypa.io/

.. _Pipenv:
.. _Pipenv documentation:
   https://pipenv.pypa.io/en/latest/

