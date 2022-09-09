======================================================================
OpenGL Shading Language 4.60 Specification 読書ノート Part 7
======================================================================

`仕様書該当部分 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#built-in-variables>`__

.. contents:: ノート目次

7. Built-In Variables
======================================================================

7.1. Built-In Language Variables
----------------------------------------------------------------------

シェーダーの機能外で行われたり、シェーダー実行形式に値を提供したり、
シェーダー実行形式から値を受け取ったりする必要がある操作もある。
シェーダーは、組み込み入力変数と出力変数を使って、
固定機能のパイプライン段階や、オプションで他のシェーダー実行形式と通信する。

7.1.1. Vertex Shader Special Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

本文で示されているように、組み込み頂点シェーダー変数が内的に宣言されている。

.. admonition:: コメント

   `コード片 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#vertex-shader-special-variables>`__

変数 ``gl_Position`` は同次座標系の頂点位置を書き込むためのものだ。
シェーダー実行中のいつでも書き込むことができる。
この値が用いられるのは、頂点処理が行われた後に基本形状を操作する基本形状組み立て、
切り取り、間引き、その他の固定機能操作だ。
基本形状への操作が存在すれば、頂点の処理が行われた後に起こる。
頂点シェーダー実行形式が ``gl_Position`` を書いていない場合、
頂点処理段階後ではその値は未定義となる。

変数 ``gl_PointSize`` は、ラスタライズされる点の大きさをシェーダーが書き込むため
のものだ。これは画素で測定される。
``gl_PointSize`` が書き込まれない場合、その値は後続のパイプ段階では未定義となる。

変数 ``gl_ClipDistance`` は、切り取り距離を書き込むためのもので、
ユーザー切り取りを制御するための前方互換装置だ。
要素 ``gl_ClipDistance[i]`` は、各平面 ``i`` に対する切り取り距離を指定する。
距離が 0 であれば、頂点が平面上にあることを意味し、
正の距離であれば、頂点が切り取り平面の内側にあることを意味し、
負の距離であれば、頂点が切り取り平面の外側にあることを意味する。
切り取り距離は基本形状全体を線形補間し、補間された距離が 0 より小さい基本形状の
部分が切り取られる。

``gl_ClipDistance`` 配列はサイズなしとして事前に宣言されているので、
シェーダーが明示的にサイズを再宣言するか、定整数式のみでインデックスをつけて
暗黙的にサイズを決める必要がある。
これには有効になっているすべての切り取り平面を含むように配列のサイズを API を
通じて決める必要がある。
サイズが有効平面すべてを含まない場合、結果は未定義だ。
サイズは最大で ``gl_MaxClipDistances`` となる。
``gl_ClipDistance`` が消費する varying 成分の個数は、
平面がいくつ有効であろうが、配列のサイズと一致する。
シェーダはまた、APIを介して有効にされた ``gl_ClipDistance`` のすべての値を設定
しなければならない。
有効化されていない平面に対する ``gl_ClipDistance`` に書き込まれる値は何の効果もない。

変数 ``gl_CullDistance`` は、ユーザー間引きを制御するための装置だ。
要素 ``gl_CullDistance[i]`` は平面 ``i`` の間引き距離を指定する。
距離が 0 であれば、頂点が平面上にあることを意味し、
正の距離であれば、頂点が間引きボリュームの内側にあることを意味し、
負の距離であれば、頂点が間引きボリュームの外側にあることを意味する。
すべての頂点が平面 ``i`` に対して負の間引き距離である基本形状は破棄される。

``gl_CullDistance`` 配列はサイズなしと事前宣言されており、
シェーダーがサイズを再宣言するか、定整数式だけでインデックスをつけるかして、
サイズを決めなければならない。
サイズは、有効間引き距離の個数と集合を決定するものであって、最大で
``gl_MaxCullDistances`` となる。
``gl_CullDistance`` が消費する　varying 成分数は配列のサイズと一致する。
``gl_CullDistance`` を書いているシェーダーは、有効距離すべてを書かなければならず、
さもなければ間引きの結果は未定義となる。

出力変数としての ``gl_CullDistance`` はシェーダーがこれらの距離を書き込む場所を用意する。
断片言語以外では入力として、直前のシェーダー段階で書き込まれた値を読み込む。
断片言語では、
``gl_CullDistance`` 配列は、シェーダーによって ``gl_CullDistance`` 頂点出力変数に
書き込まれた頂点値を線形補間した値を含む。

プログラムを構成する一連のシェーダーにおいて、
``gl_ClipDistance`` 配列と ``gl_CullDistance`` 配列のサイズの合計が
``gl_MaxCombinedClipAndCullDistances`` よりも大きくなると、コンパイルエラーまたは
リンクエラー。

変数 ``gl_VertexID`` は OpenGL 仕様書の 11.1.3.9 "Shader Inputs" で定義されている、
頂点の整数インデックスを保持する頂点シェーダー入力変数だ。
これは Vulkan を対象にしていない場合に限って存在する。存在するとしても、
``gl_VertexID`` の値が常に定義されているとは限らない。

``gl_InstanceID`` は頂点シェーダの入力変数で、インスタンス化された描画呼び出しに
おける現在の基本形状のインスタンス番号を保持する。
これは Vulkan を対象にしていない場合に限って存在する。
現在の基本形状がインスタンス化された描画呼び出しによるものでない場合、
``gl_InstanceID`` の値はゼロだ。

