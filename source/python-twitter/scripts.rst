======================================================================
付録スクリプト
======================================================================
本節では PTT の付録スクリプトについて説明する。

.. contents:: ノート目次

概要
======================================================================
Windows 環境では PTT をインストールすると、
ディレクトリー ``$PYTHONHOME/Lib/site-packages/twitter`` にパッケージを構成するモジュールファイル群をコピーする他に、
ディレクトリー ``$PYTHONHOME/Scripts`` に下に示す実行ファイル群を生成する。
これらは PTT パッケージにいくつかある関数 ``main`` を含むモジュールを実行形式にしたものだ。

* :file:`twitter-archiver`
* :file:`twitter-follow`
* :file:`twitter-log`
* :file:`twitter-stream-example`
* :file:`twitterbot`
* :file:`twitter`

本節ではこれらの実行ファイルの利用法を（取り扱いの易しい順に）簡単に述べる。

twitter-follow
======================================================================
モジュール :file:`follow.py` から生成された実行ファイルである。
指定したユーザーが follow しているユーザーや、
逆に follow されているユーザーをリストするのに用いるとよい。

初回実行時
----------------------------------------------------------------------
オプションとして指定するコマンドは何でもよいのだが、コツがふたつある。

* 初回起動時においてはファイル :file:`$HOME/.twitter-follow_oauth` がないことを確認しておく。
* 毎回起動時にコマンドラインオプション ``--oauth`` を指定する。

.. code-block:: console

   $ twitter-follow --oauth --followers showa_yojyo
   Hi there! We're gonna get you all set up to use Twitter-Follow.

   In the web browser window that opens please choose to Allow
   access. Copy the PIN number that appears on the next page and paste or
   type it here:

   Opening: https://api.twitter.com/oauth/authorize?oauth_token=XXXXXXXXXXXXXXXXXXXXXXXXXXX

   Please enter the PIN: XXXXXXX

   That's it! Your authorization keys have been written to ~/.twitter-follow_oauth.
   Browsing showa_yojyo followers, new: 25
   Resolving user ids to screen names: 25/25
   b'xxxxxxxxxxx01'
   b'xxxxxxxxxxx02'
   ...
   Total followers for showa_yojyo: 25

#. コマンドライン入力後、ほぼ即座にウェブブラウザーがアクティブになる。
   上記 URL は Twitter の認証画面である。
   コンソールにはプロンプト ``Please enter the PIN:`` までが出力されている。

#. ブラウザーでユーザーのログイン情報プラス Twitter-Follow にアクセス許可を与える。

#. するとブラウザーが PIN 番号画面を表示する。
   この番号をコンソールの ``Please enter the PIN:`` のプロンプトでタイプする。

#. これにより、テキストファイル :file:`~/.twitter-follow_oauth` が生成される。
#. 以降、サブコマンドの処理が実行される。
   この例の場合では私の follower 全員の screen name をコンソールに出力する。

二回目以降
----------------------------------------------------------------------
初回実行時の ``Hi there!`` から ``That's it!`` までの処理は簡略化され、
いきなり ``Browsing`` から処理が始まるかのように見える。

不具合
----------------------------------------------------------------------
オプション ``--ids`` が機能しない。
各行の先頭に Twitter ユーザーの user_id を示すようにするもので、
利用できれば確かに便利だ。

.. code-block:: console

   $ twitter-follow.exe -o -r -i showa_yojyo
   Browsing showa_yojyo followers, new: 25
   Resolving user ids to screen names: 25/25
   Traceback (most recent call last):
     File "d:\python35\lib\runpy.py", line 170, in _run_module_as_main
       "__main__", mod_spec)
     File "d:\python35\lib\runpy.py", line 85, in _run_code
       exec(code, run_globals)
     File "D:\Python35\Scripts\twitter-follow.exe\__main__.py", line 9, in <module>

     File "d:\python35\lib\site-packages\twitter\follow.py", line 241, in main
       print(str(uid) + "\t" + users[uid].encode("utf-8"))
   TypeError: Can't convert 'bytes' object to str implicitly

twitter-log
======================================================================
モジュール :file:`logger.py` から生成された実行ファイルである。
コマンドラインオプションが単純なので、利用法で困ることはない。
コツとしては任意指定引数の ``max_id`` をなるべく明示的に指定するとよい。
あらかじめ不要とわかっているツイートをリクエストせずに済ませられる。

