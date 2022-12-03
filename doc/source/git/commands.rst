======================================================================
コマンド
======================================================================

本節では Git_ のコマンドを、よくあるチートシートの形式で記していく。私にとって利
用価値が高いコマンドの用例を優先して掲載する。 Git はコマンドもオプションも数が
多くてとにかく憶えにくい。

.. contents::

記法規約
======================================================================

:doc:`./terminology` を参照。

共通オプション
======================================================================

ここでいう共通オプションとは、次のコマンド呼び出しの形式における
``[common-options]`` の部分に来るコマンドラインオプションのこととする。自分が使
う可能性の高いものを記す。

.. code:: console

   bash$ git [common-options] <command> [command-options] <args>

.. option:: --version

   Git 自身のバージョンを表示する。ほとんど全ての引数とオプションを無視するようだ。

.. option:: --help

   引数がない場合は、共通オプション一覧、いくつかの常用コマンド、特殊なヘルプの
   表示方法を出力する。引数がある場合は、それに関するヘルプをおそらくブラウザー
   で表示する。この場合は :command:`git help arg` と同等の動きをする。

.. option:: -C <path>

   作業ディレクトリーがまるで ``<path>`` であるかのように Git を振る舞わせるオプ
   ション。

   リポジトリーを操作するスクリプトを書くときに、いちいち :command:`cd` 系コマン
   ドを実行しなくて済む。このオプションは明らかに有用なので活用したい。

   * オプション :option:`--git-dir` や :option:`--work-tree` と組み合わせるとき
     に、これらが相対パスの形でディレクトリーを指定する場合には :option:`-C` か
     らの相対パスとしてみなされる点に注意。

.. option:: --no-pager

   Git がコンソールに長い出力をするときに、ページャーを使わせないようにするオプ
   ション。利用例としては、まとまった量のコミットログを出力するようなスクリプト
   を作成するときに適用を考える。

   * ページャーは定義されていれば環境変数 ``PAGER`` が、そうでなければ
     :command:`less` が使われる。

.. option:: --git-dir=<path>

   リポジトリーの管理部分本体、つまりディレクトリー :file:`.git` のあるパスを指
   定する。尋常でない場所に :file:`.git` があるような場合に用いるのだろう。

.. option:: --work-tree=<path>

   作業コピーのパスを指定する。リポジトリーに対して普通でない場所に作業コピーを
   持つときに用いるのだろう。

高水準コマンド
======================================================================

ヘルプドキュメントによる用途別分類をここで利用させてもらう。

主力コマンド
----------------------------------------------------------------------

Git 利用者の必修コマンドのようなものか。ヘルプドキュメントによる一覧を見てみる
と、私が利用したことがないコマンドが多数ある。

まずはメインとされているコマンド群の名称を記す。

.. code:: text

   add,
   am,
   archive,
   bisect,
   branch,
   bundle,
   checkout,
   cherry-pick,
   citool,
   clean,
   clone,
   commit,
   describe,
   diff,
   fetch,
   format-patch,
   gc,
   grep,
   gui,
   init,
   log,
   merge,
   mv,
   notes,
   pull,
   push,
   rebase,
   reset,
   revert,
   rm,
   shortlog,
   show,
   stash,
   status,
   submodule,
   tag,
   worktree.

そして私が常用するものと利用したいもののコマンドライン群、「呪文表」を次に示す。
よくあるチートシートである。

以下、コマンドライン内の :command:`git [common-options]` の部分は省略する。あ
と、Git 特有の符牒ではなく、実際にありがちな名前を例に使うかもしれない。例えば
``<tree-ish>`` ではなく ``master`` とか ``HEAD`` とかを敢えて使う。

呪文表 :command:`add`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`add` はインデックスにファイルおよびその変更を追加するのに用い
る。

``add [<pathspec>...]``
  指定したファイルだけをインデックスに追加する。

  引数なしの場合に何が起こるのかは知らない。

``add .``
  カレントディレクトリー以下の対象ファイルをインデックスに追加する。

:command:`add -p <pathspec>`
  指定したファイルの内部から追加部分を対話的に指示し、インデックスに追加する。

:command:`add -i`
  コンソールで対話的にファイルをインデックス追加処理する。

