======================================================================
GitHub Discussions documentation ノート
======================================================================

`GitHub Discussions <https://docs.github.com/en/discussions>`__ は全然知らなかっ
た機能なので全部読む。

.. contents::
   :depth: 3

* :guilabel:`Quickstart` は Quickstart for GitHub Discussions へ
* 組織絡みは割愛

Quickstart for GitHub Discussions
======================================================================

   Discussions are for conversations that need to be transparent and accessible
   but do not need to be tracked on a project board and are not related to code,
   unlike GitHub Issues. Discussions enable fluid, open conversation in a public
   forum.

古の掲示板のような感じだろうか。

リポジトリーに対する Discussions を利用可能にする手順は、リポジトリー
:menuselection:`Settings --> General` ページの :guilabel:`Features` 枠の
:guilabel:`Discussion` をオンにする。その右下の :guilabel:`Set up discussions`
ボタンを押して、テンプレートを編集する。最後に :guilabel:`Start discussions` を
押す。

   You can welcome your community and introduce a new way to communicate in a
   repository or organization by creating a welcome post and pinning the post to
   your GitHub Discussions page.

ピン留めしてページ上の貴重な空間が一つ埋まってしまってでも「歓迎枠」を設けるのが
有益だということか。

   For repository discussions, you can set contributing guidelines to encourage
   collaborators to have meaningful, useful conversations that are relevant to
   the repository.

まるで掲示板の管理人の心得だ。:file:`README` でも Disucussions の利用について述
べておく。

掲示板で言うスレッドの作成は当該リポジトリーの利用者なら可能だ。手順は次のとお
り：リポジトリー :menuselection:`Discussions --> New discussion` を押す。スレッ
ド区分を決めて :guilabel:`Get started` を押す。フォームが現れるので埋める。最後
に :guilabel:`Start discussion` を押す。

投票ページも作成可能だ。手順はスレッドと同様だが、区分を :guilabel:`Polls` とす
る。フォームで選択肢を構成するところが特徴だ。

   Repository owners and people with write access to the repository can create
   new categories to keep discussions organized.

..

   Discussions can also be recategorized after they are created.

さらに、Issues のようにラベル機能もある。

一般的な掲示板のように、調停役を設けろ。

Discussions guides
======================================================================

   GitHub Discussions is a collaborative communication forum for the community
   around an open source or internal project.

Forum というのは特定の話題に関して情報交換をする場を意味する。要するに打ち合わせ
だ。

Best practices for community conversations on GitHub
----------------------------------------------------------------------

   Discover pathways to get started or learn best practices for participating or
   monitoring your community's discussions.

参加したり注視したり？

   You might use repository discussions to discuss topics that are specific to
   the repository. If your project spans multiple repositories, you might use
   organization discussions to discuss topics that aren't specific to a single
   repository in your organization.

Discussion にはリポジトリーと組織の二種類はある。

   Before you open a discussion in a repository, check to see if the repository
   has contributing guidelines. The :file:`CONTRIBUTING` file includes
   information about how the repository maintainer would like you to contribute
   ideas to the project.

よそのリポジトリーを検索して当該ファイルを当たるとする。

Finding your discussions
----------------------------------------------------------------------

