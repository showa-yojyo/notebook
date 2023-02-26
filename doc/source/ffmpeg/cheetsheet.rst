======================================================================
技法集と豆知識
======================================================================

本稿では FFmpeg を利用した手筋を集める。各トピックを論理的な塊に集約するほどの理
解がないので、実現の簡単なものから難しいものに並べる。なお、このページに目を通す
前に、:doc:`./references` にある記事集を当たること。技術も記述も正確性において高
い。

解法がフィルター単品の適用による手筋については、公式文書の当該フィルターの記載を
も併せて確認すること：
`FFmpeg Filters Documentation <https://ffmpeg.org/ffmpeg-filters.html>`__

.. contents::

逆再生
======================================================================

.. seealso::

   * `How to Reverse a Video using FFmpeg - OTTVerse <https://ottverse.com/reverse-a-video-using-ffmpeg/>`__
   * `How to use FFmpeg Command for Reverse Video? - Video Production Stack Exchange <https://video.stackexchange.com/questions/17738/how-to-use-ffmpeg-command-for-reverse-video>`__

映像と音声を同時に逆転させることも、一方だけを逆転させることも可能だ。

.. code:: console

   bash$ ffmpeg -i input.mp4 -vf reverse output.mp4
   bash$ ffmpeg -i input.mp4 -vf reverse -af areverse output.mp4

この処理は入力全体をメモリーに格納することに注意を要する。巨大なビデオに対して
は、何分割かしてからそれぞれを個別に逆転させて結合する（上述）ことを検討する。

回転および反転
======================================================================

携帯電話で撮影した映像を扱うのであれば、ちょうど 90 度だけ回転させたり反転させた
りする手筋を覚えておくと何かのときに助かる。

.. seealso::

   * `FancyFilteringExamples - FFmpeg <https://trac.ffmpeg.org/wiki/FancyFilteringExamples>`__
   * `How to Rotate A Video using FFmpeg Easily - OTTVerse <https://ottverse.com/rotate-a-video-using-ffmpeg-90-180/>`__
   * `rotation - Rotating videos with FFmpeg - Stack Overflow <https://stackoverflow.com/questions/3937387/rotating-videos-with-ffmpeg>`__

反転
----------------------------------------------------------------------

映像フィルター ``hfilter``, ``vfilter`` を用いる。水平軸または垂直軸に関する反転
を実現する。オプションがないので紛れがない。

.. code:: console

   bash$ ffmpeg -i input.avi -vf "hflip" -c:a copy output.avi
   bash$ ffmpeg -i input.avi -vf "vflip" -c:a copy output.avi

回転
----------------------------------------------------------------------

映像フィルター ``transpose`` を用いる。コマンドの基本形は次のとおり：

.. code:: console

   bash$ ffmpeg -i input.mp4 -vf "transpose=dir=1" -c:a copy output.mp4

引数 ``dir`` の値は数字かキーワードで指定できる。都合の良いほうを使っていい：

.. csv-table::
   :delim: |
   :header: 番号,名前,変換内容
   :widths: auto

   ``0`` | ``cclock_flip`` | +90 度回転してミラー
   ``1`` | ``clock`` | -90 度回転
   ``2`` | ``clock`` | +90 度回転
   ``3`` | ``clock_flip`` | -90 度回転してミラー

* 有効な値には ``4``..``7`` もあるが、これは非推奨だ。代わりに後述の引数を指示す
  る。
* 180 度回転は ``transpose`` を合成すれば実現できる。

縦長・横長を :program:`ffmpeg` 判定させて必要な場合に限り回転させるというコマン
ドもあり得る。引数 ``passthrough=landscape`` 等を指定する。「横長ならば横長のま
まとする」の指示を意味する：

.. code:: console

   bash$ ffmpeg -i input.mp4 -vf "transpose=dir=2:passthrough=landscape" -c:a copy output.mp4

ビデオを Twitter に投稿可能な状態にエンコードし直す
======================================================================

.. seealso::

   `twitter ffmpeg · GitHub <https://gist.github.com/nikhan/26ddd9c4e99bbf209dd7>`__

携帯電話で撮影した MP4 ファイルに対してならば、上記リンク先スレッドの ``foone
commented on May 18, 2018`` コメントのコマンドを加工して実行するといい。状況に応
じてオプションを加えたり除いたりすることだ。

