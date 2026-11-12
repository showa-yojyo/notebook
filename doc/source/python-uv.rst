================================================================================
uv 利用ノート
================================================================================

.. |bin| replace:: :file:`$XDG_DATA_HOME/../bin/`
.. |brew| replace:: :program:`brew`
.. |pip| replace:: :program:`pip`
.. |pyproject| replace:: :file:`pyproject.toml`
.. |uv| replace:: :program:`uv`
.. |uvlock| replace:: :file:`uv.lock`
.. |uvx| replace:: :program:`uvx`

執筆時点では、Python の仮想環境やパッケージを管理するのに有力なプログラムをその
へんの AI に尋ねると、この |uv| を推薦するはずだ。実際に少し試したところ、これま
での同種のプログラムとは一線を画す性能の高さと機能の多さを備えていることが感じら
れる。人気があるらしいのも納得だ。これが本稿を執筆することを決めた理由だ。

.. contents:: 見出し一覧
   :local:

特徴
================================================================================

* Micromamba がそうであるように、|uv| 自身が Python と独立して動作する。インス
  トール方法に紛れがないという利点がある。
* 上級プログラマーからの信頼が厚い Rust で記述されている。

  * というか、|uv| と作者が同じだ。
  * とはいえ、インストールに Rust ランタイムは不要だ。
  * 少なくともメモリー安全性と処理効率性は折り紙付きだ。
* Python 本体のバージョン管理を得意とする。特に、ファイルシステムに指定バージョ
  ンの環境が存在すればそれを流用する。
* 外部依存関係をコメント形式で記した Python スクリプトを扱うのが上手い。
* ルートパスに |pyproject| やロックファイルを配置するようなディレクト
  リー構造の Python プロジェクトを取り扱う能力がある。

過去に存在した同種の製品を超越するという使命を |uv| は自己に課しているのだろう。
主要機能は次の五本にまとめられる：

* バージョン違いの Python を取り扱うことが上手い
* サードパーティー製パッケージに依存するスクリプトを扱うのが上手い
* サードパーティー製パッケージを道具としてインストールする機能がある
* Python プロジェクトを管理する能力がある
* 別システムに |uv| 機能を内蔵する

インストール・更新・アンインストール
================================================================================

インストールにはさまざまな方法がある。基本方式は公式サイトが配布しているシェルス
クリプトを実行するというものだが、私の WSL Ubuntu 環境では Homebrew を用いるのが
最善だと考えられる：

.. sourcecode:: bash
   :caption: Homebrew による |uv| インストール命令

   brew install uv

更新やアンインストールにも :program:`brew` を用いればいい。ただし、アンインス
トールする場合には |uv| による管理物は一部を手動で削除しろ。この後に記す。

Homebrew プロファイルコードにより Bash などの対話シェルでの自動補完処理が有効に
なる。自力で組み込むならば、次のようなコードを対話シェルのプロファイルコードに含
めればいい。Bash の場合を示す：

.. sourcecode:: bash
   :caption: |uv| 命令行自動補完を組み込む
   :force:

   # Activate auto-completion for uv
   [[ -x "$(command -v uv)" ]] && eval "$(uv generate-shell-completion bash)"

これで |uv| を実行する準備は十分だ。基本情報を確認しろ：

.. sourcecode:: console
   :caption: |uv| 基本情報を調べる

   $ type -a uv
   uv is /home/linuxbrew/.linuxbrew/bin/uv
   $ uv --version
   uv 0.13.7 (Homebrew 2026-11-03 x86_64-unknown-linux-gnu)

この他、命令 ``uv --help`` や ``uv python list`` なども最初に試すものとしては適
している。

管理パッケージを削除する
--------------------------------------------------------------------------------

|uv| による管理パッケージについてはアンインストールのみ考え方を述べる。

まず、プログラム |uv| を操作することでシステムに取り込まれたファイルを削除するた
めに、関係ディレクトリーを知っておく必要がある：

.. sourcecode:: bash
   :caption: 物置ディレクトリーパスを得る命令群

   uv python dir
   uv tool dir

それから一時ファイルを削除する命令を実行する：

.. sourcecode:: bash
   :caption: |uv| 一時ファイルを削除する命令行

   uv cache clean

最後に、|uv| は使用者の :file:`bin` ディレクトリーにファイルを置く習慣がある。こ
こにあるファイルを手動で削除する：

* :file:`$XDG_DATA_HOME/../bin/uv`
* :file:`$XDG_DATA_HOME/../bin/uvx`
* :file:`$XDG_DATA_HOME/../bin/` に配置してあり、上述の物置に配置されていた実行
  形式を参照していたシンボリックリンクファイル

構成・カスタマイズ
================================================================================

