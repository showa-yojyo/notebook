======================================================================
OpenGL: A Primer Second Edition 読書ノート 2/3
======================================================================

:doc:`angel05-note1` からの続き。

:著者: Edward Angel
:出版社: Peason Education, Inc.
:ISBN: 0-321-26982-9

.. contents:: ノート目次

Transformations
===============
これを習得しておかないと、geometric objects の操作、シーンの
アニメーションや、狙い通りのビューを得ることができない。

Line-Preserving Transformation
------------------------------
* この章の文章では、transformation は「写像」の意味で用いられている。
  <**Transformations** map vertices and vectors to other vertices and 
  vectors.> (p. 101)
* rotations and translations are known as **rigid-body transformations** (p. 101)
  換言すれば「サイズの変わらない」変換。
* 我々が興味のある写像は点・ベクトルを点・ベクトルに写すものであることは当然ながら、
  さらに直線を直線に写すものだ。とはいえ、
  <If we restrict ourselves to transformations that preserve line segments,
  then we need only transform the endpoints--two vertices--of each line
  segment.> (p. 102)
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

* すべての点は 4 つの座標成分 (x, y, z, w) の組の形で表現されている。
* 三次元の点は (x, y, z, 1) として内部的に表現されている。
* 二次元の点は (x, y, 0, 1) として内部的に表現されている。
* 一般に点は (x, y, z, w) として表現されるが、w がゼロでない限り、
  三次元の点 (x/w, y/w, z/w) として見える。
* 三次元のベクトルは (x, y, z, 0) として内部的に表現されている。
  これは無限遠点と等価だ。
* すべての transformations は点・ベクトルの同次座標表現に作用する
  4 x 4 行列となる。

Translation
-----------
* Because the camera in OpenGL is also at the origin, we want to move
  the object away from the camera, or equivalently move the camera
  away from the object. (p. 103)
* translation とは、オブジェクトに変位 (**displacement**) を加える操作だ。
* translation の距離は右手座標系による。

Concatenating Translations
~~~~~~~~~~~~~~~~~~~~~~~~~~
* The function glTranslate*() forms a translation matrix that
  is applied to the current matrix.  Thus, the two translations
  are combined or **concatenated** together to form a compound transformation.
  (p. 105)

Rotation
--------
* 回転変換には回転の影響を受けない点がある。これを **fixed point** と呼ぶ。
* 回転の向きについては、ここでも「反時計回りが正」のルールがある。

  The desired amount of rotation about this axis is measured in a 
  counterclockwise direction looking from the positive direction 
  along the given direction back toward the origin. (p. 106)

Concatenation: Rotation with Arbitrary Fixed Point
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* 任意の点を fixed point として回転変換を生じさせたいとする。
  このときは、glTranslate と glRotate を組み合わせて実現する。
  ::

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    glTranslatef(x, y, z);
    glRotatef(angle, dx, dy, dz);
    glTranslatef(-x, -y, -z);

  * *the last transformation specified is the first applied* ルール。
    OpenGL の行列乗算は postmultiplication であることをおさえる。

* ディスプレイリストに変換行列の操作が含まれている場合は、
  リストの定義終了までに行列の状態を定義開始前のそれに復元するのが肝要。
  <Any primitives that are in display lists that do not change the
  current matrices are affected by the same model-view matrix.
  Conversely, if any matrices are changed in a display list, these
  changes are in effect after the execution of the display list.> (p. 107)

Scaling
-------
* ここでも fixed point の考え方が有効だ。

  * We also note that scaling has a fixed point that is unchanged by the
    scaling. (p. 107)
  * The fixed point is at the origin, but we can use the same technique as
    with rotations to obtain any desired fixed point. (p. 108)

Setting Matrices Directly
-------------------------
* OpenGL の行列は 4 x 4 正方行列で、メモリレイアウトとしては column order だ。

  * glLoadMatrix(m) - 行列成分を直接配列の形で指示する
  * glMultMatrix(m) - current matrix に対して m を右からかける

* shear 変換を実現するには、この直接行列指示でなければならない。
  ::

    M = 1  cot(theta)  0  0
        0           1  0  0
        0           0  1  0
        0           0  0  1

* **oblique projection** を実現することもできる。
  ::

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(left, right, bottom, top, near, far);
    glMultMatrixf(M);