``add -u [<pathspec>...]``
  作業ディレクトリー配下にあるファイルのうち、既にバージョン管理中のもののみをコ
  マンドの対象とする。

  .. csv-table::
     :delim: @
     :header: 状態,インデックス

     新規ファイル @ インデックスに影響しない
     変更ファイル @ インデックスに更新対象として追加
     削除ファイル @ インデックスに削除対象として追加

  デフォルトの ``-a`` オプションとの違いに注意。

呪文表 :command:`archive`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`archive` は作業コピーのファイル全部から圧縮ファイルを作成する
のに利用できる。

``archive --format=tar.gz --prefix=prjname/ master > prjname-master.tar.gz``
  ツリー ``master`` から tar.gz 形式の圧縮ファイルを作る。

``archive master | bzip2 > source-tree.tar.bz2``
  ツリー ``master`` から tar.bz2 形式の圧縮ファイルを作る。

``archive --format=zip --prefix=projname/ master > projname.zip``
  ツリー ``master`` から zip 形式の圧縮ファイルを作る。

呪文表 :command:`bisect`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`bisect` は異色のコマンドで、コミットを二分探索法によって検索
するものだ。

:command:`bisect help`
  当コマンドの利用法の概要をコンソールに出力する。詳細を見たい場合はやはり
  :command:`help bisect` である。

:command:`bisect start HEAD v1.2`
  二分探索セッションを開始する。これは ``HEAD`` で何かマズいことになっているが、
  確か ``v1.2`` 時点では正常だった、の例。

:command:`bisect good [<rev>]`
  このリビジョンは正常だという印をセッション情報に付ける。

:command:`bisect bad [<rev>]`
  このリビジョンは何かマズイという印をセッション情報に付ける。

:command:`bisect visualize`
  現時点で残っている疑わしいものを :command:`gitk` で表示する。

  * :command:`bisect view` とタイプしても同じ。短いほうが良い。

:command:`bisect reset`
  セッションを終了して、作業コピーの状態を :command:`bisect start` 直前のものに
  戻す。

呪文表 :command:`branch`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`branch` はブランチを管理するのに用いる。

:command:`branch <new> [<existing>]`
  新規ブランチ ``new`` を既存ブランチ ``existing`` から作成する。既存ブランチの
  指定を省略すると、カレントブランチから作成する。

:command:`branch -r`
  リモート追跡ブランチだけをリストする。

:command:`branch -a`
  ローカルとリモート追跡の両方のブランチをリストする。

  * ``-v`` でより詳しく。

:command:`branch --merged`
  カレントブランチに対して完全にマージ済みのブランチ全てをリストする。

:command:`branch --track <branchname> [<start-point>]`
  リモート追跡ブランチ ``branchname`` を作成する。意味としてはリモートにある
  ``start-point`` からブランチするイメージか。

:command:`branch --set-upstream <branch> <start-point>`
  既存のブランチ ``branch`` を ``start-point`` のリモート追跡ブランチにする。

:command:`branch -m [oldbranch] <newbranch>`
  ブランチ ``oldbranch`` の名前を ``newbranch`` に変更する。引数 ``oldbranch``
  の指定を省略すると、カレントブランチを改名する。

  * ``-M`` is ``-m --force``.

:command:`branch -d <branchname>`
  ブランチ ``branchname`` を削除する。ただし、別のブランチにマージ済みであると失
  敗してくれる。

  * ``-D`` is ``-d --force``.

:command:`branch -dr <remote/branchname>`
  リモート追跡ブランチを削除する。マージ済みが条件。

  * 影響を受けるのはローカルの状態だけ。

呪文表 :command:`checkout`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`checkout` にはブランチを切り替える用法と、作業コピーのファイ
ルを復元する用法の両方があることに注意したい。

:command:`checkout <branch>`
  カレントブランチを既存のブランチ ``branch`` に切り替える。

:command:`checkout -b <branch> [<start-point>]`
  ブランチ ``branch`` を作成して、同時にカレントブランチを切り替える。明示的に
  ``start-point`` が指定されていれば、そこからブランチする。

:command:`checkout -b <branch> <remote>/<branch>`
  リモートブランチをローカルブランチとして作成する。

:command:`checkout --track <remote>/<branch>`
  リモートブランチからリモート追跡ブランチを作成する。

:command:`checkout HEAD <file>`
  ファイル ``file`` のローカルでの変更を破棄する。