変数 ``gl_VertexIndex`` は頂点言語の入力変数で、
ある基準 (a base) からの頂点の整数インデックスを保持する。
これは Vulkan を対象にしている場合に限って存在する。存在するとしても、
``gl_VertexIndex`` の値が常に定義されているとは限らない。

変数 ``gl_InstanceIndex`` は、頂点言語の入力変数で、
インスタンス化された描画呼び出しにおける現在の基本形状のインスタンス番号を、
ある基準 (a base) からの相対値で保持する。
これは Vulkan を対象にしている場合に限り存在する。
現在の基本形状がインスタンス化された描画呼び出しによるものでない場合、
``gl_InstanceIndex`` の値はゼロだ。

変数 ``gl_DrawID`` は頂点シェーダーの入力変数であり、
現在の頂点が属する描画命令の整数インデックスを保持する。
頂点が ``Multi*`` 形式の描画命令によって呼び出されていない場合、
``gl_DrawID`` の値はゼロだ。

変数 ``gl_BaseVertex`` は頂点シェーダー入力変数であり、
現在のシェーダーの呼び出しを起こした命令の
``baseVertex`` 引数に渡された整数値を保持する。

変数 ``gl_BaseInstance`` は頂点シェーダー入力変数であり、
現在のシェーダー呼び出しを起こした命令の
``baseInstance`` 引数に渡された整数値を保持する。

7.1.2. Tessellation Control Shader Special Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: コメント

   細分化制御シェーダーで内在的に宣言されている組み込み変数の仕様。
   `コード片 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html##tessellation-control-shader-special-variables>`__

Tessellation Control Input Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``gl_Position``, ``gl_PointSize``, ``gl_ClipDistance``, ``gl_CullDistance`` には、
直前のシェーダー段階に対応する出力に書き込まれた値を含む。

``gl_PatchVerticesIn`` はシェーダーで処理される入力パッチの頂点数を含む。
単一のシェーダーが異なるサイズのパッチを読み込むことができるので、
``gl_PatchVerticesIn`` の値はパッチ間で異なる可能性がある。

``gl_PrimitiveID`` は、レンダリング基本形状の現在の集合が開始された以降に
シェーダーによって処理された基本形状の数を含む。

``gl_InvocationID`` は、細分化制御シェーダーの呼び出しに代入した出力パッチ頂点数を含む。
範囲 :math:`{[0, N-1]}` の整数値が代入されており、N は基本形状ごとの出力パッチ頂点の個数だ。

Tessellation Control Output Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``gl_Position``, ``gl_PointSize``, ``gl_ClipDistance``, ``gl_CullDistance`` は
対応する頂点シェーダーの出力変数と同じ方法で使用される。

``gl_TessLevelOuter`` と ``gl_TessLevelInner`` に書き込まれた値は、
出力パッチの対応する外側・内側細分化レベルに代入される。
これらの値は細分化基本形状生成器が基本形状細分化を制御するために使用され、
細分化評価シェーダーが読み取ることができる。

7.1.3. Tessellation Evaluation Shader Special Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: コメント

   細分化評価シェーダーで内在的に宣言されている組み込み変数の仕様。
   `コード片 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#tessellation-evaluation-shader-special-variables>`__

Tessellation Evaluation Input Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``gl_Position``, ``gl_PointSize``, ``gl_ClipDistance``, ``gl_CullDistance`` は、
直前のシェーダー段階に対応する出力に書き込まれた値を含む。

``gl_PatchVerticesIn`` と ``gl_PrimitiveID`` は細分化制御シェーダーで
対応する入力変数と同じ方法で定義される。

``gl_TessCoord`` は細分化される基本形状に対するシェーダーで処理される頂点の
位置を識別する三成分 ``(u, v ,w)`` ベクトルを指定する。
値は以下の性質に従い、細分計算を再現する援助とする：

.. code:: glsl

   gl_TessCoord.x == 1.0 - (1.0 - gl_TessCoord.x) // two operations performed
   gl_TessCoord.y == 1.0 - (1.0 - gl_TessCoord.y) // two operations performed
   gl_TessCoord.z == 1.0 - (1.0 - gl_TessCoord.z) // two operations performed

細分化制御シェーダーがアクティブな場合、
入力変数 ``gl_TessLevelOuter`` と ``gl_TessLevelInner`` はその細分化制御
シェーダーによって書き込まれた出力に対応するもので埋められる。
それ以外の場合は、OpenGL 仕様の 11.2.3.3 "Tessellation Evaluation Shader Inputs"
で指定された既定の細分化レベルが代入される。

Tessellation Evaluation Output Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``gl_Position``, ``gl_PointSize``, ``gl_ClipDistance``, ``gl_CullDistance`` は
対応する頂点シェーダーの出力変数と同じ方法で使用される。

7.1.4. Geometry Shader Special Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: コメント

   幾何シェーダーで内在的に宣言されている組み込み変数の仕様。
   `コード片 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#geometry-shader-special-variables>`__

Geometry Shader Input Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``gl_Position``, ``gl_PointSize``, ``gl_ClipDistance``, ``gl_CullDistance`` には
直前のシェーダー段階で対応する出力に書き込まれた値を含む。

``gl_PrimitiveIDIn`` は、レンダリング基本形状の現在の集合が開始された以降に
シェーダーによって処理された基本形状の数を含む。

