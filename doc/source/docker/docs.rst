======================================================================
Docker Docs 読書ノート
======================================================================

.. include:: /_include/kbd.txt
.. include:: ./docker-inc.txt

|DockerDocs| は Guides, Manuals, Reference の三本柱で成り立っている。Guides の
所々にチュートリアル記事が用意されている。これを重点的に実施する。その間に
Manuals と Reference の関連箇所を必要に応じて閲覧する。

.. contents:: 本章見出し
   :depth: 3
   :local:

Guides
======================================================================

Dockerを使い始め、開発工程を最適化する方法を学ぶのに有用な手引集。始めのほうの文
書群で Docker の基本的な考え方と工程を習得する。中盤の文書群は先進的な事項を追究
する。力がついたら Docker 社会主導の資料を見つけて、その発展に貢献する方法を習得
する。

.. _anchor-docker-started:

Getting started
----------------------------------------------------------------------

* Docker overview: ``docker run -i -t ubuntu /bin/bash`` を実行する。
* Get Docker Desktop: Docker Desktop はインストールしていないが、エンジンはした
  ので ``docker run -d -p 8080:80 docker/welcome-to-docker`` を実行する。
* Develop with containers: ``docker compose watch`` を中心にこの手のシステム開発
  の工程を察する。
* Build and push your first image: |DockerHub| へのログインは端末ウィンドウから
  コマンド ``docker login`` を実行することで代用。コマンド ``docker build``,
  ``docker image ls``, ``docker push`` などを実行する。

Docker concepts
----------------------------------------------------------------------

Docker の基本的原理について理解を深める。

The basics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|DockerDocs| の著者は Docker の基本をコンテナー、イメージ、レジストリー、 Docker
Compose だとみなしている。

* What is a container?: ``docker/welcome-to-docker`` を開始してコマンド
  ``docker ps``, ``docker stop`` などを実行する。
* What is an image?: コマンド ``docker search``, ``docker pull``, ``docker
  image ls``, ``docker image history`` などを実行する。
* What is a registry?: |DockerHub| にリポジトリーを作成し、コマンド ``docker
  build``, ``docker tag``, ``docker push`` 等を実行して成果物を登録する。
* What is Docker Compose?: :file:`compose.yml`, ``docker compose up``,
  ``docker compose down``

Building images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|Dockerfile|, ビルドキャッシュ、多段階構築により、最適化コンテナーイメージを作成
する。

* Understanding the image layers: ``docker container commit``, ``docker rm`` 等
  を実行。
* Writing a Dockerfile: |Dockerfile| を作成する。
* Build, tag, and publish an image: ``docker build``, ``docker image tag``,
  ``docker push`` 等を実行する。
* Using the build cache: |Dockerfile| 最適化。ファイル :file:`.dockerignore` を
  作成。
* Multi-stage builds: このチュートリアルを実施した記憶がない。

Running containers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ポート公開、既定上書き、データ永続化、ファイル共有、複数コンテナーアプリケーショ
ン管理など、必要不可欠な技法を習得する。

* Publishing and exposing ports: オプション ``-p HOST_PORT:CONTAINER_PORT``,
  ``-P``, ファイル :file:`compose.yml` における ``ports`` リスト等。
* Overriding container defaults: オプション ``-e VAR=VALUE``, 資源制限オプション
  ``--memory``, ``--cpus``, コマンド ``docker network create``, ``docker network
  ls`` 等。
* Persisting container data: コマンド ``docker volume create``, オプション
  ``-v``, コマンド ``docker exec``, ``docker stop``, ``docker rm``, ``docker
  volume rm``, ``docker volume prune`` 等。
* Sharing local files with containers: オプション ``--mount``, ファイル権限指示
  方法、等。
* Multi-container applications: コマンド ``docker network create``, オプション
  ``--network``, ``--network-alias`` 等。

Language-specific guides
----------------------------------------------------------------------

どれか一つ、多くても二つを選んで演習すればいい。いずれのコースでも最後に
Minikube_ の出番がある。

Use-case guides
----------------------------------------------------------------------

Docker がプロジェクトや開発工程をどのように効率化できるかを確かめられる用例手引
集。

Machine learning & AI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

チュートリアルが豊富にあるものの、Docker 以外のところで環境が整わずに断念。

Data science with JupyterLab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Docker と JupyterLab はデータ科学の作業工程を強化する強力なツールだという。これ
らを併用して、再現可能なデータ科学環境を作成および実行する。

カスタマイズイメージを |DockerHub| にプッシュしてそれを ``docker run`` するのが
上手くいかない。

Suppress image vulnerabilities with VEX
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

実験的らしいので急ぎなら飛ばす。途中で必要になる実行形式ファイルは
:file:`vexctl-linux-amd64` だ。

Use containerized databases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MySQL コンテナーをビルドして実行するチュートリアル。

Build with Docker
----------------------------------------------------------------------

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
----------------------------------------------------------------------

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
----------------------------------------------------------------------

この体験型講義では Docker の始め方を一手ずつ順番に説明するとある。これを第一
チュートリアルとしてもよい。

