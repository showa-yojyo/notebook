======================================================================
Getting started
======================================================================

.. contents:: ノート目次

What is a fragment shader?
======================================================================

この節は今や読み飛ばせる。次のようなことが述べられている：

計算機で絵を描くという処理は、手書きの手紙や本を書くのと似ていて、次から次へと作業を行う命令の集合体だ。
シェーダーも命令の集合体であり、その命令は画面上のすべての画素に対して一度に実行される。
つまり、コードは画面上の画素の位置に応じて異なる動作をしなければならない。
活字印刷機のように、位置を受け取って色を返す関数としてプログラムを動作させ、
それをコンパイルすると超高速で動作することになる。

Why are shaders fast?
----------------------------------------------------------------------

この節の記述は面白い。要約すると次のようになる：

画面上の画素一つ一つを単純かつ小さなタスクとみなす。
この小さなタスクは画面上の各画素に対して行われなければならない。
例えば古の 800x600 の画面でさえ、フレームあたり 480,000 画素を処理しなければならず、
秒間 14,400,000回の計算をしなければならないということだ。これをどうクリアしているのか。

並列処理が有効な解決策となる。パイプのたとえで言うと、大きくて強力なパイプをいくつか用意するよりも、
小さな大量のパイプを同時に並列動作させたほうが良い。GPU はこの方針に基づいた処理装置だ。

本書のイラストのように、GPU と各画素データを大量のパイプの束とピンポン玉にそれぞれなぞらえる。

秒間 1,440,000個のピンポン玉を放り込もうとすれば、どんな太いパイプをも塞ぐだろう。
一方、秒間 480,000 画素の波を 30 回受信する 800x600 の小さなパイプからなる束ならばまだ円滑に処理できるだろう。
並列度の高いハードウェアほど大きなストリームを処理することができる。

これとは別に、GPU のもう一つの超能力は、ハードウェアで加速された特殊な数学だ。
あとの章で述べられる複雑な数学演算をソフトウェアではなくマイクロチップが直接解決する。
これにより、三角関数や行列の演算が非常に高速になり、電気の力を最大限に発揮できる。

What is GLSL?
----------------------------------------------------------------------

GLSL の定義が書かれている。これは当面の目的には役には立たない。

Why are Shaders famously painful?
----------------------------------------------------------------------

シェーダーを書くのは苦行なのかもしれない。

* 並列処理を行うためには、すべてのスレッド（パイプ）が他のすべてのスレッドから独立していなければならない。
  この制約は、すべてのデータが同じ方向に流れなければならないことを意味する。
  そのため、他のスレッドの結果を確認したり、入力データを修正したり、
  スレッドの結果を他のスレッドに渡したりすることはできない。
  スレッド間の通信を許可すると、データの整合性が損なわれる。
* また、GPU は並列マイクロプロセッサー（パイプ）を多忙にしており、
  空き時間になると新しい情報を受け取って処理している。
  スレッドが直前の瞬間に何をしていたかを知ることはできない。
  それは、OS の UI からボタンを描き、ゲームで空の一部を描き、
  それからメールの文章を表示するといったことであったりさえもする。
* 各スレッドはさらに記憶能力もない。

"Hello world!"
----------------------------------------------------------------------

次を技術、知識を習得できる：

* 断片シェーダーのみで背景をベタ塗りする方法
* ``vec4``, ``vec3``, ``float``, ``int``, RGBA などの基本事項各種
* ``precision {highp,mediump,lowp} float;`` のような宣言が必要であること
* GLSL で引数リストが空であるユーザー関数を定義する方法

なお ``gl_FragColor`` は WebGL2 などで書く ``version 300 es`` なシェーダーではもう使えないはずだ。
普通の ``out vec4`` 変数で代替する。

--------------

演習問題

* 浮動小数点数を整数に書き換えるとどうなるか試せ。
* ``gl_FragColor`` への代入式全体をコメントアウトするとどうなるか試せ。
* 特定の色を返す別の関数を作って、それを ``main()`` の中で使ってみろ。

解答

``vec4`` の実引数を ``float`` リテラル値から ``int`` リテラル値に書き換えても問題なく動作する。
しかし、他のページのコードではエラーになることがふつうにある。

``gl_FragColor`` への代入をやめると、背景色が地の色のままになる。

GLSL ではユーザー関数を定義することができる。ここではいちばん素朴な実装を示す。

.. code:: glsl

   vec4 red(){
       return vec4(1.0, 0.0, 0.0, 1.0);
   }

   void main() {
       gl_FragColor = red();
   }

Uniforms
======================================================================

