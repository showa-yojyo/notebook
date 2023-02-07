======================================================================
youtube-dl 利用ノート
======================================================================

YouTube やその他の映像音声サービスからビデオをダウンロードすることができるツール
youtube-dl_ について記す。

.. contents::

このツールは何であるのか
======================================================================

開発サイトの README_ から引用する：

    youtube-dl is a command-line program to download videos from YouTube.com and
    a few more sites. It requires the Python interpreter, version 2.6, 2.7, or
    3.2+, and it is not platform specific. It should work on your Unix box, on
    Windows or on macOS. It is released to the public domain, which means you
    can modify it, redistribute it or use it however you like.

私の場合は Windows の WSL2 (Ubuntu) で動作させることが可能だ。
コンソールから次の形式のコマンドラインを実行することで、上述の操作を遂行できる：

.. code:: console

   bash$ youtube-dl [OPTIONS] URL [URL...]

インストール
======================================================================

最初から :program:`youtube-dl` が WSL2 に入っていたのをそのまま使う。実態は
Python スクリプトなので、仮にシステムになかったとしてもどうにでもインストールで
きただろう。

:program:`youtube-dl` を快適に利用するために、次のツールも用意したい：

FFmpeg_
    ビデオ編集ツール。WSL にはインストール済み。
jq_
    JSON 操作ツール。管理者権限でコマンド ``apt install jq`` を実行する。

実践
======================================================================

習うより慣れろ。理論に入る前に実例を先に記しておく。

コマンドラインオプションを確認する
----------------------------------------------------------------------

GNU 製コマンドラインツールのように次のコマンドで標準出力にオプション一覧を出力す
る。もっとも、GitHub に置いてある README_ をブラウザーで閲覧するのが便利だろう。

.. code:: console

   youtube-dl --help

バージョンを確認する
----------------------------------------------------------------------

GNU ツールに従っている：

.. code:: console

   youtube-dl --version

このツールは日付でバージョンを識別するようだ。本稿執筆時点での最新版の出力はこう
なる：

.. code:: text

   2021.12.17

ビデオファイル一つをダウンロードする
----------------------------------------------------------------------

以下では ``$VIDEO_ID`` を YouTube のビデオ ID 文字列とする。

オプションなしで URL を指定するだけでダウンロードは可能だ：

.. code:: console

   youtube-dl "https://www.youtube.com/watch?v=$VIDEO_ID"

単純なコマンドラインだと保存ファイル名がゴチャゴチャしがちなので、なるべくオプ
ション ``--id`` を指定するか、またはオプション ``-o`` or ``--output`` でファイル
名を直接または間接的に指定することを強く勧める：

.. code:: console

   youtube-dl --id "https://www.youtube.com/watch?v=$VIDEO_ID"
   youtube-dl --output "%(id)s-%(title)s.%(ext)s" "https://www.youtube.com/watch?v=$VIDEO_ID"
   youtube-dl --output "%(id)s-%(title)s.%(ext)s" "https://www.youtube.com/watch?v=$VIDEO_ID"

オプション ``-o`` or ``--output`` の詳細は README_ を参照。

音楽ファイル一つをダウンロードする
----------------------------------------------------------------------

映像は要らないという場合にはオプション ``-x`` or ``--extract-audio`` を指定する。
これを利用する場合にはシステムに FFmpeg_ が必要だ。

オプション ``-x`` 単体だと既定では M4A ファイルを保存する。

.. code:: console

   youtube-dl -x "https://www.youtube.com/watch?v=$VIDEO_ID"

普通は MP3 で保存したいので、オプション ``--audio-format mp3`` を追加的に指定する：

.. code:: console

   youtube-dl -x --audio-format mp3 -o "%(id)s-%(title)s.%(ext)s" "https://www.youtube.com/watch?v=$VIDEO_ID"

これは先ほどのコマンド実行後に手動で ``ffmpeg -i xxxx.m4a xxxx.mp3`` を呼び出す
のと同じだと考えていい。

.. note::

   これ以降の記述のコマンドライン例ではオプション ``-o`` 指定は省略する。実際に
   はなるべく指定する。

ビデオファイル本体は要らないコマンドを実行する
----------------------------------------------------------------------

オプション ``--skip-download`` を指定しておけば、ビデオのダウンロードを阻止でき
る。

ビデオの情報だけを取得する
----------------------------------------------------------------------

タイトル、再生時間、ビデオ形式などの属性単品の情報を取得するには、対応するオプ
ション ``--get-xxxx`` を指定する。

