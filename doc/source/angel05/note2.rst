======================================================================
OpenGL: A Primer Second Edition 読書ノート 2/4
======================================================================

.. include:: /_include/book-details/angel05.txt

.. contents:: ノート目次

Basic Three-Dimensional Programming
===================================
Cameras and Objects
-------------------
* そもそも投影とは何か。次のように説明している。
  <The process of combining the specifications of objects and camera is
  called **projection**> (p.77)

* カメラの指定方法は、オブジェクトのそれほど直感的ではない。
  カメラ自身の位置に加え、どちらを向いているのかという情報と、
  その向きに対してどれくらい回転がかかっているのかという情報が必要。

* 直交投影 (orthographic projection) は最も単純な種類の投影だ。

* viewing volume, front/back (or near/far) clipping plane の概念をおさえること。

* ピラミッドの角をカットしたような形状を frustum という。

Orthographic Projections in OpenGL
----------------------------------
* <The viewing frustum becomes a right parallelpiped -- a rectangular box>
  (p. 80)

* ``glOrtho(left, right, bottom, top, near, far)`` - 視点座標系で引数を与える。

  * ``left < right`` かつ ``bottom < top`` かつ ``near < far`` である必要がある。

* <Note that ``gluOrtho2D()`` is derived from ``gluOrtho()`` by setting near
  and far to -1 and +1 respectively> (p.81)

Viewing a Cube
--------------
* GLUT には座標原点に指定サイズのキューブを描画する便利な関数がある。

  * ``glutWireCube(size)`` - 各辺の長さが ``size`` のワイヤーキューブを描く
  * ``glutSolidCube(size)`` - 各辺の長さが ``size`` のソリッドキューブを描く

Locating the Camera
-------------------
キューブを別の角度から見たいとする。このときカメラを動かすか、キューブを動かせば
よいのだが、カメラを動かすことを先に知る。

<We can decide on a position for the camera (called the **eye point**)
and decide where to aim it to by specifying a point at which it 
is pointing (the **at point**)>

<We need a third input, the direction we want to consider as up
in the image (the **up vector**)> (p. 83)

<A simple choice of the up vector is often :math:`(0, 1, 0)` or
the y direction in world coortinates> (p. 83)

* ``gluLookAt((eye), (at), (up))``

  :eye: 視点の位置 :math:`(x, y, z)`
  :at: 注視する点の位置 :math:`(x, y, z)`
  :up: イメージの上方を定義するベクトル :math:`(x, y, z)`

* カメラの設定コードはほぼ必ず以下のようになる。

  .. code:: c

     glMatrixMode(GL_MODELVIEW);
     glLoadIdentity();
     gluLookAt(...);

Building Objects
----------------
* <the vertices in a counterclockwise manner when each face is
  viewed from the outside> (p. 86)

Using Arrays
~~~~~~~~~~~~~
これまでのやり方だと、頂点を指定するのは大量の関数呼び出しを伴うが、
頂点配列を用いることで、関数呼び出しの回数を減らすことができる。

Vertex Arrays
~~~~~~~~~~~~~
* <OpenGL provides support for six types of arrays: vertex, color,
  color index, normal, texture coordinate, and edge flag> (p. 88)

* ``glEnableClientState(arraytype)``,
  ``glDisableClientState(arraytype)``

  :arraytype: ``GL_(VERTEX|COLOR|INDEX|NORMAL|TEXTURE_COORD|EDGE_FLAG)_ARRAY``

* ``glVertexPointer(dim, type, stride, array)``, 
  ``glColorPointer(dim, type, stride, array)``

  :dim: データの次元数 [234]
  :type: ``GL_(SHORT|INT|FLOAT|DOUBLE)``
  :stride: ``array`` の中にデータがどのように連続して詰まっているかを示す数

* ``glDrawElements(mode, n, type, indices)``

  :mode: 例えば ``GL_POLYGON`` とか
  :n: インデックスの個数
  :type: ``indices`` の型。例えば ``GL_UNSIGNED_BYTE`` とか。

