======================================================================
インストール
======================================================================
自分の Python_ 環境に NumPy_ をインストールする方法を記す。

また、NumPy に関する各種ドキュメント、リファレンスが
HTML と PDF ファイルの形で利用できるようになっている。
これらのドキュメントをローカルディスクに保存しておき、
オフラインでもすぐにアクセスできるようにする。

.. contents::

パッケージをインストールする
======================================================================
* Windows 環境ではインストーラーからインストールするのが吉。
  :file:`numpy-x.y.z-win32-superpack-python2.6.exe` みたいな名前のインストーラーを
  NumPy の `SourceForge <http://www.numpy.org/>`_ ページから検索して入手しておけばよい。
  最近は Python 3.x 系もサポートするようになった。

  64 ビット環境の場合は公式サイトではなく、
  `Python Extension Packages for Windows - Christoph Gohlke`_ を利用させてもらう。
  :file:`numpy-MKL-x.y.z.win-amd64-py3.4.exe` のような名前のインストーラーをダウンロードすることができる。

* インストールを終了したら、何はさておき :file:`README.txt` と :file:`INSTALL.txt` を一読すること。
  目をひくのは単体テストが実行できるということだが、
  これには別途 Nose_ というサードパーティー製のライブラリーを
  Python 環境にインストールしておく必要がある。

  実際にやってみるとこのような感じになる。
  なお、数値計算パッケージの単体テストゆえ、実行時間は短くはない。
  時間に余裕があるときに試すとよい。

  .. code-block:: pycon

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
     >>>

アップグレード
----------------------------------------------------------------------
最近では標準 pip_ で環境に最適なパッケージをダウンロード、
インストールするような仕組みが整備されているようだ。
そういうわけで、今回のアップグレードは pip を利用した。
手順は次のようなものだ。

#. まずは `Python Extension Packages for Windows - Christoph Gohlke`_ から
   :file:`numpy-x.y.z+mkl-cp34-none-win_amd64.whl` のような名前の whl アーカイブをダウンロードする。

#. そして適当なディレクトリーに移動し、コマンドラインから次のようにする。
   1.8.2 から 1.9.2 へのアップグレードの例である。

   .. code-block:: console

      $ pip install --upgrade numpy-1.9.2+mkl-cp34-none-win_amd64.whl
      Unpacking d:\tmp\numpy-1.9.2+mkl-cp34-none-win_amd64.whl
      Installing collected packages: numpy
      Successfully installed numpy
      Cleaning up...

#. 最後に前節の要領でインストールの成功を確認する。

ドキュメントをローカルディスクに保存する
======================================================================
オンラインであれば `Numpy and Scipy Documentation <http://docs.scipy.org/doc/>`_ のページから欲しい情報に辿り着けるだろう。
クラス名や関数名を調べるときは、キーワード検索よりもインデックスページでのサーチのほうが早い。

オフライン環境で作業せざるを得ないの場合が多いので、
上述のページからダウンロードできる次のファイルをローカルに保存しておくのが望ましい。
同じ内容ならば PDF 版よりも HTML-help (CHM) のほうを優先して入手すること。
そうすればブラウザーでも閲覧できる。

* NumPy Reference Guide (numpy.chm)

  全関数リファレンスが含まれている。

* Guide to NumPy

  こちらはどちらかと言えば読み物。読書家向けか。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
