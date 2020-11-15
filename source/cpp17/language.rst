======================================================================
What's New In C++17 言語仕様
======================================================================

このノートでは C++17 で注目すべき言語仕様を学習する。
すでに cpprefjp_ がそのへんをきれいに整理している。
それを利用して、読みながら急所を記していくことにする。

タイピングの都合で訳語は cpprefjp_ のものと一部変更して記す。

.. contents::

.. include:: /_include/cpp-refs.txt

変数・データ構造関係
======================================================================

.. | [十六進浮動小数点数リテラル](cpp17/hexadecimal_floating_literals.md) | 十六進数表記で浮動小数点数リテラルを記述できるようにする |
.. | [インライン変数](cpp17/inline_variables.md) | `inline`指定をすることで翻訳単位を跨いでひとつのオブジェクトになる変数を定義する |
.. | [構造化束縛](cpp17/structured_bindings.md) | 組・タプル・配列を展開して変数定義する |
.. | [波括弧初期化の型推論の新規則](cpp17/new_rules_for_auto_deduction_from_braced-init-list.md) | 波括弧初期化子が単一要素の場合は `T` に推論，複数要素の場合は不適格 |
.. | [`[[maybe_unused]]`属性](cpp17/maybe_unused.md)       | 使用しない可能性のある変数に対する警告を抑制する |
.. | [`[[nodiscard]]`属性](cpp17/nodiscard.md)             | 戻り値を捨ててはならないことを指定する |
.. | [値のコピー省略を保証](cpp17/guaranteed_copy_elision.md) | 右辺値を変数の初期化のために使用する場合、コピーもムーブも省略することを保証 |
.. | [厳密な式の評価順](cpp17/expression_evaluation_order.md) | 式の評価順を規定する |
.. | [参照メンバをもつクラスの置き換え](cpp17/replacement_of_class_objects_containing_reference_members.md) | 参照型メンバや`const`データメンバを含むクラスについてこれまで結果は未定義とされていた配置`new`によるオブジェクトの置き換えを条件付きで可能とする |
.. | [`enum class`変数の初期値として整数を指定する際の規則を調整](cpp17/construction_enum_class_values.md) | キャストを使用することなく整数を初期値として使用し、`E e{0};`のような初期化を許可 |
.. | [アライメント指定されたデータの動的メモリ確保](cpp17/dynamic_memory_allocation_for_over-aligned_data.md) | `operator new`と`operator delete`でアライメント値を取得できるようにする |
.. | [集成体初期化の拡張](cpp17/extension_to_aggregate_initialization.md) | 集成体初期化で基底クラスも入れ子に集成体初期化可能になる |

制御構文
======================================================================

.. | [`if`文と`switch`文の条件式と初期化を分離](cpp17/selection_statements_with_initializer.md) | `if (init; condition)`のように初期化と条件式を分けて記述できるようにする |
.. | [`[[fallthrough]]`属性](cpp17/fallthrough.md)                    | フォールスルー時の警告を抑制する |
.. | [`constexpr if`文](cpp17/if_constexpr.md)     | `if constexpr(cond)`とすることで、その`if`文はコンパイル時に処理される |
.. | [範囲 `for` ループの制限緩和](cpp17/generalizing_the_range-based_for_loop.md) | 範囲 `for` 文の `begin()` と `end()` が異なるイテレータ型を返せるようにすることで、終端イテレータを定義しやすくする |

ラムダ式
======================================================================

.. | [ラムダ式での`*this`のコピーキャプチャ](cpp17/lambda_capture_of_this_by_value.md) | キャプチャリストに`*this`を指定することで、`*this`をコピーキャプチャする |
.. | [`constexpr`ラムダ](cpp17/constexpr_lambda.md) | ラムダ式の関数オブジェクトが定数式の文脈で使用された場合に、それがコンパイル時に評価されるようにする |

テンプレート
======================================================================

.. | [畳み込み式](cpp17/folding_expressions.md)   | パラメータパックに対する二項演算の累積処理 |
.. | [テンプレートテンプレートパラメータに`typename`キーワードの使用を許可](cpp17/allow_typename_in_a_template_template_parameter.md) | `class`キーワードしか使用できなかった部分に、`typename`を許可する |
.. | [クラステンプレートのテンプレート引数推論](cpp17/type_deduction_for_class_templates.md) | コンストラクタの引数からクラスのテンプレート引数を推論できるようにする |
.. | [非型テンプレートパラメータの`auto`宣言](cpp17/declaring_non-type_template_arguments_with_auto.md)   | `template <auto x>`とすることで、`X<3>;` `X<true>;` `X<'a'>`のように定数を受け取りやすくする |
.. | [全ての非型テンプレート引数の定数式評価を許可](cpp17/allow_constant_evaluation_for_all_non-type_template_arguments.md) | ポインタの定数式評価として、配列からポインタへの変換や、関数から関数ポインタへの変換などを許可 |
.. | [`using`宣言のパック展開](cpp17/pack_expansions_in_using.md) | パラメータパックの型を基底クラスとして指定した場合に、using宣言に基底クラスのパラメータパックを指定できるようにする |
.. | [変数テンプレートのデフォルトテンプレート引数を許可](cpp17/allow_default_template_arguments_of_variable_templates.md) | 変数テンプレートのテンプレートパラメータがデフォルト引数を持つことを許可する |