* コード例

  .. code:: c

     GLfloat vertices[][3] = {...};
     GLfloat colors[][3] = {...};
     GLubyte cubeIndices[] = {
         0, 3, 2, 1,
         2, 3, 7, 6,
         ...
         };

  とすると、とりあえずは以下のように面を描画できる。

  .. code:: c

     glEnableClientState(GL_COLOR_ARRAY);
     glEnableClientState(GL_VERTEX_ARRAY);
     glVertexPointer(3, GL_FLOAT, 0, vertices);
     glColorPointer(3, GL_FLOAT, 0, colors);
     for(i = 0; i < 6; i++){
         glDrawElements(GL_POLYGON, 4, GL_UNSIGNED_BYTE, cubeIndices);
     }

  ループはさらにシンプルにできる。

  .. code:: c

     glDrawElements(GL_QUADS, 24, GL_UNSIGNED_BYTE, cubeIndices);

Hidden-Surface Removal
----------------------
* 観察者からは角度的に見えない面を描画しない手法を指す。
* 例えば

  .. code:: c

     glEnable(GL_CULL_FACE);
     glCullFace(GL_BACK);

  が考えられるが、この方法は先述のように convex objects に対してのみ働く。

* オブジェクトの奥行きを管理するバッファを z-buffer or depth buffer という。
* <In most programs, the depth buffer should be cleared whenever
  the color buffer is cleared> (p. 91)

  .. code:: c

     glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH);
     // ...
     glEnable(GL_DEPTH_TEST);

GLU and GLUT Objects
--------------------
* よく利用される幾何形状の描画は、GLU や GLUT が提供している。
* 円柱だとか球だとかもあるが、基本的には多角形近似である。

GLUT Quadrics
~~~~~~~~~~~~~
* <GLUT provides three types of quadrics: spheres, cylinders, and disks>
  (p. 92)

* ``gluNewQuadric()`` - 二次曲面オブジェクトを生成して、そのポインターを返す。
* ``gluDeleteQuadric(obj)`` - 二次曲面オブジェクトを削除する。

* Quadric objects は四種類のレンダー様式がある。
  点、線、塗りつぶしはいつも通りだが、シルエットというものがある。

  * ``gluQuadricDrawStyle(obj, style)``

    :style: ``GLU_(POINT|LINE|FILL|SILHOUETTE)``

  * ``gluQuadricNormals(obj, mode)``

    :mode: ``GLU_(NONE|FLAT|SMOOTH)``

  * ``gluQuadricTexture(obj, mode)``

    :mode: ``GL_(TRUE|FALSE)``

* どの GLU 二次曲面も内部的には多角形近似で描くのだが、
  その多角形の点の多さのようなものを引数に指示する必要がある。

  * ``gluSphare(obj, radius, slices, stacks)``

    * <The sphere is approximated with polygons using slices lines
      of longitude and stacks linces of latitude> (p. 93)

  * ``gluCylinder(obj, base, top, height, slices, stacks)``

    * 名前は円柱だが、上面と底面で半径を別々に指示できる。

  * ``gluDisk(obj, inner, outer, slices, rings)``

    * 文字通り円盤。中央に穴が開いている。

  * ``gluPartialDisk(obj, inner, outer, slices, rings, start, angle)``

    * 扇形円盤。
    * <Partial disks are disks with a wedge removed> (p. 94)

GLUT Objects
~~~~~~~~~~~~
* 球、円錐、トーラス、正多面体、果てはティーポットまで提供している。
* 二次曲面系は多角形近似のための引数指定が必要。面倒そうだな。

  * ``glutWireSphere(radius, slices, stacks)``, ``glutSolidSphere(radius, slices, stacks)``
  * ``glutWireCone(base, height, slices)``, ``glutSolidCone(base, height, slices)``
  * ``glutWireTorus(inner, outer, sides, slices)``, ``glutSolidTorus(inner, outer, sides, slices)``

* 正多面体 (regular polyhedral) をすべてサポート。キューブ以外を特に強調している。
  半径 1 の球に内接するサイズで定義されている。

  * ``glutWireTetrahedron()``, ``glutSolidTetrahedron()``
  * ``glutWireOctahedron()``, ``glutSolidOctahedron()``
  * ``glutWireDodecahedron()``, ``glutSolidDodecahedron()``
  * ``glutWireIcosahedron()``, ``glutSolidIcosahedron()``

* 特筆すべきは何と言ってもティーポットだ。
  <The Utah teapot is generated using OpenGL surface.  The teapot
  has been used for many years for testing rendering algorithms.
  It is constructed from 192 vertices.  The teapot is generated
  with both normals and texture coordinates> (p. 97)

  * ``glutWireTeapot(size)``, ``glutSolidTeapot(size)``

    ティーポットを ``size`` の大きさで描く。

