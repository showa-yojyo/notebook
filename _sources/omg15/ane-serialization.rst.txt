======================================================================
Annex E: XMI Serialization and Schema
======================================================================

.. contents::
   :depth: 2

E.1 Summary
======================================================================

   UML 2 models are serialized in XMI 2 according to the rules specified by the
   MOF 2 XMI Mapping Specification.

OMG の一般的な方針として、MOF_ 2 および UML 2 モデルの規範的な表現は :abbr:`XMI`
ファイルだ。UML 2 自体の規範的な :abbr:`XMI` 文書は一つの :abbr:`XMI` 文書で構成
されている。

関連する :abbr:`XMI` 文書として、StandardProfile と UML Diagram Interchange モデ
ルがある。UML 2 が依存し、他の仕様が依存する可能性のある PrimitiveTypes は別の
:abbr:`XMI` 文書で規定されている。

.. admonition:: 読者ノート

   :abbr:`XMI` について言及がある章をチェックしておく。リンク切れのところが怪し
   い。

   * :doc:`./ch02-conformance`
   * :doc:`./ch03-normative`
   * :doc:`./ch12-packages`

E.2 XMI Serialization of the UML 2 metamodel
======================================================================

:abbr:`XMI` を使用して生成されるスキーマや文書をタグを使用して調整することが
:abbr:`XMI` では可能だ。UML 2 モデルの :abbr:`XMI` 交換に対する UML 2 メタモデル
に表示されるタグ設定は次のとおり：

* タグ ``org.omg.xmi.nsPrefix`` を ``uml`` に設定

他に明示的に設定されているタグはない。すなわち MOF 2 XMI Mappings Specification
で文書化されている既定値を仮定する。

UML 2.5 のメタモデル要素に対する ``xmi:ids`` は、UML 2.4.1 と UML 2.5 の間で名前
が変更された関連や特性に対応する ``ids`` を除き、UML 2.4.1 と同等の要素と同じ
だ。

   The metaclasses and associations in UML 2.5 are organized in a package
   structure that corresponds to the specification clause structure. All of
   these packages are imported into the top-level UML package, so that all
   metamodel elements can be referred to unqualified in the top-level package.

UML 2.4.1 からメタモデルになされた変更点：

* 上述のパッケージ体系
* StandardProfileL2 と StandardProfileL3 を単体の StandardProfile へ統合
* 既定値を表現するために多重度の下限値（をゼロとする）緩和
* 意味を明確にするため、いくつかの特性へ順序を導入
* 関連所有特性と対応する関連の名前を一部変更
* ``NamedElement::clientDependency`` の導出
* LoopNodes をその ``loopVariables`` の所有者と同一視する。その結果、UML 2.5 と
  UML 2.4.1 モデルファイルはバージョン番号を置き換えることで次をおいては交換可能
  となる：

  * LoopNodes の ``loopVariables``
  * Dependencies の ``clients`` である NamedElements で、UML 2.4.1 では
    ``clientDependency`` を含もうとした。
  * StandardProfile への参照

LoopNodes は別として、UML 2.4.1 ではバージョン番号が 20110701 へ戻るように編集さ
れ、Dependencies の ``clients`` である NamedElements のすべてに
``clientDependency`` 属性が挿入されていれば、UML 2.4.1 ツールは UML 2.5 モデルを
表現する XMI を読み込むだろう。さらに、UML 2.5 モデルの中に StandardProfile への
参照がある場合は、

* ``http://www.omg.org/spec/UML/20110701/StandardProfileL2``
* ``http://www.omg.org/spec/UML/20110701/StandardProfileL3``

のどちらか、または両方への参照を代わりに使用する必要がある。

UML 2.5 適合ツールは UML 2.5 または UML 2.4.1 モデルのどちらも読み込むことも保存
することも可能であるものとする。

UML 2.5 ではより多くの OCL_ 制約が成文化したので、UML 2.4.1 ツールで検証されたモ
デルが UML 2.5 で検証されない場合がある。

E.3 XMI Serialization of the PrimitiveTypes model library
======================================================================

次に記すものは PrimitiveTypes モデルライブラリーで、そのライブラリーを直接的また
は間接的にインポートするモデルの :abbr:`XMI` 交換に表示されるタグ設定だ：

* タグ ``org.omg.xmi.nsPrefix`` を ``primitives`` に設定
* ``PrimitiveTypes::Boolean`` にはタグ ``org.omg.xmi.schemaType`` を
  ``http://www.w3.org/2001/XMLSchema#boolean`` に設定
* ``PrimitiveTypes::Integer`` にはタグ ``org.omg.xmi.schemaType`` を
  ``http://www.w3.org/2001/XMLSchema#integer`` に設定
* ``PrimitiveTypes::Real`` にはタグ ``org.omg.xmi.schemaType`` を
  ``http://www.w3.org/2001/XMLSchema#double`` に設定
* ``PrimitiveTypes::String`` にはタグ ``org.omg.xmi.schemaType`` を
  ``http://www.w3.org/2001/XMLSchema#string`` に設定
* ``PrimitiveTypes::UnlimitedNatural`` にはタグ ``org.omg.xmi.schemaType`` を
  ``http://www.w3.org/2001/XMLSchema#string`` に設定

表記が ``*`` である UnlimitedNatural の制限なし値は ``*`` としてシリアライズされ
るものとし、それに対して UnlimitedNatural の数値はすべて、整数としての数値の文字
列表現としてシリアライズされるものとする。

E.4 XMI Serialization of the StandardProfile
======================================================================

次に記すものは StandardProfile プロファイルで、そのプロファイルを直接的にまたは
間接的にインポートするモデルの :abbr:`XMI` 交換に現れるタグ設定だ：

* タグ ``org.omg.xmi.nsPrefix`` を ``StandardProfile`` に設定

E.5 XMI Serialization of the UMLDI
======================================================================

次に記すものはモデル図式の :abbr:`XMI` 交換に対する UMLDI メタモデル拡張に現れる
タグ設定だ：

* タグ ``org.omg.xmi.nsPrefix`` を ``umldi`` に設定

.. include:: /_include/uml-refs.txt
