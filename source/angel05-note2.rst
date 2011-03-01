======================================================================
OpenGL: A Primer Second Edition 読書ノート 2/3
======================================================================

:doc:`angel05-note1` からの続き。

:著者: Edward Angel
:出版社: Peason Education, Inc.
:ISBN: 0-321-26982-9

.. contents:: ノート目次

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

Texture Mapping
===============
* Texture mapping combines pixels with geometric objects (p. 169)

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

* Two dimensional texture mapping is the most familiar case. (p. 171)
* 二次元的なイメージは、二次元多様体にマップするのが自然だろう。
  ::

    glEnable(GL_TEXTURE_2D);
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 64, 64, 0, GL_RGB, GL_UNSIGNED_BYTE, myimage);

* イメージの縦横サイズは、2 のベキ乗の形をしていなければならない。
  註によると、新しいグラフィックカードは任意の縦横サイズを許しているようだ。

* It may take a significant amount of time to move a texture image from
  processor memory to texture memory. (p. 173)

Texture Coordinates
-------------------
* Just as with vertices, texture coordinates are represented internally
  in four dimensions that conventionally use the letters (s, t, r, q) to
  denote the coordinates. (p. 173)

* テクスチャーマッピングを試すためのコツを以下のように述べている。
  <Checkerboards are especially useful for demonstrating the various 
  options and seeing how OpenGL implements texture mapping.> (p. 174)

* We see that OpenGL renders the quadrilateral as two triangles (p. 174)

* 頂点座標と同様に、テクスチャー座標を行列を用いて変換することができる。
  ::

    glMatrixMode(GL_TEXTURE);

Texture Parameters
------------------
テクスチャー座標やテクスチャー画像以外にも、
テクスチャーマッピングが要求するパラメータがいくつもある。

* glTexParameter(target, name, value)

  :target: GL_TEXTURE_2D
  :name: GL_TEXTURE_xxx

* The required parameters determine what happens when values of 
  s, t, r, or q go outside the range (0, 1) and how sampling and
  filtering are applied. (p. 176)

* GL_TEXTURE_WRAP_(S|T), GL_(REPEAT|CLAMP) を憶える。

* magnification と minification の考え方を習得する。
  一つのテクスチャー画素が複数のピクセルに写像する方が magnification

* GL_TEXTURE_(MAG|MIN)_FILTER を GL_NEAREST にすると速い。

* 透視図法でシーンを描いている場合、テクスチャーが歪む場合がよくある。
  そういう場合は glHint を呼ぶ。
  ::

    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST);
  
  glHint は他のレンダリングオプションにも利用できる。調べる。

A Rotating Cube with Texture
----------------------------
省略。

Applying Textures to Surfaces
-----------------------------
ポリゴンの地の色とテクスチャーマッピングをミックスする方法について。

* glTexEnv(target, param, value)

  :target: GL_TEXTURE_ENV
  :param: GL_TEXTURE_ENV_MODE とか GL_TEX_ENV_COLOR とか。
  :value: GL_(MODULATE|REPLACE|BLEND|DECAL) とか色とか。

* The default mode of operation is called modulation. 
  Here the texture color multiplies the color computed for each face.
  (p. 181)
  ::

    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE);

Borders and Sizing
------------------
* テクスチャーマッピングは、テクスチャーイメージ境界付近の処理が難しい。

* One difficulty that arises when we use linear filtering is what happens
  at the edges of the texture where we lack one or more texels to use
  in the filtering. (p. 181)

* テクスチャーに枠を付加するという仕様がある。
  もし枠を指示するのなら、テクスチャーの縦横サイズを 2 のベキ乗 + 2 の形にする。

* 枠の色を別途指示することができる。
  ::
    
    glTexParameter3fv(GL_TEXTURE_2D, GL_TEXTURE_BORDER_COLOR, color);

* フレームバッファ内のイメージからテクスチャーマップを得ることができる。
  ただし「出力先」はテクスチャーメモリー。
  ::
    
    glCopyTexImage2D(target, level, iformat, x, y, w, h, border);

