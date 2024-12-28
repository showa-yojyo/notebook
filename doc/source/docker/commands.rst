======================================================================
呪文集
======================================================================

.. include:: /_include/kbd.txt
.. include:: ./docker-inc.txt

プログラム :command:`docker` のコマンドラインを素早く組み立てるようになるのが目
標だ。

.. contents:: 本章見出し
   :depth: 2
   :local:

オプション
======================================================================

共通オプション
----------------------------------------------------------------------

ここでいう共通オプションとは、次のコマンド呼び出しの形式における
``[common-options]`` の部分に来るコマンドラインオプションのこととする。

.. sourcecode:: console
   :caption: Synopsys

   $ docker [common-options] <command> [command-options] <args>

.. option:: -v, --version=true|false

   :command:`docker` 自身のバージョン情報を出力して終了する。既定値は ``false``.

.. option:: --help

   引数なしで実行すると Docker コマンド一覧と共通オプションを出力して終了する。
   :samp:`docker {command} --help` の形式で実行すると Docker コマンドの使用方法
   を出力して終了する。

.. option:: --config=<path>

   Docker クライアント構成ファイル（の格納されているディレクトリー）パスを指定す
   る。既定値は :file:`~/.docker`.

.. option:: -D, --debug=true|false

   デバッグモードを有効にする。既定値は ``false``,

.. option:: -l, --log-level="debug|info|warn|error|fatal"

   ログ水準を指定する。既定値は ``info`` だ。

出力コマンドにおける頻出オプション
----------------------------------------------------------------------

コマンド :samp:`docker {command} ls` や :samp:`docker {command} inspect` などに
備わっているオプションをまとめておく。

.. option:: -a, --all

   「すべて」を意味する（コマンドによって集合が異なる）。

.. option:: --digests

   イメージにはダイジェストと呼ばれる content addressable な識別子がある。この値
   を出力するオプションだ。

.. option:: -f, --filter=<key>[=<value>]

   条件に基づいて指定を絞り込む。キー単体、またはキーと値の対で指定する。コマン
   ド一つでこのオプションを複数指定することが可能で、その場合にはすべての条件が
   真である対象が採用される。

   よく出てくる絞り込み名：

   * ``id``
   * ``label``
   * ``name``

   このオプションを使いこなせると手練れに見える。

.. option:: --format=<template>

   カスタムテンプレートを使って出力をフォーマットする。

   * ``table``: 列ヘッダー付きの表形式で出力する。
   * ``json``: JSON 形式で出力する。
   * ``TEMPLATE``: 指定された Go テンプレートを使って出力する。

.. option:: --no-trunc

   ID などの長い文字列を出力するときに切り捨てない。

.. option:: -q, --quiet

   ID しか出力しない。これを使ったコマンド出力を :samp:`docker {command} rm` の
   入力にする用途がある。

常用コマンド
======================================================================

私が利用したいコマンドライン群、「呪文表」を示す。チートシートとして参照に耐え得
るものを用意したい。また、ヘルプ出力による用途別分類を利用させてもらう。まずは常
用に区分されているコマンド集の名称を示す：

.. csv-table:: Docker CLI Common Commands
   :delim: @
   :header-rows: 1
   :widths: auto

   Command @ Description
   ``run``     @ Create and run a new container from an image
   ``exec``    @ Alias for ``container exec``
   ``ps``      @ Alias for ``container ls``
   ``build``   @ Build an image from a Dockerfile
   ``pull``    @ Alias for ``image pull``
   ``push``    @ Alias for ``image push``
   ``images``  @ Alias for ``image ls``
   ``login``   @ Log in to a registry
   ``logout``  @ Log out from a registry
   ``search``  @ Search Docker Hub for images
   ``version`` @ Show the Docker version information
   ``info``    @ Alias for ``system info``

.. _docker-run:

呪文表 ``run``
----------------------------------------------------------------------

コマンド ``run`` 実行時の基本動作は次のようなものだ：

#. Docker クライアントは指定のイメージをどうにかして見つけ、
#. そのコンテナー内部で指定コマンドを実行する。
#. その指定コマンドが終了するとコンテナーは終了する。

.. rubric:: 頻出オプション

.. option:: -name <container_name>, --name <container_name>

   コンテナー識別名を指定する。他のコマンド中にハッシュ値ではなくこの名前で参照
   することが可能になるという利点がある。

.. option:: -d, --detach

   バックグラウンドプロセスとしてコンテナーを稼働する（端末ウィンドウをブロック
   しない）。コンテナーは自身の実行に使用したルートプロセスが終了したときに終了
   する。ただし、``--rm`` オプションとともに ``-d`` を使用すると、コンテナーは自
   身かデーモンのどちらかが早い方の終了時に削除される。

.. option:: -i, --interactive

   コンテナーの標準入力を開いておき、それを通してコンテナーに入力を送ることがで
   きるようにする。

   コンテナーの入出力ストリームを擬似端末に束縛して、コンテナーの対話型端末セッ
   ションを作成するために ``--tty`` とともに使用されがちだ。次のオプション説明と
   合わせて理解する。

.. option:: -t, --tty

   コンテナーに擬似 TTY を取り付け、端末をコンテナーの入出力ストリームに接続す
   る。この割り当ては TTY デバイスが搭載する入出力機能とやりとりできることを意味
   する。

   本文ではパスワード入力を要求するコンテナーで ``--tty`` の意義を示している。

.. option:: --rm

   コンテナー終了時にそのファイルシステムを削除させる。短期間のフォアグランドプ
   ロセス実行時に指定しがちなオプションだ。

.. option:: -w <directory>, --workdir <directory>

   指定されたディレクトリー内でコマンドを実行する。パスが存在しない場合はコンテ
   ナー内に自動的に作成される。

.. option:: -p <port1>:<port2>, --publish <port1>:<port2>,

   コンテナーのポート ``<port2>`` をホストのポート ``<port1>`` に束縛する。