Perspective Projections
-----------------------
* 透視図法投影を実現するための行列操作を習得する。
* ``glFrustum(left, right, bottom, top, near, far)``

  * 引数リストは ``glOrtho`` と同じ。
  * :math:`far > near > 0` に注意。
  * ほぼ必ず以下の手順で利用する。

    .. code:: c

       glMatrixMode(GL_PROJECTION);
       glLoadIdentity();
       glFrustum(left, right, bottom, top, near, far);

* glFrustum と gluPerspective の使いやすさの違いを憶えておく。
  <the interface provided by ``glFrustum()`` can make it difficult
  to obtain a desired view> (p. 98)

* <we change the lens and get one with a wider angle of view.
  The function ``gluPerspective()`` provides such an interface> (p. 98)

* ``gluPerspective(fov, aspect, near, far)``

  :fov: 角錐台の上下間の角度。
  :aspect: ``width / height``

* <One potential problem with perspective views is loss of
  accuracy in depth, which can be noticeable in the display>
  (p. 100)

* near plane をカメラに近づけ過ぎぬ事。
  <The problem is worst when the near plane is very close to
  the center of projection> (p. 100)

* <Placing the front clipping plane too close to the camera can lead to numerical 
  errors in depth calculations for perspective views> (p. 100)

Programming Exercises
----------------------
* 球を自力で多角形近似で描画するときのコツは、
  <Use quad strips except for triangle fans at the poles> (p. 100)
  だそうだ。


Transformations
===============
これを習得しておかないと、geometric objects の操作、シーンの
アニメーションや、狙い通りのビューを得ることができない。

Line-Preserving Transformation
------------------------------
* この章の文章では、transformation は「写像」の意味で用いられている。
  <**Transformations** map vertices and vectors to other vertices and 
  vectors> (p. 101)

* <rotations and translations are known as **rigid-body transformations**> (p. 101)
  換言すれば「サイズの変わらない」変換。

* 我々が興味のある写像は点・ベクトルを点・ベクトルに写すものであることは当然ながら、
  さらに直線を直線に写すものだ。とはいえ、
  <If we restrict ourselves to transformations that preserve line segments,
  then we need only transform the endpoints--two vertices--of each line
  segment> (p. 102)
  なので、結局点の写像のみに絞って考えればよい。

* **affine transformations** のポイント
  1. translation, rotation, scaling はその一種である
  2. 平行な直線群を平行な直線群へ写す
  3. 逆方向の変換が存在する

* **projection transformations** は通常逆変換は考えられない。
  なぜなら、二次元に投影されたイメージから、元の三次元のイメージが復元できないからだ。

Homogeneous Coordinates
-----------------------
同次座標の考え方は OpenGL のレンダリング方法論の核と言えるようだ。

* すべての点は 4 つの座標成分 :math:`(x, y, z, w)` の組の形で表現されている。
* 三次元の点は :math:`(x, y, z, 1)` として内部的に表現されている。
* 二次元の点は :math:`(x, y, 0, 1)` として内部的に表現されている。
* 一般に点は :math:`(x, y, z)` として表現されるが、w がゼロでない限り、
  三次元の点 :math:`(x/w, y/w, z/w)` として見える。
* 三次元のベクトルは :math:`(x, y, z, 0)` として内部的に表現されている。
  これは無限遠点と等価だ。
* すべての transformations は点・ベクトルの同次座標表現に作用する
  :math:`4 \times 4` 行列となる。

Translation
-----------
* <Because the camera in OpenGL is also at the origin, we want to move
  the object away from the camera, or equivalently move the camera
  away from the object> (p. 103)
* translation とは、オブジェクトに変位 (**displacement**) を加える操作だ。
* translation の距離は右手座標系による。

Concatenating Translations
~~~~~~~~~~~~~~~~~~~~~~~~~~
* <The function ``glTranslate*()`` forms a translation matrix that
  is applied to the current matrix.  Thus, the two translations
  are combined or **concatenated** together to form a compound transformation>
  (p. 105)

Rotation
--------
* 回転変換には回転の影響を受けない点がある。これを **fixed point** と呼ぶ。
* 回転の向きについては、ここでも「反時計回りが正」のルールがある。

  <The desired amount of rotation about this axis is measured in a 
  counterclockwise direction looking from the positive direction 
  along the given direction back toward the origin> (p. 106)

