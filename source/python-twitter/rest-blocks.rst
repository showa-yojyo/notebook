======================================================================
ブロック関連
======================================================================
個人的には一切利用するつもりのない Twitter のブロック機能だが、
ノートの凝集度を上げるために記す。

.. contents::

POST blocks/create
======================================================================
POST blocks/create を用いれば特定のユーザーをブロックすることができる。
ところでブロック操作を多用すると、
ブロックをしたユーザーのほうが Twitter によってブラックリストに入るという噂を聞いたが、
事実なのだろうか。

次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/blocks-create.py
   :language: python3

* [1] Twitter ユーザーを指定する。
  他の機能と同様に ``user_id`` または ``screen_name`` のどちらか一方の形式で指定する。

  この他にもオプションとして ``include_entities`` と ``skip_status`` というフラグがあるが、
  これからブロックをしようというユーザーの情報などどうでもよいので、意識して利用はしないだろう。

* [2] とりあえずブロックしたユーザーの情報を画面に出力する。

次に実行例を示す。私が私をブロックしようとするとこうなる。

.. code:: console

   $ ./blocks-create.py
   Traceback (most recent call last):
     File "D:\Python35\lib\site-packages\twitter\api.py", line 319, in _handle_response
       handle = urllib_request.urlopen(req, **kwargs)
     File "D:\Python35\lib\urllib\request.py", line 162, in urlopen
       return opener.open(url, data, timeout)
     File "D:\Python35\lib\urllib\request.py", line 471, in open
       response = meth(req, response)
     File "D:\Python35\lib\urllib\request.py", line 581, in http_response
       'http', request, response, code, msg, hdrs)
     File "D:\Python35\lib\urllib\request.py", line 509, in error
       return self._call_chain(*args)
     File "D:\Python35\lib\urllib\request.py", line 443, in _call_chain
       result = func(*args)
     File "D:\Python35\lib\urllib\request.py", line 589, in http_error_default
       raise HTTPError(req.full_url, code, msg, hdrs, fp)
   urllib.error.HTTPError: HTTP Error 403: Forbidden

   During handling of the above exception, another exception occurred:

   Traceback (most recent call last):
     File "./blocks-create.py", line 14, in <module>
       response = tw.blocks.create(screen_name='showa_yojyo')
     File "D:\Python35\lib\site-packages\twitter\api.py", line 312, in __call__
       return self._handle_response(req, uri, arg_data, _timeout)
     File "D:\Python35\lib\site-packages\twitter\api.py", line 345, in _handle_response
       raise TwitterHTTPError(e, uri, self.format, arg_data)
   twitter.api.TwitterHTTPError: Twitter sent status 403 for URL: 1.1/blocks/create.json using parameters: (oauth_consumer_key=...)
   details: {'errors': [{'message': "Sorry, you can't block yourself.", 'code': 147}]}

POST blocks/destroy
======================================================================
POST blocks/destroy は既にブロックしていたユーザーのブロックを解除する機能だ。

次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/blocks-destroy.py
   :language: python3

* [1] 認められるパラメーターは上述の POST blocks/create と同じだ。
* [2] ブロック解除対象のユーザーの情報を画面に出力する。

次に実行例を示す。ブロックしていないはずの自分を解除するとこうなる。

.. code:: console

   $ ./blocks-destroy.py
   {
       "contributors_enabled": false,
       ...
       "screen_name": "showa_yojyo",
       ...
   }

便宜上こういう動作にしてあるのだと思うが、自分のユーザーオブジェクトが得られる。

GET blocks/ids
======================================================================
GET blocks/ids は現時点で自分がブロックしているユーザーの ID を列挙する機能だ。
パラメーターは基本的には ``cursor`` があるだけだ。
多数のユーザーをブロックしている場合には基本編で述べた技法でリクエストを反復し、
データを取得するとよい。

次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/blocks-ids.py
   :language: python3

* [1] 私は誰もブロックしていないので、カーソル処理は行わない。
  ゆえにパラメーターは何も与えない。

* [2] 得られたデータを画面に出力する。

次に実行例を示す。

.. code:: console

   $ ./blocks-ids.py
   {
       "ids": [],
       "next_cursor": 0,
       "next_cursor_str": "0",
       "previous_cursor": 0,
       "previous_cursor_str": "0"
   }

空のデータが戻ってきた。

GET blocks/list
======================================================================
GET blocks/list は現時点で自分がブロックしているユーザーの情報を列挙する機能だ。

次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/blocks-list.py
   :language: python3

* [1] 私は誰もブロックしていないので、カーソル処理は行わない。
  ゆえにパラメーターは何も与えない。

  なお、GET blocks/list はユーザオブジェクトを取得するものなので、
  オプション ``include_entities`` や ``skip_status`` を指定することも可能だ。

* [2] 得られたデータを画面に出力する。

次に実行例を示す。

.. code:: console

   $ ./blocks-list.py
   {
       "ids": [],
       "next_cursor": 0,
       "next_cursor_str": "0",
       "previous_cursor": 0,
       "previous_cursor_str": "0"
   }

空のデータが戻ってきた。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
