================================================================================
Micromamba 利用ノート
================================================================================

.. |bashrc| replace:: :file:`.bashrc`
.. |mambarc| replace:: :file:`.mambarc`
.. |mamba| replace:: :program:`mamba`
.. |micromamba| replace:: :program:`micromamba`

.. contents:: 見出し
   :local:

概要
================================================================================

Python の仮想環境＆パッケージ管理には、これまで Miniconda, Mamba と使ってきた。
今は Micromamba_ を利用している。本稿では Micromamba の利用に関する考え方や手筋な
どを記す。

このノートを読み返すときに得られるようにしておく情報は次のとおり：

#. 必要なら古い Micromamba や、管理システムを環境ごとアンインストールする
#. Micromamba をインストールする
#. 所望の Python バージョンに対応する仮想環境を構築する
#. 仮想環境に所望のパッケージをインストールする

アンインストール手順
================================================================================

公式手順要旨：

* 命令 ``micromamba info`` を実行し、各種ディレクトリー、ファイルのパスを控えろ。
* シェルの開始 rc ファイルに埋め込んだ Micromamba 初期化コードを除去しろ。
* パスを控えておいたディレクトリー（仮想環境やキャッシュ）を削除しろ。
* Micromamba に対する構成ファイルを削除しろ。

ここに付け加えるなら、シェルの開始 rc ファイルに Micromamba に影響する環境変数を
定義している場合、それらを削除しろ。

インストール手順
================================================================================

公式手順は上記リンクのページ先頭付近から記述がある。

本体
--------------------------------------------------------------------------------

さまざまな方法があるが、私の WSL Ubuntu 環境では Homebrew を用いるのが最善だ。

.. sourcecode:: bash
   :caption: Homebrew による Micromamba インストール命令

   brew install micromamba

インストール直後では |micromamba| ならば実行可能かもしれない。

.. sourcecode:: console
   :caption: |micromamba| を鑑定

   $ type -a micromamba
   micromamba is /home/linuxbrew/.linuxbrew/bin/micromamba

最初の仮想環境を作るのは Micromamba 環境の基本構成が済んでからだ。

構成
================================================================================

Bash 開始ファイルに関連コードを追加する
--------------------------------------------------------------------------------

Bash 使用者おなじみの |bashrc| に |mamba| がシェルとうまく相互作用するためのコー
ドを命令 ``minimamba shell init`` を実行することで挿入する。

.. tip::

   オプション ``--dry-run`` を試せ。

素の追加コードは次のようなものだ：

.. sourcecode:: bash
   :caption: ``micromamba shell init`` が生成するコード例
   :force:

   # >>> mamba initialize >>>
   # !! Contents within this block are managed by 'mamba shell init' !!
   export MAMBA_EXE='/home/linuxbrew/.linuxbrew/Cellar/micromamba/2.10.0_2/bin/mamba';
   export MAMBA_ROOT_PREFIX='/home/USERNAME/.local/share/mamba';
   __mamba_setup="$("$MAMBA_EXE" shell hook --shell bash --root-prefix "$MAMBA_ROOT_PREFIX" 2> /dev/null)"
   if [ $? -eq 0 ]; then
       eval "$__mamba_setup"
   else
       alias mamba="$MAMBA_EXE"  # Fallback on help from mamba activate
   fi
   unset __mamba_setup
   # <<< mamba initialize <<<

このコードを次のように改造する：

* ``MAMBA_EXE`` の値を ``/home/linuxbrew/.linuxbrew/bin/mamba`` に変更する。
  これを行わないと、Homebrew で Micromamba 本体を更新するときに微妙なエラーが生
  じる。
* ``MAMBA_ROOT_PREFIX`` の値の一部を ``${XDG_DATA_HOME}`` で念のため置き換える。
* 念のため ShellCheck をかけて、うるさいようなら修正する。

ファイル |bashrc| を保存して Bash 対話セッションを再起動すると、特に、命令
``mamba activate`` と ``mamba deactiate`` が機能するようになる。

ユーザー構成ファイルパスを変更する
--------------------------------------------------------------------------------

Mamba から乗り換える場合は何も変更しなくていい。Miniconda から乗り換える場合は紛
らわしさを払拭するべく、工場出荷時設定から少し調整したい。

.. rubric:: 事前条件

* 環境変数 :envvar:`XDG_CONFIG_HOME` がいつものように設定されている

.. rubric:: 構成ファイルパス設定手順

ファイル |bashrc| に次の一行を追加する：

.. sourcecode:: bash
   :caption: ``MAMBARC`` 定義例

   export MAMBARC="$XDG_CONFIG_HOME/mamba/mambarc"

.. seealso::

   * :doc:`/xdg`

仮想環境を作成する
================================================================================

.. note::

   Micromamba の初期仮想環境は ``base`` だが、ここにおける :program:`python` は
   システムのそれを参照することに気をつけろ。

