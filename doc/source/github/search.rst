======================================================================
Search on GitHub documentation ノート
======================================================================

`Search on GitHub documentation <https://docs.github.com/en/search-github>`__

.. contents::
   :depth: 3

* :guilabel:`Overview` → :ref:`About searching on GitHub <search-overview>`

Getting started with searching on GitHub
======================================================================

.. _search-overview:

About searching on GitHub
----------------------------------------------------------------------

GitHub にログインしている状態であるのが検索機能を利用可能である条件だ。

   You can search globally across all of GitHub, or scope your search to a
   particular repository or organization.

どちらも検索したい場合がある。

* GitHub 全体から検索する場合、画面上部の検索欄を用いて :guilabel:`Search all
  of GitHub` の付いているものを選択する。
* 特定のリポジトリーや組織を検索する場合、そのページにまず移動してから検索欄を使
  う。
* 候補一覧クリックや自動補完を上手く使うといい。

検索結果画面では、それらしき項目の一覧が続く。

   After running a search on GitHub, you can sort the results, or further refine
   them by clicking one of the languages in the sidebar.

これを上手く使いこなしたい。

   Alternatively, you can use the interactive search in the GitHub Command
   Palette to search your current location in the UI, a specific user,
   repository or organization, and globally across all of GitHub, without
   leaving the keyboard.

これは？

   The advanced search page provides a visual interface for constructing search
   queries.

検索コマンドを UI 操作で組み立てる。

Understanding the search syntax
----------------------------------------------------------------------

   Note: The syntax below applies to non-code search.

不等号が使える場合がある：

   ``cats stars:>1000`` matches repositories with the word "cats" that have more
   than 1000 stars.

UML のような範囲指定が使える場合がある。

   ``cats stars:10..*`` is equivalent to ``stars:>=10`` and matches repositories
   with the word "cats" that have 10 or more stars.

..

   ``cats stars:10..50`` matches repositories with the word "cats" that have
   between 10 and 50 stars.

日付は特別扱い。不等号が使える：

   Date formatting must follow the ISO8601 standard, which is ``YYYY-MM-DD``
   (year-month-day).

あとは ``-`` や ``NOT`` で除外指定が可能：

   ``cats stars:>10 -language:javascript`` matches repositories with the word
   "cats" that have more than 10 stars but are not written in JavaScript.

..

   The ``NOT`` operator can only be used for string keywords. It does not work
   for numerals or dates.

よその検索システムと同様：

   If your search query contains whitespace, you will need to surround it with
   quotation marks.

GitHub にしかない指定方法：

   If your search query contains a qualifier that requires a username, such as
   ``user``, ``actor``, or ``assignee``, you can use any GitHub username, to
   specify a specific person, or ``@me``, to specify the current user.

例を見ないとわからない：

   ``author:nat`` matches commits authored by @nat

..

   ``is:issue assignee:@me matches issues assigned to the person viewing the
   results``

Troubleshooting search queries
----------------------------------------------------------------------

よそではあまり聞いたことがないが、処理時間上限を過ぎると検索が打ち切られる：

   To keep search fast for everyone, we limit how long any individual query can
   run.

検索自体に関わる制限：

   You can't construct a query using more than five ``AND``, ``OR``, or ``NOT``
   operators

..

   Specific search types, such as code search, might have additional
   limitations.

Sorting search results
----------------------------------------------------------------------

検索結果画面を見てすぐにわかることだが：

   Use the :guilabel:`Sort` dropdown menu to sort results by relevance, number
   of stars, number of forks, and how recently the items were updated.

検索コマンドに ``sort`` 修飾子を付ける方法もある：

   ``org:github sort:interactions`` matches issues in repositories owned by
   GitHub, sorted by the highest combined number of reactions and comments.

..

   ``feature org:github sort:author-date`` matches commits containing the word
   "feature" in repositories owned by GitHub, sorted by descending author date.

   ``feature org:github sort:committer-date`` matches commits containing the
   word "feature" in repositories owned by GitHub, sorted by descending
   committer date.

..

   ``feature sort:updated`` matches repositories containing the word "feature,"
   sorted by most recently updated date.

Searching on GitHub
======================================================================

修飾子メイン？

Finding files on GitHub
----------------------------------------------------------------------

   To search for a file in multiple repositories on GitHub, use the ``path``
   code search qualifier.

さっそく Tips に興味深い記述がある：

   By default, file finder results exclude some directories like ``build``,
   ``log``, ``tmp``, and ``vendor``. To search for files in these directories,
   use the ``path`` code search qualifier.

中間生成物を示唆するパスは最初から検索対象外。リポジトリーにあるのがそもそもおか
しいということだ。

   Alternatively, you can customize which directories are excluded by default
   using a :file:`.gitattributes` file.

Git 設定によっても不要ファイルは除ける。

File finder というのはリポジトリー :guilabel:`Go to File` を押すと出る画面の左列
にある検索欄のことらしい。ここでパス入力で合致する項目が一覧に出る。