* 既に存在するテクスチャーから、その部分のコピーを（バイナリの形で）得ることもできる。
  ::
    
    glTexSubImage2D(target, level, xoffset, yoffset, w, h, format, type, texels)

* 応用例がちょっと思いつかないが、テクスチャーメモリ内でコピーすることもできる。
  ::
    
    glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, w, h)

Mipmaps
-------
* Mipmap とはテクスチャーマッピングの LOD の技法。
  広い領域にマップするデータと、狭い領域にマップするデータを使い分ける。

* What we would prefer is to have a texture value that is the average of
  the texels values over a large area of the texture. (p. 183)

* glTexImage2D の第二引数 (level) に応じて、イメージを変える。
  本文の例では、レベルが低いほど詳細なイメージを指示している。
  ::
    
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST_MIPMAP_NEAREST);

  This is the lowest quality option. (p. 183)

* ミップマップセットを生成し、テクスチャーメモリに格納してくれる GLU の関数がある。
  ::
    
    gluBuild2DMipmaps(target, iformat, w, h, format, type, texels);

Automatic Texture Coorinate Generation
--------------------------------------
* 頂点に対してテクスチャー座標を決める作業は一般的には難しい。
  しかし、GLU 二次曲面はテクスチャー座標を生成する関数が提供されている。

  * gluQuadricTexture(obj, mode)

    :mode: GL_(TRUE|FALSE)

* <OpenGL allows us to generate texture coordinates that are measured as
  distances from a plane in either object space or eye space.> (p. 186)
  だそうだが、平面からの距離で決まる座標というのが解りにくい。

* The value ax + by + cz + dw is proportional to the distance from
  (x, y, z, w) to the plane determined by (a, b, c, d). (p. 186)

* テクスチャー座標自動生成には、例えば (s, t) の場合は以下の呼び出しが必要。
  ::

    glEnable(GL_TEXTURE_GEN_S);
    glEnable(GL_TEXTURE_GEN_T);

* glTexGen(texcoord, param, value)

  :texcoord: GL_[STRQ]
  :param: GL_TEXTURE_GENMODE か GL_(OBJECT|EYE)_LINEAR
  :value: GL_(OBJECT|EYE)_LINEAR か平面の係数配列

* 視点座標でテクスチャーを貼る：
  <If we use the GL_EYE_LINEAR mode, texture coordinates are based on
  the vertex positions in eye space so that when we move the object,
  the texture coordinates assigned to vertices change.> (p. 188)

Texture Objects
---------------
テクスチャーもまた OpenGL の「状態」の一部だ。
glTexImage を実行するときに、システムメモリからテクスチャーメモリへ
移動する。テクスチャーを何種類も利用する場合は、移動にコストをつけたくない。
そこで texture object というものを提供している。

* If there is not sufficient memory for all the textures that we need,
  we can prioritize the texture objects to minimize the amount of
  data movement from the processor to texture memory. (p. 188)

* glGenTextures(n, name) で n 個の texture objects を新規作成する。
* glIsTexture(name) で name が texture object か否かをテストする。

* glBindTexture(), that both switches between texture objects and
  forms new texture objects. (p. 189)

* glBindTexture(target, name)

  :target: GL_TEXTURE_[123]D
  :name: texture object の ID

* glBindTexture の振る舞いは、次の三つのどれか。

  * case 1: If we call glBindTexture() with name and name has not been
    used before, the subsequent calls to the various texture functions
    define the texture object with the id name.
  * case 2: If name already exists from a previous call to glBindTexture(),
    then that texture object becomes the present texture and is applied
    to surfaces until the next call to glBindTexture().
  * case 3: If glBindTexture() is called with name set to 0, then the
    normal texture calls apply and the present texture that is part of
    the OpenGL state and the current values of the texture parameters
    both apply.

* テクスチャーオブジェクトを破棄したい場合は glDeleteTextures を呼ぶ。

  * glDeleteTextures(n, namearray)

Texture Maps for Image Manipulation
-----------------------------------
テクスチャーパラメータのセットだけだが、サンプルコードのラストが参考になる。

----

:doc:`angel05-note3` へ。
