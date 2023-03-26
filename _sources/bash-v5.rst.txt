======================================================================
What's New In Bash 5 ノート
======================================================================

Bash バージョン 5.x で追加された新機能のメモ。全部を追跡するのは無理だから気にな
るものと便利とされている機能を中心に拾っていく。

.. contents::

バージョン 5.0
======================================================================

`Bash-5.0 release available <https://lists.gnu.org/archive/html/bug-bash/2019-01/msg00063.html>`__
からめぼしい項目に絞ってノートを取る。

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

`Bash-5.1 release available <https://lists.gnu.org/archive/html/info-gnu/2020-12/msg00003.html>`__
のめぼしい項目に集中してノートをつづる。

| :command:`read -e` may now be used with arbitrary file descriptors (:command:`read -u N`).

Readline が効いた状態と descriptors を指定することが両立可能になった。

| The ``select`` builtin now runs traps if its internal call to the ``read`` builtin
| is interrupted by a signal.

組み込みコマンド :command:`select` は、信号が :command:`read` の内部呼び出しに割
り込んだときにトラップするようになった。

| ``SRANDOM``: a new variable that expands to a 32-bit random number that is not
| produced by an LCRNG, and uses ``getrandom``/``getentropy``, falling back to
| :file:`/dev/urandom` or ``arc4random`` if available. There is a fallback generator if
| none of these are available.

環境変数 ``SRANDOM`` から 32 ビット長の乱数を得られる。ここに言及されているよう
な手段、関数で生成されるため、``srand`` のようなものを使って乱数列を再現すること
は不可能のようだ。

.. code:: console

   bash$ echo $SRANDOM
   3687839026
   bash$ echo $SRANDOM
   1135571563
   bash$ echo $SRANDOM
   2451151285

| ``shell-transpose-words``: a new bindable readline command that uses the same
| definition of word as ``shell-forward-word``, etc.
|
| The shell now adds default bindings for ``shell-forward-word``,
| ``shell-backward-word``, ``shell-transpose-words``, and ``shell-kill-word``.

新コマンド ``shell-transpose-words`` の意味は直観的に理解できると思うので説明を
省く（パス文字列などで ``transpose-words`` との違いを実感できる）。

ここで挙げたコマンドに対するキーバインド既定値は次のとおり：

.. csv-table::
   :delim: |
   :header: キーバインド,コマンド
   :widths: auto

   :kbd:`M-C-b` | ``shell-backward-word``
   :kbd:`M-C-d` | ``shell-kill-word``
   :kbd:`M-C-f` | ``shell-forward-word``
   :kbd:`M-C-t` | ``shell-transpose-words``

| If :command:`unset` is executed without option arguments, bash tries to unset a shell
| function if a name argument cannot be a shell variable name because it's not
| an identifier.

コマンド :command:`unset` をオプションなしで実行すると、引数を変数名として処理す
ることをまず試みる。それが失敗すると、今度は関数名として処理する。

| The :command:`test -N` operator uses nanosecond timestamp granularity if it's
| available.

ファイルが最後に読み込まれてからナノ秒単位の短時間の間に変更されたとしてもテスト
が機能するようになった。

| ``BASH_REMATCH`` is no longer readonly.

この環境変数は ``[[ target =~ pattern ]]`` テストの結果を格納する配列だ。
その読み取りしかできない性質がなくなったということは？

| :command:`wait`: has a new ``-p VARNAME`` option, which stores the PID returned by :command:`wait -n`
| or :command:`wait` without arguments.

コマンド :command:`wait` 実行時にプロセス ID を保存しておく事態になったらこれを
使おう。

| Sorting the results of pathname expansion now uses byte-by-byte comparisons
| if two strings collate equally to impose a total order; the result of a
| POSIX interpretation.

それでもなお等しいということはあり得ないか。

| Bash now allows ``SIGINT`` ``trap`` handlers to execute recursively.

これだけでは何のことかわからない。

| Process substitution is now available in posix mode.

プロセス置換が POSIX モードで利用可能になったことは本バージョンの注目項目の一つ
として紹介されている。

| ``READLINE_MARK``: a new variable available while executing commands bound with
| :command:`bind -x`, contains the value of the mark.

変数 ``READLINE_MARK`` はコマンド :command:`bind -x` で使用する Readline ライン
バッファー内の印の位置を含む変数だ。挿入点と印の間の文字列が region と呼ばれるもの
だ。

| :command:`test -v N` can now test whether or not positional parameter ``N`` is set.

``$1``, ``$2``, ... がセット済みかどうかを知る術は他にもある。

| ``local`` now honors the ``-p`` option to display all local variables at the
| current context.

今まで知らなかったが、実は ``local`` はシェル関数であったのだ。キーワードかと
思っていた。何らかの関数中で ``local -p`` を呼び出すと、上述のように機能する。

.. code:: shell

   function test-local {
       local a=3
       local b=Mono
       echo test local
       local -p
   }

実行結果の例（この出力と一致しない場合があり得る）：

.. code:: console

   bash$ test-local
   test local
   declare -- a="3"
   declare -- b="Mono"