* 影の計算なども面白い。光源を (x, y, z) として、z 平面に影を付ける変換は
  ::

    M = 1     0  0  0
        0     1  0  0
        0     0  1  0
        0  -1/y  0  0

  で与えられる。コードは大体次のような構造になる。
  ::

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
* The matrix that brings the object into the model with the
  desired size, orientation, and position is called the
  **instance transformation**. (p. 114) 聞いたことのない用語だ。
* The GLU cylinder was aligned with the z axis and has its base
  in the plane z = 0.  With such a starting point, we almost
  always want to scale the object to its desired size, then
  orient it, and finally translate it to its desired position
  in that order. (p. 114)
  ::
  
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
* we can observe that each transformation actually represents
  a *relative* change from one scaling, position, and orientation
  to another. (p. 116)
* Our first example did not require us tp save any information about 
  the model-view matrix as we went through the display callback
  because the transformations accumulated. (p.118)

Lights and Matrials
===================

Light-Material Interatctions
----------------------------
色の説明
  The colors that we see in the real world are based on the 
  interaction between light coming from light sources and
  the materials of which the objects are made. (p. 123)

影の説明
  These shadows are determined by light-material interactions.
  (p. 123)

  Such a calculation is beyond the capabilities of real-time
  rendering. (p. 123)

  Thus in OpenGL, shading must be done locally on a vertex-by-vertex 
  basis. (p. 123)

  we can do a fairly good job of shading on a vertex-by-vertex
  basis. (p. 123)

The Phong Model
---------------
* OpenGL では modifed Phong モデルをシェーディング計算に採用している。
* ある曲面をシェーディングしたいとする。このとき、曲面上の点 P に
  対して、次の四つのベクトルを導入する。

  :L: The direction to the light source from P.
  :V: The viewer is located in the direction V from P.
  :N: The normal vector at P.  
      局所的な曲面の向きという捉え方。
  :R: perfect reflector; 
      If the surface is highly refective, it will act like a 
      mirror and most of the light will go off in the direction of
      a perfect reflector R. (p. 125)

      The vector R can be computed from N and L. (p. 125)

* Phong モデルは P のシェーディングには、以下の四種類のものが
  寄与 (contributions) していると考える：

  * **diffuse reflections**
  * **specular reflections**
  * **ambient reflections**
  * **emissive light**

Diffuse Reflection
~~~~~~~~~~~~~~~~~~
* 曲面に照りつける光は、一部は材質により吸収され、一部は散乱する。
  この散乱は等方向に発生するので、diffuse の計算は V に依存しない。
* Diffuse surfaces tend to look dull like plastic. (p. 125)

Specular Reflection
~~~~~~~~~~~~~~~~~~~
* specular = 鏡のように反射する。
* a specular surface is smooth and the reflected light is
  concentrated along the direction R (p. 126)
* The Phong model characterizes this concentration with
  a **shininess coefficient**. (p. 126)
* 光沢のある材質が specular な曲面なのだ。
  <Specular surfaces include polished materials, such as metals.>
  (p. 126)
* OpenGL では R を L + V で代用して計算に用いる。

Ambient Reflection
~~~~~~~~~~~~~~~~~~
* 環境反射に関しては、これだけ憶えておけばいいか。
  <the light that we see does not depend on any of the four vectors,
  only on the incoming light and the fraction that is reflected.>
  (p. 126)

Emission
~~~~~~~~
* 物体が発光するケースもサポート。
  <we can add on an emissive term that is not affected by
  incoming light and can help model visible light sources
  or glowing objects.> (p.126)

OpenGL Lighting
---------------
* OpenGL は三種類の光源があることをおさえる。
  <In OpenGL, we can have point sources, spotlights, and ambient sources.>
  (p. 127)
* 光源は材質と共通するある性質を有している。
  <For each source there are separate diffuse, specular, and ambient
  RGB parameters.> (p. 127)
* 光源をオンにすることを忘れないこと。
  <Enabling lighting asks OpenGL to do the shading calculations.> (p 127)
* 一旦カラーのことを忘れよう。
  <Once lighting is enabled, colors assigned by glColor*() are no longer used.>
  (p. 127)
* 照光処理では、法線ベクトルの質が死活的に重要となる。
  <the user generally must supply the normal vectors through glNormal*().>
  (p. 127)
* glNormal3(dx, dy, dz)

  :dx, dy, dz: 法線ベクトルの各成分。