静止画像抽出
======================================================================

.. seealso::

   `Thumbnails &amp; Screenshots using FFmpeg - 3 Efficient Techniques - OTTVerse <https://ottverse.com/thumbnails-screenshots-using-ffmpeg/>`__

画像ファイル群からスライドショウを作成する
======================================================================

.. seealso::

   * `Slideshow - FFmpeg <https://trac.ffmpeg.org/wiki/Slideshow>`__
   * `Create Video from Images using FFmpeg - OTTVerse <https://ottverse.com/create-video-from-images-using-ffmpeg/>`__

紙幅がないのでコツを箇条書きにして済ませる：

* 単純な成果で良ければフィルターを用いることはなく実現できる。入力オプション
  ``-framerate DURATION`` くらいしか本質的には与えない。
* ページごとに表示時間を変えたいなどの場合には、後述するビデオ結合の手法を選ぶ。

  * ``file`` 行の次に ``duration`` 行を明記する。
  * 末端付近で ``file`` エントリーを重複させるのがコツとなる。二度目では
    ``duration`` を指定しない。
  * 出力オプション ``-vsync vfr`` を指定することがある。これは、同じタイムスタンプ
    を持つフレームが二つと存在しないように、タイムスタンプのまま通過させるか、一つ
    を除いて捨てる。

一枚絵のビデオを作成する
----------------------------------------------------------------------

画像ファイル ``input.jpg`` を ``10`` 秒間表示するだけのビデオを作成したいとす
る。それには次のようなコマンドを実行する：

.. code:: console

   bash$ ffmpeg -loop 1 -i input.jpg -c:v libx264 -t 10 output.mp4

次のコマンドは再生時間を音楽に合わせて ``input.mp3`` を BGM とする MP4 ビデオを
出力する：

.. code:: console

   bash$ ffmpeg -loop 1 -i input.jpg -i input.mp3 -c:v libx264 -c:a copy -shortest output.mp4

ビデオを結合する
======================================================================

.. seealso::

   * `FFmpeg Formats Documentation | 3.5 concat <https://ffmpeg.org/ffmpeg-formats.html#concat-1>`__
   * `Concatenate - FFmpeg <https://trac.ffmpeg.org/wiki/Concatenate>`__
   * `How to Concatenate mp4 Files Using FFmpeg Easily in 3 Different Ways! - OTTVerse <https://ottverse.com/3-easy-ways-to-concatenate-mp4-files-using-ffmpeg/>`__

同一形式のものを結合する
----------------------------------------------------------------------

いちばん単純な場合は画面寸法、ピクセルフォーマット、codec などが同じである MP4
ファイル二つを連結するものだ。携帯電話で撮影して保存した MP4 ファイルに対して適
用可能。結合処理は二段階からなる：

1. 連結したいファイルの名前とパスが記載されたテキストファイルを用意する
2. このテキストファイルを :program:`ffmpeg` コマンドに与える

テキストファイルの内容は次のようなものだ：

.. code:: shell

   # fileList.txt
   file '/path/to/input0.mp4'
   file '/path/to/input1.mp4'

コマンドラインはこうなる：

.. code:: console

   bash$ ffmpeg -f concat -safe 0 -i fileList.txt -c copy output.mp4

* ``-f concat``: demuxer を ``concat`` とする。
* ``-safe 0``: ファイルパスに対するチェックを大甘にする。

一般の条件で結合する
----------------------------------------------------------------------

結合コマンドを実行する前に、対象ビデオファイル群を同一形式に再エンコードする必要
がある。

* 結合前のファイルに対して再エンコードする。結合する前に品質を正確に制御できる。
* 映像フィルターのほうの ``concat`` を用いる。

後者の例は次のようなものだ。ここでは与えないが、出力オプションで encoder を指定
する余地がある：

.. code:: console

   bash$ ffmpeg -i input0.mp4 -i input1.mp4 -i input2.mp4 \
     -filter_complex "[0:v][0:a][1:v][1:a][2:v][2:a]
       concat=n=3:v=1:a=1[vv][aa]" \
     -map "[vv]" -map "[aa]" output.mp4

また、紙幅の都合上ここには記さぬが、ビデオファイルを TS フォーマットに変換すると
UNIX/Linux コマンドの :command:`cat` で直接連結が可能になる。詳しくは上述の文献
を参照。

