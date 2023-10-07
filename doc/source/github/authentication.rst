======================================================================
Authentication documentation ノート
======================================================================

`Authentication documentation <https://docs.github.com/en/authentication>`__ を
読んでおく。:guilabel:`Overview` は About authentication to GitHub に移動する。

.. contents::

Account security
======================================================================

About authentication to GitHub
----------------------------------------------------------------------

認証する場所によって異なる認証情報を使って GitHub に認証することで、アカウントの
資源に安全にアクセスする。

認証方法は次のものがある：

  * Username and password with two-factor authentication, or a passkey
  * Personal access token
  * SSH key

ブラウザーの場合：

  If you're not a member of an enterprise with managed users, you will
  authenticate using your GitHub.com username and password, or a passkey. You
  may also use two-factor authentication and SAML single sign-on, which can be
  required by organization and enterprise owners.

知らない言葉がたくさん出てきて往生するが進む。

GitHub は two-factor authentication を推奨している。それ以外の方法は割愛。

コマンドラインから Git や GitHub CLI などで GitHub にアクセスする場合：

  The method of authenticating is determined based on whether you choose an
  HTTPS or SSH remote URL when you clone the repository.

どちらのプロトコルを用いるにせよ、コマンド ``gh auth login`` を一度実行する。

Creating a strong password
----------------------------------------------------------------------

GitHub の言う強いパスワードとは何か。とにかく推奨されている技法を一読する。

  When you type a password to sign in, create an account, or change your
  password, GitHub will check if the password you entered is considered weak
  according to datasets like HaveIBeenPwned.

このチェッカーを合格すればそれは強いパスワードだ。

そもそもパスワードはどこで入力を求められるかというと、実はログイン時しかない。

Updating your GitHub access credentials
----------------------------------------------------------------------

英語の credentials の概念を次の記述から体で理解しよう：

  GitHub credentials include not only your password, but also the access tokens,
  SSH keys, and application API tokens you use to communicate with GitHub.

これらをリセットすることも可能だ。

パスワードの更新手順は <https://github.com/password_reset> から始める？

パスワードの更新手順はアカウント :menuselection:`Settings --> Password and
authentication` から :guilabel:`Change password` フォームで操作する。

アクセストークンと SSH キーの更新方法については別に述べる。

Managing your personal access tokens
----------------------------------------------------------------------

アクセストークンとは何かというと：

  Personal access tokens are an alternative to using passwords for
  authentication to GitHub when using the GitHub API or the command line.

アクセストークンを要する操作は、実行者がそのアカウント利用者本人であるかのように
処理されると覚えておく。

アクセストークンは二種類ある：

  GitHub recommends that you use fine-grained personal access tokens instead of
  personal access tokens (classic) whenever possible.

こちらのほうが安全保障上の利点が旧式よりも優る。

.. admonition:: 読者ノート

   以下、断りがない限りアクセストークンは新式のほうとする。

..

  As a security precaution, GitHub automatically removes personal access tokens
  that haven't been used in a year.

これは怖い。GitHub には頻繁にアクセスしよう。

  Before creating a new personal access token, consider if there is a more
  secure method of authentication available to you

GitHub CLI を使うときと、GitHub Actions を使うときが該当する。

アクセストークン作成方法：
アカウント :menuselection:`Settings --> Developer settings` ページへ移動。
左柱 :menuselection:`Personal access tokens --> Fine-grained tokens` を押す。
:guilabel:`Generate new token` を押す。ページ内のフォームを埋める。
最後に :guilabel:`Generate token` を押して完了。

基本的には fine grained のほうを使いたいのだが、GitHub の文書を読んでいると
classic しか対応していない機能もある。それゆえこちらの作成方法も知っておくこと。

トークンを抹消することも可能。例のページで対象トークンに対する
:guilabel:`Delete` を押す。

  Once you have a personal access token, you can enter it instead of your
  password when performing Git operations over HTTPS.

HTTPS 限定。

Reviewing your SSH keys
----------------------------------------------------------------------

各種キーは定期的に監査するものだ。

アカウント :menuselection:`Settings --> SSH and GPG keys` ページで怪しいキーを
:guilabel:`Delete` する。

