======================================================================
Oh My Posh 利用ノート
======================================================================

  Oh My Posh is a custom prompt engine for any shell that has the ability to
  adjust the prompt string with a function or variable. (Introduction)

.. contents:: 見出し一覧
   :local:

目標
======================================================================

本稿では次を目標とする：

1. Oh My Posh を Windows と WSL Ubuntu の両方にインストールする
2. 推奨フォントを Windows にインストールする
3. 推奨フォント設定を Windows Terminal と Visual Studio Code に実施する
4. プロンプトに Oh My Posh を組み込む
5. プロンプトをカスタマイズする

実施する事柄を表にまとめる：

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   タスク | Windows | Ubuntu
   Oh My Posh をシステムにインストールする | Yes | Yes
   推奨フォントを設定する | Yes | No
   プロンプトに Oh My Posh を組み込む | Yes | Yes
   プロンプトを構成する | Yes/No | No/Yes

次を事前条件をする（本ノート当該項目それぞれを参照）：

* WSL は導入済みであり、Distribution は Ubuntu であるとする。さらにシェルは Bash
  であるとする。
* Windows Terminal は導入済みであるとする。そこでは WSL も PowerShell も対応済み
  とする。
* Visual Studio Code は導入済みであるとする。

.. seealso::

   * :doc:`/wsl`
   * :doc:`/wt`
   * :doc:`vscode/index`

Oh My Posh をシステムにインストールする
======================================================================

Oh My Posh 本体を WSL (Ubuntu) と Windows それぞれにインストール、更新、アンイン
ストールする方法を記す。

WSL
----------------------------------------------------------------------

  A `Homebrew <https://brew.sh/>`__ formula is available for easy installation.
  When installing Homebrew for Linux, be sure to follow Next steps instructions
  to add Homebrew to your PATH and to your bash shell profile script, and
  Requirements to build Oh My Posh.

Homebrew についてはノートを割愛する。Homebrew がなくても Oh My Posh 単品でインス
トールすることは可能だが、更新やアンインストールの手間を考えると Homebrew の枠組
を採用するほうがいい。

インストール、更新、アンインストールのコマンドはそれぞれ次のとおり：

.. sourcecode:: shell
   :caption: 管理コマンド各種

   brew install jandedobbeleer/oh-my-posh/oh-my-posh
   brew update && brew upgrade oh-my-posh
   brew uninstall oh-my-posh

更新には次のコマンドも使える：

.. sourcecode:: console
   :caption: Oh My Posh 専用アップグレードコマンド

   $ oh-my-posh upgrade

インストール手順が完了すると、実行形式 :file:`$(brew --prefix)/bin/oh-my-posh`
とテーマ各種を格納するディレクトリー :file:`$(brew --prefix oh-my-posh)/themes`
が得られる。

Windows
----------------------------------------------------------------------

Oh My Posh 本体を Windows へインストールするには :program:`winget` を用いる。し
たがって Oh My Posh を更新、アンインストールするのにも :program:`winget` を用い
る。

.. sourcecode:: doscon

   winget install --id JanDeDobbeleer.OhMyPosh
   winget upgrade --id JanDeDobbeleer.OhMyPosh
   winget uninstall --id JanDeDobbeleer.OhMyPosh

この手順が完了すると、上述の実行可能ファイルとテーマ各種がファイルシステムにイン
ストールされる。

インストールすることで環境変数 :envvar:`PATH` が更新されて
:program:`oh-my-posh.exe` が実行可能になる。インストールしたセッションのコンソー
ルをいったん終了するといい。

推奨フォントをシステムにインストールする
======================================================================

Oh My Posh を余すとこなく利用するのにフォントを別途インストールすることが推奨さ
れている。これにより、プロンプト文字列中にマイナーな文字を書き込むと、文字化けし
て豆腐になるのを避ける。

  Oh My Posh was designed to use `Nerd Fonts <https://www.nerdfonts.com/>`__.
  Nerd Fonts are popular fonts that are patched to include icons. We recommend
  `Meslo LGM NF <https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/Meslo.zip>`__,
  but any Nerd Font should be compatible with the standard themes.