再生区間を抽出する
======================================================================

時間帯を指定して元ビデオから再生時間がより短いビデオを得たい。

.. seealso::

   * `ffmpeg Documentation | 5.4 Main options <https://ffmpeg.org/ffmpeg.html#Main-options>`__
   * `How to Cut Video Using FFmpeg in 3 Easy Ways (Extract/Trim) - OTTVerse <https://ottverse.com/trim-cut-video-using-start-endtime-reencoding-ffmpeg/>`__
   * `How i could cut the last 7 second of my video with ffmpeg? - Super User <https://superuser.com/questions/744823/how-i-could-cut-the-last-7-second-of-my-video-with-ffmpeg>`__

時間指定用オプションを以下にまとめる。まずは一部を捨てるコマンドから：

.. csv-table::
   :delim: |
   :header: 指定方式,コマンド,外で計算
   :widths: auto

   開始から指定時間だけ捨てる | ``-ss DURATION -i INPUT ... OUTPUT`` | NO
   開始から指定時刻まで捨てる | ``-ss POSITION -i INPUT ... OUTPUT`` | NO
   終了までの指定時間だけ捨てる | ``-i INPUT -t DURATION ... OUTPUT`` | YES
   指定時刻から終了まで捨てる | ``-i INPUT -to POSITION ... OUTPUT`` | YES

終了時間付近のカットは時刻なり時間なりをあらかじめ計算しておかねばならない。

一部を残すコマンドについて述べる。 ``-sseof POSITION -i INPUT`` を用いると、時刻
を終端基準とし、かつ時間軸が逆向きになる。したがって引数は負の数を指定する必要が
ある。

.. csv-table::
   :delim: |
   :header: 指定方式,コマンド,外で計算
   :widths: auto

   開始から指定時間だけ残す | ``-i INPUT -t DURATION ... OUTPUT`` | NO
   開始から指定時刻まで残す | ``-i INPUT -to POSITION ... OUTPUT`` | NO
   終了までの指定時間だけ残す | ``-sseof -DURATION -i INPUT ... OUTPUT`` | NO
   指定時刻から終了まで残す | ``-ss POSITION -i INPUT ... OUTPUT`` | NO

内側を残す方法は上記をどうにか組み合わせる。

* ``-t DURATION`` (input/output)

  * (input) 入力ファイルから読み込まれるデータの継続時間
  * (output) 出力が ``DURATION`` に達した後、書き込みを停止する。

* ``-to POSITION`` (input/output)
  * 出力の書き込みまたは入力の読み取りを ``POSITION`` で停止する。

オプション ``-to`` と ``-t`` は同時に機能しない。両方指定すると ``-t`` が優先さ
れる。

* ``-ss position`` (input/output)

  * (input) この入力ファイルの位置まで seek する。厳密には ``POSITION`` にセット
    されないことが普通だ。
  * (output) タイムスタンプが ``POSITION`` に達するまで、入力を復号しつつも捨て
    る。
* ``-sseof position`` (input)
  * ``-ss`` の EOF 基準バージョン。0 は EOF を指し、負の値はより BOF に近づく。

最後に、再エンコードをするかしないかで結合処理の性質が異なることを考慮することだ。
再エンコードせずに済むならば、変質せずに高速に処理される。

ビデオの画面を伸縮する
======================================================================

.. seealso::

   * `FFmpeg Filters Documentation | 11.212 scale <https://ffmpeg.org/ffmpeg-filters.html#scale-1>`__
   * `Resize/Scale/Change Resolution of a Video using FFmpeg Easily - OTTVerse <https://ottverse.com/change-resolution-resize-scale-video-using-ffmpeg/)>`__
   * `Scaling - FFmpeg <https://trac.ffmpeg.org/wiki/Scaling>`__

伸縮操作の基本は映像フィルター ``scale`` を用いるものだ。次のコマンド呼び出しは
省略部分が同一ならばすべてが同値だ：

.. code:: console

   bash$ ffmpeg -i input.mp4 -vf scale=w=${width}:h=${height} ... output.mp4
   bash$ ffmpeg -i input.mp4 -vf scale=${width}:${height} ... output.mp4
   bash$ ffmpeg -i input.mp4 -vf scale=${width}x${height} ... output.mp4