* キャンバスサイズ、マウス位置、時刻などを ``uniform`` 修飾された変数で処理すること。
* 先述のように、GLSL がハードウェア加速されている角度、三角関数、指数関数を用意していること。
* 特に次の関数は全て、この章を読んだ読者が履修したものとみなすようだ：

  * `sin <https://thebookofshaders.com/glossary/?search=sin>`__
  * `cos <https://thebookofshaders.com/glossary/?search=cos>`__
  * `tan <https://thebookofshaders.com/glossary/?search=tan>`__
  * `asin <https://thebookofshaders.com/glossary/?search=asin>`__
  * `acos <https://thebookofshaders.com/glossary/?search=acos>`__
  * `atan <https://thebookofshaders.com/glossary/?search=atan>`__
  * `pow <https://thebookofshaders.com/glossary/?search=pow>`__
  * `exp <https://thebookofshaders.com/glossary/?search=exp>`__
  * `log <https://thebookofshaders.com/glossary/?search=log>`__
  * `sqrt <https://thebookofshaders.com/glossary/?search=sqrt>`__
  * `abs <https://thebookofshaders.com/glossary/?search=abs>`__
  * `sign <https://thebookofshaders.com/glossary/?search=sign>`__
  * `floor <https://thebookofshaders.com/glossary/?search=floor>`__
  * `ceil <https://thebookofshaders.com/glossary/?search=ceil>`__
  * `fract <https://thebookofshaders.com/glossary/?search=fract>`__
  * `mod <https://thebookofshaders.com/glossary/?search=mod>`__
  * `min <https://thebookofshaders.com/glossary/?search=min>`__
  * `max <https://thebookofshaders.com/glossary/?search=max>`__
  * `clamp <https://thebookofshaders.com/glossary/?search=clamp>`__

--------------

演習問題

* 色の変化がほとんど気にならなくなるまで周波数を下げろ。
* ちらつきのない単一の色が見えるようになるまでスピードを上げろ。
* RGB チャンネルの周波数をいじれ。面白いパターンや動作が得られる。

解答

周期関数として ``sin`` を用いているので、例えば ``sin(2 * PI * x / T)`` だと周期は ``T`` だから
周波数すなわち ``1./T`` を上げるならば ``T`` をゼロに近づける必要がある。

.. code:: glsl

   uniform float u_time;

   const float tau = radians(360.);
   const float T = 1.; // これを書き換えて大きくしたり小さくしたりする

   void main() {
       gl_FragColor = vec4(abs(sin(tau * u_time / T)), 0.0, 0.0, 1.0);
   }

最後の問いの解答としては、これまでは R チャンネルしか変化させていないが、このようなことを G, B でもすればいい。

``gl_FragCoord``
----------------------------------------------------------------------

* 定義済み変数 ``gl_FragCoord`` の意味。
* このベクトルをキャンバス解像度で除算すれば、正規化された座標が得られる。
* キャンバスの座標系の向き。
* 線形グラデーション塗りの技法。
* マウス位置、時刻を参照してカラーパターンを変化させる手法。

--------------

演習問題

* 座標 :math:`(0.0, 0.0)` がキャンバスのどこにあるか。
  :math:`(1.0, 0.0), (0.0, 1.0), (0.5, 0.5), (1.0, 1.0)` はどうか。
* ``u_mouse`` の値が画素単位であり、正規化された値ではないことを理解した上で、
  ``u_mouse`` の使い方を理解したか。これを使って、色を動かすことができるか。
* ``u_time`` と ``u_mouse`` を使って、このカラーパターンを変更する面白い方法を想像できるか。

解答

まず、スクリーンの座標系の向きは数学と同じだから、原点はキャンバスのいちばん左下の点（本書では点とは呼んでいないが）となる。
その次の四点はキャンバス座標空間が正規化されたことを前提として、
それぞれキャンバスの右下、左上、中央、右上に等しい。

マウスの問題は微妙で、変数 ``st`` と一緒に用いるには正規化する必要がある。
色を動かすには、例えば：

.. code:: glsl

   gl_FragColor = vec4(st.x, step(u_mouse.y / u_resolution.y, st.y), 0.0, 1.0);

しかし、\ ``u_mouse`` が一様変数である以上は正規化をシェーダーの外でやるべきだろう。

最後の問いは省略。

Running your shader
======================================================================

著者が製作した、シェーダーを作成、表示、共有、管理するためのツール群。
これらのツールは Linux, MacOS, Windows, Raspberry Pi,
ブラウザー間で一貫して動作し、コードを変更する必要がないとある。

Running your shaders on the browser
----------------------------------------------------------------------

* この本に掲載されているすべてのライブサンプルは、
  `glslCanvas <https://github.com/patriciogonzalezvivo/glslCanvas>`__ を使って表示している。
  スタンドアロンシェーダーの実行プロセスが驚くほど簡単だ。
* コンソールから直接シェーダーを実行したいと思う人は glslViewer をチェックするといい。
  シェルスクリプトやパイプラインにシェーダーを組み込み、
  ImageMagick と同様の方法で使用することができる。

  .. code:: console

     bash$ glslViewer yourShader.frag yourInputImage.png —w 500 -h 500 -E screenshot,yourOutputImage.png

* `glslEditor <https://github.com/patriciogonzalezvivo/glslEditor>`__ というオンラインエディターを著者が用意した。
  `スタンドアローンの Web アプリケーション版 <http://editor.thebookofshaders.com/>`__\ もある。
* And more...

Running your shaders on your favorite framework
----------------------------------------------------------------------

本書で使用する ``u_XXXX`` 変数と同じものを使って、いくつかの人気フレームワークにシェーダーを設定する方法の例が示されている。

* `Three.js <https://threejs.org/>`__: これは未着手
* `Processing <https://processing.org/>`__: これは初耳のフレームワーク
* `openFrameworks <https://openframeworks.cc/>`__: C++ のフレームワーク
* Blender 用に `glslTexture <https://github.com/patriciogonzalezvivo/glslTexture>`__ というアドオンを製作
