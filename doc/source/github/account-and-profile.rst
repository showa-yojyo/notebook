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

..

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

.. code:: console

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
:guilabel:`Add people` ボタンを押して検索欄を使って招待相手を表示する。最後にボ
タンを押すと招待メールが相手に送られる。

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

Setting up and managing your GitHub profile
======================================================================

Customizing your profile
----------------------------------------------------------------------

About your profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  If you add a README file to the root of a public repository with the same name
  as your username, that README will automatically appear on your profile page.

このノートを綴っている時点で、この使えそうな機能に手を出していない。大至急実施し
たい。

About your organization's profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  You can customize your organization's public profile by adding a
  :file:`README.md` file

個人アカウントにもあった機能の組織版だ。

Personalizing your profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

まずはアカウント :menuselection:`Settings --> Public profile` を操作して初期状態
を脱出しろ。

* :guilabel:`Profile pitcure` で証明写真画像などをアップロード可能。
* :guilabel:`Name` で名前を示す。
* :guilabel:`Bio` に経歴を書く。

ここまでは UI を見れば分かる。

  You can set a location and time zone on your profile to show other people your
  local time.

これもいちおう設定しておく。同じくこの画面内にある :guilabel:`Location` 区画にて、

* :guilabel:`Display current local time` をオンにする。
* :guilabel:`Time zone` で ``(GMT+09:00) Tokyo`` を選択する。

有名な SNS にアカウントを持っている場合、:guilabel:`Social accounts` 下にアドレ
スを記入しておくとプロフィール画面にそれらへのページのリンクが現れる。

  When you set your status, you can also let people know that you have limited
  availability on GitHub.

ものぐさな人は右上ドロップダウンで :guilabel:`Busy` に設定する。初回は近影を、設
定済みの場合は状態をクリック。フォーム内のチェックボックスをオンにする。

  When you participate in certain programs, GitHub automatically displays a
  badge on your profile.

バッヂは上級者向けの装飾要素だろう。この一覧を見る限り何も獲れそうにない。

  Achievements celebrate specific events and actions that happen on GitHub. They
  will appear as small badges listed in the sidebar of your profile.

これの一覧がどこかにないものか。

Managing your profile README
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  GitHub shows your profile README at the top of your profile page.

GitHub アカウント名と合致する公開リポジトリーに中身のある :file:`README.md` が
あれば、それが適用される。

GitHub 上でそのようなリポジトリーを最初に作成すると：

  The generated README file is pre-populated with a template to give you some
  inspiration for your profile README.

この README 公表を撤回したい場合は、リポジトリーを private にするなり
:file:`README.md` を空にしてコミットしたりするなどする。

Pinning items to your profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

プロフィール画面の :guilabel:`Customize your pins` の UI で実施。この小さい
フォームには自作リポジトリーと gists が人気順に並んでいる。

Setting your profile to private
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  After making your profile private, you can still view all your information
  when you visit your own profile.

:menuselection:`Settings --> Contributions & Activity` の :guilabel:`Make
profile private and hide activity` をオン。:guilabel:`Update preferences` で確定。

しかしこの機能は不要だ。

Managing contribution settings on your profile
----------------------------------------------------------------------

Viewing contributions on your profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

プロフィール画面に示される情報などを知る。

  On your profile page, certain actions count as contributions:

  * Committing to a repository's default branch or ``gh-pages`` branch
  * Creating a branch
  * Opening an issue
  * Opening a discussion
  * Answering a discussion
  * Proposing a pull request
  * Submitting a pull request review

:guilabel:`Popular repositories` 枠はピン機能を使うとなくなる。

Showing an overview of your activity on your profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  A viewer can only see information in the activity overview about repositories
  they have read access to.

プロフィール画面のカレンダー (contributions graph) 右上 :guilabel:`Contribution
settings` ドロップダウンリストから適当なものを選択する。

Showing your private contributions and achievements on your profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  If you publicize your private contributions, people without access to the
  private repositories you work in won't be able to see the details of your
  private contributions. Instead, they'll see the number of private
  contributions you made on any given day. Your public contributions will
  include detailed information.

:menuselection:`Contribution settings --> Private contributions` を見せる方向
に設定する。

アカウント :menuselection:`Settings --> Profile settings` の
:guilabel:`Show Achievements on my profile` をオンにする。

プロフィール画面の実績それぞれをクリックするとポップアップが表示される。この左上
の目ボタンを押すと表示状態を切り替える。

Sending enterprise contributions to your GitHub.com profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

これはよくわからない。割愛。

Why are my contributions not showing up on my profile?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

この記述が貢献の定義とみなせる。

Troubleshooting commits on your timeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  If the author and commit date are different, you can manually change the
  commit date in the URL to see the commit details

.. admonition:: 読者ノート

   プロフィール画面での貢献の表示に関する記述がここまで多いということは、何を意
   味するか。

Managing subscriptions and notifications on GitHub
======================================================================

Setting up notifications
----------------------------------------------------------------------

About notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

通知機能の意義は：

  You can use the notifications inbox to customize, triage, and manage your
  updates.

  Notifications are updates that you receive for specific activity that you are
  subscribed to.

自動的に購読させられる場合がある：

  By default, you also automatically watch all repositories that you create and
  are owned by your personal account.

だからリポジトリーを作成するや否や、Notification をオフにする習慣をつける。

  You can choose to view your notifications through the notifications inbox at
  https://github.com/notifications and in the GitHub Mobile app, through your
  email, or some combination of these options.