Specifying Light Sources
------------------------
* glLight に関する説明に紙幅を割いているが、ポイントは前半部に集中。
* The defaults are slightly different for light 0 and all the other sources.
  (p. 128)
* ライト 0 は白色なのだが、その他は黒となっている。
  <The default value of the position is (0.0, 0.0, 1.0, 0.0).  This value is 
  in eye coordinates, so it is  behind the default camera> (p. 128)
* z 軸の正の方向に無限の距離だけ離れたところが初期値。
  <w component indicates that the source is at infinity because w = 0
  indicates it is the representation of direction rather than of a point.>
  (p. 128)
* スポットライトのカットオフ角の初期値は 180 度だ。
* 光の減衰を指定するパラメータ (GL_xxx_ATTENUATION) があるが、
  デフォルトが減衰なしであることを憶えておけば、今はいい。

Light Sources and Transformations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* glLight で指定する光源の位置と向きは、モデルビュー変換の影響を受ける。

Specifying a Material
~~~~~~~~~~~~~~~~~~~~~
* Material properties match the lighting properties.  A material has
  reflectively properties for each type of light. (p. 131)
* glMaterial(face, name, value)

  :face: GL_FRONT, GL_BACK, GL_FRONT_AND_BACK
  :name: GL_AMBIENT 等

  Often the ambient and diffuce properties are the same and can be
  set together using GL_AMBIENT_AND_DIFFUSE. (p. 132)

* 材質のアルファ値は、その材質の透明感をシミュレートする用途で使うことができる。
* 余力があれば、材質のデフォルト値を憶えておく。
* GL_SHININESS については、
  <The higher the value of this parameter, the shinier the material appears
  as the specular highlights are concentrated in a small area near the
  angle of a perfect reflection.> (p. 132) 
  とのこと。

Shading the Rotating Cube
-------------------------
* ここのコードのポイントは以下の通り。

  * 照光処理を有効にして、利用する光源を有効にする。
    ::

      glEnable(GL_LIGHTING);
      glEnable(GL_LIGHT0);

  * 現在の材質を設定する。この例では前面だけに指定している。
    ::

      glMaterialfv(GL_FRONT, GL_AMBIENT, currentMaterials->ambient);
      glMaterialfv(GL_FRONT, GL_DIFFUSE, currentMaterials->diffuse);
      glMaterialfv(GL_FRONT, GL_SPECULAR, currentMaterials->specular);
      glMaterialf(GL_FRONT, GL_SHININESS, currentMaterials->shininess);

  * 光源の特徴を設定する。
    ::

      glLightfv(GL_LIGHT0, GL_AMBIENT, currentLighting->ambient);
      glLightfv(GL_LIGHT0, GL_DIFFUSE, currentLighting->diffuse);
      glLightfv(GL_LIGHT0, GL_SPECULAR, currentLighting->specular);
      glLightfv(GL_LIGHT0, GL_POSITION, light0_pos);

Controlling the Shading Calculation
-----------------------------------
* 照光処理は大量のリソースを必要とする。ゆえに、通常は前面だけを処理させるように
  glLightModel を介して設定する。

  * glLightModel(param, value)

    :param: GL_LIGHT_MODEL_(AMBIENT|LOCAL_VIEWER|TWO_SIDE)

    どうしても両面でシェーディングをしたければ TWO_SIDE を GL_TRUE にセット。

  * オブジェクトが視点から相当距離離れている場合、照光計算を簡略化するべく
    LOCAL_VIEWER を TRUE にセットすることができる。

  * すべての光源がオフであっても、少量の環境光が存在するように指示できる。
    AMBIENT にグローバルな環境光の RGBA 値を指示すればよい。

Smooth Shading
--------------
* GL_SMOOTH がデフォルトの照光処理。
* 巨大なポリゴンをシェーディングすると、中央部が妙に暗くなる。
  これを回避するには、ポリゴンを細分化する。

Working with Normals
--------------------
* the quality of our shading depends on the normals (p. 138)
* Smooth shading is sometimes called Gouraud shading. (p. 138) グーローシェーディング。
* The lighting calculations require that the normal vector have unit length (p. 138)
* 効率が落ちるのを覚悟で、OpenGL に法線の長さを 1 になるようにお願いすることができる。
  ::

    glEnable(GL_NORMALIZE);

  しかし、何と言っても最大の注意点は、
  <Scaling changes the lengths of normals.> (p. 139)
  ということだ。