:command:`checkout -- <file>`
  ファイル ``file`` のローカルでの変更を破棄する。

:command:`checkout .`
  カレントディレクトリー以下のローカルでの変更をすべて破棄する。

:command:`checkout <branch> <file>`
  別のブランチ ``branch`` にあるファイル ``file`` をカレントブランチへ持ってく
  る。

呪文表 :command:`clean`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`clean` の役割は、バージョン管理されていないファイルを消去する
ことである。

:command:`clean -n`
  仮に :command:`clean` を実行すると、何が起こるのかをプレビューする。

  オプション ``-n`` は他のコマンドでも dry run の意味でサポートされている場合がある。
  まとめたほうがよいかも。

:command:`clean -f`
  Git の構成に依らず、とにかく削除する。

呪文表 :command:`clone`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`clone` はリポジトリーを新規ディレクトリーに複製する。これによ
り作業コピーができる。

:command:`clone <repository> [<directory>]`
  リポジトリー ``repository`` の作業コピーを ``directory`` に作成する。

  ``repository`` には普通なんちゃら ``.git`` のような文字列が来る。
  たまにローカルにある作業コピーのパスを指示するような場合もある。

呪文表 :command:`commit`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`commit` はリポジトリーの変更を確定するために用いる。そしてコ
ミットを修正することもできる。

:command:`commit -a`
  自動的に変更ファイルと削除ファイルをステージに置いてコミットする。

:command:`commit -m <msg>`
  コミットログメッセージを ``msg`` としてコミットする。

  * もっとも普通のコミットコマンドの形式。
  * ログメッセージは普通は引用符で囲む。

:command:`commit -v`
  リポジトリーの変更情報を表示しながらコミットする。

:command:`commit --amend`
  直前のコミットを修正する。

:command:`commit --amend <file> ...`
  直前のコミットに変更ファイルを追加してコミットをやり直す。

:command:`commit --amend --reset-author [--no-edit]`
  直前のコミットの作業者情報を上書きする。

  * タイムスタンプを更新することに注意。
  * オプション ``--no-edit`` を併用すれば、ログメッセージを再利用できる。

.. todo::

   * タイムスタンプが 2 種類あることについて言及する。
   * タイムスタンプを任意のタイミングに指定する方法について言及する。

呪文表 :command:`diff`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`diff` は相異なるコミット間の差分や、特定コミットと作業コピー
との差分を表示する。ファイル単位で差分を確認することができるが、ここに挙げる例は
対象ファイル全部になる。

:command:`diff HEAD`
  指定ファイル群について、作業コピーとレポジトリーの最新リビジョン ``HEAD`` との
  差分を表示する。

:command:`diff --cached`
  作業コピーとステージとの差分を表示する。

  別名 ``--staged`` がある。

:command:`diff --no-index <file1> <file2>`
  ファイルの差分をバージョン管理の文脈と無関係に表示する。
  単に GNU diff を利用するのが素直だ。

呪文表 :command:`fetch`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`fetch` はよそにあるリポジトリーからデータをダウンロードする。

:command:`fetch [bookmark]`
  リポジトリブックマークからすべての履歴をダウンロードします。

:command:`fetch <repository> [<branch>]`
  リモートリポジトリー ``repository`` からブランチ ``branch`` をダウンロードす
  る。

:command:`fetch <remote> -p`
  リモート ``remote`` に関してデータをダウンロードし、削除済みリモートブランチが
  あれば、それに対応するリモート追跡ブランチをローカルにおいて削除する。

:command:`fetch --all --prune`
  すべてのリモートリポジトリーからダウンロードする。なおかつ、削除済みリモートブ
  ランチがあれば、それに対応するリモート追跡ブランチをローカルにおいて削除する。

  * ``--prune`` is ``-p``.

呪文表 :command:`format-patch`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

パッチを作成するコマンド。滅多に使わない。

:command:`format-patch HEAD^`
  最新のコミットのパッチを生成する。これは別のクローンまたはブランチにコマンド
  :command:`am` が適用する。

:command:`format-patch <rev>^..<rev>`
  単一リビジョンにおけるパッチを作成する。

呪文表 :command:`gc`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`gc` は不要ファイルを削除してローカルリポジトリーの最適化をす
る。気分転換の意味で実行することが多い。