.. code:: console

   youtube-dl --skip-download --get-title "https://www.youtube.com/watch?v=$VIDEO_ID"
   youtube-dl --skip-download --get-url "https://www.youtube.com/watch?v=$VIDEO_ID"
   youtube-dl --skip-download --get-id "https://www.youtube.com/watch?v=$VIDEO_ID"
   youtube-dl --skip-download --get-thumbnail "https://www.youtube.com/watch?v=$VIDEO_ID"
   youtube-dl --skip-download --get-description "https://www.youtube.com/watch?v=$VIDEO_ID"
   youtube-dl --skip-download --get-duration "https://www.youtube.com/watch?v=$VIDEO_ID"
   youtube-dl --skip-download --get-filename "https://www.youtube.com/watch?v=$VIDEO_ID"
   youtube-dl --skip-download --get-format "https://www.youtube.com/watch?v=$VIDEO_ID"

一度の実行で属性を複数指定してもよい。その場合は各属性値が改行されて出力される。
したがってテキスト処理が難しい。

.. code:: console

   youtube-dl --skip-download --get-title --get-description "https://www.youtube.com/watch?v=$VIDEO_ID"

ビデオ情報をなるべく詳細に取得するには JSON 出力を採用する。そのためのオプションは次の二種類ある：

* ``-j`` or ``--dump-json``
* ``-J`` or ``--dump-single-line``

実際には改行文字を入れるかどうかくらいの差しかなさそうだ。どうせ :program:`jq`
を利用するので、改行文字を用いない後者のオプションを使おう。

.. code:: console

   youtube-dl -J "https://www.youtube.com/watch?v=$VIDEO_ID" > $VIDEO_ID.json

ビデオごとの属性は作業するたびにコマンド ``jq 'keys' < xxxx.json`` で確認するほ
うがいい。有用かつ YouTube の仕様が変化しても存続するであろう属性の名前を挙げて
おく：

.. csv-table::
   :delim: |
   :header: キー,値
   :widths: auto

   ``description`` | ビデオの説明文
   ``duration`` | ビデオの再生時間（秒）
   ``fps`` | FPS
   ``height`` | 解像度縦幅（ドット）
   ``id`` | ビデオ ID 文字列
   ``title`` | ビデオのタイトル
   ``upload_date`` | アップロード日
   ``view_count`` | 再生数
   ``webpage_url`` | このビデオのメイン URL
   ``width`` | 解像度横幅（ドット）

完全な属性の集合を本稿の末尾に付録として掲載する。

サムネイル
----------------------------------------------------------------------

上記の阻止オプションとサムネイルオプションを併用するのが基本だ。

サムネイル画像の URL が欲しい
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

URL だけを知っておき、後ほど選択的に別ツールでダウンロードするということだ。オプ
ション ``--list-thumbnails`` は有効なサムネイル全部の URL を得る。

.. code:: console

   youtube-dl --skip-download --get-thumbnail "https://www.youtube.com/watch?v=$VIDEO_ID"
   youtube-dl --skip-download --list-thumbnails "https://www.youtube.com/watch?v=$VIDEO_ID"

サムネイル画像だけが欲しい
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

JPEG ファイルとして保存することになる。こちらも単複両バージョン用意されている。

.. code:: console

   youtube-dl --skip-download --write-thumbnail "https://www.youtube.com/watch?v=$VIDEO_ID"
   youtube-dl --skip-download --write-all-thumbnails "https://www.youtube.com/watch?v=$VIDEO_ID"

YouTube プレイリスト
----------------------------------------------------------------------

ここからはプレイリストに関する操作コマンドを書き連ねていく。ビデオをダウンロード
しない操作から述べていく。以下では ``$PLAYLIST_ID`` を適当な YouTube のプレイリ
スト ID 文字列とする。

プレイリストに関する情報一覧
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

オプション ``--get-xxxx`` 系はプレイリストに対しても有効だ。各ビデオに対する情報を
出力する。属性単品を見るときに手軽で便利だ。

.. code:: console

   youtube-dl --skip-download --get-title "https://www.youtube.com/playlist?list=$PLAYLIST_ID"
   youtube-dl --skip-download --get-id "https://www.youtube.com/playlist?list=$PLAYLIST_ID"

情報を JSON 形式で得る
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ビデオ単品の場合と同じだ。一般には出力が多いので、いったん JSON をファイルに保存
するのを勧める。これを :program:`jq` で解析、整形するのが実践的だろう。

.. code:: console

   youtube-dl -J "https://www.youtube.com/playlist?list=$PLAYLIST_ID" > dump-single-line.json
   jq -r '.entries[] | [.webpage_url, .title] | @tsv' < dump-single.json

プレイリストの場合には、次のキーも有用だ：

