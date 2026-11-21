======================================================================
1 Scope
======================================================================

UML 2.5 の最初のページはこの仕様の適用範囲を規定するものだ。本仕様書の記念すべき
最初のパラグラフは次だ：

   This specification defines the Unified Modeling Language (UML), revision 2.
   The objective of UML is to provide system architects, software engineers, and
   software developers with tools for analysis, design, and implementation of
   software-based systems as well as for modeling business and similar
   processes.

目的を述べた後、UML の初版の成立について簡単に述べられている。Booch_, OMT_,
OOSE_ という有力なオブジェクト指向手法に加え、モデリング言語設計、オブジェクト指
向プログラミング、建築用記述言語からのいくらかの best practices を取り込んだもの
がその起源のようだ。UML 2 では何が変わったのか：

   Relative to UML 1, this revision of UML has been enhanced with significantly
   more precise definitions of its abstract syntax rules and semantics, a more
   modular language structure, and a greatly improved capability for modeling
   large-scale systems.

1. 抽象的な文法や意味論をより正確に定義
2. 言語構造をさらにモジュール化
3. 大規模システムのモデリング能力を大幅に向上

UML の主要な目標の一つに、ビジュアルモデリングツールの相互運用を可能にするという
のがある。

   However, to enable meaningful exchange of model information between tools,
   agreement on semantics and syntax is required.

そのためには UML が次の要件を満たすとある：

* 普通の MOF_ に基づくメタモデルから作った正式な定義であること。
* UML モデリング概念の意味を詳細に説明するものであること。
* モデリング概念を表現する記法要素の仕様であること。

MOF_ というのは、これ単品で仕様が存在する。

.. include:: /_include/uml-refs.txt
