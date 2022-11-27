======================================================================
pip 利用ノート
======================================================================

本稿は <A tool for installing and managing Python packages>(pip_) である
:program:`pip` に関する覚え書きである。すべての Python ユーザーはそうなのではな
いかと思うのだが、 Python のバージョンアップのたびに、サードパーティー製のパッ
ケージもインストールし直すという、かなり面倒な作業が発生してしまう。インストー
ラー実行で即セットアップ終了となるなのは、あくまでも Python 本体でしかない。
NumPy や Sphinx 等は別途明示的なインストール作業が利用するパッケージの個数回必要
となる。ハードコアな Python ユーザーはサードパーティー製パッケージを大量に持って
いるため、この作業の手間を軽減するのが重要になるのだ。それには :program:`pip` と
いうパッケージを利用するのがたいへん具合がよい。そこで、この覚え書きを残し
て、Python のアップグレードのときに見返そうというわけだ。

この :program:`pip` 自体の入手方法について、少々動きがあったので付記しておく。
Python 3.4 以前は :program:`pip` もまたサードパーティー製パッケージの一つであっ
たのだが、うれしいことに 3.4 では Python 本体に同パッケージが同梱されている。
:file:`Scripts` フォルダー内に :program:`easy_install` と :program:`pip` がある
ので、後述するインストールの手順を飛ばして、いきなりその他のサードパーティー製
パッケージのインストール作業に取り掛かることができる。

.. contents:: ノート目次

.. note::

   * OS

     * Windows XP Home Edition SP3
     * Windows 7 Home Premium x64 SP1
     * Windows 10 Home x64

   * 本稿において、利用した各パッケージのバージョンは次のとおり。

     * Python_: 2.6.6, 2.7.3, 3.4.1, 3.5.0
     * pip_: 1.1, 1.5.6, 7.1.2, 8.1.1
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

Python 3.4 以前の環境では、手動でインストールする必要がある。以下に記す手順でイ
ンストールする。

* 事実関係

  * PyPI_ のトップページには :program:`easy_install` の文字列は見当たらない。

  * pip_ 公式には、virtualenv 内部での :program:`pip` の利用を推奨している。
  * virtualenv 環境内は自動的に :program:`pip` がインストール済み状態だ。
  * そうではなく、「グローバルに」インストールする状況も当然ある。

    * そのような場合での :program:`pip` のインストールの事前条件は、setuptools_
      または distribute_ のどちらかがインストールされていること。

    * :program:`easy_install` が環境にあれば、下記コマンドプロンプト入力で
      :program:`pip` のインストールは実現できる。

      .. code:: console

         bash$ easy_install pip

    * ソースコードを入手、解凍してコマンドプロンプトから
      :command:`setup.py install` でインストールするやり方もある。

.. admonition:: 利用者ノート

   :program:`easy_install` でインストールした。まったく問題はなかった。

初歩的な利用例
======================================================================

:program:`easy_install` から乗り換えたばかりなので、当面それほど凝った操作を必要
とはしていない。次に挙げる操作だけ覚えておく。

:program:`pip` は実行ファイル形式で :file:`$PYTHONHOME/Scripts` フォルダーに格納
されている。

ヘルプ・バージョン表示
----------------------------------------------------------------------

言うまでもないが :command:`help` は目を通したほうがよい。コマンドラインオプショ
ンはそれほど多くはない。

.. code:: console

   bash$ pip help # ヘルプ表示
   bash$ pip --version # バージョン表示

アンインストール
----------------------------------------------------------------------

以前に :program:`easy_install` でインストールしてしまったパッケージも
:program:`pip` でアンインストールできる。

.. code:: console

   bash$ pip uninstall simplejson
   Uninstalling simplejson:
     d:\python26\lib\site-packages\simplejson
     d:\python26\lib\site-packages\simplejson-2.4.0-py2.6.egg-info
   Proceed (y/n)?

インストール・アップグレード
----------------------------------------------------------------------

一番重要なインストールのやり方について記す。

インストールしたいパッケージの形態によって、コマンドが異なる。いずれも重要な手順
なので、すべて説明する。

インターネットからパッケージをダウンロードする
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

パッケージ名を指定して :command:`pip install` または
:command:`pip install --upgrade` を実行する。この方法でインストールやアップグ
レードができれば、手間が最小で済む。

.. code:: console

   bash$ pip install --upgrade httplib2
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

ダウンロード済みパッケージをインストールする
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

一部の手の込んだパッケージは、Visual C++ によるコンパイル処理などが含まれていた
り、最新の Python のビルドに対応したバイナリーが公式に存在しなかったりする。この
ため、一般的な環境ではビルドできないことが考えられる。

そういう場合は親切な人がビルドした whl 形式のパッケージを別途ダウンロードして、
:command:`pip` の引数にそのファイル名を指定することでインストールやアップグレー
ドが実現できる。