``gl_InvocationID`` は、幾何シェーダーの呼び出しに代入した呼び出し番号を含む。
範囲 :math:`{[0, N-1]}` の整数値が代入されており、N は基本形状ごとの幾何シェーダー
の呼び出し回数だ。

Geometry Shader Output Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: コメント

   ここの節は未知の概念が特に多く含まれる。何か手がかりとなるものはないか。

``gl_Position``, ``gl_PointSize``, ``gl_ClipDistance``, ``gl_CullDistance`` は
対応する頂点シェーダーの出力変数と同じ方法で使用される。

``gl_PrimitiveID`` には、断片シェーダーに対する基本形状識別子として機能する
単一の整数で埋められる。これは断片シェーダーが利用できるもので、
シェーディングされる基本形状の provoking 頂点から書き込まれた基本形状 ID を
選択することになる。
``gl_PrimitiveID`` を使用する断片シェーダーがアクティブで、
幾何シェーダーもアクティブな場合、幾何シェーダーが ``gl_PrimitiveID`` に書き込まなければ、
断片シェーダーの入力 ``gl_PrimitiveID`` は未定義となる。
詳しくは OpenGL 仕様の 11.3.4.5 "Geometry Shader Outputs" を参照。

``gl_Layer`` は多重レイヤーフレームバッファー付属物の特定のレイヤー
（またはキューブマップの面とレイヤー）を選択するために使用される。
実際に使用されるレイヤーは、シェーディングされている基本形状の頂点一つに由来する。
その由来がどこかは、OpenGL 仕様書 11.3.4.6 "Layer and Viewport Selection" で
議論されているように決定されるが、
未定義の場合もあるので、基本形状の頂点すべてに同じレイヤーの値を書くのがよかろう。
シェーダが静的に ``gl_Layer`` に値を代入すると、レイヤーありレンダリングモードが
有効になる。
詳細は OpenGL 仕様書の 11.3.4.5 と 9.4.9 "Layered Framebuffers" を参照。
シェーダーが ``gl_Layer`` に静的に値を代入し、
``gl_Layer`` を設定しないシェーダーの実行経路がある場合、
その経路を通るシェーダーの実行では ``gl_Layer`` の値は未定義となる。

出力変数 ``gl_Layer`` は、キューブマップテクスチャーの配列で使用される場合、
特別な値をとる。
レイヤーを参照するばかりではなく、キューブマップの面とレイヤーを選択するために
使用される。
``gl_Layer`` に値 ``layer * 6 + face`` を設定すると、
レンダリングは ``layer`` レイヤーで定義された立方体の面に行われる。
面値は OpenGL 仕様書 9.4.9 表 9.3 に定義されている：

.. csv-table::
   :delim: @
   :header: Face Value, Resulting Target

   0 @ ``TEXTURE_CUBE_MAP_POSITIVE_X``
   1 @ ``TEXTURE_CUBE_MAP_NEGATIVE_X``
   2 @ ``TEXTURE_CUBE_MAP_POSITIVE_Y``
   3 @ ``TEXTURE_CUBE_MAP_NEGATIVE_Y``
   4 @ ``TEXTURE_CUBE_MAP_POSITIVE_Z``
   5 @ ``TEXTURE_CUBE_MAP_NEGATIVE_Z``

例えば、キューブマップ配列の第 5 層に位置する正の ``y`` のキューブマップ面に
レンダリングするには、
``gl_Layer`` を ``5 * 6 + 2`` に設定する。

出力変数 ``gl_ViewportIndex`` は、幾何シェーダーが出力する次回基本形状が描画されるべき
ビューポートのインデックスを提供する。
幾何シェーダーが生成する基本形状は ``gl_ViewportIndex`` の値によって
選択されたビューポート変換と鋏矩形を使用して、
ビューポート変換と鋏検定を行う。
使用されるビューポートインデックスは、シェーディングされる基本形状の頂点の一つに
由来する。
しかし、ビューポートインデックスがどの頂点から来ているかは実装依存であるので、
基本形状の頂点すべてに同じビューポートインデックスを使用するのが得策だ。
幾何シェーダーが ``gl_ViewportIndex`` に値を代入していない場合、
ビューポート変換と鋏矩形 0 が使用される。
幾何シェーダーが ``gl_ViewportIndex`` に値を静的代入し、
シェーダーの中に ``gl_ViewportIndex`` に値を代入しない実行経路がある場合、
そこを通るシェーダーの実行時には ``gl_ViewportIndex`` の値は未定義となる。
詳細については OpenGL 仕様書の 11.3.4.6 "Layer and Viewport Selection" を参照。

7.1.5. Fragment Shader Special Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: コメント

   断片シェーダーで内在的に宣言されている組み込み変数の仕様。
   `コード片 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#>`__

断片シェーダー実行形式の出力は、API パイプラインの後段にある固定機能演算
によって処理される。

断片に対する固定機能で計算された奥行きは ``gl_FragCoord.z`` を読み取ること
で得られる可能性がある。