リンク先からフォントをダウンロードして Windows のインストールするのかと思いき
や、Oh My Posh 自身がフォントのインストールをサポートしている。次のコマンドを管
理者権限で起動したコンソールから実行する：

.. sourcecode:: doscon

   oh-my-posh font install

コンソール上にメニューが現れるので、本文で推奨されている ``Meslo`` を選択、決定
などする。成功するとその旨が表示される。念のため :file:`C:\\Windows\\Fonts` を調
べるといい。

最後に、特殊フォントを必要としない Oh My Posh テーマが用意されていることを心に留
めておく：

  If you are not interested in using a Nerd Font, you will want to use a theme
  which doesn't include any Nerd Font icons. The ``minimal`` themes do not make
  use of Nerd Font icons. (Fonts)

推奨フォントを端末エミュレーターに設定する
----------------------------------------------------------------------

次に Windows Terminal および Visual Studio Code それぞれで端末ウィンドウのフォン
トを指定する。

.. seealso::

   * :doc:`/wt`
   * :doc:`/vscode/index`

Windows Terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Windows Terminal のフォント設定は例えば :guilabel:`Settings` から
:menuselection:`Defaults --> Appearance` の :guilabel:`Font face`,
:guilabel:`Font size` を調整して :guilabel:`Save` ボタンを押す。もしくは下記のよ
うに JSON ファイルをエディターで書き換えてもよい。いずれの方法にせよ、同じ結果に
なる：

  Once you have installed a Nerd Font, you will need to configure the Windows
  Terminal to use it. This can be easily done by modifying the Windows Terminal
  settings This can be easily done by modifying the Windows Terminal settings
  (default shortcut: :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`,`). In your
  :file:`settings.json` file, add the :guilabel:`font.face` attribute under the
  :guilabel:`defaults` attribute in profiles

Visual Studio Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  This can be done by changing the Integrated: Font Family value in the Terminal
  settings (default shortcut: :kbd:`Ctrl` + :kbd:`,` and search for
  :guilabel:`Integrated: Font Family` or via
  :menuselection:`Users --> Features--> Terminal`).
  If you are using the JSON based settings, you will need to update the
  ``terminal.integrated.fontFamily`` value. Example in case of ``MesloLGM NF``
  Nerd Font:

.. admonition:: 利用者ノート

   ``editor.fontFamily`` のほうをきっちり指定しておき、端末フォントのほうは空欄
   にしておくといい。

   .. sourcecode:: json
      :caption: 文字が豆腐にならないような ``editor.fontFamily`` 設定例

      {
        "editor.fontFamily": "'BIZ UDGothic', 'MesloLGL NFM', Consolas, 'Courier New', monospace"
      }


プロンプトを Oh My Posh に割り当てさせる
======================================================================

Oh My Posh にプロンプト文字列を動的に構成させる方法を記す。これはシェルごとの構
成になる。まずは設定ファイルを指定せず、既定の構成を適用する方法を記す。

Bash
----------------------------------------------------------------------

Oh My Posh は UNIX/Linux 系シェルの対応しているものの、私は Bash しか利用しない。

  Add the following to :file:`~/.bashrc` (could be :file:`~/.profile` or
  :file:`~/.bash_profile` depending on your environment):

  .. sourcecode:: shell
     :caption: Bash 対話環境に Oh My Posh を組み込む

     eval "$(oh-my-posh init bash)"

自分のスタートアップファイルを確認して、環境変数 :envvar:`PS1` などを初期化して
いるコードを含む方に追加すると整合する。コマンド ``oh-my-posh init bash`` は環境
変数 :envvar:`PROMPT_COMMAND` を独自関数プラス既存の :envvar:`PROMPT_COMMAND` で
置き換えるシェルコードを生成する。このコードは是非とも一読しておきたい。

起動ファイルを編集、保存したのちに :command:`source` するかセッションを再起動す
ることで、端末画面上のプロンプトの見栄えが著しく変化することが確認できるはずだ。