| The ``@a`` variable transformation now prints attributes for unset array
| variables.
|
| The ``@A`` variable transformation now prints a declare command that sets a
| variable's attributes if the variable has attributes but is unset.

やってみよう：

.. code:: console

   bash$ declare -a myarray
   bash$ echo ${myarray@a}
   a
   bash$ echo ${myarray@A}
   declare -a myarray

| ``declare`` and ``local`` now have a ``-I`` option that inherits attributes and
| value from a variable with the same name at a previous scope.

これは入れ子スコープで変数を複製するのに利用できるだろうか。

| When run from a ``-c`` command, ``jobs`` now reports the status of completed jobs.

コマンド :command:`jobs` を :command:`bash -h` 中に実行するとジョブの実行状況を
確認できる。

| New ``U``, ``u``, and ``L`` parameter transformations to convert to uppercase,
| convert first character to uppercase, and convert to lowercase,
| respectively.

変数変換 ``${parameter@operator}`` において、``operator`` 部分にこれらの記号が対
応された。それぞれの変換は Emacs における ``upcase-word``, ``capitalize-word``,
``lowercase-word`` に相当すると憶えておくといい。

.. code:: console

   myvar=varName
   echo ${myvar@u} ${myvar@U} ${myvar@L}
   VarName VARNAME varname

| ``PROMPT_COMMAND``: can now be an array variable, each element of which can
| contain a command to be executed like a string ``PROMPT_COMMAND`` variable.

変数 ``PROMPT_COMMAND`` は ``PS1`` を表示する前に毎回実行されるコマンドを指定す
るものだ。複数のコマンドを実行するために配列を代入することが可能になった。例えば

.. code:: shell

   PROMPT_COMMAND=( "command1" "command2" ... )

とすると、端末でコマンドを何か入力、実行するたびに ``command1``, ``command2``, ...
がいちいち実行されるようになる。

| :command:`ulimit` has a ``-R`` option to report and set the ``RLIMIT_RTTIME`` resource.

コマンド :command:`ulimit` 自体を全く利用しないので後回し。

| Associative arrays may be assigned using a list of key-value pairs within
| a compound assignment. Compound assignments where the words are not of
| the form ``[key]=value`` are assumed to be key-value assignments. A missing or
| empty key is an error; a missing value is treated as ``NULL``. Assignments may
| not mix the two forms.

連想配列への key-value の代入および追加方法が次のような式が合法になるように拡張
された：

.. code:: console

   bash$ declare -A mymap=(k0 v0 k1 v1)
   bash$ echo "${mymap[@]}"
   v0 v1
   bash$ mymap+=(k2 v2 k3 v3)
   bash$ echo "${mymap[@]}"
   v0 v1 v2 v3

| New ``K`` parameter transformation to display associative arrays as key-
| value pairs.

連想配列の値を引用符で囲まれた可能性のある出力を生成する。先ほどの例の ``mymap``
に適用すると：

.. code:: console

   echo "${mymap[@]@K}"
   k0 "v0" k1 "v1" k2 "v2" k3 "v3"

| ``SECONDS`` and ``RANDOM`` may now be assigned using arithmetic expressions, since
| they are nominally integer variables. ``LINENO`` is not an integer variable.

そのようなことはしない。

| Bash temporarily suppresses the verbose option when running the ``DEBUG`` trap
| while running a command from the :command:`fc` builtin.

状況がわからない。

| :command:`wait -n` now accepts a list of job specifications as arguments and will
| wait for the first one in the list to change state.

オプションの ``-n`` は the next の意。この変更は理に適っている。

| ``HISTFILE`` is now readonly in a restricted shell.

制限シェル :command:`rbash` を起動して変数の属性を先ほど習った変数展開で調べる：

.. code:: console

   $ echo ${HISTFILE@a}
   r

| ``GLOBIGNORE`` now ignores ``.`` and ``..`` as a terminal pathname component.

環境変数 ``GLOBIGNORE`` はコロン区切りのパターンのリストであって、パス展開時に無
視されるパターンを定義する。Bash 5.1 からはドットおよびドットドットが端末パス名
構成要素としては無視されるようになったと言っている。

バージョン 5.2
======================================================================

.. todo::

   現在利用している Ubuntu 22.04.2 LTS の Bash はバージョンが 5.1 だ。本節以降を
   記すのは Ubuntu をアップグレードしてバージョンが 5.2 以上になってからとする。

参考資料
======================================================================

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
* `Bash 5.1 has already been released and these are its news | Linux Addicts <https://www.linuxadictos.com/en/bash-5-1-has-already-been-released-and-these-are-its-news.html>`__
* `bash - Is $PROMPT_COMMAND a colon-separated list? - Unix & Linux Stack Exchange <https://unix.stackexchange.com/questions/460651/is-prompt-command-a-colon-separated-list>`__
* `Bash fc Command : Easily Wield the Bash Shell Like a Pro <https://adamtheautomator.com/bash-fc-command/>`__
* その他、Bash Reference Manual やヘルプなど