``eval "$(ssh-agent -s)"`` の手順で ``ssh-add -l -E sha256`` が成功しない場合は
単に ``ssh-add`` してからもう一度 ``ssh-add -l -E sha256`` を実行すればいいだろ
う。

Reviewing your deploy keys
----------------------------------------------------------------------

リポジトリーの :menuselection:`Settings --> Deploy keys` ページを開く。
要らなくなったキーを :guilabel:`Delete` するようにする。

Token expiration and revocation
----------------------------------------------------------------------

  When you create a personal access token, we recommend that you set an
  expiration for your token.

これならば期限を超えると自動的に失効となる。

  If a valid OAuth token, GitHub App token, or personal access token is pushed
  to a public repository or public gist, the token will be automatically
  revoked.

この運用ならば安心だ。他にもこのようなトークン失効を引き起こす事象がある。

Reviewing your security log
----------------------------------------------------------------------

アカウントの :menuselection:`Settings --> Security log` ページを開く。

  The name for each audit log entry is composed of a category of events,
  followed by an operation type. For example, the ``repo.create`` entry refers
  to the ``create`` operation on the ``repo`` category.

この機能は当分利用しないだろう。

Security log events
----------------------------------------------------------------------

アカウントの :menuselection:`Settings --> Security log` のフィルター ``action:``
一覧。

Removing sensitive data from a repository
----------------------------------------------------------------------

``git filter-repo`` を使って公にしてはならないファイルを履歴から抹消する技法を述
べている。実際にローカルで試してみたのだが、対象データとは影響のないコミットの
SHA も変化してしまうので、よほどのことがあっても使わない。

記事終わりの回避策を参考にするがいい：

  * Avoid the catch-all commands ``git add .`` and ``git commit -a`` on the
    command line—use ``git add filename`` and ``git rm filename`` to
    individually stage files, instead.
  * Use ``git add --interactive`` to individually review and stage changes
    within each file.
  * Use ``git diff --cached`` to review the changes that you have staged for
    commit. This is the exact diff that ``git commit`` will produce as long as
    you don't use the ``-a`` flag.

About anonymized URLs
----------------------------------------------------------------------

ここは何を述べているのかわからない。

  To host your images, GitHub uses the `open-source project Camo
  <https://github.com/atmos/camo>`__. Camo generates an anonymous URL proxy for
  each file which hides your browser details and related information from other
  users. The URL starts ``https://<subdomain>.githubusercontent.com/``, with
  different subdomains depending on how you uploaded the image.

About GitHub's IP addresses
----------------------------------------------------------------------

  For applications to function, you must allow TCP ports 22, 80, and 443 via our
  IP ranges for ``github.com``.

GitHub's SSH key fingerprints
----------------------------------------------------------------------

  You can add the following ssh key entries to your :file:`~/.ssh/known_hosts`
  file to avoid manually verifying GitHub hosts:

これを実施しておくと吉。

Sudo mode
----------------------------------------------------------------------

次の操作は GitHub が特に気密性が高いとしている：

  * Modification of an associated email address
  * Authorization of a third-party application
  * Addition of a new SSH key
  * Creation of a PAT or application

このような処理を行うために認証を通った後、セッションは一時的に sudo mode になる。

  GitHub has a two-hour session timeout period before prompting you for
  authentication again. During this time, any sensitive action that you perform
  will reset the timer.

Preventing unauthorized access
----------------------------------------------------------------------

  GitHub will gradually begin to require all users who contribute code on
  GitHub.com to enable one or more forms of two-factor authentication (2FA).

Viewing and managing your sessions
----------------------------------------------------------------------

  You can view a list of devices that have logged into your account, and revoke
  any sessions that you don't recognize.

アカウントの :menuselection:`Settings --> Sessions` ページを開く。セッション一覧
で項目を :guilabel:`See more` を押す。必要があれば :guilabel:`Revoke session` を
押す。

Securing your account with two-factor authentication (2FA)
======================================================================

About two-factor authentication
----------------------------------------------------------------------

  With 2FA, you have to log in with your username and password and provide
  another form of authentication that only you know or have access to.

とにかく別のものが必要だ。

  After you enable 2FA, GitHub generates an authentication code any time someone
  attempts to sign into your account on GitHub.com.

