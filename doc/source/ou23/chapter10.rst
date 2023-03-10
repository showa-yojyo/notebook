======================================================================
Chapter 10 Outlook: Introduction of C++20
======================================================================

`Chapter 10 Outlook: Introduction of C++20 <https://changkun.de/modern-cpp/en-us/10-cpp20/>`__
に関するノート。C++20 が導入する重要な機能のいくつかを紹介するとのことだが、まだ
脱稿していないようだ。

.. contents::

Concept
======================================================================

テンプレートプログラミングをさらに強化したものがコンセプトだ。テンプレートプログ
ラミングはコンパイラーにテンプレート引数を評価させることが本質的だが、テンプレー
しばしばさまざまな凶悪なエラーに遭遇する。これは、これまでのところ、テンプレート
引数を検証したり制限したりすることができなかったから起こるのだ。次のようなコード
でさえ読みにくいエラーメッセージを大量に出力する：

.. code:: c++

   #include <list>
   #include <algorithm>

   int main() {
       std::list<int> l = {1, 2, 3};
       std::sort(l.begin(), l.end());
       return 0;
   }

このコードエラーの根本的な原因は、``std::sort`` が受け付けるのはランダム反復子の
ペアである必要があり、``std::list`` から得られる反復子はランダムではないからだ。
コンセプトの言葉で言えば、``std::list`` の反復子は ``std::sort`` のランダム反復
子というコンセプトの制約を満たさない．コンセプトを導入した後、次のようにテンプ
レート引数を制約することができる：

.. code:: c++

   template <typename T>
   requires Sortable<T> // Sortable is a concept
   void sort(T& c);

これをこう略す：

.. code:: c++

   template<Sortable T> // T is a Sortable typename
   void sort(T& c);

型として直接使うこともある：

.. code:: c++

   void sort(Sortable& c); // c is a Sortable type object

Module
======================================================================

なんにのない

Contract
======================================================================

なんにのない

Range
======================================================================

なんにのない

Coroutine
======================================================================

なんにのない

Conclusion
======================================================================

まだ早い。

Further Readings
======================================================================

`C++ compiler support - cppreference.com <https://en.cppreference.com/w/cpp/compiler_support>`__
    今使っている :program:`g++` は 11.3.0 だ。これは C++20 の新機能、ライブラリー
    をほとんどすべて網羅していると読める。
`History of C++ - cppreference.com <https://en.cppreference.com/w/cpp/language/history>`__
    当然だが C++20 は 2020 年。
