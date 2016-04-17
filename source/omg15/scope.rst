======================================================================
最初の数章
======================================================================
UML 2.5 の最初の数章に関するノート。

.. contents:: ノート目次

1 Scope
======================================================================
* この仕様書は UML revision 2 についてのものである。
* UML の目的は <to provide system architects, software engineers,
  and software developers with tools for analysis, design, and implementation of
  software-based systems as well as for modeling business and similar processes>(p. 1)
  である。

* UML の初期バージョンの成立について簡単に述べられている。
  Booch_, OMT_, OOSE_ という有力なオブジェクト指向手法に加え、
  モデリング言語設計、オブジェクト指向プログラミング、建築用記述言語からの
  いくらかの best practices を取り込んだものがその起源のようだ。

* 異なるモデリングツール同士の情報のやりとりを可能にするべく、
  モデリング言語の意味 (semantics) と構文 (syntax) の統一化・仕様化が必要となる、
  という議論。

* MOF_ ベースの何とかという文言が出てくるが、これはこれで別個の仕様が存在している。

2 Conformance
======================================================================
ここはそれほど真剣に読み込む必要はないだろう。

準拠の種類には次の 5 種類がある。断りのない限りこれらの種類は独立している。

#. Abstract syntax conformance
#. Concrete syntax conformance
#. Model interchange conformance
#. Diagram interchange conformance

   * Diagram interchange conformance は暗に
     Concrete syntax conformance と
     Model interchange conformance の両方でもある。

#. Semantic conformance

   * Semantic conformance は暗に abstract syntax conformance でもある。

3 Normative References
======================================================================
パラグラフ一個だけからなる短い章。

ISO/IEC Directives, Part 2, Rules for the structure and drafting of International Standards, Sixth Edition 2011
  これだけリンクがないが、次のページから文書にアクセスできる。
  `Directives and Policies <http://www.iso.org/iso/standards_development/processes_and_procedures/iso_iec_directives_and_iso_supplement.htm>`_

  PDF で 72 ページ程度の文書。仕様書の規約に関する仕様と思われる。

OMG Object Constraint Language (OCL_) 2.3.1 Specification
  2009 年の文書。

OMG Meta Object Facility (MOF_) Core 2.5 Specification
  2005 年の文書。

OMG XML Metadata Interchange (XMI) 2.5 Specification
  リンク切れ。

OMG Diagram Definition (DD) 1.1 Specification
  リンク切れ。

4 Terns and Definitions
======================================================================
一行からなるパラグラフ一個からなる章。大したことは書いていない。
というより、意味がわからない。

5 Notational Conventions
======================================================================
主に 2 点の注意事項が述べられている。

5.1 Key words for Requirement Statements
----------------------------------------------------------------------
キーワードというか、いくつかの英語の助動詞が本仕様書中に現われているとき、
それを前述した ISO/IEC Directives, Part 2 の Annex H に従って解釈するものとする。
そのような一文が書かれている。

この英文法に関する知識は他の言語仕様書を読み込むときにも潰しが効くので、
私の読書ノートとしては異例なのだが、別の仕様書の当該部分をここに抜粋しておく。

SHALL
  「必要」「必須」の意味に解釈する。

  * is to
  * is required to
  * it is required that
  * has to
  * etc.

SHALL NOT
  「禁止」の意味に解釈する。

  * is not allowed/permitted/acceptable/permissible
  * is required to be not
  * is required that ... be not
  * is not to be

SHOULD
  「～するのがよい」の意味に解釈する。

  * it is recommended that
  * ought to

SHOULD NOT
  「～しないほうがよい」の意味に解釈する。

  * it is not recommended that
  * ought not to

MAY
  「許可」の意味に解釈する。
  「可能」の意味に解釈しない。

  * is allowed/permitted/permissible

NEED NOT
  「～を必要とはしない」の意味か。

  * it is not required that
  * no ... is required

CAN
  「能力がある」の意味に解釈する。

  * be able to
  * it is possible to
  * etc.

CANNOT
  「能力がない」の意味に解釈する。

  * be unable to
  * it is not possible to
  * etc.

5.2 Annotations on Example Diagrams
----------------------------------------------------------------------
本仕様書中にある図の見本が説明用の注釈を含むものがある。
これらを UML 図の一部と混同せぬこと。
注釈用のテキストや矢印については UML 図の境界の外側に記すようにしてあるし、
赤色で描画してある。

.. _Booch: https://en.wikipedia.org/wiki/Booch_method
.. _OMT: https://en.wikipedia.org/wiki/Object-modeling_technique
.. _OOSE: https://en.wikipedia.org/wiki/Object-oriented_software_engineering
.. _OCL: http://www.omg.org/spec/OCL/2.3.1
.. _MOF: http://www.omg.org/spec/MOF/2.5
