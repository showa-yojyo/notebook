======================================================================
コードを書く
======================================================================

C ではなく Python を利用して OpenGL プログラムを書く利点は、PyOpenGL_ の API を
NumPy_ や Pillow_ といった、高品質なサードパーティ製パッケージの部品と簡単に組み
合わせて利用できるという点に尽きる。

欠点は何度も言うように実行が遅いことだ。悲しいくらい遅い。しかし、グラフィックの
初学者には遅い方が学習の上ではむしろ好都合ということもあるだろう。なぜ遅いのか、
何をすれば速くなるのかを考察することは、技術の向上には役に立つ。

.. toctree::
   :maxdepth: 2

   coding-intro
   tips
   appbase
   deprecatedapp
   modernapp
   program-manager
   transform
   view-navigation
   imagefile
   shader

.. include:: /_include/python-refs-sci.txt
.. include:: /_include/python-refs-vision.txt