Concatenation: Rotation with Arbitrary Fixed Point
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* 任意の点を fixed point として回転変換を生じさせたいとする。
  このときは ``glTranslate`` と ``glRotate`` を組み合わせて実現する。

  .. code:: c

     glMatrixMode(GL_MODELVIEW);
     glLoadIdentity();
     glTranslatef(x, y, z);
     glRotatef(angle, dx, dy, dz);
     glTranslatef(-x, -y, -z);

  * <*the last transformation specified is the first applied*> ルール。
    OpenGL の行列乗算は postmultiplication であることをおさえる。

* ディスプレイリストに変換行列の操作が含まれている場合は、
  リストの定義終了までに行列の状態を定義開始前のそれに復元するのが肝要。

  <Any primitives that are in display lists that do not change the
  current matrices are affected by the same model-view matrix.
  Conversely, if any matrices are changed in a display list, these
  changes are in effect after the execution of the display list> (p. 107)

Scaling
-------
* ここでも fixed point の考え方が有効だ。

  * <We also note that scaling has a fixed point that is unchanged by the
    scaling> (p. 107)
  * <The fixed point is at the origin, but we can use the same technique as
    with rotations to obtain any desired fixed point> (p. 108)

Setting Matrices Directly
-------------------------
* OpenGL の行列は :math:`4 \times 4` 正方行列で、メモリレイアウトとしては column-major order だ。

  * ``glLoadMatrix(m)`` - 行列成分を直接配列の形で指示する
  * ``glMultMatrix(m)`` - current matrix に対して ``m`` を右からかける

* shear 変換を実現するには、この直接行列指示でなければならない。

  .. math::
     :nowrap:

     \begin{pmatrix}
     1 & \cot \theta & 0 & 0 \\
     0 & 1           & 0 & 0 \\
     0 & 0           & 1 & 0 \\
     0 & 0           & 0 & 1
     \end{pmatrix}

* **oblique projection** を実現することもできる。

  .. code:: c

     glMatrixMode(GL_PROJECTION);
     glLoadIdentity();
     glOrtho(left, right, bottom, top, near, far);
     glMultMatrixf(M);

* 影の計算なども面白い。光源を :math:`(x, y, z)` として、z 平面に影を付ける変換は

  .. math::
     :nowrap:

     \begin{align*}
     \left(
         \begin{array}{rrrr}
             1 &0             &0 &0 \\
             0 &1             &0 &0 \\
             0 &0             &1 &0 \\
             0 &-\dfrac{1}{y} &0 &0
         \end{array}
     \right)
     \end{align*}

  で与えられる。コードは大体次のような構造になる。

  .. code:: c

     glMatrixMode(GL_MODELVIEW);
     cube();

     glPushMatrix();
     glPushAttrib(...);
     glTranslate(x, y, z);
     glMultMatrix(M);
     glTranslate(-x, -y, -z);
     glColor3fv(shadow_color)
     cube();
     glPopAttrib();
     glPopMatrix();

Transformations and Coordinate Systems
--------------------------------------
色々な座標（系）が出てきたので、ちょっと整理する。

* **world coordinates**
* **camera (or eye) coordinates**
* **clipping coordinates**
* **normalized device coordinates**
* **window coordinates**

Modeling with Transformations
-----------------------------
Instancing
~~~~~~~~~~
* <The matrix that brings the object into the model with the
  desired size, orientation, and position is called the
  **instance transformation**> (p. 114) 聞いたことのない用語だ。

* <The GLU cylinder was aligned with the z axis and has its base
  in the plane :math:`z = 0`.  With such a starting point, we almost
  always want to scale the object to its desired size, then
  orient it, and finally translate it to its desired position
  in that order> (p. 114)

  .. code:: c

     glMatrixMode(GL_MODELVIEW);
     glLoadIdentity();
     glTranslatef(x, y, z);
     glRotatef(theta, dx, dy, dz);
     glScalef(sx, sy, sz);

  文章に表れる変換順序と、OpenGL コードに現れる関数コール順が逆であることをおさえておく。

Hierarchical Models
~~~~~~~~~~~~~~~~~~~
* 人体モデルを木構造のデータとして表現する話題。
  木のルートから transform を適用していくテクニックを紹介している。
  ここでは胴体をルートとしている。

* <we can observe that each transformation actually represents
  a *relative* change from one scaling, position, and orientation
  to another> (p. 116)

* <Our first example did not require us tp save any information about 
  the model-view matrix as we went through the display callback
  because the transformations accumulated> (p.118)