「誰か」にはアカウント利用者自身も含まれる。

  We strongly urge you to enable 2FA for the safety of your account, not only on
  GitHub, but on other websites and apps that support 2FA.

どうせ同じコード生成ソフトを使うから手間は GitHub のときと変わらないだろう。

Configuring two-factor authentication
----------------------------------------------------------------------

ユーザー名とパスワードに付加する認証情報を何にするかは利用者に選択肢がある。

  We strongly recommend using a time-based one-time password (TOTP) application
  to configure 2FA, and security keys as backup methods instead of SMS.

TOTP はワンタイムパスワードの acronym らしい。以下、これらの方法を中心に読んでい
く。

  After you configure 2FA, your account will enter a 28-day check up period. You
  can leave the check up period by successfully performing 2FA in those 28 days.

これはもう済んでいるから忘れていい。

  Just search for TOTP app in your browser to find various options.

ワンタイムパスワード用のソフトを別途用意しておく。ブラウザーの拡張機能にあるはず
だ。

.. admonition:: 読者ノート

   Google Chrome 系のブラウザーでは Authenticator という拡張をインストールしてお
   きたい。

アカウントの :menuselection:`Settings --> Password and authentication -->
Two-factor authentication` で :guilabel:`Enable two-factor authentication` して
おく。

:guilabel:`Setup authenticator app` は二度と出来ない？ 本文の記述どおりの UI が
出て来ない。

パスキーの設定もやっておこう。途中で Windows Hello がしゃしゃり出てくれば OK だ
ろう。

Configuring two-factor authentication recovery methods
----------------------------------------------------------------------

  In addition to securely storing your two-factor authentication (2FA) recovery
  codes, we strongly recommend configuring two or more authentication methods to
  avoid losing access to your account.

回復コードをダウンロードして保存しておく。

  If you generate new recovery codes or disable and re-enable 2FA, the recovery
  codes in your security settings automatically update. Reconfiguring your 2FA
  settings without disabling 2FA will not change your recovery codes.

アカウントの :menuselection:`Settings --> Password and authentication -->
Two-factor authentication` で :guilabel:`Recovery codes` を :guilabel:`View` す
る。

  Once you use a recovery code to regain access to your account, it cannot be
  reused.

これはうっかりしそうだから忘れるな。

.. todo::

   Authenticator ソフトにバックアップ機能があるから確認しておく。

Accessing GitHub using two-factor authentication
----------------------------------------------------------------------

  After you sign in to GitHub using your password, you'll need to provide an
  authentication code, tap a notification in GitHub Mobile, or use a security
  key to perform 2FA.

第一の方法しか行使したことがない。

  If you delete your authenticator application after configuring two-factor
  authentication, you'll need to provide your recovery code to get access to
  your account.

Authenticator ソフトをむやみに削除してはならない。

  If you have enabled 2FA, and you have added a passkey to your account, you can
  use the passkey to sign in. Since passkeys satisfy both password and 2FA
  requirements, you can complete your sign in with a single step.

これは便利そうだ。

  Enabling 2FA doesn't change how you authenticate to GitHub on the command line
  using SSH URLs.

良かった。

Recovering your account if you lose your 2FA credentials
----------------------------------------------------------------------

なるべく世話になりたくない項目。前節で述べられた
:file:`github-recovery-codes.txt` を安全に保存しておく。

ログイン時に :guilabel:`Use a recovery code or request a reset` を押せ。

  If you have added a passkey to your account, you can use your passkey to
  automatically regain access to your account.

この仕様があることもあり、パスキー認証は済ませておきたい。

以降、回復手順が複数記述されている。必要になったら本文を当たる方がいいだろうから
ノートをやめる。

Changing your preferred two-factor authentication method
----------------------------------------------------------------------

本文の記述と現行の UI が合致していない。

About mandatory two-factor authentication
----------------------------------------------------------------------

  Your account is selected for mandatory 2FA if you have taken some action on
  GitHub that shows you are a contributor.

いずれにせよ two-factor 認証を有効にしておく。

  We recommend setting up a time-based one-time password (TOTP) app as your
  primary 2FA method, and adding a passkey or security key as a backup.

..

  TOTP apps are the recommended 2FA factor for GitHub.

