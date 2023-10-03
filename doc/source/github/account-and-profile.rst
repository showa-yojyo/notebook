======================================================================
Account and profile documentation ノート
======================================================================

`Account and profile documentation <https://docs.github.com/en/account-and-profile>`__
を読んで、自分のアカウントを作り込もう。

.. contents::

Setting up and managing your personal account on GitHub
======================================================================

Managing user account settings
----------------------------------------------------------------------

About your personal dashboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

個人用ダッシュボードは GitHub 全画面に共通して見える、左上の Octocat アイコン押
しでしか出ない画面だ。ログイン状態で GitHub のトップページに行くのに相当する。

画面左柱は自分と関係がある区画だ：

* :guilabel:`Top Repositories`
* :guilabel:`Recent activity`

それ以外は GitHub からの案内のような情報だ。

Managing your theme settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

昨今どこでも見かけられるテーマ機能。本来の用途は次の考え方だったのだと思う：

  If you have low vision, you may benefit from a high contrast theme, with
  greater contrast between foreground and background elements. If you have
  colorblindness, you may benefit from our light and dark colorblind themes.

アカウント :menuselection:`Settings --> Appearance --> Theme preferences` で設定す
る。素直に :guilabel:`Light default` でいいだろう。

Managing your tab size rendering preference
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

タブのスペース数をアカウント :menuselection:`Settings --> Appearance --> Tab
size preference` で指示可能。テキストエディターと同じ感覚で指定するものだ。

Changing your GitHub username
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GitHub アカウント名を変更するなら :menuselection:`Settings --> Account -->
Change user name` を操作する。これを乱用してはいけない。

アカウント名を変更すると、GitHub 内にある関連データも可能な限り自動更新されるよ
うだ。利用者が手動で変更しなければならないものもある：

  After changing your username, :file:`CODEOWNERS` files that include your old
  username will need to be manually updated.

Permission levels for a personal account repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  You can also invite users on GitHub to your repository as collaborators.

この機能があるので権限 (permission) の考えがある。

リポジトリー所有者はリポジトリーに対する操作すべてが許可されている。協力者はすべ
てではないが、それでもかなりの操作が許可されている。引用が面倒なので本文の一覧を
参照。

Permission levels for a project board owned by a personal account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  There is only one owner of a user-owned project board; this permission cannot
  be shared with another personal account. In addition to the owner, other
  people can collaborate on project boards.

権限は三種類ある。名称だけで意味は通じるだろう：

* Read
* Write
* Admin

  The project board owner and collaborators with admin access have full control
  of the project board.

所有者と管理権限付き協力者は同等ということになる。この権限は次のことを特に許可さ
れている：

* Manage, view, and add collaborators
* Configure a project board as public or private
* Delete a project board
* Close a project board
* Reopen a closed project board

Read および Write の権限で許可されている操作一覧は本文参照。

  You can change the project board's visibility from private to public and back
  again.

Managing accessibility settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Accessibility settings can be essential for people with disabilities, but can
  be useful to anyone.

この考え方を忘れてはいけない。

アカウント :menuselection:`Settings --> Accessibility --> Content --> Link
underines` でリンクの見てくれを設定する。下線を付けるかどうかを制御可能。

アカウント :menuselection:`Settings --> Accessibility --> Keyboard shortcuts` で
修飾キーの有無やコマンドパレットのキーバインドを少しは制御可能。

アニメーション GIF の描画設定もあるがノート割愛。

Managing the default branch name for your repositories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ここで言う default branch は GitHub でリポジトリーを新規に作成すると最初からあ
るブランチを意味する。

アカウント :menuselection:`Settings --> Repositories --> Repository default
branch` で名称を指定する。決めたら :guilabel:`Update` を押す。

Managing security and analysis settings for your personal account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

アカウント :menuselection:`Settings --> Code security and analysis` を開いて
:guilabel:`Enable` できるところは全部押せばよさそうだが、性能に影響するかもしれ
ない。

Managing access to your personal account's project boards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

協力者の定義は project board に関係して与えられている：

  A collaborator is a person who has permissions to a project board you own.

協力者の設定方法は割愛。

Managing your cookie preferences for GitHub's enterprise marketing pages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  You can customize how non-essential cookies behave on any GitHub enterprise
  marketing page.

必要でないなら消そう。方法は https://resources.github.com/ に移動してページの最
下部まで行く。リンク :guilabel:`Manage Cookies` を押す。Cookies を拒否して
:guilabel:`Save changes` する。

