======================================================================
コードを書く
======================================================================

.. todo::

   :doc:`./view-navigation` を書き終えた時点で全体の構成が気に入らないものになったので、
   スケルトンからやり直したい。

C ではなく Python を利用して OpenGL プログラムを書く利点は、
PyOpenGL_ の API を NumPy_ や Pillow_ といった、高品質なサードパーティ製パッケージの
部品と簡単に組み合わせて利用できるという点に尽きる。

欠点は何度も言うように実行が遅いことだ。悲しいくらい遅い。
しかし、グラフィックの初学者には遅い方が学習の上ではむしろ好都合ということもあるだろう。
なぜ遅いのか、何をすれば速くなるのかを考察することは、技術の向上には役に立つ。

.. toctree::
   :maxdepth: 5

   coding-intro
   appbase
   deprecatedapp
   modernapp
   program-manager
   transform
   view-navigation
   shader

.. include:: /_include/pyopengl-refs.txt