.. option:: -P, --publish-all

   すべての公開ポートをホストに公開する。Docker は各公開ポートをホスト上のランダ
   ムなポートに束縛する。

   |Dockerfile| の ``EXPOSE`` 指定や ``docker run`` の ``--expose`` オプションは
   公開フラグが明示的に付けられたポート番号しか公開しない。

.. option:: -v <dir1>:<dir2>, --volume <dir1>:<dir2>

   ホスト側ディレクトリー ``<dir1>`` をコンテナーの ``<dir2>`` にマウントする。

   バインドマウントされたボリュームのホストディレクトリーが存在しない場合、
   Docker が実行者に代わって ``<dir1>`` をホスト上に作成する。

   引数はコロンで区切られたフィールド三つで構成される。フィールドは正しい順序で
   並んでいなければならない。

   * 名前付きボリュームの場合、最初のフィールドはボリュームの名前で、指定された
     ホストマシン上で唯一無二だ。匿名ボリュームの場合、最初のフィールドは省略さ
     れる。
   * 二番目のフィールドは、ファイルまたはディレクトリーがコンテナにマウントされ
     るパスだ。
   * 三番目のフィールドは省略可能で、``ro`` などのオプションからなる CSV だ。

.. option:: --mount <mount>

   ボリュームやホストディレクトリーをコンテナー内にマウントする。「マウントす
   る」の意味はファイルシステム解説書を当たれ。

   このオプションは ``--volume`` が対応しているオプションのほとんどを対応するも
   のの、構文は異なる。

   本文で言われているように、``--volume`` よりも ``--mount`` を優先して使え。

   引数はカンマ区切りの :samp:`{key}={value}` で構成する。それらの順序は任意。有
   効なキーのうち重要なものを記すと：

   * ``type`` でマウントの型を指定する。このオプションでは ``bind`` 一択。
   * ``source`` でマウント元を指定する。バインドマウントの場合、Docker デーモン
     ホスト上のパスだ。
   * ``destination`` はコンテナー内でファイルやディレクトリーがマウントされてい
     るパスを指定する。
   * ``readonly`` オプションを指定すると、バインドマウントは読み取り専用としてコ
     ンテナーにマウントされる。これは値を書かずに済む。このオプションが使用可能
     である場合は指定するのが望ましい。

   .. admonition:: 利用者ノート

      UNIX の :program:`mount` のヘルプを読んでおくといいかもしれない。

.. option:: --network <network_name>

   コンテナーをネットワークに接続する。ネットワークは後述する関連コマンドでなん
   とかする。

.. option:: -e <varname[=value]>, --env <varname[=value]>

   稼働するコンテナー内部に対して環境変数を設定したり、コンテナーのイメージの
   |Dockerfile| で定義された変数を上書きしたりする。

.. option:: --env-file <file>

   環境変数をファイルからロードする。ファイルの書式は変数名と値の代入文が並ぶと
   いうものだ。

.. rubric:: 呪文例

``docker run alpine ls -l``
   コマンド ``ls -l`` を指定したので、Docker はディレクトリー一覧出力をコンテ
   ナー内で実行する。出力が終了するとコンテナーはシャットダウンする。

:samp:`docker run --name {<container_name>} {<image_name>}`
   イメージからコンテナーを生成、稼働する。コンテナーに独自の名前を与える。

:samp:`docker run -d {<image_name>}`
   コンテナーをバックグランドで稼働する。
``docker run -it --rm ubuntu bash``
   コンテナー ``ubuntu`` を端末ウィンドウから入出力を行えるように稼働して、終了
   時にそのファイルシステムを削除する。
``docker run -dt ubuntu sleep infinity``
   イメージ ``ubuntu`` に基づいて新しいコンテナーを作成し、バックグラウンドで実
   行し続けるために :command:`sleep` を実行する。

:samp:`docker run -p {<host_port>}:{<container_port>} {<image_name>}`
   実行元マシンに公開するポートを指定してコンテナーを稼働する。

``docker run -v $PWD:/test -w /test golangci/golangci-lint golangci-lint run``
   コマンドはコンテナー内の :file:`/test` ディレクトリーで実行するものとする。

``docker run -d -e POSTGRES_PASSWORD=secret -p 5434:5432 --network mynetwork postgres``
   Postgres コンテナーがバックグラウンドで起動し、ホストポート 5434 に写され、
   ネットワーク ``mynetwork`` に接続する。

``docker run -d -p 8080:80 nginx``
   ホストポート 8080 からコンテナーポート 80 へ写す。この状態でホスト端末から
   localhost:8080 へアクセスすると、コンテナーの 80 にアクセスしたことになる。
``docker run -p 80 nginx``
   ホストのいずれかのポートからコンテナーのポート 80 へ写す。
``docker run -P nginx``
   イメージによって設定されたすべてのポートを公開する。

``docker run --name=db -e POSTGRES_PASSWORD=secret -d -v postgres_data:/var/lib/postgresql/data postgres``
   ホスト側ディレクトリー ``postgres_data`` とコンテナー側ディレクトリー
   :file:`/var/lib/postgresql/data` にマウントして :command:`postgres` をバック
   グランウンドで稼働する。

``docker run -d -p 80:80 -v log-data:/logs docker/welcome-to-docker``
   コンテナが実行されると、:file:`/logs` ディレクトリーに書き込まれるすべての
   ファイルが、コンテナー外のこのボリューム ``log-data`` に保存される。コンテ
   ナーを削除し、同じボリュームを使用して新しいコンテナーを稼働してもファイルは
   そのまま残る。

``docker run --detach --publish 80:80 --name linux_tweet_app --mount type=bind,source="$(pwd)",target=/usr/share/nginx/html $DOCKERID/linux_tweet_app:1.0``
   マウント指定の例。

   * ``type=bind``: バインドマウントを適用し、
   * ``source="$(pwd)"``: ホスト側のコマンド実行時のディレクトリーから、
   * ``target=/usr/share/nginx/html``: コンテナー側の
     :file:`/usr/share/nginx/html` を利用可能にする。