電話番号は教えなくていい：

  You only have to provide your phone number if you use SMS for 2FA.

Countries where SMS authentication is supported
----------------------------------------------------------------------

  If we don't support two-factor authentication via text message for your
  country of residence, you can set up authentication via a TOTP mobile
  application.

利用者がいる国によって SMS 認証の利用可能性が決まるという事情がなぜなのか気にな
るが、Japan があることを確認して忘れる。

Disabling two-factor authentication for your personal account
----------------------------------------------------------------------

アカウントの :menuselection:`Settings --> Password and authentication` ページを
開いて :guilabel:`Two-factor authentication` 見出しの右のボタンを押す。

.. admonition:: 読者ノート

   これをしてはいけない。

Authenticate with a passkey
======================================================================

About passkeys
----------------------------------------------------------------------

  You can also use passkeys for sudo mode and resetting your password.

妙に威力がある認証要素だ。

  Passkeys are pairs of cryptographic keys (a public key and a private key) that
  are stored by an authenticator you control. （略） Authenticators come in many
  forms, such as an iPhone or Android device, Windows Hello, a FIDO2 hardware
  security key, or a password manager.

RSA の一種なのか？

  When you sign in to GitHub.com using a passkey, your authenticator uses public
  key cryptography to prove your identity to GitHub without ever sending the
  passkey.

GitHub と利用者の間に authenticator という存在がある。利用者が何者であるかを保証
する存在だ。後述されている。

  For 2FA users, if you already have passkey-eligible security keys registered
  to your account for 2FA, you can upgrade these existing credentials into
  passkeys in your account settings.

おそらく、私の場合はこのようにはなっていない。

パスキーはデバイスに縛られるという表現が気になる。

Manage your passkeys
----------------------------------------------------------------------

パスキーの追加方法：アカウント :menuselection:`Settings --> Password and
authentication` ページを開く。:guilabel:`Add a passkey` を押して手なりで進める。
この途中の手順はパスキー供与者次第。

パスキーを削除するには、項目右のゴミ箱ボタンを押す。

  If you are only using device-bound passkeys, it is a best practice to register
  passkeys on at least two different devices, in case you lose access to one.

今は一台しかない PC でしかパスキーを使っていないから、もう一台で、たぶん Android
携帯電話で同様の手続きをすればいい。

Sign in with a passkey
----------------------------------------------------------------------

<https://github.com/login?passkey=true> で実行。すでにログインしている場合には
GitHub の Home ページが開く。

Connecting to GitHub with SSH
======================================================================

About SSH
----------------------------------------------------------------------

  When you connect via SSH, you authenticate using a private key file on your
  local machine.

SSH と鍵と計算機が関係することを覚えておく。

  You must also add the public SSH key to your account on GitHub before you use
  the key to authenticate or sign commits.

鍵は二種類あり、もう一方を GitHub に託す。

  You can further secure your SSH key by using a hardware security key,

電子の世界にない鍵を使うことが可能。

SSH 鍵目録を定期的に確認する。

  If you haven't used your SSH key for a year, then GitHub will automatically
  delete your inactive SSH key as a security precaution.

一年間出番のなかった SSH 鍵は GitHub が削除する。

Using SSH agent forwarding
----------------------------------------------------------------------

:command:`ssh-agent` の簡単な説明がある。

.. code:: console

   bash$ ssh -T git@github.com
   Hi showa-yojyo! You've successfully authenticated, but GitHub does not provide shell access.

   bash$ cat ~/.ssh/config
   Host github.com
       IdentityFile ~/.ssh/id_rsa
       User git

本文では転送設定を述べているが、ここでは行わない。コマンド ``echo
$SSH_AUTH_SOCK`` でそれらしい出力が得られればそれでいい。

.. code:: console

   bash$ ssh-add -L

これで鍵が :command:`ssh-agent` に見えることを確認。

Managing deploy keys
----------------------------------------------------------------------

まず SSH agent forwarding という技法について述べている。短所はあまりないようで：

  * Users must SSH in to deploy; automated deploy processes can't be used.
  * SSH agent forwarding can be troublesome to run for Windows users.

以前の節で述べられていた手順でこれをオンにして、配備スクリプトが SSH agent
forwading をするように仕向けろとある：

