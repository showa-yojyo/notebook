======================================================================
Pytube 利用ノート
======================================================================

本稿では Python のサードパーティ製パッケージである pytube_ について述べる。これ
を習得すれば YouTube にアップロードされている個々のビデオファイルをダウンロード
してローカルディスクに保存できる。

.. note::

   単純な場合には :command:`download-yt` を使え。

.. contents:: ノート目次

.. note::

   執筆時点での環境の概略を記す。

   * OS

     * Windows 10 Home x64

       * WSL 2: Ubuntu 20.04.2 LTS

   * Python 環境

     * Python_: 3.7.4, 3.9.5
     * pytube_: 9.5.2, 10.8.4

目的
======================================================================

目的は YouTube の任意のビデオファイルを MP3 に変換してローカルディスクに保存する
ことだ。

実際には MP4 ファイルさえダウンロードすれば十分だ。 MP4 ファイルを MP3 に変換す
ることは FFmpeg_ などの既存のツールで対応することにする。ダウンロードまでの処理
に pytube_ の能力を活用する。

導入手順
======================================================================

pip_ でのインストールになる。アップグレード手順もこれに準じる。

.. code:: console

   bash$ pip install pytube
   bash$ pip install --upgrade pytube
   Collecting pytube
     Downloading https://files.pythonhosted.org/packages/.../pytube-9.5.2-py3-none-any.whl
   Installing collected packages: pytube
     Found existing installation: pytube 9.5.1
       Uninstalling pytube-9.5.1:
         Successfully uninstalled pytube-9.5.1
   Successfully installed pytube-9.5.2

テスト手順
======================================================================

私はまだ試していないのだが、GitHub にあるリポジトリーをローカルに clone すれば単
体テスト用のディレクトリー :file:`tests` にアクセスできる。そこで
:command:`nosetests` するものと思われる。

使用例
======================================================================

いちばん簡単な用例
----------------------------------------------------------------------

某ビデオゲームのサントラ視聴用ビデオをダウンロードする例を示す。次のようなコード
がビデオファイルを MP4 形式でローカルディスクに保存する処理でもっとも単純なもの
になるだろう。

.. code:: pycon

   >>> from pytube import YouTube
   >>> watch_url = 'https://www.youtube.com/watch?v=wDmlxKLqgGo'
   >>> tube = YouTube(watch_url)
   >>> media = tube.streams.filter(only_audio=True, file_extension='mp4').first()
   >>> media.download()
   '/path/to/beatmania IIDX 26 Rootage ORIGINAL SOUNDTRACK【Disc3】.mp4'

ここではあとで MP3 形式に変換する前提なので、``.filter()`` に示すようなキーワー
ド引数を与えている。以上のコードを実行すると、作業ディレクトリーにビデオのある
ページのタイトル名に拡張子 ``.mp4`` が付いたファイルが生成する。

* まずは ``YouTube()`` に与える URL に

  .. code:: text

     watch?v=XXXXXXXXXXX

  のような文字列で終わるものを扱うといい。単一のビデオファイルだけではなく、
  YouTube のページにあるプレイリストのダウンロード機能も備えている。
* ``.download()`` で実際にローカルディスクにファイルを作成する。この例では画のな
  い MP4 ファイルが生成する。

より進んだ用例
----------------------------------------------------------------------

pytube_ の README に記述されている内容をよく読むこと。

コマンドラインツール
----------------------------------------------------------------------

インストール後にパッケージと同名の :command:`pytube` という実行スクリプトが利用
可能になる。内容は ``pytube.cli.main()`` を実行するものだ。YouTube から単発のビ
デオ・オーディオをダウンロードする用途ならばコードを自作する必要はなく、これを実
行するほうが早い。

次では ``URL`` を ``https://www.youtube.com/watch?v=XXXXXXXXXXX`` のタイプのもの
とする。