:command:`gc [--prune[=<date>]]`
  リポジトリーのゴミ掃除を行う。

  オプション ``--prune`` は未参照オブジェクトを削除するかどうかのフラグだ。これ
  は既定で on である。

呪文表 :command:`grep`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

オプションにもよるが、リポジトリー管理対象ファイル限定版 :command:`grep` と表現
できる。それ以外は GNU :command:`grep` と同じように利用できる。

と言うわけで、ここにはコマンドラインを記さない。

呪文表 :command:`init`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`init` はリポジトリーを（再）作成する。

:command:`init [directory]`
  ディレクトリー ``directory`` を Git リポジトリーとして初期化する。

:command:`init --bare [directory]`
  ディレクトリー ``directory`` に生リポジトリーを作成する。理解としてはディレク
  トリー :file:`.git` の初期状態を生成するものだ。

呪文表 :command:`log`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`log` はコミットログを出力する。構文はたいへん単純だが、オプ
ションが多いので実は憶えにくい。

:command:`log`
  引数オプション一切なしでは全ログを出力することになる。新しい順。

:command:`log --decorate`
  関係するブランチとタグがあれば、そのコミットのログにはそれらの名前を一緒に出力
  する。

:command:`log <ref>..<ref>`
  指定リビジョン範囲におけるコミットに限定してログを出力する。

:command:`log [--] <path>...`
  指定したファイルやディレクトリーに関係するコミットに限定してログを出力する。

:command:`log -<number>`
  指定したコミット数だけログを出力する。

  別名 ``-n <number>`` および ``--max-count <number>`` がある。

:command:`log --after="MMM DD YYYY"`
  指定期日よりも新しいコミットに限定してログを出力する。

  別名 ``--since`` がある。

:command:`log --before="MMM DD YYYY"`
  指定期日よりも古いコミットに限定してログを出力する。

  別名 ``--until`` がある。

:command:`log --author=<pattern>`
  執筆者がパターン ``pattern`` にマッチするコミットに限定してログを出力する。

:command:`log --grep=<pattern>`
  ログメッセージがパターンにマッチするコミットに限定してログを出力する。

:command:`log --merge`
  マージで衝突があったものに限定してログを出力する。

:command:`log --pretty=short`
  短いフォーマットでログを出力する。

:command:`log --format=oneline`
  コミット当たり一行でログを出力する。先頭に SHA-1 付き。

:command:`log --oneline`
  コミット当たり一行でログを出力する。

:command:`log --oneline --graph --all --decorate`
  色んな物をログとして出力する。

:command:`log --graph`
  アスキーアートによるコミットグラフをメッセージの左に添える。

:command:`log -p`
  変更内容を表示する。

:command:`log -p <file>`
  ファイル ``file`` が関係するコミットに限定して、変更内容を込めてログを出力する。

:command:`log --stat`
  差分に関する統計を添えてログを出力する。

:command:`log --summary`
  ファイルの作成、移動、削除に関する概要を添えてログを出力する。

:command:`log --color`
  差分に色を付けてログを出力する。
  オプション単体では意味がないようだ。

呪文表 :command:`merge`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`merge` はカレントブランチに別のブランチのコミット履歴を取り込
む。

:command:`merge <branch>`
  ブランチ ``branch`` のコミット履歴をカレントブランチに統合する。

:command:`merge --no-commit <branch>`
  ブランチ ``branch`` をカレントブランチにマージするが、新しいコミットを自動的に
  作らない。

:command:`merge -s ours <branch>`
  ブランチ ``branch`` をカレントブランチにマージするが、何か衝突がある場合はこち
  ら側の変更を採用する。

:command:`merge --no-ff <branch>`
  ブランチ ``branch`` をカレントブランチにマージするが、それが fast-forward で解
  決してもマージコミットを生成する。

:command:`merge -ff-only <branch>`
  次のような場合はマージしないで異常終了とする。

  * カレントの ``HEAD`` が既に最新である
  * マージが fast-forward で解決する

:command:`merge --abort`
  現在のマージが衝突したら処理を中止して、状態をマージ直前に復元することを試み
  る。

呪文表 :command:`mv`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`mv` はファイルを移動する、もしくは名前を変える。ファイルは
ディレクトリーとシンボリックリンクを含む。