..

  You can filter your inbox by the reason you're subscribed to notifications.

..

  Notifications that are not marked as :guilabel:`Saved` are kept for 5 months.
  Notifications marked as :guilabel:`Saved` are kept indefinitely. If your saved
  notification is older than 5 months and you unsave it, the notification will
  disappear from your inbox within a day.

マークしていない通知項目はおのずと消える。しないほうがいいのか。

Configuring notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GitHub 上の活動に関する通知を受け取る場所は三つある：

* GitHub の受信箱
* GitHub Mobile の受信箱（上記のものと同期）
* 登録した主要メールアドレス（上記のものと同期）

メール以外の場所については特別な機能がある。次節で述べられる。メールについては次
の利点？がある：

  One benefit of using an email client is that all of your notifications can be
  kept indefinitely depending on your email client's storage capacity.

メールソフトの機能で GitHub の活動情報を整理することが可能だと言いたいのだ。

  You can customize notifications for a repository. For example, you can choose
  to only be notified when updates to one or more types of events (issues, pull
  requests, releases, security alerts, or discussions) happen within a
  repository, or ignore all notifications for a repository.

このカスタマイズは興味がないこともない。

  Each email notification that GitHub.com sends contains header information. The
  header information in every email is consistent, so you can use it in your
  email client to filter or forward all GitHub notifications, or certain types
  of GitHub notifications.

つまり、メールソフトでフィルターを作成しやすい。

通知設定方法：画面右上の受信箱ボタンを押す。ページ左下 :menuselection:`Manage
notifications --> Notification settings` を押す。

  If "Automatically watch repositories" is disabled, then you will not
  automatically watch your own repositories.

これは無効にしておきたい。

リポジトリーの :guilabel:`Watch` ボタンで欲しい通知をカスタマイズ指定することが
可能。

  When a new secret is detected, GitHub notifies all users with access to
  security alerts for the repository according to their notification
  preferences.

ユーザー全てに通知してもかまわないような事態だろうか。

  For repositories that are set up with GitHub Actions and that you are
  watching, you can choose how you want to receive workflow run updates.

これはかなり後で詳しく習いたい。

  When you install GitHub Mobile, you will automatically be opted into web
  notifications.

これもインストールしたい。どこにあるのか。Android で検索すればいいと思うが。

Viewing and triaging notifications
----------------------------------------------------------------------

Managing notifications from your inbox
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Your inbox shows all of the notifications that you haven't unsubscribed to or
  marked as Done. You can customize your inbox to best suit your workflow using
  filters, viewing all or just unread notifications, and grouping your
  notifications to get a quick overview.

未読の通知を一覧には :guilabel:`Unread` ボタンを押すのがいい。

複数の通知項目に対して同一の操作をするにはチェックを入れて :menuselection:`...`
メニューを選ぶか、ヘッダーにある :guilabel:`Done` ボタンなどを押す。

フィルターを自作することが可能。画面左柱 :guilabel:`Filters` の歯車を押す。ボタ
ン :guilabel:`Create new filter` を押してフィルター名と問い合わせコマンドを入
力。:guilabel:`Create` で確定。

問い合わせコマンドのノートについては検索の章に回す。``is:`` は見慣れぬキーワード
を伴うものもある。

Triaging a single notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  You can choose how you want to receive future notifications for a specific
  issue or pull request.

画面右柱の :guilabel:`Notifications` 右にある :menuselection:`Customize -->
Custom` を押す。通知されたいタイミングを指定して :guilabel:`Create` を押す。

Customizing a workflow for triaging your notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Before you start triaging your inbox, consider whether you prefer to first
  find and respond to the most important updates or to clear your inbox of
  distracting updates that are easy to remove or triage.

言葉を選ばすに言い換えれば気ままに選ぶということだ。

  Choose which type of notifications are most urgent to review and pick a time
  to review them that's best for you. You might consider the question "Who am I
  blocking?"

この視点は面白い。協力者の妨げになっている事項を優先する。

  Choose which type of notifications are quickest and easiest for you to triage
  and remove from your inbox, ideally triaging multiple notifications at once.

捨てやすいものは捨てるのが正しい。

Managing subscriptions for activity on GitHub
----------------------------------------------------------------------

Viewing your subscriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  We recommend auditing and unsubscribing from your subscriptions as a part of a
  healthy notifications workflow.

購読や監視をしたまま忘れてしまうと受信箱がパンパンになる。

受信箱トップページ左柱 :menuselection:`Notifications --> Subscriptions` を押す。
この一覧のヘッダーから項目を絞り込んで issue や pull request の購読をやめる。

.. admonition:: 読者ノート

   自分の状況を確認したら 300 以上の項目があったので、古いものから unsubscribe
   した。

受信箱トップページ左柱 :menuselection:`Notifications --> Watched repositories`
を押す。購読をやめるリポジトリーの右のドロップダウンリストから
:guilabel:`Ignore` を押す。

Managing your subscriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Note: Instead of unsubscribing, you have the option to ignore a repository. If
  you ignore a repository, you won't receive any notifications. We don't
  recommend ignoring repositories as you won't be notified if you're @mentioned.

無視するときは上記を注意したい。

  You can only filter your subscriptions by repository and the reason you're
  receiving the notification.

このフィルターだけで十分なのか。

残りは :guilabel:`Unsubscribe` と :guilabel:`Unwatch` の説明。
