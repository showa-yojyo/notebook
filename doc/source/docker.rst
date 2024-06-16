======================================================================
Docker 利用ノート
======================================================================

.. include:: /_include/kbd.txt
.. |Dockerfile| replace:: :file:`Dockerfile`

遅ればせながら Docker を習う。

.. contents:: 本章見出し
   :depth: 3
   :local:

手順
======================================================================

WSL2 Ubuntu 22.04.4 LTS に Docker Engine をインストールして学習を進める。Docker
Desktop は当面の間導入しないでおく。今のところ、その選択による不都合は ``docker
init`` が使えないくらいしかない。

.. contents::
   :depth: 1
   :local:

以前の Docker 環境の残滓を一掃する
----------------------------------------------------------------------

環境が完全にクリーンである場合にはここを飛ばしてインストール工程を読め。以前、何
かの Docker チュートリアルをやって上手くいかなかった場合にはこの工程が外せない。

`Install Docker Engine on Ubuntu
<https://docs.docker.com/engine/install/ubuntu/>`__ 文書内の Uninstall old
versions 節および Uninstall Docker Engine 節の記述に従い、ゴミを掃除する。

* 列挙されている非公式パッケージを ``sudo apt remove`` でアンインストールする。
* それ以外は ``suto apt purge`` でアンインストールする。
* :file:`/var/lib/docker/` および :file:`/var/lib/containerd` をディレクトリーご
  と削除する。

さらにユーザー設定ファイルも削除するべきだと考えられる。ディレクトリー
:file:`~/.docker` があれば、丸ごと削除する。後ほど XDG Base Directory 対応と同時
に設定ファイルを作り直す想定だ。

Docker Engine をインストールする
----------------------------------------------------------------------

同ページ内 Install using the :command:`apt` repository 節の記述に従う。

初めて Docker Engine をインストールする前に Docker リポジトリーを仕掛ける必要が
ある。著名なデータベース等のインストール手順と共通するコマンドが含まれており、慌
てることはない。急所は次の二つのファイルを準備することだ：

* :file:`/etc/apt/keyrings/docker.asc`
* :file:`/etc/apt/sources.list.d/docker.list`

それが済んだら ``sudo apt install docker-ce`` を実行。関連パッケージも同時にイン
ストール。

Docker の世界における Hello world は次のコマンドを実行することのようだ：

.. sourcecode:: console
   :caption: Docker Engine 動作確認コマンド

   $ sudo docker run hello-world

以上が完了すれば、チュートリアルをひたすら消化して Docker を体で覚える段階だ。

.. rubric:: もう一工夫

`Linux post-installation steps for Docker Engine
<https://docs.docker.com/engine/install/linux-postinstall/>`__ に記述されている
ことをいくつか実施しておくとよい。

* :command:`sudo` なしで Docker コマンドを実行可能にする
* :command:`systemd` を使って Docker を起動するように構成する
* ストレージを無駄にせぬようにログファイル出力を構成する（このノートで後述）

Docker Hub のアカウントを開設する
----------------------------------------------------------------------

すぐ後に述べる :ref:`anchor-docker-started` で初めて必要になるのが普通だと考えら
れる。GitHub と同様に、

* 無料アカウントを作成する
* 二因子認証を構成する

ところまで行えば十分だ。

チュートリアル実施を中心に Docker Docs を読む
----------------------------------------------------------------------

`Docker Docs`_ は Guides, Manuals, Reference の三本柱で成り立っている。Guides の
所々にチュートリアル記事が用意されている。これを重点的に実施する。その間に
Manuals と Reference の関連箇所を必要に応じて閲覧する。

Guides
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dockerを使い始め、開発工程を最適化する方法を学ぶのに有用な手引集。始めのほうの文
書群で Docker の基本的な考え方と工程を習得する。中盤の文書群は先進的な事項を追究
する。力がついたら Docker 社会主導の資料を見つけて、その発展に貢献する方法を習得
する。

.. contents::
   :depth: 1
   :local:

.. _anchor-docker-started:

Getting started
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Docker overview: ``docker run -i -t ubuntu /bin/bash`` を実行する。
* Get Docker Desktop: Docker Desktop はインストールしていないが、エンジンはした
  ので ``docker run -d -p 8080:80 docker/welcome-to-docker`` を実行する。