* Part 2: Containerize an application: |Dockerfile| を書いてコマンド ``docker
  build``, ``docker run``, ``docker ps`` 等を実行する。
* Part 3: Update the application: さらにコマンド ``docker stop``, ``docker rm``
  等を習う。
* Part 4: Share the application: |DockerHub| アカウント開設後、コマンド ``docker
  login``, ``docker tag``, ``docker push`` 等を実行する。
* Part 5: Persist the DB: ``docker volume create``, ``--mount type=volume``,
  ``docker volume inspect`` 等。
* Part 6: Use bind mounts: ``--mount type=bind``, ``docker logs`` 等。
* Part 7: Multi-container apps: ``docker network create`` と MySQL とその他。
* Part 8: Use Docker Compose: :file:`compose.yaml` を作成してコマンド ``docker
  compose up`` を実行。コマンド ``docker compose down`` で破壊。

Educational resources
----------------------------------------------------------------------

Docker と Kubernetes の理解を深めるための資料集とある。

* `Live Debugging Node.js with Docker
  <https://training.play-with-docker.com/nodejs-live-debugging/>`__ は完走可能。
* `Docker CLI cheat sheet
  <https://docs.docker.com/get-started/docker_cheatsheet.pdf>`__ はペラ一枚。

Manuals
======================================================================

説明書ではあるのだが、読者の理解を助けるためなのか、How to と Quickstart が挿ま
ることがあるのでそれらを取り組む。また、重要な記述を気づきしだい拾っていく。

Get Docker
----------------------------------------------------------------------

Docker Desktop を入手する方法が紹介されているが、生の Docker Engine を使いたいの
でページ下の方の囲み記事のリンク先なら確認する。

Docker Desktop
----------------------------------------------------------------------

この章はほとんど飛ばすことになるが、

WSL
   この節は読んでおいたほうがいい。

Docker Extensions
----------------------------------------------------------------------

Docker Extensions を使えば Docker Desktop 内でサードパーティーのツールを使って機
能を拡張することができるというものだ。したがってこの章も飛ばす。

Docker Scout
----------------------------------------------------------------------

Docker Scout はソフトウェア供給鎖の安全保障を強化する解法だ。イメージを分析する
ことで :abbr:`SBOM (Software Bill of Materials)` としても知られる部品の目録を作
成する。SBOM は継続的に更新される脆弱性データベースと照合され、保障上の弱点を突
き止める。

Quickstart
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

実践的なチュートリアル。やるべきだ。

Install
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

XDG Base Directory に従いたいので、スクリプト実行後にバイナリーを :command:`mv`
する。スクリプトを修正してから実行するとなぜか上手くいかない。

Docker Engine
----------------------------------------------------------------------

Install
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Docker Engine を Linux にインストールする。Ubuntu の箇所を読む。

* Install Docker Engine on Ubuntu: 前述のとおり、これをいの一番に実施する。
* Linux post-installation steps for Docker Engine: :command:`sudo` を使わなくて
  も :command:`docker` を呼び出せるようにする支度等。
* Troubleshoot Docker Engine installation: デーモン起動コマンドを確認する。

Networking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コンテナーにおけるネットワークとは、コンテナー同士が互い接続して通信する機能等を
指す。

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`docker` についての手引集だ。

* Use the Docker CLI: 重要な設定項目があるのでチェックする。
* Completion: これは信じ難い。Bash の補完機能が :file:`~/.local/share` 以下を確
  認するというのか？
* Filter commans: ``--filter KEY=VALUE`` を受け入れるコマンドを知るといい。
* Format command and log output: これを読んで思った。Go 言語を学習するのがいい。

Manage resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

今のところ削除コマンドが最重要項目であるので、それしか読んでいない。

* Prune unused objects: チュートリアルではないが掃除コマンドが一覧になっていて重
  要だ。

Daemon
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

手動でもシステム起動時にも起動できるようになる。

* Start the daemon: WSL の設定が甘いと ``sudo systemctl start docker`` が失敗す
  るはずだ。
* Configure the daemon: 構成ファイルパスとコマンドライン例
* Configure with systemd: TODO
* Engine plugins

  * Managed plugin system: ``docker plugin install``, ``docker plugin ls``

Logs and metrics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AppArmor, SELinux, GRSEC 等の適切な堅牢化システムを有効にすることで、Docker コン
テナーの安全性を既定よりもさらに高めることができる。

Swarm mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Docker には swarm と呼ばれる Docker Engine の群れを管理する Swarm モードがあ
る。Docker CLI を使用して swarm を作成し、アプリケーションサービスを swarm に配
備し、swarm の動作を管理する。

たぶん満足に学習できない。

* Get started with swarm mode: チュートリアル

Docker build
----------------------------------------------------------------------

Docker Build は Docker Engine で最も使われている機能だ。Docker Build はイメージ
をビルドするためのコマンドであり、一般的な作業工程問題だけでなく、より複雑かつ高
度な筋道を支援する道具や機能の全体を指すようだ。

Building images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Packaging your software: チュートリアルとは言っていないが、この記事を基にイ
  メージをビルドするといい。|Dockerfile| はおそらく修正することになる。Flask を
  インストールする命令にオプション ``--break-system-packages`` を付ける。