What does the 'Available for hire' checkbox do?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

この機能は廃止された。

Managing your personal account
----------------------------------------------------------------------

Managing multiple accounts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

例えば個人アカウントと勤務先から貸与されたアカウントの二つを持つ利用者がいるとす
る：

  If you want to use one workstation to contribute from both accounts, you can
  simplify contribution with Git by using a mixture of protocols to access
  repository data, or by using credentials on a per-repository basis.

認証は PC 単位でなされるらしいことを覚えておく。

  If you contribute with two accounts from one workstation, you can access
  repositories by using a different protocol and credentials for each account.

ここで HTTPS か SSH のどちらを採用するのかという問題があるかもしれない。私は
Git 操作では SSH しか使わないのでその辺のノートを割愛する。

  If you want to use the SSH protocol for both accounts, you can use different
  SSH keys for each account.

アカウントごとに SSH キーを用意することが可能だという言い回しに注意する。具体的
には環境変数 :envvar:`GIT_SSH_COMMAND` を設定して Git コマンドを実行する。例えば
``git clone`` を実行するにも次のように長いコマンドラインを書くことになる：

.. code:: bash

   bash$ GIT_SSH_COMMAND='ssh -i PATH/TO/KEY/FILE -o IdentitiesOnly=yes' git clone git@github.com:OWNER/REPOSITORY

Merging multiple personal accounts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

複数アカウント統合方法について述べられている。GitHub の複数の操作を手動で行うこ
とによる：

+ 削除したいアカウントから、残したいアカウントにリポジトリーを引き継ぐ。Issues,
  pull requests, wikis も引き継がれる。
+ 移動されたリポジトリーに対するローカルクローンのリモート URL を更新する。
+ 古い方のアカウントを削除する

仕上げとして：

  To attribute past commits to the new account, add the email address you used
  to author the commits to the account you're keeping.

Converting a user into an organization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

利用するつもりのない機能なので割愛。アカウントを引き継ぐ操作が急所。

Best practices for leaving your company
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

会社を辞める際の最善技法。勤め人ではないので必要ない。

Unlinking your email address from a locked account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Since an email address can only be associated with a single GitHub account,
  unlinking your email address from a locked account allows you to link that
  email address to a new or existing account. Additionally, linking a previously
  used commit email address to a new account will connect your commit history to
  that account.

閉め出されている状態にならないようにしたい。

Deleting your personal account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

個人アカウントの削除は :menuselection:`Settings --> Account --> Delete your
account` だ。これを実施するつもりはない。

Managing email preferences
----------------------------------------------------------------------

Adding an email address to your GitHub account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  GitHub allows you to add as many email addresses to your account as you like.
  If you set an email address in your local Git configuration, you will need to
  add it to your account settings in order to connect your commits to your
  account.

追加という言い回しに注意。アカウント :menuselection:`Settings --> Emails --> Add
email address`.

:guilabel:`Primary email address` で指定したアドレスが GitHub から操作する Git
操作に適用される。

Changing your primary email address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

上記で説明した UI を使えばいい。要らなくなった余分なアドレスならゴミ箱ボタンで消
せる。

Setting a backup email address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

アカウント :menuselection:`Settings --> Emails --> Backup email address` で
宛先を登録済みアドレスすべてか、主要アドレスのみにするかを選択。

Setting your commit email address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ここはけっこう重要なので今理解する。GitHub は利用者に特殊なメールアドレスを用意
する：

  If you'd like to keep your personal email address private, you can use a
  ``noreply`` email address from GitHub as your commit email address. To use
  your ``noreply`` email address for commits you push from the command line, use
  that email address when you set your commit email address in Git.

ローカルのコンソールで ``git config`` コマンドで設定する。次のオプションをオンに
すれば、このメールアドレス引数に提供アドレスを指定可能だと述べている。

  To use your ``noreply`` address for web-based Git operations, set your commit
  email address on GitHub and choose to :guilabel:`Keep my email address
  private`.

項目位置はアカウント :menuselection:`Settings --> Emails --> Keep my email
addresses private` だ。オンにしておきたい。提供アドレスはこのチェックボックスの
下のテキスト中にあるはずだ。

Git コマンドはリポジトリーごとでも大域的にでも設定可能：

.. code:: console

   bash$ git config user.email ADDRESS
   bash$ git config --global user.email ADDRESS

Blocking command line pushes that expose your personal email address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  If you enable this setting, each time you push to GitHub, we’ll check the most
  recent commit. If the author email on that commit is a private email on your
  GitHub account, we will block the push and warn you about exposing your
  private email.