:file:`.gitattributes` を使う方法は：

   For example, the following :file:`.gitattributes` file would cause files in
   the ``build/`` directory to be available to the file finder:

   .. code:: text

      build/** linguist-generated=false

Searching for repositories
----------------------------------------------------------------------

   With the ``in`` qualifier you can restrict your search to the repository
   name, repository description, repository topics, contents of the README file,
   or any combination of these.

例えば ``jquery in:readme`` は README ファイルに検索対象を限定する。

   Besides using ``in:readme``, it's not possible to find repositories by
   searching for specific content within the repository.

思っている以上に README の記述は重要であることがわかった。

   To search in all repositories owned by a certain user or organization, you
   can use the ``user`` or ``org`` qualifier.

例えば ``user:defunkt forks:>100`` など。

   The ``size`` qualifier finds repositories that match a certain size (in
   kilobytes)

これは有用かもしれない。次のようにして枠を超えそうな危ないリポジトリーを発見した
い：

   ``size:>=30000`` matches repositories that are at least 30 MB.

きりがないのでこの辺でノートを切り上げる。見出しだけ写しておこう：

* Search by repository name, description, or contents of the README file
* Search based on the contents of a repository
* Search within a user's or organization's repositories
* Search by repository size
* Search by number of followers
* Search by number of forks
* Search by number of stars
* Search by when a repository was created or last updated
* Search by language
* Search by topic
* Search by number of topics
* Search by license
* Search by repository visibility
* Search based on whether a repository is a mirror
* Search based on whether a repository is a template
* Search based on whether a repository is archived
* Search based on number of issues with good first issue or help wanted labels
* Search based on ability to sponsor

Searching topics
----------------------------------------------------------------------

メイン検索欄でキーワード検索してから左列で ``Topics`` を押す。

GitHub 推奨の検索修飾子がある：

   The ``is:featured`` search qualifier will narrow search results to the topics
   with the most repositories on GitHub.

よくわからない。

   The ``is:curated`` search qualifier will narrow search results to topics that
   community members have added extra information to.

これもよくわからない。

   You can filter topics based when they were created using the date parameter
   and ``created:`` or based on how many repositories are associated with this
   topic using ``repositories:n``.

日付検索は不等号でさらに絞り込みが可能。

Topics を手動で検索するには：

   You can use the ``topic:`` qualifier to find every repository connected to a
   particular topic.

Searching code (legacy)
----------------------------------------------------------------------

割愛。

Searching commits
----------------------------------------------------------------------

個人的にはコミットログの書き方を参考にするのにこの検索が使える。

   When you search for commits, only the default branch of a repository is
   searched.

これが基本と信じたいが、Web 検索と同様に：

   You can find commits that contain particular words in the message.

コミット特有の検索修飾子を使って、次のような検索が可能：

* Search by author or committer
* Search by authored or committed date
* Filter merge commits
* Search by hash
* Search by parent
* Search by tree
* Search within a user's or organization's repositories
* Filter by repository visibility

例えば、

   ``author:defunkt`` matches commits authored by @defunkt.

Git 周りの検索オプションが面白い。例えば、

   The ``parent`` qualifier matches commits whose parent has the specified SHA-1
   hash.

Searching issues and pull requests
----------------------------------------------------------------------

   You can search for issues and pull requests globally across all of GitHub, or
   search for issues and pull requests within a particular organization.

..

   By default, GitHub search will return both issues and pull requests. However,
   you can restrict search results to just issues or pull requests using the
   ``type`` or ``is`` qualifier.

* ``type:pr``, ``is:pr``
* ``type:issue``, ``type:pr``

他の検索オプションは次のとおり：

* Search by the title, body, or comments
* Search within a user's or organization's repositories
* Search by open or closed state
* Search for pull requests in the merge queue
* Search by the reason an issue was closed
* Filter by repository visibility
* Search by author
* Search by assignee
* Search by mention
* Search by team mention
* Search by commenter
* Search by a user that's involved in an issue or pull request
* Search for linked issues and pull requests
* Search by label
* Search by milestone
* Search by project board
* Search by commit status
* Search by commit SHA
* Search by branch name
* Search by language
* Search by number of comments
* Search by number of interactions
* Search by number of reactions
* Search for draft pull requests
* Search by pull request review status and reviewer
* Search by when an issue or pull request was created or last updated
* Search by when an issue or pull request was closed
* Search by when a pull request was merged
* Search based on whether a pull request is merged or unmerged
* Search based on whether a repository is archived
* Search based on whether a conversation is locked
* Search by missing metadata

Searching discussions
----------------------------------------------------------------------

Discussions を対象にする検索では次のような絞り込みが可能：

* Search by the title, body, or comments
* Search within a user's or organization's repositories
* Search by open or closed state
* Search based on whether a discussion was answered
* Search based on whether a discussion is locked
* Filter by repository visibility
* Search by author
* Search by commenter
* Search by user who has answered a discussion
* Search by a user that's involved in a discussion
* Search by number of comments
* Search by when a discussion was created or last updated
* Search by category
* Search by label

Searching GitHub Marketplace
----------------------------------------------------------------------

   You can search for apps and actions that are available on GitHub Marketplace.

この機能はまだ全然文書に現れていない。

画面左上の Octocat 左のハンバーガーリストから Marketplace のサイトに移動可能。そ
この専用検索欄を利用する方法もある。

Searching users
----------------------------------------------------------------------

* Search only users or organizations
* Search by account name, full name, or public email
* Search by number of repositories a user owns
* Search by location
* Search by repository language
* Search by when a personal account was created
* Search by number of followers
* Search based on ability to sponsor

例えば、

* ``in:name 猫`` でアカウント名に猫を含むものを検索。``user:猫`` より広い。
* ``location:arctic`` で（自称）在北極アカウントを検索。

Searching for packages
----------------------------------------------------------------------

これは検索オプションが ``user:``, ``org:``, ``is:`` しかない。

Searching wikis
----------------------------------------------------------------------

* Search within a user's or organization's repositories
* Search within a wiki page title or body text
* Search by last updated date

Searching in forks
----------------------------------------------------------------------

   To show forks in repository search results, add ``fork:true`` or
   ``fork:only`` to your query.

通常、フォークは検索結果としては現れないので専用の検索修飾子を要する。

   The ``fork:true`` qualifier finds all results that match your search query,
   including forks. The ``fork:only`` qualifier finds only forks that match your
   search query.

..

   ``github fork:true`` matches all repositories containing the word "github,"
   including forks.

一方、

   ``github fork:only`` matches all fork repositories containing the word
   "github."

Searching gists
----------------------------------------------------------------------

Gists 特有の修飾子だと思う ``anon:`` というフラグがある。

   ``cat anon:true`` includes anonymous gists in your search for cat-related
   gists.

..

   ``join extension:coffee`` finds all instances of "join" in gists with a
   coffee extension.

内容に ``join`` を含む拡張子 ``coffee`` のファイルを検索するということか。

GitHub Code Search
======================================================================

About GitHub Code Search
----------------------------------------------------------------------

   This search engine is designed to be scalable, code-aware, and support
   searching code across GitHub using regular expressions, boolean operations,
   specialized qualifiers, and symbol search.

やっとらしくなってきた。

   You must be logged in to a GitHub account to use code search, including for
   searching code in public repositories.

他の検索ではログインが不要だったか？

   Note that the syntax and qualifiers for searching for non-code content, such
   as issues, users, and discussions, is not the same as the syntax for code
   search.

それゆえコード検索のみ節が他の検索と独立している。

   The query length is limited to 1000 characters.

コード検索でこの制限は強い？

   Code search supports searching for symbol definitions in code, such as
   function or class definitions, using the ``symbol:`` qualifier.

これもらしいオプションだ。

Using GitHub Code Search
----------------------------------------------------------------------

GitHub 画面上部の検索欄を活動させると：

   Under the search bar, you will see a list of suggestions organized by
   category, including recent searches and suggested repositories, teams, and
   projects that you have access to. You can also see a list of saved searches
   that you have created.

そのどれかの項目を押すと、検索結果に移動したりする。

検索欄でタイプし始めると、補完機能が勝手に動作する。

検索欄に ``saved:`` とタイプすると、下に :guilabel:`Saved queries` という枠が出
る。:guilabel:`Manage saved searches` を押すと検索パターンを保存するためのフォー
ムが現れる。

Understanding GitHub Code Search syntax
----------------------------------------------------------------------

   A bare term with no qualifiers will match either the content of a file or the
   file's path.

内容のみならず、ファイル名にもマッチすることに注意。

空白文字は ``AND`` と等価だ。

   You can also use regular expressions in your searches by surrounding the
   expression in slashes.

私が知る限り正規表現を対応している唯一の検索エンジン。

   You can use specialized keywords to qualify your search.

   * Repository qualifier
   * Organization and user qualifiers
   * Language qualifier
   * Path qualifier
   * Symbol qualifier
   * Content qualifier
   * Is qualifier

修飾子 ``language:`` には非コード検索とは異なり、プログラミング言語を与える。

.. code:: text

   language:ruby OR language:cpp OR language:csharp

`対応している言語名 <https://github.com/github-linguist/linguist>`__

修飾子 ``path:``
はワイルドカードも正規表現も使えるらしい。正規表現はスラッシュで囲んで認識させる：

.. code:: text

   path:/(^|\/)README\.md$/
   path:*.txt
   path:src/*.js
   path:/src/*.js
   path:/src/**/*.js
   path:*.a?c

スラッシュで囲むということは、スラッシュを含む正規表現で注意することがあるという
ことだ：

   Note that you'll have to escape any forward slashes within the regular
   expression.

コード検索では単なる文字列ではなく、識別子として検索可能：

   You can search for symbol definitions in code, such as function or class
   definitions, using the ``symbol:`` qualifier.

ただし：

   Symbol extraction is supported for the following languages.

   * C#
   * Python
   * Go
   * Java
   * JavaScript
   * TypeScript
   * PHP
   * Protocol Buffers
   * Ruby
   * Rust

ファイル名を検索から外したいとき：

   To restrict a search to strictly match the content of a file and not file
   paths, use the ``content:`` qualifier.

Twitter でユーザー名を検索から外したい状況と似ている。