* Develop with containers: ``docker compose watch`` を中心にこの手のシステム開発
  の工程を察する。
* Build and push your first image: Docker Hub へのログインは端末ウィンドウからコ
  マンド ``docker login`` を実行することで代用。コマンド ``docker build``,
  ``docker image ls``, ``docker push`` などを実行する。

Docker concepts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Docker の基本的原理について理解を深める。

The basics
   Docker Docs の著者は Docker の基本をコンテナー、イメージ、レジストリー、
   Docker Compose だとみなしている。

   * What is a container?: ``docker/welcome-to-docker`` を開始してコマンド
     ``docker ps``, ``docker stop`` などを実行する。
   * What is an image?: コマンド ``docker search``, ``docker pull``, ``docker
     image ls``, ``docker image history`` などを実行する。
   * What is a registry?: Docker Hub にリポジトリーを作成し、コマンド ``docker
     build``, ``docker tag``, ``docker push`` 等を実行して成果物を登録する。
   * What is Docker Compose?: :file:`compose.yml`, ``docker compose up``,
     ``docker compose down``
Building images
   |Dockerfile|, ビルドキャッシュ、多段階構築により、最適化コンテナーイメージを
   作成する。

   * Understanding the image layers: ``docker container commit``, ``docker rm``
     等を実行。
   * Writing a Dockerfile: |Dockerfile| を作成する。
   * Build, tag, and publish an image: ``docker build``, ``docker image tag``,
     ``docker push`` 等を実行する。
   * Using the build cache: |Dockerfile| 最適化。ファイル :file:`.dockerignore`
     を作成。
   * Multi-stage builds: このチュートリアルを実施した記憶がない。
Running containers
   ポート公開、既定上書き、データ永続化、ファイル共有、複数コンテナーアプリケー
   ション管理など、必要不可欠な技法を習得する。

   * Publishing and exposing ports: オプション ``-p HOST_PORT:CONTAINER_PORT``,
     ``-P``, ファイル :file:`compose.yml` における ``ports`` リスト等。
   * Overriding container defaults: オプション ``-e VAR=VALUE``, 資源制限オプ
     ション ``--memory``, ``--cpus``, コマンド ``docker network create``,
     ``docker network ls`` 等。
   * Persisting container data: コマンド ``docker volume create``, オプション
     ``-v``, コマンド ``docker exec``, ``docker stop``, ``docker rm``, ``docker
     volume rm``, ``docker volume prune`` 等。
   * Sharing local files with containers: オプション ``--mount``, ファイル権限指
     示方法、等。
   * Multi-container applications: コマンド ``docker network create``, オプショ
     ン ``--network``, ``--network-alias`` 等。

Language-specific guides
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

どれか一つ、多くても二つを選んで演習すればいい。いずれのコースでも最後に
Minikube_ の出番がある。

Use-case guides
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Docker がプロジェクトや開発工程をどのように効率化できるかを確かめられる用例手引
集。

Machine learning & AI
   チュートリアルが豊富にあるものの、Docker 以外のところで環境が整わずに断念。
Data science with JupyterLab
   Docker と JupyterLab はデータ科学の作業工程を強化する強力なツールだという。こ
   れらを併用して、再現可能なデータ科学環境を作成および実行する。

   カスタマイズイメージを Docker Hub にプッシュしてそれを ``docker run`` するの
   が上手くいかない。
Suppress image vulnerabilities with VEX
   実験的らしいので急ぎなら飛ばす。途中で必要になる実行形式ファイルは
   :file:`vexctl-linux-amd64` だ。
Use containerized databases
   MySQL コンテナーをビルドして実行するチュートリアル。

Build with Docker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

この手引は Docker でソフトウェアをビルドするための入門書であると述べているので、
これを第一チュートリアルとしてもよい。

* Introduction: |Dockerfile|, コマンド ``docker build``, ``docker run``,
  ``docker exec``, ``docker stop`` を扱う。
* Layers: |Dockerfile| は記述順が重要ということを強調して述べている。
* Multi-stage: ``FROM`` を見たら多段構築と思え。
* Mounts: ``--mount``
* Build arguments: ``ARG`` と ``--build-arg``
* Export binaries: ``AS`` と ``--output``
* Test: ``AS`` と ``--target``
* Multi-platform: ``--platform`` ここはまだ。