.. code-block:: console

   $ twitter-log showa_yojyo 665555132273192960 > mylog.txt
   Hi there! We're gonna get you all set up to use the Python Twitter Logger.

   In the web browser window that opens please choose to Allow
   access. Copy the PIN number that appears on the next page and paste or
   type it here:

   Opening: https://api.twitter.com/oauth/authorize?oauth_token=XXXXXXXXXXXXXXXXXXXXXXXXXXX

   Please enter the PIN: XXXXXXX

   That's it! Your authorization keys have been written to ~/.twitter_log_oauth.

   Processed 200 tweets (max_id 654306485879590912)
   Processed 399 tweets (max_id 643085522257055744)
   Processed 598 tweets (max_id 628606432930197504)
   ...
   Processed 3186 tweets (max_id 474969803539496961)
   That's it, we got all the tweets we could. Done.

#. 初回起動時のみ、例によってコマンドライン入力後にウェブブラウザーがアクティブになる。
   コンソールにはプロンプト ``Please enter the PIN:`` までが出力されている。
   ブラウザーには「アカウントの利用を許可しますか」画面が出ているので、
   自分の Twitter ユーザーログイン情報を入力して「連携アプリを認証」ボタンを押す。

#. ブラウザーが PIN 番号画面を表示するので、先程と同様にする。

#. テキストファイル :file:`$HOME/.twitter_log_oauth.` が生成される。

#. あとはツイートを取得して標準出力が指定したテキストファイルに、
   進捗が標準エラー出力で確認できる。
   テキストファイルの内容は次のようなデータが延々と続くハズ。

   .. code-block:: text

      showa_yojyo 665555132273192960
      Date: Sat Nov 14 15:41:23 +0000 2015


          体が冷える。


      showa_yojyo 665213539838136321
      Date: Fri Nov 13 17:04:01 +0000 2015


          変なメンホン。5200 でファイナルアンサー？ https://t.co/VIBF8QBRQg


      showa_yojyo 665209925069484036
      Date: Fri Nov 13 16:49:39 +0000 2015


          候補アカウントをかき集めるのは自動でよいのだが、最終確認（＝これが本当にボットなのか）がどうしても人力任せになる。ここを早く解決しないと面白くない。


      ...

   実際は出力書式が若干ズレて、メッセージ、ユーザー、日付の順にテキストが出力された。

気になる点
----------------------------------------------------------------------
* 取得するツイートの上限は 3200 決め打ち。この値は気になる。
  Twitter のドキュメントによると
  API ``statuses/user_timeline`` の ``count`` として与えられる値は 
  <up to a maximum of 200 per distinct request> とされている。
  しかしこのスクリプトの実装では 3200 を与えている。

* 得られるツイートは指定した ID よりも古いものだけであることに注意。

* もっとツイートを取得したい場合は、得られた最後のツイート ID を
  次回 twitter-log 実行時の ``max_id`` 引数に指定することで可能。
  というインターフェイスに見えるが、実際に試してみるとそうはならなかった。
  前回取得した最後のツイートより古いものがどうしても得られなかった。

この辺りの細かい振る舞いをカスタマイズしたければ、
もう :file:`logger.py` をコピーして編集して自分のスクリプト箱に入れるほかない。

twitter-archiver
======================================================================
モジュール :file:`archiver.py` から生成された実行ファイルである。
主な機能は次のとおり（括弧内は実装が利用する Twitter API の名前）。

* (application/rate_limit_status) 自分の API 利用制限状況を出力する。
* (statuses/user_timeline, statuses/home_timeline) 指定ユーザーのタイムラインをアーカイブする。
* (statuses/mentions_timeline) 指定ユーザーのツイートで、
  内容に ``@screen_name`` みたいなパターンを含むものをアーカイブする。
* (favorites/list) 指定ユーザーのツイートブックマークをアーカイブする。
* (direct_messages, direct_messages/sent) 指定ユーザーに送られたダイレクトメッセージや、
  反対にユーザーが送ったダイレクトメッセージをアーカイブする。

初回起動
----------------------------------------------------------------------
いい具合に API の利用制限状況を見るだけのモードがあるので、
それを利用して認証を済ませよう。

.. code-block:: console

   $ twitter-archiver -o -a showa_yojyo
   Hi there! We're gonna get you all set up to use Twitter-Archiver.

   In the web browser window that opens please choose to Allow
   access. Copy the PIN number that appears on the next page and paste or
   type it here:

   Opening: https://api.twitter.com/oauth/authorize?oauth_token=XXXXXXXXXXXXXXXXXXXXXXXXXXX

   Please enter the PIN: XXXXXXX

   That's it! Your authorization keys have been written to ~/.twitter-archiver_oauth.
   Remaining API requests: 179/180 (interval limit)
   Next reset in 897s (Wed Nov 18 23:07:14 2015)

