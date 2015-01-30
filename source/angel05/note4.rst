======================================================================
OpenGL: A Primer Second Edition 読書ノート 4/4
======================================================================

.. include:: /_include/book-details/angel05.txt

.. contents:: ノート目次

Texture Mapping
===============
* <Texture mapping combines pixels with geometric objects> (p. 169)

What Is a Texture Map?
----------------------
* ピクセル配列を二次元のパラメータ区間に写像する。
  このパラメータ区間から、三次元空間上の曲面に写像する。
  この合成写像がテクスチャーマッピングだと大雑把に読み取れた。
* テクスチャー座標は記号 (s, t) で表現する。

Constructing a Texture Map
--------------------------
1. テクスチャーのイメージを準備する。イメージの表現については前章参照。
2. テクスチャーマッピングのためのパラメータを指定する。
3. 頂点に対してテクスチャー座標を定義する。

* <Two dimensional texture mapping is the most familiar case> (p. 171)
* 二次元的なイメージは、二次元多様体にマップするのが自然だろう。

  .. code-block:: c

     glEnable(GL_TEXTURE_2D);
     glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 64, 64, 0, GL_RGB, GL_UNSIGNED_BYTE, myimage);

* イメージの縦横サイズは、2 のベキ乗の形をしていなければならない。
  註によると、新しいグラフィックカードは任意の縦横サイズを許しているようだ。

* <It may take a significant amount of time to move a texture image from
  processor memory to texture memory> (p. 173)

Texture Coordinates
-------------------
* <Just as with vertices, texture coordinates are represented internally
  in four dimensions that conventionally use the letters (s, t, r, q) to
  denote the coordinates> (p. 173)

* テクスチャーマッピングを試すためのコツを以下のように述べている。
  <Checkerboards are especially useful for demonstrating the various 
  options and seeing how OpenGL implements texture mapping> (p. 174)

* <We see that OpenGL renders the quadrilateral as two triangles> (p. 174)

* 頂点座標と同様に、テクスチャー座標を行列を用いて変換することができる。

  .. code-block:: c

     glMatrixMode(GL_TEXTURE);

Texture Parameters
------------------
テクスチャー座標やテクスチャー画像以外にも、
テクスチャーマッピングが要求するパラメータがいくつもある。

* ``glTexParameter(target, name, value)``

  :target: ``GL_TEXTURE_2D``
  :name: ``GL_TEXTURE_xxx``

* <The required parameters determine what happens when values of 
  s, t, r, or q go outside the range (0, 1) and how sampling and
  filtering are applied> (p. 176)

* ``GL_TEXTURE_WRAP_(S|T)``, ``GL_(REPEAT|CLAMP)`` を憶える。

* magnification と minification の考え方を習得する。
  一つのテクスチャー画素が複数のピクセルに写像する方が magnification

* ``GL_TEXTURE_(MAG|MIN)_FILTER`` を ``GL_NEAREST`` にすると速い。

* 透視図法でシーンを描いている場合、テクスチャーが歪む場合がよくある。
  そういう場合は ``glHint`` を呼ぶ。

  .. code-block:: c

     glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST);

  ``glHint`` は他のレンダリングオプションにも利用できる。調べる。

A Rotating Cube with Texture
----------------------------
省略。

Applying Textures to Surfaces
-----------------------------
ポリゴンの地の色とテクスチャーマッピングをミックスする方法について。

* ``glTexEnv(target, param, value)``

  :target: ``GL_TEXTURE_ENV``
  :param: ``GL_TEXTURE_ENV_MODE`` とか ``GL_TEX_ENV_COLOR`` とか。
  :value: ``GL_(MODULATE|REPLACE|BLEND|DECAL)`` とか色とか。

* <The default mode of operation is called modulation. 
  Here the texture color multiplies the color computed for each face>
  (p. 181)

  .. code-block:: c

     glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE);

Borders and Sizing
------------------
* テクスチャーマッピングは、テクスチャーイメージ境界付近の処理が難しい。

* <One difficulty that arises when we use linear filtering is what happens
  at the edges of the texture where we lack one or more texels to use
  in the filtering> (p. 181)

* テクスチャーに枠を付加するという仕様がある。
  もし枠を指示するのなら、テクスチャーの縦横サイズを 2 のベキ乗 + 2 の形にする。