* Multi-stage builds: ``FROM`` 命令に :samp:`AS {name}` を追加することで舞台に名
  前を与えることが可能だ。
* Variables: ``ARG`` 命令には変数有効域の概念がある。
* Building best practices: ``apt update`` を単独で ``RUN`` 命令中で実行するとミ
  スキャッシュと後続の ``apt install`` の失敗を生じる。
* Multi-platform images: ``docker buildx ls``, ``docker buildx create``
* Build secrets: :samp:`docker build --secret {XXXXXXX}`
* Create a base image: コンテナー構築の出発点として ``scratch`` を使用することが
  可能。次の |Dockerfile| コマンドがイメージの最初の階層になる。

Drivers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BuildKit バックエンドをどこでどのように実行するかの設定がドライバーだ。この設定
はカスタマイズ可能で、ビルダーをきめ細かく制御できる。

* Kubernetes driver: 例アリ。Minikube_ を導入してから実施する。
* Remote driver: 例アリ

Exporters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ビルド結果を指定の出力タイプに保存する機能。:samp:`--output type={type}` 形式で
指定。

Continuous integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

開発過程の一部であって、コードの変更をプロジェクトの主要ブランチに併合することを
言う。テストとビルドを実行し、コードの変更が悪さを引き起こさないことを確認する意
味がある。

* CI with Docker
* GitHub Actions

  * Introduction: Docker GitHub Actions を設定して Docker イメージをビルドし、
    |DockerHub| にプッシュするチュートリアルを含む。

Docker Compose
----------------------------------------------------------------------

Install
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

記憶がない

Quickstart
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|Dockerfile|, :file:`compose.yaml`, ``docker compose up``, ``docker compose
down``, ``docker compose watch``, ``docker compose ps``, ``docker compose stop``

Sample apps with Compose
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

外部リンク先にチュートリアルか？

Compose FAQs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

チラ見でいい

Docker Hub
----------------------------------------------------------------------

Create an account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Docker をインストールしたらすぐに実行可能。

Quickstart
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

アカウントを開設したらすぐに実行可能。

Administration
----------------------------------------------------------------------

管理者は |DockerHub| または Docker Admin Console を使って会社や組織をなんとかす
ることができる。

Reference
======================================================================

チュートリアルを全部こなしてから確かめることになる文書群。|Dockerfile| などの書
式仕様と CLI の説明書を確かめることが多い。後者に関して注目したいのは、文書が
:program:`docker` と ``docker compose`` とで別枠になっていることだ。

Glossary
----------------------------------------------------------------------

抜粋したり、自分なりに大雑把に解釈したことを以下に記す。

Docker
   #. 開発者とシステム管理者がアプリケーションを開発、出荷、実行するための土台。
   #. イメージとコンテナーを管理するホスト上で動作する :command:`dockerd`.
|DockerHub|
   次の機能などを有する Web サービスという解釈でいい：

   * Docker イメージをホストするレジストリー
   * 使用者認証
   * イメージの自動ビルド、ビルドトリガーや Web フックなどの作業工程ツール
   * GitHub や Bitbucket との統合
   * 安全保障脆弱性検査
Docker ID
   |DockerHub| のアカウント ID という認識。これを取得していれば、そのリポジト
   リーにアクセス可能になる。
|Dockerfile|
   Docker イメージを構築するために通常手動で実行するコマンドすべてを含むテキスト
   ファイル。Docker はこのファイルから指示を読み取り、イメージを構築する。
イメージ
   階層化されたファイルシステム同士を積み重ねたものと考えられる。イメージからコ
   ンテナーが生まれる。イメージは immutable であると、どこかに記してあった。
基底イメージ
   |Dockerfile| にその親イメージが指定されていないイメージ。``FROM scratch`` 司
   令を持つ |Dockerfile| から作成される。

   一般的に、イメージには派生関係があり、その根に相当するイメージが基底イメージ
   だ。
親イメージ
   あるイメージの |Dockerfile| の ``FROM`` 司令で指定されたイメージ。
コンテナー
   イメージの実行時インスタンス。オブジェクト指向言語の類比で言うとクラスに対す
   るオブジェクトに相当する。
リポジトリー
   イメージの集合。リポジトリーはレジストリサーバーに push することで共有可能。
レジストリー
   イメージのリポジトリーを含むサービス。
タグ
   リポジトリ内ーのイメージに適用されるラベルがタグだ。リポジトリー内のさまざま
   なイメージを区別する方法だ。
仮想機械
   計算機を模倣するプログラム。物理的なハードウェア資源は他の使用者と共有しなが
   ら、OS は分離される。最終使用者は仮想機械上で専用ハードウェアと同じ体験をする
   ことになる。
ボリューム
   一つまたは複数のコンテナー内の特別なディレクトリーだ。ボリュームはコンテナー
   の寿命とは無関係にデータを永続化するように設計されている。Docker はコンテナー
   を削除する際にボリュームを自動的に削除することはなく、コンテナーから参照され
   なくなったボリュームをゴミ回収することもない。
