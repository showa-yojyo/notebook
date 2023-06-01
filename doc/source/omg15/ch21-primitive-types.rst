======================================================================
21 Primitive Types
======================================================================

UML 2.5 pp. 675-676 に関するノート。ここはもはや学習対象にならない。

.. contents:: ノート目次

21.1 Summary
======================================================================

* PrimitiveType パッケージとは、メタモデルの定義において一般に用いられる、再利用
  可能な PrimitiveType の集合を定義する独立パッケージである。

* Figure 21.1 Primitive Types

  * この 5 個が PrimitiveTypes のすべてであるらしい。

21.2 Semantics
======================================================================

* Table 21.1 PrimitiveType domains

  * Integer オブジェクトは整数の（無限）集合の要素の一つである。
  * Boolean オブジェクトは定義済みの値である ``true`` と ``false`` のどちらかで
    ある。
  * String オブジェクトは文字の配列を定義する。

    * 文字集合は非ラテン文字でない文字を含んでよい。
    * 文字列自身の意味はその目的に依る。コメント、計算上の言語表現、OCL 式、等々
      であり得る。

  * UnlimitedNatural オブジェクトは自然数と ``unlimited`` の（無限）集合の要素の
    一つである。

    * 値 ``unlimited`` は ``"*"`` を用いて示される。
    * UnlimitedNatural は典型的に多重度等の範囲の上限を示すのに用いられる。な
      お、範囲に上限がないことを指定するときにはいつでも ``unlimited`` が用いら
      れる。

  * Real オブジェクトは実数の（無限）集合の要素である。

    * 典型的には実装は内部的に ISO/IEC/IEEE 60559:2011 のような浮動小数点標準を
      用いて表現するものである。

21.3 Notation
======================================================================

* PrimitiveTypes の表記法はない。PrimitiveTypes のリテラル値の表記法はある。こ
  の表記法は :doc:`./ch08-values` で網羅済み。

21.4 Examples
======================================================================

特になし。

* Figure 21.2 An Integer used as a type for an attribute, with a default value
* Figure 21.3 A Boolean used as a type for an attribute, with a default value
* Figure 21.4 A String used as a type for an attribute, with a default value
* Figure 21.5 An UnlimitedNatural used as an upper bound for a multiplicity
* Figure 21.6 Two attributes with type Real

.. include:: /_include/uml-refs.txt