``gl_FragDepth`` に書き込むと、処理中の断片の奥行き値が確定する。
奥行きバッファリングが有効で、どのシェーダーも ``gl_FragDepth`` を書き込まない場合は、
奥行きの固定関数値が断片の奥行き値として使用される。
シェーダーが ``gl_FragDepth`` に値を静的代入し、シェーダーの中に
``gl_FragDepth`` を設定しない実行経路がある場合、その経路を通るシェーダーの実行では、
断片の奥行きの値が未定義になる可能性がある。
つまり、リンクされた断片シェーダーの集合が
``gl_FragDepth`` への書き込みを静的に含む場合は、常にそれを書き込む責任がある。

シェーダーが ``discard`` キーワードを実行した場合、断片は廃棄され、
ユーザー定義断片出力、
``gl_FragDepth``, ``gl_SampleMask`` の値は意味がなくなる。

変数 ``gl_FragCoord`` は断片シェーダー内からの入力変数として利用でき、
断片のウィンドウ相対座標 ``(x、y、z、1/w)`` の値を保持する。
多重サンプリングの場合、この値は画素内の任意の位置、または断片標本の
一つたり得る。
``centroid`` を使用しても、この値は現在の基本形状の内部に制限されない。
この値は頂点処理後の基本形状を補間して断片を生成する固定機能の結果だ。
``z`` 成分はどのシェーダーも ``gl_FragDepth`` への書き込みを含んでいない場合に、
断片の奥行きに使用されるであろう値だ。
これは、シェーダーが条件付きで ``gl_FragDepth`` を計算するが、
そうでなければ固定機能の断片の奥行きを求める場合のばらつきに役立つ。

断片シェーダーは入力組み込み変数 ``gl_FrontFacing`` にアクセスでき、
その値は断片が正面基本形状に属していれば真となる。
使い方としては、頂点シェーダーや幾何シェーダーで計算された二つの色のうちの
一つを選択することで、両面照光を模倣することができる。

``gl_PointCoord`` の値は点スプライトが有効な場合、点基本形状の中で現在の断片が
どの位置にあるかを示す二次元座標だ。
これらの値は、点全体で 0.0 から 1.0 の範囲にある。
現在の基本形状が点でない場合や、点スプライトが有効でない場合は
``gl_PointCoord`` から読み取られる値は未定義だ。

入力配列 ``gl_SampleMaskIn[]`` と出力配列 ``gl_SampleMask[]`` の両方について、
マスク M の、ここでは ``gl_SampleMaskIn[M]`` または ``gl_SampleMask[M]`` のビット
B は標本 ``32 * M + B`` に対応する。これらの配列は
``ceil(s / 32)`` 個の要素を持つ。
ここで ``s`` は実装で対処されている色標本の最大数だ。

入力変数 ``gl_SampleMaskIn`` は、多重標本ラスタライズ時に断片を生成する
基本形状が被覆する標本の集合を示す。

出力配列 ``gl_SampleMask[]`` は、処理中の断片の標本マスクを設定する。
現在の断片に対する被覆範囲は、被覆範囲マスクと出力の
``gl_SampleMask`` の論理積になる。
この配列は、断片シェーダーの中で、
最大標本数で決まる実装依存の最大標本マスク（32 ビット要素の配列として）よりも
大きくならないようにサイズを暗黙的または明示的に決めなければならない。
断片シェーダーが ``gl_SampleMask`` に値を静的代入する場合、
値の代入に失敗するどのような断片シェーダー呼び出しのどのような配列要素に
ついても標本マスクは未定義となる。
シェーダーが ``gl_SampleMask`` に値を静的代入していない場合、
標本マスクは断片の処理に影響を与えない。

入力変数 ``gl_SampleID`` には現在処理されている標本の標本番号が入る。
この変数は 0 から ``gl_NumSamples - 1`` の範囲にある。ここで
``gl_NumSamples`` はフレームバッファー内の標本の総数であり、
非多重標本フレームバッファーにレンダリングする場合は 1 だ。
断片シェーダーでのこの変数の静的使用は、シェーダー全体が標本ごとに評価
されるようになる。

入力変数 ``gl_SamplePosition`` は、多重標本描画バッファー内の現在の標本の位置を含む。
``gl_SamplePosition`` の ``x`` および ``y`` 成分には、
現在の標本の部分画素座標が含まれており、0.0 から 1.0 の範囲の値を持つ。
断片シェーダーでのこの変数の静的使用は、シェーダー全体が標本ごとに評価
されるようになる。

値 ``gl_HelperInvocation`` は断片シェーダーの呼び出しが補助呼び出し
とみなされる場合は真、そうでない場合は偽になる。
補助呼び出しとは、断片シェーダー非補助呼び出しで使用するための
微分係数を評価する目的でのみ作成された断片シェーダー呼び出しだ。
このような微分係数は、組み込み関数 ``texture()`` で暗黙的に計算され
(:ref:`8.9. Texture Functions`)、
例えば ``dFdx()`` や ``dFdy()`` など、
:ref:`8.14.1. Derivative Functions` の導関数で明示的に計算される。

断片シェーダー補助呼び出しは、非補助呼び出しと同じシェーダー
コードを実行するが、
フレームバッファーや他のシェーダーにアクセス可能なメモリーを修正する副作用はない。
特に：

* 補助呼び出しに対応する断片は、シェーダーの実行が完了すると、
  フレームバッファーを更新することなく破棄される。
* 補助呼び出しによって実行される画像およびバッファー変数への格納は、
  裏方の画像またはバッファーのメモリーに影響を与えない。
