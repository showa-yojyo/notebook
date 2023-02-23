======================================================================
:program:`ffprobe`
======================================================================

:program:`ffprobe` は MP4 ファイルなどから情報を収集し、何らかのテキスト形式で出
力する。例えば、使用されているコンテナーの形式や、その中に含まれる各メディアスト
リームの属性を確認するといった用途に向いている。

:program:`ffprobe` は、スタンドアロンアプリケーションとして、またはテキストフィ
ルターと組み合わせて、より高度な処理、例えば統計処理やプロットを行うというような
用途に便利だ。コマンドの構文は次のように単純なものだ：

.. code:: console

   bash$ ffprobe [options] input_url

.. contents::

例：フレーム数を得る
======================================================================

簡単かつ一般的な例を挙げて、重要なコマンドラインオプションのいくつかを習得する。
例えば、ビデオのフレーム数を得るには次のコマンドを実行するのだが、長くて覚えられ
ない：

.. code:: console

   bash$ ffprobe \
     -select_streams v:0
     -count_frames \
     -show_entries stream=nb_read_frames \
     -print_format csv \
     input.mp4

オプション ``-select_streams STREAM_SPEC`` を用いると、指定ストリームしか選択し
ない。ストリームに関連するオプションにしか影響しない（後で述べる）。この例ではス
トリーム指定が ``v:0`` であるので、映像 0 のみを選択する。忘れぬうちに述べておく
と FFmpeg では序数を 0 から開始する。

.. .. seealso::
..
..    :doc:`./stream-spec`

オプション ``-count_frames`` はストリームごとにフレーム数を勘定し、対応するスト
リームセクション (``nb_read_frames``) に報告するものだ。この例ではストリーム指定
が ``v:0`` なので、映像 0 のフレーム数しか報告しない。

オプション ``-show_entries SECTION_ENTRIES`` はエントリーのリストを指定してそれ
らの情報を出力する。セクション名を指定し、その後に ``=`` を付けない場合、含まれ
るすべてのセクションとともにエントリーすべてが出力される。この例では
``stream=nb_read_frames`` なので、対応ストリーム ``v:0`` 全体ではなく、その
``nb_read_frames`` だけが出力される。このオプションについては後ほど詳述する。

オプション ``-print_format WRITER`` については後述。この例では ``csv`` なので
CSV 形式のテキストが出力される。

ファイルの構成を把握する
======================================================================

:program:`ffprobe` の出力するセクションの構造および情報を出力する。実行結果を一
度は見ておくことを強く勧める。後ほど述べる ``-show`` 系オプション各種の意味を把
握しやすくなる。

.. code:: console

   ffprobe -show_sections input.mp4

セクションエントリーを出力する
======================================================================

先述のように、オプション ``-show_entries SECTION_ENTRIES`` を指定する。
``SECTION_ENTRIES`` はセクションエントリーの一覧をコロンで区切った文字列を指定す
る。セクションエントリーそれぞれは、セクション名と、オプションでそのセクションに
ローカルなエントリーのリストがカンマ ``,`` で区切られた形で続く。例えば
``width,height`` など。セクション名を指定し、その後に ``=`` を付けない場合、含ま
れるすべてのセクションとともにエントリーすべてが出力される。

例コマンドをいくつか挙げる：

.. code:: console

   bash$ ffprobe -of flat -select_streams v:0 -show_entries stream=width,height input.mp4
   bash$ ffprobe -of default=nw=1 -select_streams v:0 -show_entries packet=pts_time input.mp4 | head
   bash$ ffprobe -show_entries stream=duration input.mp4
   bash$ ffprobe -select_streams v:0 -show_entries frame=pict_type input.mp4 | head
   bash$ ffprobe -select_streams v:0 -show_entries stream=bit_rate input.mp4
   bash$ ffprobe -select_streams v:0 -show_entries stream=codec_name,codec_long_name,profile,codec_tag_string input.mp4
   bash$ ffprobe -select_streams v:0 -show_entries stream=pix_fmt input.mp4

ファイル要素の情報を得る
======================================================================

次の四オプションについて記す：

* ``-show_streams``
* ``-show_format``
* ``-show_packets``
* ``-show_frames``

.. code:: console

   bash$ ffprobe -show_streams input.mp4
   bash$ ffprobe -show_format input.mp4
   bash$ ffprobe -show_packets input.mp4
   bash$ ffprobe -show_frames input.mp4

ストリーム情報を得る
----------------------------------------------------------------------

オプション ``-show_streams`` は入力に含まれるストリームの情報を出力する。オプ
ション ``-print_format`` の値にもよるが、ストリーム情報は出力の ``STREAMS`` とい
うセクションに含まれる。例えば JSON 形式で出力すると、次のような構造のテキストが
出力される（キー名は小文字になる）：

