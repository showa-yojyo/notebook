======================================================================
21 Primitive Types
======================================================================

.. contents::

21.1 Summary
======================================================================

PrimitiveTypes パッケージとは、メタモデルの定義において一般に用いられる、再利用
可能な PrimitiveTypes の集合を定義する独立パッケージだ。UML メタモデルはこの
PrimitiveTypes パッケージを使用する。

   Figure 21.1 Primitive Types

この五個の型が PrimitiveTypes のすべてだ。

21.2 Semantics
======================================================================

   Table 21.1 PrimitiveType domains

Integer
   Integer オブジェクトは整数の集合に含まれる値だ。
Boolean
   Boolean オブジェクトは定義済みの値である真と偽のどちらかだ。
String
   String オブジェクトは文字の配列を定義する。

   * 文字集合は非ラテン文字でない文字を含むことがある。
   * 文字列自身の意味はその目的によって異なる。コメント、計算言語式、OCL 式、等々
     であり得る。
UnlimitedNatural
   UnlimitedNatural オブジェクトは自然数の集合に *unlimited* を加えた集合の値
   だ。

   * 値 *unlimited* は ``*`` を用いて示される。
   * UnlimitedNatural の値はふつう、多重度などの範囲の上限を示すのに用いられる。
     範囲に上限がないことを指定するときにはいつでも *unlimited* が用いられる。
Real
   Real オブジェクトは実数の集合の要素だ。通常、実装は内部的に ISO/IEC/IEEE
   60559:2011 のような浮動小数点規格を用いて表現する。

21.3 Notation
======================================================================

   There is no notation for PrimitiveTypes. There is notation for literal values
   of PrimitiveTypes; this notation is covered in sub clause 8.2.

21.4 Examples
======================================================================

上述のように記法がないので、以下の図式でリテラル値の表記を例示している：

* Figure 21.2 An Integer used as a type for an attribute, with a default value
* Figure 21.3 A Boolean used as a type for an attribute, with a default value
* Figure 21.4 A String used as a type for an attribute, with a default value
* Figure 21.5 An UnlimitedNatural used as an upper bound for a multiplicity
* Figure 21.6 Two attributes with type Real

.. include:: /_include/uml-refs.txt