TBW

使用方法・コツ
================================================================================

.. admonition:: 利用者ノート

   本節では先述した |uv| の機能のうち、次の三本に関してまず記す：

   * Python をバージョン別に管理する手筋
   * サードパーティー製パッケージに依存するスクリプトの基本的な取り扱い方
   * サードパーティー製パッケージが CLI である場合の取り扱い方

   残りの機能については後日加筆する計画だ。

システムにないバージョンの Python をインストール・更新する
--------------------------------------------------------------------------------

2026 年 11 月上旬時点で私の Ubuntu 26.04 LTS にある Python はバージョンが 3.14で
あるが、次の命令を実行すると Python 3.15 の実行形式が |uv| にインストールされ
る：

.. sourcecode:: bash
   :caption: ``uv python install`` 引数なし
   :force:

   uv python install

さらに、|uv| は |bin| にこの実行形式へのシンボリックリンク :file:`python3.15` を
追加する。

* 引数として Python バージョンを明示することが可能。旧版でも開発版でも。
* 命令 ``uv python list`` の出力により、このようにインストールした Python を一覧
  確認できる。

このようにしてインストールした Python は、バグ修正バージョンに更新するのを命令一
発で実現できる：

* 命令 ``uv python upgrade 3.15`` は |uv| にインストールさせた Python 3.15 を最
  新パッチリリースに更新させる。
* 命令 ``uv python upgrade`` は |uv| にインストールさせた Python すべてを上記と
  同様にパッチリリースに更新させる。

サードパーティー製パッケージに依存するスクリプトを扱う
--------------------------------------------------------------------------------

例を挙げる。自作の Python スクリプト :file:`mjnet-scraper.py` はサードパーティー
製パッケージ Click, PyYAML, Scrapy の三つに依存した実装だ。従来型の Python 環境
でこれを実行するには、実行する前に次のような準備をする必要がある：

#. Python 仮想環境を設ける
#. その仮想環境に上記パッケージ三つをインストールしておく
#. その仮想環境をスクリプト実行時に活動状態にする

この方式に悪い点があるとすれば、仮想環境をスクリプトごとに設けることだろう。

|uv| を採用すると、これを仮想環境を設けずに実行できる：

.. sourcecode:: console
   :caption: 命令 ``uv run`` で外部依存しているスクリプトを呼び出す例
   :force:

   $ uv run --with click --with pyyaml --with scrapy mjnet-scraper.py
   Installed 50 packages in 82ms
   (... output by mjnet-scraper.py ...)

二度目以降の実行ではインストール済みパッケージが利用される。

素晴らしい点はここからだ。命令行に羅列したこの依存情報をコメントとしてスクリプト
に埋め込むことが可能だ。命令 :samp:`uv add --script {SCRIPT} {PACKAGE ...}` を用
いる。例：

.. sourcecode:: console
   :caption: :samp:`uv add --script {SCRIPT} {PACKAGE ...}` の例
   :force:

   $ uv add --script mjnet-scraper.py click pyyaml scrapy
   Resolved 50 packages in 212ms
   $ head mjnet-scraper.py
   #!/usr/bin/env python
   # /// script
   # requires-python = ">=3.15"
   # dependencies = [
   #     "click>=8.5.1",
   #     "pyyaml>=6.0.3",
   #     "scrapy>=2.20.0",
   # ]

これにより、実行命令行は ``uv run --script mjnet-scraper.py`` で十分となる。

依存パッケージの更新をしたい場合は適切な命令行オプションを用いればいい：

* ``--update``
* :samp:`--upgrade-package {PACKAGE}`

サードパーティー製パッケージを道具としてインストールする
--------------------------------------------------------------------------------

Ruff, pytest, mypy など、CLI 形式で利用するプログラムに対しては |uvx| を用いるの
が定石とされている。例：

.. sourcecode:: bash
   :caption: |uvx| で :program:`ruff` を実行する例

   uvx ruff check

インストールオプションを指定したい場合、|uvx| に同等の命令行オプションが備わって
いることが多い。例：

.. sourcecode:: bash
   :caption: |uvx| で開発最新版 :program:`yt-dlp` を実行する例

   uvx --pre --from "yt-dlp[default]" yt-dlp ...

また、命令 :samp:`uv tool install {PACKAGE}` で CLI プログラムを |bin| にインス
トールする方法も有力だ。このとき、現在の環境の Python が *PACKAGE* を利用可能、
例えば ``import`` 可能になるわけではないことに注意しろ。

資料集
================================================================================

* uv_: 最低でも Getting Started, Guides, Concepts の章は通読しろ。

.. include:: /_include/python-refs-core.txt
.. _uv: https://docs.astral.sh/uv/