:samp:`docker run --mount type=bind,source={HOST_PATH},target={CONTAINER_PATH},readonly nginx``
   マウント指定の例をもう一つ。バインドマウントを適用し、ホスト側の `HOST_PATH`
   からコンテナー側の :file:`/usr/share/nginx/html` を利用可能にする。かつ、パス
   にあるファイルを読み取りと専用する。

``docker run -d --name redis --network sample-app --network-alias redis redis``
   Redis コンテナーを起動し、先に作成したネットワーク ``sample-app`` に取り付け
   てネットワーク別名を作成する。DNS lookup に便利だ。

``docker run -e foo=bar postgres env``
   コンテナー内側での環境変数 ``foo`` を指定する。値は文字列 ``bar`` とする。
``docker run --env-file .env postgres env``
   環境変数の集合をファイル :file:`.env` で指定する。

.. rubric:: 少し高度なオプション例

``docker run --memory="512m" --cpus="0.5" postgres``
   コンテナーのメモリー使用量と CPU 枠を制限する。
:samp:`docker run -v {HOST-DIRECTORY}:{CONTAINER-DIRECTORY}:rw nginx`
   TODO: おそらく read-write モードの例

呪文表 ``exec``
----------------------------------------------------------------------

コマンド ``container exec`` の別名。:ref:`docker-container-exec` を参照しろ。

呪文表 ``ps``
----------------------------------------------------------------------

コマンド ``container ls`` の別名。:ref:`docker-container-ls` を参照しろ。

.. _docker-build:

呪文表 ``build``
----------------------------------------------------------------------

| :samp:`docker image build {[OPTIONS]} {PATH}`

|Dockerfile| と context からイメージをビルドするコマンドが ``docker build`` だ。
ビルドの context とは指定されたパスや URL にあるファイルの集合だ。ビルド過程はコ
context 内のどのファイルでも参照可能だ。例えば ``COPY`` 指令を使って参照する。

既定では ``docker build`` は context ルートにある |Dockerfile| を探す。

ほとんどの場合、|Dockerfile| を空ディレクトリーに置くのが最善だ。そのディレクト
リーにはビルドに必要なファイルしか追加しない。ビルドの性能を上げるには、そのディ
レクトリーに :file:`.dockerignore` を追加して、ファイルやディレクトリーを除外す
ることも可能だ。

.. rubric:: 頻出オプション

.. option:: -t <name>, --tag <name>

   ビルドするイメージに対して名前とオプションでタグを指定する。両者はコロンで区
   切る。このコマンドラインオプションを複数することも可能。

.. option:: -f <path>, --file <path>

   |Dockerfile| を指定する。レファレンスを見るとビルドターゲットに応じて
   |Dockerfile| を分けて用意する場合に有用であるようだ。

.. option:: --build-arg [<varname>=<value>]

   ビルド実行時変数を設定する。イメージをビルドするホストにより、変数を分けて定
   義したい。|Dockerfile| 内の ``ARG`` 指令にある変数に対して、このオプションを
   使ってビルド実行時に値を設定可能だ。

   ビルド引数それぞれに対して ``--build-arg`` を指定する必要がある。

   値を指定せずに使用する場合、デーモンはローカル環境からビルド中の Docker コン
   テナーに値を渡す。

.. option:: --target <stage>

   ビルドする対象ステージを指定する。

   複数のビルドステージを持つ |Dockerfile| でビルドする場合、このオプションを使
   用して、結果イメージの最終ステージとして中間ビルドステージを名前で指定可能
   だ。デーモンは対象ステージ以降のコマンドを実行しない。

   例えば |Dockerfile| に :samp:`FROM {base_image} AS {stage}` 指令がある場合、
   コマンド :samp:`docker build --target {stage} ...` が考えられる。

.. option:: -o <target>, --output <target>

   通常、ビルド結果からローカルコンテナーイメージを生成するのだが、このオプショ
   ンを指定すると、この動作を上書きしてカスタムエクスポーターを指定可能だ。カス
   これにより、ビルド結果を Docker イメージではなく、ローカルファイルシステム上
   のファイルとしてエクスポート可能だ。

   このオプションの引数の書式は CSV だ。

   このオプションは対象ステージからファイルすべてをエクスポートする。

.. option:: --platform <value[,value]>

   ビルドの対象プラットフォームを設定する。|Dockerfile| の中で ``--platform`` フ
   ラグを持たない ``FROM`` 指令はすべてこのプラットフォーム用のベースイメージを
   引いてくる。

   既定値はビルドを実行する BuildKit デーモンのプラットフォームだ。

.. option:: --progress <auto|plain|tty|rawjson>

   進捗出力の型を設定する。コンテナー出力を表示するには ``plain`` を指定する。

.. rubric:: 呪文例

``docker build .``
   イメージを構築する。Docker に |Dockerfile| を :file:`.` から参照させる。
:samp:`docker build -t {<image_name>}`
   |Dockerfile| からイメージを構築する。イメージ名は例えば ``hello:v0.1`` のよう
   な文字列で指定可。
:samp:`docker build -t {<image_name>} . --no-cache`
   キャッシュなしで |Dockerfile| からイメージを構築する。

``docker build --build-arg="GO_VERSION=1.19" .``
   |Dockerfile| に ``ARG`` 指令で宣言されている変数 ``GO_VERSION`` の値を
   ``1.19`` に定義してビルドする。
:samp:`docker build --build-arg HTTP_PROXY={url} .`
   ``HTTP_PROXY`` など、|Dockerfile| に記されずともあらかじめ存在するビルド変数
   がある。

``docker build --tag=buildme-client --target=client .``
   タグ ``buildme-client`` を付与してイメージ ``client`` をビルドする。
``docker build --target=client --progress=plain . 2> log1.txt``
   進捗をログファイル :file:`log1.txt` に出力する。
``docker build --output=. --target=server .``
   対象 ``server`` のファイルをホストファイルシステム上の現在の作業ディレクト
   リーにエクスポートする。

``docker build --target=server --platform=linux/arm/v7 .``
   Linux/ARM/v7 プラットフォーム用の ``server`` イメージを構築する。

``docker build -o out .``
   ビルドコンテキストを現在のディレクトリーとしてイメージをビルドする。そしてサ
   ブディレクトリー :file:`out` に成果物をエクスポートする。このサブディレクト
   リーは必要に応じて自動的に作成される。型オプションを省略した構文を ``-o`` オ
   プションで使用しているため、既定のエクスポーター local が用いられる。
``docker build --output type=local,dest=out .``
   上のコマンドと等価。
``docker build --output type=tar,dest=out.tar .``
   上のコマンドと同じ対象をビルドし、成果物ファイルを ``.tar`` アーカイブとして
   エクスポートする。

``docker build -t node-docker-image-test --progress=plain --no-cache --target test .``
   ``test`` ステージを対象として新しいイメージをビルドし、テスト結果を表示する。

   * ビルド出力を表示するのは ``--progress=plain`` による。
   * テストがつねに実行されるのは ``--no-cache`` による。
   * ``test`` ステージが対象であるのは ``--target test`` による。
``docker build --provenance=true --sbom=true --tag ORG/scout-demo-service:v1 --push .``
   認証オプション各種盛りの例。

   * ``--provenance=true`` で来歴証をすべて有効にする。
   * ``--sbom=true`` で ソフトウェア部品証をすべて有効にする。
   * ``--push`` でビルド結果を自動的にレジストリーに押す。

呪文表 ``pull``
----------------------------------------------------------------------

コマンド ``image pull`` の別名。:ref:`docker-image-pull` を参照しろ。

呪文表 ``push``
----------------------------------------------------------------------

コマンド ``image push`` の別名。:ref:`docker-image-push` を参照しろ。

呪文表 ``images``
----------------------------------------------------------------------

コマンド ``image ls`` の別名。:ref:`docker-image-ls` を参照しろ。

呪文表 ``login``
----------------------------------------------------------------------

レジストリー、普通は |DockerHub| にログインする。

:samp:`docker login -u {<username>}`
   使用者を指定して Docker にログインする。Password のプロンプトが表示される。こ
   れに適切な入力を与えればレジストリーとやり取り可能になる。
:samp:`docker login -u {<username>} -p {PASSWORD}`
   使用者とパスワードを両方指定してログインする。

.. todo::

   二因子認証の場合、ログアウトしてまたログインするときの対処法を記す。

呪文表 ``logout``
----------------------------------------------------------------------

レジストリーからログアウトする。

``docker logout``
   <https://registry-1.docker.io/> にある Docker の公開レジストリーからログアウ
   トする。
``docker logout localhost:8080``
   ローカルホストのレジストリーからログアウトする。

呪文表 ``search``
----------------------------------------------------------------------

:samp:`docker search {<image_name>}`
   イメージを |DockerHub| から検索する。
``docker search --filter=is-official=true Python``
   Python に関係するであろう、公式イメージを検索する。
:samp:`docker search --filter=stars=3 sql`
   SQL に関係するであろうイメージで、ランク 3 かそれ以上のものを検索する。

呪文表 ``version``
----------------------------------------------------------------------

``docker version``
   Docker バージョン情報を出力する。
``docker version --format '{{.Server.Version}}'``
   サーバーバージョンを出力する。

呪文表 ``info``
----------------------------------------------------------------------

コマンド ``system info`` の別名。:ref:`docker-system-info` を参照しろ。

運営コマンド
======================================================================

.. sourcecode:: text
   :caption: Docker CLI Management Commands

   builder     Manage builds
   buildx*     Docker Buildx
   checkpoint  Manage checkpoints
   compose*    Docker Compose
   container   Manage containers
   context     Manage contexts
   image       Manage images
   manifest    Manage Docker image manifests and manifest lists
   network     Manage networks
   plugin      Manage plugins
   scout*      Docker Scout
   system      Manage Docker
   trust       Manage trust on Docker images
   volume      Manage volumes

呪文表 ``builder``
----------------------------------------------------------------------

``docker builder prune -af``
   ビルドキャッシュを消去する。リビルドの直前に実行する。

呪文表 ``compose``
----------------------------------------------------------------------

マルチコンテナーアプリケーションの定義および実行に対するコマンドを構成する。

``docker compose down``
   コンテナーを完全に終了する。
``docker compose down --volumes``
   コンテナーを完全に終了する。ボリュームをも削除する。
``docker compose up``
   プロジェクトディレクトリーから実行することでアプリケーションを起動する。
``docker compose up -d``
   サービスをバックグラウンドで実行したい場合はオプション ``-d`` を加える。
``docker compose up -d --build``
   コンテナーを開始する前にイメージをビルドし、バックグラウンドでコンテナープロ
   セスを稼働する。
``docker compose watch``, ``docker compose up --watch``
   アプリケーションをビルドして稼働し、ファイル監視モードを開始する。
``docker compose ps``
   現在稼働中のコンテナー一覧を出力する。
``docker compose rm``
   停止サービスコンテナーを削除する。
``docker compose run server npm run test``
   コンテナー内のファイル :file:`package.json` からテストスクリプトを実行する。
``docker compose exec redis redis-cli monitor``
   サービス ``redis`` 内でコマンド ``redis-cli monitor`` を実行する。コマンドは
   既定で端末を割り当てるので、対話型のプロンプトが表示される。

呪文表 ``container``
----------------------------------------------------------------------

コンテナーを運営するためのコマンド。

.. sourcecode:: text
   :caption: Subcommands of ``docker container``

   attach      Attach local standard input, output, and error streams to a running container
   commit      Create a new image from a container's changes
   cp          Copy files/folders between a container and the local filesystem
   create      Create a new container
   diff        Inspect changes to files or directories on a container's filesystem
   exec        Execute a command in a running container
   export      Export a container's filesystem as a tar archive
   inspect     Display detailed information on one or more containers
   kill        Kill one or more running containers
   logs        Fetch the logs of a container
   ls          List containers
   pause       Pause all processes within one or more containers
   port        List port mappings or a specific mapping for the container
   prune       Remove all stopped containers
   rename      Rename a container
   restart     Restart one or more containers
   rm          Remove one or more containers
   run         Create and run a new container from an image
   start       Start one or more stopped containers
   stats       Display a live stream of container(s) resource usage statistics
   stop        Stop one or more running containers
   top         Display the running processes of a container
   unpause     Unpause all processes within one or more containers
   update      Update configuration of one or more containers
   wait        Block until one or more containers stop, then print their exit codes

呪文表 ``container commit``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| :samp:`docker container commit [{OPTIONS}] {<CONTAINER>} [{REPOSITORY}[:{TAG}]]`

コンテナーの変化からイメージを新規作成するコマンド。コンテナーのファイル変更や設
定を新しいイメージにコミットすると便利で、対話型シェルを実行してコンテナーをデ
バッグしたり、作業中のデータセットを別のサーバーにエクスポートしたりと、いろいろ
なことが可能になる。

別名 ``commit`` を使用可。

:samp:`docker commit {CONTAINER_ID}`
   差分をコミットする。
``docker commit -m "Add node" base-container node-base``
   コミットメッセージ "Add node" を与える。
``docker commit -c "CMD node app.js" -m "Add app" app-container sample-app``
   このコマンドは ``sample-app`` という新しいイメージを作成するだけでなく、
   |Dockerfile| に記述を追加することでコンテナー起動時の既定コマンドを ``node
   app.js`` に（追加的に？）設定する。

呪文表 ``container cp``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ホスト側ファイルシステムとコンテナー側のそれとでファイルをコピーする。

別名 ``cp`` を使用可。

``docker cp dvdrental.tar some-postgres:/tmp/dvdrental.tar``
   ホスト側作業ディレクトリーにある :file:`dvdrental.tar` をコンテナー
   ``some-postgres`` のディレクトリー :file:`/tmp` 直下に転送する。

呪文表 ``container diff``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コンテナのファイルシステム上のファイルやディレクトリーの変更を検査する。

別名 ``diff`` を使用可。

:samp:`docker diff {<container ID>}`
   これは説明を読むよりも実際に実行して出力を見るほうが理解が早い。適当なコンテ
   ナーを与えて試せ。稼働中である必要はない。

.. _docker-container-exec:

呪文表 ``container exec``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| :samp:`docker container exec [{OPTIONS}] <{CONTAINER}> <{COMMAND}> [{ARG...}]`

稼働中のコンテナーの中でコマンドを実行する。オプションは ``run`` と共通するもの
もある。

別名 ``exec`` を使用可。

:samp:`docker exec -it {<container_name>} {command}`
   稼働中のコンテナー `container_name` の内側で対話的に :command:`command` を実
   行する。
:samp:`docker exec {<container_id>} ls`
   稼働中のコンテナー `container_name` の内側で :command:`ls` を実行する。
``docker exec -it mydb sh``
   MySQL コンテナーである ``mydb`` 内に対話型シェル :program:`sh` が表示される。
``docker exec -it mydb mysql --user=root --password=$MYSQL_ROOT_PASSWORD --version``
   より実践的なコマンド。
``docker exec my-mysql mysql -u root -pmy-secret-pw -e "SELECT * FROM mydb.myothertable;"``
   実践的なコマンドその二。
``docker exec -it mariadbtest mariadb -p``
   MariaDB コンテナーで :program:`mariadb` シェルを実行する。

呪文表 ``container kill``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

稼働中のコンテナーにシグナルを送る。複数指定可。

:samp:`docker kill {container1} {container2}`
   コンテナー `container1`, `container2` を殺す。
:samp:`docker kill --signal=SIGHUP {container}`
   既定値は SIGKILL だが、シグナルをオプション ``--signal`` で指定することも可
   能。値によってはコンテナーが終了しないことに注意。

呪文表 ``container logs``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

別名 ``logs`` を使用可。

:samp:`docker logs -f {<container_name>}`
   コンテナーのログを取得、追跡する。
``docker logs -f --until=2s test``
   コンテナー ``test`` のログを二秒まで取得、追跡する。

   この例では時刻を相対的に指示している。絶対時刻指定も可能。

.. _docker-container-ls:

呪文表 ``container ls``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コンテナー一覧を示す。

別名 ``ps`` を使用可。

``docker ps``
   現在稼働中のコンテナーすべてを一覧する。稼働でないコンテナーは返されない。
``docker ps --all``
   稼働中でも停止中でも、コンテナーすべてを一覧する。
``docker ps --size``
   コンテナーそれぞれに対して、実消費量と仮想消費量の二つの容量を示す。仮想とあ
   るのは、コンテナーで使用される読み取り専用のイメージデータと、書き込み可能な
   レイヤーに使用されるディスク容量の和を表す。

``docker ps --filter "label=color=blue"``
   ラベル ``color`` が付いていて、かつその値が ``blue`` であるコンテナー一覧を出
   力する。値を問わない場合には ``=blue`` を指定しない。
``docker ps --filter "name=nostalgic"``
   名前に ``nostalgic`` を含むコンテナー一覧を出力する。
``docker ps -a --filter 'exited=0'``
   終了したコンテナー一覧を出力する。
``docker ps --filter ancestor=ubuntu``
   最新の ``ubuntu`` イメージを使用しているか、その子、孫、……、コンテナーの一覧
   を出力する。

.. sourcecode:: console
   :caption: ``docker ps --filter`` 用例

   $ docker ps -f before=<container>
   $ docker ps -f since=<container>
   $ docker ps -f volume=/data --format "table {{.ID}}\t{{.Mounts}}"
   $ docker ps -f publish=80
   $ docker ps -f expose=8000-8080/tcp

``docker ps --format "{{.ID}}: {{.Command}}"``
   ヘッダーのないテンプレートを使用し、稼働中のコンテナーすべてについて、コロン
   で区切りの ID とコマンドの登録項目を出力する。
``docker ps --format "table {{.ID}}\t{{.Labels}}"``
   稼働中のコンテナーすべてをラベルとともに表形式で一覧表示する。
``docker ps --format json``
   稼働中のコンテナーすべてを JSON 形式で一覧表示する。

また、オプション ``-q``, ``--quiet`` で ID のみを出力することを注意する。これは
コマンドパイプラインの先頭で使って ``docker rm`` に流すというような使い方があ
る。次節参照。

呪文表 ``container rm``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

別名 ``rm`` を使用可。

``docker rm $(docker ps --filter status=exited -q)``
   停止中のコンテナーすべてを削除する。
:samp:`docker rm -f {<container>}``
   コンテナーを稼働中であっても削除する。
