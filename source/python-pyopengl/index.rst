======================================================================
PyOpenGL 利用ノート
======================================================================
本稿は、筆者の個人的な PyOpenGL の環境構築方法および、コードの記述方法等の覚え書きである。

筆者が昔 OpenGL をやる必要に迫られたときに、当時所持していた PC のスペックでは C/C++ の環境をまともに構築できず、研究ができない状態になって一瞬困った。
そこで、困ったときの Python 頼みということで、パッケージを探したところ、簡単に PyOpenGL_ に突き当たった。
早速 PyOpenGL の環境を構築し、学習を始めた。
始めるとすぐに、これが他の NumPy_ や PIL_ 等の有力パッケージとの強力なコンビ技で、むしろ Python のほうが学習環境に向いていることに気付いた。
OpenGL の勉強には Python を使う。これはなかなかよいコツかもしれない。

.. toctree::
   :maxdepth: 5

   setup
   doc
   coding

.. note::

   * OS

     * Windows XP Home Edition SP 3
     * Windows 7 Home Premium SP 1

   * 本稿執筆にあたり利用した各パッケージのバージョンは次のとおり。

     * Python_: 2.6.6, 2.7.3, 3.4.1
     * PyOpenGL_: 3.0.2a5, 3.1.0
     * NumPy_: 1.6.1, 1.6.2, 1.8.2
     * PIL_: 1.1.7 (unofficial) 現在は Pillow に取って代わられた。
     * Pillow_: 2.5.1

関連リンク
======================================================================
PyOpenGL_ (The Python OpenGL Binding)
  本パッケージ総本山サイト。インストール方法やドキュメント等。

`Python Extension Packages for Windows - Christoph Gohlke`_
  非公式インストーラー配布元。

関連ノート
======================================================================
* :doc:`/python-numpy/index`
* :doc:`/python-pillow`

.. include:: /_include/pyopengl-refs.txt