* 枠の色を別途指示することができる。

  .. code-block:: c

     glTexParameter3fv(GL_TEXTURE_2D, GL_TEXTURE_BORDER_COLOR, color);

* フレームバッファ内のイメージからテクスチャーマップを得ることができる。
  ただし「出力先」はテクスチャーメモリー。
 
  .. code-block:: c

     glCopyTexImage2D(target, level, iformat, x, y, w, h, border);

* 既に存在するテクスチャーから、その部分のコピーを（バイナリの形で）得ることもできる。

  .. code-block:: c

     glTexSubImage2D(target, level, xoffset, yoffset, w, h, format, type, texels)

* 応用例がちょっと思いつかないが、テクスチャーメモリ内でコピーすることもできる。

  .. code-block:: c

     glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, w, h)

Mipmaps
-------
* Mipmap とはテクスチャーマッピングの LOD の技法。
  広い領域にマップするデータと、狭い領域にマップするデータを使い分ける。

* <What we would prefer is to have a texture value that is the average of
  the texels values over a large area of the texture> (p. 183)

* ``glTexImage2D`` の第二引数 (``level``) に応じて、イメージを変える。
  本文の例では、レベルが低いほど詳細なイメージを指示している。

  .. code-block:: c

     glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST_MIPMAP_NEAREST);

  <This is the lowest quality option> (p. 183)

* ミップマップセットを生成し、テクスチャーメモリに格納してくれる GLU の関数がある。

  .. code-block:: c

     gluBuild2DMipmaps(target, iformat, w, h, format, type, texels);

Automatic Texture Coorinate Generation
--------------------------------------
* 頂点に対してテクスチャー座標を決める作業は一般的には難しい。
  しかし、GLU 二次曲面はテクスチャー座標を生成する関数が提供されている。

  * ``gluQuadricTexture(obj, mode)``

    :mode: ``GL_(TRUE|FALSE)``

* <OpenGL allows us to generate texture coordinates that are measured as
  distances from a plane in either object space or eye space> (p. 186)
  だそうだが、平面からの距離で決まる座標というのが解りにくい。

* <The value :math:`ax + by + cz + dw` is proportional to the distance from
  :math:`(x, y, z, w)` to the plane determined by :math:`(a, b, c, d)`> (p. 186)

* テクスチャー座標自動生成には、例えば (s, t) の場合は以下の呼び出しが必要。

  .. code-block:: c

     glEnable(GL_TEXTURE_GEN_S);
     glEnable(GL_TEXTURE_GEN_T);

* ``glTexGen(texcoord, param, value)``

  :texcoord: ``GL_[STRQ]``
  :param: ``GL_TEXTURE_GENMODE`` か ``GL_(OBJECT|EYE)_LINEAR``
  :value: ``GL_(OBJECT|EYE)_LINEAR`` か平面の係数配列

* 視点座標でテクスチャーを貼る：
  <If we use the ``GL_EYE_LINEAR`` mode, texture coordinates are based on
  the vertex positions in eye space so that when we move the object,
  the texture coordinates assigned to vertices change> (p. 188)

Texture Objects
---------------
テクスチャーもまた OpenGL の「状態」の一部だ。
glTexImage を実行するときに、システムメモリからテクスチャーメモリへ
移動する。テクスチャーを何種類も利用する場合は、移動にコストをつけたくない。
そこで texture object というものを提供している。

* <If there is not sufficient memory for all the textures that we need,
  we can prioritize the texture objects to minimize the amount of
  data movement from the processor to texture memory> (p. 188)

* ``glGenTextures(n, name)`` で ``n`` 個の texture objects を新規作成する。
* ``glIsTexture(name)`` で ``name`` が texture object か否かをテストする。

* <``glBindTexture()``, that both switches between texture objects and
  forms new texture objects> (p. 189)

* ``glBindTexture(target, name)``

  :target: ``GL_TEXTURE_[123]D``
  :name: texture object の ID