:command:`mv <source> <destination>`
  ファイル ``source`` を ``destination`` に移動するか、名前を変える。

  引数 ``source`` が複数ファイルの場合は、引数 ``destination`` は既存のディレク
  トリーであるものとする。

呪文表 :command:`pull`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`pull` は :command:`fetch` と :command:`merge` を同時に行うよ
うなものだ。

:command:`pull [<repository>]`
  カレントブランチのリモートリポジトリー ``repository`` のコピーをダウンロードし
  て、それを直ちにローカルの ``HEAD`` にマージする。

:command:`pull [<repository> [<refspec> ...]]`
  リモートリポジトリー ``repository`` のブランチ ``refspec`` に対して、そのコ
  ピーをダウンロードしてローカルの ``HEAD`` にマージする。

  ところで ``repository`` や ``refspec`` のデフォルト値は、カレントブランチの構
  成に依存する。

:command:`pull --rebase <repository>`
  これは :command:`fetch` と :command:`rebase` を同時に行うようなものだ。上手い
  人向けのコマンド。

呪文表 :command:`push`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`push` はローカルのコミットをリモートにアップロードする。

:command:`push [<repository> [<refspec> ...]]`
  ローカルの ``refspec`` をリモートリポジトリー ``repository`` にアップロードす
  る。

  なお、これらの引数のデフォルト値はカレントブランチの構成に従う。

:command:`push --all [<repository>]`
  ローカルのすべてのブランチをリモートリポジトリー ``repository`` にアップロード
  する。

  言い換えると ``refs/heads/`` 配下の refs をリモートリポジトリーにアップロード
  する。

:command:`push --mirror`
  ローカルのすべての状態とリモートリポジトリーの状態が同一となるようにアップロー
  ドする。

  言い換えると ``refs/`` 配下をリモートリポジトリーにコピーする。

:command:`push --tags`
  ``refs/tags`` 配下にあるすべての refs をアップロードする。

:command:`push -n`
  コマンド実行時のプレビューができる。

  別名 ``--dry-run`` がある。

:command:`push --force <repository>`
  マージが fast-forward にならない :command:`push` であっても、強引にアップロー
  ドする。

:command:`push <repository> :<pattern>`
  リモートリポジトリー ``repository`` にパターン ``pattern`` にマッチする ref が
  あれば、それを削除する。

:command:`push --delete <repository> <pattern>`
  同上。

:command:`push <repository> <start-point>:refs/heads/<branch>`
  リモートリポジトリー ``repository`` にブランチ ``branch`` を作成する。ブランチ
  の基点はリモートの ``start-point`` とする。

呪文表 :command:`rebase`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`rebase` は私にとってはコミット履歴の修正ツールだ。

:command:`rebase [<upstream> [<branch>]]`
  ブランチ ``upstream`` をブランチ ``branch`` に :command:`rebase` する。

:command:`rebase -i [<upstream> [<branch>]]`
  テキストエディター上でコミット履歴の操作を行う。

  テキストエディター上にはコミット履歴が各行にリストされている。そこで各行の先頭
  にコミット操作命令をタイプしてエディターを終了すると、いい感じにコミット履歴が
  改竄される。

  例えば次のことができる：

  * コミットログを修正する
  * 複数のコミットの順序を交換する
  * 複数のコミットを合併する
  * コミットをキャンセルする

  :command:`rebase -i HEAD~5`
    直近 5 コミットの履歴の改竄を開始する。

:command:`rebase --continue`
  手動による衝突を解消してインデックスが望み通りの状態になったとき
  に、:command:`rebase` 処理の対象を次のコミットへ進ませる。

:command:`rebase --abort`
  手動による衝突解消が上手くいかなかったときに、:command:`rebase` 開始直前の状態
  に戻す。

:command:`rebase --skip`
  衝突したままだが、とにかく次のコミットへ :command:`rebase` 処理を進ませる。

呪文表 :command:`reset`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`reset` はカレントの HEAD を指定した状態へ戻すのに用いる。用法
にはファイルに作用するものと、コミットに作用するものがある。

:command:`reset <paths>...`
  インデックスでファイル ``paths`` に関する項目をリセットする。

  ヘルプでは ``add <paths>...`` の逆操作だと表現している。

