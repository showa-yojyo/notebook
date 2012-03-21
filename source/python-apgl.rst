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
<The automatic testing routine requires Python 2.7 or later,
or the unittest2 testing framework for Python 2.3-2.6> (p. 2)

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

* <adjacency matrices> (p. 1)
* <The current graph types in APGL are ``SparseGraph``, ``DenseGraph``
  and ``PySparseGraph`` which use *adjacency* or *weight matrices* as
  the underlying data structure> (p. 2)
* ``DictGraph`` は weight matrices を用いない。
* 行列の ij 成分が 1 ならば、グラフの頂点 i-j 間にエッジがあることを表現する。
* weight matrix は一般に実数を成分に取る。
* undirect graph と direct graph の違いは ij と ji の違い。

* グラフ

  .. csv-table::
     :header: "グラフクラス","格納","コメント"

     ``DenseGraph``,``numpy.ndarray``,
     ``SparseGraph``,``scipy.sparse``,efficient for the storage of large graphs without many edges
     ``PySparseGraph``,``Pysparse``,written in C and hence may be faster

* グラフ頂点にはラベルが付けられる。

  * ``VertexList``: 各頂点に ``numpy.ndarray`` 型の値をラベルとして付ける。
  * ``GeneralVertexList``: 各頂点に任意のラベルを付けられる。

* ``SparseGraph`` はデフォルトで無向グラフとなる。
  有向グラフにしたい場合は、コンストラクターのキーワード引数
  ``undirected`` に ``False`` を指定する。

* ``SparseGraph`` はデフォルトで SciPy の ``csr_matrix`` で構築される。
  これは何かというと、rows に対するアクセスが速い行列だ。
  
  * デフォルトの行列型を使いたくない場合は、
    グラフコンストラクターのキーワード引数 ``W`` に
    呼び出し側が用意した別の行列インスタンスを渡すことになる。
    
    ``csr_matrix`` よりは ``lil_matrix`` がよいようだ？

* 隣接頂点列を得るには、グラフメソッド ``neighbours`` を呼ぶ。

* グラフの最短経路

  * Floyd-Warshall アルゴリズムは行列の最短経路 P を計算する方法だ。
    これは計算コストがグラフサイズ n について O(n**3) という、たいへん重いものだ。

  * Dijkstra のアルゴリズムに基づいたグラフメソッド ``findAllDistances`` も利用可。

  * 最短経路は一度計算しておけば、二度使える（つまり何度でも使える）。

* グラフに関する集合演算がサポートされている。
  メソッド名だけノートしておくと ``union``, ``intersect``, ``setDiff``,
  ``complement``, ``subgraph``

* グラフのファイル I/O は CSV ベースのショボイものがあるだけか？
* NetworkX, iGraph は知らないのでパス。
* ``DictGraph`` は ``addEdge("a", "b")`` のような操作ができる。
  一見便利だが、エッジに weight を指定することができないようだ。

* ランダムグラフ生成

  * ``BarabasiAlbertGenerator``
  * ``ConfigModelGenerator``
  * ``EdrosRenyiGenerator``: デモコードあり。
    ``numpy.random`` モジュールを利用している。
    従って、同じシード (``numpy.random.seed``) 値を使えば、
    いつでも同一のグラフを得ることになる。
  * ``KroneckerGenerator``
  * ``SmallWorldGenerator``

利用例
======================================================================

findAllDistances
----------------------------------------------------------------------

グラフのインスタンスメソッド ``findAllDistances`` を使ってみる。
前述のとおり、内部で Dijkstra アルゴリズムを適用している。

これは各エッジの重みを、そのエッジの長さとみなした
グラフを構成するすべての頂点ペア最短経路における総距離を一発で計算するものだ。

.. image:: /_static/apgl-findall.png
   :scale: 100%

イラストのグラフの最短経路を計算するコードは次のとおり。

.. code-block:: python

   from apgl.graph.SparseGraph import SparseGraph
   from apgl.graph.GeneralVertexList import GeneralVertexList
   
   # Make a graph.
   numVertices = 6
   vlist = GeneralVertexList(numVertices)
   graph = SparseGraph(vlist, undirected=True)

   graph[0, 1] = 10.0
   graph[0, 2] = 14.0
   graph[0, 3] = 12.0
   graph[1, 2] = 8.0
   graph[1, 4] = 19.0
   graph[2, 3] = 7.0
   graph[2, 5] = 22.0
   graph[3, 5] = 21.0
   graph[4, 5] = 11.0
   
   # Compute the shortest paths with Dijkstra's algorithm.
   dists = graph.findAllDistances(True)
   print(dists)

実行結果はこういう感じになる。
行列 ``dists`` の ij 成分が、頂点 i と頂点 j を結ぶ最短経路のエッジウェイトの総和になっている。
無向グラフの経路は ``dists[i, j] == dists[j, i]`` となる。

.. code-block:: text

   [[  0.  10.  14.  12.  29.  33.]
    [ 10.   0.   8.  15.  19.  30.]
    [ 14.   8.   0.   7.  27.  22.]
    [ 12.  15.   7.   0.  32.  21.]
    [ 29.  19.  27.  32.   0.  11.]
    [ 33.  30.  22.  21.  11.   0.]]

また、この例でのグラフは孤立した頂点はないが、
一般的には接続の切れているような頂点ペアに関しては、
計算不能を示す値が来るということを記しておく。

不明点
======================================================================
* Graph Properties は勉強しないとわからない。
* エッジに weight 以外のラベルを付けることができるか？
* 最短経路の総距離は求められるのに、頂点順序は求められない？


.. _Python: http://www.python.org/
.. _Python Extension Packages for Windows - Christoph Gohlke: http://www.lfd.uci.edu/~gohlke/pythonlibs/
.. _easy_install: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _pip: http://pypi.python.org/pypi/pip
.. _`Another Python Graph Library`: http://packages.python.org/apgl/
.. _APGL: http://packages.python.org/apgl/
.. _Numpy: http://scipy.org/NumPy/
.. _SciPy: http://www.scipy.org/

