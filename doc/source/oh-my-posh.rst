======================================================================
Oh My Posh 利用ノート
======================================================================

  Oh My Posh is a custom prompt engine for any shell that has the ability to
  adjust the prompt string with a function or variable.

.. contents::

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
   :header: タスク,Windows,Ubuntu
   :widths: auto

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
   * :doc:`/windows-terminal`
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

Homebrew についてはノートを割愛する。 Homebrew がなくても Oh My Posh 単品でイン
ストールすることは可能だが、更新やアンインストールの手間を考えると Homebrew の枠
組を採用するほうがいい。

インストール、更新、アンインストールのコマンドはそれぞれ次のとおり：

.. code:: console

   $ brew install jandedobbeleer/oh-my-posh/oh-my-posh
   $ brew update && brew upgrade oh-my-posh
   $ brew uninstall oh-my-posh

インストール手順が完了すると、実行形式 :file:`$(brew --prefix)/bin/oh-my-posh`
とテーマ各種を格納するディレクトリー :file:`$(brew --prefix oh-my-posh)/themes`
が得られる。

Windows
----------------------------------------------------------------------

Oh My Posh 本体を Windows へインストールするには :program:`winget` を用いる。し
たがって Oh My Posh を更新、アンインストールするのにも :program:`winget` を用い
る。

.. code:: doscon

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

.. code:: doscon

   oh-my-posh font install

コンソール上にメニューが現れるので、本文で推奨されている ``Meslo`` を選択、決定
などする。成功するとその旨が表示される。念のため :file:`C:\\Windows\\Fonts` を調
べるといい。

最後に、特殊フォントを必要としない Oh My Posh テーマが用意されていることを心に留
めておく：

  If you are not interested in using a Nerd Font, you will want to use a theme
  which doesn't include any Nerd Font icons. The ``minimal`` themes do not make
  use of Nerd Font icons.

推奨フォントを端末エミュレーターに設定する
----------------------------------------------------------------------

次に Windows Terminal および Visual Studio Code それぞれで端末ウィンドウのフォン
トを指定する。

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

   ところがこれが上手くいかない。各種アイコン文字が豆腐になる。おそらく VS Code
   のクセではないか。

プロンプトを Oh My Posh に割り当てさせる
======================================================================

Oh My Posh にプロンプト文字列を動的に構成させる方法を記す。これはシェルごとの構
成になる。まずは設定ファイルを指定せず、既定の構成を適用する方法を記す。

Bash
----------------------------------------------------------------------

Oh My Posh は UNIX/Linux 系シェルの対応しているものの、私は Bash しか利用しない。

  Add the following to :file:`~/.bashrc` (could be :file:`~/.profile` or
  :file:`~/.bash_profile` depending on your environment):

  .. code:: shell

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

.. code:: pwsh

   oh-my-posh init pwsh | Invoke-Expression

この起動ファイルを編集、保存する。PowerShell セッションが開いていればそこで

.. code:: pwsh

   . $PROFILE

を実行するか、あるいは PowerShell を再起動すれば、端末画面内のプロン
プトの見栄えが変化していることが確認できる。

プロンプトをカスタマイズする
======================================================================

  For your convenience, the existing themes from Oh My Posh have been added to
  version 3, so you can get started even without having to understand the
  theming.

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

.. code:: shell

   eval "$(oh-my-posh init bash --config ~/.omp.json)"

これにより環境変数 :envvar:`POSH_THEME` にパス :file:`$HOME/.omp.json` を割り当
て、環境変数 :envvar:`PROMPT_COMMAND` はその影響を受ける。自作テーマを与えるに
は、既存テーマファイルを複製し、それを好みで編集すればいい。既存テーマの場所は後
述するコツで述べる。

PowerShell
----------------------------------------------------------------------

考え方は Bash の場合と同じだ。スタートアップファイル `$PROFILE` に加えた行を次のように修正する：

.. code:: pwsh

   oh-my-posh init pwsh --config "$env:USERPROFILE\omp.json" | Invoke-Expression

テーマファイルはパス :file:`%USERPROFILE%omp.json` に用意したものとする。

  When using oh-my-posh in Windows and the WSL, know that you can share your
  theme with the WSL by pointing to a theme in your Windows user's home folder.

二重管理を避け、テーマファイルをどちらか一方の環境で管理するのが望ましい。
Windows から WSL にある設定ファイルを指定するならば、WSL Ubuntu がドライブ U に
マウントされているとして次のように書ける：

.. code:: pwsh

   oh-my-posh init pwsh --config "U:\home\USERNAME\PATH\TO\omp.json" | Invoke-Expression

普通は Windows 側に設定ファイルを置いて WSL 側から
:file:`/mnt/c/PATH/TO/omp.json` で参照するのが安定するだろうが、私は WSL の Git
でバージョン管理をしたいのでそれを避けざるを得ない。

テーマファイルを編集する
----------------------------------------------------------------------

以下、JSON 形式でテーマファイルを管理するものとする。

後述するインストール済みテーマを確認するの節の内容に沿って既存のテーマを下見し、
気に入ったものを複製して :envvar:`HOME` などに :file:`omp.json` などの名前で置い
たことを前提として記す。

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

Block
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Block | Oh My Posh <https://ohmyposh.dev/docs/configuration/block>`__

設定オブジェクトは ``blocks`` という配列型属性を一つ含む。その属性をいくつか述べ
る。