* 補助の呼び出しによって実行される、画像、バッファー、不可分計数器変数への
  不可分操作は、裏方の画像、バッファーメモリに影響を与えない。
  このような不可分操作によって返される値は未定義だ。

補助呼び出しは、レンダリングされている基本形状によって被覆されていない画素に
対して生成されることがある。
``centroid`` 修飾された断片シェーダーの入力は、通常、画素と基本形状の
交点で採取される必要があるが、画素と基本形状の間には交点がないため、このような
画素ではその要求は無視される。

補助呼び出しは、断片が早期断片検定（修飾子 ``early_fragment_tests`` を使用）
によって殺されたときにレンダリングされる基本形状が被覆する断片に対して
生成されるかもしれないし、断片シェーダーを実行しても他の断片シェーダー
呼び出しのための導関数の計算を支援する以外の効果がないことを実装が判断できる場合
にも生成される。

基本形状の任意の集合を処理するときに生成される補助呼び出しの集合は実装依存だ。

``gl_ClipDistance`` は、シェーダーが ``gl_ClipDistance`` 出力変数に書き込む
頂点パイプラインの値を線形補間した値を含む。
この配列の中で切り取りが有効になっている要素しか定義された値を持たないことになる。

入力変数 ``gl_PrimitiveID`` には、幾何シェーダーが存在する場合は、
``gl_PrimitiveID`` 幾何シェーダー出力に書き込まれた値が入る。
それ以外の場合は、レンダリング基本形状の現在の集合が開始されてから、
シェーダーによって処理された基本形状の個数で埋められる。

入力変数 ``gl_Layer`` には、幾何シェーダーが存在する場合は、
``gl_Layer`` 幾何シェーダー出力に書き込まれた値が入る。
幾何段階が値を ``gl_Layer`` に動的代入しない場合、
断片段階での ``gl_Layer`` の値は未定義となる。
幾何段階が ``gl_Layer`` に静的代入を行わない場合、
断片段階の入力値は 0 になる。
そうでなければ、断片段階は、幾何段階が書き込んだ値と同じ値を、
その値が範囲外であったとしても読み込む。
断片シェーダーが ``gl_Layer`` への静的アクセスを含む場合、
それは断片段階への入力の最大数に対する実装定義の限界に加味される。

入力変数 ``gl_ViewportIndex`` には、幾何シェーダーが存在する場合には、
幾何段階の出力変数 ``gl_ViewportIndex`` に書き込まれた値が入る。
幾何段階で ``gl_ViewportIndex`` に値を動的代入しない場合は、
断片シェーダーでの ``gl_ViewportIndex`` の値は未定義となる。
幾何段階が ``gl_ViewportIndex`` に静的代入を行わない場合、
断片段階は 0 を読み取る。
そうでなければ、たとえその値が範囲外であったとしても、
断片段階は幾何段階が書き込んだのと同じ値を読み取る。
断片シェーダーが ``gl_ViewportIndex`` への静的アクセスを含む場合、
それは断片段階への入力の最大数に対する実装定義の限界に加味される。

7.1.6. Compute Shader Special Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: コメント

   計算シェーダーで宣言されている組み込み変数の仕様。
   `コード片 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#compute-shader-special-variables>`__

組み込み変数 ``gl_NumWorkGroups`` とは計算シェーダー入力変数であって、
計算シェーダーを実行する dispatch の各次元の作業グループ数を含むものだ。
その内容は DispatchCompute API 入場地点に渡された
``num_groups_x``, ``num_groups_y``, ``num_groups_z`` の各引数が指定する値に等しい。

組み込み定数 ``gl_WorkGroupSize`` は、シェーダーの作業グループサイズを含む計算
シェーダー定数だ。
X, Y, Z 次元における作業グループのサイズは ``x``, ``y``, ``z`` の各成分に格納される。
``gl_WorkGroupSize`` の定数値は、現在のシェーダーに必要な
``local_size_x``, ``local_size_y``, ``local_size_z`` レイアウト修飾子で指定された
ものと一致する。
作業グループ内で共有できるメモリーの配列のサイズを決めるのに使用できるようにする
ためにこれは定数だ。
固定の作業グープサイズを宣言していないシェーダーで、
あるいはそのシェーダーが固定の作業グループサイズを宣言する前に、
``local_size_x``, ``local_size_y``, ``local_size_z`` を使って
``gl_WorkGroupSize`` を使用するとコンパイルエラーとなる。

組み込み変数 ``gl_WorkGroupID`` は、現在の呼び出しが実行されている
作業グループの三次元インデックスを含む計算シェーダーの入力変数だ。
取り得る値は ``DispatchCompute`` に渡された引数の範囲、
すなわち ``(0, 0, 0)`` から
``(gl_NumWorkGroups.x - 1, gl_NumWorkGroups.y - 1, gl_NumWorkGroups.z - 1)``
までだ。

組み込み変数 ``gl_LocalInvocationID`` は、
作業グループ内の現在の作業項目の三次元インデックスを含む計算シェーダーの入力変数だ。
この変数の取り得る値は、作業グループのサイズの範囲、
すなわち ``(0, 0, 0)`` から
``(gl_WorkGroupSize.x - 1, gl_WorkGroupSize.y - 1, gl_WorkGroupSize.z - 1)``
までだ。
``gl_LocalInvocationID`` の使用は、
``local_size_x``, ``local_size_y``, ``local_size_z`` の宣言の前に許される。

