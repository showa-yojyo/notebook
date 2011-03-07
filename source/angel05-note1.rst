======================================================================
OpenGL: A Primer Second Edition 読書ノート 1/3
======================================================================

:著者: Edward Angel
:出版社: Peason Education, Inc.
:ISBN: 0-321-26982-9

.. contents:: ノート目次

Preface
=======
* 赤本と青本

  * the OpenGL Progamning Guide, Fourth Edition (Addison-Wesley), the "red book"
  * the OpenGL 1.4 Reference Manual, Fourth Edition (Addison-Wesley), the "blue book"

* OpenGL ARB については後で説明あり。
* it is much easier to get started with OpenGL and use it to master the basic concepts.
  For those of us who work with scientific applications and in a cross platform environment,
  OpenGL is the API of choice. (p. xvi)

Introduction
============
OpenGL is an interactive computer graphics system that allows programmers to write
programs that access graphics hardware.  OpenGL has two important benefits for
application programmers.  It is close enough to the hardware so that programs written
with OpenGL run effectively, and OpenGL is easy to learn and use. (p. 1)

The OpenGL API
--------------
* OpenGL came from an interface called GL, short for Graphics Library, originally
  developed for Silicon Graphics Inc. (SGI) hardware. (p. 1)
* OpenGL にはアプリを組むためにある 200 を越える関数がある。
* この本ではレンダリングを以下のように説明している。
  <taking the specification of geometric objects and their properties and
  forming a picture of them with a virtual camera and lights.>(p. 2)

* GLUT について、T が Toolkit の頭文字であることを記憶する。
* Rather than write platform-dependent code, we shall use a simple toolkit,
  the OpenGL Utility Toolkit (GLUT)... (p.1)

Three Views of OpenGL
---------------------
The OpenGL State Machine
~~~~~~~~~~~~~~~~~~~~~~~~
* OpenGL を State Machine として考えることができる。

The OpenGL Pipeline
~~~~~~~~~~~~~~~~~~~
* OpenGL はパイプラインモデルをベースにしている。
  入力を Vertices とし、出力を Pixels となるようなパイプラインだ。

What's in OpenGL
----------------
* OpenGL 関数のカテゴライズ

  1. Primitve functions - イメージを生み出す要素を定義する関数
     geometric と image の二通りがある。
  2. Attribute functions - プリミティヴの見てくれをコントロールする関数
     色、線の種類、材質、光源、テクスチャー等。
  3. Viewing functions - カメラの性質を定義する関数
  4. Windowing functions - 
     こういう関数は GLUT に入っている。
  5. Control functions - OpenGL の色々な機能を有効にする関数
  
  このうち、2. から 5. までが state-changing な関数だ。

OpenGL Versions and Extensions
------------------------------
* OpenGL は OpenGL Architectural Review Board (ARB) がコントロールする。
* ARB は Silicon Graphics, IBM, NVIDIA といったメーカーから来たメンバーを持つ。
* OpenGL extensions は後回しでいいや。

Two-Dimensional Programming in OpenGL
=====================================
A Simple Program
----------------
* GLX for X Windows, wgl for Windows, and agl for the Macintosh (p. 11)

GLUT
----
* Figure 2.2 では GLUT 層が GLX or WGL or AGL 層を完全にラップしている。
  GLUT を利用することで、プラットフォーム間の垣根を越える。
* Depending on the platform, GLUT uses glX, wgl, or agl. (p. 13)

Event Loops and Callback Functions
----------------------------------
* glutInit は他のいかなる GLUT と OpenGL 関数呼び出しの前に呼ぶこと
* glutCreateWindow によるウィンドウのサイズは 300 x 300 pixels
* イベントキューという用語を憶える。
* コールバック関数。どうしてもグローバル変数の世話にならざるを得ない。
* glutMainLoop の呼び出し行以降の行は、実行されない。