* ``glBindTexture`` の振る舞いは、次の三つのどれか。

  * case 1: <If we call ``glBindTexture()`` with name and name has not been
    used before, the subsequent calls to the various texture functions
    define the texture object with the id name>

  * case 2: <If name already exists from a previous call to ``glBindTexture()``,
    then that texture object becomes the present texture and is applied
    to surfaces until the next call to ``glBindTexture()``>

  * case 3: <If ``glBindTexture()`` is called with name set to 0, then the
    normal texture calls apply and the present texture that is part of
    the OpenGL state and the current values of the texture parameters
    both apply>

* テクスチャーオブジェクトを破棄したい場合は ``glDeleteTextures`` を呼ぶ。

  * ``glDeleteTextures(n, namearray)``

Texture Maps for Image Manipulation
-----------------------------------
テクスチャーパラメータのセットだけだが、サンプルコードのラストが参考になる。

Curves and Surfaces
===================
ベジエ中心の話題。

Parameteric Curves
------------------
* この本にしては例外的に数学の話が多くなるが、
  「コンピューターには区分的パラメトリック曲線が相性がいい」
  のようなことを述べている。

* <Parametric curves give a point in homogeneous coordinate space
  :math:`(x(u), y(u), z(u), w(u))` for each value of u> (p. 193)

* 簡単にするため、当分 :math:`w = 1` と固定して話を進める。

* 指定した点を通過するような n 次多項式を決めるには、
  :math:`3(n + 1)` 個の係数を求める必要があるので、
  :math:`3(n + 1)` 個の独立した条件を与える必要がある。

* 以降、基本的に 3 次式の話になる。4 つの点を決めれば、多項式の係数が求まる。

* <However, in computer graphics, interpolating curves usually
  are not the most useful type due to their lack of smoothness>
  (p. 194) 通過点を指定する曲線の決め方は、コントロールが難しい。

Parameteric Surfaces
--------------------
* 曲面を二変数関数で表現する。
  CG での曲面関数は通常は bicubic polynomial だと言っている。
  曲線を curve segment の継ぎはぎで表現したのと同じ発想で、
  曲面を surface patch で表現する。

Bezier Curves and Surfaces
--------------------------
* 三次ベジエ多項式の性質についてザッと説明している。

  * コントロールポイントが 4 つ (Q0, Q1, Q2, Q3) ある。
  * Q0 と Q3 は曲線の始点と終点にそれぞれ一致する。
  * 直線 Q0Q1 と Q2Q3 は、それぞれ曲線の始点と終点の接線だ。
  * 曲線全体は多角形 Q0Q1Q2Q3 に内包される。
    これを convex hull property という。
  * Bernstein 多項式として知られる多項式の族である。
    Bernstein 多項式はとても効率的に実装できる。

* 任意の多項式曲線、多項式曲面はベジエ曲線、ベジエ曲面から得られる。

* <OpenGL implements Bezier curves and surfaces through a mechanism known
  as **evaluators**> (p. 197)

* <such as line segments and polygons that approximate the curve or surface>
  (p. 197)

One-Dimensional OpenGL Evaluators
---------------------------------
* まず ``glMap1`` 関数の紹介から始まる。

  * ``glMap1(entity, u0, u1, stride, order, data)``

    :entity: この曲線が何の値を表現しているのかを指定する。
             <If we want a curve, we set entity to ``GL_MAP1_VERTEX_3``> (p. 198)
             ただし ``glEnable(GL_MAP1_VERTEX_3)`` の呼び出しが別途必要。

    :order: ベジエ曲線の次数プラス 1 を与える。
            すなわち、制御点の総数を意味する。

* ``glMap1`` で曲線を定義したら、その計算をし、結果を取得する。
  それには ``glEvalCoord1`` を用いる。
  今までは ``glVertex`` 等を利用していたところを ``glEvalCoord1`` に置き換わる感じ。

  * ``glEvalCoord1(u)``

* ところで、パラメータ u をいちいち手計算して与えるのは面倒だ。そんなときには
  <OpenGL provides an alternative for equally spaced values of u>
  (p. 199)

  * ``glMapGrid1(n, u0, u1)``

    :n: 区分数を意味する。

  * ``glEvalMesh1(mode, first, last)``

    :mode: ``GL_(LINE|POINT)``
    :first, last: 0 以上 ``glMapGrid1`` で与えた n 以下の数。

