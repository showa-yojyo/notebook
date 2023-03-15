======================================================================
Chapter 08: File System
======================================================================

`Chapter 08: File System <https://changkun.de/modern-cpp/en-us/08-filesystem/>`__
についてのノートなのだが、本文が実質空なので読者自身で学習するかもしれない。

ファイルシステムライブラリーは、ファイルシステム、パス、正規ファイル、ディレクト
リーなどの操作に関する機能を備えている。正規表現ライブラリーと同様に、Boost 由来
ライブラリーの一つで、最終的には C++ 標準に統合された。

.. contents::

8.1 Document and Link
======================================================================

.. admonition:: 読者ノート

   なんにのない。何を述べるのかも不明。

8.2 ``std::filesystem``
======================================================================

.. admonition:: 読者ノート

   本節も内容が空なので、次の節まで好きなことを勝手に記す。種本は
   cppreference.com の文章だろうから、それを私なりに要約していく。

.. mermaid::
   :align: center
   :alt: std::filesystem components
   :caption: Dependency of std::filesystem components

   flowchart LR
       directory_entry -.-> file_status & path
       D["{,recursive_}directory_iterator"] -.-> path & directory_entry & directory_options

       ss[["{,symlink_}status"]] -.-> file_status & path
       file_status -.-> file_type & perms

       cc[["copy{,_file}"]] -.-> path & copy_options
       permissions[[permissions]] -.-> path & perms & perm_options
       space[[space]] -.-> path & space_info

       L[[last_write_time]] -.-> file_time_type & path

       A[["Most\nNon-member\nFunctions"]] -..-> path

本ライブラリーで用いられる諸概念
----------------------------------------------------------------------

C++ の言葉というより、ファイルシステムのそれだ：

ファイル (file)
    ファイルシステムの主な構成要素であるオブジェクトだ。
    ファイルには名前、属性、種別がある。ファイル種別は次のようなものだ。

    ディレクトリー (directory)
        ファイルの容器となるファイル。他のディレクトリーを入れ子にすることができ
        る。
    通常ファイル (regular file)
        ディレクトリーに入っているファイルであって、名前と存在するファイルを関連
        付ける物（ハードリンク）。
    シンボリックリンク (symbolik link, symlink)
        ディレクトリーに入っているファイルであって、名前とパスを関連付ける物。パ
        スは実際に存在しなくてもよい。

    この他にもファイル種別はあるが、省略。

ファイル名 (file name)
    ファイル名を表す文字列。利用可能な文字、大文字小文字の区別、最大長は実装定
    義。文字列 ``"."`` および ``".."`` は当ライブラリーで特別な意味がある。
パス (path)
    ファイルを識別するための一連の要素。パス名は、オプションのルート名で始ま
    り、0 個以上のファイル名の連なりだ。パスの文字列表現（パス名）のネイティブ書
    式（例：セパレーターが何か）や文字エンコーディングは実装依存なのだが、本ライ
    ブラリーは可搬性のあるパス表現を与える。

    絶対パス (absolute path)
        ファイルの場所を一義的に特定する示すパス。

        正規パス (canonical path)
            シンボリックリンク、``"."``, ``".."`` のいずれも含まない絶対パス。
    相対パス (relative path)
        ファイルシステム上のある場所からの相対的なファイルの位置を特定するための
        パス。``"."`` や ``".."`` を含むのが普通。

クラス ``path``
----------------------------------------------------------------------

当ライブラリー最重要コンポーネントであるクラスは ``path`` だ。
``std::filesystem`` にあるほとんどのクラスメンバー関数、フリー関数、演算子各
種がこのクラスのオブジェクトを引数に取る。

パスオブジェクトを得る方法はいくつかある：

* パスを表現する文字列を引数としてコンストラクターを呼び出す
* 特別なパスを返すフリー関数を呼び出す
* ``directory_entry`` オブジェクトからメンバー関数 ``path`` を呼び出す
* 既存の ``path`` オブジェクトを加工してオブジェクトを新しく生成する

