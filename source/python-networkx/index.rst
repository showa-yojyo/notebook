======================================================================
NetworkX 利用ノート
======================================================================

本稿では Python のグラフライブラリーである NetworkX_ のインストール方法、
動作確認、簡単なグラフアルゴリズムの利用例、グラフのイメージ化方法について記す。
余裕があれば、高級なグラフアルゴリズムの応用例をいくつか示したい。

本稿でのグラフとは、計算機科学の教科書に書いてあるような、
ノードとエッジの集合うんぬんのグラフである。
変数と関数のとる値を座標平面にプロットした曲線ではない。
そちらについては :doc:`../python-matplotlib` のほうが相応しい。

.. toctree::
   :maxdepth: 5

   setup
   practice
   glossary

.. note::

   * OS

     * Windows 7 Home Premium SP 1 64bit

   * 本稿において、利用した各パッケージのバージョンは次のとおり。

     * Python_: 3.4.1
     * NetworkX_: 1.9.1
     * Nose_: 1.3.4
     * Numpy_: 1.9.1
     * Matplotlib_: 1.4.2

関連リンク
======================================================================
NetworkX_
  公式サイト。インストール方法から基本的な利用方法、応用等が文書化されている。

関連ノート
======================================================================
* :doc:`../python-nose`
* :doc:`../python-matplotlib`

.. _Python: http://www.python.org/
.. _NetworkX: https://networkx.github.io/
.. _Numpy: http://scipy.org/NumPy/
.. _Nose: http://somethingaboutorange.com/mrl/projects/nose/
.. _Matplotlib: http://matplotlib.sourceforge.net/
