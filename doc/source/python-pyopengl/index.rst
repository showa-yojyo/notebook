======================================================================
PyOpenGL 利用ノート
======================================================================

.. important::

   動作環境の OS をアップグレードして Windows 10 環境にした途端、グラフィックド
   ライバーがデグレードしてしまった。その結果、サポートする OpenGL のバージョン
   (``GL_VERSION``) が 1.1 に落ちぶれてしまった。現在当ノートの改訂作業ができな
   い状態だ。

   現在の ``glGetString`` による情報を示す。稼動時の情報については後述する。

   .. csv-table::
      :delim: :
      :header-rows: 1
      :widths: auto

      名前 : 値
      ``GL_VENDER``: Microsoft Corporation
      ``GL_RENDERER``: GDI Generic
      ``GL_VERSION``: 1.1.0
      ``GL_SHADING_LANGUAGE_VERSION``: 表示できない
      ``GL_EXTENSIONS``: ``GL_WIN_swap_hint GL_EXT_bgra GL_EXT_paletted_texture``

   デグレードと記したものの、Windows のデバイスマネージャーで確認したところ、グ
   ラフィックドライバーは別段古いものではなかった。

   OpenGL Extensions Viewer を導入して、稼働中のグラフィックドライバーが OpenGL
   の GLSL をサポートしていることを（ついでに関数 ``wglCreateContextAttribsARB``
   が利用可能であることも）確認したり、ベンダーのツールでドライバーを最新に更新
   できないか試したりと努力はしたが、本文で述べる PyOpenGL で書いたコードがどう
   しても正しいグラフィックドライバーを認識せず、 Microsoft の GDI Generic だと
   断言するのを改めようとしない。

   そうこうしていると Windows のブルースクリーンが出てしまった。再起動したら画面
   がバグってしまって何も操作できないという、たいへんな危機的状況になってしまっ
   た。もう一度再起動しても画面がカーソルの残像で埋め尽くされて何も見えないとい
   う始末。なんとか Windows の自動修復機能を強引に発動させて原状回復を果たした
   が、もう懲りた。無念だが本稿用の研究を全て打ち切る。

本稿は、筆者の個人的な PyOpenGL の環境構築方法および、コードの記述方法等の覚え書
きである。

筆者が昔 OpenGL をやる必要に迫られたときに、当時所持していた PC のスペックでは
C/C++ の環境をまともに構築できず、研究ができない状態になって一瞬困った。そこで、
困ったときの Python 頼みということで、パッケージを探したところ、簡単に PyOpenGL_
に突き当たった。早速 PyOpenGL の環境を構築し、学習を始めた。始めるとすぐに、これ
が他の NumPy_ や PIL_ 等の有力パッケージとの強力なコンビ技で、むしろ Python のほ
うが学習環境に向いていることに気付いた。 OpenGL の勉強には Python を使う。これは
なかなかよいコツかもしれない。

.. toctree::
   :maxdepth: 3

   setup
   doc
   coding

.. note::

   * OS

     * Windows XP Home Edition SP3
     * Windows 7 Home Premium x64 SP1
     * Windows 10 Home x64

   * 本稿執筆にあたり利用した各パッケージのバージョンは次のとおり。

     * Python_: 2.6.6, 2.7.3, 3.4.1, 3.5.0 (?), 3.5.2
     * PyOpenGL_: 3.0.2a5, 3.1.0, 3.1.1a1 (?)
     * NumPy_: 1.6.1, 1.6.2, 1.8.2, 1.10.0, 1.11.1
     * Quaternion_: 0.3.1
     * PIL_: 1.1.7 (unofficial) 現在は Pillow に取って代わられた。
     * Pillow_: 2.5.1, 3.0.0, 3.2.0

関連リンク
======================================================================

PyOpenGL_ (The Python OpenGL Binding)
  本パッケージ総本山サイト。インストール方法やドキュメント等。
`Python Extension Packages for Windows - Christoph Gohlke`_
  非公式インストーラー配布元。

関連ノート
======================================================================

* :doc:`/python-numpy/index`
* :doc:`/python-quaternion`
* :doc:`/python-pillow`

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
.. include:: /_include/python-refs-vision.txt
