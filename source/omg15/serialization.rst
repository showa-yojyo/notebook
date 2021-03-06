======================================================================
Annex E: XMI Serialization and Schema
======================================================================
UML 2.5 pp. 751-752 に関するノート。
これは別に読まなくてもよかったのではないか。

.. contents:: ノート目次

E.1 Summary
======================================================================
* UML 2 モデルは
  MOF 2 XMI Mapping Specification により仕様化された規則に従う
  XMI 2 でシリアライズする。

* OMG にとって共通の方針である、
  MOF 2 および UML 2 の規範的表現法は XMI ファイルである。

E.2 XMI Serialization of the UML 2 metamodel
======================================================================
* XMI はタグの使用法に
  作り出されたスキーマと XMI を使って作り出された文書とを
  調整することを許可する。

* 他に明示的にセットされているタグはないのだが、
  MOF 2 XMI Mappings Specification で文書化されているように
  それらがデフォルト値を仮定することを意味する。

* UML 2.5 のメタモデル要素のための ``xmi:ids`` は、
  UML 2.4.1 と UML 2.5 の間で変更された名前の
  関連と特性に対応する ``ids`` は除いて、
  UML 2.4.1 の等価な要素のためのものと同じである。

* 2.4.1 からメタモデルになされた変更点：

  * 上述のパッケージ体系
  * StandardProfile2 と StandardProfil3 を単体の StandardProfile へ合体
  * デフォルト値を表現するために多重度の下限値（をゼロとする）緩和
  * 関連に所有される特性と対応する関連のいくつかの名前変更
  * NamedElement::``clientDependency`` を派生物とする
  * LoopNodes を ``loopVariables`` の所有者と同一視する。
    結果として UML 2.5 と UML 2.4.1 モデルファイルは次のものを措いて
    バージョン番号を置き換えることで交換可能となる。

    * LoopNodes の ``loopVariables``

    * Dependencies の ``clients`` である NamedElements で、
      UML 2.4.1 では ``clientDependency`` を含もうとした。

    * StandardProfile への参照

* LoopNodes は別として、
  バージョン番号を 20110701 へ戻すように編集し、
  なおかつ Dependencies の ``clients`` である NamedElements のすべてが
  ``clientDependency`` 属性を挿入させるならば、
  UML 2.4.1 ツールは UML 2.5 モデルを表現する XMI を読み込む能力が
  あるだろう。

* UML 2.5 準拠ツールは UML 2.5 または UML 2.4.1 モデルの
  どちらとも読み込むことも保存することもできるものとする。

  * UML 2.5 はたくさんの OCL 制約を成文化したので、
    UML 2.4.1 ツールで有効であるモデルが
    UML 2.5 で有効でなくともよいという場合があってよい。

E.3 XMI Serialization of the PrimitiveTypes model library
======================================================================
* 次に記すものは
  そのライブラリーを直接的または間接的にインポートするモデルの
  XMI 交換に利用される PrimitiveTypes モデルライブラリーに現れる
  タグのセッティングである。

  * タグ ``org.omg.xmi.nsPrefix`` を ``primitives`` にセット
  * PrimitiveTypes::Boolean にはタグ ``org.omg.xmi.schemaType`` を ``http://www.w3.org/2001/XMLSchema#boolean`` にセット
  * PrimitiveTypes::Integer にはタグ ``org.omg.xmi.schemaType`` を ``http://www.w3.org/2001/XMLSchema#integer`` にセット
  * PrimitiveTypes::Real にはタグ ``org.omg.xmi.schemaType`` を ``http://www.w3.org/2001/XMLSchema#double`` にセット
  * PrimitiveTypes::String にはタグ ``org.omg.xmi.schemaType`` を ``http://www.w3.org/2001/XMLSchema#string`` にセット
  * PrimitiveTypes::UnlimitedNatural にはタグ ``org.omg.xmi.schemaType`` を ``http://www.w3.org/2001/XMLSchema#string`` にセット

* UnlimitedNatural の制限なし値、表記は ``*`` であるが、
  これは ``*`` としてシリアライズされるものとし、
  それに対して UnlimitedNatural の数値はすべて、
  整数としての数の文字列表現としてシリアライズされるものとする。

E.4 XMI Serialization of the StandardProfile
======================================================================
* 次に記すものは
  そのプロファイルを直接的にまたは間接的にインポートするモデルの
  XMI 交換のための StandardProfile プロファイルに現れる
  タグのセッティングである。

  * タグ ``org.omg.xmi.nsPrefix`` を ``StandardProfile`` にセット

E.5 XMI Serialization of the UMLDI
======================================================================
* 次に記すものは
  モデル図式の XMI 交換のための UMLDI メタモデル拡張に現れる
  タグのセッティングである。

  * タグ ``org.omg.xmi.nsPrefix`` を ``umldi`` にセット

.. include:: /_include/uml-refs.txt