アカウント :menuselection:`Settings --> Emails --> Block command line pushes
that expose my email` をオンにする。

Remembering your GitHub username or email
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GitHub にログインするときの名前を忘れた場合の悪あがき。この記事では利用者の PC
に GitHub とのやりとりの跡が何かしら残っているという仮定だ。

名前については自分のリポジトリーからクローンしたローカルリポジトリーの情報を確認
するのがいいと思われる：

.. code:: console

   bash$ git remote -v
   origin  git@github.com:showa-yojyo/notebook (fetch)
   origin  git@github.com:showa-yojyo/notebook (push)

Types of emails GitHub sends
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

割愛。

Managing marketing emails from GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

アカウント :menuselection:`Settings --> Emails --> Email preferences` で
:guilabel:`Only receive account related emails, and those I subscribe to.`
を選択しておく。

Managing access to your personal repositories
----------------------------------------------------------------------

Inviting collaborators to a personal repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  To collaborate with users in a repository that belongs to your personal
  account on GitHub.com, you can invite the users as collaborators.

招待というのがミソだ。

  GitHub limits the number of people who can be invited to a repository within a
  24-hour period. If you exceed this limit, either wait 24 hours or create an
  organization to collaborate with more people.

制限は気にしなくていい。

招待手順。目的リポジトリー :menuselection:`Settings --> Collaborators` を開く。
`Add people` ボタンを押して検索欄を使って招待相手を表示する。最後にボタンを押す
と招待メールが相手に送られる。

Removing a collaborator from a personal repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

目的リポジトリー :menuselection:`Settings --> Collaborators` を開く。対象の脇に
あるボタン :guilabel:`Remove` を押す。

Removing yourself from a collaborator's repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

自分が協力者を辞める場合の手順だ。

アカウント :menuselection:`Settings --> Repositories` を開く。対象の脇にあるボタ
ン :guilabel:`Leave` を押す。最後に確認ボタンを押す。

Maintaining ownership continuity of your personal account's repositories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  We recommend inviting another GitHub user to be your successor, to manage your
  user owned repositories if you cannot.

こういう事態はなるべくならないで欲しい。

  An appointed successor can manage your public repositories after presenting a
  death certificate then waiting for 7 days or presenting an obituary then
  waiting for 21 days.

相続人を指定するような重要な仕事をしているわけではないので、未対応でいいだろう。

Managing your membership in organizations
----------------------------------------------------------------------

About organization membership
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

組織所有者や管理人の能力：

  An organization owner can invite you to join their organization as a member,
  billing manager, or owner. An organization owner or member with admin
  privileges for a repository can invite you to collaborate in one or more
  repositories as an outside collaborator.

組織から招待を受けて承諾した場合、組織所有者は私の各種情報を確認可能となる。本文
参照。

  By default, your organization membership visibility is set to private.

自分から口外しなければ、ある組織の構成員だということは一般人に知られない。

  You can leave an organization at any time.

任意に離脱可能。

Accessing an organization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

自分が所属している組織を見るには、アカウント :menuselection:`Your organizations`
を押す。

Viewing people's roles in an organization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

組織画面のメニュー右端 :menuselection:`People` を押す。フィルターの
:guilabel:`Role` から何かを選ぶ。

Requesting organization approval for OAuth apps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Organization members and outside collaborators can request that an owner
  approve access to organization resources for OAuth apps.

アカウント :menuselection:`Settings --> Applications --> Authorized OAuth Apps`
へ進む。ここで目的のアプリケーションの項目を押す。そのページに
:guilabel:`Request access` ボタンがあるらしいので、それを押して
:guilabel:`Request approval from owners` を押す。

Publicizing or hiding organization membership
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  If you'd like to tell the world which organizations you belong to, you can
  display the avatars of the organizations on your profile.

名の通った組織に所属している場合には、その事実を公表することで押しが効く。

先述の :menuselection:`People` から自身が所属する組織一覧画面へ進み、対象の組織
項目を表示する。そこで枠内の :guilabel:`Private` を :guilabel:`Public` に切り替
える。

Managing your scheduled reminders
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Get reminders in Slack when you or your team have pull requests waiting for
  review.

アカウント :menuselection:`Settings --> Scheduled remainders` で組織項目枠内に何
か出るらしいが、私の画面と合致しない。

Removing yourself from an organization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

アカウント :menuselection:`Settings --> Organizations` で目的の組織を選び
:guilabel:`Leave` 押す。