組み込み変数 ``gl_GlobalInvocationID`` は、
現在の作業項目の大域インデックスを含む計算シェーダーの入力変数だ。
この値は、現在の ``DispatchCompute`` 呼び出しによって開始されたすべての作業
グループにわたる他のすべての呼び出しからこの呼び出しを一意に識別する。
これは次のように計算される：

.. code:: glsl

   gl_GlobalInvocationID =
       gl_WorkGroupID * gl_WorkGroupSize + gl_LocalInvocationID;

組み込み変数 ``gl_LocalInvocationIndex`` は ``gl_LocalInvocationID`` の
一次元表現を含む計算シェーダーの入力変数だ。これは次のように計算される：

.. code:: glsl

   gl_LocalInvocationIndex =
       gl_LocalInvocationID.z * gl_WorkGroupSize.x * gl_WorkGroupSize.y +
       gl_LocalInvocationID.y * gl_WorkGroupSize.x +
       gl_LocalInvocationID.x;

``gl_LocalInvocationIndex`` の使用は、
``local_size_x``, ``local_size_y``, ``local_size_z`` を宣言する前に許される。

7.1.7. Compatibility Profile Built-In Language Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

互換性プロファイルを使用する場合、GL は頂点および断片のプログラム可能
パイプライン段階に固定機能の動作を供給することができる。
例えば、固定機能の頂点段階とプログラム可能な断片段階を混在させることができる。

後続のプログラム可能シェーダ段階や固定機能の断片段階の入力を指定するために、
次の組み込み頂点、細分化制御、細分化評価、幾何出力変数が利用可能だ。
特定の変数は、対応する断片シェーダーまたは固定パイプラインのいずれかの機能が
その変数またはその変数から派生した状態を使用する場合、書き込まれるべきだ。
それ以外の場合、動作は未定義だ
これらの言語では、出力 ``gl_PerVertex`` ブロックに以下のメンバーが追加されている：

.. code:: glsl

   out gl_PerVertex { // part of the gl_PerVertex block described in 7.1
       // in addition to other gl_PerVertex members...
       vec4  gl_ClipVertex;
       vec4  gl_FrontColor;
       vec4  gl_BackColor;
       vec4  gl_FrontSecondaryColor;
       vec4  gl_BackSecondaryColor;
       vec4  gl_TexCoord[];
       float gl_FogFragCoord;
   };

出力変数 ``gl_ClipVertex`` は、頂点シェーダーと幾何シェーダーが、
ユーザー切り取り平面で使用する座標を書き込む場所を与える。
``gl_ClipDistance`` への書き込みは、ユーザー切り取りのための好ましい方法だ。
プログラムを構成する一連のシェーダーが ``gl_ClipVertex`` と
``gl_ClipDistance`` または ``gl_CullDistance`` の両方を静的に読み書きすることは、
コンパイルエラーまたはリンクエラーとなる。
``gl_ClipVertex`` も ``gl_ClipDistance`` も書き込まれていない場合、それらの値は
未定義であり、ユーザー切り取り平面に対するいかなる切り取りも未定義となる。

前にコアプロファイルについて説明したのと同様に、
``gl_PerVertex`` ブロックをシェーダーで再宣言して、これらの追加メンバーを明示的に
含めることができる。例えば：

.. code:: glsl

   out gl_PerVertex {
       vec4 gl_Position;    // will use gl_Position
       vec4 gl_FrontColor;  // will consume gl_color in the fragment shader
       vec4 gl_BackColor;
       vec4 gl_TexCoord[3]; // 3 elements of gl_TexCoord will be used
   }; // no other aspects of the fixed interface will be used

ユーザーは切り取り頂点とユーザー切り取り平面が同じ座標空間で定義されていることを
間違いなくする必要がある。ユーザー切り取り平面は線形変換のもとでしか適切に動作しない。
非線形変換のもとで何が起こるかは未定義である。

出力変数 ``gl_FrontColor``, ``gl_FrontSecondaryColor``, ``gl_BackColor``,
``gl_BackSecondaryColor`` は、処理される頂点を含む基本形状の正面と背面の一次色と
二次色を代入する。出力変数 ``gl_TexCoord`` は処理される頂点のテクスチャー座標を
代入する。

``gl_FogFragCoord`` の場合、OpenGL 仕様の互換性プロファイルの 16.4 "Fog" の
"c" 値として、固定機能パイプラインで使用されるので、
書き込まれた値が使用される。
例えば、カメラ空間における断片の ``z`` 座標を "c" としたい場合、
それが頂点シェーダーの実行形式が ``gl_FogFragCoord`` に書き込むべき値だ。

すべての配列と同様に、
``gl_TexCoord`` の添字に使用されるインデックスは、定整数式であるか、
またはこの配列がシェーダーによってサイズと一緒に再宣言されなければならない。
このサイズは最大 ``gl_MaxTextureCoords`` にすることができる。
0 に近いインデックスを使用すると、実装が様々な (varying) 資源を保存するのに
役立つかもしれない。
``gl_TexCoord`` の再宣言は、例えば、大域スコープで行うこともできる：

.. code:: glsl

   in vec4 gl_TexCoord[3];
   out vec4 gl_TexCoord[4];