仮想環境を構築するには ``mamba create`` を実行する。仮想環境にはわかりやすい名前
をなるべくつけろ。安直でかまわない。例えば Python 3.15 が入手可能の最新版ならば
次のような手順が自然だ：

.. sourcecode:: console
   :caption: ``mamba create`` 実行例
   :force:

   mamba create -n python-3.15 "python==3.15"
   mamba activate python-3.15

仮想環境を作成したら、何かしらのパッケージをただちにインストールするのが普通だ。

利用するサードパーティー製パッケージがあらかじめ判明している場合には、仮想環境作
成命令行引数にパッケージ名を列挙すればよい。必要最低限に絞っておくのがコツだ：

.. sourcecode:: console
   :caption: 仮想環境 ``myenv`` を作成すると同時に Scrapy をインストールする
   :force:

   mamba create -n myenv scrapy "pyopenssl>=24"

Python パッケージを管理する
================================================================================

Python パッケージを管理するならば、先述の環境構成を終えてからだ。

仮想環境からパッケージをアンインストールする
--------------------------------------------------------------------------------

仮想環境 `myenv` から例えば Scrapy をアンインストールするには次のようにする：

.. sourcecode:: console
   :caption: ``mamba remove`` 命令行例
   :force:

   mamba remove -n myenv scrapy

このとき、Scrapy に依存する別のパッケージがあれば、それらも併せてアンインストー
ルされる。

パッケージを一度に複数アンインストールすることも可能。引数にパッケージ名を並べれ
ば良い。

すべてのインストール済みパッケージをアンインストールするならば、次のようにするの
がよい：

.. sourcecode:: console
   :caption: ``mamma remove --all`` 命令行例
   :force:

   mamba remove -n myenv --all

仮想環境にパッケージをインストールする
--------------------------------------------------------------------------------

仮想環境 `myenv` に例えば Scrapy をインストールしたいとする。次のようにしろ：

.. sourcecode:: console
   :caption: ``mamba install`` 実行例
   :force:

   mamba install -n myenv scrapy "pyopenssl>=24"

仮想環境におけるパッケージ一覧を示す
--------------------------------------------------------------------------------

仮想環境におけるパッケージ一覧を示すには命令 ``mamba list`` を使う。

:samp:`mamba list -n {myenv}`
   仮想環境 ``myenv`` にインストールしたパッケージすべてを確認する。
:samp:`mamba list -n {myenv} --export`
   命令 ``mamba create`` オプション ``--file`` の引数ファイルの内容として有効
   な書式で出力する。出力をファイルに保存しておき、後で新しい仮想環境を構築する
   ときの入力として使用することが可能だ。

仮想環境にあるパッケージを更新する
--------------------------------------------------------------------------------

パッケージを更新するには命令 ``mamba update`` を用いる。ここで言う更新とは、互換
性のある最新版に置き換えることを意味する。パッケージ名（一般には複数）を受け取
り、環境内の他のすべてのパッケージと互換性のあるバージョンをダウンロードして置き
換えるのだ。

最新版をインストールすることを達成するために、インストール済みのパッケージを更新
したり、他のパッケージを追加的にインストールしたりすることがある。

:samp:`mamba update -n {myenv} pyopenssl`
   パッケージ pyOpenSSL を更新する。仮想環境 `myenv` にインストールされているも
   のとする。
:samp:`mamba update -n {myenv} --all`
   パッケージすべてを更新する。パッケージ名を列挙する手間が省略できている。

パッケージを収蔵庫から検索する
--------------------------------------------------------------------------------

目当てのパッケージを検索するというより、その最新バージョンを確認するほうが主な目
的として命令 ``mamba search`` を実行する。

.. sourcecode:: console
   :caption: ``mamba search`` 実行例
   :force:

   mamba search 'python>=3.15'
   mamba search 'python[version=>=3.15]'

未使用パッケージやキャッシュを消去する
--------------------------------------------------------------------------------

命令 ``mamba clean`` は掃除操作に使う。仮想環境を指定しない。

``mamba clean --all``
   インデックスキャッシュ、ロックファイル、未使用のキャッシュパッケージ、tar
   ファイルを削除する。
``mamba clean --all --force-pkg-dirs``
   さらに書き込み可能なパッケージ込みで全てを消去する。

仮想環境を管理する
================================================================================

仮想環境を管理する場合、命令 ``mamba env`` の下位命令を実行することになる。

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   命令 @ 操作
   ``list``   @ 仮想環境一覧
   ``create`` @ 新規仮想環境を作成する
   ``export`` @ 仮想環境の構成パッケージ一覧
   ``remove`` @ 仮想環境を Micromamba 環境から削除する
   ``update`` @ 仮想環境を更新する
   ``config`` @ 仮想環境を構成する

命令例をいくつか挙げる：

``mamba env list``
   Micromamba が管理する仮想環境全てを一覧で示す。現在の仮想環境は ``Active`` 欄
   に米印が付く。
:samp:`mamba env export --name {ENV_NAME}`
   仮想環境の構成を YAML 形式で出力する。