Drawing a Rectangle
-------------------
* The fundamental entity for specifying geometric objects is the vertex,
  a location in space.  Simple geometric objects such as lines and polygons
  can be specified through a collection of vertices. (p. 15)
* OpenGL puts the rendered image in an area of memory called a **color buffer**
  that usually resides on the graphics card.  Color buffers are one of a 
  number of types of buffers that make up the **frame buffer**. (p. 16)

Changing the GLUT Defaults
--------------------------
* glutInitDisplayMode(mode)

  :mode: GLUT_(RGB|INDEX|SINGLE|DOUBLE), etc.

* glutInitWindowSize(width, height)
* glutInitWindowPosition(x, y)

Color in OpenGL
---------------
* In RGBA mode, we use a fourth color component, A or alpha, which is
  an opacity. (p. 18)
* Opacity というのは日本語にないような。透明度の裏の概念というか。

Color and State
~~~~~~~~~~~~~~~
* <colors are not attached to objects but rather to the internal state
  of OpenGL.> (p. 20) OpenGL の世界では色もまた状態なのだ。
* OpenGL actually has only one internal form for the present color,
  which is in RGBA form, usually a floating point number for each color
  component. (p. 20)
* どんな glColor 関数を利用しようが、内部的なデータの形式は一つしかない。
  glColor3i のほうが glColor4fv より軽いなどということはないようだ。

Coorinate System Differences Between GLUT and OpenGL
----------------------------------------------------
* ウィンドウの Y 軸の正の方向について、OpenGL の座標系と GLUT の座標系では逆。

Two-Dimensional Viewing
-----------------------
* gluOrtho2D(left, right, bottom, top)

* gluOrtho2D によって定義する矩形をクリッピングウィンドウと呼ぶ。

The Viewport
------------
* glViewport(x, y, width, height)

  ウィンドウのどの部分を canvas とするのかを指定する。
  通常はウィンドウ全域を glViewport に渡すが、二次元的にイメージを描く場合などは、
  本当にウィンドウの特定部分を指定することが多い。

Coordinate Systems and Transformations
--------------------------------------
* The function gluOrtho2D is used to specify a projection matrix for two-
  dimensional applications. (p. 23)
* まず間違いなく以下の手順で利用する。
  ::

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(left, right, bottom, top);

* <In OpenGL, there are three basic types of geometric primitives: 
  points, line segments, and polygons.>(p. 26) たった三種類しかないのだ。

Primitives and Attributes
-------------------------
* <in fact, OpenGL regards attributes as part of its state.>(p. 26)
  アトリビュートも他の何かと同様に「状態」ということ。

Points
~~~~~~
* glPointSize(size)

  :size: サイズはスクリーンピクセル単位

* glPointSize は glBegin - glEnd の間に入れない。

Lines
~~~~~
* 線分は三種類のタイプしかない。

  * GL_LINES
  * GL_LINE_STRIP
  * GL_LINE_LOOP

* 線分の属性は 
  
  1. 色
  2. 線幅
  3. パターン

* glLineWidth(width)

  :width: 幅はピクセル単位で与える。

* glLineStipple(factor, pattern)

  :factor: パターンの繰り返し回数。1 から 256 の間の値。
  :pattern: line stipple のビットパターン (16 bit) の与え方をおさえておくこと。

Enabling OpenGL Features
~~~~~~~~~~~~~~~~~~~~~~~~
* OpenGL の機能の中には、明示的にそれを有効にしなければ利用できないものがある。
* glEnable(feature) で機能 feature を ON にする。
  ::

    glEnable(GL_LINE_STIPPLE);

* glDisable(feature) で機能 feature を OFF にする。

Filled Primitives
~~~~~~~~~~~~~~~~~
* ポリゴン。六種類のタイプがある。
  このノートには敢えて書かないが、説明の英文は丸暗記しておきたい。

  * GL_POLYGON
  * GL_TRIANGLES
  * GL_TRIANGLE_STRIP
  * GL_TRIANGLE_FAN
  * GL_QUADS
  * GL_QUAD_STRIP