なお、この処理は ``gl_TexCoord[]`` の特殊な場合であり、ブロックのメンバーを再宣言
するための一般的な方法ではない。
``gl_TexCoord[]`` を大域スコープで再宣言すると、対応する組み込みブロックの再宣言
がある場合にはコンパイルエラーとなる。
シェーダー内では一つの形式の再宣言しか認められない
（それゆえ、ブロックの再宣言はそれを使用するすべてのシェーダーに亘って一致
しなければならないため、段階内でも同様だ）。

細分化制御、同評価、幾何シェーダーでは、上述の直前段階の出力は、
これらの言語の入力 ``gl_PerVertex`` ブロックでも利用可能だ。

.. code:: glsl

   in gl_PerVertex { // part of the gl_PerVertex block described in 7.1
       // in addition to other gl_PerVertex members...
       vec4  gl_ClipVertex;
       vec4  gl_FrontColor;
       vec4  gl_BackColor;
       vec4  gl_FrontSecondaryColor;
       vec4  gl_BackSecondaryColor;
       vec4  gl_TexCoord[];
       float gl_FogFragCoord;
   } gl_in[];

これらは、前述の出力ブロック ``gl_PerVertex`` と同様に、
明示的なパイプラインインターフェイスを設置するために再宣言することができ、
入力の再宣言は、直前段階の出力再宣言と一致しなければならない。
ただし、インスタンス名を持つ組み込みインターフェースブロック（
``gl_in`` など）を再宣言する場合は、
再宣言にインスタンス名を含めなければならない。
組み込みインスタンス名を含まない場合や、名前を変更する場合は、
コンパイルエラーとなる。例えば、以下のようになる：

.. code:: glsl

   in gl_PerVertex {
       vec4 gl_ClipVertex;
       vec4 gl_FrontColor;
   } gl_in[]; // must be present and must be "gl_in[]"

サイズとともに宣言済み組み込みブロック配列は、サイズなしの構文で再宣言することができる。
これにより、それらのサイズは元の宣言済みサイズと等しくなる。

``gl_TexCoord[]`` の再宣言の扱いも、出力ブロックの ``gl_TexCoord[]`` の再宣言で
述べたと同じだ。

次の断片入力ブロックは、互換性プロファイルを使用する場合、断片
シェーダーでも使用できる：

.. code:: glsl

   in gl_PerFragment {
       in float gl_FogFragCoord;
       in vec4  gl_TexCoord[];
       in vec4  gl_Color;
       in vec4  gl_SecondaryColor;
   };

``gl_Color`` と ``gl_SecondaryColor`` の値は、断片を生成する基本形状で
どの面が見えているかに基づいて、
``gl_FrontColor``, ``gl_BackColor``, ``gl_FrontSecondaryColor``,
`gl_BackSecondaryColor`` からシステムが自動的に導き出す。
頂点処理に固定機能が使われている場合は、
``gl_FogFragCoord`` は、カメラ空間における断片の ``z`` 座標か、
OpenGL 仕様の互換性プロファイルの 16.4 "Fog" で記述されている霧座標の補間になる。
``gl_TexCoord[]`` の値は、頂点シェーダーからの補間された
``gl_TexCoord[]`` の値か、固定パイプライン基準頂点機能のテクスチャー座標だ。

断片シェーダーの ``gl_TexCoord`` 配列に対するインデックスは、
上記の頂点シェーダーテキストで記述したとおりだ。

入力および出力 ``gl_PerVertex`` ブロックについて上述したように、
``gl_PerFragment`` ブロックは、別のプログラムへの明示的なインターフェイスを作成
するために再宣言することができる。
別々のプログラム間でこれらのインターフェイスを合致させる場合、
``gl_PerVertex`` 出力ブロック内のメンバーは、それらから生成された対応する
断片シェーダーメンバーが ``gl_PerFragment`` 入力ブロック内に存在する場合
かつその場合に限り、宣言されなければならない。
これらの合致については、OpenGL 仕様書 7.4.1 "Shader Interface Matching" で詳しく
説明されている。
プログラム内でこれらが一致しない場合、リンクエラー。
不一致が二つのプログラム間にある場合、プログラム間で渡される値は未定義となる。
他のすべてのブロックマッチングとは異なり、
``gl_PerFragment`` 内の宣言の順番はシェーダー間で一致する必要はなく、
一致する ``gl_PerVertex`` の再宣言の宣言の順番と一致する必要もない。

互換性プロファイルを使用する場合、以下の断片出力変数が断片
シェーダーで使用できる：

.. code:: glsl

   out vec4 gl_FragColor;
   out vec4 gl_FragData[gl_MaxDrawBuffers];

``gl_FragColor`` に書き込むと、後続の固定機能パイプラインで使用される断片
色を指定する。
後続の固定機能が断片色を消費し、断片シェーダー実行形式の実行時に
``gl_FragColor`` に値を書き込まなかった場合、消費される断片色は未定義だ。

変数 ``gl_FragData`` は配列だ。
``gl_FragData[n]`` へ書き込むと、後続の固定機能パイプラインがデータ ``n`` に対して
使用する断片データを指定する。
後続の固定機能が断片データを消費し、断片シェーダー実行形式の
実行がその値を書き込まない場合、消費される断片データは未定義だ。

シェーダーが ``gl_FragColor`` に値を静的代入する場合、
``gl_FragData`` のどの要素にも値を代入してはならない。
シェーダーが ``gl_FragData`` の任意の要素に値を静的に書き込む場合、
``gl_FragColor`` に値を代入してはならない。
つまり、シェーダーは ``gl_FragColor`` と ``gl_FragData`` のどちらか一方にしか
値を代入することができない。両方に代入することはできない。
また、リンクされている複数のシェーダーも、一貫してこれらの変数をただ一つ
書かなければならない。
同様に、ユーザー宣言された出力変数が使用された（静的代入された）場合には、
組み込み変数 ``gl_FragColor`` と ``gl_FragData`` に代入してはいけない。
これらの不正な使用方法は、いずれもコンパイルエラーまたはリンクエラーとなる。

シェーダーが ``discard`` キーワードを実行した場合、断片は廃棄され、
``gl_FragDepth`` と ``gl_FragColor`` の値は無意味になる。

7.2. Compatibility Profile Vertex Shader Built-In Inputs
----------------------------------------------------------------------

以下の宣言済み入力名は、互換性プロファイルを使用する際に、
頂点シェーダーから OpenGL 状態の現在の値にアクセスするために使用できる：

.. admonition:: コメント

   `コード片 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#compatibility-profile-vertex-shader-built-in-inputs>`__