:samp:`docker rm --volumes {<container>}`
   コンテナーを関連ボリュームすべてと共に削除する。ただし、名前が指定されていた
   ボリュームは削除しない。

呪文表 ``container run``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``run`` の別名。:ref:`docker-run` を参照しろ。

呪文表 ``container start``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

停止しているコンテナーを稼働する。

別名 ``start`` を使用可。

:samp:`docker start {<container>}`
   既存のコンテナーを開始する。

呪文表 ``container stats``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

別名 ``stats`` を使用可。

``docker stats``
   稼働中のコンテナーそれぞれに対する資源使用統計を標準出力に出力する。|Ctrl+C|
   で終了。
:samp:`docker stats {<container>}`
   特定のコンテナーに対する統計を出力する。
``docker stats nginx --no-stream --format "{{ json . }}"``
   コンテナー ``nginx`` の統計を JSON 形式で出力する。
``docker stats --all --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}" container``
   稼働中でも停止中でも、コンテナーすべてのそれぞれに対して、カスタマイズされた
   フォーマットで統計を表形式で出力する。

呪文表 ``container stop``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

別名 ``stop`` を使用可。

:samp:`docker stop {<container>}`
   既存のコンテナーを停止する。

呪文表 ``container top``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:samp:`docker container top {<container>}`
   コンテナー `<container>` の実行中プロセスを表示する。

