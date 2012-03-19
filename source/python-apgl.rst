======================================================================
Another Python Graph Library (APGL) 利用ノート
======================================================================

.. contents:: ノート目次

.. note::

   * OS: Windows XP Home Edition SP 3
   * 本稿において、利用した各パッケージのバージョンは次のとおり。

     * Python_: 2.6.6
     * APGL_: 0.6.10
     * NumPy_: 1.6.1
     * SciPy_: 0.10.1

関連リンク
======================================================================
`Another Python Graph Library`_ (APGL)
  パッケージ配布元。

関連ノート
======================================================================
* :doc:`python-numpy`
* :doc:`python-scipy`

インストール
======================================================================
自分の Python_ 環境 (Windows XP) に APGL_ をインストールする方法を記す。
単体テストが走るところまで確認できたら、インストール成功とみなす。

* NumPy_ と SciPy_ で実装されているパッケージなので、これらを先にインストールしてあることを前提とする。
  関連ノート参照。

* APGL はその他に pysparse_ というパッケージを利用する。
  ほとんどのグラフを表現するためには疎行列が欠かせないのだが、
  SciPy_ が提供する疎行列の他に、pysparse のそれを利用するようだ。
  必須ではないらしいが、あっても困らないので併せてインストールする。

pysparse
----------------------------------------------------------------------
Windows 版のビルドを利用するのが手っ取り早い。いつもお世話になっている
`Python Extension Packages for Windows - Christoph Gohlke`_
からインストーラーをダウンロードし、実行すればよい。

apgl
----------------------------------------------------------------------
`easy_install`_ または、可能ならば pip_ を利用してインストールする。
当ノートでは後者を推奨する。

.. code-block:: console

   $ pip install apgl

インストール処理終了後、Python で公式ドキュメントにあるように
apgl のテストを起動する。

.. code-block:: pycon

   >> import apgl
   >> apgl.test()

.. warning::

   私の環境では ``E`` が大量に出るばかりでなく、テストランナーが途中で中断終了した。
   次のタイプのエラーが二度と、

   .. code-block:: text

      Traceback (most recent call last):
        File "<string>", line 1, in <module>
        File "D:\Python26\lib\multiprocessing\forking.py", line 342, in main
          self = load(from_parent)
        File "D:\Python26\lib\pickle.py", line 1370, in load
          return Unpickler(file).load()
        File "D:\Python26\lib\pickle.py", line 858, in load
          dispatch[key](self)
        File "D:\Python26\lib\pickle.py", line 880, in load_eof
          raise EOFError

   最後に下のエラーが出て強制終了。

   .. code-block:: text

      Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "D:\Python26\lib\site-packages\apgl\__init__.py", line 66, in test
          unittest.TextTestRunner(verbosity=1).run(overallTestSuite)
        File "D:\Python26\lib\unittest.py", line 756, in run
          result.printErrors()
        File "D:\Python26\lib\unittest.py", line 724, in printErrors
          self.printErrorList('ERROR', self.errors)
        File "D:\Python26\lib\unittest.py", line 730, in printErrorList
          self.stream.writeln("%s: %s" % (flavour,self.getDescription(test)))
        File "D:\Python26\lib\unittest.py", line 686, in getDescription
          return test.shortDescription() or str(test)
        File "D:\Python26\lib\site-packages\setuptools\tests\doctest.py", line 2261, in shortDescription
          return "Doctest: " + self._dt_test.name
      AttributeError: 'str' object has no attribute 'name'

   原因は不明だが、Python 2.7 ではまともに動作するのではないかと予想する。
   新 PC を調達するまでは Python 本体をアップグレードする気はないので、
   2.6 のまま様子を見たい。

ドキュメント
======================================================================
APGL_ のウェブページに "An Introduction to APGL" という PDF ファイルへのリンクがある。
これを読むことで、グラフのごく基礎的な利用法を習得できる。

TBW

利用例
======================================================================
TBW

不明点
======================================================================
TBW

.. _Python: http://www.python.org/
.. _Python Extension Packages for Windows - Christoph Gohlke: http://www.lfd.uci.edu/~gohlke/pythonlibs/
.. _easy_install: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _pip: http://pypi.python.org/pypi/pip
.. _`Another Python Graph Library`: http://packages.python.org/apgl/
.. _APGL: http://packages.python.org/apgl/
.. _Numpy: http://scipy.org/NumPy/
.. _SciPy: http://www.scipy.org/