7.3. Built-In Constants
----------------------------------------------------------------------

以下の組み込み定数は、すべてのシェーダーで宣言されている。
実際に使用される値は実装依存だが、少なくとも示された値はなければならない：

.. admonition:: コメント

   `コード片 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#built-in-constants>`__

定数 ``gl_MaxVaryingFloats`` はコアプロファイルで削除された。
代わりに ``gl_MaxVaryingComponents`` を使用する。

7.3.1. Compatibility Profile Built-In Constants
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: コメント

   `コード片 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#compatibility-profile-built-in-constants>`__

7.4. Built-In Uniform State
----------------------------------------------------------------------

SPIR-V を生成する際、組み込み一様状態は利用できない。
その他、OpenGL 処理状態にアクセスするための支援として、
以下の一様変数が OpenGL Shading Language に組み込まれている：

.. admonition:: コメント

   `コード片 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#built-in-uniform-state>`__

これらの変数は、断片段階でのみ利用可能であることが保証されている。
他の段階では、その存在と機能は実装定義だ。

7.4.1. Compatibility Profile State
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

これらの変数は、互換性プロファイルにしか存在しない。
計算シェーダー以外のシェーダーで使用できる。

.. admonition:: コメント

   `コード片 <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html#compatibility-profile-state>`__

7.5. Redeclaring Built-In Blocks
----------------------------------------------------------------------

``gl_PerVertex`` ブロックをシェーダー内で再宣言することで、
固定パイプラインインターフェイスのどの部分集合を使用するかを明示的に示すことができる。
これは複数のプログラム間のインターフェイスを設定するために必要だ。
例えば、以下のようになる：

.. code:: glsl

   out gl_PerVertex {
       vec4 gl_Position;   // will use gl_Position
       float gl_PointSize; // will use gl_PointSize
       vec4 t;             // error, only gl_PerVertex members allowed
   }; // no other members of gl_PerVertex will be used

これはシェーダーが後続のパイプライン段階で使用する出力インターフェイスを設定する。
これは ``gl_PerVertex`` の組み込みメンバーの部分集合でなければならない。
このような再宣言では、不変修飾子、補間修飾子、レイアウト修飾子
``xfb_offset``, ``xfb_buffer``, ``xfb_stride`` を追加することができる。
また、サイズなし配列に対しては、配列のサイズを追加することもできる。
例えば、以下のようになる：

.. code:: glsl

   out layout(xfb_buffer = 1, xfb_stride = 16) gl_PerVertex {
       vec4 gl_Position;
       layout(xfb_offset = 0) float gl_ClipDistance[4];
   };

``location`` のような他のレイアウト修飾子は、特に明記されていない限り、
このような再宣言に追加することはできない。

組み込みインターフェイスブロックを再宣言する場合は、
組み込み宣言に含まれるメンバーを使用する前にシェーダに現れなければならず、
そうでない場合はコンパイルエラーとなる。
ブロックを二度以上再宣言したり、組み込みブロックを再宣言した後に
再宣言に含まれていない組み込みブロックのメンバーを使用することもコンパイルエラー
になる。
また、組み込みインターフェイスブロックが再宣言された場合、
ブロックの再宣言の外側で組み込み宣言のメンバーを再宣言することはできない。
同じインターフェイスに属する組み込みブロックのメンバーを使用する複数のシェーダー
が同一プログラム内でリンクされている場合、
すべてのシェーダーが同じ方法で組み込みブロックを再宣言しなければ、リンクエラーとなる
(:ref:`4.3.9. Interface Blocks`)。
また、あるプログラム内のシェーダーが特定の組み込みインターフェイスブロックを
再宣言しているにもかかわらず、
そのプログラム内の別のシェーダーがそのインターフェイスブロックを再宣言していない
にもかかわらず、
そのインターフェイスブロックのメンバーを使用している場合も、リンクエラーとなる。
組込みインターフェイスが異なるプログラムのシェーダー間に形成されている場合、
シェーダーはすべて同じ方法で（単一のプログラムについて記述されたように）
組込みブロックを再宣言しなければ、インターフェイスに沿って渡される値は未定義となる。