PowerShell
----------------------------------------------------------------------

私は PowerShell をほとんど利用しないが、Oh My Posh の機能を堪能するべくこちらも
試す。

  Edit your PowerShell profile script, you can find its location under the
  ``$PROFILE`` variable in your preferred PowerShell version.

Bash でいうところの :file:`.bash_profile` のようなファイルをテキストエディターで
開く。実際には :file:`Microsoft.PowerShell_profile.ps1` のような名前のファイル
だ。そして次のような行を加えておく：

.. sourcecode:: pwsh

   oh-my-posh init pwsh | Invoke-Expression

この起動ファイルを編集、保存する。PowerShell セッションが開いていればそこで

.. sourcecode:: pwsh

   . $PROFILE

を実行するか、あるいは PowerShell を再起動すれば、端末画面内のプロン
プトの見栄えが変化していることが確認できる。

プロンプトをカスタマイズする
======================================================================

  For your convenience, the existing themes from Oh My Posh hhave been added to
  version 4, so you can get started even without having to understand the
  theming. So, let's no longer waste time on theory, have a look at the
  installation guide to get started right away! (Introduction)

Oh My Posh は既定のテーマを用意しているためテーマを自作しなくても利用できる。あ
くまでも利便性のためにそうなっているだけであり、プログラマーがテーマをカスタマイ
ズして作業するのが Oh My Posh の常識だ。

Bash
----------------------------------------------------------------------

先述のコマンド ``oh-my-posh init`` が生成するコードが含む関数 ``_omp_hook()`` を
見ればわかるように、コマンド ``oh-my-posh print primary`` が Bash 環境変数
:envvar:`PS1` の値を割り当てる。注目するべきは ``--config="$POSH_THEME"`` の部分
だ。この環境変数の値がテーマファイルを示す。

シェルのスタートアップファイルに追加した :command:`eval` 呼び出しを、例えば次の
ように書き換える：

.. sourcecode:: shell
   :caption: Bash 対話環境に Oh My Posh を組み込む際に構成ファイルを指定する

   eval "$(oh-my-posh init bash --config $XDG_CONFIG_HOME/.omp.json)"

これにより次の影響がある：

* 環境変数 :envvar:`POSH_THEME` にパス :file:`$XDG_CONFIG_HOME/.omp.json` が割り
  当てられる。
* 環境変数 :envvar:`PROMPT_COMMAND` が変化する。

自作テーマを与えるには、既存テーマファイルを複製し、それを好みで編集すればいい。
既存テーマの場所は後述するコツで述べる。

PowerShell
----------------------------------------------------------------------

考え方は Bash の場合と同じだ。スタートアップファイル `$PROFILE` に加えた行を次のように修正する：

.. sourcecode:: pwsh

   oh-my-posh init pwsh --config "$env:USERPROFILE\omp.json" | Invoke-Expression

テーマファイルはパス :file:`%USERPROFILE%omp.json` に用意したものとする。

  When using oh-my-posh in Windows and the WSL, know that you can share your
  theme with the WSL by pointing to a theme in your Windows user's home folder.

二重管理を避け、テーマファイルをどちらか一方の環境で管理するのが望ましい。
Windows から WSL にある設定ファイルを指定するならば、WSL Ubuntu がドライブ U に
マウントされているとして次のように書ける：

.. sourcecode:: pwsh

   oh-my-posh init pwsh --config "U:\home\USERNAME\PATH\TO\omp.json" | Invoke-Expression

普通は Windows 側に設定ファイルを置いて WSL 側から
:file:`/mnt/c/PATH/TO/omp.json` で参照するのが安定するだろうが、私は WSL の Git
でバージョン管理をしたいのでそれを避けざるを得ない。

テーマファイルを編集する
----------------------------------------------------------------------

以下、JSON 形式でテーマファイルを管理するものとする。

後述するインストール済みテーマを確認するの節の内容に沿って既存のテーマを下見し、
気に入ったものを複製して :envvar:`XDG_CONFIG_HOME` などに :file:`.omp.json` など
の名前で置いたことを前提として記す。

  To fully understand how to customize a theme, read through the documentation
  in the configuration and segments sections. The configuration section covers
  the basic building blocks and concepts of Oh My Posh themes, while the
  segments section covers how to configure each available segment.