.. code:: bash

   bash$ ssh -A serverA 'bash -s' < deploy.sh

:command:`ssh` のオプション ``-A`` を覚えておけばいい。

  If you don't want to use SSH keys, you can use HTTPS with OAuth tokens.

この場合の短所は：

  * You must make sure that you configure your token with the correct access
    scopes.
  * Tokens are essentially passwords, and must be protected the same way.

Deploy key の定義：

  You can launch projects from a repository on GitHub.com to your server by
  using a deploy key, which is an SSH key that grants access to a single
  repository.

ここまで読んで、一連の機能を個人的には使いそうにないことが理解できた。この節の記
述はまだ続くが、いずれ必要になった場合に、読みに来てノートを取ることにする。

Checking for existing SSH keys
----------------------------------------------------------------------

このページは Linux タブを見ればいい。

  DSA keys (ssh-dss) are no longer supported. You cannot add new DSA keys to
  your personal account on GitHub.com.

.. code:: bash

   bash$ ls -al ~/.ssh

..

  Check the directory listing to see if you already have a public SSH key. By
  default, the filenames of supported public keys for GitHub are one of the
  following.

  * :file:`id_rsa.pub`
  * :file:`id_ecdsa.pub`
  * :file:`id_ed25519.pub`

鍵を新規作成するか、既存の鍵をアップロードすればいい。前者については次節で。

Generating a new SSH key and adding it to the ssh-agent
----------------------------------------------------------------------

  When you generate an SSH key, you can add a passphrase to further secure the
  key. Whenever you use the key, you must enter the passphrase.

.. code:: console

   bash$ ssh-keygen -t ed25519 -C YOUR_EMAIL

``YOUR_EMAIL`` では GitHub で利用しているアドレスを指定する。特に ``noreply`` ア
ドレスを用いている場合には、そのアドレスを指定しなければ verify してくれない。

これを実行する前に passphrase を決めておく。そして次の用意して鍵を追加する：

.. code:: console

   bash$ eval "$(ssh-agent -s)"
   bash$ ssh-add ~/.ssh/id_ed25519

最後に GitHub 上で鍵を追加する設定（次節参照）をする。

ハードウェア版手順の記載もあるが、この PC ではやらない。

Adding a new SSH key to your GitHub account
----------------------------------------------------------------------

前節の手続きは完了しているとする。GitHub での操作が述べられている。

アカウント :menuselection:`Settings --> SSH and GPG keys` ページを開く。
:guilabel:`SSH keys` 見出しの右の :guilabel:`New SSH key` を押す。フォームを埋め
て :guilabel:`Add SSH key` ボタンを押す。:guilabel:`Key` 欄には公開鍵を記入す
る。

この流れでは :file:`~/.ssh/id_ed25519.pub` の内容をコピー＆ペーストすることにな
る。入力欄のキューを読めばわかる。

Testing your SSH connection
----------------------------------------------------------------------

再び：

.. code:: console

   bash$ ssh -T git@github.com

Working with SSH key passphrases
----------------------------------------------------------------------

  With SSH keys, if someone gains access to your computer, the attacker can gain
  access to every system that uses that key. To add an extra layer of security,
  you can add a passphrase to your SSH key.

PC が盗まれたときに備えた仕掛けだ。

.. code:: console

   bash$ ssh-keygen -p -f ~/.ssh/id_ed25519

:command:`ssh-agent` は走らせておくものらしい。

Troubleshooting SSH
======================================================================

  When using SSH to connect and authenticate to GitHub, you may need to
  troubleshoot unexpected issues that may arise.

実際に問題が起こってから読んでも間に合う。

Using SSH over the HTTPS port
----------------------------------------------------------------------

HTTPS ポート経由の SSH が可能かどうかを試すコマンドは：

.. code:: console

   bash$ ssh -T -p 443 git@ssh.github.com

初回実行時にはプロンプトが出るが、次の文言ならば yes と答えて構わない：

.. code:: text

   The authenticity of host '[ssh.github.com]:443 ([20.27.177.118]:443)' can't be established.
   ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
   This host key is known by the following other names/addresses:
       ~/.ssh/known_hosts:4: [hashed name]
   Are you sure you want to continue connecting (yes/no/[fingerprint])?