以下、手順のイメージを擬似コードで表現する。

.. code:: console

   bash$ (download) PyXYZ-x.y.z-cp35-none-win_amd64.whl
   bash$ pip install PyXYZ-x.y.z-cp35-none-win_amd64.whl

編集可能パッケージをインストールする
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

オープンソースなプロジェクトによるパッケージについては、公開レポジトリーから作業
コピーをローカルに作成し、そこをインストールする方法がある。

以下、手順のイメージを擬似コードで表現する。どのディレクトリーで作業をするかは
:file:`setup.py` が存在する階層でよいことが多い。

.. code:: console

   bash$ git clone https://github.com/XYZ/XYZ.git
   ...
   bash$ cd XYZ/src/
   bash$ pip install -e .

インストール済みパッケージをリスト
----------------------------------------------------------------------

.. code:: console

   bash$ pip freeze
   PIL==1.1.7
   babel==0.9.6
   coverage==3.5.1
   docutils==0.8.1
   以下略

余談だが、Google で ``pip freeze`` を検索すると、他の Python プログラマーがどの
ようなパッケージを利用しているか垣間見える。

更新対象パッケージを調べる
----------------------------------------------------------------------

最新のバージョンにアップグレードできるパッケージが何かあるか調べたい。こういう場
合は :command:`list` コマンドにオプション ``--outdated`` を指定する。

次に示すように現在 Python 環境にある各パッケージのバージョン、最新バージョンの情
報、および ``[wheel]`` や ``[sdist]`` などのインストール形態がリストされる。例え
ばパッケージ ``alabaster`` は現在はバージョン 0.7.6 が .whl によりインストールさ
れていて、更新すると 0.7.7 にアップグレードできることを示している。

.. code:: console

   bash$ pip list --outdated
   alabaster (0.7.6) - Latest: 0.7.7 [wheel]
   astroid (1.3.8) - Latest: 1.4.5 [wheel]
   Babel (2.1.1) - Latest: 2.2.0 [wheel]
   ...
   virtualenv (13.1.2) - Latest: 15.0.1 [wheel]

この出力を適宜整形してテキストファイルを保存して、:command:`pip install -U -r`
に指定して実際に更新作業を開始することを勧める。出力リストからある種のパッケージ
を手動で取り除いておかねばならない。例えば手作業でダウンロードしたい .whl からイ
ンストールしたいパッケージ、ローカルリポジトリーからインストールしたいものは別途
アップグレードする必要がある。

インストール済みパッケージの情報を表示する
----------------------------------------------------------------------

コマンド :command:`pip show` を実行することで、インストール済みパッケージの情報
を出力できる。これは当ノートの更新作業のときにしばしば実行する。

.. code:: console

   bash$ pip show matplotlib
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

コマンドライン引数にパッケージ名を複数指定すると、情報を上記の書式で連続して出力
する。

ファイルからパッケージリストを読み込んで各種操作する
----------------------------------------------------------------------

:command:`pip freeze` の出力をテキストファイルに出力しておき、次のようにすること
ができる。今の環境の :file:`site-packages` を別の環境で再現するとき等に利用でき
るというわけだ。

.. code:: console

   bash$ pip freeze > FILE
   ...
   bash$ pip install -r=FILE
   bash$ pip install --upgrade -r=FILE

パッケージの検索
----------------------------------------------------------------------

例えば Amazon 関係のパッケージがあるのか知りたいとする。しかも PyPI_ で検索する
よりも、コンソールで見たいような状況であれば :command:`pip search` の出番だ。

.. code:: console

   bash$ pip search amazon
   AWSpider                  - Amazon Web Services web crawler
   boto                      - Amazon Web Services Library
   bellatrix                 - Bellatrix is a comprehensive set of tools to
                               automate the management of Amazon EC2 services.
   以下略

まれに使うことになるかもしれない使用例
======================================================================

ミラーサイトを指定してインストール
----------------------------------------------------------------------

PyPI_ のウェブサイトがダウンしているときには :command:`pip install` 系操作は失敗
する。サーバーが復旧するまで待てない場合、ミラーサイトを指定してインストールを試
みることができる。

.. code:: console

   bash$ pip install --use-mirrors --mirrors=http://d.pypi.python.org/ sphinx

ミラーサイトのリストは次の通り。

* <http://b.pypi.python.org/>
* <http://c.pypi.python.org/>
* <http://d.pypi.python.org/>
* <http://e.pypi.python.org/>
* <http://f.pypi.python.org/>

Python_ のどこかのページに書いてあるが、ご本尊ごとサーバーがダウンしていたら読め
ないので、ここに転載する。本当はこれらを設定ファイルに書いておくのが作法。

.. include:: /_include/python-refs-core.txt