:command:`reset <commit>`
  カレントブランチの HEAD をコミット ``commit`` にリセットする。インデックスの状
  態もそれに応じてリセットする

:command:`reset --soft HEAD^`
  カレントブランチの状態を直前のコミット直後の状態にリセットする。ローカルでの作
  業はインデックス外に作業コピーに残る。

:command:`reset --hard`
  衝突したパッチを破棄する。

:command:`reset --hard <commit>`
  カレントブランチの ``HEAD`` をコミット ``commit`` 直後の時点にリセットする。そ
  れ以降になされた作業コピーにおけるファイル変更は破棄される。

:command:`reset --hard HEAD`
  カレントブランチの状態を直前のコミット直後の状態にリセットする。コミット以後の
  ローカルでの作業があれば、それは破棄される。

:command:`reset --hard ORIG_HEAD`
  マージが成功したコミットのうち最新のものをアンドゥする。例によってそれ以降の作
  業コピーでのファイル変更は破棄される。

:command:`reset --keep <commit>`
  カレントブランチの ``HEAD`` をコミット ``commit`` 直後の時点にリセットする。そ
  れ以降になされた作業コピーにおいてファイル変更があれば、リセットを中止する。

呪文表 :command:`revert`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`revert` は既存のコミットを無効にするのに用いる。

:command:`revert <commit>`
  コミット ``comit`` をなかったことにする。方法はそのコミットの内容を打ち消すよ
  うな新しいコミットを生み出すことによる。

``-n`` または ``--no-commit`` オプションというのがあり、これは新しいコミットを生
じない。

呪文表 :command:`rm`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`rm` はリポジトリーからファイルを削除する。

:command:`rm [--] <file>...`
  ファイル ``file`` を削除する。

:command:`rm -n`
  コマンド実行時のプレビューができる。

  別名 ``--dry-run`` がある。

:command:`rm -r [--] <directory>`
  ディレクトリー ``directory`` 以下にあるすべてのファイルを削除する。

:command:`rm --cached [--] <file>`
  ファイル ``file`` をインデックスからのみ削除する。

呪文表 :command:`show`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`show` はあらゆる Git オブジェクトを表示する。

:command:`show <commit>`
  コミット ``commit`` との現在の差分を表示する。

:command:`show <commit>:<file>`
  コミット ``commit`` でのファイル ``file`` の内容を表示する。

:command:`show --name-only`
  変更ファイルの名前だけを表示する。差分は表示しない。

:command:`show <branch> -- <file>`
  ブランチ ``branch`` でのファイル ``file`` の内容を表示する。

呪文表 :command:`stash`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`stash` は作業コピーでのファイル変更を一時的に退避するのに用い
る。スタックのイメージだと思う。

:command:`stash list`
  退避領域の内容を一覧で示す。

:command:`stash show <stash> -p`
  退避領域の内容物を表示する。差分形式で表示できる。

:command:`stash drop`
  直近に一時保存された変更セットを破棄する。

:command:`stash pop`
  直近に一時保存されたファイルを作業コピーへ復元する。

:command:`stash apply`
  直近に一時保存されたファイルを作業コピーへ復元する。ただし保存データはまだ退避
  領域にある。

:command:`stash save <message>`
  現在の作業コピーでの変更ファイルを退避する。この退避には名前が付く。

:command:`stash clear`
  退避領域を完全に消去する。退避内容は失われる。

呪文表 :command:`status`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`status` は作業コピーの状態を表示するのに用いる。

:command:`status`
  引数なしでも色々と情報が得られる。

:command:`status -uno`
  管理外のファイルの情報は要らない。つまり ``Untracked files:`` のセクションを表
  示させない。

呪文表 :command:`submodule`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`submodule` はサブモジュールを管理するのに用いる。

:command:`submodule add <repository> [<path>]`
  リモートリポジトリー ``repository`` を ``path`` に追加する。

:command:`submodule update [--init]`
  登録済みサブモジュールを更新する。

:command:`submodule foreach <command>`
  シェルコマンド :command:`command` を各サブモジュールに対して実行する。

呪文表 :command:`tag`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`tag` はタグを管理するのに用いる。

:command:`tag <tagname> [<commit>|<object>]`
  コミットや何かにタグを付ける。

:command:`tag -d <tagname>`
  名前を指定してタグを削除する。

:command:`tag -l [<pattern>]`
  パターンにマッチするタグをリストする。