失敗した場合には後述の Permission denied (publickey) を読め。

  If you are able to SSH into ``git@ssh.github.com`` over port 443, you can
  override your SSH settings to force any connection to GitHub.com to run
  through that server and port.

次の内容を :file:`~/.ssh/config` に追加する：

.. code:: text

   Host github.com
       Hostname ssh.github.com
       Port 443
       User git

動作確認コマンドは ``ssh -T git@github.com`` だ。

Recovering your SSH key passphrase
----------------------------------------------------------------------

Mac 以外では回復不能で、鍵ペアの作り直しとなる。

Deleted or missing SSH keys
----------------------------------------------------------------------

先述のように、GitHub は一年間利用がないキーを削除する。

  You can check if you haven't used an SSH key in a year by reviewing your
  account's security log.

Error: Host key verification failed
----------------------------------------------------------------------

  You may see this error if the server has changed its keys unexpectedly

GitHub が SSH ホスト鍵を変更した場合はブログで告知される。それを確認する。

  You can find an up-to-date list of GitHub's public SSH keys on GitHub Docs.

Error: Permission denied (publickey)
----------------------------------------------------------------------

* Git では :command:`sudo` をなるべく使わない。
* 正しいドメインに接続しようとしていることを確認する。
* 接続はすべて ``git`` ユーザーで行う必要がある。GitHub の利用者名ではない。
* 使用中の鍵があることを確認する。コマンド ``sh-add -l -E sha256``.

用がなくてもコマンド ``ssh -vT git@github.com`` は一度実行しておいて出力を眺めて
おくといい。

この節の内容は残りも有用。

Error: Bad file number
----------------------------------------------------------------------

  This error usually means you were unable to connect to the server. Often this
  is caused by firewalls and proxy servers.

解決策は HTTPS を使うようにするか、別のネットワークで試すか、前述の SSH over the
HTTPS port 技法を適用する。

Error: Key already in use
----------------------------------------------------------------------

たぶん鍵を使い回そうとしている。

  To resolve the issue, first remove the key from the other account or
  repository and then add it to your account.

Deploy key の使い回し問題も考えられる。

Error: Permission to user/repo denied to other-user
----------------------------------------------------------------------

  To fix this, the owner of the repository (user) needs to add your account
  (other-user) as a collaborator on the repository or to a team that has write
  access to the repository.

そもそも、Git のことをよくわからずに他人のリポジトリーに push しようとしていない
か。

Error: Permission to user/repo denied to user/other-repo
----------------------------------------------------------------------

このエラーはたぶん出ない。

Error: Agent admitted failure to sign
----------------------------------------------------------------------

まれに出るかもしれないエラー。

  You should be able to fix this error by loading your keys into your SSH agent
  with :command:`ssh-add`

.. code:: console

   bash$ eval "$(ssh-agent -s)"
   bash$ ssh-add PATH_TO_KEY

Error: ssh-add: illegal option -- K
----------------------------------------------------------------------

このエラーは生じない。

Error: SSL certificate problem, verify that the CA cert is OK
----------------------------------------------------------------------

CA ルート証明書が古い。

  If your CA root certificate needs to be updated, you won't be able to push or
  pull from GitHub repositories.

CA を更新する必要があり、それは OS を更新すれば十分のようだ。

Error: Unknown key type
----------------------------------------------------------------------

OpenSSH を更新する。

Error: We're doing an SSH key audit
----------------------------------------------------------------------

SSH 鍵が検証されていない。

  To fix this, you need to review your SSH keys and either reject or approve the
  unverified key.

GitHub のアカウント :menuselection:`Settings --> SSH and GPG keys` で適当に操作
する。

Managing commit signature verification
======================================================================

個人でリポジトリーを使うぶんには必要のない概念だが見ていく。

  GitHub will automatically sign commits you make using the GitHub web
  interface.

About commit signature verification
----------------------------------------------------------------------

署名の概念は辞書どおりに理解していい。

  If a commit or tag has a GPG, SSH, or S/MIME signature that is
  cryptographically verifiable, GitHub marks the commit or tag "Verified" or
  "Partially verified."

