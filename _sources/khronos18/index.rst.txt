======================================================================
OpenGL Shading Language 4.60 Specification 読書ノート
======================================================================

`OpenGL Shading Language 4.60 Specification (July 10, 2019) <https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.4.60.html>`__
を読んでいく。

.. toctree::
   :maxdepth: 3
   :glob:

   note*

.. note::

   * 当ノートでは仕様書の文章と個人的な感想、確認メモなどを交えて記す。
     他人が参考にするような文書とはならない。
   * 専門用語の和訳・定訳がわからないものについては、調べ方がわからないので、
     今のところ好きに表している。そのうち修正したい。

.. admonition:: Copyright © 2008-2018 The Khronos Group Inc. All Rights Reserved.

   本仕様書は、著作権法により保護されており、Khronos Group, Inc. が所有する資料を含む。

   本仕様書またはその構成要素は、Khronos Group の書面による明示的な事前許可なしに、
   いかなる方法でも複製、再発行、配布、送信、表示、放送、またはその他の方法で利用することは許されない。

   ここに記載されている機能を実装するために、本仕様書に記載されている商標、著作権、その他の通知を
   変更または削除することなく使用することができるが、
   本仕様書を受領または所有しても、その内容を複製、開示、配布する権利や、
   本仕様書に記載されているものを全部または一部を製造、使用、販売する権利を付与するものではない。

   Khronos Group は、Khronos の現在の後援者、寄稿者、または
   採用者のメンバーに対し、本仕様書の費用が発生せず、可能な限りあらゆる
   バージョンの API について利用可能な最新の仕様書を使用することを条件に、
   本仕様書の変更されていないバージョンをいかなる方法でもコピーおよび再配布することを明示的に許可する。
   配布された仕様書は、仕様書の内容に変更がない限り、文書形式を変更することができる。
   本仕様書は、販売者が独自に開発した重要な作品が含まれている限り、
   販売される製品に組み込むことができる。
   本仕様書を配布する際には、可能な限り Khronos Group のウェブサイトにある
   本仕様書の最新版へのリンクを含めるべきだ。

   Khronos Group は、本仕様書に関して、明示的にも黙示的にも、商品性、特定目的への適合性、
   知的財産権の非侵害に関する黙示的な保証を含むがこれに限定されない、
   いかなる表明も保証も行わず、また明示的にも放棄するものとする。
   Khronos Group は、本仕様書の正確さ、完全性、適時性、および信頼性に関して、
   明示的にも黙示的にもいかなる保証も行わず、明示的にも放棄する。
   いかなる状況においても、Khronos Group、その後援者、寄稿者、
   構成員、またはそれぞれの相棒、役員、取締役、従業員、代理人、または代表者は、
   これらの資料に起因または関連して生じた、直接的、間接的、特別、または収益の損失、
   利益の損失などの結果的な損害について責任を負わない。

   Khronos, Vulkan, SYCL, SPIR, WebGL, EGL, COLLADA, StreamInput, OpenVX,
   OpenKCam, glTF, OpenKODE, OpenVG, OpenWF, OpenSL ES, OpenMAX, OpenMAX AL,
   OpenMAX IL, OpenMAX DL は Khronos Group Inc. の商標であり、
   WebCL は Khronos Group Inc. の認証商標だ。
   OpenCL は Apple Inc. の商標であり、
   OpenGL および OpenML は Apple Inc. の登録商標、
   OpenGL ES および OpenGL SC ロゴ は Silicon Graphics International
   の商標であり、Khronos 社の許諾に基づき使用されている。
   その他の製品名、商標、および会社名は、識別のためにのみ使用されており、
   それぞれの所有者に帰属する。

.. note::

   原文の英語を、次のように単語を日本語に（機械的に）読み換える：

   * advertised: 公表された、公称された
   * aggregate: 集約、集約型
   * argument: （実）引数
   * atomic: 不可分～
   * barrier: 障壁
   * binary: 二進数、二項～
   * bind, binding: 束縛する、束縛～
   * built-in: 組み込み
   * capture: 捕捉
   * clip: 切り抜く
   * coherent: 密着
   * component: 成分（数学から）
   * composite: 合成～（数学から）
   * compute: (n) 計算
   * counter: 計数器
   * cull: 間引く（この訳はよくない）
   * default: 既定の
   * depth: 奥行き（深度とはしない）
   * dereference: 逆参照する（C++ 本から）
   * dimension: 次元（数学から）、寸法
   * directive: 指令（文）
   * executable: 実行形式
   * expression: 式（プログラミングから）
   * extension: 拡張
   * feedback: 反響
   * fence: 柵
   * fog: 霧
   * formal parameter: 仮引数
   * fragment: 断片（ピクセルの最終データを計算するために使用される状態の集合）
   * geometry: 幾何～（一律にこう訳す）
   * global: 大域～（C++ から）
   * image: 画像
   * integral: 整数～
   * local: 局所～（数学から）
   * location: 位置（場所になっていたら置換漏れ）
   * lookup: 検索（もっといいのはないか？）
   * match: 一致、合致
   * memory: 記憶（機械的には置換不可）
   * opaque: 不透明～
   * packed: 充満
   * pair: （一）対
   * parameter: 引数
   * pixel: 画素
   * primitive: 基本形状（三角形、線、点などの基本的な描画形状の総称だろう）
   * processor: 処理器
   * programmable: プログラム可能～
   * qualifier: 修飾子
   * query: 問い合わせる
   * resource: 資源
   * rule: 規則
   * runtime: 実行時
   * sample: 標本、採取
   * sampler: 採取器
   * set: 集合（数学から）
   * signed: 符号あり～
   * space: 空間（機械的にこの訳で固定する）
   * stage: 段階
   * statement: 文（プログラミングから）
   * stencil: 型抜き
   * storage: 格納、収納（する場所・空間）
   * subset: 部分集合（数学から）
   * superset: 超集合（数学から）
   * tessellation: 細分化（OpenGL Wiki の当該記述を意識して仕様書を読んでいる）
   * test: 検査、検定、判定。場合によって訳を分ける。
   * type: 型（種類とすることがまれ）
   * unary: 単項～
   * undefined: 未定義（機械的にこの訳で固定する）
   * unpack: 分解
   * uniform: 一様（数学から）
   * unit: 構成単位、～単位
   * varying: TODO
   * vertex: 頂点（数学から）
   * volume: TODO

   その他、定訳がなかったり、カタカナ表記でないと逆にわかりにくいような単語
   (access, active, address, alignment, algorithm, application, assembler
   back up, bit, block, byte, buffer,
   category, clamp, client, code, comment, compile, constructor, context,
   data, decrement, driver, dynamic range,
   error,
   file, filter, flow, font, format, framebuffer,
   graphics, group,
   handle, hardware, increment, index, instance, inteface,
   jump, keyword,
   label, layout, library, link, list, literal, load, loop,
   macro, mask, matching, member, memory, mipmap, mode,
   noise,
   object, offset, operand, option, overflow,
   patch, pattern, pipeline, platform, pragma, profile, program, prototype,
   provoking vertex, push,
   rasterize, render,
   scalar, scope, screen, shader, size, source, stream, subpass, subroutine,
   texel, text, texture, token, transaction,
   underflow, user, vector, version,
   window, etc.)
   についてはカタカナ表記という手抜きをする。
