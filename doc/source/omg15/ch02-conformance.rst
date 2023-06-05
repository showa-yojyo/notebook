======================================================================
2 Conformance
======================================================================

UML を扱うツールがあるとして、その性質がどれほど良いかを規定する章と考えられる。

   There are five distinct types of conformance. These are listed below. Unless
   otherwise stated these types of conformance are independent.

先に適合性を一覧する：

#. Abstract syntax conformance
#. Concrete syntax conformance
#. Model interchange conformance
#. Diagram interchange conformance
#. Semantic conformance

:dfn:`Abstract syntax conformance` があるツールとは、次の二点を備えるものとす
る：

* UML メタクラスのインスタンスを作成、読み取り、更新、削除できる UI and/or API
* UML メタモデルで定義された制約に対応するモデルの整形性を検証する方法

:dfn:`Concrete syntax conformance` があるツールとは、上記の具体版だ。さらに、UML
で定義されていない追加的な図式や表記要素を作成、読み取り、更新、削除する機能を提
供しても構わない：

* UML 記法のインスタンスを作成、読み取り、更新、および削除できる UI and/or API

:dfn:`Model interchange conformance` があるツールとは、プロファイルが定義または
適用されたモデルを含む、すべての有効な UML モデルに対して、適合した :abbr:`XMI`
をインポートおよびエクスポートできるものだ。この適合性は、上述の abstract syntax
conformance を含意する。適合する UML 2.5 ツールは、UML 2.5 形式だけでなく、UML
2.4.1 形式の:abbr:`XMI` を読み書きできなければならない
(:doc:`./ane-serialization`)。

:dfn:`Diagram interchange conformance` のあるツールとは、図式を含む有効な UML モ
デルすべて（プロファイルが定義・適用されたモデルを含む）について、適合した
:abbr:`DI` (:doc:`./anb-interchange`) をインポートおよびエクスポートが可能なもの
だ。当適合性は concrete syntax conformance と model interchange conformance の双
方を含意する。

:dfn:`Semantic conformance` とは、コード生成、モデル実行、意味論的モデル分析な
ど、UMLの意味論を解釈するための実証的な方法を備えているという性質だ。これも
abstract syntax conformance を含意する。

   Where the UML specification provides options for a conforming tool, these are
   explicitly stated in the specification. In a number of other cases, certain
   aspects of the semantics are listed as "undefined" or “intentionally not
   specified” or “not specified”, allowing for domain- or application-specific
   customizations.

この規則が仕様に記載のない事柄についての判断基準となる。

   This specification comprises this document together with XMI serialization
   contained in machine-consumable files as listed on the cover page. If there
   are any conflicts between this document and the machine-consumable files, the
   machine-consumable files take precedence.

この仕様書は一部がどう見ても機械生成によるものなのだが、そのことと関係がある。