* STRIP 系の図形描画は、関数呼び出しの回数が少なく済むという利点がある。
  <many CAD applications generate triangles or quadrilaterals with shared
  edges.  Strip primitives allow us to define these primitives with far
  fewer OpenGL function calls than if we had to treat each as a separate
  polygon.>(p. 30)

Rectangles
~~~~~~~~~~
* 長方形を描くのなら、glRect で済む場合がある。
  glVertex を四回書かなくて済むし、おすすめ。

Polygon Stipple
~~~~~~~~~~~~~~~
* polygon stipple の模様は、プリミティブを回転しても回転しない。
* glEnable(GL_POLYGON_STIPPLE) で有効にする。
* glPolygonStipple(mask)

  :mask: 32 x 32 ビットのパターン。

Polygon Types
-------------
* 塗りつぶしポリゴンを描くときには、その形状に気をつける点がある。
  <**simple polygons** -- polygons whose edges do not cross -- two different
  OpenGL implementations may render them differently.> (p. 31)
* Convex polygons are much easier to render. (p. 32)
* 面には表と裏がある。それらを描画し分ける手段がある。

  * glPolygonMode(face, mode) - 面をどう描くか

    :face: GL_(FRONT|BACK|FRONT_AND_BACK)
    :mode: GL_(POINT|LINE|FILL)

  * glCullFace(mode) - 描くか否か

    :mode: GL_(FRONT|BACK|FRONT_AND_BACK)

  * glFrontFace(mode) - 面の表裏をどう定義するか

    :mode: GL_(CCW|CW)

* By default, a front face is one in which the order of the vertices is
  counter-clockwise when we view the polygon.  A back face is one in which
  the vertices are specified in a clockwise order.  These definitions
  make sense for convex polygons. (p. 32)

  In OpenGL, the edges of a polygon are part of the inside of the polygon (p. 33)

* 塗りつぶしと線の描画を重ねあわすことについて、
  場合によってはポリゴンオフセットをかけないと美しくないかも。

* glPolygonOffset(factor, units)

  :factor, units: 謎のパラメータ。

  glPolygonOffset 関数は次のようにして利用する。
  ::
  
    glPolygonOffset(1.0, 1.0);
    glEnable(GL_POLYGON_OFFSET_LINE);

Color Interpolation
-------------------
* The default is to use smooth shading where OpenGL will interpolate the colors
  at the vertices to obtain the color of intermediate pixels. (p. 34)
* OpenGL がポリゴンに対して何らかの補間を行うときは、大抵は bilinear interpolation だ。
* glShadeModel(mode)

  :mode: GL_(SMOOTH|FLAT)

Tessellation and Edge Flags
~~~~~~~~~~~~~~~~~~~~~~~~~~~
glEdgeFlag と tessellation, subdivision の話が続く。

Tessellation and Subdivision
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
subdivision は図形にねじれを加えるような画像効果を実現する手段として利用できるようだ。

Text
----
* フォントには bitmap と stroke の二種類がある。
* bitmap は高速に描画できるが、スケーリング等の変換がかけられない。
  stroke はその逆の長所短所がある。
* フォントはシステム依存のものなので、GLUT がその辺をカバーしてくれている。
* glutBitmapCharacter(font, character)

  :font: GLUT_BITMAP_TIMES_ROMAN_10 のようなシンボルを指定する。
  :character: 一文字を指定する。

* Raster position は左下原点
* The current raster position is offset automatically so that the next
  character will not be rendered on top of the previous one. (p. 44)

* glRasterPos(xyzw) - ラスター位置を設定する。
* glutBitmapWidth(font, character) - 文字幅をピクセル値で返す。
* glutStrokeCharacter(font, character) - ストロークフォントにて文字を描画する。
* glutStrokeWidth(font, character) - 文字幅をビット単位で返す。

