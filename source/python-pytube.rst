======================================================================
Pytube 利用ノート
======================================================================

本稿では Python のサードパーティ製パッケージである pytube_ について述べる。
これを習得すれば YouTube にアップロードされている個々のビデオファイルをダウンロードしてローカルディスクに保存できる。

.. contents:: ノート目次

.. note::

   執筆時点での環境の概略を記す。

   * OS

     * Windows 10 Home x64

   * Python 環境

     * Python_: 3.7.4
     * pytube_: 9.5.2

目的
======================================================================

目的は YouTube の任意のビデオファイルを MP3 に変換してローカルディスクに保存することだ。

実際には MP4 ファイルさえダウンロードすれば十分だ。
MP4 ファイルを MP3 に変換することは FFmpeg_ などの既存のツールで対応することにする。
ダウンロードまでの処理に pytube_ の能力を活用する。

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

私はまだ試していないのだが、GitHub にあるリポジトリーをローカルに clone すれば単体テスト用の
``tests`` ディレクトリーにアクセスできる。そこで ``nosetests`` するものと思われる。

使用例
======================================================================

いちばん簡単な用例
----------------------------------------------------------------------

某ビデオゲームのサントラ視聴用ビデオをダウンロードする例を示す。
次のようなコードがビデオファイルを MP4 形式でローカルディスクに保存する処理でもっとも単純なものになるだろう。

.. code:: pycon

   >>> from pytube import YouTube
   >>> watch_url = 'https://www.youtube.com/watch?v=wDmlxKLqgGo'
   >>> tube = YouTube(watch_url)
   >>> media = tube.streams.filter(only_audio=True, file_extension='mp4').first()
   >>> media.download()
   '/path/to/beatmania IIDX 26 Rootage ORIGINAL SOUNDTRACK【Disc3】.mp4'

ここではあとで MP3 形式に変換する前提なので、``.filter()`` に示すようなキーワード引数を与えている。
以上のコードを実行すると、作業ディレクトリーにビデオのあるページのタイトル名に拡張子 ``.mp4`` が付いたファイルが生成する。

* まずは ``YouTube()`` に与える URL に

  .. code:: text

     watch?v=XXXXX

  のような文字列で終わるものを扱うといい。
  単一のビデオファイルだけではなく、YouTube のページにあるプレイリストのダウンロード機能も備えている。
* ``.download()`` で実際にローカルディスクにファイルを作成する。
  この例では画のない MP4 ファイルが生成する。

より進んだ用例
----------------------------------------------------------------------

pytube_ の README に記述されている内容をよく読むこと。

オプション
----------------------------------------------------------------------

TBW

YouTube 側仕様変更に伴う回避策
======================================================================

現在は pytube_ の開発状況が活発なので、仕様変更が発生しても直ちに対応することが大いに期待できる。
したがって、次に記すような回避策をライブラリー利用者が個別に講じることもなくなってきた。

* `私の過去ツイートより <https://twitter.com/showa_yojyo/status/1160392041118879745>`__

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