パスに関する操作を目的で分類し、興味のあるものから習得すればいいだろう：

結合
    パス二つを結合して一つのパスにする操作だ。ファイルシステムの観点ではディレク
    トリーにファイルを指定することに対応するものと、ディレクトリーの名前を文字列
    として末尾に付け足すことに対応する操作がある。前者にはメンバー関数
    ``append``, ``operator/=``, フリー関数 ``operator/`` いずれかを、後者にはメ
    ンバー関数 ``concat``, ``operaor+=`` のいずれかをそれぞれ用いる。
修正
    ディレクトリーセパレーターをプラットフォームに相応しいものに変換するメソッド
    ``make_preferred``, パスからファイル名を除去するメソッド ``remove_filename``,
    ファイル名や拡張子を置換するメソッド ``replace_filename``, ``replace_extension``,
    パスを空にするメソッド ``clear`` などがある。
変換
    パス形式を正規形に変換するメソッド ``lexically_normal`` や、基準パスを指定し
    て相対パスに変換するメソッド ``lexically_relative`` がある。何が lexically
    なのかというと、パスが実際に意味のある位置を指すか否かは不問だからだ。
分解
    メソッド名から操作内容は解る。名前だけ並べると ``root_name``,
    ``root_directory``, ``root_path``, ``relative_path``, ``parent_path``,
    ``filename``, ``stem``, ``extension``.
照会
    オブジェクトが初期状態かどうかはメソッド ``empty`` でテストする。

    パスが絶対パス、相対パスかを調べるにはメソッド ``is_absolute``,
    ``is_relative`` をそれぞれ確認する。

    メソッド名が ``has_`` で始まるものは、その目的語部分がパスにあるかどうかを返
    す。例えば ``has_extension`` はパスが拡張子を有するかどうかを返す。

二つのパスを比較演算子で辞書式比較することができる。

パスオブジェクトをシフト演算子で ``std::ostream`` に作用させることができる。すな
わち ``std::cout`` にパスを出力することができる。

パスの取得と操作
----------------------------------------------------------------------

クラス ``path`` のメンバーでない機能をいくつか記す。

関数 ``equivalent`` は指定された二つのパスが同じファイルシステム実体を指すものか
どうかをチェックする。どちらかが存在しない場合にはエラーが得られる。それに加え、
``operator==`` 系や ``compare`` という、パスが文字列的に等しいかをテストする関数
も用意されている。

関数 ``current_path`` は用途が二つある。戻り値を返す方はシェルコマンド
:command:`pwd` が出力するようなパスを絶対パスで返す。引数として ``path`` を取る
方はシェルコマンド :command:`cd path` のように振る舞う。

関数 ``absolute`` は指定パスと同じファイルシステムの場所を参照する絶対パスを返
す。指定パスにファイルが存在するかどうかは考慮されない。

関数 ``canonical`` は指定パスを正規パスに変換してそれを返す。指定パスが絶対パス
でない場合、この関数は ``absolute`` によって最初に絶対パスにされたかのように動作
する。こちらの関数は指定パスはファイルシステム上に存在しなければならない。

関数 ``relative`` は基準パスに対する指定パスへの相対パスを返す。他の処理に先立っ
て、引数のパスを正規化する。

あとは ``is_regular_file``, ``is_directory`` など、``is_`` から始まる一連の述語
関数がある。

ファイル属性を参照または設定する
----------------------------------------------------------------------

.. mermaid::
   :align: center
   :alt: status and symlinks
   :caption: Dependency of status and symlinks

   flowchart LR
     subgraph ss [functions]
       direction LR
       m1[[status]]
       m2[[symlink_status]]
     end
     ss -.-> file_status & path
     file_status -.-> file_type & perms

関数 ``status``, ``symlink_status`` は指定パスのファイル属性を返す。後者はシンボ
リックリンクをたどらず、リンク自身の属性を返す。これらの関数はクラス
``file_status`` のオブジェクトを返す。この戻り値から次に述べるファイル種別とアク
セス権を取得したり設定したりすることになる：

