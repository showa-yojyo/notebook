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

TBW

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
て :guilabel:`Add SSH key` ボタンを押す。:guilabel:`Key` 欄には公開鍵を記入する。

`ssh-add -l -E sha256` と同じ文字列だ。

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