* ストローク系のフォントサイズは単位がよくわからないので注意。
  StrokeWidth の 1 が世界座標系の長さ単位の 100 程度とのこと。

Querues and Errors
------------------
* glGet(Boolean|Integer|Float|Double|Pointer) 系の話はノート省略。
* glGetError と gluErrorString はデバッグのために憶えておく。
  これらを組み合わせてエラーを知る。
* GLUT の状態は glutGet で得る。

Saving the State
----------------
* OpenGL はステートマシーンなので、プログラムを書いていると、
  各種状態をちょっと前の時点のものに戻したいくなる状況になることがよくある。

* 行列の（成分という意味での）状態に関しては、glPushMatrix, glPopMatrix が利用できる。
  各行列モードに対して、行列スタックが存在する。
  one pop for each one push ルールを肝に銘じること。

* 各種属性に関しては glPushAttrib, glPopAttrib を利用できる。
  全属性状態を一気に push することも可能だが、
  通常は必要なものだけを push するのだろう。
  引数がビットマスクなので、適切な値を指示することに慣れる必要がある。

Interaction and Animation
=========================
The Reshape Callback
--------------------
* Within the loop, the program responds to discrete events
  involving the keyboard and the mouse through callback functions that
  the application programer writes. (p. 49)
* This action generates a window event that is handled by the reshape
  callback. (p. 49)

* glutReshapeFunc(f)
  
  :f: void (*)(int width, int height) 型の関数のアドレス。
      <A display callback is invoked automatically after executing f().> (p. 49)

* The reshape callback is invoked when a window is first created (p. 49)
* Reshape callback でプログラマーが書くことは、ビューポートのリセットと
  クリッピングウィンドウのリセットの二点だ。
* gluOrtho2D の bottom, top の値をウィンドウのサイズに依存するように決める。
  幅と高さの短い方を分母にしたアスペクト比。

The Idle Callback
-----------------
* The idle callback identifies a function, which should be executed 
  whenever there are no otther events to be handled, that is, whenever
  the event queue is empty. (p. 51)

* glutIdleFunc(f)

  :f: void (*)() 型の関数のアドレスを渡す。

* Use of glutPostRedisplay() ensures the window gets drawn at most once
  each time that GLUT goes through the event loop.  In general, it is a 
  good idea to never call the display callback directly but rather to use
  the glutPostRedisplay() whenever the display needs to be redrawn. (p. 52)

* glutPostRedisplay() - 現在のコールバックがリターンした後にディスプレイコールバックが
  実行されるようにお願いする関数。

A Rotating Square
-----------------
ここでは三角関数を利用して円に内接する正方形を回転するアニメーションを実装している。

Double Buffering
----------------
* This refresh process is not controllable from the user program (p. 54)
* ダブルバッファは二つの color buffers を使うというのがミソ。それぞれ
  **front buffer** と **back buffer** と呼ぶ。

  :front buffer: ディスプレイハードウェアによってディスプレイされるバッファ
  :back buffer: アプリケーションが書き込む先のバッファ

* glutSwapBuffers() - front buffer と back buffer を入れ替える。
* 書くのが最後になったが、ダブルバッファを有効にするには glutInitDisplayMode で
  指定する。
  ::

    glutInitDisplayMode(GLUT_DOUBLE | ...);

Using the Keyboard
------------------
* GLUT ignores releasing of the key (p. 54)
* glutKeyboardFunc(f)

  :f: void (*)(key, x, y) 型関数アドレス。スクリーン座標が存在するのが面白い。

* GLUT の関数でマウス位置を扱うものは、すべてウィンドウ左上が原点。
* Esc キーは 8 進数で 027 となる。16 進数では 0x1B となる。

Special Keys
~~~~~~~~~~~~
* glutSpecialFunc(f) - F1 キーとか↑キーとかのプレスイベントをハンドルする。

  :f: glutKeyboardFunc のと同じ。

