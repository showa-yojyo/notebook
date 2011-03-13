======================================================================
OpenGL: A Primer Second Edition 読書ノート 1/4
======================================================================

:著者: Edward Angel
:出版社: Peason Education, Inc.
:ISBN: 0-321-26982-9

.. contents:: ノート目次

Preface
=======
* 赤本と青本

  * <the OpenGL Progamning Guide, Fourth Edition (Addison-Wesley), the "red book">
  * <the OpenGL 1.4 Reference Manual, Fourth Edition (Addison-Wesley), the "blue book">

* OpenGL ARB については後で説明あり。
* <it is much easier to get started with OpenGL and use it to master the basic concepts.
  For those of us who work with scientific applications and in a cross platform environment,
  OpenGL is the API of choice> (p. xvi)

Introduction
============
<OpenGL is an interactive computer graphics system that allows programmers to write
programs that access graphics hardware.  OpenGL has two important benefits for
application programmers.  It is close enough to the hardware so that programs written
with OpenGL run effectively, and OpenGL is easy to learn and use> (p. 1)

The OpenGL API
--------------
* <OpenGL came from an interface called GL, short for Graphics Library, originally
  developed for Silicon Graphics Inc. (SGI) hardware> (p. 1)

* OpenGL にはアプリを組むためにある 200 を越える関数がある。

* この本ではレンダリングを以下のように説明している。
  <taking the specification of geometric objects and their properties and
  forming a picture of them with a virtual camera and lights> (p. 2)

* GLUT について、T が Toolkit の頭文字であることを記憶する。

* <Rather than write platform-dependent code, we shall use a simple toolkit,
  the OpenGL Utility Toolkit (GLUT)> (p.1)

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
* <GLX for X Windows, wgl for Windows, and agl for the Macintosh> (p. 11)

GLUT
----
* Figure 2.2 では GLUT 層が GLX or WGL or AGL 層を完全にラップしている。
  GLUT を利用することで、プラットフォーム間の垣根を越える。

* <Depending on the platform, GLUT uses glX, wgl, or agl> (p. 13)

Event Loops and Callback Functions
----------------------------------
* ``glutInit`` は他のいかなる GLUT と OpenGL 関数呼び出しの前に呼ぶこと。
* ``glutCreateWindow`` によるウィンドウのサイズは 300 x 300 pixels
* イベントキューという用語を憶える。
* コールバック関数。どうしてもグローバル変数の世話にならざるを得ない。
* ``glutMainLoop`` の呼び出し行以降の行は、実行されない。

Drawing a Rectangle
-------------------
* <The fundamental entity for specifying geometric objects is the vertex,
  a location in space.  Simple geometric objects such as lines and polygons
  can be specified through a collection of vertices> (p. 15)

* <OpenGL puts the rendered image in an area of memory called a **color buffer**
  that usually resides on the graphics card.  Color buffers are one of a 
  number of types of buffers that make up the **frame buffer**> (p. 16)

Changing the GLUT Defaults
--------------------------
* ``glutInitDisplayMode(mode)``

  :mode: ``GLUT_(RGB|INDEX|SINGLE|DOUBLE)``, etc.

* ``glutInitWindowSize(width, height)``
* ``glutInitWindowPosition(x, y)``

Color in OpenGL
---------------
* <In RGBA mode, we use a fourth color component, A or alpha, which is
  an opacity> (p. 18)

* Opacity というのは日本語にないような。透明度の裏の概念というか。

Color and State
~~~~~~~~~~~~~~~
* <colors are not attached to objects but rather to the internal state
  of OpenGL> (p. 20)

  OpenGL の世界では色もまた状態なのだ。

* <OpenGL actually has only one internal form for the present color,
  which is in RGBA form, usually a floating point number for each color
  component> (p. 20)

* どんな ``glColor`` 関数を利用しようが、内部的なデータの形式は一つしかない。
  ``glColor3i`` のほうが ``glColor4fv`` より軽いなどということはないようだ。

Coorinate System Differences Between GLUT and OpenGL
----------------------------------------------------
* ウィンドウの Y 軸の正の方向について、OpenGL の座標系と GLUT の座標系では逆。

Two-Dimensional Viewing
-----------------------
* ``gluOrtho2D(left, right, bottom, top)``

* ``gluOrtho2D`` によって定義する矩形をクリッピングウィンドウと呼ぶ。