これまでの各ツールと同様、認証キーが記されたテキストファイルがディレクトリー ``$HOME`` に生成される。
上記の最後の 2 行だけが本来のコマンドの出力である。
あと 179 回のリクエストが 897 秒以内において許されている。

mentions
----------------------------------------------------------------------
オプション ``--mentions <file>`` により、
指定ユーザーに話しかけているツイートをアーカイブすることができる。

.. code-block:: console

   $ twitter-archiver -o -m showa_yojyo
   * Archiving own mentions in .\showa_yojyo
   Browsing home statuses, new tweets: 102
   Total mentions: 102
   Total: 0 tweets (0 new) for 0 users

ファイルの中身はこのような感じだった。

.. code-block:: text

   170145264236118018 b'2012-02-16 22:59:26 JST <showa_yojyo> @showa_yojyo \xe8\x8b\xa5\xe3\x81\x84\xe3\x83\xaa\xe3\x83\x93\xe3\x82\xb8\xe3\x83\xa7\xe3\x83\xb3\xe3\x81\xab\xe8\xa1\xa8\xe3\x81\xab\xe5\x87\xba\xe3\x81\x97\xe3\x81\x9f\xe3\x81\x8f\xe3\x81\xaa\xe3\x81\x84\xe5\x80\x8b\xe4\xba\xba\xe6\x83\x85\xe5\xa0\xb1\xe3\x81\x8c\xe3\x81\x82\xe3\x82\x8a\xe3\x81\x9d\xe3\x81\x86\xe3\x81\xa0\xe3\x81\x8b\xe3\x82\x89\xe3\x80\x81\xe3\x81\x9d\xe3\x82\x8c\xe3\x81\xaf\xe3\x82\x84\xe3\x82\x81\xe3\x80\x82\xe3\x83\x90\xe3\x83\x83\xe3\x82\xaf\xe3\x82\xa2\xe3\x83\x83\xe3\x83\x97\xe6\xb6\x88\xe5\xa4\xb1\xe3\x81\xae\xe3\x81\xbb\xe3\x81\x86\xe3\x81\x8c\xe3\x83\x9e\xe3\x82\xb7\xe3\x80\x82'
   171595193252986880 b'2012-02-20 23:00:56 JST <showa_yojyo> Try to retweet; RT: @showa_yojyo: Echofon http://t.co/Gt8X5bwM'
   172319721562189824 b'2012-02-22 22:59:57 JST <showa_yojyo> @showa_yojyo \xe5\xbc\xb7\xe3\x81\x84\xe3\x81\xa6\xe3\x82\x84\xe3\x82\x8b\xe3\x81\xaa\xe3\x82\x89 #cplusplus \xe3\x81\xa7\xe6\xa4\x9c\xe7\xb4\xa2\xe3\x81\x99\xe3\x82\x8b\xe3\x81\x97\xe3\x81\x8b\xe3\x81\xaa\xe3\x81\x95\xe3\x81\x9d\xe3\x81\x86\xe3\x81\xa0\xe3\x80\x82\xe3\x81\x93\xe3\x82\x8c\xe3\x81\x8b\xe3\x82\x89\xe3\x81\xaf C++ \xe3\x82\x92\xe6\x8d\xa8\xe3\x81\xa6\xe3\x81\xa6\xe7\x94\x9f\xe3\x81\x8d\xe3\x81\xa6\xe3\x81\x84\xe3\x81\x8f\xe3\x81\x93\xe3\x81\xa8\xe3\x81\xab\xe3\x81\xaa\xe3\x82\x8b\xe3\x81\x8b\xe3\x82\x82\xe3\x81\xaa\xe3\x81\x81\xe3\x80\x82'
   172661701282496512 b'2012-02-23 21:38:52 JST <showa_yojyo> @showa_yojyo \xe3\x82\xbf\xe3\x82\xb0\xe3\x81\xa8\xe3\x81\x97\xe3\x81\xa6\xe3\x81\xaf #cpp \xe3\x81\xae\xe3\x81\xbb\xe3\x81\x86\xe3\x81\x8c\xe5\x84\xaa\xe5\x8b\xa2\xe3\x81\xa0\xe3\x81\xa3\xe3\x81\x9f\xe6\xa8\xa1\xe6\xa7\x98\xe3\x80\x82'
   ...略...
   521103371999010816 b'2014-10-12 10:01:40 JST <awa_shuwa> @showa_yojyo \xe3\x81\x97\xe3\x82\x85\xe3\x82\x8f\xe3\x81\xa3'
   538723478451408897 b'2014-11-30 00:57:40 JST <showa_yojyo> \xe3\x81\x99\xe3\x81\x84\xe3\x81\xbe\xe3\x81\x9b\xe3\x82\x93\xe3\x80\x82\xe5\x8f\xb3\xe3\x82\xaf\xe3\x83\xaa\xe3\x83\x83\xe3\x82\xaf\xe3\x83\xa1\xe3\x83\x8b\xe3\x83\xa5\xe3\x83\xbc\xe3\x81\x8c\xe5\x87\xba\xe3\x81\xaa\xe3\x81\x84\xe3\x80\x82 RT @showa_yojyo: \xe4\xbb\x8a\xe3\x81\xab\xe3\x81\xaa\xe3\x81\xa3\xe3\x81\xa6 Python (command line) \xe3\x82\x92 ConEmu \xe3\x82\xbf\xe3\x83\x96\xe5\x8c\x96\xe3\x81\xa7\xe3\x81\x8d\xe3\x82\x8b\xe3\x82\x88\xe3\x81\x86\xe3\x81\xab\xe3\x81\x97\xe3\x81\x9f\xe3\x80\x82\xe6\xb0\x97\xe4\xbb\x98\xe3\x81\x8f\xe3\x81\xae\xe3\x81\x8c\xe9\x81\x85\xe3\x81\x84\xe3\x80\x82'
   569523049386549248 b'2015-02-23 00:44:10 JST <showa_yojyo> @showa_yojyo \xe3\x82\x84\xe3\x81\xa3\xe3\x81\xb1\xe3\x82\x8a\xe5\x9b\xba\xe3\x81\x84\xe3\x80\x82\xe3\x81\x93\xe3\x81\xae\xe7\xa7\x81\xe3\x81\x8c\xe3\x83\xac\xe3\x83\x99\xe3\x83\xab 300 \xe3\x81\x84\xe3\x81\x8b\xe3\x81\xaa\xe3\x81\x84\xe3\x81\xa8\xe3\x81\x84\xe3\x81\x86\xe3\x81\xae\xe3\x81\xaf\xe3\x81\x8a\xe3\x81\x8b\xe3\x81\x97\xe3\x81\x84\xe3\x80\x82'
   569525223294283777 b'2015-02-23 00:52:49 JST <showa_yojyo> @showa_yojyo \xe4\xbb\x8a\xe3\x81\x95\xe3\x81\xa3\xe3\x81\x8d\xe5\xbe\xa9\xe6\x97\xa7\xe3\x81\x97\xe3\x81\x9f\xe3\x82\x82\xe3\x82\x88\xe3\x81\x86\xe3\x80\x82'