* glutGetModifiers() - マウスやキーを押されたときに、以下のキーの状態を見る。

  :return: GLUT_ACTIVE_(SHIFT|CTRL|ALT)

Using the Mouse Callback
------------------------
* glutMouseCallback(f)

  :f: void (*)(button, state, x, y)

    :button: GLUT_(LEFT|MIDDLE|RIGHT)_BUTTON
    :state: GLUT_(UP|DOWN)

* x, y は GLUT の座標系での値なので、<The most important is the necessity
  of inverting the y value returned by the mouse callback.> (p. 58)
* ディスプレイコールバックが必要のないプログラムを書く場合もあるが、
  <As a practical matter, GLUT insists that every program have a display
  callback.> (p. 59) だそうだ。そういう場合は空の実装を与える。
* しかし普通はそんなことはしない。<A more general strategy is to 
  place drawing functions in the display callback and use the other 
  callbacks for state changes.>(p. 59)
  その上で glutPostRedisplay をすればよい。

Mouse Motion
------------
* マウスモーションには glutMotionFunc と glutPassiveMotionFunc の二種類のコールバックが利用できる。
* Passive とは、マウスボタンが押されていない状態でマウスが動いているイベントのことだ。
* glutMotionFunc(f), glutPassiveMotionFunc(f)

  :f: void (*)(x, y) 型関数のアドレス

* glutEntryFunc(f): マウスキャプチャーに使うのか？

  :f: void (*)(state) 型関数のアドレス
  
    :state: GLUT_(ENTERED|LEFT)

The NULL Callback
-----------------
glutXXXFunc にヌルを渡すと、コールバックを削除できる。

Subwindows and Multiple Windows
-------------------------------
* コンテキストの概念は重要。
* Each window can have its own properties, referred to as its context. (p. 64)

Display Lists
-------------
* ディスプレイリストをファイルに例えて説明している。
  <Display lists can be thought of as a type of graphics file in which we can
  place OpenGL rendering and state update commands.  We open a display list,
  give it a name, place commands in it, and close it.> (p. 67)
* ディスプレイリストを定義するときは、各種状態の push/pop が重要だ。
  <Note that we push and pop the current attributes, which include the present
  color.  We must do this action to prevent the state change due to setting
  a new color from affecting anything that we do subsequently.  Often we can
  prevent unforeseen side effects of state changes by starting a display
  list by pushing the matrices and the state at the beginning of the display
  last popping them at the end.> (p. 68)
  後続のディスプレイリストに余計な状態を残さぬように、リストを定義する。

* glNewList(name, mode): ディスプレイリストの定義を開始する。

  :name: ディスプレイリストの名前。
         通常、次節で紹介されている glGenLists の戻り値を指定する。
  :mode: GL_COMPILE か GL_COMPILE_AND_EXECUTE

* glEndList(): ディスプレイリストの定義を終了する。
* glCallList(name): ディスプレイリストを実行する。
* glGet 等の「状態を返すだけの関数」をディスプレイリスト定義中に呼ぶことはできない。
* ディスプレイリストを階層的に glCallList することができる。
* ディスプレイリストは、一度作成したら変更できない。
* glDeleteLists(first, number): ディスプレイリストを削除する。

  名前が first のリストから、number 個目までのリストを削除する。

Multiple Display Lists
~~~~~~~~~~~~~~~~~~~~~~
* glListBase(offset) - glCallList の実引数にゲタをはかせる
* glCallLists(num, type, list)

  :num: list の個数
  :type: list の型
  :list: ディスプレイリストの名前（つまり整数値）の配列

* glGenLists(n) - ディスプレイリスト新規作成のための有効な名前を n 個生成する。

Display Lists and Text
~~~~~~~~~~~~~~~~~~~~~~
* To generate a character string on the display, we do one function call per character.
  (p. 69)