Deployment and orchestration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

コンテナ化されたアプリケーションを管理、拡張、保守するためのツールをオーケストレ
イターと呼ぶ。最も人気のあるオーケストレイションツールは Kubernetes と Docker
Swarm の二つだ。Docker Desktop を使わない縛りを入れたので、本ノートでは
Kubernetes を有効にする方法に関しては Minikube_ の文書に従うことにする。

:command:`minikube` のインストールと構成の確認も行う。メモ：

.. sourcecode:: console
   :caption: 本書の手順前に :command:`minikube` で実行しておくべきコマンド

   $ minikube config set driver docker
   $ minikube start --driver=docker
   $ alias kubectl='minikube kubectl --'

* Deploy to Kubernetes: 次節のチュートリアル Part 2 まで終わったら実施可能。ただ
  し localhost:30001 でページが開かない。ポートが異なるから 404 エラーになるのは
  当然だと考えられるが違うのか？
* Deploy to Swarm: コマンド ``docker stack``, ``docker service`` 等。こちらも
  localhost:8000 でページが開かない（応答がない）。

Docker workshop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

この体験型講義では Docker の始め方を一手ずつ順番に説明するとある。これを第一
チュートリアルとしてもよい。

* Part 2: Containerize an application: |Dockerfile| を書いてコマンド ``docker
  build``, ``docker run``, ``docker ps`` 等を実行する。
* Part 3: Update the application: さらにコマンド ``docker stop``, ``docker rm``
  等を習う。
* Part 4: Share the application: Docker Hub アカウント開設後、コマンド ``docker
  login``, ``docker tag``, ``docker push`` 等を実行する。
* Part 5: Persist the DB: ``docker volume create``, ``--mount type=volume``,
  ``docker volume inspect`` 等。
* Part 6: Use bind mounts: ``--mount type=bind``, ``docker logs`` 等。
* Part 7: Multi-container apps: ``docker network create`` と MySQL とその他。
* Part 8: Use Docker Compose: :file:`compose.yaml` を作成してコマンド ``docker
  compose up`` を実行。コマンド ``docker compose down`` で破壊。

Educational resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Docker と Kubernetes の理解を深めるための資料集とある。

* `Live Debugging Node.js with Docker
  <https://training.play-with-docker.com/nodejs-live-debugging/>`__ は完走可能。
* `Docker CLI cheat sheet
  <https://docs.docker.com/get-started/docker_cheatsheet.pdf>`__ はペラ一枚。

Manuals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

説明書ではあるのだが、読者の理解を助けるためなのか、How to と Quickstart が挿ま
ることがあるのでそれらを取り組む。また、重要な記述を気づきしだい拾っていく。

.. contents::
   :depth: 1
   :local:

Get Docker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Docker Desktop を入手する方法が紹介されているが、生の Docker Engine を使いたいの
でページ下の方の囲み記事のリンク先なら確認する。

Docker Desktop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

この章はほとんど飛ばすことになるが、

WSL
   この節は読んでおいたほうがいい。

Docker Extensions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Docker Extensions を使えば Docker Desktop 内でサードパーティーのツールを使って機
能を拡張することができるというものだ。したがってこの章も飛ばす。

Docker Scout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Docker Scout はソフトウェア供給鎖の安全保障を強化する解法だ。イメージを分析する
ことで :abbr:`SBOM (Software Bill of Materials)` としても知られる部品の目録を作
成する。SBOM は継続的に更新される脆弱性データベースと照合され、保障上の弱点を突
き止める。

Quickstart
   実践的なチュートリアル。やるべきだ。
Install
   XDG Base Directory に従いたいので、スクリプト実行後にバイナリーを
   :command:`mv` する。スクリプトを修正してから実行するとなぜか上手くいかない。

Docker Engine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install
   Docker Engine を Linux にインストールする。Ubuntu の箇所を読む。

   * Install Docker Engine on Ubuntu: 前述のとおり、これをいの一番に実施する。
   * Linux post-installation steps for Docker Engine: :command:`sudo` を使わなく
     ても :command:`docker` を呼び出せるようにする支度等。
   * Troubleshoot Docker Engine installation: デーモン起動コマンドを確認する。