SSH 署名は単純であり、GPG はより高級：

  SSH signatures are the simplest to generate. （略） Generating a GPG signing
  key is more involved than generating an SSH key, but GPG has features that SSH
  does not. A GPG key can expire or be revoked when no longer used. GitHub shows
  commits that were signed with such a key as "Verified" unless the key was
  marked as compromised.

コミット状態は vigilane mode でない場合には次の三種類：

* Verified
* Unverified
* No verification status

GitHub でブランチをマージすると署名検証が機能しない。ローカルでマージする。

コミット状態は vigilane mode である場合には次の三種類：

* Verified
* Partially verified
* Unverified

署名を義務付けることが可能：

  Repository administrators can enforce required commit signing on a branch to
  block all commits that are not signed and verified.

ローカルで署名を検証することが可能だ：

  GitHub will automatically use GPG to sign commits you make using the web
  interface. Commits signed by GitHub will have a verified status. You can
  verify the signature locally using the public key available at
  https://github.com/web-flow.gpg. The full fingerprint of the key is ``5DE3
  E050 9C47 EA3C F04A 42D3 4AEE 18F8 3AFD EB23``.

..

  You can optionally choose to have GitHub GPG sign commits you make in GitHub
  Codespaces.

GPG を使って署名コミットをする手順は：

  + Check for existing GPG keys
  + Generate a new GPG key
  + Add a GPG key to your GitHub account
  + Tell Git about your signing key
  + Sign commits
  + Sign tags

個別について詳細は後述。

  You can use SSH to sign commits with an SSH key that you generate yourself.

  + Check for existing SSH keys
  + Generate a new SSH key
  + Add a SSH signing key to your GitHub account
  + Tell Git about your signing key
  + Sign commits
  + Sign tags

GitHub はローカルで署名したコミットやタグが GitHub.com のアカウントに追加した公
開鍵に対して暗号的に検証可能かどうかを確認する。

S/MIME は企業向けらしいので割愛。

Displaying verification statuses for all of your commits
----------------------------------------------------------------------

  You can enable vigilant mode for commit signature verification to mark all of
  your commits and tags with a signature verification status.

署名の意図はこうだ：

  Git allows you to set the author of your changes and the identity of the
  committer. This, potentially, makes it difficult for other people to be
  confident that commits and tags you create were actually created by you.

他人に信用させるのが目的だ。

  you can give other users increased confidence in the identity attributed to
  your commits and tags by enabling vigilant mode in your GitHub settings.

Vigilant mode を有効にする条件は限定される：

  You should only enable vigilant mode if you sign all of your commits and tags
  and use an email address that is verified for your account on GitHub as your
  committer email address. After enabling this mode, any unsigned commits or
  tags that you generate locally and push to GitHub will be marked "Unverified."

手順：アカウント :menuselection:`Settings --> SSH and GPG keys` ページへ移動。
:menuselection:`Vigilant mode --> Flag unsigned commits as unverified` をオンに
する。

.. admonition:: 読者ノート

   署名コミットの準備が整わない間はオフでいいと思う。

Checking for existing GPG keys
----------------------------------------------------------------------

  Before you generate a GPG key, you can check to see if you have any existing
  GPG keys.

.. code:: console

   bash$ gpg --list-secret-keys --keyid-format=long

おそらく：

  If there are no GPG key pairs or you don't want to use any that are available
  for signing commits and tags, then generate a new GPG key.

次の節を参照。

コミットやタグの署名に使いたい GPG 鍵対が用意してある場合は、次のコマンドを使っ
て公開キーを表示し、使いたい GPG 鍵 ID を割り当てることが可能：

.. code:: console

   bash$ gpg --armor --export XXXXXXXXXXXXX

それから GitHub の設定ページを開くことになるはずだ。

Generating a new GPG key
----------------------------------------------------------------------

コマンド実行に入る前に利用者情報と passphrase を用意しておく。メールアドレスの入
力はいつもの ``noreply`` アドレスに関する注意をする。

.. code:: console

   bash$ gpg --full-generate-key
   ...
   bash$ gpg --list-secret-keys --keyid-format=long
   ... (GPG_ID)
   bash$ gpg --armor --export GPG_ID

出力された長い文字列を定型コードに埋め込んで GitHub に設定（次節参照）。