テーマプレビュー、仕様書、エディター、端末画面を反復しながらカスタマイズするしか
テーマの何たるかを理解する手段はない。

テーマオブジェクト概要
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Oh My Posh renders your prompt based on the definition of blocks (like Lego)
  which contain one or more segments.

Block と Segment の概念が重要だとわかるが、それでもテーマオブジェクトにもわずか
な属性がある。カスタマイズの観点からはそれほど重要ではない属性でありそうだが、目
を通しておこう。

  Oh My Posh themes can utilize JSON Schema to validate their contents. Themes
  should include a link to the external schema document which prescribes the
  appropriate structure and contents for various elements. If your code editor
  is configured to use JSON Schema, it will compare your custom theme to the
  external document, and issue warnings for discrepancies.

Visual Studio Code でテーマ JSON ファイルを編集するときにこの事実が効いてくる。
テキスト補完時に適切な選択肢を提示してくれるのだ。

ルート部分
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

JSON オブジェクトのいちばん外側の属性をまとめる。

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   属性 @ 型 @ 機能
   ``accent_color`` @ 文字列 @ ``accent`` 色が使用不可能の場合の代替色
   ``blocks`` @ 配列 @ Block オブジェクトの配列（次節参照）
   ``final_space`` @ 真偽値 @ プロンプトの末尾に空白字を追加するか否か
   ``terminal_background`` @ 文字列 @ 背景部分の色
   ``upgrade`` @ Upgrade @ アップグレードの自動処理や通知を構成する
   ``var`` @ Object @ 自作の定数をここに配置可能
   ``version`` @ 数 @ 構成バージョンの値 ``4``

* 色指定については公式文書にある記述 (color_) を見ろ。
* 属性 ``var`` の値は Segment 属性 ``template`` の値文字列、二重中括弧記法中にお
  いて :samp:`.Var.variable-name` の形式により参照可能。
* 属性 ``upgrade`` については公式文書にある記述 (upgrade_) を見ろ。

Block
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Block | Oh My Posh <https://ohmyposh.dev/docs/configuration/block>`__

設定オブジェクトは ``blocks`` という配列型属性を一つ含む。その配列要素をブロック
と呼ぶ。以下、ブロックの属性をいくつか述べる。

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   属性 @ 型 @ 機能
   ``alignment`` @ ``left`` | ``right`` @ ブロックが左揃えか右揃えか
   ``filler`` @ 文字列 @ 左揃えブロックと右揃えブロックの間を埋める文字列
   ``force`` @ 真偽値 @ 内容が空であってもブロックを描くか否か
   ``leading_diamond`` @ 文字列 @ 下記参照
   ``newline`` @ 真偽値 @ ブロックを新規行から開始するか否か
   ``overflow`` @ ``break`` | ``hide`` @ 下記参照
   ``segments`` @ 配列 @ 次節参照
   ``trailing_diamond`` @ 文字列 @ 下記参照
   ``type`` @ ``prompt`` | ``rprompt`` @ 下記参照

属性 ``leading_diamond`` は、ブロックがどの Segment で始まろうが、開始ダイヤモン
ドとして用いる記号を値に取る。属性 ``trailing_diamond`` はその終了ダイヤモンド版
だ。

属性 ``filler`` は右揃えブロックに対して設定する。テンプレートを含んだ文字列を指
定可能。

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   名前 @ 型 @	効果
   ``.Overflow`` @ 文字列 @ 必要に応じて ``hide`` または ``break``
   ``.Padding`` @ 整数 @ 左右ブロック間の長さ

属性 ``newline`` は値がどちらであっても、``"bash"`` と ``"pwsh"`` の場合にはプロ
ンプトが一行目にあるとき、シェルセッション開始時には、最初のブロックに定義されて
いる改行を表示しない。