* ファイル種別を操作するにはメソッド ``type`` を呼び出す。
* アクセス権を操作するにはメソッド ``permissions`` を呼び出す。

どちらのメソッドも取得用と設定用オーバーロードがある。

``std::filesystem`` では、ファイル種別を次の列挙型の値で表現する。各定数の値はど
れをとっても互いに等しくない：

.. code:: c++

   enum class file_type {
       none,
       not_found,
       regular,
       directory,
       symlink,
       // ...
   };

アクセス権を操作する
----------------------------------------------------------------------

メソッド ``file_status::permissions`` の他に、フリー関数の ``permissions`` でも
ファイルのアクセス権を操作することが可能だ。

.. mermaid::
   :align: center
   :alt: permissions
   :caption: Dependency of permissions

   flowchart LR
       permissions[[permissions]] -.-> path & perms & perm_options

``std::filesystem`` では、ファイルに対するアクセス権を次の列挙型の値で表現する。
各定数はビット演算が効くように定義されている。UNIX の :command:`chmod` と同じと
思っていい：

.. code:: c++

   enum class perms{
       none = 0,
       owner_read = 0400,
       owner_write = 0200,
       owner_exec = 0100,
       owner_all = 0700,
       // ...
       all = 0777,
       mask = 07777,
       unknown = 0xffff
   };

さらにオプション指定のために列挙型 ``perm_opsions`` がある。意味が通じる限りはメ
ンバーの論理ビット演算が許されるようだ：

.. code:: c++

   enum class perm_options{
       replace,
       add,
       remove,
       nofollow
   };

用例を引用しておく：

.. code:: c++

   std::filesystem::permissions(
       "test.txt",
       std::filesystem::perms::owner_all | std::filesystem::perms::group_all,
       std::filesystem::perm_options::add);

その他のファイル情報を取得する
----------------------------------------------------------------------

関数 ``file_size`` は指定パスにある通常ファイルのサイズをバイト単位で返す。
パスがシンボリックリンクの場合は、実体のサイズを返す。ディレクトリーなど、それら
以外の場合は結果は実装定義とされる。

関数 ``space`` は指定パスに関する利用可能な空き容量を返す。戻り値は次の構造体オ
ブジェクトだ：

.. code:: c++

   struct space_info {
       std::uintmax_t capacity;
       std::uintmax_t free;
       std::uintmax_t available;
   };

関数 ``last_write_time`` は指定ファイルのおそらく mtime を取得または変更する。

.. admonition:: 読者ノート

   後者の操作については、時刻の指定方法を別途習わねばならない。

ディレクトリー内のファイルを一つ一つ処理する
----------------------------------------------------------------------

ディレクトリーを指定してファイルを訪問するための反復子クラスが二つ用意されてい
る。それぞれの違いは名前のとおりであるので述べない。

.. mermaid::
   :align: center
   :alt: iterator classes
   :caption: Dependency of iterator classes

   flowchart LR
     subgraph Iterators[iterator classes]
       direction LR
       directory_iterator
       recursive_directory_iterator
     end
   Iterators -.-> path & directory_entry & directory_options
   directory_entry -.-> path & file_status

オブジェクトをいったん生成すると、``for`` ループで関連ファイルにアクセスするとい
う装置だ。オブジェクトはコンストラクターを直接呼び出すことで生成する。普通はディ
レクトリーを指示するパスを指定する。オプションとして次の列挙型の値を与えてもよい：

.. code:: c++

   enum class directory_options {
       none,
       follow_directory_symlink,
       skip_permission_denied
   };

反復子はクラス ``directory_entry`` のオブジェクトを指す。メンバーとしてパスを格
納し、ディレクトリーの反復中にファイル属性（ハードリンク数、ステータス、シンボ
リックリンク、ファイルサイズ、最終書き込み時間）を追加的に格納することもできる。
例コードを引用する：