The Viewport
------------
* ``glViewport(x, y, width, height)``

  ウィンドウのどの部分を canvas とするのかを指定する。
  通常はウィンドウ全域を ``glViewport`` に渡すが、二次元的にイメージを描く場合などは、
  本当にウィンドウの特定部分を指定することが多い。

Coordinate Systems and Transformations
--------------------------------------
* <The function ``gluOrtho2D`` is used to specify a projection matrix for two-
  dimensional applications> (p. 23)

* まず間違いなく以下の手順で利用する。

  .. code-block:: c

     glMatrixMode(GL_PROJECTION);
     glLoadIdentity();
     gluOrtho2D(left, right, bottom, top);

* <In OpenGL, there are three basic types of geometric primitives: 
  points, line segments, and polygons> (p. 26)

  たった三種類しかないのだ。

Primitives and Attributes
-------------------------
* <in fact, OpenGL regards attributes as part of its state> (p. 26)
  アトリビュートも他の何かと同様に「状態」ということ。

Points
~~~~~~
* ``glPointSize(size)``

  :size: サイズはスクリーンピクセル単位

* ``glPointSize`` は ``glBegin`` と ``glEnd`` の間に入れない。

Lines
~~~~~
* 線分は三種類のタイプしかない。

  * ``GL_LINES``
  * ``GL_LINE_STRIP``
  * ``GL_LINE_LOOP``

* 線分の属性は 

  1. 色
  2. 線幅
  3. パターン

* ``glLineWidth(width)``

  :width: 幅はピクセル単位で与える。

* ``glLineStipple(factor, pattern)``

  :factor: パターンの繰り返し回数。1 から 256 の間の値。
  :pattern: line stipple のビットパターン (16 bit) の与え方をおさえておくこと。

Enabling OpenGL Features
~~~~~~~~~~~~~~~~~~~~~~~~
* OpenGL の機能の中には、明示的にそれを有効にしなければ利用できないものがある。
* ``glEnable(feature)`` で機能 feature を ON にする。

  .. code-block:: c

     glEnable(GL_LINE_STIPPLE);

* ``glDisable(feature)`` で機能 feature を OFF にする。

Filled Primitives
~~~~~~~~~~~~~~~~~
* ポリゴン。六種類のタイプがある。
  このノートには敢えて書かないが、説明の英文は丸暗記しておきたい。

  * ``GL_POLYGON``
  * ``GL_TRIANGLES``
  * ``GL_TRIANGLE_STRIP``
  * ``GL_TRIANGLE_FAN``
  * ``GL_QUADS``
  * ``GL_QUAD_STRIP``

* STRIP 系の図形描画は、関数呼び出しの回数が少なく済むという利点がある。

  <many CAD applications generate triangles or quadrilaterals with shared
  edges.  Strip primitives allow us to define these primitives with far
  fewer OpenGL function calls than if we had to treat each as a separate
  polygon> (p. 30)

Rectangles
~~~~~~~~~~
* 長方形を描くのなら ``glRect`` で済む場合がある。
  ``glVertex`` を四回書かなくて済むし、おすすめ。

Polygon Stipple
~~~~~~~~~~~~~~~
* polygon stipple の模様は、プリミティブを回転しても回転しない。
* ``glEnable(GL_POLYGON_STIPPLE)`` で有効にする。
* ``glPolygonStipple(mask)``

  :mask: 32 x 32 ビットのパターン。

Polygon Types
-------------
* 塗りつぶしポリゴンを描くときには、その形状に気をつける点がある。
  <**simple polygons** -- polygons whose edges do not cross -- two different
  OpenGL implementations may render them differently> (p. 31)

* <Convex polygons are much easier to render> (p. 32)

* 面には表と裏がある。それらを描画し分ける手段がある。

  * ``glPolygonMode(face, mode)`` - 面をどう描くか

    :face: ``GL_(FRONT|BACK|FRONT_AND_BACK)``
    :mode: ``GL_(POINT|LINE|FILL)``

  * ``glCullFace(mode)`` - 描くか否か

    :mode: ``GL_(FRONT|BACK|FRONT_AND_BACK)``

  * ``glFrontFace(mode)`` - 面の表裏をどう定義するか

    :mode: ``GL_(CCW|CW)``