.. code:: text

   -----BEGIN PGP PUBLIC KEY BLOCK-----
   略
   -----END PGP PUBLIC KEY BLOCK-----

Adding a GPG key to your GitHub account
----------------------------------------------------------------------

鍵は用意できているものとする。

  You can add multiple public keys to your account on GitHub. Commits signed by
  any of the corresponding private keys will show as verified.

アカウント :menuselection:`Settings --> SSH and GPG keys` ページを開く。
:guilabel:`New GPG key` を押して :guilabel:`Title` と :guilabel:`Key` を記入す
る。フォームを埋めたら :guilabel:`Add GPG Key` を押す。

:guilabel:`Key` の内容は前節で述べた長い文字列だ。

Telling Git about your signing key
----------------------------------------------------------------------

  To sign commits locally, you need to inform Git that there's a GPG, SSH, or
  X.509 key you'd like to use.

GPG 鍵が複数ある場合に意味がある。

.. code:: console

   bash$ git config --global --unset gpg.format
   bash$ gpg --list-secret-keys --keyid-format=long
   bash$ git config --global user.signingkey XXXXXXXXXXX
   bash$ git config --global commit.gpgsign true

:file:`.bashrc` のどこかで ``export GPG_TTY=$(tty)`` する。少し試したい場合には
この環境変数をその場で定義すればいい。

  You can use an existing SSH key to sign commits and tags, or generate a new
  one specifically for signing.

.. code:: console

   bash$ git config --global gpg.format ssh
   bash$ git config --global user.signingkey /PATH/TO/.SSH/KEY.PUB

:file:`.gitconfig` を公開できる設定と非公開設定とに分割して、``include`` で非公
開部分を取り込むようにファイルを構成するといい。非公開部分にフルパス指定を含め
るのだ。

X.509 鍵は割愛。

Associating an email with your GPG key
----------------------------------------------------------------------

  If you're using a GPG key that matches your committer identity and your
  verified email address associated with your account on GitHub.com, then you
  can begin signing commits and signing tags.

.. code:: console

   bash$ gpg --edit-key XXXXXXXXXXX
   gpg> adduid
   ...
   gpg> save
   bash$ gpg --armor --export XXXXXXXXXXX

前節で述べられてるようにして GitHub にアップロードする。

.. admonition:: 読者ノート

   メールアドレスを ``noreply`` のほうで作ること。いったん間違えると ``uid`` 系
   サブコマンドを駆使して修正するハメになる。このときの対話的操作にクセがあり、
   けっこう難しい。

Signing commits
----------------------------------------------------------------------

  You can sign commits locally using GPG, SSH, or S/MIME.

..

  To configure your Git client to sign commits by default for a local
  repository, in Git versions 2.0.0 and above, run ``git config commit.gpgsign
  true``. To sign all commits by default in any local repository on your
  computer, run ``git config --global commit.gpgsign true``.

繰り返しになるが：

  If you have multiple keys or are attempting to sign commits or tags with a key
  that doesn't match your committer identity, you should tell Git about your
  signing key.

``git commit`` のオプション ``-S`` で署名コミットとなる。

Signing tags
----------------------------------------------------------------------

  You can sign tags locally using GPG, SSH, or S/MIME.

``git tag`` コマンドのオプション ``-s`` で署名する。署名したタグを確認するにはオ
プション ``-v`` を使う。

Troubleshoot verification
======================================================================

Check verification status
----------------------------------------------------------------------

  You can check the verification status of your commit and tag signatures on
  GitHub.

GitHub のリポジトリー画面 :guilabel:`Pull request` 以下から確認する。
:guilabel:`Commits` タブを開くと :guilabel:`Verified` ボタンがあるはず。

タグに対しては :menuselection:`Releases --> Tags` で :guilabel:`Verified` ボタン
がある。

Use verified email in GPG key
----------------------------------------------------------------------

コミットとタグはメールアドレスを複数含むことがある。コミットについては：

  For commits, there is the author — the person who wrote the code — and the
  committer — the person who added the commit to the tree. When signing a commit
  with Git, whether it be during a merge, cherry-pick, or normal git commit, the
  committer email address will be yours, even if the author email address isn't.

タグについては簡単で：

  The tagger email address is always the user who created the tag.