.. code:: text

   {
       "streams": [
           {
               ...
           },
           ...
       ]
   }

映像ストリームと音声ストリームとで構成が異なるので、詳しくは手許の適当なビデオ
ファイルで確認するといい。

コンテナー形式を得る
----------------------------------------------------------------------

オプション ``-show_format`` は入力のコンテナー形式に関する情報を表示する。各属性
はセクション ``FORMAT`` に先のオプションと同様に含まれる。この出力で確認できる有
用そうな属性を挙げておく：

* ``filename``
* ``nb_streams``
* ``format_name``
* ``format_long_name``
* ``start_time``
* ``duration``
* ``size``
* ``bit_rate``

パケット情報を得る
----------------------------------------------------------------------

オプション ``-show_packets`` は入力が含むパケットに関する情報を表示する。例に
よって各パケットの情報は ``PACKET`` という名前を持つ専用のセクションにある。

パケットというのは、音声や映像のデータの送受信単位だと考えられる。各パケットには
ファイルの小さな断片が含まれている。プレイヤーはこのパケットの流れを受け取り、映
像や音声に変換して再生する。

フレームまたは字幕情報を得る
----------------------------------------------------------------------

オプション ``-show_frames`` は入力が含む各フレームおよび字幕の情報を表示する。例
によって各フレームの情報は ``FRAME`` または `SUBTITLE``` という名称の専用セク
ションにある。

フレームには ``media_type`` という属性があり、この値によって構成が異なる。
例：``video`` には ``width``, ``height`` があるが、``audio`` にはない。

出力書式を指定する
======================================================================

:program:`ffprobe` のオプション ``-print_format`` a.k.a. ``-of`` の引数
``WRITER`` について記す。

``WRITER`` には :program:`ffprobe` が対応する出力書式を与える。さらに、``WRITER``
は採用するオプションを指定する一つ以上の引数を受け取ることができる。オプションは
コロンで区切られた ``key=value`` のペアのリストとして与えるものとする。

また、各書式オプションにはさらにオプションが用意されているものがある。
有効な ``WRITER`` のうち、よく用いられるものを次に挙げる：

.. csv-table::
   :delim: |
   :header: Writer,Format
   :widths: auto

   ``default`` | 既定の書式
   ``csv``     | CSV
   ``flat``    | プレーンテキスト
   ``xml``     | XML
   ``json``    | JSON

``default``
----------------------------------------------------------------------

書式 ``default`` は次のような出力をする：

.. code:: text

   [SECTION]
   key1=val1
   ...
   keyN=valN
   [/SECTION]

次のオプションがあり、どれも利用価値がある。既定値は ``0`` なので出力が長くなる。

``nokey``, ``nk``
    ``1`` を指定すると、フィールドのキー部分を出力しないようになる。

    .. code:: text

       [SECTION]
       val1
       ...
       valN
       [/SECTION]

``noprint_wrappers``, ``nw``
    ``1`` を指定すると、セクションタグを出力しないようになる。

    .. code:: text

       key1=val1
       ...
       keyN=valN

``csv``
----------------------------------------------------------------------

既定では、書式 ``csv`` は次のような出力を生じる：

.. code:: text

   section,val1, ... ,valN

次のオプションがある：

``item_sep``, ``s``
    カンマ以外の文字で区切りたい場合にはこのオプションでそれを指示する。
``nokey``, ``nk``
    書式 `default` と意味は同じ。ただし書式 ``csv`` では既定値が ``1`` であるこ
    とが異なる。
``escape``, ``e``
    エスケープ方法を ``c``, ``csv``, ``none`` から指定する。今はこのオプションの
    存在を知ってさえいればいい。
``print_section``, ``p``
    各行の先頭にセクション名を出力する (``1``) かどうか。

``flat``
----------------------------------------------------------------------

平坦な出力をする。

各行が ``streams.stream.3.tags.foo=bar`` のような明示的な ``key=value`` を含む自
由形式の出力だ。出力はシェルエスケープされており、区切り文字が英数字かアンダース
コアである限り、シェルスクリプトに直接埋め込める。

``json``
----------------------------------------------------------------------

各セクションを JSON 記法で出力する。改行文字を調整するオプションがある。

``compact``, ``c``
    ``1`` に設定すると各セクションが一行で出力される。

``xml``
----------------------------------------------------------------------

XML 形式で出力する。FFmpeg の :file:`datadir` に XML スキーマ記述ファイル
:file:`ffprobe.xsd` がインストールされている。このスキーマの最新版は
<http://www.ffmpeg.org/schema/ffprobe.xsd> にある（実際は開発版にリダイレク
ト）。