* <By default, a front face is one in which the order of the vertices is
  counter-clockwise when we view the polygon.  A back face is one in which
  the vertices are specified in a clockwise order.  These definitions
  make sense for convex polygons> (p. 32)

* <In OpenGL, the edges of a polygon are part of the inside of the polygon> (p. 33)

* 塗りつぶしと線の描画を重ねあわすことについて、
  場合によってはポリゴンオフセットをかけないと美しくないかも。

* ``glPolygonOffset(factor, units)``

  :factor, units: 謎のパラメータ。

  ``glPolygonOffset`` 関数は次のようにして利用する。
  
  .. code-block:: c

     glPolygonOffset(1.0, 1.0);
     glEnable(GL_POLYGON_OFFSET_LINE);

Color Interpolation
-------------------
* <The default is to use smooth shading where OpenGL will interpolate the colors
  at the vertices to obtain the color of intermediate pixels> (p. 34)

* OpenGL がポリゴンに対して何らかの補間を行うときは、大抵は bilinear interpolation だ。

* ``glShadeModel(mode)``

  :mode: ``GL_(SMOOTH|FLAT)``

Tessellation and Edge Flags
~~~~~~~~~~~~~~~~~~~~~~~~~~~
``glEdgeFlag`` と tessellation, subdivision の話が続く。

Tessellation and Subdivision
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
subdivision は図形にねじれを加えるような画像効果を実現する手段として利用できるようだ。

Text
----
* フォントには bitmap と stroke の二種類がある。
* bitmap は高速に描画できるが、スケーリング等の変換がかけられない。
  stroke はその逆の長所短所がある。
* フォントはシステム依存のものなので、GLUT がその辺をカバーしてくれている。

* ``glutBitmapCharacter(font, character)``

  :font: ``GLUT_BITMAP_TIMES_ROMAN_10`` のようなシンボルを指定する。
  :character: 一文字を指定する。

* Raster position は左下原点
* <The current raster position is offset automatically so that the next
  character will not be rendered on top of the previous one> (p. 44)

* ``glRasterPos(xyzw)`` - ラスター位置を設定する。
* ``glutBitmapWidth(font, character)`` - 文字幅をピクセル値で返す。
* ``glutStrokeCharacter(font, character)`` - ストロークフォントにて文字を描画する。
* ``glutStrokeWidth(font, character)`` - 文字幅をビット単位で返す。

* ストローク系のフォントサイズは単位がよくわからないので注意。
  StrokeWidth の 1 が世界座標系の長さ単位の 100 程度とのこと。

Querues and Errors
------------------
* ``glGet(Boolean|Integer|Float|Double|Pointer)`` 系の話はノート省略。
* ``glGetError`` と ``gluErrorString`` はデバッグのために憶えておく。
  これらを組み合わせてエラーを知る。
* GLUT の状態は ``glutGet`` で得る。

Saving the State
----------------
* OpenGL はステートマシーンなので、プログラムを書いていると、
  各種状態をちょっと前の時点のものに戻したいくなる状況になることがよくある。

* 行列の（成分という意味での）状態に関しては、
  ``glPushMatrix``, ``glPopMatrix`` が利用できる。
  各行列モードに対して、行列スタックが存在する。
  one pop for each one push ルールを肝に銘じること。

* 各種属性に関しては ``glPushAttrib``, ``glPopAttrib`` を利用できる。
  全属性状態を一気に push することも可能だが、
  通常は必要なものだけを push するのだろう。
  引数がビットマスクなので、適切な値を指示することに慣れる必要がある。

Interaction and Animation
=========================
The Reshape Callback
--------------------
* <Within the loop, the program responds to discrete events
  involving the keyboard and the mouse through callback functions that
  the application programer writes> (p. 49)
* <This action generates a window event that is handled by the reshape
  callback> (p. 49)

* ``glutReshapeFunc(f)``
  
  :f: ``void (*)(int width, int height)`` 型の関数のアドレス。
      <A display callback is invoked automatically after executing ``f()``> (p. 49)

* <The reshape callback is invoked when a window is first created> (p. 49)

* Reshape callback でプログラマーが書くことは、ビューポートのリセットと
  クリッピングウィンドウのリセットの二点だ。

* ``gluOrtho2D`` の ``bottom``, ``top`` の値をウィンドウのサイズに依存するように決める。
  幅と高さの短い方を分母にしたアスペクト比。

