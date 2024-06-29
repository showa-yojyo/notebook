======================================================================
構成ファイル
======================================================================

他のツールのようにドットファイルを作り込む必要は実のところほとんどない。

.. include:: ./docker-inc.txt

.. contents:: 本章見出し
   :local:

:file:`config.json`
======================================================================

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
======================================================================

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
