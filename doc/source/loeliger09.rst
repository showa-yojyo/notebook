======================================================================
実用 Git 読書ノート
======================================================================

.. include:: /_include/book-details/loeliger09.txt

書名には「実用」とあるが、個人的には Git の理論解説書として読んだ。 Git はその基
礎概念をしっかり理解することが、要領良く習得することに直結する。例えばインデック
ス、ツリー、ブロブ等の重要概念を押さえていないとダメであることが本書を読んでわ
かった。私の場合では、なかなか覚えられない Git のコマンドがいくつかあったのだ
が、それがどの構成要素に作用するのかを理解していないから覚えられないということが
ようやくわかった。

特に 9, 10, 11 章のマージ、コミット、リモートリポジトリの各内容を着実に理解でき
れば OK だろう。

.. todo::

   以下、書き殴りメモ。いつか整理するはず。

* 4.1.2 blob tree commit tag
* 4.1.3 index ←→ merge object ←→ SHA1
* 4.3

  * :command:`git cat-file -p 3b18e51...`
  * :command:`git rev-parse 3b18e51...`
  * :command:`git ls-files -s`

* 4.3.6 :command:`git show --pretty=fuller`
* 4.3.7 :command:`git tag -m "～" V1.0 3ede452`
* あとで p. 38 fig 4.1 を確認。
* 5 index commit stage

  * :command:`git status` は index の status
  * status ::= (tracked|ignored|untracked)

* 5.3 :command:`git ls-files --stage`
* :command:`git rm --cached XXX` →アンステージ
* 5.4.1 :command:`git commit -a`
* 5.6 :command:`git log --follow XXX`
* 5.7 ``mv`` 系はツリーだけに影響する。
* 5.8 :file:`.gitignore` は下位フォルダーの方が強い。
* 5.9 index を tree と同じシンボルで図示している。

  * master とか HEAD とかいきなり出てくる？
  * ※index を「仮想的な tree」とみなす。

* 直接的な参照 SHA1 c.f. 間接的な参照 e.g. "HEAD"
* 6.2.1 :command:`git log -1 --pretty=oneline XXX`
* 6.2.2 symref

  .. code:: text

     refs/
       heads/～
       remotes/～  origin/master は本当は refs/remotes/origin/master
       tags/～

* HEAD ::= current branch の最新のコミット
* XXX_HEAD というような名前のシンボルが他に 3 つある。
* 6.2.3 ``C^`` とか ``C~`` とか。``^`` は複数で ``~`` は世代か？

  * :command:`git show-branch --more=35 | tail -10`

* 6.3.1 :command:`git log` は :command:`git log HEAD` （到達可能）
* 6.3.3 ``M~12..M~10`` では 12 のは含まない。

  * ``A...B`` で symmetric difference を意味する。

* 6.4.1 :command:`git bisect`
* 6.4.2 :command:`git blame`
* :command:`git merge-base オリジナル 新`
* :command:`git branch ブランチ [コミット]`
* :command:`git branch`, :command:`git show-branch`, ``[-r -a]``, ``*`` 印がカレ
  ント。
* :command:`git checkout ブランチ` でスイッチする。
* 7.7.3 :command:`git checkout -m` でローカルの変更を新しい working directory に
  持ち込む（マージ）。
* 7.7.4 :command:`git checkout -b 新ブランチ`
* 7.7.5 detached HEAD
* 7.7.8 :command:`git branch -d XXX`

  * :command:`git merge bug/pr-3` して :command:`git branch -d bug/pr-3` する。

* 8.1

  .. code:: text

     git diff                           ←作業コピーと index との比較
     git diff コミット                  ←p. 114 fig. 8-1
     git diff --cached コミット
     git diff コミット1 コミット2

* 8.2 「インデックスと HEAD との比較」←→ステージ

  .. code:: text

     git diff           ←作業コピーと index との比較
     git diff HEAD      ←作業コピーと HEAD との比較
     git diff --cached  ←index と HEAD との比較

     git diff HEAD^ HEAD

* 8.4

  .. code:: text

     git diff --stat master~5 master Documentation
     git diff -S "octopus" master~50

* 9.1

  .. code:: text

     git checkout ブランチ
     git merge 別ブランチ

* 9.1.2

  .. code:: text

     git checkout -b alternate master~
     git log --graph --pretty=oneline --abbrev-commit

* 9.1.3 :command:`git merge なんとか` の直後に commit する→
  :command:`git diff` で見る→テキスト編集→
  :command:`git add ファイル` →
  :command:`git commit`

* 9.2.1 :command:`git status` :command:`git ls-files -u`
* 9.2.2.1 :command:`git diff MERGE_HEAD`

  * :command:`git log --merge --left-right -p`
  * :command:`git diff :1:hello :3:hello`

* 9.2.5

  .. code:: text

     git reset --hard HEAD        ←マージ中断
     git reset --hard ORIG_HEAD   ←マージを破棄

* 9.3 マージ基点、3-way merge, criss cross (pp. 146-147)
* 9.3.1 already up-to-date VS fast forward

  * 同じ祖先を持つ？
  * 追跡ブランチ上でよく起こる。

* 9.3.2

  * resolve
  * recursive
  * octopus

  :command:`git merge -s resolve Bob`

* 9.4.2 squash commit
* 10.2 :command:`git reset` は作業コピーをいじるコマンド。soft, mixed, hard
* 10.3 :command:`git cherry-pick dev~2`
* 10.6 :command:`git commit --amend`
* 10.7 :command:`git rebase`: 基点の変更
* 11.1.1 base
* 11.1.2

  * :command:`git clone 元リポジトリー 新クローン`
  * :command:`git clone git://～/～.git`
  * origin と呼ばれるリモート

* 11.1.3

  * :command:`git fetch`
  * :command:`git pull` →変更マージあり
  * :command:`git push`
  * :command:`git ls-remote`

* 11.3.1 :command:`git clone --bare すでにリポジトリー 新.git`
* 11.3.2

  * :command:`git remote add origin /tmp/Depot/public_html` → :file:`.git/config` が書き換わる。
  * :command:`git remote update` →「ローカルにおける origin の定義をリモートで更新する」
  * ``master``
  * ``origin/master`` →追跡

* 11.3.5 :command:`git remote show origin`
* 11.3.6 :command:`git pull` == :command:`git fetch` + :command:`git (merge|rebase)`
