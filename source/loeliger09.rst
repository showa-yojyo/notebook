======================================================================
実用 Git
======================================================================

:著者: Jon Loeliger
:訳者: 吉藤 英明（監訳）、本間 雅洋、渡邉 健太郎、浜本 階生
:出版社: オライリー・ジャパン
:発行年: 2010 年
:ISBN: 978-4-87311-440-8

書名には「実用」とあるが、個人的には Git の理論解説書として読んだ。
Git はその基礎概念をしっかり理解することが、要領良く習得することに直結する。
例えばインデックス、ツリー、ブロブ等の重要概念を押さえていないとダメであることが本書を読んでわかった。
私の場合では、なかなか覚えられない Git のコマンドがいくつかあったのだが、
それがどの構成要素に作用するのかを理解していないから覚えられないということがようやくわかった。

特に 9, 10, 11 章のマージ、コミット、リモートリポジトリの各内容を着実に理解できれば OK だろう。

.. todo::

   以下、書き殴りメモ。いつか整理するはず。

* 4.1.2 blob tree commit tag
* 4.1.3 index ←→ merge object ←→ SHA1
* 4.3 

  * ``git cat-file -p 3b18e51...``
  * ``git rev-parse 3b18e51...``
  * ``git ls-files -s``

* 4.3.6 ``git show --pretty=fuller``
* 4.3.7 ``git tag -m "～" V1.0 3ede452``
* あとで p. 38 fig 4.1 を確認。
* 5 index commit stage

  * ``git status`` は index の status
  * status ::= (tracked|ignored|untracked)

* 5.3 ``git ls-files --stage``
* ``git rm --cached XXX`` →アンステージ
* 5.4.1 ``git commit -a``
* 5.6 ``git log --follow XXX``
* 5.7 ``mv`` 系はツリーだけに影響する。
* 5.8 gitignore は下位フォルダーの方が強い。
* 5.9 index を tree と同じシンボルで図示している。

  * master とか HEAD とかいきなり出てくる？
  * ※index を「仮想的な tree」とみなす。

* 直接的な参照 SHA1 c.f. 間接的な参照 e.g. "HEAD"
* 6.2.1 ``git log -1 --pretty=oneline XXX``
* 6.2.2 symref

  .. code-block:: text

     refs/
       heads/～
       remotes/～  origin/master は本当は refs/remotes/origin/master
       tags/～

* HEAD ::= current branch の最新のコミット
* XXX_HEAD というような名前のシンボルが他に 3 つある。
* 6.2.3 ``C^`` とか ``C~`` とか。``^`` は複数で ``~`` は世代か？

  * ``git show-branch --more=35 | tail -10``

* 6.3.1 ``git log`` は ``git log HEAD`` （到達可能）
* 6.3.3 ``M~12..M~10`` では 12 のは含まない。

  * ``A...B`` で symmetric difference を意味する。

* 6.4.1 ``git bisect``
* 6.4.2 ``git blame``
* ``git merge-base オリジナル 新``
* ``git branch ブランチ [コミット]``
* ``git branch``, ``git show-branch``, ``[-r -a]``, ``*`` 印がカレント。
* ``git checkout ブランチ`` でスイッチする。
* 7.7.3 ``git checkout -m`` でローカルの変更を新しい working directory に持ち込む（マージ）。
* 7.7.4 ``git checkout -b 新ブランチ``
* 7.7.5 detached HEAD
* 7.7.8 ``git branch -d XXX``

  * ``git merge bug/pr-3`` して ``git branch -d bug/pr-3`` する。

* 8.1

  .. code-block:: text

     git diff                           ←作業コピーと index との比較
     git diff コミット                  ←p. 114 fig. 8-1
     git diff --cached コミット
     git diff コミット1 コミット2

* 8.2 「インデックスと HEAD との比較」←→ステージ

  .. code-block:: text

     git diff           ←作業コピーと index との比較
     git diff HEAD      ←作業コピーと HEAD との比較
     git diff --cached  ←index と HEAD との比較

     git diff HEAD^ HEAD

* 8.4

  .. code-block:: text

     git diff --stat master~5 master Documentation
     git diff -S "octopus" master~50

* 9.1

  .. code-block:: text

     git checkout ブランチ
     git merge 別ブランチ

* 9.1.2

  .. code-block:: text

     git checkout -b alternate master~
     git log --graph --pretty=oneline --abbrev-commit

* 9.1.3 ``git merge なんとか`` の直後に commit する→
  ``git diff`` で見る→テキスト編集→
  ``git add ファイル`` →
  ``git commit``

* 9.2.1 ``git status`` ``git ls-files -u``
* 9.2.2.1 ``git diff MERGE_HEAD``

  * ``git log --merge --left-right -p``
  * ``git diff :1:hello :3:hello``

* 9.2.5

  .. code-block:: text

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

  ``git merge -s resolve Bob``

* 9.4.2 squash commit
* 10.2 ``git reset`` は作業コピーをいじるコマンド。soft, mixed, hard
* 10.3 ``git cherry-pick dev~2``
* 10.6 ``git commit --amend``
* 10.7 ``git rebase``: 基点の変更
* 11.1.1 base
* 11.1.2

  * ``git clone 元リポジトリー 新クローン``
  * ``git clone git://～/～.git``
  * origin と呼ばれるリモート

* 11.1.3

  * ``git fetch``
  * ``git pull`` →変更マージあり
  * ``git push``
  * ``git ls-remote``

* 11.3.1 ``git clone --bare すでにリポジトリー 新.git``
* 11.3.2

  * ``git remote add origin /tmp/Depot/public_html`` → ``.git/config`` が書き換わる。
  * ``git remote update`` →「ローカルにおける origin の定義をリモートで更新する」
  * ``master``
  * ``origin/master`` →追跡

* 11.3.5 ``git remote show origin``
* 11.3.6 ``git pull`` == ``git fetch`` + ``git (merge|rebase)``