属性 ``type`` の値が ``"rprompt"`` の場合、断片はキャレットの右に揃えられる。こ
のようなブロックは高々一つしか許されない。

属性 ``newline`` は値がどちらであっても、``"bash"`` と ``"pwsh"`` の場合にはプロ
ンプトが一行目にあるとき、シェルセッション開始時には、最初のブロックに定義されて
いる改行を表示しない。

属性 ``overflow`` は右寄せブロックに対しては、ブロックが長過ぎて左寄せのブロック
からはみ出る場合、ブロックを壊すか、非表示にするかを指示する。

Segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Segment | Oh My Posh <https://ohmyposh.dev/docs/configuration/segment>`__

ブロックオブジェクトには次の型のオブジェクトからなる配列 ``segments`` を値とする
属性がある。この構成要素の型を Segment と呼ぶ。以下、Segment の属性をいくつか説
明する。

属性 ``type`` には Segment の分類を指示する文字列を与える。私が使いたいものは次
のものだ：

.. csv-table::
   :delim: |
   :header: 値,意味
   :widths: auto

   ``"git"``    | 位置する Git リポジトリーの情報を示す
   ``"node"``   | アクティブ Node.js バージョン示す
   ``"npm"``    | アクティブ NPM バージョンを示す
   ``"path"``   | 現在のパスを示す
   ``"python"`` | アクティブ Python バージョンおよび仮想環境を示す
   ``"root"``   | 現在ユーザーが root である場合に表示する
   ``"shell"``  | 現在のシェルを示す
   ``"time"``   | 現在時刻を書く
   ``"text"``   | 文字列を書く

この値によって Segment の属性 ``properties`` の値オブジェクトの構成が決まること
に注意する。対応する ``type`` を知るには、上記リンク先のページ左側の Segment ツ
リーを見るといい。

属性 ``style`` には次の選択肢がある：

.. csv-table::
   :delim: |
   :header: 値,意味
   :widths: auto

   ``"powerline"`` | 属性 ``powerline_symbol`` の値により segment を分割
   ``"plain"``     | 透過背景に文字しかない単純な描画
   ``"diamond"``   | ``powerline`` の変種で、始点にも対応
   ``"accordion"`` | ``powerline`` の変種で、無効時でもテキストなしで描画

本稿では断りのない限り値 ``"powerline"`` を与えているものとする。

属性 ``foreground``, ``background`` には文字色、背景色をそれぞれ指定する。値の書
式は ``#rrggbb`` 形式で指定するのが無難。透明は ``"transparent"`` とする。より高
級な属性 ``foreground_templates``, ``background_templates`` も存在し得る。

属性 ``template`` がいちばん重要だ。この Segment の内容を与える Template を定義
する。属性 ``templates`` は Segment の Template 文字列を複数行にまたがるようにす
るものだ。属性 ``template_logic`` に基づき、狙いに応じて結果となり得るものが二つ
ある：

.. csv-table::
   :delim: |
   :header: 値,意味
   :widths: auto

   ``"first_match"`` | 配列のうち最初の非空白文字列であるもの
   ``"join"``        | 配列要素すべてを評価し、非空白文字列のものすべてを結合したもの

属性 ``properties`` は適当なオブジェクトの配列を値にとるものであり、Segment の描
画調整に主に用いられる。その属性 ``include_folders`` および ``exclude_folders``
はどの Segment においても考慮される Property の属性であり、パス文字列の配列を値
にとる。特殊な属性についてはおそらく属性 ``type`` により定まるものと考えられる。

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

   .. code:: console

      $ oh-my-posh print primary --config omp-temp.json --shell uni

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

.. code:: console

   $ oh-my-posh toggle python

とする。直後のプロンプト表示から当該 Segment の表示がオフになる。このコマンドを
再び実行すると、Python 情報 Segment 表示がオンに戻る。

  To list the currently toggled segments, use ``oh-my-posh get toggles``.

このコマンドは表示オフ Segment のすべてが一覧できる。

インストール済みテーマを確認する
----------------------------------------------------------------------

PowerShell ならば次のコマンドでインストールされているテーマとそのプレビューを一
覧することが可能だ：

.. code:: pwsh

   Get-PoshThemes

Bash ならばテーマディレクトリーが次のパスにある。演習として PowerShell
``Get-PoshThemes`` 相当の機能を自分で実装してみるのもありだろう。

.. code:: shell

   $HOMEBREW_PREFIX/Cellar/oh-my-posh/$(oh-my-posh version)/themes

オンラインでウェブブラウザーが開いていれば、次のページを確認するのが早いかもしれ
ない： `Themes | Oh My Posh <https://ohmyposh.dev/docs/themes>`__

言語系 Segment の `properties` の内容は似ている
----------------------------------------------------------------------

次の Segment の属性 ``type`` が ``"python"``, ``"ruby"``, ``"node"`` などの場合
には属性 ``properties`` の値オブジェクトにおいて、キー ``home_enabled``,
``display_mode``, ``fetch_version``, その他が共通して有効だ。

.. code:: json

   {
       "type": "xxxx",
       "style": "powerline",
       "powerline_symbol": "xxxx_symbol",
       "template": " {{ .Full }}",
       "properties": {
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

.. code:: json

   {
        "type": "time",
        "style": "plain",
        "invert_powerline": true,
        "foreground": "#ff1493",
        "properties": {
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