* 全 ASCII 文字についてディスプレイリストをコンパイルするやり方を紹介している。
  ディスプレイリストの ID を文字コードと同じにして……という方法だ。
  日本語に応用できるとは思えない。

Display Lists and Objects
~~~~~~~~~~~~~~~~~~~~~~~~~
* <display lists can give the user a way of building more object-oriented program
  than in immediate mode.> (p.70) とあり、人間の顔を描くと思われるディスプレイリストを
  定義するコードを記載している。glNewList と glEndList の間に、
  顔のパーツを定義するディスプレイリストを glCallList するという例だ。

Picking and Selection Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~
* 本書ではピックの定義を以下のように与えている。
  <**Picking** is the operation of locating an object on the screen.> (p.71)
* ピックのためには、描画要素にある種のタグ付けを行う必要がある。
  <We could create some sort of tag system that would give labels to
  parts of our program.> (p. 71)
* **selection mode** で描画を行うと、オブジェクトは color buffer にレンダーされない。
* ピック処理はコードを書くのが面倒。関係する関数が次に挙げるように、妙に多い。

  * glRenderMode(mode) - render mode の選択

    :mode: GL_(RENDER|SELECTION|FEEDBACK)

  * glSelectBuffer(n, buffer) - 選択データを置く配列を決める
  * glInitNames() - name stack の初期化
  * glPushName(name) - name stack に name を積む
  * glPopName() - name stack から name をひとつ捨てる
  * glLoadName(name) - name stack の一番上の要素を name で置き換える

* glRenderMode() returns the number of hits that have been processed. (p. 73)
* gluPickMatrix(), that should be applied before gluOrtho2D() when we
  are in selection mode. (p. 73)
* If we had a hierarchical object in which multiple parts of the object could
  all be located near the cursor, we could use glPushName() so that we could
  have multiple names on the stack for a given hit.  For an object with multiple
  parts, all the parts that were close to the cursor would have their names
  placed in the same stack. (p. 75)
* ヒットレコードのバイトレイアウトについて、細かく説明している。
  <we find three types of information, all stored as integers.  First, there
  is the number of names on the name stack when there was a hit.  It is followed
  by two integers that give scaled minimum and maximum depths for the hit primitive.
  These three integers are followed by entries in the name stack.> (p. 75)

Basic Three-Dimensional Programming
===================================
Cameras and Objects
-------------------
* そもそも投影とは何か。次のように説明している。
  <The process of combining the specifications of objects and camera is
  called **projection**.> (p.77)

* カメラの指定方法は、オブジェクトのそれほど直感的ではない。
  カメラ自身の位置に加え、どちらを向いているのかという情報と、
  その向きに対してどれくらい回転がかかっているのかという情報が必要。

* 直交投影 (orthographic projection) は最も単純な種類の投影だ。

* viewing volume, front/back (or near/far) clipping plane の概念をおさえること。

* ピラミッドの角をカットしたような形状を frustum という。

Orthographic Projections in OpenGL
----------------------------------
* The viewing frustum becomes a right parallelpiped -- a rectangular box.
  (p. 80)

* glOrtho(left, right, bottom, top, near, far) - 視点座標系で引数を与える。

  * left < right かつ bottom < top かつ near < far である必要がある。

* Note that gluOrtho2D() is derived from gluOrtho() by setting near
  and far to -1 and +1 respectively. (p.81)

Viewing a Cube
--------------
* GLUT には座標原点に指定サイズのキューブを描画する便利な関数がある。

  * glutWireCube(size) - 各辺の長さが size のワイヤーキューブを描く
  * glutSolidCube(size) - 各辺の長さが size のソリッドキューブを描く