呪文表 ``image``
----------------------------------------------------------------------

コマンド ``image`` はサブコマンドで構成されている：

.. sourcecode:: text
   :caption: Subcommands of ``docker image``

   build       Alias for ``build``
   history     Show the history of an image
   import      Import the contents from a tarball to create a filesystem image
   inspect     Display detailed information on one or more images
   load        Load an image from a tar archive or STDIN
   ls          List images
   prune       Remove unused images
   pull        Download an image from a registry
   push        Upload an image to a registry
   rm          Remove one or more images
   save        Save one or more images to a tar archive (streamed to STDOUT by default)
   tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE

呪文表 ``image build``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド ``build`` の別名。:ref:`docker-build` を参照しろ。

呪文表 ``image history``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

イメージがどのようにビルドされてきたのかという履歴を示すコマンドだ。

:samp:`docker image history {<image_name>}`
   イメージのレイヤー一覧を出力する。
``docker image history --no-trunc getting-started``
   オプション ``--no-trunc`` で完全な出力を得る。
``docker history --format "{{.ID}}: {{.CreatedSince}}" busybox``
   ヘッダーなしテンプレートを使い、``busybox`` イメージの ID と CreatedSince 登
   録項目をコロンで区切って出力する。

呪文表 ``image inspect``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

