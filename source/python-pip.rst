======================================================================
pip 利用ノート
======================================================================

本稿は <A tool for installing and managing Python packages>(pip_) である pip に関する覚え書きである。
すべての Python ユーザーはそうなのではないかと思うのだが、
Python のバージョンアップのたびに、サードパーティー製のパッケージもインストールし直すという、
かなり面倒な作業が発生してしまう。
インストーラー実行で即セットアップ終了となるなのは、あくまでも Python 本体でしかない。
NumPy や Sphinx 等は別途明示的なインストール作業が利用するパッケージの個数回必要となる。
ハードコアな Python ユーザーはサードパーティー製パッケージを大量に持っているため、
この作業の手間を軽減するのが重要になるのだ。
それには pip というパッケージを利用するのがたいへん具合がよい。
そこで、この覚え書きを残して、Python のアップグレードのときに見返そうというわけだ。

この pip 自体の入手方法について、少々動きがあったので付記しておく。
Python 3.4 以前は pip もまたサードパーティー製パッケージの一つであったのだが、
うれしいことに 3.4 では Python 本体に同パッケージが同梱されている。
``Scripts`` フォルダー内に ``easy_install`` と ``pip`` があるので、
後述するインストールの手順を飛ばして、
いきなりその他のサードパーティー製パッケージのインストール作業に取り掛かることができる。

.. contents:: ノート目次

.. note::

   * OS

     * Windows XP Home Edition SP 3
     * Windows 7 Home Premium SP 1
     * Windows 10 Home Edition

   * 本稿において、利用した各パッケージのバージョンは次のとおり。

     * Python_: 2.6.6, 2.7.3, 3.4.1, 3.5.0
     * pip_: 1.1, 1.5.6, 7.1.2
     * setuptools_: 0.6c11
     * distribute_: 未使用
     * virtualenv: 未使用

関連リンク
======================================================================
pip_
  公式サイト。インストール方法から基本的な利用方法、応用等が文書化されている。

`easy_install`_
  easy_install の公式サイト。

入手からインストールまで
======================================================================
Python 3.4 以前の環境では、手動でインストールする必要がある。
以下に記す手順でインストールする。

* 事実関係

  * PyPI_ のトップページには ``easy_install`` の文字列は見当たらない。

  * pip_ 公式には、virtualenv 内部での ``pip`` の利用を推奨している。
  * virtualenv 環境内は自動的に ``pip`` がインストール済み状態だ。
  * そうではなく、「グローバルに」インストールする状況も当然ある。

    * そのような場合での ``pip`` のインストールの事前条件は、
      setuptools_ または distribute_ のどちらかがインストールされていること。

    * ``easy_install`` が環境にあれば、
      下記コマンドプロンプト入力で ``pip`` のインストールは実現できる。

      .. code-block:: console

         $ easy_install pip

    * ソースコードを入手、解凍してコマンドプロンプトから
      ``setup.py install`` でインストールするやり方もある。

* コメント

  * ``easy_install`` でインストールした。まったく問題はなかった。

初歩的な利用例
======================================================================
``easy_install`` から乗り換えたばかりなので、当面それほど凝った操作を必要とはしていない。
次に挙げる操作だけ覚えておく。

``pip`` は実行ファイル形式で ``$PYTHONHOME/Scripts`` フォルダーに格納されている。

ヘルプ・バージョン表示
----------------------------------------------------------------------
言うまでもないが help は目を通したほうがよい。
コマンドラインオプションはそれほど多くはない。

.. code-block:: console

   $ pip help # ヘルプ表示
   $ pip --version # バージョン表示

アンインストール
----------------------------------------------------------------------
以前に ``easy_install`` でインストールしてしまったパッケージも
``pip`` でアンインストールできる。

.. code-block:: console

   $ pip uninstall simplejson
   Uninstalling simplejson:
     d:\python26\lib\site-packages\simplejson
     d:\python26\lib\site-packages\simplejson-2.4.0-py2.6.egg-info
   Proceed (y/n)?

インストール・アップグレード
----------------------------------------------------------------------
パッケージ名を指定して ``pip install`` または ``pip install --upgrade`` を実行する。

.. code-block:: console

   $ pip install --upgrade httplib2
   Downloading/unpacking httplib2 from http://pypi.python.org/packages/source/h/httplib2/httplib2-0.7.4.tar.gz#md5=略
     Downloading httplib2-0.7.4.tar.gz (106Kb): 106Kb downloaded
     Running setup.py egg_info for package httplib2
   Installing collected packages: httplib2
     Found existing installation: httplib2 0.7.2
       Uninstalling httplib2:
         Successfully uninstalled httplib2
     Running setup.py install for httplib2
   Successfully installed httplib2
   Cleaning up...

インストール済みパッケージをリスト
----------------------------------------------------------------------

.. code-block:: console

   $ pip freeze
   PIL==1.1.7
   babel==0.9.6
   coverage==3.5.1
   docutils==0.8.1
   以下略

余談だが、Google で ``pip freeze`` を検索すると、
他の Python プログラマーがどのようなパッケージを利用しているか垣間見える。

インストール済みパッケージの情報を表示する
----------------------------------------------------------------------
コマンド ``pip show`` を実行することで、インストール済みパッケージの情報を出力できる。
これは当ノートの更新作業のときにしばしば実行する。

.. code-block:: console

   $ pip show matplotlib
   ---
   Metadata-Version: 2.0
   Name: matplotlib
   Version: 1.4.3
   Summary: Python plotting package
   Home-page: http://matplotlib.org
   Author: John D. Hunter, Michael Droettboom
   Author-email: mdroe@stsci.edu
   License: BSD
   Location: d:\python35\lib\site-packages
   Requires: python-dateutil, pytz, numpy, six, pyparsing

コマンドライン引数にパッケージ名を複数指定すると、
情報を上記の書式で連続して出力する。

ファイルからパッケージリストを読み込んで各種操作する
----------------------------------------------------------------------
``pip freeze`` の出力をテキストファイルに出力しておき、次のようにすることができる。
今の環境の ``site-packages`` を別の環境で再現するとき等に利用できるというわけだ。

.. code-block:: console

   $ pip freeze > FILE
   ...
   $ pip install -r=FILE
   $ pip install --upgrade -r=FILE

パッケージの検索
----------------------------------------------------------------------
例えば Amazon 関係のパッケージがあるのか知りたいとする。
しかも PyPI_ で検索するよりも、コンソールで見たいような状況であれば、
``pip search`` の出番だ。

.. code-block:: console

   $ pip search amazon
   AWSpider                  - Amazon Web Services web crawler
   boto                      - Amazon Web Services Library
   bellatrix                 - Bellatrix is a comprehensive set of tools to
                               automate the management of Amazon EC2 services.
   以下略

まれに使うことになるかもしれない使用例
======================================================================

ミラーサイトを指定してインストール
----------------------------------------------------------------------
PyPI_ のウェブサイトがダウンしているときには ``pip install`` 系操作は失敗する。
サーバーが復旧するまで待てない場合、ミラーサイトを指定してインストールを試みることができる。

.. code-block:: console

   $ pip install --use-mirrors --mirrors=http://d.pypi.python.org/ sphinx

ミラーサイトのリストは次の通り。

* http://b.pypi.python.org/
* http://c.pypi.python.org/
* http://d.pypi.python.org/
* http://e.pypi.python.org/
* http://f.pypi.python.org/

Python_ のどこかのページに書いてあるが、
ご本尊ごとサーバーがダウンしていたら読めないので、ここに転載する。
本当はこれらを設定ファイルに書いておくのが作法。

.. include:: /_include/python-refs-core.txt
