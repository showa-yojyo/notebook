======================================================================
What's New In Bash 5 ノート
======================================================================

Bash バージョン 5.x で追加された新機能のメモ。全部を追跡するのは無理だから気にな
るものと便利とされている機能を中心に拾っていく。

.. contents::

バージョン 5.0
======================================================================

| There is an ``EPOCHSECONDS`` variable, which expands to the time in seconds
| since the Unix epoch.

例えばコマンド ``echo $EPOCHSECONDS`` を実行すると、コマンド ``date +%s`` と同じ
ものを出力する。

| There is an ``EPOCHREALTIME`` variable, which expands to the time in seconds
| since the Unix epoch with microsecond granularity.

これも同様で、コマンド ``echo $EPOCHREALTIME`` を実行すれば ``date +%s.%6N`` と
同じ出力が得られる。

| ``BASH_ARGV0``: a new variable that expands to ``$0`` and sets ``$0`` on assignment.

変数 ``$0`` に値を代入することは不可能だが、それを可能にするのが変数
``BASH_ARGV0`` だ。デバッグ用途らしい。

| ``history -d`` understands negative arguments: negative arguments offset from
| the end of the history list.

例えば ``history -d -10`` とすれば、有効なコマンド履歴の十個前に実行したコマンド
を履歴から削除する。

| The ``wait`` builtin now has a ``-f`` option, which signfies to wait until the
| specified job or process terminates, instead of waiting until it changes
| state.

コマンド ``wait -f ID`` はジョブ状態が変更されたときに返るのではなく、ジョブ
``ID`` が実際に終了するのを待ってからその終了コードを返すようになる。

| If a non-interactive shell with job control enabled detects that a foreground
| job died due to ``SIGINT``, it acts as if it received the ``SIGINT``.

これは既存の何かに影響するか？

| A new ``shopt`` option: ``localvar_inherit``; if set, a local variable inherits the
| value of a variable with the same name at the nearest preceding scope.

次の関数で説明する。局所変数 ``var`` を内側の局所変数スコープとそのすぐ外側のス
コープに宣言する。このオプションを有効にすると、局所変数スコープ突入前に同名の変
数に値が初期化済みならば、その値を引き継ぐようになる。

.. code:: shell

   function demo_localvar_inherit
   {
       function outer
       {
           local var
           echo In call: $var
           var=localvar
           echo In call, after setting: $var
       }
       local var=globalvar
       echo Before call: $var
       outer
       echo After call: $var
   }

オプションを変えて関数を呼んだ結果を比較する：

.. code:: console

   bash$ shopt -u localvar_inherit; demo_localvar_inherit
   Before call: globalvar
   In call:
   In call, after setting: localvar
   After call: globalvar

   bash$ shopt -s localvar_inherit; demo_localvar_inherit
   Before call: globalvar
   In call: globalvar
   In call, after setting: localvar
   After call: globalvar

継承しないほうが、つまり従来と同じ設定のほうが変数のスコープの意味が生きるから好
みだ。

| The ``history`` builtin can now delete ranges of history entries using
| ``-d start-end``.

コマンド履歴を履歴番号範囲を指定することで削除できるようになった。次を実行すると
コマンド履歴番号 1103 から 1118 までの履歴を削除する：

.. code:: console

   bash$ history -d 1103-1118

先ほど挙げた負のオフセットを ``start`` および ``end`` の値として受け入れる。例え
ば次のようなコマンドが考えられる：

.. code:: console

   bash$ history -d -16--1

| The command completion code now matches aliases and shell function names
| case-insensitively if the readline ``completion-ignore-case`` variable is set.

ファイル :file:`$HOME/.inputrc` で ``set completion-ignore-case on`` を指定して
いるはずだ。こうすると ``alias`` や ``function`` の名前補完にも効果があるように
なった。これは便利なのかどうかわからない。その手の識別子には小文字しか使わないよ
うにしている。

| There is a new ``assoc_expand_once`` shell option that attempts to expand
| associative array subscripts only once.

これはなぜあるのだろう。

| The ``umask`` builtin now allows modes and masks greater than octal 777.

要するに四桁のマスクを操作可能になったということか。

| The ``complete`` builtin now accepts a ``-I`` option that applies the completion
| to the initial word on the line.