* ツイートが時刻順に古いものから新しいものへ配列されている。
* Python の bytes オブジェクトが出力されているが、
  これは私（人間）が読みにくいのでダメだ。

アーカイブツールということで、次回以降の実行時に以前の出力結果を再利用する。
しかし、そのデータのロードで失敗する。

.. code-block:: console

   $ twitter-archiver -o -m showa_yojyo
   * Archiving own mentions in .\showa_yojyo
   Error when loading saved tweets: name 'unicode' is not defined - continuing without
   Browsing home statuses, new tweets: 102
   Total mentions: 102
   Total: 0 tweets (0 new) for 0 users

当ノート冒頭に宣言したように私は Python 3 系ですべてテストしているのだが、
とっくに廃止されている関数 ``unicode`` がコード中にいることが原因だ。

twitter-stream-example
======================================================================
モジュール :file:`stream_example.py` から生成された実行ファイルである。
何をするツールなのかはよくわからないので、試しながら理解していく。

なお、今回のツールは access token と consumer key/secret を両方ともユーザー自身で用意せねばならない。
これら 4 つのコマンドライン引数をコンソールでタイプするのは骨が折れるので、
その辺は適宜工夫すること。

以下、次のシェル関数を実装したものとして話を進める。

.. code-block:: bash

   function my-stream-example()
   {
       local TOKEN=...
       local TOKEN_SECRET=...
       local CONSUMER_KEY=...
       local CONSUMER_SECRET=...

       twitter-stream-example \
           --token=$TOKEN \
           --token-secret=$TOKEN_SECRET \
           --consumer-key=$CONSUMER_KEY \
           --consumer-secret=$CONSUMER_SECRET \
           "$@"
   }