The Idle Callback
-----------------
* <The idle callback identifies a function, which should be executed
  whenever there are no otther events to be handled, that is, whenever
  the event queue is empty> (p. 51)

* ``glutIdleFunc(f)``

  :f: ``void (*)()`` 型の関数のアドレスを渡す。

* <Use of ``glutPostRedisplay()`` ensures the window gets drawn at most once
  each time that GLUT goes through the event loop.  In general, it is a 
  good idea to never call the display callback directly but rather to use
  the ``glutPostRedisplay()`` whenever the display needs to be redrawn> (p. 52)

* ``glutPostRedisplay()`` - 現在のコールバックがリターンした後にディスプレイコールバックが
  実行されるようにお願いする関数。

A Rotating Square
-----------------
ここでは三角関数を利用して円に内接する正方形を回転するアニメーションを実装している。

Double Buffering
----------------
* <This refresh process is not controllable from the user program> (p. 54)

* ダブルバッファは二つの color buffers を使うというのがミソ。それぞれ
  **front buffer** と **back buffer** と呼ぶ。

  :front buffer: ディスプレイハードウェアによってディスプレイされるバッファ
  :back buffer: アプリケーションが書き込む先のバッファ

* ``glutSwapBuffers()`` - front buffer と back buffer を入れ替える。

* 書くのが最後になったが、ダブルバッファを有効にするには ``glutInitDisplayMode`` で
  指定する。

  .. code-block:: c

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_XXXX);

Using the Keyboard
------------------
* <GLUT ignores releasing of the key> (p. 54)

* ``glutKeyboardFunc(f)``

  :f: ``void (*)(key, x, y)`` 型関数アドレス。スクリーン座標が存在するのが面白い。

* GLUT の関数でマウス位置を扱うものは、すべてウィンドウ左上が原点。
* Esc キーは 8 進数で 027 となる。16 進数では 0x1B となる。

Special Keys
~~~~~~~~~~~~
* ``glutSpecialFunc(f)`` - F1 キーとか↑キーとかのプレスイベントをハンドルする。

  :f: ``glutKeyboardFunc`` のと同じ。

* ``glutGetModifiers()`` - マウスやキーを押されたときに、以下のキーの状態を見る。

  :return: ``GLUT_ACTIVE_(SHIFT|CTRL|ALT)``

Using the Mouse Callback
------------------------
* ``glutMouseCallback(f)``

  :f: ``void (*)(button, state, x, y)``

    :button: ``GLUT_(LEFT|MIDDLE|RIGHT)_BUTTON``
    :state: ``GLUT_(UP|DOWN)``

* ``x``, ``y`` は GLUT の座標系での値なので、<The most important is the necessity
  of inverting the ``y`` value returned by the mouse callback> (p. 58)

* ディスプレイコールバックが必要のないプログラムを書く場合もあるが、
  <As a practical matter, GLUT insists that every program have a display
  callback> (p. 59) だそうだ。そういう場合は空の実装を与える。

* しかし普通はそんなことはしない。<A more general strategy is to 
  place drawing functions in the display callback and use the other 
  callbacks for state changes>(p. 59)
  その上で ``glutPostRedisplay`` をすればよい。

Mouse Motion
------------
* マウスモーションには ``glutMotionFunc`` と ``glutPassiveMotionFunc`` の二種類のコールバックが利用できる。
* Passive とは、マウスボタンが押されていない状態でマウスが動いているイベントのことだ。
* ``glutMotionFunc(f)``, ``glutPassiveMotionFunc(f)``

  :f: ``void (*)(x, y)`` 型関数のアドレス

* ``glutEntryFunc(f)``: マウスキャプチャーに使うのか？

  :f: ``void (*)(state)`` 型関数のアドレス
  
    :state: ``GLUT_(ENTERED|LEFT)``

The NULL Callback
-----------------
``glutXXXFunc`` にヌルを渡すと、コールバックを削除できる。

Subwindows and Multiple Windows
-------------------------------
* コンテキストの概念は重要。
* <Each window can have its own properties, referred to as its context> (p. 64)

Display Lists
-------------
* ディスプレイリストをファイルに例えて説明している。
  <Display lists can be thought of as a type of graphics file in which we can
  place OpenGL rendering and state update commands.  We open a display list,
  give it a name, place commands in it, and close it> (p. 67)