Two-Dimensional Evaluators
--------------------------
* 次の関数を利用して二次元 Bernstein 多項式を評価することができる。
  すなわち、ベジエ曲面を描画できる。

  * ``glMap2(entity, u0, u1, ustride, uorder, v0, v1, vstride, vorder, data)``
  * ``glEvalCoord2(u, v)``
  * ``glMapGrid(n, u0, u1, m, v0, v1)``
  * ``glEvalMesh2(mode, ufirst, ulast, vfirst, vlast)``

Other Types of Curves
---------------------
* <In other words, a cubic polynomial is both a Bezier curve and
  an interpolating curve for different set of control points> (p. 203)

* 通過点から制御点を求める行列を紹介している。憶えなくてよい。

B-Splines
~~~~~~~~~
* まず、ベジエ曲線・曲面はスプライン曲線・曲面の一種であることをおさえる。

* B スプラインもキュービックが基本。
  <The most popular type of spline is the cubic B-spline> (p. 204)

* キュービックスプラインの制御点を、同一形状のベジエ曲線の制御点に
  変換する行列を紹介している。憶えなくてよい。

NURBS
~~~~~
* OpenGL では GLU が NURBS をサポートしている。
* NURBS のキモは w 成分にあるようだ。

The Utah Teapot
---------------
* 例のティーポットの構成を説明。
  <The teapot is composed of 32 cubic Bezier surface patches, defined
  by 306 distinct control points.  The data set is widely available
  and usually is given as 32 lines, each of 16 integers in the range
  of 1-192.  Each integer is a pointer to one of the 306 (x, y, z)
  values> (p. 207)

Normals and Shading
-------------------
* 曲面 evaluator が内部的に生成する頂点に対して法線を指定するには、

  .. code-block:: c

    glEnable(GL_AUTO_NORMAL);

  するだけでよい。

Texturing Surfaces
------------------
* <We can also use evaluators to generate normals for shading and
  texture coordinates> (p. 213)

  どうするかというと、 ``glMap2`` で実現できる。

  .. code-block:: c

    glMap2f(GL_MAP2_TEXTURE_COORD_2, u0, u1, ...);

Putting It Together and Moving On
=================================
今まで紹介した機能プラスアルファで、デモプログラムを作る。
目玉はトラックボールとフォグか。

A Demo Program
--------------

A Virtual Trackball
~~~~~~~~~~~~~~~~~~~
マウスの動きから仮想的なトラックボールを作る。方針は
<by projecting the position of the mouse upward to the virtual
hemisphere, as in Figure 10.2.  As the mouse moves, the program
tracks the change in position on the hemisphere.  Two positions
on the hemisphere determine both an axis of rotation and an 
angle to rotate about this axis, as shown in Figure 10.3> (p. 216)

Other OpenGL Features
---------------------
* OpenGL tessellator で凸多角形制限をかわすことができる。
* <the use of NURBS requires more understanding of their mathematical
  underpinnings than we can present here> (pp. 230-231)

Buffers
-------
* OpenGL は色々なバッファをサポートしているが <not all of these buffers
  need be available on all implementations> (p. 231) だ。

* accumulation バッファや stencil バッファを利用するプログラムでは、
  ``glutInitDisplayMode`` の引数に、そのことを明示的に指示する。

  .. code-block:: c

    glutInitDisplayMode(GL_XXX | GL_STENCIL | GL_ACCUM);

    glClear(GL_XXX | GL_ACCUM_BUFFER_BIT | GL_STENCIL_BUFFER_BIT);

* auxiliary バッファはマルチパスレンダリングに利用するかもしれない。

The Accumulation Buffer
~~~~~~~~~~~~~~~~~~~~~~~
* カラーバッファの精度に不足がある場合にこのバッファが役に立つらしい。
  まさに CPU レジスタの accumulator のような働きをするようだ。

* ``glAccum(operation, value)``

  :operation: ``GL_(ACCUM|LOAD|RETURN|ADD|MULT)``

* カメラがブレているような画像効果を狙ったマルチパスレンダリングに応用する
  ことが考えられる。

The Stencil Buffer
~~~~~~~~~~~~~~~~~~
* <Stencils are masks that we can use to determine where to draw> (p. 232)