.. code:: c++

   std::filesystem::path sandbox /* = ... */;
   for (const& auto entry : std::filesystem::recursive_directory_iterator{sandbox})
   {
       process_entry(entry);
   }

.. admonition:: 読者ノート

   ``recursive_directory_entry`` の訪問順序は DFS とも BFS とも指定されていない。
   内容物それぞれがただ一度ずつ訪問されることしか指定されていない。

ファイルの存在を確かめる
----------------------------------------------------------------------

関数 ``exists`` は指定されたパス（または ``file_status`` 値）がファイルシステム
の既存ファイルに対応するかどうかを ``bool`` 値で返す。

ファイル種別が特定のものであるかどうかを確かめる
----------------------------------------------------------------------

対象となるファイルを ``path`` または ``file_status`` オブジェクトとして持ってい
るならば、そのファイルを次の関数の引数に与えて呼び出すことで述語判定できる：

* ``is_regular_file``
* ``is_directory``
* ``is_symlink``
* etc.

.. admonition:: 読者ノート

   一連の判定関数は実践的には例外を送出しないと考えられるが、関数署名上
   ``noexcept`` 修飾がないオーバーロードがあることを心に留めておく？

ファイル作成
----------------------------------------------------------------------

まず、通常ファイルを作成するには従来どおり ``std::ofstream`` が使えることに注意
する。

関数 ``create_directory`` または ``create_directories`` はパスを与えてディレクト
リーを新規作成する。いずれもシェルコマンド :command:`mkdir -p` のように振る舞う
と読める。既存のパスを引数に取るオーバーロードもあり、それらは属性を複製するため
のものだ。

関数 ``create_symlink`` と ``create_directory_symlink`` はシェルコマンド
:command:`ln -s` のように振る舞う。対象がディレクトリーであるか否かを気にする OS
向けにこれらの関数が用意されている。

ファイル複製
----------------------------------------------------------------------

関数 ``copy`` はファイルとディレクトリーを複製する。一方、関数 ``copy_file`` は
単一ファイルの内容を複製する。列挙型 ``copy_options`` を組み合わせてオプションを
指定することが可能なオーバーロードもある。

関数 ``copy_symlink`` はシンボリックリンクをシンボリックリンクとして複製する。関
数 ``create_symlink`` や ``create_directory_symlink`` を使い分けることなく呼び出
せる利点がある。

ファイル移動
----------------------------------------------------------------------

関数 ``rename`` はシェルコマンド :command:`mv old new` のように振る舞う。シンボ
リックリンクに対しては、それ自身の名前を変えるように動作し、対象は変わらない。

ファイル削除
----------------------------------------------------------------------

関数 ``remove`` はファイルまたは空ディレクトリーをファイルシステムから削除する。
シェルコマンドの :command:`rm filepath` や :command:`rmdir dirpath` に相当する。

関数 ``remove_all`` はディレクトリーを指定する場合、それとそのすべてのサブディレ
クトリーの内容を再帰的に削除する。シェルコマンドの :command:`rm -r dirpath` 相当。

これらの関数のいずれもシンボリックリンクはそれ自身に作用し、リンク対象を削除する
ものではない。

異常時処理
----------------------------------------------------------------------

節の最後になったが、操作時に異常が発生したときの関数の振る舞いについてまとめてお
く。``std::filesystem`` にある失敗する可能性のある関数のすべてに対して、次の性質
を持つオーバーロードのペアが用意されている：

1. 失敗時に例外 ``std::filesystem_error`` オブジェクトを送出するもの
2. 失敗時に関数呼び出し時に参照渡しをされた ``std::error_code`` オブジェクトにエ
   ラーを報告するもの

後者の関数は前者が送出する型ではない型の例外オブジェクトを送出するものとしないも
のがある。パスを扱う関係で ``std::bad_alloc`` を送出する可能性がある。

Further Readings
======================================================================

.. admonition:: 読者ノート

   `Filesystem library (since C++17) - cppreference.com <https://en.cppreference.com/w/cpp/filesystem>`__
       この資料からとりあえず学ぶ。