品質が劣化するのが気になる場合は出力オプション部に encoding 指定をする。例えば
libx264 の低速プリセットで ``crf=18`` を使用するなど：

.. code:: console

   bash$ ffmpeg -i input.mp4 -vf scale=${width}:${height} -preset slow -crf 18 output.mp4

入力画面の幅と高さをそれぞれ ``iw`` と ``ih`` で参照できる。

* 例：画面幅を二倍に拡大する ``scale=iw*2:ih``. この ``*`` はシェルに展開されな
  い。
* 例：寸法を半分にする ``scale=iw/2:ih/2``. こちらは引用符で囲むこと。

アスペクト比を維持して伸縮する
----------------------------------------------------------------------

アスペクト比を保ったまま動画を拡大縮小したい場合、 ``height`` か``width`` のどち
らかの引数を値で設定し、もう一方の引数の値を負の値に設定するといい。

映像形式によっては画面寸法が偶数であることを要求する。そのときは ``-1`` の代わりに
``-2`` を指定する：

.. code:: console

   bash$ ffmpeg -i input.mp4 -vf scale=320:-2 output.mp4

関数 ``min()`` と ``iw``, ``ih`` を組み合わせれば最小の幅と高さを決められる。単
純な方法で質の悪い伸縮を防げる手筋だ：

.. code:: console

   bash$ ffmpeg -i input.mp4 -vf "scale='min(320,iw)':'min(240,ih)'" output.mp4

テキスト
======================================================================

字幕という手もあるが、ここではフィルター ``drawtext`` を用いる方法を述べる。

.. seealso::

   * `FFmpeg Filters Documentation | 11.76 drawtext <https://ffmpeg.org/ffmpeg-filters.html#drawtext-1>`__
   * `FFmpeg drawtext filter to Insert Dynamic Overlays, Scrolling Text, and Timestamps - OTTVerse <https://ottverse.com/ffmpeg-drawtext-filter-dynamic-overlays-timecode-scrolling-text-credits/>`__
   * `FilteringGuide - FFmpeg <https://trac.ffmpeg.org/wiki/FilteringGuide>`__ の ``drawtext`` を利用した節二つ

文字を打ち込む作業は何度も何度も画面を見直すから :program:`ffplay` で確認すると
いい：

.. code:: console

   bash$ ffplay -vf "drawtext=text='なんらかのテキスト':
       fontfile=/path/to/fontfile:
       box=0:boxcolor=white@0.5:
       x=20:y=20:
       shadowx=1:shadowy=1:shadowcolor=deeppink@0.9:
       fontcolor=deeppink:fontsize=48:line_spacing=8" -autoexit -y 480 input.mp4

.. admonition:: 利用者ノート

   問題はオプション ``fontfile`` の指定だ。これは Windows のフォントを指定しても
   OK ではある。しかし、できれば WSL 側で適宜設定して単純なパスで指定するか、あ
   るいは代わりにオプション ``font`` でフォント名だけを指定すれば十分であるよう
   に持っていきたい。

   あと、TrueType フォントを指定すると描画が乱れる現象が起こっている。現状、拡張
   子 ``.ttc`` のものしか描けない。

複数配置
======================================================================

フィルター ``hstack``, ``vstack``, ``xstack`` がその目的にはふさわしい。

.. seealso::

   * `Stack Videos Horizontally, Vertically, in a Grid With FFmpeg - OTTVerse <https://ottverse.com/stack-videos-horizontally-vertically-grid-with-ffmpeg/>`__
   * `Vertically or horizontally stack (mosaic) several videos using ffmpeg? - Stack Overflow <https://stackoverflow.com/questions/11552565/vertically-or-horizontally-stack-mosaic-several-videos-using-ffmpeg>`__

フィルター ``hstack``, ``vstack`` を組み合わることで 2x2 レイアウトを実現するこ
ともできるが、効率がより良いフィルター `xstack` があるのでそれを利用したい。例を
示す。簡単のために、入力映像の画面寸法はすべて同じであると仮定する：

.. code:: console

   bash$ ffmpeg \
       -i input0.mp4 -i input1.mp4 \
       -i input2.mp4 -i input3.mp4 \
       -filter_complex "xstack=inputs=4:layout=0_0|0_h0|w0_0|w0_h0:shortest=1"
       output.mp4