オプションなしで実行 (statuses.sample)
----------------------------------------------------------------------
コマンドラインオプションなしで twitter-stream-example を実行しよう。
すると、Ctrl+C を押すまでの間は延々と何らかのツイートの垂れ流しが続く。
単に実行開始時点に Twitter のデータベース的なものにある全ツイートを若い順に表示しているだけかもしれない。

.. code-block:: console

   $ my-stream-example
   -- Some data: {'delete': {'timestamp_ms': '1447787581389', 'status': {'id': <censored>, 'user_id': <censored>, 'id_str': '<censored>', 'user_id_str': '<censored>'}}}
   -- Some data: {'delete': {'timestamp_ms': '1447787581463', 'status': {'id': <censored>, 'user_id': <censored>, 'id_str': '<censored>', 'user_id_str': '<censored>'}}}
   -- Some data: {'delete': {'timestamp_ms': '1447787581478', 'status': {'id': <censored>, 'user_id': <censored>, 'id_str': '<censored>', 'user_id_str': '<censored>'}}}
   -- Some data: {'delete': {'timestamp_ms': '1447787581492', 'status': {'id': <censored>, 'user_id': <censored>, 'id_str': '<censored>', 'user_id_str': '<censored>'}}}
   -- Some data: {'delete': {'timestamp_ms': '1447787581544', 'status': {'id': <censored>, 'user_id': <censored>, 'id_str': '<censored>', 'user_id_str': '<censored>'}}}
   -- Some data: {'delete': {'timestamp_ms': '1447787581543', 'status': {'id': <censored>, 'user_id': <censored>, 'id_str': '<censored>', 'user_id_str': '<censored>'}}}
   -- Some data: {'delete': {'timestamp_ms': '1447787581530', 'status': {'id': <censored>, 'user_id': <censored>, 'id_str': '<censored>', 'user_id_str': '<censored>'}}}
   -- Some data: {'delete': {'timestamp_ms': '1447787581631', 'status': {'id': <censored>, 'user_id': <censored>, 'id_str': '<censored>', 'user_id_str': '<censored>'}}}
   @<censored>
   @<censored>
   Follow back?
   RT @<censored>: Gingrich: "Madness And Suicidal" To Bring In More Syrian Refugees https://t.co/UPVSXTG0Ss
   RT @<censored>: *shops online instead of doing work in class*
   RT @<censored>: no respiro wey

   #1DMX https://t.co/6wrea3Od9c
   -- Some data: {'delete': {'timestamp_ms': '1447787581702', 'status': {'id': <censored>, 'user_id': <censored>, 'id_str': '<censored>', 'user_id_str': '<censored>'}}}
   RT @<censored>: ・・#1DJP
   ・・#1DJP
   ・・#1DJP
   ・・#1DJP
   ・・#1DJP
   ・・#1DJP
   ・・#1DJP
   ・・#1DJP
   ・・#1DJP
   ・・#1DJP
   ・・#1DJP
   ・・#1DJP
   ・・#1DJP
   ・・#1DJ窶ｦ
   @<censored> ・ｴ・､ ・們・・・・ｬ・ｰ ・ｬ・・擽・ｼ・・ ・們┳﨑們強・懍丶 嵭・・・・
   﨑ｨ・､. ・駆捩 ・川峡 ・ｴ・ｴ・ｭ・懍丶
   This bus is a mess yikes
   pad thai never fails
   螳壽悄縲螳壽悄縲https://t.co/01ZIMlUU4j
   讙ｻ譛医■繧・ｓ縺ｮ蟆剰ｪｬ縺ｧ縺呻ｼ・ｼ・ｼ∵弍髱櫁ｪｭ繧薙〒縺上□縺輔＞・・ｼ・
   RT @<censored>: Kitaplarﾄｱn ﾅ歛rjﾄｱ bitmez, bisikletler benzin zammﾄｱndan etkilenmez. Bir kitap bir bisiklet. ﾃ奔gﾃｼrlﾃｼk ucuzdur坿燈
   RT @<censored>: https://t.co/eH1XxgX66I
   @<censored> @<censored> 繧｢繧､繧ｹ縺翫▲縺ｱ縺・Γ繝ｭ繝ｳ繝代Φ縺ｨ縺ｯ・・^o^)・ｼ
   RT @<censored>: Tenho tanta coisa para fazer para amanhﾃ｣ q acho q ficar nosofﾃ｡ ﾃｩ a melhor soluﾃｧﾃ｣o
   -- Some data: {'delete': {'timestamp_ms': '1447787581673', 'status': {'id': <censored>, 'user_id': <censored>, 'id_str': '<censored>', 'user_id_str': '<censored>'}}}
   @<censored> ・溢搆 ・甯醐葺・・､..
   Have you ever wondered what bus drivers talk about? They talk about being stuckin traffic.... ・#thestruggleisreal
   @<censored> @<censored> @<censored> no joke. So beautiful.
   -- Some data: {'delete': {'timestamp_ms': '1447787581693', 'status': {'id': <censored>, 'user_id': <censored>, 'id_str': '<censored>', 'user_id_str': '<censored>'}}}
   #CWHIranDebate Lily gave us a lot to think about with her opening statement. Very compelling argument, especially with school bus mention.
   Taken #1DTR
   Sﾃｩ que soy muy pesadito con el tema, pero de verdad, pan de molde sin corteza mﾃ｡s chocolate Nesquik es una combinaciﾃｳn ganadora.
   RT @<censored>: @<censored> glad you like it. Thank you
   Traceback (most recent call last):
     ...略...
   KeyboardInterrupt