行の最初の単語に補完を適用することができるようになった。

| The ``localvar_inherit`` option will not attempt to inherit a value from a
| variable of an incompatible type (indexed vs. associative arrays, for
| example).

新規オプション ``localvar_inherit`` に関する仕様の一部。型を指定して局所変数を宣
言するデモを書いて試したいところだ。

| The ``globasciiranges`` option is now enabled by default; it can be set to
| off by default at configuration time.

オプション ``globasciiranges`` 自体は以前からある。5.0 でこの既定値が on になっ
たと言っている。例えば、パターン ``[a-d]`` が ``a``, ``b``, ``c``, ``d`` のいず
れかにマッチするパターンを意味するように指定したい場合（大文字などは不要）に有効
にする。

| Associative and indexed arrays now allow subscripts consisting solely of
| whitespace.

配列の添字が空白文字のみから構成されても構わないと読めるが、実際には先頭の要素が
参照されるという理解でいいか？

| ``checkwinsize`` is now enabled by default.

このオプションは WSL が明示的に on にしているので気にしない。

| The ``localvar_unset`` ``shopt`` option is now visible and documented.

隠しオプション ``localvar_unset`` が表に浮上。

このオプションが on の場合、直前の関数スコープにある局所変数に対する ``unset``
呼び出しが、その関数が戻るまでに後続の検索でそれらが未設定であることをわかるよう
に印をつけるようになる。この挙動は現在の関数スコープでローカル変数の設定を解除し
たときのそれと同じだ。

| The ``progcomp_alias`` shopt option is now visible and documented.

隠しオプション ``progcomp_alias`` が表に浮上。仕様を読むと ``alias`` が絡むダブ
ル補完を試みると読める。

| There is a new ``seq`` loadable builtin.

手許の環境では存在しない。

| The ``$_`` variable doesn't change when the shell executes a command that forks.

ではどうなるのか。

| POSIX mode now enables the ``shift_verbose`` option.

コマンド ``shift`` で範囲外の数を指定すると、たいていのシェルではエラーとなる。
しかし、本家 POSIX ではエラーとする仕様では特にない。Bash 5.0 からはこのオプショ
ン自体を有効にするようになった。そう解釈していいか。

バージョン 5.1
======================================================================

.. todo::

   調査してノート。

参考資料
======================================================================

主要資料
----------------------------------------------------------------------

* `Bash-5.0 release available <https://lists.gnu.org/archive/html/bug-bash/2019-01/msg00063.html>`__

先人たちの記事
----------------------------------------------------------------------

* `Bash 5.0 is here with new features and improvements | Packt Hub <https://hub.packtpub.com/gnu-bash-5-0-is-here-with-new-features-and-improvements/>`__
* `Bash 5.0 Released with New Features <https://itsfoss.com/bash-5-release/>`__
* `What's New in GNU Bash 5? <https://www.shell-tips.com/bash/what-is-new-in-gnu-bash-5/>`__
* `upgrade - What's going to be new in bash 5 - Unix & Linux Stack Exchange <https://unix.stackexchange.com/questions/478590/whats-going-to-be-new-in-bash-5>`__
* `Get current time in seconds since the Epoch on Linux, Bash - Stack Overflow <https://stackoverflow.com/questions/1092631/get-current-time-in-seconds-since-the-epoch-on-linux-bash>`__
* `variable - What is the purpose of BASH_ARGV0 in bash? - Unix &amp; Linux Stack Exchange <https://unix.stackexchange.com/questions/493221/what-is-the-purpose-of-bash-argv0-in-bash>`__
* `scope - Bash: Hide global variable using local variable with same name - Stack Overflow <https://stackoverflow.com/questions/54204612/bash-hide-global-variable-using-local-variable-with-same-name>`__
* `Globbing e as variáveis ‘LANG’ e ‘LC_’ – DEBXP COMUNIDADE <https://debxp.org/globbing-e-as-variaveis-lang-e-lc_/>`__
* `linux - How to delete history of last 10 commands in shell? - Stack Overflow <https://stackoverflow.com/questions/14750650/how-to-delete-history-of-last-10-commands-in-shell>`__
* `Bash wait Command with Examples <https://phoenixnap.com/kb/bash-wait-command>`__
* etc.