イメージの詳細情報を得る。

:samp:`docker image inspect {<image_name>}`
   書式指定なしの場合、JSON 形式で情報を出力する。
``docker image inspect --format "{{ json .RootFS.Layers }}" container``
   イメージ層の一覧を得る。SHA 値が羅列される。

.. _docker-image-ls:

呪文表 ``image ls``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| :samp:`docker image ls [{OPTIONS}] [{REPOSITORY}[:{TAG}]]`

別名 ``images`` を使用可。打鍵数が少ない方を選べ。

``docker images``
   システムにあるイメージすべての一覧を出力する。トップレベルのイメージすべて、
   そのリポジトリーとタグ、サイズを表示する。
``docker images java``
   リポジトリー ``java`` にあるイメージすべてを一覧表示する。
``docker images --no-trunc``
   完全 ID を一覧表示。
``docker images --filter "dangling=true"``
   タグなしイメージを一覧表示する。

   これに ``--quiet`` を加えた結果を ``docker rmi`` に渡す場合がある。

このコマンドもオプション ``--filter`` が使える。

.. sourcecode:: console
   :caption: Examples of ``docker images --filter``

   $ docker images --filter "label=com.example.version=1.0"
   $ docker images --filter "before=image1"
   $ docker images --filter "since=image3"
   $ docker images --filter=reference='busy*:*libc'

そしてオプション ``--format`` も使える。

.. sourcecode:: console
   :caption: Examples of ``docker images --format``

   $ docker images --format "{{.ID}}: {{.Repository}}"
   $ docker images --format "table {{.ID}}\t{{.Repository}}\t{{.Tag}}"
   $ docker images --format json

呪文表 ``image prune``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docker image prune``
   タグを持たず、子を持たないイメージすべてを削除する。
``docker image prune -a``
   さらに未参照イメージすべても削除する。
``docker image prune -a --force --filter "until=2017-01-04T00:00:00"``
   2017-01-04T00:00:00 以前に作成されたイメージを削除する。
``docker image prune -a --force --filter "until=240h"``
   十日以上前に作成されたイメージを削除する。

.. _docker-image-pull:

呪文表 ``image pull``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

別名 ``pull`` を利用可。

端末ウィンドウで実行中に |Ctrl+C| を押すなどして ``docker pull`` 操作を取り消せ
る。

:samp:`docker pull {image_name}`
   |DockerHub| から指定イメージを取得し、システムに保存する。イメージにタグが指
   定されていない場合、``latest`` タグを既定とする。

.. _docker-image-push:

呪文表 ``image push``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

別名 ``push`` を利用可。

これもコマンド実行中に |Ctrl+C| を押すと操作が取り消される。

:samp:`docker push {<username>}/{<image_name>}`
   イメージを |DockerHub| に押す。
``docker image push --all-tags registry-host:5000/myname/myimage``
   オプション ``--all-tags`` を付けて押すと、イメージ
   ``registry-host:5000/myname/myimage`` のタグすべてが押される。

