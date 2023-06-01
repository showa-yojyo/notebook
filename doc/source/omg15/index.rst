======================================================================
Unified Modeling Language 2.5 読書ノート
======================================================================

`OMG Unified Modeling Language Version 2.5 <http://www.omg.org/spec/UML/2.5>`_
を時間を書けても構わないので読み込み、ここにノートを残していく。

ノートの対象は章で言えば 1 章から 22 章および付録の A 章から E 章までに相当す
る。ちなみに本文では私が章と呼ぶ物を clause と呼んでいる。 1 章から数章は短い内
容が続くので単一の reST/HTML ファイルにノートをまとめるが、それ以降は基本的には
一章当たり一個のファイルを割り当てる予定でいる。本格的に UML の仕様を記述する 7
章から 22 章はそれぞれに専用のファイルを割り当てる予定だ。もっとも中盤付近に一章
の内容としては情報量がたいへん多いものがいくつかあるので、そこは分割することを考
えるかもしれない。

.. note::

   この仕様書は市販の書籍ではないので、他では記載することにしている対象書籍に付
   随する著者、出版社、ISBN 等の情報を省く。

.. toctree::
   :maxdepth: 2

   ch01-scope
   ch06-additional-information
   ch07-common-structure
   ch08-values
   ch09-classification
   ch10-simple-classifiers
   ch11-structured-classifiers
   ch12-packages
   ch13-common-behavior
   ch14-statemachines
   ch15-activities
   ch16-actions
   ch17-interactions
   ch18-usecases
   ch19-deployments
   ch20-informationflows
   ch21-primitive-types
   ch22-standard-profile
   ana-diagrams
   anb-interchange
   anc-keywords
   and-tabular-notation
   ane-serialization

.. todo::

   誤訳や変な解釈がいかにもありそうなので、発覚次第修正する。

.. note::

   訳語検討。個人的に訳すのが厳しい、訳したくない、訳に納得していない英単語集。

   * activity (n.) 他にも良さそうなのはあるが、active (adj.) を「活性」とする都
     合もあり、「活動」にしておく。
   * across the edge: 「エッジの端から端まで」の意。「横切る」などではない。
   * automaton (n.) ここはそのままカタカナで。「状態機械」は state machine に使
     いたい。原文では複数形の automata で記されていたとしてもここでは「オートマ
     トン」と書くかもしれない。
   * behavior (n.) 「振る舞い」「挙動」「行動」を気まぐれに使い分ける。字数を費
     やしたくない都合上、「挙動」を多用する。
   * component profile (n.)
   * concurrent (adj.) 本文中にあるように、必ずしも「同時に起こる」とは限らな
     い。
   * configuration (n.) ここでは「配置」とする。
   * context (n.)「文脈」を避けたい場合は「前後」「状況」「背景」「脈絡」など？
   * coregion (n.) codomain のようなものだろう。
   * critical region (n.) 「危急区域」とする。誰もこんな訳語は使っていない。
   * deliverables (n.) これは artifacts と同義かもしれない。
   * emergent (adj.) 「不意に起こる」ぐらいの意味のはず。
   * enter (v.) 入場する。
   * exit (v.) 退場する。
   * event (n.) ふつうは「イベント」とするが、当ノートでは実験的に「事象」で統一
     してみる。イベントプールが事象プールになるが、気にしない。
   * flow (n.) 「流れ」「流動」で済ませたい。
   * guard (n.) 「防御」にしておくが、しっくりこない。
   * interleave (v.) 「交互に配置する」で我慢する。
   * invoke (v.), etc. 「発動する」とした。「呼び出す」で十分伝わるかもしれな
     い。
   * lifeline (n.) 某文書では「生存線」という用語を採用しているようなので拝借す
     る。
   * occurrence(s) (n.) これは instance(s) の Event 版と言える。「出来事」か「発
     生」か気分次第。
   * offer (v.) 語源は「～の方へ運ぶ」を意味するラテン語らしいのだが、まさにこの
     文脈に相応しい。

     * 本文を読み返したら 11.3.3.1 節の第 2 パラグラフに provides (offers) と書
       いてあったので、やはり provide と同じように訳すのが良いだろう。ということ
       は、やはり訳しづらい単語であることには変わりないということだが。

   * open end (n.) 違うと思うが「開放端」にしておく。
   * operand (n.) 「演算子 (operator) が作用する対象」を意味する英単語だ。しか
     し、本文を読むと operator が演算子であるように感じられない。意味がやや限定
     されている。 「演算」よりは「作用」に寄っている感じがするので、 「被演算
     子」よりは「作用対象」のほうが訳語としてましと思われる。そうすると operator
     も「作用素」にしたくなるところだが、少しは検討してから変えるかどうか決め
     る。
   * orthogonal (adj.) 「直交の」だが、たいていの場合、幾何学的な意味あいでとは
     限らない。
   * protocol (n.) 通信等の手順。「約束によって成り立っている規則」くらいの意味
     だろう。辞書には儀礼とか典礼ともあり、むしろここではこれらが相応しい？
   * partial ordering (n.) 「半順序」とする。集合論の教科書で現れる用語と同じも
     のだろう。
   * qualifier value (n.)
     何かを限定する値の意だとは思う。
     C++ だと ``const`` や ``volatile`` を qualifier と言うのだが、
     ここでは忘れてよい。
   * reduce (v.) 数学とかプログラミングとかでよくある状況での用法での訳。
     ここでは「縮合する」と訳しておく。
   * region (n.) 「領域」「区域」など。
   * streaming (n.) これはどうしよう。
   * submachine (n.) 「部分機械」と機械的に訳すことにする。
   * substate (n.) 「部分状態」。
   * successor (n.) 「後者」としておく。
     ペアノの公理での successor と単語の使われ方が似ているから。
   * tool (n.) なぜだか「道具」や「器具」ではしっくりと来ない。
   * trace (n.) 「跡」「足跡」「痕跡」「形跡」「線」「記録」など。
   * trigger (n.) 普通はカタカナで「トリガー」とするのが一般的だが、実験的に「引
     き金」や、踏み込んで「撃鉄」なども採用する。何かの引き金になる、何かのきっ
     かけになる、何かを誘発する、等々。
   * token (n.) 「トークン」とする。代用硬貨とかではさすがに意味が通らないが、本
     質的な意味はまさにそれ。
   * unmarshal (v.) のスペリングに注意。
     仕様書では最後の l をどんな場合でも重ねるが、
     辞書によると不定詞では l は一個しかない。
   * workflow (n.) 「仕事の流れ」としたが、おそらく不適当。