補助コマンド
----------------------------------------------------------------------

ヘルプドキュメントは補助コマンド群を操作目的のものと問い合わせ目的のものに分けて
紹介している。

次のコマンド群が操作用とされている：

.. code:: text

   config,
   fast-export,
   fast-import,
   filter-branch,
   mergetool,
   pack-refs,
   prune,
   reflog,
   relink,
   remote,
   repack,
   replace.

そして次のコマンド群が問い合わせ用とされている：

.. code:: text

   annotate,
   blame,
   cherry,
   count-objects,
   difftool,
   fsck,
   get-tar-commit-id,
   help,
   instaweb,
   merge-tree,
   rerere,
   rev-parse,
   show-branch,
   verify-commit,
   verify-tag,
   whatchanged.

呪文表 :command:`config`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`config` は各種構成オプションを設定するのに用いる。ユーザー固
有の設定、リポジトリー固有の設定、グローバル設定すべてをこれでまかなう。

:command:`config --global user.name <name>`
  コミットログに含まれる著者の名前を設定する。

:command:`config --global user.email <address>`
  コミットログに含まれるメールアドレスを設定する。

:command:`config --global color.ui auto`
  コマンドラインの出力を見やすくする色を設定する。

:command:`config --list`
  すべてのオプションを表示する。何かテキトーな順番で表示されるので、ソートにパイ
  プしたい。

:command:`config -e [--global]`
  テキストエディターでファイル :file:`.git/config` や :file:`~/.gitconfig` を編
  集する。

呪文表 :command:`reflog`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`reflog` は Git 操作自体の履歴情報を管理するのに用いる。履歴の
改竄作業のヒントになる。

:command:`reflog [show] --relative-date`
  番号の代わりに現在からの時間差を表示する。
  例えば ``HEAD@{7}`` などではなく ``HEAD@{8 days ago}`` などのような表示になる。

:command:`reflog [show] --all`
  すべての ref を表示する。

呪文表 :command:`remote`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`remote` はリモートリポジトリーおよびそれに関係のあるブランチ
の管理をする。

:command:`remote -v`
  饒舌オプション。

:command:`remote add <name> <url>`
  リモートリポジトリー ``url`` を追加して、ここでは ``name`` と呼ぶ。

:command:`remote add -t master -m master origin <url>`
  リモートリポジトリー ``url`` を追加する。ブランチ ``master`` の追跡ブランチを
  ``origin`` という名前で追加する。

:command:`remote set-url origin newurl`
  ``origin`` のリモートリポジトリーの URL が ``newurl`` に変更されたので、ローカ
  ル側で管理している URL 情報を更新する。

:command:`remote show <repository>`
  リモートリポジトリー ``repository`` の情報を表示する。

:command:`remote prune <repository>`
  リモートリポジトリー ``repository`` 側では既に存在しないブランチに対応するリ
  モート追跡ブランチを削除する。

:command:`remote -v update`
  リモートリポジトリーから更新データをダウンロードする。

呪文表 :command:`blame`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`blame` はあるファイルの各行について、リビジョンと著者を表示す
るというものだ。変なソースコードだなと思ったらこれを使うのもよいだろう。

:command:`blame [<rev>] <file>`
  リビジョン ``rev`` 時点でのファイル ``file`` の各行の著者を表示する。

呪文表 :command:`help`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`help` は当然ながらヘルプ機能を供するものだ。

:command:`help [-w] [<command>]`
  コマンド :command:`command` のヘルプドキュメントをブラウザーで開く。

:command:`help -a`
  一度は試すことを勧める。

:command:`help -g`
  一度は試すことを勧める。

呪文表 :command:`whatchanged`

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`whatchanged` は :command:`log` に似ているが、よくわからない。

:command:`whatchanged <file>`
  ファイル ``file`` のコミットログと、何かの変更を表示する。

外部連携コマンド
----------------------------------------------------------------------

ヘルプによると、次のコマンド群が外部連携コマンドとして位置づけられている。他の
バージョン管理システムとのデータ変換という意味と、他の利用者とのリポジトリーデー
タの交換という意味があるようだ。

.. code:: text

   archimport,
   cvsexportcommit,
   cvsimport,
   cvsserver,
   imap-send,
   p4,
   quiltimport,
   request-pull,
   send-email,
   svn.