画面左上のハンバーガーメニューから :menuselection:`Disucussions` を押す。
:guilabel:`Created`` か :guilabel:`Commented` を押すと、自分の作成したものや会話
したものがフィルターされて現れる。

Granting higher permissions to top contributors
----------------------------------------------------------------------

   Repository administrators can promote any community member to a moderator and
   maintainer.

YouTube のチャット欄のようなものを想像する。

* Step 1: Audit your GitHub Discussions top contributors
* Step 2: Review permission levels for GitHub Discussions
* Step 3: Change permissions levels for top contributors
* Step 4: Notify community members of elevated access

リポジトリーまたは組織の :guilabel:`Discussions` を押す。その画面でどの協力者が
議長に適しているかを確認できるらしい。それから協力者の権限を昇格させる。

Collaborating with your community using discussions
======================================================================

   Gather and discuss your project with community members and other maintainers.

話し合おう。

About discussions
----------------------------------------------------------------------

   Use discussions to ask and answer questions, share information, make
   announcements, and conduct or participate in a conversation about a project
   on GitHub.

そういう用途なら全公開リポジトリーで Discussions を有効にしてもいいか。

   You might use repository discussions to discuss topics that are specific to
   the repository. If your project spans multiple repositories, you might use
   organization discussions to discuss topics that aren't specific to a single
   repository in your organization.

リポジトリー Discussions と組織 Discussions の使い分け。

   If a repository administrator or project maintainer enables GitHub
   Discussions for a repository, anyone who has access to the repository can
   create and participate in discussions for the repository.

明示的に有効にしないと使えない。組織版も同様。

   You can create polls in the polls category to gauge interest in new ideas and
   project direction.

よその SNS でも見受けられる投票機能か。選択肢は 8 までとか。

   You can organize discussions with categories, sections, and labels.

分類機能。分類しないと人に見つけてもらえない。

   Each category has a format: open-ended discussion, question and answer, or
   announcement.

..

   GitHub will automatically recognize community members who contribute the most
   comments marked as answers to discussions with a question/answer format.

   To organize discussions more granularly, you can apply labels.

..

   If an issue turns out to be a question or open-ended conversation instead of
   a work item to track and prioritize, you can convert the issue to a
   discussion.

これがあるなら Discussions を有効にしてもよい。

Participating in a discussion
----------------------------------------------------------------------

会話することが可能。Discussions はオープンだ。

   You can block users and report disruptive content to maintain a safe and
   pleasant environment for yourself on GitHub.

共同体の活動を邪魔する不逞の輩を GitHub は許さない。

Discussion 作成方法：リポジトリーの場合、:guilabel:`Discussions` 画面を開く。右
側に :guilabel:`New discussion` ボタンがあるので押す。所望の区分の
:guilabel:`Get started` ボタンを押す。フォームを埋めて :guilabel:`Start
discussion` を押す。

投票を作成する方法もある。

   Discussion authors and users with the triage role or greater for a repository
   can mark a comment as the answer to a discussion in the repository.

Stack Overflow とかで見るあれか。決定的なコメントを :guilabel:`Mark as answer`
する。

   You can upvote discussions to give more visibility to the topics that matter
   to you, and sort discussions to see which have been upvoted the most.

これも SNS でよく見かける様式だ。上矢印ボタンを押すとよい。

Collaborating with maintainers using discussions
----------------------------------------------------------------------

   For repository discussions, people with maintain or admin permissions to the
   repository define the categories for discussions in that repository.

カテゴリーはリポジトリーや組織によって異なることになる。

   As your project grows, you can grant higher access permissions to active
   members of your community.

プロジェクトが大きくなるにつれて？

   You can search for discussions and filter the list of discussions in a
   repository or organization.

:guilabel:`Discussions` 画面の :guilabel:`Search all discussions` 欄で検索する。

ソートも可能。

Managing discussions for your community
======================================================================

   You can enable and configure GitHub Discussions for your repository, and you
   can use tools on GitHub to moderate conversations among community members.

Managing discussions
----------------------------------------------------------------------

* Changing the category for a discussion
* Pinning a discussion
* Editing a pinned discussion
* Unpinning a discussion
* Transferring a discussion
* Deleting a discussion
* Closing a discussion
* Converting issues based on labels

..

   You can also move a discussion to a different category. It's not possible to
   move a discussion to or from the polls category.

対象 discussion 右側の :guilabel:`Catagory` 右の歯車ボタンを押す。

   You can pin a discussion above the list of discussions for the repository or
   organization. You can also pin a discussion to a specific category. The
   globally pinned discussions will be shown in addition to the discussions
   pinned to a specific category.

Discussion の右にある :guilabel:`Pin discussion` を押す。区分版として
:guilabel:`Pin to XXXXXX` を押す。:guilabel:`Edit pinned discussion` を押すと見
てくれをいじれる。

   You can unpin a discussion from the list of discussions for the repository or
   organization, or from the list of discussions in a specific category.

やめる場合は :guilabel:`Unpin discussion` や :guilabel:`Unpin discussion from
this category` を押す。

:guilabel:`Transfer this discussion` で所属する Discussions を移籍可能。

Discussion を削除するには :menuselection:`Delete discussion --> Delete this
discussion`.

   You can close a discussion when the discussion has been resolved, is no
   longer relevant, or is a duplicate.

コメント欄下の :guilabel:`Close discussion` を押す。

   You can convert all issues with the same label to discussions in bulk. Future
   issues with this label will also automatically convert to the discussion and
   category you configure.

この仕様はやや癖がある。

Managing categories for discussions
----------------------------------------------------------------------

   Each category must have a unique name and emoji pairing, and can be
   accompanied by a detailed description stating its purpose.

..

   Each repository or organization can have up to 25 categories.

   To further organize your discussions, you can create sections and then nest
   your categories within a section.

* Default categories
* Creating a category
* Creating a section
* Editing a category
* Editing a section
* Deleting a category
* Deleting a section

Default categories は六個ある。

Category を作成するには :guilabel:`Discussions` 画面の左 :guilabel:`Categories`
右の鉛筆を押す。新しい画面で :guilabel:`New category` を押す。フォームを埋めて
:guilabel:`Create` を押す。この過程で Section を作成してもよい。:guilabel:`New
section` を押す。

Category や section を編集するのも鉛筆を押し、フォームを書き換えて
:guilabel:`Save changes` を押す。

   When you delete a category, GitHub will move all discussions in the deleted
   category to an existing category that you choose.

Category 右のゴミバケツを押す。移転先を決めたら :guilabel:`Delete & Move` を押
す。

   When you delete a section, all categories within the section will no longer
   belong to a section.

ゴミバケツから :guilabel:`Delete` ボタンへ。

Moderating discussions
----------------------------------------------------------------------

   When you mark a question as an answer, GitHub will highlight the comment and
   replies to the comment to help visitors quickly find the answer.

コメント下の :guilabel:`Mark as answer` を押す。

右側 :guilabel:`Lock conversation` で discussion へのコメントを追加不能にする。

   When you convert an issue to a discussion, the discussion is automatically
   created using the content from the issue.

これは Issue 画面から操作する。:guilabel:`Convert to discussion` を押して区分を
選択して :guilabel:`I understand, convert this issue to a discussion` を押す。

   Organization owners and moderators can block a user from the organization if
   their comments don't align with the community's code of conduct.

組織専用機能か。

Viewing insights for your discussions
----------------------------------------------------------------------

   You can use discussions insights to help understand the contribution
   activity, page views, and growth of your discussions community.

リポジトリー :menuselection:`Insights --> Community` で各種統計をチェック。

Creating discussion category forms
----------------------------------------------------------------------

   You can customize the templates that are available for community members to
   use when they open new discussions in your repository.

次節で述べられる YAML 形式で定義する。

   To use a discussion category form in your repository, you must create a new
   file and add it to the :file:`/.github/DISCUSSION_TEMPLATE/` folder in your
   repository.

出来合いのテンプレートを盗み見したほうが話が早そうだ。

Syntax for discussion category forms
----------------------------------------------------------------------

   The name must correspond with the slug for one of your discussion categories.

YAML コードの例があるのでチェックしておく。
