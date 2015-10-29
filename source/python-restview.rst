======================================================================
Restview 利用ノート
======================================================================
本章では Python_ のサードパーティー製パッケージである Restview_ の利用に関することを記す。

本ノートが Sphinx_ を利用しているため、このツールの利用状況はかなり限定的になる。
具体例を挙げると ``README.rst`` のような、
Sphinx のビルド対象外の孤立した rst ファイルの確認に用いる。

.. contents::

.. note::

   本稿執筆時の動作環境は次のとおり。

   * OS: Windows 10 Home x64
   * Python_: 3.5.0
   * Restview_: 2.5.0

インストール
======================================================================
いつものように ``pip install`` によりパッケージをインストールする。

.. code-block:: console

   $ pip install restview
   Collecting restview
     Downloading restview-2.5.0-py2.py3-none-any.whl
   Requirement already satisfied (use --upgrade to upgrade): pygments in d:\python35\lib\site-packages (from restview)
   Requirement already satisfied (use --upgrade to upgrade): docutils in d:\python35\lib\site-packages (from restview)
   Collecting readme (from restview)
     Downloading readme-0.6.0-py2.py3-none-any.whl
   Requirement already satisfied (use --upgrade to upgrade): six in d:\python35\lib\site-packages (from readme->restview)
   Collecting bleach (from readme->restview)
     Downloading bleach-1.4.2-py2.py3-none-any.whl
   Collecting html5lib>=0.999 (from bleach->readme->restview)
     Downloading html5lib-0.9999999.tar.gz (889kB)

   Installing collected packages: html5lib, bleach, readme, restview
     Running setup.py install for html5lib
   Successfully installed bleach-1.4.2 html5lib-0.9999999 readme-0.6.0 restview-2.5.0

演習
======================================================================

README.rst を確認する
----------------------------------------------------------------------
オプションなしで ``restview`` を実行すると、HTTP サーバーが ``localhost:xxxx`` で起動する。
直ちにウェブブラウザーが自動的に開いて README の HTML 版を表示する。
その後、下に示すように HTTP ログを表示し続ける。

.. code-block:: console

   $ restview README.rst
   Listening on http://localhost:64492/
   127.0.0.1 - - [29/Oct/2015 22:32:18] "GET / HTTP/1.1" 200 -
   127.0.0.1 - - [29/Oct/2015 22:32:20] "GET /favicon.ico HTTP/1.1" 200 -
   127.0.0.1 - - [29/Oct/2015 22:32:26] "GET /favicon.ico HTTP/1.1" 200 -

* ポートはランダムに決定してくれる。明示的にポートを指定するオプションもある。

この状態でテキストエディター等で ``README.rst`` をデタラメに編集して保存すると、

#. ブラウザーで開いている README のビューが更新されている。
#. コンソールのログが増えていく。

次のログは rst ファイルの 99 行目辺りにテキトーにテキストを挿入して保存した例である。

.. code-block:: console

   127.0.0.1 - - [29/Oct/2015 22:41:55] "HEAD /polling?pathname=/&mtime=1446040040.280132 HTTP/1.1" 200 -
   README.rst:99: (ERROR/3) Unexpected indentation.
   127.0.0.1 - - [29/Oct/2015 22:41:56] "GET / HTTP/1.1" 200 -

Restview を停止する
----------------------------------------------------------------------
普通にコンソールで Ctrl+C を押す。

スタイルシートの設定
----------------------------------------------------------------------
オプション ``--css=URL|FILENAME`` を指定する。
複数のスタイルシートをカンマ区切りで指定することができる。

ただし、この機能は使いどころが難しい。
README を見せるのは主に GitHub のページであり、
自作のスタイルシートの出番がないから厳密な見栄えには興味がないのだ。

感想
======================================================================
ここまで書いておいてなんだが、色々と代替手段があることを最後に書き添えておきたい。

* `Online reStructuredText editor`_ のようなオンラインサービスが既にあるので、
  そちらで間に合うのであればこれをインストールする必要性はない。

* Docutils があるのだから、自力で HTML に変換してブラウザーで開いても手間はあまり変わらない。
  ただ Cygwin 環境だと Python のスクリプト呼び出しが若干面倒なので確かに有用かもしれない。

  .. code-block:: console

     $ python "$PYTHON_SCRIPTS_DIR/rst2html.py" README.rst > /tmp/README.html
     $ cygstart /tmp/README.html

  工夫としては最初の長いコマンドラインの固定部分をシェルの設定ファイルに関数化しておくことが考えられる。
  次のブラウザー呼び出しもつなげてしまってよさそうだ。

関連リンクおよび参考サイト
======================================================================
Restview_
  当パッケージの公式サイト。

`Online reStructuredText editor`_
  ウェブブラウザー上で rst テキストを編集して、
  その HTML への変換結果を動的に表示できるサービス。

.. include:: /_include/python-refs-core.txt
.. _restview: http://mg.pov.lt/restview/
.. _Online reStructuredText editor: http://rst.ninjs.org/
