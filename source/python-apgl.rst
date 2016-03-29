======================================================================
Another Python Graph Library (APGL) 利用ノート
======================================================================
本稿は :doc:`python-networkx/index` を書くよりも昔に書いたものだ。

.. contents:: ノート目次

.. note::

   * OS

     * Windows XP Home Edition SP3
     * Windows 7 Home Premium x64 SP1
     * Windows 10 Home x64

   * 本稿において、利用した各パッケージのバージョンは次のとおり。

     * Python_: 2.6.6, 2.7.3, 3.4.1, 3.5.0
     * APGL_: 0.6.10, 0.7.1, 0.8.1
     * NumPy_: 1.6.1, 1.6.2, 1.8.2, 1.10.0
     * SciPy_: 0.10.1, 1.3.1, 0.16.0

関連リンク
======================================================================
`Another Python Graph Library`_ (APGL)
  パッケージ配布元。

関連ノート
======================================================================
* :doc:`python-networkx/index`
* :doc:`python-numpy/index`
* :doc:`python-scipy/index`

インストール
======================================================================
自分の Python_ 環境 (Windows XP) に APGL_ をインストールする方法を記す。
単体テストが走るところまで確認できたら、インストール成功とみなす。

* NumPy_ と SciPy_ で実装されているパッケージなので、
  これらを先にインストールしてあることを前提とする。関連ノート参照。

* APGL はその他に pysparse_ というパッケージを利用する。
  ほとんどのグラフを表現するためには疎行列が欠かせないのだが、
  SciPy_ が提供する疎行列の他に、pysparse のそれを利用するようだ。
  必須ではないらしいが、あっても困らないので併せてインストールする。

pysparse
----------------------------------------------------------------------
Windows 版のビルドを利用するのが手っ取り早い。いつもお世話になっている
`Python Extension Packages for Windows - Christoph Gohlke`_
からインストーラーをダウンロードし、実行すればよい。

残念ながら、本稿執筆時点では上記サイトに Python 3.x 用および 64 ビット用のビルドは存在しない。

apgl
----------------------------------------------------------------------
pip_ を利用してインストールする。

.. code-block:: console

   $ pip install apgl

インストール処理終了後、Python で公式ドキュメントにあるように
apgl のテストを起動するのがよいだろう。
<The automatic testing routine requires Python 2.7 or later,
or the unittest2 testing framework for Python 2.3-2.6> (p. 2)

.. code-block:: pycon

   >> import apgl
   >> apgl.test()
   Running tests from D:\Python35\lib\site-packages\apgl
   ... more dots ...
   ----------------------------------------------------------------------
   Ran 438 tests in 40.034s

   FAILED (failures=14, errors=29, skipped=148)
   >>>

どのバージョンもスキップが多すぎて不安になる事態が改善されていない。

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
     :delim: :
     :header: クラス, データ, コメント
     :widths: 8, 8, 82

     ``DenseGraph``:``numpy.ndarray``:
     ``SparseGraph``:``scipy.sparse``:efficient for the storage of large graphs without many edges
     ``PySparseGraph``:``Pysparse``:written in C and hence may be faster

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

  * Floyd-Warshall アルゴリズムは行列の最短経路 `P` を計算する方法だ。
    これは計算コストがグラフ頂点数 `n` について :math:`O(n^3)` という、たいへん重いものだ。

  * Dijkstra のアルゴリズムに基づいたグラフメソッド ``findAllDistances`` も利用可。
    グラフの最短経路と言われれば、まずこの手法の適用可能性を検討するのが自然だろう。

  * 最短経路は一度計算しておけば、二度使える（つまり何度でも使える）。

* グラフの部分もまたグラフである。
  そこで、グラフに関する集合演算がサポートされている。
  メソッド名だけノートしておくと ``union``, ``intersect``, ``setDiff``,
  ``complement``, ``subgraph``

* グラフのファイル I/O は CSV ベースのショボイものがあるだけか？
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

メソッド ``findAllDistances``
----------------------------------------------------------------------
グラフのインスタンスメソッド ``findAllDistances`` を使ってみる。
前述のとおり、内部で Dijkstra アルゴリズムを適用している。

これは各エッジの重みを、そのエッジの長さとみなした
グラフを構成するすべての頂点ペア最短経路における総距離を一発で計算するものだ。

.. figure:: /_static/apgl-findall.png
   :align: center
   :alt: 最短経路計算対象グラフ
   :width: 387px
   :height: 251px
   :scale: 100%

イラストのグラフの最短経路を計算するコードは次のとおり。

.. literalinclude:: /_sample/apgl/dijkstra.py
   :language: python3

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

``PySparseGraph``
----------------------------------------------------------------------

:file:`PySparseGraph` の冒頭のインポートがおかしいので、自分で修正する。

.. code-block:: python3

   #from pysparse.sparse.pysparseMatrix import PysparseMatrix
   from pysparse.pysparseMatrix import PysparseMatrix

不明点
======================================================================
* Graph Properties は勉強しないとわからない。
* エッジに weight 以外のラベルを付けることができるか？
* 最短経路の総距離は求められるのに、頂点順序は求められない？

NetworkX_ ではこれらは明らか。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
.. _`Another Python Graph Library`: http://packages.python.org/apgl/
.. _APGL: http://packages.python.org/apgl/
.. _NetworkX: https://networkx.github.io/