属性 ``overflow`` は右寄せブロックに対しては、ブロックが長過ぎて左寄せのブロック
からはみ出る場合、ブロックを壊すか、非表示にするかを指示する。

属性 ``type`` の値が ``"rprompt"`` の場合、断片はキャレットの右に揃えられる。こ
のようなブロックは高々一つしか許されない。

.. seealso::

   `Deprecating the bash rprompt <https://ohmyposh.dev/blog/deprecating-bash-rprompt>`__

Segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Segment | Oh My Posh <https://ohmyposh.dev/docs/configuration/segment>`__

ブロックオブジェクトには次の型のオブジェクトからなる配列 ``segments`` を値とする
属性がある。この構成要素の型を Segment と呼ぶ。以下、Segment の属性をいくつか説
明する。

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   属性 @ 型 @ 機能
   ``alias`` @ 文字列 @ 本稿では取り扱わない
   ``background`` @ 文字列 @ 背景色
   ``background_templates`` @ 配列 @ Template 配列
   ``cache`` @ Cache @ 本稿では取り扱わない
   ``exclude_folders`` @ 配列 @ このいずれかで作業している場合は無効
   ``force`` @ 真偽値 @ 空白しかなくても出力するか否か
   ``foreground`` @ 文字列 @ 文字色
   ``foreground_templates`` @ 配列 @ Template 配列
   ``include_folders`` @ 配列 @ このいずれかで作業している場合は有効
   ``index`` @ 数 @ 本稿では取り扱わない
   ``interactive`` @ 真偽値 @ 対話型プロンプトのエスケープ文字を生のまま使うか否か？
   ``invert_powerline`` @ 真偽値 @ 文字色と背景色を交換するか否か
   ``leading_diamond`` @ 文字列 @ Segment 先頭で使用する文字
   ``leading_powerline_symbol`` @ 文字列 @ Segment 先頭に使用する文字
   ``max_width`` @ 桁数 @ 端末幅がこの値より大きい場合に Segment を隠す
   ``min_width`` @ 桁数 @ 端末幅がこの値より小さい場合に Segment を隠す
   ``options`` @ 配列 @ Option 配列
   ``placeholder`` @ 文字列 @ 本稿では取り扱わない
   ``powerline_symbol`` @ 文字列 @ Segment 末尾に使用する文字
   ``style`` @ 文字列 @ 下記参照
   ``template`` @ 文字列 @ プロンプトを描くための Go 様式テキストテンプレート
   ``templates`` @ 配列 @ 本稿では取り扱わない
   ``templates_logic`` @ 文字列 @ 本稿では取り扱わない
   ``timeout`` @ ミリ秒 @ 実行時間切れ
   ``trailing_diamond`` @ 文字列 @ Segment 末尾で使用する文字
   ``type`` @ 文字列 @ Segment の型名

属性 ``foreground``, ``background`` には文字色、背景色をそれぞれ指定する。値の書
式は ``#rrggbb`` 形式で指定するのが無難。透明は ``"transparent"`` とする。より高
級な属性 ``foreground_templates``, ``background_templates`` も存在し得る。現在の
状況に応じて色を定義する文字列テンプレートの配列だ。詳しくは公式文書 (color_) を
見ろ。

属性 ``cache`` は Segment の更新頻度を調整する Cache 型の値をとる。その属性は次
のとおり：

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   属性 @ 型 @ 機能
   ``duration`` @ 文字列 @ Segment をキャッシュしておく期間
   ``strategy`` @ ``session`` | ``folder`` | ``device`` @ キャッシュ判断戦略

属性 ``{include,exclude}_folders`` は特定のディレクトリーで Segment を有効または
無効にするのに用いられる。

属性 ``{leading,trailing}_diamond`` の意味は Block における同名属性と同様。ただ
し、文字の色は Segment 背景色に等しい。

属性 ``leading_powerline_symbol`` は Segment の先頭で使用する文字。ただし、属性
``style`` が ``"powerline"`` である場合に用いられる。用途は、Segment 開始に黒い
ちらつきが見える場合に、この属性値として ``powerline_symbol`` 値の対応文字を設定
するというものらしい。

