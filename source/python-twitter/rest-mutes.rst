======================================================================
ミュート関連
======================================================================
個人的には一切利用するつもりのない Twitter のミュート機能だ。
ミュート機能のインターフェイスはブロック機能のそれと酷似しているので、
書かなくてもよいかという気はするが、ノートの凝集度を上げるために記す。

.. contents::

POST mutes/users/create
======================================================================
POST mutes/create を用いれば特定のユーザーをミュートすることができる。
こうすれば、ミュートされたユーザーのツイートは自分の所有タイムラインに出てこなくなるらしい。

次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/mutes-users-create.py
   :language: python3

* [1] Twitter ユーザーを指定する。
  他の機能と同様に ``user_id`` または ``screen_name`` のどちらか一方の形式で指定する。

* [2] とりあえずミュートしたユーザーの情報を画面に出力する。

次に実行例を示す。自分で自分をミュートしよう。

.. code-block:: console

   $ ./mutes-users-create.py
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
     File "./mutes-users-create.py", line 14, in <module>
       response = tw.mutes.users.create(screen_name='showa_yojyo')
     File "D:\Python35\lib\site-packages\twitter\api.py", line 312, in __call__
       return self._handle_response(req, uri, arg_data, _timeout)
     File "D:\Python35\lib\site-packages\twitter\api.py", line 345, in _handle_response
       raise TwitterHTTPError(e, uri, self.format, arg_data)
   twitter.api.TwitterHTTPError: Twitter sent status 403 for URL: 1.1/mutes/users/create.json using parameters: (oauth_consumer_key=...)
   details: {'errors': [{'code': 271, 'message': "You can't mute yourself."}]}

ブロックのときとおおむね同様の展開となった。

POST mutes/users/destroy
======================================================================
POST mutes/users/destroy は既にミュートしていたユーザーのミュートを解除する機能だ。

次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/mutes-users-destroy.py
   :language: python3

* [1] 認められるパラメーターは上述の POST mutes/users/destroy と同じだ。
* [2] 解除対象のユーザーの情報を画面に出力する。

次に実行例を示す。ミュートしていないはずの自分を指定解除するとこうなる。

.. code-block:: console

   $ ./mutes-users-destroy.py
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
     File "./mutes-users-destroy.py", line 14, in <module>
       response = tw.mutes.users.destroy(screen_name='showa_yojyo')
     File "D:\Python35\lib\site-packages\twitter\api.py", line 312, in __call__
       return self._handle_response(req, uri, arg_data, _timeout)
     File "D:\Python35\lib\site-packages\twitter\api.py", line 345, in _handle_response
       raise TwitterHTTPError(e, uri, self.format, arg_data)
   twitter.api.TwitterHTTPError: Twitter sent status 403 for URL: 1.1/mutes/users/destroy.json using parameters: (oauth_consumer_key=...)
   details: {'errors': [{'code': 272, 'message': 'You are not muting the specified user.'}]}

ミュート解除はブロック解除とは異なり、常識的なエラーが返ってくる。

GET mutes/users/ids
======================================================================
GET mutes/users/ids は現時点で自分がミュートしているユーザーの ID を列挙する機能だ。
パラメーターは基本的には ``cursor`` があるだけだ。
多数のユーザーをミュートしている場合には基本編で述べた技法でリクエストを反復し、
データを取得するとよい。

次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/mutes-users-ids.py
   :language: python3

* [1] 私は誰もミュートしていないので、カーソル処理は行わない。
  ゆえにパラメーターは何も与えない。

* [2] 得られたデータを画面に出力する。

次に実行例を示す。

.. code-block:: console

   $ mutes-users-ids.py
   {
       "previous_cursor": 0,
       "next_cursor": 0,
       "next_cursor_str": "0",
       "ids": [],
       "previous_cursor_str": "0"
   }

空のデータが戻ってきた。

GET mutes/users/list
======================================================================
GET mutes/users/list は現時点で自分がミュートしているユーザーの情報を列挙する機能だ。

次にサンプルコードを示す。

.. literalinclude:: /_sample/ptt/mutes-users-list.py
   :language: python3

* [1] 私は誰もブロックしていないので、カーソル処理は行わない。
  ゆえにパラメーターは何も与えない。

  ここでは省略するが、
  オプション ``include_entities`` や ``skip_status`` を指定することも可能だ。

* [2] 得られたデータを画面に出力する。

次に実行例を示す。

.. code-block:: console

   $ ./mutes-users-ids.py
   {
       "previous_cursor": 0,
       "next_cursor": 0,
       "next_cursor_str": "0",
       "ids": [],
       "previous_cursor_str": "0"
   }

空のデータが戻ってきた。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