* :command:`pytube --help` でヘルプを表示する。これだけは覚えておく必要がある。
* :command:`pytube --version` でバージョンを表示する。
* :command:`pytube --list URL`` でストリーム一覧を出力する。オプション
  ``--itag`` の引数に与えることができる値だ。
* :command:`pytube URL` でビデオをダウンロードしてファイルに保存する。利用可能な
  最高解像度のプログレッシブストリームが選ばれる。

  * :command:`pytube --itag ITAG URL` で特定のストリームをダウンロードする。
  * :command:`pytube --audio FORMAT URL` でダウンロードして MP4 に保存する。

    例えば :command:`pytube --audio mp4 URL` で利用可能な最高ビットレートの
    AAC/mp4 オーディオデータをダウンロードしてファイルに保存する。

YouTube 側仕様変更に伴う回避策
======================================================================

現在は pytube_ の開発状況が活発なので、仕様変更が発生しても直ちに対応することが
大いに期待できる。したがって、次に記すような回避策をライブラリー利用者が個別に講
じることもなくなってきた。

`私の過去ツイート <https://twitter.com/showa_yojyo/status/1160392041118879745>`__
より。

改造案
======================================================================

思いつきを記す。

メソッド ``_extract_videos()`` および ``_paginate()`` の戻り値変更
----------------------------------------------------------------------

特定の YouTube チャンネルやプレイリストのビデオ全部の何らかの情報を効率良く取得
したい。クラス ``Playlist`` やそのサブクラスの ``Channel`` にはビデオ一覧を返す
プロパティーやメソッド ``videos``, ``video_generator()`` があるので、これを用い
て得られる ``YouTube`` オブジェクトのメソッドやプロパティーからデータを取得する
ことになる。しかし、これはオブジェクトの個数だけサーバーへのリクエストが発生して
すこぶる遅い。

これらの機能の実装はプライベートメソッド ``_extract_videos()`` と ``_paginate()``
が核となっている。そこでは YouTube の HTML ページの構造化された情報を URL 以外捨
て去っている。これをやめるように改造すれば、少なくともプレイリストページやチャン
ネルトップページに表示されるビデオのタイトル、閲覧数、アップロード日などの簡単な
情報を高速に得られることが期待できる。

次のコード片は ``Playlist._extract_videos()`` の終了部の抜粋だ。
``Channel._extract_videos()`` にも同様の処理がある。

.. code:: python

   # remove duplicates
   return (
       uniqueify(
           list(
               # only extract the video ids from the video data
               map(
                   lambda x: (
                       f"/watch?v="
                       f"{x['playlistVideoRenderer']['videoId']}"
                   ),
                   videos
               )
           ),
       ),
       continuation,
   )

上記の ``map`` 処理を ``x['playlistVideoRenderer']`` を抽出するように変更したい
というのが本項の主張だ。

FFmpeg を併用して MP3 に変換する
======================================================================

本節は pytube_ とは無関係の内容だ。

次のようなシェル関数を作成していつでも利用可能にしておくと楽ができるだろう：

.. code:: bash

   convert_mp3 ()
   {
       if ! command -v ffmpeg &> /dev/null; then
           echo 'Error: ffmpeg is not available.' 1>&2
           return
       fi

       local ffmpeg_global_options="-loglevel error -y"
       local ffmpeg_input_options=""
       local ffmpeg_output_options="-qscale:a 0 -map a"

       for i in "$@";
       do
           local input_url="$i"
           local output_url="${input_url%.mp4}.mp3"
           echo "Processing ${input_url}..." 1>&2
           ffmpeg -hide_banner $ffmpeg_global_options $ffmpeg_input_options -i "$input_url" $ffmpeg_output_options "$output_url"
           if [[ $? != 0 ]]; then
               echo "Error: $output_url is not generated" 1>&2
               continue
           fi
           rm -i -f "$input_url"
       done
   }

.. include:: /_include/python-refs-core.txt
.. _pytube: https://github.com/nficano/pytube
.. _FFmpeg: https://www.ffmpeg.org/