:samp:`mamba env remove --name {ENV_NAME} --yes`
   仮想環境 `ENV_NAME` を Minimamba から削除する。
:samp:`mamba env update --name {ENV_NAME} --dry-run`
   仮想環境 `ENV_NAME` を更新するとどのパッケージが更新するかを確認する。

仮想環境を切り替える
================================================================================

仮想環境を指定して実行形式を走らせる
--------------------------------------------------------------------------------

他の仮想環境管理プログラムにも同等の機能があるように、命令 ``mamba run`` を使う
と、指定した仮想環境において指定した命令を走らせる。利点は ``activate`` と
``deactivate`` を前後に実行する手間が省けることだ。

:samp:`mamba run -n {MYENV} {COMMAND}`
   仮想環境 `MYENV` にあるものとして命令 `COMMAND` を実行させる。

現在の仮想環境を別のものに変更する
--------------------------------------------------------------------------------

命令 ``mamba activate`` を用いると、仮想環境を別のものに切り替えることになる。こ
の命令は他のものとは異なり、仮想環境をオプション ``--name`` ではなく実引数として
指定する。

:samp:`mamba activate {MYENV}`
   現在の仮想環境を `MYENV` に切り替える。
:samp:`mamba activate --stack {MYENV}`
  現在の仮想環境を `MYENV` に切り替える。次に ``deactivate`` を実行すると、仮想
  環境が ``activate`` 実行時の仮想環境に切り替わる。

現在の仮想環境を抜ける
--------------------------------------------------------------------------------

命令 ``mamba deactivate`` を実行すると、現在の仮想環境が原則的に ``base`` に切り
替わる（前節の ``--stack`` の記述を見ろ）。

Micromamba 自体を管理する
================================================================================

Micromamba 環境を構成する
--------------------------------------------------------------------------------

Micromamba 構成を管理する命令は ``mamba config`` だ。実際の動作としてはファイル
|mambarc| に記載した項目を操作する。

:samp:`mamba config list {ITEM ...}`
   項目に関する最終的な構成値を示す。引数が指定されていない場合は、設定値全てに
   関する情報を示す。
:samp:`mamba config describe {ITEM ...}`
   指定された設定項目について叙述する。引数が指定されていない場合は、すべての設
   定パラメータに関する情報を示す。
``mamba config sources``
   |mamba| が認識している構成ファイル全ての一覧を示す。

変更操作の例については割愛。

Micromamba の情報を確認する
--------------------------------------------------------------------------------

Micromamba 自体の情報を確認するには命令 ``mamba info`` を実行する。

``mamba info``
   目的に合わせてオプション ``--json`` を指定し、JSON 書式で出力することも考えろ。
``mamba info --base``
   仮想環境 ``base`` のルートディレクトリーパスしか示さない。
``mamba info --envs``
   仮想環境一覧。米印の付くものは現在の仮想環境を示す。

Micromamba 命令の共通事項
================================================================================

.. rubric:: CLI 定番オプション

``mamba --help``
   |mamba| の使用法を示す。命令一覧を確認可能。
:samp:`mamba {COMMAND} --help``
    命令 :samp:`mamba {COMMAND}` の用途、引数、オプションを示す。
``mamba --version``
   |mamba| のバージョンを示す。

.. rubric:: 構成オプション

|mamba| 全ての命令で次のオプション指定を受け付ける。

* オプション ``--rc-file`` *FILE ...* で |mamba| に読み込ませる構成ファイルを指
  定可能。
* オプション ``--no-rc`` を指定すると、構成ファイルを全く読み込ませない。
* オプション ``--no-env`` を指定すると、環境変数を全く参照させない。

.. rubric:: 共通オプション

これらのオプションを指定する場合、|mamba| 命令名の前までに置く必要がある：

* ``-v``/``--verbose``
* :samp:`--log-level {LEVEL}`
* ``-q``/``--quiet``
* ``-y``/``--yes``
* ``--json``
* ``--dry-run``

.. note::

   オプション ``--quiet`` と ``--json`` は ``--yes`` を含意する。

.. rubric:: パスや環境を指定するオプション

* ``-r`` / :samp:`--root-prefix {ROOT_PATH}`: ルートへのパスを指定
* ``-p`` / :samp:`--prefix {ENV_PATH}`: 仮想環境をパスで指定
* ``-n`` / :samp:`--name {ENV_NAME}`: 仮想環境を名前で指定

上のオプション二つは使わないと思う。オプション ``--name`` は頻繁に用いる。これら
のオプションを使わないときの採用値を確認するには命令 ``mamba info`` を実行する。

資料集
================================================================================

Mamba_
   Micromamba と Mamba 両方の公式文書。
`mamba-org/micromamba-releases <https://github.com/mamba-org/micromamba-releases>`__
   Micromamba GitHub リポジトリー。

.. include:: /_include/python-refs-core.txt
.. _Mamba:
.. _Micromamba: https://mamba.readthedocs.io/en/latest/