Transparancy
------------
シェーディングのことをいったん忘れて、ブレンディングの話題になる。

* OpenGL は RGBA 値の A の値の指定は通常無視するが、ブレンディングを
  明示的に有効にすれば意味を持つようになる。
  ::

    glEnable(GL_BLEND);

* アルファ値は、通常 opacity を表現する。透明度の逆の概念。
  <the usual use is to use this value to determine the degree of opacity
  of a color or material.> (p. 139)

* 半透明オブジェクトの描画に関しては、忘れてはならない重大なポイントがある。
  オブジェクトの描画順によって、結果が違ってくるということだ。

* OpenGL provides a variety of constants that determine how to
  blend colors and alpha values. (p. 140)

* source 色と destination 色という考え方。塗り絵みたいなもんだ。
  <When blending is disabled, the source color simply replaces
  the destination color.> (p. 140)

  結果色 := X * source + Y * destination

* glBlendFunc(source, destination)

  :source: source 側のブレンディング係数。e.g. GL_SRC_ALPHA
  :destination: destination 側のブレンディング係数。e.g. GL_ONE_MINUS_SRC_ALPHA

  よく使う係数はこれ：
  <When we draw polygonal surfaces, the most common choices for the 
  source factor and destination factors are GL_SRC_ALPHA and
  ONE_MINUS_SRC_ALPHA, respectively.> (p. 140)
  つまり、ソースのアルファ値のみをブレンド率としている。
  ::

    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

* ブレンド率をいいかげんに指定すると、最終的な値が [0, 1] の外にいってしまうことがある。
  デプスバッファがここでも活躍する。
  <We can use the depth buffer to keep track of whether or not a 
  polygon is in front of all polygons that have been rendered so far.>
  (p. 141)
  <OpenGL provides a function glDepthMask(), which can make the depth
  buffer read-only (GL_FALSE) or writeable (GL_TRUE).> (p. 141)

* アルファ値 (opacity) が 1.0 であるオブジェクトを描く前にデプスマスクを
  有効にし、半透明なオブジェクトを描く前には read-only にすればよい。

Images
======
この章ではフレームバッファとピクセルの概念を頭に叩き込む。

Pixels and Bitmaps
------------------
* The frame buffer is really a collection of buffers.  For each x, y value
  in screen space, there is a corresponding group of bits that can be thought
  of as a generalized picture element or **pixel**. (p. 143)

* 明らかに註が重要。用語の意味の汲み方を間違えぬこと。
  ピクセルという用語に与える意味は、OpenGL のほうが一般の CG の
  教科書より優れている気がする。
  <OpenGL uses *color buffer* to refer to these bits and the *frame buffer*
  (or framebuffer) is the collection of all the buffers, including the
  color buffer(s) and the depth buffer.> (p. 143)

* we need the ability to read and write rectangular arrays of pixels. (p. 143)
* Figure 7.1 の n x m frame buffer shown with k parallel bit planes を憶える。
* we shall use the term pixel to denote a group of bits. (p.144)

* ピクセルを直にいじる操作のことを **bit block transfer** という。
  これを縮めて **bitblt** というのだ。

* Figure 7.2. Vertices パイプラインと Pixels パイプラインがラスタライズステージで合流する。

  ::

    Vertices --> Geometric Processing --> Rasterization --> Display
                                            |
      Pixels --> Pixel Operations ----------|

* We have to warry about the differences in how pixels are formatted in
  the application program. (p. 145)
* a pixel might represent an RGB color, an RGBA color, a luminance value,
  or a depth value. (p. 145)

Bitmaps
-------
Displaying a Bitmap
~~~~~~~~~~~~~~~~~~~
* glBitmap 関数の説明。ラスタポジションの状態を変更することに言及している。

Mixing Bitmaps and Geometry
~~~~~~~~~~~~~~~~~~~~~~~~~~~
* gluOrtho2D と glRasterPos2i のコンビ技について説明している。
  二次元的に描画するときの基本的な考え方。
* One solution to this problem is to use two sets of viewing conditions,
  one for the geometry and the other for the bitmaps. (p. 148)

Colors and Masks
~~~~~~~~~~~~~~~~
ビットマップをマスクという観点で説明する。
glColor と glClearColor のチェッカーボードの例を挙げている。

