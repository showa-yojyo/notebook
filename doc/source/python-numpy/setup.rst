======================================================================
インストール
======================================================================

自分の Python_ 環境に NumPy_ をインストールする方法を記す。

また、NumPy に関する各種ドキュメント、リファレンスが HTML と PDF ファイルの形で
利用できるようになっている。これらのドキュメントをローカルディスクに保存してお
き、オフラインでもすぐにアクセスできるようにする。

.. contents::

パッケージをインストールする
======================================================================

基本的には :ref:`miniconda-anchor-pip` の方針に従え。

インストールを終了したら、何はさておき :file:`README.txt` と:file:`INSTALL.txt`
を一読すること。目をひくのは単体テストが実行できるということだが、これには別途
Nose_ というサードパーティー製のライブラリーを Python 環境にインストールしておく
必要がある。

実際にやってみるとこのような感じになる。なお、数値計算パッケージの単体テストゆ
え、実行時間は短くはない。時間に余裕があるときに試すとよい。

>>> import numpy
>>> numpy.test()
Running unit tests for numpy
NumPy version 1.8.2
NumPy is installed in D:\Python34\lib\site-packages\numpy
Python version 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:45:13) [MSC v.1600 64 bit (AMD64)]
nose version 1.3.3
... more dots ...
----------------------------------------------------------------------
Ran 4762 tests in 207.414s
OK (KNOWNFAIL=10, SKIP=8)
<nose.result.TextTestResult run=4762 errors=0 failures=0>

アップグレード
----------------------------------------------------------------------

Anaconda_ または Miniconda_ で Python 環境を管理しているのであれば、コンソールか
ら ``conda update numpy`` で問題ないはずだ。

最近では標準 pip_ で環境に最適なパッケージをダウンロード、インストールするような
仕組みが整備されているようだ。そういうわけで、今回のアップグレードは
:program:`pip` を利用した。手順は次のようなものだ。

#. まずは `Python Extension Packages for Windows - Christoph Gohlke`_ から
   :file:`numpy-x.y.z+mkl-cp34-none-win_amd64.whl` のような名前の whl アーカイブをダウンロードする。
#. そして適当なディレクトリーに移動し、コマンドラインから次のようにする。1.8.2
   から 1.9.2 へのアップグレードの例である。

   .. code:: console

      bash$ pip install --upgrade numpy-1.9.2+mkl-cp34-none-win_amd64.whl
      Unpacking d:\tmp\numpy-1.9.2+mkl-cp34-none-win_amd64.whl
      Installing collected packages: numpy
      Successfully installed numpy
      Cleaning up...

#. 最後に前節の要領でインストールの成功を確認する。

ドキュメントをローカルディスクに保存する
======================================================================

オンラインであれば `Numpy and Scipy Documentation <http://docs.scipy.org/doc/>`_
のページから欲しい情報に辿り着けるだろう。クラス名や関数名を調べるときは、キー
ワード検索よりもインデックスページでのサーチのほうが早い。

オフライン環境で作業せざるを得ないの場合が多いので、上述のページからダウンロード
できる次のファイルをローカルに保存しておくのが望ましい。同じ内容ならば PDF 版よ
りも HTML-help (CHM) のほうを優先して入手すること。そうすればブラウザーでも閲覧
できる。

NumPy Reference Guide (:file:`numpy.chm`)
  全関数リファレンスが含まれている。
Guide to NumPy
  こちらはどちらかと言えば読み物。読書家向けか。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