定数式
======================================================================

.. | [`static_assert`のメッセージ省略を許可](cpp17/extending_static_assert.md) | 第2引数だった診断メッセージの省略を許可する |
.. | [`constexpr`ラムダ](cpp17/constexpr_lambda.md) | ラムダ式の関数オブジェクトが定数式の文脈で使用された場合に、それがコンパイル時に評価されるようにする |
.. | [`if constexpr`文](cpp17/if_constexpr.md) | `if constexpr(cond)`とすることで、その`if`文はコンパイル時に処理される |

名前空間
======================================================================

.. | [入れ子名前空間の定義](cpp17/nested_namespace.md)               | `namespace A::B {}`のように、入れ子の名前空間を簡単に定義できるようにする |
.. | [名前空間と列挙子への属性付加を許可](cpp17/attributes_for_namespaces_and_enumerators.md) | 名前空間の定義と、列挙型の各要素の定義に、属性を付けられるようにする |
.. | [`using`宣言のパック展開](cpp17/pack_expansions_in_using.md) | パラメータパックの型を基底クラスとして指定した場合に、using宣言に基底クラスのパラメータパックを指定できるようにする |

例外
======================================================================

.. | [例外仕様を型システムの一部にする](cpp17/exception_spec_be_part_of_the_type_system.md) | 関数の型に例外仕様が含まれるようにする |
.. | [非推奨だった古い例外仕様を削除](cpp17/remove_deprecated_exception_specifications.md) | `throw`キーワードによる例外仕様を削除。`throw()`は残る |

属性
======================================================================

.. | [`[[fallthrough]]`属性](cpp17/fallthrough.md)                 | フォールスルー時の警告を抑制する |
.. | [`[[maybe_unused]]`属性](cpp17/maybe_unused.md)               | 使用しない可能性のある変数に対する警告を抑制する |
.. | [`[[nodiscard]]`属性](cpp17/nodiscard.md)                     | 戻り値を捨ててはならないことを指定する |
.. | [名前空間と列挙子への属性付加を許可](cpp17/attributes_for_namespaces_and_enumerators.md) | 名前空間の定義と、列挙型の各要素の定義に、属性を付けられるようにする |
.. | [属性の名前空間指定に繰り返しをなくす](cpp17/using_attribute_namespaces.md) | `[[using CC: opt(1), debug]]`のように属性の名前空間宣言をまとめて行う |
.. | [不明な属性を無視する](cpp17/non_standard_attributes.md)                 | 実装が知らない名前空間の属性は無視する |

プリプロセッサ
======================================================================

.. | [`__has_include`](cpp17/has_include.md) | インクルードするファイルが存在するかを確認する |

機能の削除
======================================================================

.. | [トライグラフの削除](cpp17/removing_trigraphs.md) | 現代では使用する必要がなくなったトライグラフ機能を削除 |
.. | [非推奨だった`register`キーワードを削除](cpp17/remove_deprecated_use_of_the_register_keyword.md) | コンパイラから単に無視されていた`register`キーワードを削除。予約語は残る |
.. | [非推奨だった`bool`型に対するインクリメント演算子を削除](cpp17/remove_deprecated_increment_of_bool.md) | `bool`変数に対して`++`すると`true`になる仕様を削除 |
.. | [非推奨だった古い例外仕様を削除](cpp17/remove_deprecated_exception_specifications.md) | `throw`キーワードによる例外仕様を削除。`throw()`は残る |

小さな変更
======================================================================

ここでは、コア言語作業グループへ問題報告され、その解決策として導入された言語仕様の変更を解説する。

.. | [更新された定義済みマクロ](cpp17/predefined_macros.md) | 標準規格で定義されたマクロの更新 |
.. | [機能テストマクロ](cpp17/feature_test_macros.md)       | C++17 の機能がサポートされているかどうかをテストするためのマクロ |
.. | [`noexcept`付きのラムダ式から変換する関数ポインタに`noexcept`を付加する](cpp17/lambda_to_noexcept_function_pointer.md) | キャプチャを持たない非ジェネリックラムダに`noexcept`を付加した場合、変換した関数ポインタに`noexcept`を付加する |
.. | [UTF-8文字リテラル](cpp17/utf8_character_literals.md) | UTF-8の指定が文字列リテラルに対してしかできなかったが、文字リテラルにもUTF-8指定をできるようにする |

.. include:: /_include/cpp-refs.txt