* ここは理解しにくい：
  <OpenGL stores both a present drawing color and a present raster color>
  (p. 149)
  <The checkerboard is drawn in red because the raster color is the color
  that was in effect the last time that the function glRasterPos2i() was
  executed.> (p. 149)

Drawing Modes
-------------
* Figure 7.6 の模式を憶えること。Logic Op の回路。
* glLogicOp(op) を利用するには、glEnable で有効にする必要がある。
  ::
    
    glEnable(GL_COLOR_LOGIC_OP);

* If we use XOR, wesimply draw the same object a second time at the same
  place that we drew it the first time.  The second draw undoes the first.
  (p. 151)

* Applications of this simple idea include moving a cursor around the
  screen, rubberbanding lines and rectangles. (p.152)

Reading and Writing Pixels
--------------------------
* Figure 7.7 Pixel pipeline を意識する。
  ::

    Processor                   Pixel        Pixel       Pixel       Frame
    Memory    --> Unpacking --> Transfer --> Mapping --> Testing --> Buffer
       |                                                                |
       |<--------------------------- Packing <--------------------------|

Writing Pixels
~~~~~~~~~~~~~~
* glDrawPixels(w, h, format, type, array)

  :w, h: ピクセル矩形のサイズ
  :format: GL_UNSIGNED_BYTE とか
  :type: GL_UNSIGNED_BYTE_3_3_2 とか
  :array: 描画したいデータ

Reading Pixels
~~~~~~~~~~~~~~
* glReadPixels(x, y, w, h, format, type, array)

  :x, y: フレームバッファのどの位置からデータを読み込むのかを指示

* dithering について言及しているが、よくわからなかった。

Copying Pixels
~~~~~~~~~~~~~~
* glCopyPixels はフレームバッファ内でピクセルをコピーするというのがポイント。
  glCopyPixels はデータをシステムメモリに運ばないので、
  glReadPixels と glDrawPixels を組み合わせてコピーをするよりも、パフォーマンスが優れている。

Selecting Buffers
-----------------
* シングルバッファモードで読み書きが起こるのは front color buffer で、
  ダブルバッファモードでは back color buffer で起こる。
* OpenGL は実装によってはさらなる color buffer をサポートしている。
  どのバッファを用いるのかを選択するのには、glReadBuffer と glDrawBuffer 
  関数を利用する。

Pixel Store Modes
-----------------
* どのようにしてプロセッサーメモリにバイトが配列されているのかを
  OpenGL に教えてやる必要があるとする。この場合、glPixelStore を利用する。
* バイトオーダーの話題か。

Displaying a PPM Image
----------------------
いまさら PPM を扱うことはあるまい。

Using Luminace
--------------
* **Luminance** とは <images that consist only of shades of gray> (p. 163) のこと。
  モノクロ画像だ。

* RGB 値から luminance の値を計算する式は次で与えられるらしい。
  ::

    L = .30R + .59G + .11B

  明らかに G 成分が支配的。

Pixel Mapping
-------------
* カラーバッファの RGB ピクセルの値を補正することができる。
* glPixelTransfer(name, value) - pixel transfer mode を指定する。
* glPixelMap(map, size, array) - 補正テーブルをセットする。

  :map: GL_PIXEL_MAP_I_TO_R など。
  :size: 2 のベキ乗でなければならない。

Pixel Zoom
----------
* ピクセルブロックのスケーリングには glPixelZoom を用いる。

  * glPixelZoom(sx, sy)

    :sx, sy: スケール係数。負数も許す。負数の場合はピクセルの並び順が逆転する。

* そしていまいち使い方がわからない gluScaleImage 関数。
  イメージをトリムするのかストレッチするのかがわからない。

  * gluScaleImage(format, win, hin, typein, imagein, wout, hout, typeout, imageout)

Image Processing in OpenGL
--------------------------
* ヒストグラムやフィルタリング。高度な内容らしい。
* Convolution という単語がフィルタに関連する理由が、次の文のおかげでわかった。
  <Convolution or filtering that replaces a pixel value by a linear function
  of the surrounding pixel values.> (p. 167)
* Imaging Pipeline
  ::

    Pixels   Color                      Color      Color      Color                 Pixels
        -->  Lookup --> Convolution --> Lookup --> Matrix --> Lookup --> Histogram -->
             Table                      Table                 Table

----

:doc:`angel05-note3` へ。