* 一部出力を加工した。
* 文字化けをしているのは私の端末環境がショボいのも一因（ここに記す場合に限っては、文字化けしているほうが好都合）。
  Mintty でシェルを起動するなり、
  文字コードをあらかじめ ``chcp 65001`` で変えるなり、
  パイプで less にテキストを流し込むなりするとマシになる。

オプション track-keywords を指定して実行 (statuses.filter)
----------------------------------------------------------------------
オプション track-keywords を指定して実行すると、
Twitter 検索のライブバージョンのように振る舞うのではないかと期待して実行する。

.. code-block:: console

   $ my-stream-example --track-keywords="Terror France"
   [France 24 fr] Cinq ex-"terroristes" demandent la suspension de leur déchéance de nationalité: Cinq ex-"terror... https://t.co/WKD8KzXTnG
   Belgium questioned 'terror brothers' before Paris attacks - but didn't tell France https://t.co/YhqSavbWKz
   RT @<censored>: Huck's 1 Min Response- Terror in France #gop #ccot #tcot #pjnet #imwithhuck #trump2016 https://t.co/BJGSjk07Kw … … https:…
   RT @<censored>: World supports France, ignores other terror attacks  [VIDEO] https://t.co/DKdloeu1Qs @<censored> https://t.co/yBnsEk3GKK
   Podemos DEFIENDE al grupo terrorista vasco ETA https://t.co/jjdaxqgQvm Podemos DEFENDS Basque terrorist group ETA  https://t.co/zMM2JvQuqg
   Belgium questioned 'terror brothers' before Paris attacks - but didn't tell France https://t.co/LCsfl8s9rJ LiveLeak #News
   RIP Diesel The Police Dog Killed In The Crazy France Terror Raids Early This Morning https://t.co/Mb0fLPpKVR https://t.co/AuoGnWS8uq
   Netanyahu called Hollande, said Israel stands w France in fight against terror,problem is international, and so is the solution.
   RIP Diesel The Police Dog Killed In The Crazy France Terror Raids Early This… https://t.co/CwfvmXk84W @<censored> https://t.co/uutbBtTeUT

   KeyboardInterrupt

* 一部出力を加工した。

オプション user-stream を指定して実行 (user)
----------------------------------------------------------------------
オプション user-stream をして実行すると Twitter API の site が適用される。

.. code-block:: console

   $ my-stream-example --user-stream
   -- Some data: {'friends': []}

おそらく自分に関係する Twitter イベントがリアルタイムで閲覧できる。
例えばこのツールを起動している間に、誰かが私のツイートをリツイートしたとする。
すると「誰それがリツイートした」のようなメッセージがコンソールに出力されるものと思われる。

オプション site-stream を指定して実行 (site)
----------------------------------------------------------------------
オプション site-stream をして実行すると Twitter API の site が適用される。
しかし Twitter のドキュメントによると <Site Streams is currently in a closed beta.
Applications are no longer being accepted> とのことなので、
これは動作を期待できない。

.. code-block:: console

   $ my-stream-example --site-stream
   Traceback (most recent call last):
     File "d:\python35\lib\site-packages\twitter\stream.py", line 207, in handle_stream_response
       handle = urllib_request.urlopen(req,)
     ...
   urllib.error.HTTPError: HTTP Error 403: Forbidden
   ...