属性 ``{max,min}_width`` を、端末幅の長さからくる制約のために隠したい Segment が
あれば、それを隠すのに利用可能だ。値を ``0`` にすると、この機能は効かない。

属性 ``options`` の構成は Segment の類型によって異なる。

属性 ``style`` には次の選択肢がある：

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   値 | 意味
   ``"powerline"`` | 属性 ``powerline_symbol`` の値により Segment を分割
   ``"plain"``     | 透過背景に文字しかない単純な描画
   ``"diamond"``   | ``powerline`` の変種で、始点にも対応
   ``"accordion"`` | ``powerline`` の変種で、無効時でもテキストなしで描画

本稿では断りのない限り値 ``"powerline"`` を与えているものとする。

属性 ``template`` がいちばん重要だ。この Segment の内容を与える Template を定義
する。文字列であって、二重中括弧に囲まれた何かが含まれるようなものだ。

.. sourcecode:: json
   :caption: 公式より引用
   :force:

   {
      "template": " {{ if .Segments.Git.UpstreamGone }}{{ else if gt .Code 0 }}{{ else }}{{ end }} "
   }

属性 ``templates`` は Segment の Template 文字列を複数行にわたり記述するためのも
のだ。長い文字列を一行で定義したくないという理由だけで採用することがよくある。属
性 ``template_logic`` の値に基づき、狙いに応じて結果となり得るものが二つある：

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   値 | 意味
   ``"first_match"`` | 配列のうち最初の空白以外の文字列を返し、それ以外すべてを飛ばす
   ``"join"``        | 配列要素すべてを評価し、非空白文字列のものすべてを結合したもの

属性 ``type`` には Segment 類型を文字列により指示する。私が使いたいものは次のも
のだ：

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   値 @ リンク @ 意味
   ``"git"``   @ Git リポジトリーの情報を示す
   ``"node"``  @ アクティブ Node.js バージョン示す
   ``"npm"``   @ アクティブ NPM バージョンを示す
   ``"path"``  @ 現在のパスを示す
   ``"python"``@ アクティブ Python バージョンおよび仮想環境を示す
   ``"root"``  @ 現在ユーザーが root である場合に表示する
   ``"shell"`` @ 現在のシェルを示す
   ``"text"``  @ 文字列を書く
   ``"time"``  @ 現在時刻を書く

使用可能 ``type`` を知るには、上記リンク先のページ左側の Segment ツリーを見ると
いい。

* <https://ohmyposh.dev/docs/segments/scm/git>
* <https://ohmyposh.dev/docs/segments/languages/node>
* <https://ohmyposh.dev/docs/segments/cli/npm>
* <https://ohmyposh.dev/docs/segments/system/path>
* <https://ohmyposh.dev/docs/segments/languages/python>
* <https://ohmyposh.dev/docs/segments/system/root>
* <https://ohmyposh.dev/docs/segments/system/shell>
* <https://ohmyposh.dev/docs/segments/system/text>
* <https://ohmyposh.dev/docs/segments/system/time>

Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Templates | Oh My Posh <https://ohmyposh.dev/docs/configuration/templates>`__

Segment の看板属性とも言える ``template`` の書式の仕様だ。Go 言語の知識があれば有
利らしい。

コツ
======================================================================

プレビュー
----------------------------------------------------------------------

1. 一時的な設定ファイルを用意する。以降の説明では :file:`omp-temp.json` とする。
2. 次のコマンドを実行する：

   .. sourcecode:: shell
      :caption: プレビューコマンド

      oh-my-posh print primary --config omp-temp.json --shell uni

この出力が Oh My Posh プロンプト文字列だ。次で述べるコツと併用するといい。もっと
も、``oh-my-posh init bash --config`` がプロンプト表示時に常時評価されるので、い
つも使っている JSON を編集しつつ、端末で :kbd:`Enter` を押すのが楽だ。