Networking
   コンテナーにおけるネットワークとは、コンテナー同士が互い接続して通信する機能
   等を指す。

   * Networking tutorials

     * Bridge network tutorial: ``docker network inspect``, ``docker container
       attach``, |Ctrl+P|, |Ctrl+Q|, ``docker network create``, ``docker network
       ls``, ``docker network connect``, ``docker network rm``
     * Host networking tutorial: ``--network host``, ``netstat -tulpn``
     * Overlay networking tutorial: 互いに通信可能な物理または仮想 Docker ホスト
       が三機必要。これらのホストがファイアウォールを介さずに同一ネットワーク上
       で動作していることを想定している。TODO: 後述の方法で演習する。
     * Macvlan network tutorial: 基本的なネットワーク知識がないと演習不能。具体
       的には ``--subnet``, ``--gateway`` の適切な引数を示せないようではダメだ。
CLI
   コマンド :command:`docker` についての手引集だ。

   * Use the Docker CLI: 重要な設定項目があるのでチェックする。
   * Completion: これは信じ難い。Bash の補完機能が :file:`~/.local/share` 以下を
     確認するというのか？
   * Filter commans: ``--filter KEY=VALUE`` を受け入れるコマンドを知るといい。
   * Format command and log output: これを読んで思った。Go 言語を学習するのがい
     い。
Manage resources
   今のところ削除コマンドが最重要項目であるので、それしか読んでいない。

   * Prune unused objects: チュートリアルではないが掃除コマンドが一覧になってい
     て重要だ。
Daemon
   手動でもシステム起動時にも起動できるようになる。

   * Start the daemon: WSL の設定が甘いと ``sudo systemctl start docker`` が失敗
     するはずだ。
   * Configure the daemon: 構成ファイルパスとコマンドライン例
   * Configure with systemd: TODO
   * Engine plugins

     * Managed plugin system: ``docker plugin install``, ``docker plugin ls``
Logs and metrics
   ログと何？

   * Container logs

     * Configure logging drivers: :file:`daemon.json` でログ出力を制御する。
     * Logging drivers

       * Local file logging driver: ``--log-driver local``
       * JSON File logging driver: ``--log-driver json-file``
   * Daemon logs: ``journalctl -xu docker.service``
   * Runtime metrics: ``docker stats``
   * Collect metrics with Prometheus: 例アリ
Security
   AppArmor, SELinux, GRSEC 等の適切な堅牢化システムを有効にすることで、Docker
   コンテナーの安全性を既定よりもさらに高めることができる。
Swarm mode
   Docker には swarm と呼ばれる Docker Engine の群れを管理する Swarm モードがあ
   る。Docker CLI を使用して swarm を作成し、アプリケーションサービスを swarm に
   配備し、swarm の動作を管理する。

   たぶん満足に学習できない。

   * Get started with swarm mode: チュートリアル

Docker build
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Building images
   TBD

   * Multi-platform images: ``docker buildx ls``, ``docker buildx create``
Drivers
   TBD

   * Kubernetes driver: 例アリ。Minikube_ を導入してから実施する。
   * Remote driver: 例アリ
Continuous integration
   TBW

   * GitHub Actions

     * Introduction: Docker GitHub Actions を設定して Docker イメージをビルドし、
       Docker Hub にプッシュするチュートリアルを含む。

Docker Compose
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install
   記憶がない
Quickstart
   |Dockerfile|, :file:`compose.yaml`, ``docker compose up``, ``docker compose
   down``, ``docker compose watch``, ``docker compose ps``, ``docker compose
   stop``
Sample apps with Compose
   外部リンク先にチュートリアルか？
Compose FAQs
   チラ見でいい

Docker Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create an account
   Docker をインストールしたらすぐに実行可能。
Quickstart
   アカウントを開設したらすぐに実行可能。

Administration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TODO

Reference
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

チュートリアルを全部こなしてから確かめることになる文書群。|Dockerfile| などの書
式仕様と CLI の説明書を確かめることが多い。後者に関して注目したいのは、文書が
:program:`docker` と ``docker compose`` とで別枠になっていることだ。

さらに修行する
----------------------------------------------------------------------