.. csv-table::
   :delim: |
   :header: キー,値
   :widths: auto

   ``n_entries`` | プレイリストが含むビデオの個数
   ``playlist_index`` | ビデオがプレイリストにある場合、そのインデックス

JSON は構造的でありすぎるという場合には CSV や TSV 形式に変換するといい。スプ
レッドシートに貼り付けて帳簿のように用いるなどできる：

.. code:: console

   jq -r '.entries[] | [.playlist_index, .title, .webpage_url] | @tsv' < dump-single-playlist.json
   jq -r '.entries[] | [.upload_date, .title, .webpage_url] | @tsv' < dump-single-channel.json

例えば ``webpage_url`` だけをテキストファイルに保存しておいて、オプション
``--batch-file`` で一括ダウンロードするという運用が考えられる。ファイルが要らなけ
れば標準入力 ``-`` にパイプしてもよい。

プレイリストのビデオをすべて取得する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

最も official な手法はオプション ``--download-archive`` を用いるものと思われる。
これを採用すると、一度ダウンロードしたファイルは次回以降のダウンロードを省略して
くれる。

.. code:: console

   youtube-dl --download-archive archive.txt "https://www.youtube.com/playlist?list=$PLAYLIST_ID"

他の方法としては、上述の JSON データを用意してから、それを編集して欲しいものを部
分的に得るというものがあるだろう。

.. todo::

   次のコマンドを確認する：

   .. code:: console

      youtube-dl --output "%(title)s.%(ext)s" --yes-playlist "https://www.youtube.com/playlist?list=$PLAYLIST"

構成
======================================================================

必ず指定するコマンドラインオプションがもしあれば、毎度コマンド実行時に指定するの
ではなく、下記のテキストファイルに列挙しておくと楽ができる：

.. csv-table::
   :delim: |
   :header: パス,内容
   :widths: auto

   :file:`/etc/youtube-dl.conf` | システム全体の構成
   :file:`$HOME/.config/youtube-dl/config` | ユーザー個別の構成

保存ファイル名のテンプレート
======================================================================

ダウンロードしたファイル名はそのままでは扱いづらいので、ユーザー側で明示的に変更
するのが普通だ。それにはオプション ``-o`` or ``--output TEMPLATE`` を指定する。
基本は ``youtube-dl -o FORMAT_STRING URL`` のように指定する。

``FORMAT_STRING`` には直接出力パスを指定することも可能だし、Python の文字列書式
の要領で特別なパターンを含めることも可能だ。例えば ``%(ATTRIB_NAME)s`` や
``%(ATTRIB_NAME)05d`` のようなものだ。

もちろん ``%(ATTRIB_NAME)s`` などのパターンが対応する実際の値に置換される。適切
な値が存在しない場合、オプション ``--output-na-placeholder`` で指定された値に置換
される。この既定値は文字列 ``NA`` だ。

数値列の場合は、数値に関連する書式を使用できる。例えば、``%(view_count)05d`` と
すると、``00042`` のように 5 文字までのゼロで埋め尽くされた ``view_count`` が文
字列として出力される。

出力テンプレートには任意の階層パスを含めてもよい。たとえば、

.. code:: text

   -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s

とすると、結果としてこのパステンプレートに対応するディレクトリーに各ビデオをダウ
ンロードする。見つからないディレクトリーがあれば自動的に作成する。

.. admonition:: 利用者ノート

   README_ を読み込まないと使いこなせない。

精選コマンドラインオプション
======================================================================

以下、一度は用いるか、よく用いるコマンドラインオプションを記す。

GNU 様式のオプション：

``-h``, ``--help``
    コマンドラインオプションを確認する。
``--version``
    バージョンを確認する。

対応プラットフォームを確認するオプションには次のようなものがある。一度は内容を確
認しておくとこのツールの能力が実感できる。

``--list-extractors``
    対応プラットフォームの一覧を標準出力に出力する。
``--extractor-descriptions``
    上のオプションの出力に対応して、プラットフォームの説明文一覧を標準出力に出力する。

.. todo::

   ``--flat-playlist``
       プレイリストの動画は抽出せず、一覧表示しかしない。これを多用したい。

取捨選択オプション
----------------------------------------------------------------------

まず、プレイリストの部分集合を取得するのに有用なオプションを知っておく：

``--playlist-start NUMBER``
    プレイリストの ``NUMBER`` 番目から処理する。既定値は ``1`` すなわちリスト先
    頭にあるものを指示する。
``--playlist-end NUMBER``
    プレイリストの ``NUMBER`` 番目まで処理する。既定値は ``last`` すなわち末尾に
    あるものを指示する。
``--playlist-items ITEM_SPEC``
    番号直接指定。書式はなんとなく :program:`curl` に似ている？

    * :samp:`1,2,5,8`
    * :samp:`1-3,7,10-13`