* ディスプレイリストを定義するときは、各種状態の push/pop が重要だ。
  <Note that we push and pop the current attributes, which include the present
  color.  We must do this action to prevent the state change due to setting
  a new color from affecting anything that we do subsequently.  Often we can
  prevent unforeseen side effects of state changes by starting a display
  list by pushing the matrices and the state at the beginning of the display
  last popping them at the end> (p. 68)

  後続のディスプレイリストに余計な状態を残さぬように、リストを定義する。

* ``glNewList(name, mode)``: ディスプレイリストの定義を開始する。

  :name: ディスプレイリストの名前。
         通常、次節で紹介されている ``glGenLists`` の戻り値を指定する。
  :mode: ``GL_COMPILE`` か ``GL_COMPILE_AND_EXECUTE``

* ``glEndList()``: ディスプレイリストの定義を終了する。
* ``glCallList(name)``: ディスプレイリストを実行する。
* ``glGet`` 等の「状態を返すだけの関数」をディスプレイリスト定義中に呼ぶことはできない。
* ディスプレイリストを階層的に ``glCallList`` することができる。
* ディスプレイリストは、一度作成したら変更できない。
* ``glDeleteLists(first, number)``: ディスプレイリストを削除する。

  名前が ``first`` のリストから、
  ``number`` 個目までのリストを削除する。

Multiple Display Lists
~~~~~~~~~~~~~~~~~~~~~~
* ``glListBase(offset)`` - ``glCallList`` の実引数にゲタをはかせる
* ``glCallLists(num, type, list)``

  :num: ``list`` の個数
  :type: ``list`` の型
  :list: ディスプレイリストの名前（つまり整数値）の配列

* ``glGenLists(n)`` - ディスプレイリスト新規作成のための有効な名前を n 個生成する。

Display Lists and Text
~~~~~~~~~~~~~~~~~~~~~~
* <To generate a character string on the display, 
  we do one function call per character> (p. 69)

* 全 ASCII 文字についてディスプレイリストをコンパイルするやり方を紹介している。
  ディスプレイリストの ID を文字コードと同じにして……という方法だ。
  日本語に応用できるとは思えない。

Display Lists and Objects
~~~~~~~~~~~~~~~~~~~~~~~~~
* <display lists can give the user a way of building more object-oriented program
  than in immediate mode> (p.70) とあり、人間の顔を描くと思われるディスプレイリストを
  定義するコードを記載している。
  ``glNewList`` と ``glEndList`` の間に、
  顔のパーツを定義するディスプレイリストを ``glCallList`` するという例だ。

Picking and Selection Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~
* 本書ではピックの定義を以下のように与えている。
  <**Picking** is the operation of locating an object on the screen> (p.71)

* ピックのためには、描画要素にある種のタグ付けを行う必要がある。
  <We could create some sort of tag system that would give labels to
  parts of our program> (p. 71)

* **selection mode** で描画を行うと、オブジェクトは color buffer にレンダーされない。
* ピック処理はコードを書くのが面倒。関係する関数が次に挙げるように、妙に多い。

  * ``glRenderMode(mode)`` - render mode の選択

    :mode: ``GL_(RENDER|SELECTION|FEEDBACK)``

  * ``glSelectBuffer(n, buffer)`` - 選択データを置く配列を決める
  * ``glInitNames()`` - name stack の初期化
  * ``glPushName(name)`` - name stack に name を積む
  * ``glPopName()`` - name stack から name をひとつ捨てる
  * ``glLoadName(name)`` - name stack の一番上の要素を name で置き換える

* <``glRenderMode()`` returns the number of hits that have been processed> (p. 73)

* <``gluPickMatrix()``, that should be applied before ``gluOrtho2D()`` when we
  are in selection mode> (p. 73)

* <If we had a hierarchical object in which multiple parts of the object could
  all be located near the cursor, we could use ``glPushName()`` so that we could
  have multiple names on the stack for a given hit.  For an object with multiple
  parts, all the parts that were close to the cursor would have their names
  placed in the same stack> (p. 75)

* ヒットレコードのバイトレイアウトについて、細かく説明している。
  <we find three types of information, all stored as integers.  First, there
  is the number of names on the name stack when there was a hit.  It is followed
  by two integers that give scaled minimum and maximum depths for the hit primitive.
  These three integers are followed by entries in the name stack> (p. 75)

----

:doc:`angel05-note2` へ。