チュートリアルをやり続けたい場合はこのノート末尾に挙げる資料にある記事に行くとい
い。

構成ファイル
======================================================================

:file:`config.json`
----------------------------------------------------------------------

プログラム :program:`docker` 既定の構成ファイルパスは
:file:`~/.docker/config.json` だが、現代の感覚ではホームの直下にこのようなドット
ファイルを置くことを良しとしない。次のようにする：

#. 環境変数 ``XDG_CONFIG_HOME`` をシェルのスタートアップファイル (e.g.
   :file:`.bashrc`) で定義する
#. 環境変数 ``DOCKER_CONFIG`` をシェルのスタートアップファイルで定義する
#. コマンド ``mkdir -p $DOCKER_CONFIG`` を実行する
#. ファイル :file:`$DOCKER_CONFIG/config.json` を用意する

最初の変数については :doc:`/xdg` に記した。それ以降の適当な行に次を記せ：

.. sourcecode:: shell
   :caption: DOCKER_CONFIG を定義する

   export DOCKER_CONFIG=$XDG_CONFIG_HOME/docker

バージョン管理されている :file:`$XDG_CONFIG_HOME` に :file:`config.json` を置い
ておきながらなんだが、Docker に関係する構成ファイルには機密事項である各種認証情
報が含まれている可能性が高い。このようなものはバージョン管理のリポジトリーに登録
してはいけない。無視ファイル目録 (e.g. :file:`.gitignore`) を適宜設定しろ。

.. sourcecode:: json
   :caption: ファイル :file:`config.json` 例

   {
     "auths": {
       "https://index.docker.io/v1/": {
         "auth": "<SHA64>"
       }
     },
     "cliPluginsExtraDirs": [
       "<HOMEDIR>/.local/share/docker/cli-plugins"
     ],
     "plugins": {
       "docker-scout": {
         "organization": "<DOCKERID>"
       }
     }
   }

プロパティー ``auths`` は意味を正確に述べるのが難しい。機密情報であることを利用
者が認識する必要があることだけは忘れてはいけない。

プロパティー ``cliPluginsExtraDirs`` については Docker Scout の文書に記述がある。

プロパティー ``plugins`` は CLI プラグイン固有の設定だ。キーと値はプラグイン名と
そのプラグインに固有のオプションをそれぞれ表す。

:file:`daemon.json`
----------------------------------------------------------------------

プログラム :program:`dockerd` の構成ファイルの既定パスは
:file:`/etc/docker/daemon.json` だ。

.. sourcecode:: json
   :caption: ファイル :file:`/etc/docker/daemon.json` 例

   {
     "features": {
       "containerd-snapshotter": true
     },
     "log-driver": "local",
     "log-opts": {
       "max-size": "10m"
     }
   }

特に、演習段階のうちにログファイルが肥大化しない設定を済ませたい。`Configure
logging drivers
<https://docs.docker.com/config/containers/logging/configure/>`__ 内 Tip 記事に
よる。

構成ファイルの構文を検査することが可能だ：

.. sourcecode:: console
   :caption: 構成ファイルの構文を検査するコマンド

   $ dockerd --validate

基本コマンド
======================================================================

TBD

名言集
======================================================================

TBD

用語と術語と隠語
----------------------------------------------------------------------

資料
======================================================================

`Docker Docs`_
   一級資料。この文書群を丹念に読んで分析すれば入門者には十分だ。
`Docker Hub <https://hub.docker.com/>`__
   Docker イメージの物置サービス。GitHub と意味が似ている。
`Play with Docker Classroom <https://training.play-with-docker.com/>`__
   Docker Docs の補助教材として利用する。説明が詳細でありながら明瞭で気に入って
   いる。Hands On ページの右側コンソールを使わぬと試せない機能 (Swarm, etc.) が
   あり、押さえておくがよかろう。
Minikube_
   プログラム :program:`kubectl` を導入するためのパッケージ。導入は容易い。今の
   ところは Kubernetes に関係するチュートリアルを消化するために必要だから導入し
   たに過ぎない。

整理中
======================================================================

* Minikube_

.. _`Docker Docs`: https://docs.docker.com/
.. _Minikube: https://minikube.sigs.k8s.io/docs/
