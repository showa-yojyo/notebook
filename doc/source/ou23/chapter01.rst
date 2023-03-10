======================================================================
Chapter 01: Towards Modern C++
======================================================================

`Chapter 01: Towards Modern C++ <https://changkun.de/modern-cpp/en-us/01-intro/>`__
についてのノート。

.. contents::

本書著者が用いているコンパイラー :program:`clang++` のオプション ``-std=c++2a``
は C++20 相当だと思っていいだろう。

.. admonition:: 読者ノート

   私の :program:`g++` による動作確認コマンドを記す。Visual Studio Code の
   :file:`.vscode/tasks.json` のコマンドラインオプション配列に次のコマンドライン
   と同等の引数を指定しておく：

   .. code:: console

      g++ -fdiagnostics-color=always \
          -g -Werror -Wall -Wextra -ansi -pedantic -std=c++17 \
          ${file} \
          -latomic \
          -o ${fileDirname}/${fileBasenameNoExtension}

1.1 Deprecated Features
======================================================================

非推奨機能とは、C++11 以降にそうなったと解釈する。私が心得るべき項目だけ挙げる：

* ``auto_ptr`` は非推奨。代えて ``unique_ptr`` を用いる。
* クラスがデストラクターを持つ場合、そのクラスがコピーコンストラクターやコピー代
  入演算子を生成するプロパティーは非推奨。
* 旧式の引数バインディングは非推奨。

1.2 Compatibilities with C
======================================================================

C++ と C を混ぜて使うときの注意点が記されている。もう必要ない。

Further Readings
======================================================================

A Tour of C++ (2nd Edition) Bjarne Stroustrup
  Stroustrup 先生の著述には目を通さぬ手はないだろう。
`C++ compiler support - cppreference.com <https://en.cppreference.com/w/cpp/compiler_support>`__
  この参考文献はもう一度登場する。
`Incompatibilities Between ISO C and ISO C++ <http://david.tribble.com/text/cdiffs.htm#C99-vs-CPP98>`__
  2001 年の資料。C99 と C++98 との比較。