twitterbot
======================================================================
モジュール :file:`ircbot.py` から生成された実行ファイルである。
自分のタイムラインから screen_name を検索しては follow したり unfollow したりするツールのようだ。
したがって本稿では割愛する。

twitter
======================================================================
モジュール :file:`cmdline.py` から生成された実行ファイルである。
次の Twitter API にアクセスするコマンドラインツールとなっている。

* account.verify_credentials
* application.rate_limit_status
* friendships.create
* friendships.destroy
* lists.list
* statuses.home_timeline
* statuses.mentions_timeline
* statuses.update

他のツールと同様に初回だけ認証作業が必要になるので、
最初はそのためにあるコマンドを実行する。
それ以降は、その他の Twitter データを操作するためのコマンドを実行していこう。

コマンド authorize
----------------------------------------------------------------------
コマンド authorize を実行することで、
次回以降の実行に備えるべく次のものを生成しておきたい。

* 認証キー格納ファイル :file:`$HOME/.twitter_oauth`

.. code-block:: console

   $ twitter authorize
   Hi there! We're gonna get you all set up to use the Command-Line Tool.

   In the web browser window that opens please choose to Allow
   access. Copy the PIN number that appears on the next page and paste or
   type it here:

   Opening: https://api.twitter.com/oauth/authorize?oauth_token=XXXXXXXXXXXXXXXXXXXXXXXXXXX

   Please enter the PIN: XXXXXXX

   That's it! Your authorization keys have been written to ~/.twitter_oauth.

コマンド follow
----------------------------------------------------------------------
コマンド follow は指定のユーザーを follow する。私は使わない。

コマンド friends
----------------------------------------------------------------------
コマンド friends はホームタイムラインを出力する。
ちなみにこのツールのデフォルトのコマンドはこれなので、コマンド名の入力を省略できる。

.. code-block:: console

   $ [work tmp 243]$ twitter friends -dt
   2015-11-16 01:47:40 @<censored> Your branch is ahead of なんちゃらのコミット数とプッシュされたコミット数が一致していないだと？
   2015-11-16 02:05:26 @<censored> 今日の頭ハネ。カンニンしてくれ。 https://t.co/I4igUP7ai7
   ...
   2015-11-19 01:48:40 @<censored> [notebook] https://t.co/ekdItM0nh0 showa_yojyo- (scripts.rst) Update twitter-stream-example.

* オプション ``--datestamp`` と ``--timestamp`` でツイート更新時刻を出力する。
* デフォルトで 20 件出力。オプション ``--length <count>`` で最大 200 までならば取得数指定可能。
* ツイートの並び順は古い順。

コマンド leave
----------------------------------------------------------------------
コマンド leave は指定のユーザーを unfollow する。私は使わない。

コマンド mylist
----------------------------------------------------------------------
コマンド mylist は自分の作成リストと購読リストの両方を出力する。
リスト名と説明だけを表示するのでたいへん単純だ。
そして余計な空行が気になる。