コマンド名には CVS やら Perforce やら、懐かしいバージョン管理システムの名前が見
受けられる。私個人が自由に管理できた Subversion のリポジトリーはすべて Git に変
換済みなので、これらのコマンドが行うであろう機能は私にとってもはや興味がない。

低水準コマンド
======================================================================

ここから先に記すコマンドは、ドキュメントでは低水準コマンドという括りになっている。
一般利用者にとっては実行頻度が低いものということだ。

操作コマンド
----------------------------------------------------------------------

リポジトリーにあるオブジェクトやインデックスを操作するコマンド群である。

.. code:: text

   apply,
   checkout-index,
   commit-tree,
   hash-object,
   index-pack,
   merge-file,
   merge-index,
   mktag,
   mktree,
   pack-objects,
   prune-packed,
   read-tree,
   symbolic-ref,
   unpack-objects,
   update-index,
   update-ref,
   write-tree.

呪文表 :command:`hash-object`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`hash-object` はファイルのオブジェクト ID を計算する。

:command:`hash-object <file>`
  ファイル ``file`` のオブジェクト ID を計算して SHA1 値として出力する。

問い合わせコマンド
----------------------------------------------------------------------

ヘルプによると、次のコマンド群は問い合わせるのに用いるものとして位置づけられている。
原則的にこれらは作業コピーのファイルを :command:`touch` しないコマンドということ
になっているので、安心して実行してよさそうだ。

.. code:: text

   cat-file,
   diff-files,
   diff-index,
   diff-tree,
   for-each-ref,
   ls-files,
   ls-remote,
   ls-tree,
   merge-base,
   name-rev,
   pack-redundant,
   rev-list,
   show-index,
   show-ref,
   unpack-file,
   var,
   verify-pack.

呪文表 :command:`ls-files`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`ls-files` はインデックスと作業コピーに限定した :command:`ls`
のようなものである。テキスト一括処理の対象ファイルを絞るツールとして活用したい。

:command:`ls-files --other --ignored --exclude-standard`
  作業コピーにあるすべての管理対象外ファイルをリストする。

次のものはシェルでインデックスから削除されたファイルを本当に削除するときのコマン
ド例だ：

.. code:: console

   bash$ rm $(git ls-files --deleted)

作業コピー管理内のファイルに限定して、何らかの文字列挿入・置換・削除をしたい場合
がかなりある。そのときは次のようなワンライナーで一気に片付く。次にファイル内の文
字列 ``OLD_PATTERN`` を ``NEW_PATTERN`` に置換する例を示す。

.. code:: console

   bash$ git ls-files -z | xargs -0 sed -i -e 's/OLD_PATTERN/NEW_PATTERN/g'

呪文表 :command:`ls-remote`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コマンド :command:`ls-remote` はリモートリポジトリーの参照をリストする。

:command:`ls-remote <repositry> [HEAD]`
  リモートリポジトリー ``repository`` の ``HEAD`` 時点での参照をリストする。左列
  が ID で右列がブランチとタグ。

同期コマンド
----------------------------------------------------------------------

ヘルプによると、次のコマンド群は同期コマンドとして位置づけられている。一般ユー
ザー用のコマンドと、実装用コマンドに分けてリストされている。ここではどちらも私の
興味がないということで、一気に名前のみを挙げる。

次のコマンド群が操作用とされている：

.. code:: text

   daemon,
   fetch-pack,
   http-backend,
   send-pack,
   update-server-info.

次のコマンド群が実装用とされている：

.. code:: text

   http-fetch,
   http-push,
   parse-remote,
   receive-pack,
   shell,
   upload-archive,
   upload-pack.

内部コマンド
----------------------------------------------------------------------

ヘルプによると、次のコマンド群は内部コマンドとして位置づけられている：

.. code:: text

   check-attr,
   check-ignore,
   check-mailmap,
   check-ref-format,
   column,
   credential,
   credential-cache,
   credential-store,
   fmt-merge-msg,
   interpret-trailers,
   mailinfo,
   mailsplit,
   merge-one-file,
   patch-id,
   sh-i18n,
   sh-setup,
   stripspace.

もっとも <end users typically do not use them directly> とのことなので、私も当然
利用しない。

.. include:: /_include/git-refs.txt