Locating the Camera
-------------------
キューブを別の角度から見たいとする。このときカメラを動かすか、キューブを動かせば
よいのだが、カメラを動かすことを先に知る。

  We can decide on a position for the camera (called the **eye point**)
  and decide where to aim it to by specifying a point at which it 
  is pointing (the **at point**).
  
  We need a third input, the direction we want to consider as up
  in the image (the **up vector**). (p. 83)

  A simple choice of the up vector is often (0, 1, 0) or
  the y direction in world coortinates. (p. 83)

* gluLookAt((eye), (at), (up))

  :eye: 視点の位置 (x, y, z)
  :at: 注視する点の位置 (x, y, z)
  :up: イメージの上方を定義するベクトル (x, y, z)

* カメラの設定コードはほぼ必ず以下のようになる。
  ::

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(...);

Building Objects
----------------
* the vertices in a counterclockwise manner when each face is
  viewed from the outside (p. 86)

Using Arrays
~~~~~~~~~~~~~
これまでのやり方だと、頂点を指定するのは大量の関数呼び出しを伴うが、
頂点配列を用いることで、関数呼び出しの回数を減らすことができる。

Vertex Arrays
~~~~~~~~~~~~~
* OpenGL provides support for six types of arrays: vertex, color,
  color index, normal, texture coordinate, and edge flag. (p. 88)

* glEnableClientState(arraytype), glDisableClientState(arraytype)
  
  :arraytype: GL_(VERTEX|COLOR|INDEX|NORMAL|TEXTURE_COORD|EDGE_FLAG)_ARRAY

* glVertexPointer(dim, type, stride, array), glColorPointer(dim, type, stride, array)

  :dim: データの次元数 [234]
  :type: GL_(SHORT|INT|FLOAT|DOUBLE)
  :stride: array の中にデータがどのように連続して詰まっているかを示す数

* glDrawElements(mode, n, type, indices)

  :mode: 例えば GL_POLYGON とか
  :n: インデックスの個数
  :type: indices の型。例えば GL_UNSIGNED_BYTE とか。

* コード例
  ::

    GLfloat vertices[][3] = {...};
    GLfloat colors[][3] = {...};
    GLubyte cubeIndices[] = {
        0, 3, 2, 1,
        2, 3, 7, 6,
        ...
        };

  とすると、とりあえずは以下のように面を描画できる。
  ::

    glEnableClientState(GL_COLOR_ARRAY);
    glEnableClientState(GL_VERTEX_ARRAY);
    glVertexPointer(3, GL_FLOAT, 0, vertices);
    glColorPointer(3, GL_FLOAT, 0, colors);
    for(i = 0; i < 6; i++){
        glDrawElements(GL_POLYGON, 4, GL_UNSIGNED_BYTE, cubeIndices);
    }

  ループはさらにシンプルにできる。
  ::

    glDrawElements(GL_QUADS, 24, GL_UNSIGNED_BYTE, cubeIndices);

Hidden-Surface Removal
----------------------
* 観察者からは角度的に見えない面を描画しない手法を指す。
* 例えば
  ::

    glEnable(GL_CULL_FACE);
    glCullFace(GL_BACK);

  が考えられるが、この方法は先述のように convex objects に対してのみ働く。

* オブジェクトの奥行きを管理するバッファを z-buffer or depth buffer という。
* In most programs, the depth buffer should be cleared whenever
  the color buffer is cleared. (p. 91)
  ::
    
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH);
    ...
    glEnable(GL_DEPTH_TEST);

GLU and GLUT Objects
--------------------
* よく利用される幾何形状の描画は、GLU や GLUT が提供している。
* 円柱だとか球だとかもあるが、基本的には多角形近似である。

GLUT Quadrics
~~~~~~~~~~~~~
* GLUT provides three types of quadrics: spheres, cylinders, and disks.
  (p. 92)

* gluNewQuadric() - 二次曲面オブジェクトを生成して、そのポインターを返す。
* gluDeleteQuadric(obj) - 二次曲面オブジェクトを削除する。