.. code-block:: console

   $ twitter mylist
   【MJ5】Twitter連動

   Everything O'Reilly

   Fenrir Inc.                    (フェンリルの公式アカウントなど。)

   日経グループ                         (日経グループ内の公式アカウントのリストです。
   #WelcomeToTwitter)

   followed-by                    (People who follow(ed) me for a fixed period. For some reason some followers are not included.)

   videogame                      (Accounts related to videogame productions, amusement facilities, etc.)

   informative                    (Accounts of people or organizations that supplyeveryone helpful information and knowledge.)

   tools                          (Accounts that inform of software, hardware, events, bug-fixes, release schedules, etc.)

   bot                            (A list of amusing bot accounts.)

   ...

コマンド list
----------------------------------------------------------------------
コマンド list は指定ユーザーの作成リストと購読リストの両方を出力する。
上述の mylist コマンドと酷似しているので詳細は省略。

.. code-block:: console

   $ twitter mylist twitter
   Developers                     (Learn how to build with Twitter from our platform relations teams and developer advocates.)

   Twitter & IR                   (Investment news and company updates.)

   International                  (Accounts highlighting local Twitter news, stories and more from our teams around world. )

   Support                        (Learn how to boost your Twitter skills and keepyour account secure.)

   Media                          (Discover the best content on Twitter from media, entertainment, sports, government and more.)

   Engineering                    (Tweets from Twitter's engineering teams about our technology, tools and events.)

   Offices & Culture              (See how we're building Twitter together, from our offices around the world.)

   Ads & Sales                    (Follow these accounts for Twitter Ads product updates, tips, success stories and support.)

   Official Twitter Accounts      (Accounts managed by Twitter, Inc.)

コマンド pyprompt
----------------------------------------------------------------------
コマンド pyprompt は対話モードで ``twitter`` オブジェクトを操作できる。
ちょっとくせがあるので使いにくい。

コマンド rate
----------------------------------------------------------------------
コマンド rate は Twitter API の利用制限状況を一覧するのにたいへん便利。
出力行数がかなり多いので、ファイルにリダイレクトするとよい。

.. code-block:: console

   $ twitter rate
   Remaining API requests for /blocks/list: 15 / 15
   Next reset in 897s (Thu Nov 19 23:35:07 2015)

   Remaining API requests for /blocks/ids: 15 / 15
   Next reset in 897s (Thu Nov 19 23:35:07 2015)

   Remaining API requests for /direct_messages/show: 15 / 15
   Next reset in 897s (Thu Nov 19 23:35:07 2015)

   Remaining API requests for /direct_messages: 15 / 15
   Next reset in 897s (Thu Nov 19 23:35:07 2015)

   ...

コマンド repl
----------------------------------------------------------------------
コマンド repl は対話モードでオブジェクト ``t`` と ``u`` を操作するものだ。
困ったことに ``t`` の使い方はよく知っているが ``u`` の使い方がわからない。

.. code-block:: console

   $ twitter repl

   Use the 'twitter' object to interact with the Twitter REST API.
   Use twitter_upload to interact with upload.twitter.com


   Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
   Type "help", "copyright", "credits" or "license" for more information.
   (InteractiveConsole)
   >>> u
   <twitter.api.Twitter object at 0x00000080581EAAC8>
   >>> u.domain
   'upload.twitter.com'
   >>> t
   <twitter.api.Twitter object at 0x00000080564A2470>
   >>> t.domain
   'api.twitter.com'

コマンド replies
----------------------------------------------------------------------
コマンド replies は自分への返信ツイートを発生時刻の古い順に出力する。
オプションはコマンド friends と同じように通じる。

コマンド search
----------------------------------------------------------------------
これは動作しない。検索ならば別のツールを使うのがよい。

.. code-block:: console

   $ twitter search Abandaned
   Twitter sent status 410 for URL: search.json using parameters: (...)
   details: {'errors': [{'message': 'The Twitter REST API v1 is no longer active. Please migrate to API v1.1. https://dev.twitter.com/docs/api/1.1/overview.', 'code': 64}]}
   Use 'twitter -h' for help.

コマンド set
----------------------------------------------------------------------
コマンド set は名前からはそれとわかりにくいが、ツイートを生成する。

.. code-block:: console

   $ twitter set "もっとモット日本語テスト"
   $ twitter -l1
   @showa_yojyo もっとモット日本語テスト

コンソールからの実行ゆえ、日本語文字やハッシュタグ # の扱いに気をつけること。

コマンド shell
----------------------------------------------------------------------
コマンド shell は対話モードでスクリプトを起動する。
プロンプトで通常のコマンドライン引数をタイプすることになる。

.. code-block:: console

   $ twitter shell -dt
   twitter> ppp
   No such action: ppp
   twitter> replies -l 3
   2014-11-30 00:57:40 @showa_yojyo すいません。右クリックメニューが出ない。 RT @showa_yojyo: 今になって Python (command line) を ConEmu タブ化できるようにした。気付くのが遅い。
   2015-02-23 00:44:10 @showa_yojyo @showa_yojyo やっぱり固い。この私がレベル 300 いかないというのはおかしい。
   2015-02-23 00:52:49 @showa_yojyo @showa_yojyo 今さっき復旧したもよう。
   twitter> set 日本語テスト
   twitter> friends -l 3
   2015-11-19 00:57:33 @showa_yojyo 六萬は下家が暗刻で固めていた。5200 でいいや。
   2015-11-19 01:48:40 @showa_yojyo [notebook] https://t.co/ekdItM0nh0 showa_yojyo - (scripts.rst) Update twitter-stream-example.
   2015-11-19 22:49:53 @showa_yojyo 日本語テスト
   twitter> exit

寸評
======================================================================
手直しして自分の利用パターンに特化したツールとするのもアリ。

.. include:: /_include/python-refs-twitter.txt
