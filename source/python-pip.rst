======================================================================
Python pip 利用ノート
======================================================================

PyPI_ のページを久しぶりに見たら、
<To use a package from this index either "``pip install package``"
(get pip) or download, unpack and "``python setup.py install``" it>
と書いてあった。

だから本ノートを記す。ごく初歩的な内容のノートに留めておく。

.. note::

   * OS: Windows XP Home Edition SP 3
   * 本稿において、利用した各パッケージのバージョンは次のとおり。

     * Python_: 2.6.6
     * pip_: 1.1
     * setuptools_: 0.6c11
     * distribute_: 未使用
     * virtualenv: 未使用

.. contents:: ノート目次

入手からインストールまで
======================================================================
公式文書の説明に不明な点はなかった。

* 事実関係

  * PyPI_ のトップページには ``easy_install`` の文字列は見当たらない。

  * 公式には、virtualenv 内部での ``pip`` の利用を推奨している。
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

ファイルからパッケージリストを読み込んで各種操作する
----------------------------------------------------------------------
``pip freeze`` の出力をテキストファイルに出力しておき、次のようにすることができる。
今の環境の ``site-packages`` を別の環境で再現するとき等に利用できるというわけだ。

.. code-block:: console

   $ pip install --requirements=FILE

パッケージの検索
----------------------------------------------------------------------
例えば Amazon 関係のパッケージがあるのか知りたいとする。
しかも PyPI_ で検索するよりも、コンソールで見たいような状況であれば、
``pip search`` の出番だ。

.. code-block:: console

   $ pip search amazon
   AWSpider                  - Amazon Web Services web crawler
   bellatrix                 - Bellatrix is a comprehensive set of tools to
                               automate the management of Amazon EC2 services.
   boto                      - Amazon Web Services Library
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

関連リンク
======================================================================

* pip_:
  公式サイト。インストール方法から基本的な利用方法、応用等が文書化されている。


.. _Python: http://www.python.org/
.. _PyPI: http://pypi.python.org/pypi
.. _pip: http://www.pip-installer.org/en/latest/index.html
.. _easy_install: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _setuptools: http://peak.telecommunity.com/DevCenter/setuptools
.. _distribute: http://pypi.python.org/pypi/distribute