呪文表 ``image rm``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ホストノードからイメージを削除したりタグを取ったりする。イメージにタグが複数ある
場合、タグを引数にしてこのコマンドを実行することでタグだけを削除する。タグが一つ
の場合はイメージとタグのどちらも削除することになる。

画像を参照しているタグが一つ以上ある場合は、イメージを削除する前にタグをすべて削
除する必要がある。

別名 ``rmi`` が打鍵量が最も少ない。

:samp:`docker rmi {<image_name>}`
   イメージを削除する。
:samp:`docker rmi -f {<image_id>}`
   指定された ID に一致するイメージのタグをすべて解除し、削除する。

呪文表 ``image tag``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| :samp:`docker image tag {SOURCE_IMAGE}[:{TAG}] {TARGET_IMAGE}[:{TAG}]`

|DockerHub| などにイメージを押すために、名前とタグを用いてイメージをグループ化す
るためのコマンドだ。タグを指定しないと既定名 ``latest`` が採用される。

別名 ``tag`` を使用可。

:samp:`docker tag {<image_id>} {<image_name>}`
   イメージにラベルを付けてバージョン管理することができる。
``docker tag my-username/my-image another-username/another-image:v1``
   イメージに別のタグを追加できる。
``docker tag 0e5574283393 fedora/httpd:version1.0``
   ローカルイメージ 0e5574283393 に ``fedora/httpd`` としてタグ ``version1.0``
   を付ける。
``docker tag httpd fedora/httpd:version1.0``
   ローカルイメージ ``httpd`` にタグ ``version1.0`` 付き名前 ``fedora/httpd`` を
   付ける。
``docker tag httpd:test fedora/httpd:version1.0.test``
   ローカルイメージ ``httpd:test`` に以下同文。上のコマンドの対象イメージは実際
   には ``httpd:latest`` であることに注意しろ。
``docker tag 0e5574283393 myregistryhost:5000/fedora/httpd:version1.0``
   公衆レジストリーではなく、私設レジストリーにイメージを押すには、レジストリー
   のホスト名と、必要ならばポートをも指定する。

呪文表 ``network``
----------------------------------------------------------------------

.. csv-table:: Subcommands of ``docker network``
   :delim: @
   :header-rows: 1
   :widths: auto

   Command @ Description
   ``connect``    @ Connect a container to a network
   ``create``     @ Create a network
   ``disconnect`` @ Disconnect a container from a network
   ``inspect``    @ Display detailed information on one or more networks
   ``ls``         @ List networks
   ``prune``      @ Remove all unused networks
   ``rm``         @ Remove one or more networks

呪文表 ``network create``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: 利用者ノート

   このコマンドは難しいので習得を諦める。

``docker network create mynetwork``
   カスタムネットワークを新規作成する。

呪文表 ``network inspect``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ネットワークに関する情報を出力する。既定ではこのコマンドは結果を JSON 形式で表示
する。

``docker network inspect``
   コンテナーがネットワークに接続されているかどうかを確認できる。
``docker network inspect bridge``
   ``bridge`` と呼ばれるネットワークの詳細を表示する。

このコマンドでもオプション ``--format`` が使える。

呪文表 ``network ls``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docker network ls``
   現在の Docker ホスト上の既存のコンテナーネットワークを表示する。既存というの
   は、デーモンが知っているネットワークすべてということだ。クラスター内のホスト
   複数にまたがるネットワークも含む。
``docker network ls --no-trunc``
   ID を切り捨てずに出力する。

``docker network ls --filter driver=bridge``
   ネットワークドライバーが ``bridge`` と合致するものを一覧する。
``docker network ls --filter id=95e74588f40d``
   ID を指定して一覧する。存在さえすれば、ID の部分だけを指定して通じる。
``docker network ls -f "label=usage"``
   ラベルフィルターはラベルと値の存在に基づいてネットワークを一覧する。ラベル
   ``usage`` を持つネットワークを一覧する。その値は何でもかまわない。
``docker network ls -f "label=usage=prod"``
   これは値の合致まで求める。
``docker network ls --filter name=foo``
   名前に ``foo`` を含むネットワークを一覧する。
``docker network ls --filter type=custom -q``
   使用者定義のネットワークすべての ID を出力する。これを ``docker network rm``
   の入力としてネットワークを一掃する場合がある。

オプション ``--format`` がある。

.. sourcecode:: console
   :caption: Examples of ``docker network ls --format``

   $ docker network ls --format "{{.ID}}: {{.Driver}}"``
   $ docker network ls --format json``

呪文表 ``network rm``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ネットワークを削除するコマンドだが、ネットワークを削除するには、まずそのネット
ワークに接続しているコンテナーをすべて切断する必要がある。

:samp:`docker network rm {<network>}`
   ネットワークを削除する。
``docker network rm 3695c422697f my-network``
   一度の実行で複数削除する。どれか削除に失敗しても残りのネットワークの削除を試
   みる。

呪文表 ``scout``
----------------------------------------------------------------------

これは高級なコマンドなので後回しとする。

``docker scout repo enable ORG/scout-demo-service``
   リポジトリー上で Docker Scout を有効にする。
``docker scout cves --only-cve-id CVE-2022-24999``
   イメージの脆弱性を表示する。CVE-2022-24999 という CVE を確認する。
``docker scout cves --only-cve-id CVE-2022-24999 --vex-location .``
   ``--vex-location`` フラグを使うと VEX 文書を含むディレクトリーを指定できる。

.. docker scout attestation add \
..   --file in-toto.vex.json \
..   --predicate-type https://openvex.dev/ns/v0.2.0 \
..   ORG/scout-demo-service:v1

.. docker scout cves \
..   --only-cve-id CVE-2022-24999 \
..   registry://ORG/scout-demo-service:v1

呪文表 ``system``
----------------------------------------------------------------------

.. sourcecode:: text
   :caption: Subcommands of ``docker system``

   df          Show docker disk usage
   events      Get real time events from the server
   info        Display system-wide information
   prune       Remove unused data