Segment 単位のオンオフ切り替え
----------------------------------------------------------------------

  Sometimes run into a situation where you don't want to see a specific segment
  but the use-case does not justify using a conditional template. In this case
  you can use the ``oh-my-posh toggle <type>`` command to toggle the segment on or
  off. This works on a **per shell session basis**, meaning that if you toggle a
  segment off in one instance of a shell, it will not disable in the others.

例えばプロンプトには ``type`` が ``"python"`` である Segment を含んでいて現在そ
れが表示されるが、今は Node.js に依存するプロジェクトを開発しているので、一時的
に Python 情報表示をオフにしたいとする。こういうときに

.. sourcecode:: shell
   :caption: ``python`` Segment のオンオフを切り替えるコマンド

   oh-my-posh toggle python

とする。直後のプロンプト表示から当該 Segment の表示がオフになる。このコマンドを
再び実行すると、Python 情報 Segment 表示がオンに戻る。

  To list the currently toggled segments, use ``oh-my-posh get toggles``.

このコマンドは表示オフ Segment のすべてが一覧できる。

インストール済みテーマを確認する
----------------------------------------------------------------------

PowerShell ならば次のコマンドでインストールされているテーマとそのプレビューを一
覧することが可能だ：

.. sourcecode:: pwsh

   Get-PoshThemes

Bash ならばテーマディレクトリーが次のパスにある。演習として PowerShell
``Get-PoshThemes`` 相当の機能を自分で実装してみるのもありだろう。

.. sourcecode:: shell

   $HOMEBREW_PREFIX/Cellar/oh-my-posh/$(oh-my-posh version)/themes

オンラインでウェブブラウザーが開いていれば、次のページを確認するのが早いかもしれ
ない： `Themes | Oh My Posh <https://ohmyposh.dev/docs/themes>`__

言語系 Segment の ``options`` の内容は似ている
----------------------------------------------------------------------

次の Segment の属性 ``type`` が ``"python"``, ``"ruby"``, ``"node"`` などの場合
には属性 ``options`` の値オブジェクトにおいて、キー ``home_enabled``,
``display_mode``, ``fetch_version``, その他が共通して有効だ。

.. sourcecode:: json
   :caption: 属性 ``options`` 例

   {
       "type": "xxxx",
       "style": "powerline",
       "powerline_symbol": "xxxx_symbol",
       "template": " {{ .Full }}",
       "options": {
           "home_enabled": true,
           "fetch_version": true,
           "display_mode": "files"
       }
   }

属性 ``home_enabled`` の既定値は ``false`` であるが、これは :file:`$HOME` 直下に
スクリプトファイルがないことが普通だからと考えられる。

属性 ``fetch_version`` の既定値は ``true`` であり、これが自然なので明記しなくて
いい。

属性 ``display_mode`` の既定値は文字列 ``files`` であり、言語に関係するファイル
が :file:`$PWD` にある場合に Segment が有効になることを指示する。言語によっては
もっと細かい制御をする値が用意されている。

時刻を JST で表示する
----------------------------------------------------------------------

Segment の構成を模索中。時刻書式の指定を Go 言語方式でする。これは難解だ。

.. sourcecode:: json
   :caption: 時刻書式例
   :force:

   {
        "type": "time",
        "style": "plain",
        "invert_powerline": true,
        "foreground": "#ff1493",
        "options": {
          "time_format": "15:04:05 JST+9:00"
        },
        "template": " \uf64f {{ dateInZone .Format .CurrentDate \"Asia/Tokyo\" }}"
   }

.. admonition:: 利用者ノート

   垢抜けていないので、より相応しい記法が実はある予感がする。

色指定をする
----------------------------------------------------------------------

`Colors | Oh My Posh <https://ohmyposh.dev/docs/configuration/colors>`__

パレットの概念がある。同じ色を何度も指定するようなテーマを実現するのならば上手く
使いたい。

資料
======================================================================

* `Introduction | Oh My Posh <https://ohmyposh.dev/docs>`__
* `Homebrew <https://brew.sh/>`__

.. _color: https://ohmyposh.dev/docs/configuration/colors
.. _upgrade: https://ohmyposh.dev/docs/installation/upgrade
