======================================================================
Pandoc 利用ノート
======================================================================

.. contents::
   :depth: 2

本稿は `Pandoc <https://pandoc.org/>`__ を利用して Markdown ファイルを
reStrucutredText ファイルに変換することに関するノートだ。

利用に関する想定
======================================================================

単独の ``.md`` ファイルを ``.rst`` ファイルに変換する。ここで、各ファイルは読書
ノートの特定の主題の一章または一節という段階に対応するものとする。

したがって、実行するコマンドは次のものの派生形しかない：

.. code:: console

   bash$ pandoc -o output.rst input.md

インストール
======================================================================

ここではインストール手順を記さない。WSL で Miniconda で構築した Python 環境に他
のパッケージにまぎれて入ったものと思われる。

.. code:: console

   bash$ pandoc --version
   pandoc 2.12
   Compiled with pandoc-types 1.22, texmath 0.12.1.1, skylighting 0.10.4,
   citeproc 0.3.0.8, ipynb 0.1.0.1
   User data directory: /home/USERNAME/.local/share/pandoc
   Copyright (C) 2006-2021 John MacFarlane. Web:  https://pandoc.org
   This is free software; see the source for copying conditions. There is no
   warranty, not even for merchantability or fitness for a particular purpose.

オプション
======================================================================

Pandoc はオプションをたくさん用意している。使えるものは使う。

全般
----------------------------------------------------------------------

オプション ``--from`` の末尾に符号付きで指定する要素を入力元オプションと呼ぶこと
にする。 Pandoc に指定したい Markdown の取り扱い方は次のものだ：

====================== ===
オプション             値
====================== ===
smart                  OFF
east_asian_line_breaks ON
====================== ===

したがって ``--from markdown-smart+east_asian_line_breaks`` ということになる。

オプション ``--to`` の末尾に符号付きで指定する要素を入力元オプションと呼ぶことに
する。 Pandoc に指定したい reST の取り扱い方は次のものだ：

========== ===
オプション 値
========== ===
smart      OFF
========== ===

以下、拡張機能のノート。

* ``smart``: 普通の単引用符を海外の文章でよく見られる斜めの引用符に、トリプルマ
  イナスをエムダッシュ、ダブルマイナスを得ぬダッシュ、トリプルドットを三点リー
  ダーとしてそれぞれ解釈させる。

  ただし、特定の省略、例えば Mr. のドットなどの後には
  non-breaking space を挿し込ませる。

* ``east_asian_line_breaks``: 段落内の改行が二つのワイド文字間にある場合、空白文
  字や硬い改行として扱わず、無視する。東アジアのワイド文字と他の文字が混在するテ
  キストでは ``ignore_line_breaks`` よりも良い選択だろう。

読み込み
----------------------------------------------------------------------

* ``--shift-heading-level-by -1``: Markdown ファイルの Front Matter をレベル
  1 のセクション、それ以降をレベル 2, 3, ... としたい。

書き込み
----------------------------------------------------------------------

* ``--standalone``: 断片ではなく、完全な reST を生成することを指示する。この指定
  は見出しと TOC を書き出すのに必要だ。
* ``--eol lf``: 他プラットフォームでの作業も想定して、改行コードを明示しておく。
* ``--columns 80``: テキスト幅を指定する。常用するテキストエディターの指定値に一
  致させる。
* ``--table-of-contents``: reST ファイルの見出し直後に TOC を生成する。
* ``--toc-depth 2``: その TOC のツリーの深さ 2 にする。3 にしたければそうする。
* ``--wrap preserve``: 場合によっては ``--column`` の指定をやめてこちらにする。
  自筆の Markdown コードに自信があり、なるべく改行位置を変えたくないときなどに採
  用する。

指定を再利用する
======================================================================

オプション ``-d`` または ``--defaults`` で、以上の設定をまとめて記した YAML ファ
イルを与えることで、同等のコマンドラインオプション群を一括して指定するのと同じこ
とになる。

例えば、次のテキストを :file:`.defaults.yaml` という名前のファイルで保存する。場
所はひとまず作業ディレクトリーとしておく。

.. code:: yaml

   verbosity: INFO
   from: markdown-smart+east_asian_line_breaks
   to: rst-smart+east_asian_line_breaks

   shift-heading-level-by: -1

   standalone: true
   eol: lf
   columns: 80
   toc: true
   toc-depth: 2
   #wrap: preserve

その上で次のコマンドを実行すると、

.. code:: console

   bash$ pandoc -d defaults.yaml -o output.rst input.md

次のコマンドの実行と同じ効果が得られる：

.. code:: console

   bash$ pandoc
       --from markdown-smart+east_asian_line_breaks \
       --to rst-smart+east_asian_line_breaks \
       --shift-heading-level-by=-1 \
       --standalone --eol=lf --columns=80 --toc --toc-depth=2 \
       -o output.rst input.md

ちなみに ``.yaml`` は省略できる。

この YAML ファイルは同じ内容で再利用したい。Pandoc は ``--defaults`` の引数の
ファイルを次のディレクトリーから順次検索することになっている：

* :file:`$PWD`
* :file:`$HOME/.local/share/pandoc/defaults`: 正確には
  :command:`pandoc --version` の出力から User data directory とされているパスの
  サブディレクトリー :file:`defaults` となる。

したがって、YAML ファイルでの設定内容に満足したら次のようにする：

.. code:: console

   bash$ mkdir -p ~/.local/share/pandoc/defaults
   bash$ mv defaults.yaml ~/.local/share/pandoc/defaults

あるいはバージョン管理しているドットファイル群ディレクトリーに適宜配置してシンボ
リックリンクを置く。

テンプレートを与える
======================================================================

出力する reST ファイルのテンプレートを Pandoc の既定のものから変更することができ
る。しかし、変えたい部分を変えることができないので、この機能には深く立ち入らな
い。

いくつか断片的なメモを残す。

* オプション ``--standalone`` が必要
* コマンド :command:`pandoc -D rst` で reST 用の既定のテンプレートを出力
* オプション ``--data-dir`` の引数パスまたは
  :file:`$HOME/.local/share/pandoc/templates/default.rst` をテンプレートとする

例えば出力内容の ``contents`` ディレクティブの終端に必ずコメント行が入るのが気に
入らないとする。

.. code:: text

   $if(toc)$
   .. contents::
      :depth: $toc-depth$
   ..

   $endif$

この ``..`` の行を削ったものを上述のファイルパス :file:`default.rst` に保存して
おけばよい。
