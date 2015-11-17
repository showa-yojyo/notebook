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

* 初回起動時においてはファイル :file:`~/.twitter-follow_oauth` がないことを確認しておく。
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

.. todo::

   * 実際に初回起動
   * 実際に各オプションを試す

twitter-stream-example
======================================================================
モジュール :file:`stream_example.py` から生成された実行ファイルである。

.. todo:: 何か書く。

twitterbot
======================================================================
モジュール :file:`ircbot.py` から生成された実行ファイルである。

.. todo:: 何か書く。

twitter
======================================================================
モジュール :file:`cmdline.py` から生成された実行ファイルである。

.. todo:: 何か書く。

.. include:: /_include/python-refs-twitter.txt
