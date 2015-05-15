======================================================================
Matplotlib 利用ノート
======================================================================
本稿では Python ユーザー御用達のプロットパッケージである Matplotlib_ について記す。

Matplotlib_ パッケージはとても奥が深い。
手足のように使いこなせるようになるには、相当時間を要すると見た。
Python_ では遊びたいことが他にもたくさんあるので
Matplotlib で目的を拡大し過ぎないように、ここまでできれば十分だという目的を決めておく。
個人的には次の 3 点で十分だ。

* 数学の教科書にありがちな曲線グラフを描画する。
  特に xy 平面上に n 次多項式やスプライン曲線が描画できればいい。

* 数学の教科書にありがちな数式を描画する。
  つまり TeX 環境の簡易版として利用したい。

* それらを PNG 画像または PDF ファイルとして出力したい。
  できれば SVG ファイルをも得たい。

.. toctree::
   :maxdepth: 5

   setup
   basic
   advanced
   config

.. note::

   * OS

     * Windows XP Home Edition SP 3
     * Windows 7 Home Premium SP 1

   * 本稿において、利用した各パッケージのバージョンは次のとおり。

     * Python_ 2.6.6, 2.7.3, 3.4.1
     * Setuptools_ 0.6c11
     * Matplotlib_ 1.1.0, 1.1.1, 1.3.1, 1.4.3
     * NumPy_ 1.6.0, 1.6.2, 1.8.2, 1.9.2
     * PyParsing_ 2.0.2
     * PyQt_ 4.8.4, 5.3.1

関連リンク
======================================================================
Matplotlib_
  パッケージ配布元。

関連ノート
======================================================================
:doc:`/python-numpy/index` および :doc:`/python-scipy/index`
  プロットしたいデータを表現するには、これらのパッケージの機能が活躍するはずだ。

:doc:`/python-ipython`
  IPython_ を Python シェルとして利用すると、入力周りが快適かつ便利だ。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
.. _PyQt: http://www.riverbankcomputing.com/software/pyqt/intro
.. _PyParsing: https://pypi.python.org/pypi/pyparsing