ビデオ投稿日に基づいた選択オプションを挙げる：

``--date DATE``
    この日付に投稿されたビデオしか扱わない。
``--datebefore DATE``
    指定日付またはそれ以前のビデオを扱う。
``--dateafter DATE``
    指定日付またはそれ以降のビデオを扱う。

.. code:: console

   # Download only the videos uploaded in the last 6 months
   youtube-dl --dateafter now-6months

   # Download only the videos uploaded on January 1, 1970
   youtube-dl --date 19700101

   # Download only the videos uploaded in the 200x decade
   youtube-dl --dateafter 20000101 --datebefore 20091231

タイトル文字列の正規表現マッチによる問い合わせオプションも挙げる：

``--match-title REGEX``
    正規表現 ``REGEX`` に合致するものを扱う。
``--reject-title REGEX``
    正規表現 ``REGEX`` に合致するものを扱わない。

ファイルシステムオプション
----------------------------------------------------------------------

一括ダウンロード用のオプションを頭に入れておきたい。再利用性があるので有用だ：

``-a``, ``--batch-file FILE``
    URL 一覧ファイルを与えてダウンロードさせる。

保存ファイルの名前に関するオプション：

``--id``
    保存ファイル名をビデオの ID ベースにする。
``-o``, ``--output TEMPLATE``
    保存ファイル名をパターン化する。

サムネイルオプション
----------------------------------------------------------------------

サムネイル画像を別途得ることも可能だ。

``--write-thumbnail``
    サムネイル画像も保存する。
``--write-all-thumbnails``
    サムネイル画像すべてを保存する。
``--list-thumbnails``
    サムネイル一覧情報を出力する。ビデオはダウンロードしない。

情報出力オプション
----------------------------------------------------------------------

まずは GNU 様式のオプションを二つ：

``-q``, ``--quiet``
    他のツールでよく目にするそれと同じ意味。
``-v``, ``--verbose``
    他のツールでよく目にするそれと同じ意味。

ダウンロード抑止用のオプション：

``-s``, ``--simulate``
    ビデオをダウンロードさせないし、何もディスクに保存させない。
``--skip-download``
    ビデオをダウンロードさせない。

次のオプション群に関しては ``-qs`` を暗黙に含む。用例は先述の記述を参照：

``-e``, ``--get-title``
    タイトルを得る。
``--get-id``
    ビデオの ID を得る。
``--get-duration``
    ビデオの再生時間を得る。
``--get-filename``
    ビデオのファイル名を得る。

JSON を得るオプションをまとめておく：

``-j``, ``--dump-json``
    JSON 形式でビデオの情報を得る。オプション ``-qs`` を暗黙に含む。
``-J``, ``--dump-single-json``
    コマンドライン引数それぞれについて JSON 情報を得る。こちらも ``-qs`` を暗黙
    に含む。
``--print-json``
    JSON 形式で情報を得る。かつビデオもダウンロードする。オプション ``-q`` を暗
    黙に含む。

ビデオ形式オプション
----------------------------------------------------------------------

``-f``, ``--format FORMAT``
    TODO 後回し
``-F``, ``--list-formats``
    :program:`youtube-dl` で有効な映像形式すべてを得る。一度確認しておけばいい。

後処理オプション
----------------------------------------------------------------------

先の記述を参照。

``-x``, ``--extract-audio``
    ビデオを音声のみのファイルに変換する。
``--audio-format FORMAT``
    音声形式を指定する。上記オプションと共に指定する。

付録
======================================================================

JSON ダンプの構造をチェックするコマンド例などを記す。

.. code:: console

   jq -r '.entries[0] | keys | join("\n")' < dump.json

本稿執筆時点での出力：

.. code:: text

   abr
   acodec
   age_limit
   automatic_captions
   average_rating
   categories
   channel
   channel_id
   channel_url
   description
   display_id
   duration
   ext
   extractor
   extractor_key
   format
   format_id
   formats
   fps
   height
   id
   is_live
   n_entries
   playlist
   playlist_id
   playlist_index
   playlist_title
   playlist_uploader
   playlist_uploader_id
   requested_formats
   requested_subtitles
   resolution
   stretched_ratio
   subtitles
   tags
   thumbnail
   thumbnails
   title
   upload_date
   uploader
   uploader_id
   uploader_url
   vbr
   vcodec
   view_count
   webpage_url
   webpage_url_basename
   width

.. _youtube-dl: https://github.com/ytdl-org/youtube-dl/
.. _README: https://github.com/ytdl-org/youtube-dl/
.. _FFmpeg: https://ffmpeg.org/
.. _jq: https://stedolan.github.io/jq/
