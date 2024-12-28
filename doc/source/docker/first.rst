======================================================================
Docker 導入時手順
======================================================================

.. include:: ./docker-inc.txt

遅ればせながら Docker を習う。WSL2 Ubuntu 22.04.4 LTS に Docker Engine をインス
トールして学習を進める。Docker Desktop は当面の間導入しないでおく。今のところ、
その選択による不都合は ``docker init`` が使えないことと、Kubernetes との連携が実
現できなくなることくらいしかない。

.. contents:: 本章見出し
   :depth: 3
   :local:

以前の Docker 環境の残滓を一掃する
======================================================================

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
======================================================================

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
======================================================================

すぐ後に述べる :ref:`anchor-docker-started` で初めて必要になるのが普通だと考えら
れる。GitHub と同様に、

* 無料アカウントを作成する
* 二因子認証を構成する

ところまで行えば十分だ。

チュートリアル実施を中心に Docker Docs を読む
======================================================================

:doc:`./docs`

さらに修行する
======================================================================

チュートリアルをやり続けたい場合は :doc:`資料一覧<./reference>` にある記事に行く
といい。
