================================================================================
Bash Reference Manual 読書ノート
================================================================================

私は Bash を計算機利用全ての基本だと考えているので、その基本要素の理解に漏れがあ
るというのは避けたい。そうなれば、いつかは Bash Reference Manual を通読するのが
不可欠だと考える。その「いつか」がべらぼうに遅れてしまったが、読解を少しずつ消化
していこうと思う。

私の興味関心の順位に従い、本書の章立てを意識せず、不規則な順序で読んでは綴るを反
復していく。例えば、Bash 後方互換性と POSIX モードに関係する機能は読まない。

かなりの数のノートができたので、この段階でノートの索引をひとまず設けておく。半々
くらいの確率で追加第二弾がある。

.. Introduction
.. Definitions
.. toctree::
   :caption: Basic Shell Features
   :maxdepth: 1

   Quoting ノート <https://gist.github.com/showa-yojyo/88f7f1b954b6ecb7013aeb347f22c68a>
   命令をまとめる方法ノート <https://gist.github.com/showa-yojyo/fd9fdd89d384633fab90f233f37aa569>
   二重角括弧ノート <https://gist.github.com/showa-yojyo/6c223d863a717999d8edd43a4fa113b5>
   Coprocesses ノート <https://gist.github.com/showa-yojyo/621408d2d3ee3b702ce4b0cb79c23740>
   関数ノート <https://gist.github.com/showa-yojyo/6b4cb5a92d1c64f023870c8ba8c05eec>
   位置引数ノート <https://gist.github.com/showa-yojyo/911f64c27882313075a0e4754e31119d>
   中括弧展開ノート <https://gist.github.com/showa-yojyo/500a833243aaec0976c2ddb13fdb2660>
   Tilde 展開ノート <https://gist.github.com/showa-yojyo/f0584c60026cde627ce18dc3c3653c39>
   変数展開ノート <https://gist.github.com/showa-yojyo/7a7005f5d909964a140468a927a57169>
   命令置換ノート <https://gist.github.com/showa-yojyo/0ea327c649c1ce44cfcfaeef2d3d33a7>
   プロセス置換ノート <https://gist.github.com/showa-yojyo/508cd4c1c1c72e8025b6774a42b07427>
   ファイル名展開ノート <https://gist.github.com/showa-yojyo/dbc6b610d76c6f3c63586922338e1855>
   Redirections ノート <https://gist.github.com/showa-yojyo/e06b2cae967d080783b47614ba9b5cf1>
   環境ノート <https://gist.github.com/showa-yojyo/0893ad67b3d7da09b7c94a0008572290>
   実行環境ノート <https://gist.github.com/showa-yojyo/43eef1dc0804b7b007416c00696f7933>
   終了状態ノート <https://gist.github.com/showa-yojyo/9bf95bbf349051929ac85aae8e1c748c>
   信号ノート <https://gist.github.com/showa-yojyo/bbc18d191c65c9649684d180631621b2>

.. toctree::
   :caption: Shell Builtin Commands
   :maxdepth: 1

   Bash trap ノート <https://gist.github.com/showa-yojyo/444c1d94172f68072c756ac720fafe12>

.. Shell Variables
.. toctree::
   :caption: Bash Features
   :maxdepth: 1

   呼び出し仕様ノート <https://gist.github.com/showa-yojyo/de3d1c75233963bc865fa53d9cea8361>
   始動ノート <https://gist.github.com/showa-yojyo/77413133afd3d1ef1d95aa934cea15f5>
   対話モードノート <https://gist.github.com/showa-yojyo/894d05c917ccf4176218bdbced852627>
   条件式ノート <https://gist.github.com/showa-yojyo/d4c204bed253016db7321d89159e2039>
   算法ノート <https://gist.github.com/showa-yojyo/615f43f2b0473ebb32739b2a7be68d11>
   別名ノート <https://gist.github.com/showa-yojyo/7f036a9d5d80d3ef6dc999268f7f8431>
   配列ノート <https://gist.github.com/showa-yojyo/65d2f961a991f1808b70c7a095394a2a>
   Directory stack ノート <https://gist.github.com/showa-yojyo/e4b82a77fc439709240622ffbaba7226>

.. toctree::
   :caption: Job Control
   :maxdepth: 1

   ジョブノート <https://gist.github.com/showa-yojyo/25c5bf5d76be2872a5a502e95f18cd39>

.. toctree::
   :caption: Command Line Editing
   :maxdepth: 1

   Readline 基本ノート <https://gist.github.com/showa-yojyo/5621aa89f14d4619b02108f6edfb7d2a>
   Readline ドットファイルノート <https://gist.github.com/showa-yojyo/0fd088846db3d5a15114160d2d8f3e48>
   Readline 命令ノート <https://gist.github.com/showa-yojyo/7dfa1190dd49808c63155fa73f044ab2>
   プログラム可能補完内蔵命令ノート <https://gist.github.com/showa-yojyo/fc06eabe197ecc33dc2ea073c82f2b7a#file-bash-completion-builtins-md>
   プログラム可能補完ノート <https://gist.github.com/showa-yojyo/fc06eabe197ecc33dc2ea073c82f2b7a#file-bash-completion-md>
   自動補完事例ノート <https://gist.github.com/showa-yojyo/fc06eabe197ecc33dc2ea073c82f2b7a#file-bash-completion-examples-md>

.. toctree::
   :caption: Using History Interactively
   :maxdepth: 1

   履歴展開ノート <https://gist.github.com/showa-yojyo/8c14887d265ef4f3ee7cd9158ed51eb7>
   履歴に関係する変数ノート <https://gist.github.com/showa-yojyo/f39558b180007a179863dd6106d714e3>
   履歴オプションノート <https://gist.github.com/showa-yojyo/36ae8c20b17daf21558de71f01ca75a2>

.. Installing Bash
.. Reporting Bugs
.. Major Differences From The Bourne Shell