Fragment Tests
~~~~~~~~~~~~~~~
* <in OpenGL the rasterizer produces **fragments**, which contain all the
  information needed to update pixels in the frame buffer pixel> (p. 233)

* <Fragments that are produced by the rasterizer go through a sequence of
  tests--scissor, alpha, stencil, depth--and operations--blending,
  dithering, logical--on their way to the color buffer> (p. 233)

Writing Portable, Efficient, Robust Code
----------------------------------------
* OpenGL はポータブルとはいえ、当然その実装によっては制限がある。

* <One is that once we start using advanced features, such as the 
  accumulation and stencil buffers, we often lose portability, 
  as these features are not supported on all implementations> (p. 233)

* <We do not know--nor do we usually need to know> (p. 234)

Looking to the Future
=====================
* <OpenGL version 1.0 was released in 1992> (p. 235)

Versions and Extensions
-----------------------
* <extensions may apply to only some systems>

OpenGL Version 1.1
~~~~~~~~~~~~~~~~~~
* 1995 年に登場。このバージョンが特に重要な理由は
  <Version 1.1 is still the most widely used version> (p.235)
  だから。

* 頂点配列、テクスチャー操作、RGBA 色に対する論理演算、
  ポリゴンオフセットが導入された。

OpenGL Version 1.2
~~~~~~~~~~~~~~~~~~
* 1998 年に登場。三次元テクスチャーマッピング機能。
* imaging subset の追加

OpenGL Version 1.3
~~~~~~~~~~~~~~~~~~
* 2001 年に登場。テクスチャー処理性能を向上させる目的の機能追加。

* 転置行列関数もこのバージョンで登場した機能。
  これで Fortran 式の column order な配列だけでなく、
  C 言語風の row order 配列もそのまま使えるようになった。

OpenGL Version 1.4
~~~~~~~~~~~~~~~~~~
* 2002 年に登場。かつての拡張機能がコアに追加された。

OpenGL Version 1.5
~~~~~~~~~~~~~~~~~~
* 2003 年に登場。コアにマイナーチェンジを施しただけ。

OpenGL Extensions
-----------------
* <Individual manufacturers can propose and implement extensions> (p. 237)
* <As hardware evolves, high-end features that were only available 
  as extensions become part of later versions of OpenGL> (p. 237)

Going Beyond Read-Time Graphics
-------------------------------
* <Pixar's RenderMan interface>
* <we cannot edit OpenGL display lists> (p. 238)
* <all the information about the image is in the tree of Figure 11.1.
  This tree is known as a **scene graph**> (p. 238)

* シーングラフを設計するのは難しい。
  <The answer today should be a set of atomic primitives that can take
  advantage of the existing hardware and APIs> (p. 239)

* <an application programer who wants to use scene graphs can often
  avoid writing a program using the scene graph API by specifying
  the scene through a text file that provides an alternate method
  of describing the tree> (p.239)

Programmable Pipelines
----------------------
* パイプラインの一部をユーザープログラムで置き換えるような造りを考える。
* <Graphics processors have become programmable> (p. 240)
* vertex shader と fragment shader の 2 ブロックがそうだ。

Vertex Shaders
~~~~~~~~~~~~~~
例えば Phong モデル以外の照光モデルで頂点の色を計算できる。

Fragment Shaders
~~~~~~~~~~~~~~~~
* <In particular, the fragment shader can access one or more texture
  coordinates, light properties, normals, and camera properties>
  (p. 241)

Shading Languages
-----------------
RenderMan Shading Language
~~~~~~~~~~~~~~~~~~~~~~~~~~
* <Once we realize that the Phong shader can be written as a tree data
  structure, it is fairly simple to extend this concept to other shaders
  by adding nodes to the tree and altering the contents of its node.
  This concept of a **shading tree** is fundamental to much recent work
  on shading languages> (pp. 242-243)

The OpenGL Shading Language
~~~~~~~~~~~~~~~~~~~~~~~~~~~
* 2003 年に ARB が extension として採用したのが OpenGL シェーディング言語。
  C 言語がベースで、vertex shader と fragment shader の両方に用いられる。

Cg
~~
* <Rather than have separate APIs for accessing programmable hardware
  for OpenGL and Direct3D, NVIDIA and Microsoft developed the Cg
  (C for graphics) language> (p. 244)
