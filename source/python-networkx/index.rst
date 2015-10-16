======================================================================
NetworkX 利用ノート
======================================================================
本稿では Python のグラフライブラリーである NetworkX_ のインストール方法、
動作確認、簡単なグラフアルゴリズムの利用例、グラフのイメージ化方法について記す。
余裕があれば、高級なグラフアルゴリズムの応用例をいくつか示したい。

本稿でのグラフとは、計算機科学の教科書に書いてあるような、
ノードとエッジの集合うんぬんのグラフである。
変数と関数のとる値を座標平面にプロットした曲線ではない。
そちらについては :doc:`/python-matplotlib/index` のほうが相応しい。

.. toctree::
   :maxdepth: 5

   setup
   practice
   connected-components
   topological-sorting
   minimum-spanning-tree
   shortest-path
   matching
   eulerian-cycle
   connectivity
   network-flow
   drawing
   glossary

.. note::

   * OS

     * Windows 7 Home Premium x64 SP1
     * Windows 10 Home x64

   * 本稿において、利用した各パッケージのバージョンは次のとおり。

     * Python_: 3.4.1, 3.5.0
     * NetworkX_: 1.9.1, 2.0.dev20151014034116
     * Nose_: 1.3.4, 1.3.7
     * Numpy_: 1.9.1, 1.10.0
     * Matplotlib_: 1.4.2, 1.4.3

関連リンク
======================================================================
NetworkX_
  公式サイト。インストール方法から基本的な利用方法、応用等が文書化されている。

関連ノート
======================================================================
* :doc:`/python-nose`
* :doc:`/python-matplotlib/index`

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
.. _NetworkX: https://networkx.github.io/