.. _docker-system-info:

呪文表 ``system info``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

システム全体の情報を得るコマンド。

別名 ``info`` を使用可。

``docker info``
   システム全体の情報を表示する。
``docker info --format '{{json .}}'``
   それを JSON 書式で出力する。

呪文表 ``volume``
----------------------------------------------------------------------

.. csv-table:: Subcommands of ``docker volume``
   :delim: @
   :header-rows: 1
   :widths: auto

   ``create``  @ Create a volume
   ``inspect`` @ Display detailed information on one or more volumes
   ``ls``      @ List volumes
   ``prune``   @ Remove unused local volumes
   ``rm``      @ Remove one or more volumes
   ``update``  @ Update a volume (cluster volumes only)

呪文表 ``volume create``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docker volume create log-data``
   ``log-data`` という名前のボリュームを作成する。後続する ``docker run`` コマン
   ドに :samp:`-v log-data:{path}` の形の引数を与えて実行する。

呪文表 ``volume inspect``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:samp:`docker volume inspect {<volume>}``
   データをどこに保存しているのかなど、ボリュームの構成を出力する。

呪文表 ``volume ls``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docker volume ls``
   ボリュームすべてを一覧する。
``docker volume ls -f dangling=true``
   どのコンテナーからも参照されていないボリュームを一覧する。
``docker volume ls -f driver=local``
   ドライバー ``local`` で作成されたボリュームを一覧する。
``docker volume ls --filter label=is-timelord``
   ラベル ``is-timelord`` を有するボリュームを一覧する。値は何でもかまわない。
``docker volume ls --filter label=is-timelord=yes``
   ラベル ``is-timelord`` を有し、かつ値が ``yes`` に合致するボリュームを一覧す
   る。
``docker volume ls -f name=rose``
   名前に指定文字列を含むボリュームを一覧する例。

例によってオプション ``--format`` が備わっている。

呪文表 ``volume prune``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docker volume prune``
   未使用の（どのコンテナーにも付属していない）ボリュームすべてを削除する。匿名
   ボリュームのみ。
``docker volume prune -a``
   匿名ボリュームも込めてすべて削除する。

オプション ``--filter`` が備わっている。

呪文表 ``volume rm``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:samp:`docker volume rm {<volume-name-or-id>}`
   ボリュームを削除する。ボリュームがどのコンテナーにも付属していない場合にのみ
   機能する。ボリュームを削除する前にそれをコンテナーから取り外す必要がある。

Swarm コマンド
======================================================================

.. sourcecode:: text
   :caption: Docker CLI Management Commands

   config      Manage Swarm configs
   node        Manage Swarm nodes
   secret      Manage Swarm secrets
   service     Manage Swarm services
   stack       Manage Swarm stacks
   swarm       Manage Swarm

.. admonition:: 利用者ノート

   高度なコマンドゆえ、基本ができてからの後回しにする。

無印コマンド
======================================================================

ほとんどは別のコマンドの別名であり、おそらく打鍵効率の便宜上設けられているものと
考えられる。実際、環境変数 :envvar:`DOCKER_HIDE_LEGACY_COMMANDS` を設定しておく
とコマンド ``docker --help`` などの出力から下記の一覧出力が省かれる。

.. csv-table:: Docker CLI Commands
   :delim: @
   :header-rows: 1
   :widths: auto

   Command @ Description
   ``attach``  @ Alias for ``container attach``
   ``commit``  @ Alias for ``container commit``
   ``cp``      @ Alias for ``container cp``
   ``create``  @ Alias for ``container create``
   ``diff``    @ Alias for ``container diff``
   ``events``  @ Alias for ``system events``
   ``exec``    @ Alias for ``container exec``
   ``export``  @ Alias for ``container export``
   ``history`` @ Alias for ``image history``
   ``import``  @ Alias for ``image import``
   ``inspect`` @ Return low-level information on Docker objects
   ``kill``    @ Alias for ``container kill``
   ``load``    @ Alias for ``image load``
   ``logs``    @ Alias for ``container logs``
   ``pause``   @ Alias for ``container pause``
   ``port``    @ Alias for ``container port``
   ``rename``  @ Alias for ``container rename``
   ``restart`` @ Alias for ``container restart``
   ``rm``      @ Alias for ``container rm``
   ``rmi``     @ Alias for ``image rm``
   ``save``    @ Alias for ``image save``
   ``start``   @ Alias for ``container start``
   ``stats``   @ Alias for ``container stats``
   ``stop``    @ Alias for ``container stop``
   ``tag``     @ Alias for ``image tag``
   ``top``     @ Alias for ``container top``
   ``unpause`` @ Alias for ``container unpause``
   ``update``  @ Alias for ``container update``
   ``wait``    @ Alias for ``container wait``

呪文表 ``inspect``
----------------------------------------------------------------------

Docker オブジェクトの低水準情報を出力するコマンド。通常は JSON 形式で出力する。

:samp:`docker inspect {<container>}`
   稼働中のコンテナーを検査する。
``docker inspect --type=volume myvolume``
   名前が ``myvolume`` であるボリュームの情報を出力する。
``docker inspect --size mycontainer``
   コンテナー専用オプション。

このコマンドはオプション ``--format`` が備わっている。かなり簡単な方法で任意の
フィールドを JSON から引き出すことができる。

:samp:`docker inspect --format='\\{\\{range .NetworkSettings.Networks\\}\\}\\{\\{.IPAddress\\}\\}\\{\\{end\\}\\}' {<INSTANCE>}`
   IP アドレスを出力する。
``docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mariadbtest``
   その例。MariaDB コンテナーの IP アドレスを得る。
:samp:`docker inspect --format='\\{\\{range .NetworkSettings.Networks\\}\\}\\{\\{.MacAddress\\}\\}\\{\\{end\\}\\}' {<INSTANCE>}`
   MAC アドレスを出力する。
:samp:`docker inspect --format='\\{\\{.LogPath\\}\\}' {<INSTANCE>}`
   ログパスを出力する。