* Quadric objects は四種類のレンダー様式がある。
  点、線、塗りつぶしはいつも通りだが、シルエットというものがある。

  * gluQuadricDrawStyle(obj, style)

    :style: GLU_(POINT|LINE|FILL|SILHOUETTE)

  * gluQuadricNormals(obj, mode)

    :mode: GLU_(NONE|FLAT|SMOOTH)

  * gluQuadricTexture(obj, mode)

    :mode: GL_(TRUE|FALSE)

* どの GLU 二次曲面も内部的には多角形近似で描くのだが、
  その多角形の点の多さのようなものを引数に指示する必要がある。

  * gluSphare(obj, radius, slices, stacks)

    * The sphere is approximated with polygons using slices lines
      of longitude and stacks linces of latitude. (p. 93)

  * gluCylinder(obj, base, top, height, slices, stacks)

    * 名前は円柱だが、上面と底面で半径を別々に指示できる。

  * gluDisk(obj, inner, outer, slices, rings)

    * 文字通り円盤。中央に穴が開いている。

  * gluPartialDisk(obj, inner, outer, slices, rings, start, angle)

    * 扇形円盤。
    * Partial disks are disks with a wedge removed. (p. 94)

GLUT Objects
~~~~~~~~~~~~
* 球、円錐、トーラス、正多面体、果てはティーポットまで提供している。
* 二次曲面系は多角形近似のための引数指定が必要。面倒そうだな。

  * glutWireSphere(radius, slices, stacks), glutSolidSphere(radius, slices, stacks)
  * glutWireCone(base, height, slices), glutSolidCone(base, height, slices)
  * glutWireTorus(inner, outer, sides, slices), glutSolidTorus(inner, outer, sides, slices)

* 正多面体 (regular polyhedral) をすべてサポート。キューブ以外を特に強調している。
  半径 1 の球に内接するサイズで定義されている。

  * glutWireTetrahedron(), glutSolidTetrahedron()
  * glutWireOctahedron(), glutSolidOctahedron()
  * glutWireDodecahedron(), glutSolidDodecahedron()
  * glutWireIcosahedron(), glutSolidIcosahedron()

* 特筆すべきは何と言ってもティーポットだ。
  <The Utah teapot is generated using OpenGL surface.  The teapot
  has been used for many years for testing rendering algorithms.
  It is constructed from 192 vertices.  The teapot is generated
  with both normals and texture coordinates.> (p. 97)

  * glutWireTeapot(size), glutSolidTeapot(size)

    ティーポットを size の大きさで描く。

Perspective Projections
-----------------------
* 透視図法投影を実現するための行列操作を習得する。
* glFrustum(left, right, bottom, top, near, far)
  
  * 引数リストは glOrtho と同じ。
  * far > near > 0 に注意。
  * ほぼ必ず以下の手順で利用する。
    ::

      glMatrixMode(GL_PROJECTION);
      glLoadIdentity();
      glFrustum(left, right, bottom, top, near, far);

* glFrustum と gluPerspective の使いやすさの違いを憶えておく。
  <the interface provided by glFrustum() can make it difficult
  to obtain a desired view.> (p. 98)

* we change the lens and get one with a wider angle of view.
  The function gluPerspective() provides such an interface. (p. 98)

* gluPerspective(fov, aspect, near, far)

  :fov: 角錐台の上下間の角度。
  :aspect: width / height

* One potential problem with perspective views is loss of
  accuracy in depth, which can be noticeable in the display.
  (p. 100)

* near plane をカメラに近づけ過ぎぬ事。
  <The problem is worst when the near plane is very close to
  the center of projection> (p. 100)

* Placing the front clipping plane too close to the camera can lead to numerical 
  errors in depth calculations for perspective views. (p. 100)

Programming Exercises
----------------------
* 球を自力で多角形近似で描画するときのコツは、
  <Use quad strips except for triangle fans at the poles.> (p. 100)
  だそうだ。

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

----

:doc:`angel05-note2` へ。