これは次のようなレイアウトになる：

.. code:: text

   input0 input2
   input1 input3

引数 ``layout`` の値は縦棒区切りの謎の記号だが、これで出力における各映像入力の位
置を指示する。``POSX_POSY`` のような形式で座標を指定している。数字は序数で
``w0`` や ``h0`` はそれぞれ入力映像 ``0`` の幅と高さを表す。

同系統のフィルターと同様に、入力映像すべてが同一のピクセルフォーマットでなければ
ならない。

グリッドの個数は 2 以上でも可能だし、極端に言えばグリッド状でなくてもいい。同一
の映像入力を用いてもよい。演習として、ビートマニアの V のクリップのようなものを
構成してみるといい。

ぼかし
======================================================================

映像の空間的に、または時間的に一部をぼかす方法を記す。

.. seealso::

   * `Blur a Video using FFmpeg's BoxBlur Filter - OTTVerse <https://ottverse.com/blur-a-video-using-ffmpeg-boxblur/>`__
   * `How to Apply a Gaussian Blur to a Video with FFmpeg - Bannerbear <https://www.bannerbear.com/blog/how-to-apply-a-gaussian-blur-to-a-video-with-ffmpeg/>`__

考え方を述べる。オリジナルの映像の一部を矩形に「クリップボード」にコピーし、ぼか
しフィルターで加工する。加工した映像矩形を元映像の同じ位置に「貼り付ける」という
のが基本的な考え方だ。コマンドラインも比較的単純な構造になる。オプション
``-filter_complex`` の引数だけを抜粋したものを示す：

.. code:: console

   bash$ ffmpeg -i input.mp4 \
     -filter_complex "
       [0:v]crop=400:400:300:350,boxblur=10[fg];
       [0:v][fg]overlay=300:350[v]" \
     -map "[v]" output.mp4

模式化しておく：

.. mermaid::

   flowchart TB
     input --> 0(0:v)
     0 --> crop\n400:400:300:350 --> boxblur\n10 --> fg(fg);

     0 --> overlay[overlay\n300:350]
     fg --> overlay

     overlay --> output

* ``crop=400:400:300:350``: 座標 (300, 350) を原点とする矩形 400x400 を crop す
  るの意。
* ``overlay=300:350``: オーバーレイ座標。
* ``boxblur=10``: ぼかしの強度。

ぼかしを矩形の周囲にしたい場合は全域を ``boxblur`` した絵にオリジナルの矩形を
``crop`` したものを ``overlay`` すればいい。また、フィルターには ``boxblur`` の
他にも豊富にある。

映像遷移効果
======================================================================

Demuxer ``concat`` で物足りないときにはフィルター ``xfade`` を検討したい。これは
ある映像から別の映像へ切り替わるときに、スライドやワイプなどの視覚的効果を与える
ものだ。

.. seealso::

   * `FFmpeg Filters Documentation | 11.283 xfade <https://ffmpeg.org/ffmpeg-filters.html#toc-xfade>`__
   * `Xfade - FFmpeg <https://trac.ffmpeg.org/wiki/Xfade>`__
   * `CrossFade, Dissolve, and other Effects using FFmpeg's xfade Filter - OTTVerse <https://ottverse.com/crossfade-between-videos-ffmpeg-xfade-filter/>`__

次のコマンドは :file:`input0.mp4` から :file:`input1.mp4` へクロスフェイドす
る映像を出力するはずだ：

.. code:: console

   bash$ ffmpeg \
       -i input0.mp4 \
       -i input1.mp4 \
       -filter_complex "xfade=transition=fade:
       duration=${TRANSITION_DURATION_IN_SECONDS}:
       offset=${OFFSET_RELATIVE_TO_FIRST_STREAM_IN_SECONDS}" \
       output.mp4

オプション ``transition`` に効果を指定する。``xfade`` が対応する利用可能な遷移効
果を指定する。選択肢がべらぼうに多いので本稿では割愛。

オプション ``duration`` には遷移効果時間を指定する。60 秒以下である必要がある。

オプション ``offset`` には遷移を開始する時刻を秒単位で指定する。時刻の基準は最初
の映像開始時点とする。

最後に出力ファイルを指定する。望むなら encoding オプションを追加的に指定する。
