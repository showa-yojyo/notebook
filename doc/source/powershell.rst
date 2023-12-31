======================================================================
PowerShell 利用ノート
======================================================================

PowerShell を試す。基本を固めたら意外な自動化用途を発見したい。

.. contents::
   :depth: 3

PowerShell 利用環境を整える
======================================================================

.. note::

   執筆時の環境は次のとおり：

   :OS: Windows 10 Home, 22H2, 19045.3636
   :PowerShell: PowerShell 7.4.0-rc.1

PowerShell 本体回り
----------------------------------------------------------------------

本体をインストールする
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

最初に PowerShell 最新版を Windows にインストールする。素直に最新リリース版をイ
ンストールするのが安全だが、本稿ではプレビュー版を試す。

コンソールで :program:`winget` を用いてインストールするのが公式推奨手段だ。更新
やアンインストールも本ツールを用いる：

.. code:: console

   winget install --id Microsoft.Powershell.Preview --source winget

.. seealso::

   :doc:`/winget`

プロファイルを用意する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PowerShell コンソールを起動して ``$PROFILE`` の値を見る。このパスが指す
PowerShell ファイルが Bash で言うところの :file:`.bash_profile` に相当する。ひと
まずは空のファイルを作成しておく。Windows Explorer で作成してもよいし、せっかく
だから PowerShell で作成してもよい：

.. code:: pwsh

   New-Item -ItemType File -Path $PROFILE

内容は後述する。

Windows Terminal 構成
----------------------------------------------------------------------

上記のように PowerShell をインストールした後、Windows Terminal で
:menuselection:`Settings --> PowerShell 7 Preview` が現れる。適宜構成する。

項目 :guilabel:`Run this profile as Administrator` を Off と On の二通りで異なる
タブプロファイルを作成しておくのもありかもしれない。演習の時に管理者権限を必要と
するコマンドを用いる場合がある。

.. seealso::

   :doc:`/windows-terminal`

Visual Studio Code 構成
----------------------------------------------------------------------

.. seealso::

   :doc:`vscode/index`

PowerShell 拡張をインストール
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:kbd:`Ctrl` + :kbd:`Shift` + :kbd:`X` を押すなどして拡張サイドバーを展開する。検
索欄に ``powershell`` と入力して Microsoft 謹製の PowerShell 拡張を見つける。
:guilabel:`Install` を押す。

次のような欲しい機能は備えている：

* 構文強調
* 書式整形
* コード片
* IntelliSense
* 変数や関数などへの定義・参照にジャンプ
* アウトライン表示
* 選択コード実行 (:menuselection:`Run Selection`; :kbd:`F8`)
* オンラインヘルプ表示 (:menuselection:`Get Help for Command`; :kbd:`Ctrl` +
  :kbd:`F1`)
* デバッガー

Terminal 周りの設定を追加する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VS Code 基本機能の設定項目を適宜調整する。PowerShell 拡張にインストールにより自
動的に調整されることはなさそうだ。例：

.. code:: json

   {
       "terminal.integrated.profiles.windows": {
           "PowerShell": {
               "path": "${env:PROGRAMFILES}\\PowerShell\\7-preview\\pwsh.exe",
               "args": [
                  "-noexit",
                  "-file",
                  "${env:USERPROFILE}\\Documents\\PowerShell\\Microsoft.PowerShell_profile.ps1"
               ],
               "icon": "terminal-powershell"
           }
       }
   }

Oh My Posh
----------------------------------------------------------------------

.. seealso::

   :doc:`/oh-my-posh`

PowerShell コンソールを起動する
======================================================================

次のいずれかの方法による：

* Windows のスタートメニュー :menuselection:`PowerShell --> PowerShell 7-preview
  (x64)` を押す
* Windows Terminal を起動して :menuselection:`PowerShell 7 Preview` タブを開く
* Visual Studio Code を起動して :menuselection:`View --> Output` を開いて
  :guilabel:`TERMINAL` に上述の手順で設定済みの PowerShell プロファイルの指す項
  目を選択する

他にも方法はある。本ノートでは Windows Terminal を利用する方法を採る。

カスタマイズ
======================================================================

:file:`Microsoft.PowerShell_profile.ps1` を VS Code などで開いて次のように編集し
て保存。PowerShell セッションを起動する：

.. code:: pwsh

   $OMP_CONFIG_PATH = /path/to/oh-my-posh.json
   try{
       oh-my-posh init pwsh --config $OMP_CONFIG_PATH | Invoke-Expression
   }
   catch{
       ;
   }

   Set-PSReadLineOption -EditMode Emacs -HistoryNoDuplicates
   Set-PSReadLineKeyHandler -Key Tab -Function MenuComplete

   Set-Location $env:HOME\Documents\PowerShell

   # aliases
   Set-Alias -Name a -Value Get-Alias
   # ...

手筋集
======================================================================

少しずつ埋めていこう。

バージョンを得る
----------------------------------------------------------------------

``$PSVersionTable`` で PowerShell のバージョン情報を得る

ヘルプ ``Get-Help``
----------------------------------------------------------------------

本名ではなく関数 ``help`` や別名 ``man`` のほうをよくタイプする。これらはページ
送りが付く。

* :samp:`help {word}`
* :samp:`help {word} -Full`
* :samp:`help {word} -Parameter {name}`
* :samp:`help {word} -Parameter *`: これは必修
* :samp:`help {word} -ShowWindow`: これがいちばん便利
* :samp:`help *{word}*`
* :samp:`help {cmdlet} -Examples`
* ``help about_*`` でトピック別ヘルプ記事を閲覧

``Get-Alias``: 別名を知る
----------------------------------------------------------------------

別名の考え方を PowerShell 学習の早い段階で理解すると効率的だろう。``Get-Alias``
は本来は別名を取って正体を返すものだが、そういう使い方はめったにない。

* ``Get-Alias``: 引数なしで全別名一覧出力
* ``Get-Alias -Definition Get-Alias``: 自身の別名を得る
* ``gal -Definition Get-Command, Get-Member``: こちらはあり得る
* ``gal | where {$_.Options -Match "ReadOnly"}``: 組み込み別名を出力
* 別名は覚えないとあまり使わないものだ。
* ``help about_Aliases`` を読め

組み込まれている別名は ``gal`` であることがわかる。``a`` のような短い別名を自分
で付けたい：

* ``Set-Alias -Name a -Value Get-Alias``
* ``Set-Alias -Name np -Value C:\Windows\notepad.exe``

別名には実行ファイルパスや関数を与えることが可能。

``Get-Command``: 命令を得る
----------------------------------------------------------------------

広義の命令を得るために呼び出す。別名 ``gcm`` をタイプ時に採用する。

* ``gcm -ListImported`` 現在利用可能な命令一覧
* :samp:`gcm -Noun {pattern}` E.g. Computer, Host, Item, Location,
  Object, Process, Windows.
* :samp:`gcm -Verb {verb} -Module Microsoft.PowerShell.Utility` E.g. Format,
  Out, Write.
* :samp:`gcm -Name {pattern}`
* :samp:`gcm -Name {pattern} -CommandType Cmdlet, Function, Alias`
* ``gcm -ParameterName ComputerName``
* ``gcm *`` は実行ファイルをも示す
* :samp:`(gcm {cmdlet}).ModuleName` 所属モジュールを示す

上記の他には、型に関する情報を得る複雑な呪文が重要そうだ。

``Show-Command``: 命令一覧およびコマンドライン構築
----------------------------------------------------------------------

``Show-Command`` は専用ウィンドウをコンソールの外に表示して、操作者が命令一覧を
確認したり、指定した命令のコマンドラインを GUI で構築したりするのに用いる。
別名は ``shcm``.

* ``shcm``: :guilabel:`Commands` ウィンドウを表示
* :samp:`shcm -Name {command-name}`: 命令 *command-name* の引数指定ウィンドウを表示
* :samp:`shcm -Name {command-name} -Height {win-height} -Width {win-width} -ErrorPopup`
* :samp:`${command} = shcm -PassThru`: 戻り値を ``Invoke-Expression`` に与えられる
* :samp:`${command} = shcm {command-name} -ErrorPopup`

``Get-Member``: オブジェクトの特徴を得る
----------------------------------------------------------------------

PowerShell の命令出力は UNIX のようなテキスト形式が主体ではなく、オブジェクトで
あることが普通だ。オブジェクトの挙動や性質を知りたいときに ``Get-Member`` を用い
る。

タイプ時には別名 ``gcm`` を採用する。

* :samp:`{object} | gm`
* :samp:`{object} | gm -MemberType Method`
* :samp:`{object} | gm -MemberType Methods`
* :samp:`{object} | gm -MemberType Property`
* :samp:`{object} | gm -MemberType Properties`
* ``"" | gm`` 文字列のメソッドを主に示す

パイプライン
----------------------------------------------------------------------

PowerShell ではパイプに流れるのはテキストではなくオブジェクトだ。まずは ``help
about_Pipelines`` を読め。

* 長いコマンドライン入力は開括弧、引用符、句読点などで改行して続行可。
* コマンドライン入力途中の :kbd:`Shift` + :kbd:`Enter` で改行可。

パイプのフィルターとなる命令
----------------------------------------------------------------------

``Select-Object`` でオブジェクトの性質 (``-Property``) またはコレクションの要素
(``-First``, ``-Last``, ``-Unique``, ``-Skip``, ``-Index``) を選ぶ。横にも縦にも
絞ることが可能。

タイプの便宜を図るために別名 ``select`` が与えられている。

* :samp:`{object} | select -Property {property-name ...}`
* :samp:`{object} | select -Property *`
* :samp:`{object} | select -Property Name, {hash-table}`
* :samp:`{object} | select -ExpandProperty Name`: 文字列配列として得る
* :samp:`{array} | select -First {number}`
* :samp:`{array} | select -Unique` これはソート不要
* :samp:`{array} | select -Index 0, (${array}.count - 1)`

``Where-Object`` は性質値により選ぶ。「どの性質」ではなく「性質がどの値」で選
ぶ。別名は ``where`` または ``?`` が使える。

* :samp:`{object} | where {prop-name} -eq {prop-value}`
* :samp:`{object} | where {prop-name}` とすると *prop-name* が存在するものを抽出
  する
* :samp:`{object} | where {prop-name} -Match {regex}`
* ``$_`` を参照することがよくある。

例は示さぬが ``Where-Object`` の引数にブロックの形を取れる。

コレクションを並び替える
----------------------------------------------------------------------

``Sort-Object`` はオブジェクトの性質値に従うソートを実施する。ソートに使えそうな
性質がない場合には、オブジェクト同士の比較に基づくソートを行う。

ソートを決定づける性質は複数指定することが可能だ。

別名として ``sort`` を使える。

* :samp:`{object} | sort -Property {prop-name ...} -Descending` 降順ソート
* :samp:`sort -Property {hash-table ...}`
* ``-Property`` 自身の記述は省略可
* :samp:`Get-Content -Path {file} | sort -Unique`
* :samp:`Get-Content -Path {file} | Sort-Object {[int]$_}` 数としてソート

``Group-Object`` は SQL で言う ``GROUP BY`` に相当するコレクション順序変更操作を
行い、集計表を出力する。集計をソートにパイプすることがありがちだ。

別名として ``group`` を使える。

* :samp:`{array} | group -Property {prop}`
* :samp:`{array} | group -Property {prop} -NoElement`: ``Group`` 列を省く
* :samp:`{array} | group -Property {prop} -AsHashtable`: ``Name`` と ``Value``
  からなるハッシュ表でデータを得る。

書式整形
----------------------------------------------------------------------

書式整形 (``Get-Command -Verb Format``) コマンドはパイプラインのいちばん右に置か
れるものだ。

``Format-Table`` は表形式。出力オブジェクトの性質と表の列が対応する。別名 ``ft``
を使える。

* :samp:`{array} | ft -Autosize`: 各列の幅をいい感じにする
* :samp:`{array} | ft -GroupBy {prop-name ...}`
* :samp:`{array} | ft -Property {prop-name ...}`
* :samp:`{array} | ft -Wrap`: レコード途中改行を許す

``Format-List`` a.k.a. ``fl`` は出力が縦に長い。

* :samp:`{array} | fl -Property {prop-name ...}`
* :samp:`{array} | fl -Property *`

``Format-Hex`` a.k.a. ``fhx`` という十六進ダンプコマンドが存在する。UNIX で言う
``hexdump -C`` に相当する。

* ``'HOT-B' | fhx``: 484F542D42 を示す
* :samp:`{object} | fhx`
* :samp:`fhx -Path {path}`: ファイル全体を十六進ダンプ
* :samp:`fhx -Path {path} -Count {number} -Offset {offset}`

``Format-Wide`` a.k.a. ``fw`` は単一性質を複数列に亘り出力する。

* :samp:`{object} | Format-Wide -Property {prop}`
* :samp:`{object} | Format-Wide -Property {prop} -Column {number}`

.. todo::

   ビューのカスタマイズ (``help about_Format.ps1xml``) について丸々残っている。

演算子
----------------------------------------------------------------------

PowerShell の演算子はたくさんある。関連ヘルプも複数に及ぶ。まず ``help
about_Operators`` で分類を確認して、関心のある区分の演算子に関するヘルプ記事で詳
細を当たるようにする。

算術演算子
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

算術演算子は四則演算に加えて色々とある。``help about_Arithmetic_Operators`` を読
め。この記事には数値演算に関する事項も述べられている。

単項演算子としては負の符号 ``-`` を付けるものがある。残りはすべて二項演算子だ。

四則演算（と剰余）は他の言語と同様の演算子が用意されている。

ビット演算子は ``-bnot``, ``-band``, ``-bor``, ``-bxor``.
シフト演算子は ``-shl``, ``-shr``.

代入演算子
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

単純な代入を行う演算子および算術演算子と代入が複合した演算子の集合。
``help about_Assignment_Operators`` を読め。

代入演算子は ``=`` だ。この記号を用いる代入仕様の詳細はヘルプを参照しろ。

四則演算（と剰余）の演算子と代入演算子が複合する形の演算子が用意されている。働き
は他の言語と同様。ビット演算子やシフト演算子と代入演算子が複合したものはない。

インクリメント演算子とデクリメント演算子は C/C++ と同様のものがある。前置と後置
が両方ある。

合体演算子 ``??=`` は JavaScript にあるものと同様の演算だ。第一オペランドが
``null`` に評価される場合に限り、第二オペランドの値を第一オペランドに代入する。

比較演算子
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PowerShell には比較演算子が多くある。``help about_Comparison_Operators`` を読め。

ヘルプでは比較演算子の集合を次のように区分している：

Equality
   数学記号で言う等号と不等号に相当するもの。``-eq`` などの基本形に大文字小文字
   の違いを考慮する変種 ``-ieq``, ``-ceq`` がある、という具合だ。
Matching
   ワイルドカードや正規表現を第二オペランドとして取る種の演算子。基本形は
   ``-like`` と ``-match`` で、ここに否定 ``-not`` と大文字小文字考慮 ``-i``,
   ``-c`` が複合したりしなかったりして演算子を形成する。E.g. ``-inotlike``.
Relacement
   ``-replace`` と、これに ``-i`` または ``-c`` が複合する演算子の三種。
   正規表現を第二オペランドに取り、合致する文字列を置換する。
Containment
   ``-contains`` とその複合版はコレクションが値を含むかどうかを判定する。一方、
   ``-in`` とその否定版は値がコレクションに含まれるかどうかを判定する。
Type
   ``-is`` はとその否定版（これだけは ``not`` がケツに付く）は両オペランドが同じ
   型かどうかを判定する。

コツとしては、オペランドの型を意識することか。

論理演算子
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

否定演算子は ``-not`` か ``!`` を用いる。その他の論理演算子は ``-and``, ``-or``,
``-xor`` の三種。なお、``&&`` と ``||`` はパイプに関する別の演算子として存在す
る。``help about_Logical_Operators`` を読め。

キャスト演算子
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

演算子 ``-as`` で型を変換する。``'05/13/20' -as [datetime]`` のように使う。詳し
くは ``help about_Type_Operators`` を読め。

正規表現
----------------------------------------------------------------------

まず ``help about_Regular_Expressions`` に目を通せ。

PowerShell で正規表現が現れる場合、よそ者には非常識に感じられることに大文字小文
字を区別しない。次のようにする：

* ``Select-String`` では ``-CaseSensitive`` スイッチを指定する
* 正規表現を扱う演算子では ``-c`` が付くほうを採用する
* ``switch`` 文では ``-casesensitive`` を指定する

正規表現を含む文字列をエスケープするには次のようにする：
:samp:`[regex]::escape({regex-pattern})`

変数
----------------------------------------------------------------------

まず ``help about_Variables`` を読め。それから次の三つを読め：

* ``help about_Environment_Variables``
* ``help about_Automatic_Variables``
* ``help about_Preference_Variables``

現在利用可能な変数を一覧するには ``Get-Variable *`` が良い。

環境変数
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

環境変数は :samp:`$Env:{name}` で参照する。E.g. ``$Env:USERPROFILE``. コロンをタ
イプした直後にタブ補完をすると、存在する変数一覧が示される。

Windows では、環境変数の照準域が三種類ある：

システム照準域
   システム定義の環境変数に関する照準域。
利用者照準域
   利用者定義の環境変数に関する照準域。ここまでのものは環境変数エディターなどで
   確認可能。
プロセス照準域
   現在プロセス、つまり PowerShell コンソールセッションで利用可能なものを含む。
   親プロセスから引き継いだ変数、System, User 両照準域の変数からなる。

上二つの環境変数を変更するには、次のようにする：

* :samp:`[Environment]::SetEnvironmentVariable({name}, {value}, 'Machine')`
* :samp:`[Environment]::SetEnvironmentVariable({name}, {value})`
* :samp:`[Environment]::SetEnvironmentVariable({name}, '')`: 変数削除

システム照準域に対しては管理者権限も必要だ。

PowerShell が考慮する ``POWERSHELL_`` で始まる固有の環境変数がいくつかあり、上述
のヘルプで確認可能。使いそうなものは：

:envvar:`POWERSHELL_TELEMETRY_OPTOUT`
   余計な情報を提供したくない人向け
:envvar:`POWERSHELL_UPDATECHECK`
   Preview 版か否かで値を使い分けたい？

自動変数
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PowerShell の状態情報を格納する ``$$``, ``$?``, などの特別な変数だ。``$null``,
``$false``, ``$true`` など、純粋な定数も用意されている。

優先変数
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PowerShell の挙動をカスタマイズする変数のうち、有用なものを記す。

``$ConfirmPreference``
   この変数はオプション ``-Confirm`` がある命令・関数に対して機能する。

   PowerShell の命令と変数には危険度という性質がある。この値が高ければ高いほど、
   実行が危険であるとみなされ、実行直前に確認メッセージが表示される仕組みがある。
   その危険度と確認表示の閾値を保持する変数だ。

   安全第一で行くなら ``HIGH`` を、メッセージが邪魔なら ``NONE`` を代入しておく
   といい。
``$DebugPreference``, ``$VerbosePreference``, ``$WarningPreference``
   ``$DebugPreference`` は ``Write-Debug`` が生じたときに PowerShell がどう振る
   舞うかを決定する変数だ。デバッグ時ならば ``STOP`` を指定して実行を停止させ
   る。リリース版では ``SILENTLYCONTINUE`` でかまわないだろう。

   残り二つのそれぞれは、 ``Write-Verbose`` と ``Write-Warning`` がそれぞれ生じ
   たときに PowerShell がどう振る舞うかを決定する変数だ。
``$WhatIfPreference``
   この変数はオプション ``-WhatIf`` がある操作に対して機能する。いわゆる dry run
   を実装する命令に対して、それを有効にするか否かを決定する。

   値は 0 か 1 であり、後者だと対応する操作のすべてで ``-WhatIf`` が自動的にオン
   になる。

反復
----------------------------------------------------------------------

このようなループよりはパイプで済ませるほうが効率的な処理だと考えられる。

``ForEach-Object``, ``foreach``, ``%``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``help about_Foreach`` と ``help ForEach-Object`` を読め。

* :samp:`{collection} | ForEach-Object {statement-list}`
* :samp:`foreach(${item} in ${collection})\\{{statement-list}\\}``

なお、C 言語のような ``for`` ループもある。

``do`` 文
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

他の言語にあるものと同様の構造だ。``help about_Do`` を読め。

* :samp:`do\\{ {statement-list} \\}until({condition})`
* :samp:`do\\{ {statement-list} \\}while({condition})`

``while`` 文
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

他の言語にあるものと同様の構造だ。``help about_While`` を読め。

* :samp:`while({condition})\\{statement-list\\}`

反復制御文
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

以上のループ構造では C 言語のような ``break``, ``continue`` が使え、さらにラベル
指定機能がある。また、構造自体がコマンドなので ``return`` 文が使える。詳しくはそ
れぞれのヘルプ記事を読め。

関数
----------------------------------------------------------------------

* いちばん単純な定義形式は :samp:`function {function-name}\\{ {statements} \\}`
* 引数リストの定義形式は一つではない
* 引数自体を細かく指定することがある
* ``help about_Functions*`` を全部読む
* ``help about_*Parameters`` を全部読む

例外処理
----------------------------------------------------------------------

``help about_Try_Catch_Finally``, ``help_Throw`` を読め。

* ``catch`` 節に対象である例外型を指定するには、角括弧に囲んだ型名を用いる。
* ``catch`` 節に対象である例外型を書かないと、それは catch all を意味する。
* ``catch`` 節では捕捉した例外を参照するのにも ``$_`` を用いる。
* ``catch`` 節では自動変数 ``$Error`` を調べることもある。
* ``throw`` は任意のオブジェクトを取れる。
* ``throw`` 文ではオブジェクトを送出するか、何も明示しないで記す。後者の場合、
  ``ScriptHalted`` というものが送出される。
* PowerShellプロセスを表すオブジェクトを ``throw`` することもある。

.. admonition:: 読者ノート

   PowerShell にはもう一つ、``trap`` というエラー処理の仕組みがある。これは

Providers: 疑似（本物も含む）ファイルシステムドライブ集合
----------------------------------------------------------------------

まずは ``help about_Provides`` を読め。

* ``Get-PSProvider``: その一覧を出力

  * ``Get-PSProvider | ft`` で provider すべてについてそれらの特徴と値の一覧を示
    す。
* ``Get-PSDrive`` a.k.a. ``gdr``: ドライブ一覧だが、ファイルシステムとしてのドラ
  イブよりも抽象度が一段高い。

  * :samp:`Get-PSDrive {drive-letter}`
  * ``gdr -PSProvider FileSystem``: ファイルシステムドライブすべて
  * ``gdr -PSProvider FileSystem | select Name, @{Name="Used"; Expression={$_.Used/1GB}}``
  * ``gdr -PSProvider Registry``
* :samp:`Remove-PSDrive -Name {usb}`

CIM
----------------------------------------------------------------------

   The Common Information Model (CIM) is an extensible, object-oriented data
   model that contains information about different parts of an enterprise.

計算機の情報を得るのに用いる命令として ``Get-CimInstance`` a.k.a. ``gcim`` があ
る。基本的に :samp:`gcim {cim-class} | {filter}` の形で実行する。

* ``gcim CIM_BIOSElement``
* ``gcim CIM_LogicalDisk``
* ``gcim CIM_OperatingSystem | fl``
* ``gcim CIM_Printer``: ``Get-Printer`` と同様か
* ``gcim CIM_Process``: ``Get-Process`` と同様か
* ``gcim CIM_Product | sort -Property Name | ft IdentifyingNumber, Name, LocalPackage -AutoSize``
* ``gcim CIM_PhysicalMemory | fl``
* ``gcim CIM_Service``: ``Get-Service`` と同様か
* ``gcim CIM_VideoController``
* ``gcim Win32_Environment``: 環境変数と値
* ``gcim Win32_NetworkAdapterConfiguration -Filter IPEnabled=$true``
* ``gcim Win32_SystemDriver``
* ``gcim Win32_UserAccount``

``-Class`` の適切な実引数を ``Get-CimClass`` で知ることができる：

.. code:: pwsh

   Get-CimClass -Namespace root/CIMV2 | Sort-Object CimClassName

.. admonition:: 読者ノート

   これを使いこなせるようになれば、PC ショップ店頭の Windows 機でスペックを
   PowerShell で確認できて効率が良い。

動詞
----------------------------------------------------------------------

PowerShell には命令や関数名を動詞で始めるということ、さらにその動詞の集合が内規
で定められている。規則ではないので、不認可動詞を使っても動作しないということはな
い。

認可動詞は ``Group`` という区分で分類されている。

* ``Get-Verb``: 認可されている動詞すべてを示す
* :samp:`Get-Verb {pattern}`: パターンに合致する動詞すべてを示す
* ``Get-Verb | Select-Object Group -Unique``: 有効な ``Group`` を示す
* :samp:`Get-Verb -Group {group}`: *group* に分類される動詞を示す
* :samp:`{commands} | where Verb -notin (Get-Verb).Verb`: 不認可動詞を探す

.. admonition:: 読者ノート

   ``Get-Verb`` の出力表を眺めていると、設計者がプログラミングという概念をどのよ
   うに捉えているのかが垣間見えて面白い。

モジュール
----------------------------------------------------------------------

まずは ``help about_Modules`` を読め。

PowerShell はインストール済みモジュール内の命令を初めて実行した時点で、当該モ
ジュールを自動的にインポートする。

``$env:PSModulePath`` で指定された場所にあるモジュールしか自動インポートされない。
一般の場所にあるモジュールについては ``Import-Module`` 命令が必要。

``$env:PSModulePath -split ';'`` が読みやすい。

自動インポート機能の有効性を切り替える優先変数があり、それは
``$PSModuleAutoloadingPreference`` だ。

モジュールをインストールする手順は、フォルダーごと ``$env:PSModulePath`` のいず
れかの場所に単にコピーすればいい。

* ``Get-Module``: 現在ロード済みのモジュール一覧を示す
* ``Get-Module -ListAvailable``: その裏を示す
* :samp:`Import-Module {path}`: 一般の場所にあるモジュールをインポートする
* ``Import-Module -DisableNameChecking``: 不認可動詞から始まる命令や関数を見逃す

項目 (``Get-Command -Noun Item``)
----------------------------------------------------------------------

UNIX では everything is a file だが、PowerShell では everything is an item なの
だろう。

* :samp:`New-Item -Path {target} -ItemType Directory`
* :samp:`New-Item -Path {target} -ItemType File`
* ``Rename-Item`` は移動不能の名前変更
* :samp:`Rename-Item -Path {source} {target}`
* :samp:`Move-Item -Path {source} -Destination {target} -PassThru`
* :samp:`Copy-Item -Path {source} -Destination {target}`
* :samp:`Copy-Item -Path {source} -Destination {target} -Recurse -Force -Passthru`
* :samp:`Remove-Item {path}`
* :samp:`Remove-Item {path} -Recurse`
* ``Invoke-Item`` は Win32 API で言う ``ShellExecute`` と同等
* ``ii .``: 現在フォルダーを Explorer で開く

* ``Get-ChildItem`` は UNIX の :program:`ls` に相当

  * :samp:`Get-ChildItem -Path {path}`
  * :samp:`Get-ChildItem -Path {path} -Name`
  * :samp:`Get-ChildItem -Path {path} -Force -Recurse` 隠し項目をも出力
  * :samp:`Get-ChildItem -Path * -Include {glob}` マッチのみ出力
  * :samp:`Get-ChildItem -Path * -Exclude {glob}` マッチを除外

項目性質 (``Get-Command -Noun ItemProperty``)
----------------------------------------------------------------------

レジストリー操作で用いることが多い。

* :samp:`Get-ItemProperty -Path {registry-path}`
* :samp:`Get-ItemProperty -Path {registry-path} -Name {key}`
* :samp:`Set-ItemProperty -Path {registry-path} -Name {key} -Value {value}`
* :samp:`New-ItemProperty -Path {registry-path} -Name {key} -PropertyType String -Value {value}`
* :samp:`Rename-ItemProperty -Path {registry-path} -Name {old-key} -NewName {new-key}`
* :samp:`Remove-ItemProperty -Path {registry-path} -Name {key}`

プロセス
----------------------------------------------------------------------

* :samp:`Get-Process` で全項目表示
* :samp:`Get-Process -Name {process}` では :samp:`-Id {pid}` もあり得る（以下同様）
* ``Get-Process | Group-Object -Property Name -NoElement | Where-Object {$_.Count -gt 1}``
* :samp:`Stop-Process -Name {process} -Confirm`
* ``Get-Process | Where-Object -FilterScript {-not $_.Responding} | Stop-Process``
* :samp:`Start-Process -FilePath {executable}` は PATH が通っていれば OK
* :samp:`Start-Process -FilePath {executable} -Wait -WindowStyle Maximized`
* :samp:`Start-Process {process} -Verb RunAs`
* :samp:`Start-Process -FilePath {executable} -ArgumentList {arguments}`

サービス
----------------------------------------------------------------------

サービスを開発するときにあると便利な再起動スクリプトを作成するときの道具になる。

* :samp:`Get-Service -Name {service}`
* :samp:`Get-Service -DisplayName {service}`
* :samp:`Get-Service -Name {service} -RequiredServices`
* :samp:`Get-Service -Name {service} -DependentServices`
* :samp:`Stop-Service -Name {service}`
* :samp:`Start-Service -Name {service}`
* :samp:`Suspend-Service -Name {service}`
* :samp:`Restart-Service -Name {service}`
* TODO: Set-Service

出力先 (``Get-Command -Verb Out``)
----------------------------------------------------------------------

* :samp:`{object} | Out-Null`: 出力を捨てる
* :samp:`{object} | Out-Default`: パイプラインの最後に来る暗黙の出力コマンドと考
  えられる
* :samp:`{object} | Out-Host | -Paging`
* :samp:`{object} | Out-Printer -Name {printer-name}`
* :samp:`{object} | Out-File -Path {output-path}`
* :samp:`{object} | Out-File -Path {output-path} -Width {columns}`
* :samp:`{object} | Out-GridView`: 数ソート不能
* :samp:`{object} | Out-String``: 今のところ用途不明

作業場所 (``Get-Command -Noun Location``)
----------------------------------------------------------------------

* ``Get-Location`` は Bash で言う :command:`pwd` に相当
* ``Set-Location`` は Bash で言う :command:`cd` に相当
* :samp:`Set-Location -Path {path}`
* ``Push-Location``, ``Pop-Location`` はそれぞれ :command:`pushd`,
  :command:`popd` に相当

.. admonition:: 読者ノート

   Bash :command:`dirs` 相当が不明。

キーバインド
----------------------------------------------------------------------

* ``Get-PSReadLineKeyHandler`` または :kbd:`Ctrl` + :kbd:`Alt` + :kbd:`?` で確認
* ``Set-PSReadLineKeyHandler -Key Tab -Function MenuComplete`` で補完を少し楽に
* ``Get-PSReadLineOption`` でオプション設定値を確認
* ``Set-PSReadLineOption -EditMode Emacs`` で Bash に近いキーバインドに変更（プ
  ロファイルに書いておく）

命令履歴
----------------------------------------------------------------------

``help about_History`` を読め。

* ``Get-History`` または ``h`` で Bash で言う :command:`history` 相当を行う
* ``Clear-History`` で自身の実行までの履歴すべてを削除
* :samp:`Clear-History -Count {num} -Newest` 直近 *num* 個を履歴から削除
* :samp:`Clear-History -CommandLine {pattern}` 指定パターン命令を履歴から削除
* :samp:`Clear-History -Id {id ...}`
* :samp:`Clear-History -Id {id} -Count {num}`
* ``Invoke-History`` 過去の命令を再実行する
* :samp:`Invoke-History -Id {id-or-part}`
* :samp:`{first-id}..{last-id} | ForEach \\{Invoke-History -Id $_ \\}`
* :samp:`Get-History -Id {id} -Count {num} | ForEach \\{Invoke-History -Id $_.Id\\}`
* 余裕があれば ``Add-History`` の活用を考える

ファイル入出力
----------------------------------------------------------------------

``Get-Content``, 別名 ``cat`` はファイルの内容をコンソールに出力するのに使える。
ファイルの内容からオブジェクトを作成するのが本来の仕事なのだろう。

* :samp:`cat -Path {path}`
* :samp:`cat -Path {path} -TotalCount {num}`: UNIX で言う :samp:`head -n {num} {path}`
* :samp:`cat -Path {path} -Tail {num}`: UNIX で言う :samp:`tail -n {num} {path}`
* :samp:`cat -Path {path} -Raw`: 単一の文字列として得る
* :samp:`${byteArray} = cat -Path {path} -AsByteStream -Raw`

``Set-Content`` はファイルの中身を上書きする。

* :samp:`Set-Content -Path {path ...} -Value {text}`: 指定したファイルすべてを上書き
* :samp:`Set-Content -Path {path ...} -Value ({command})`

さらに ``Add-Content``, 別名 ``ac`` はファイルの終端から内容を追加する。

* :samp:`ac -Path {path ...} -Value {object}`
* :samp:`cat -Path {source-path} | ac -Path {target-path}`
* :samp:`ac -Path {target-path} -Value (cat -Path {source-path})`

``Clear-Content``, 別名 ``clc`` はファイルの中身を空にする。

出力ストリーム
----------------------------------------------------------------------

``help about_Output_Streams`` を読め。

出力ストリームはログレベルのように種類があり、それぞれに Write 命令が対応する設
計であるようだ：

.. csv-table::
   :delim: |
   :header: 番号,ストリーム,命令
   :widths: auto

   1   | SUCCESS     | ``Write-Output``
   2   | ERROR       | ``Write-Error``
   3   | WARNING     | ``Write-Warning``
   4   | VERBOSE     | ``Write-Verbose``
   5   | DEBUG       | ``Write-Debug``
   6   | INFORMATION | ``Write-Information``
   n/a | PROGRESS    | ``Write-Progress``

``Write-Output`` は必ずしも画面に表示するわけではない。

リダイレクト
----------------------------------------------------------------------

``help about_Redirection`` を読め。

* ``Out-File`` でファイルに出力
* ``Tee-Object`` でファイルとパイプラインの両方に出力
* 演算子によるリダイレクト

  * :samp:`{n}>` でストリーム *n* をファイルに書き込む
  * :samp:`{n}>>` でストリーム *n* をファイル末尾に書き込む
  * :samp:`{n}>&1` でストリーム *n* を成功ストリームにつなぐ

    * E.g. ``2>&1`` でエラー出力を成功出力にリダイレクト

  * ``*>`` でストリームすべてをファイルにリダイレクト

クリップボード
----------------------------------------------------------------------

``Get-Clipboard`` でクリップボードからデータを受け取る。WSL のシェル環境で利用す
ることになる：

.. code:: bash

   alias getclip='/path/to/pwsh.exe -noprofile -command Get-Clipboard'

``Set-Clipboard`` も存在するが、WSL では :program:`iconv` をインストールしている
ので敢えて使わなくていい：

.. code:: bash

   alias putclip='iconv -f utf-8 -t utf-16le | clip.exe'

``Select-String``: 文字列検索
----------------------------------------------------------------------

UNIX の :program:`grep` のようなことをするには ``Select-String`` を用いる。

* :samp:`{text} | Select-String -Pattern {literal} -CaseSensitive -SimpleMatch`: :program:`fgrep` 相当
* :samp:`Select-String -Path {path ...} -Pattern {regex}`: 典型的 :program:`grep`
* :samp:`Get-WinEvent {args} | Select-String -InputObject {$_.message} -Pattern {regex}`
* :samp:`Get-ChildItem -Path {path ...} -Recurse | Select-String -Pattern {regex} -CaseSensitive`: ``grep -R`` 相当
* :samp:`{text} | Select-String -Pattern {regex ...} -NotMatch`: ``grep -v`` 相当
* :samp:`{text} | Select-String -Pattern {regex ...} -Context 2, 3`: ``grep -B 2 -A 3`` 相当

テキストベースデータ変換
----------------------------------------------------------------------

PowerShell では CSV や JSON データなどを追加的モジュールのインポートなしに処理可
能だ。

CSV
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: ``ConvertFrom-Csv``

* :samp:`{object} | ConvertFrom-Csv`
* :samp:`ConvertFrom-Csv -InputObject {object} -Delimiter '{character}'`
* :samp:`{object} | ConvertFrom-Csv -Header {header}` ここで *header* は列名から
  なる配列

.. rubric:: ``ConvertTo-Csv``

* :samp:`{object} | ConvertTo-Csv`
* :samp:`{object} | ConvertTo-Csv -Delimiter {character}`
* :samp:`{object} | ConvertTo-Csv -NoTypeInformation` 高速化するわけではなさそうだ
* :samp:`ConvertTo-Csv -InputObject {object} -Delimiter {character} -NoTypeInformation`
* :samp:`{object} | ConvertTo-Csv -QuoteFields {field-name ...}`
* :samp:`{object} | ConvertTo-Csv -UseQuotes AsNeeded` 一貫性を気にしないのなら

.. rubric:: ``Export-Csv`` a.k.a. ``epcsv``

* :samp:`{object} | Export-Csv -Path {output-path} -NoTypeInformation`
* :samp:`{object} | Export-Csv -Path {output-path} -NoTypeInformation -Append`
* オプション ``-QuoteFields``, ``-UseQuotes`` が使える

.. rubric:: ``Import-Csv`` a.k.a. ``ipcsv``

* :samp:`${csv} = Import-Csv -Path {input-path}`
* :samp:`Import-Csv -Path {input-path} -Delimiter {character}`
* :samp:`Import-Csv -Path {input-path} -Header {header}`
* :samp:`Import-Csv -Path {input-path} -Header {column-name ...}`

JSON
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: ``ConvertFrom-Json``

* :samp:`Get-Content -Raw {input-path} | ConvertFrom-Json`
* :samp:`{json} | ConvertFrom-Json -AsHashtable`
* :samp:`{json} | ConvertFrom-Json -NoEnumerate`

.. rubric:: ``ConvertTo-Json``

* :samp:`{object} | ConvertTo-Json`
* :samp:`{object} | ConvertTo-Json -AsArray`
* :samp:`{object} | ConvertTo-Json -Compress`
* ``Get-Date | Select-Object -Property * | ConvertTo-Json``

XML
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: ``ConvertTo-Xml``

* :samp:`{object} | ConvertTo-Xml` パイプ用
* :samp:`{object} | ConvertTo-Xml -As String` テキストダンプ用
* :samp:`{object} | ConvertTo-Xml -As "Document" -Depth {num}`

.. rubric:: ``Export-Clixml``

``Export-Clixml`` はオブジェクトの CommonLanguage Infrastructure XML に基づく表
現をファイルに保存する。疑似 XML と考えて差し支えなさそうだ。

* :samp:`{object} | Export-Clixml -Path {output-path}`
* :samp:`${Credential} | Export-Clixml {output-path}`

.. rubric:: ``Import-Clixml``

* :samp:`${Clixml} = Import-Clixml -Path {output-path}`
* :samp:`${Credential} = Import-Clixml {input-path}`

便利な命令
----------------------------------------------------------------------

* ``Get-Date``: 日付を得る

  * ``Get-Date -UFormat "%Y-%m-%d (%A) %T"``: 時計
  * ``Get-Date -Format o | foreach { $_ -replace ":", "." }``: タイムスタンプ
* ``Get-Random``: 乱数を得たり選んだりする

  * ``Get-Random -Minimum 1 -Maximum 7``: サイコロ
  * ``1..6 | Get-Random``: サイコロ
  * ``Get-Random -Minimum 10.7 -Maximum 20.93``: 浮動小数点数も OK
  * ``1, 2, 3, 5, 8, 13 | Get-Random -Count 3``
  * ``1, 2, 3, 5, 8, 13 | Get-Random -Shuffle``
* ``Show-Markdown``: Markdown ファイルをコンソール内に描画するかも
* ``Invoke-RestMethod``: RSS, ATOM を含む XML や JSON を処理するのに使える

  * :samp:`Invoke-RestMethod https://www.youtube.com/feeds/videos.xml?channel_id={id} | Out-GridView`
  * :samp:`Invoke-RestMethod https://blogs.msdn.microsoft.com/powershell/feed/ | Format-Table -Property {prop ...}`
  * :samp:`Invoke-RestMethod -Method 'Post' -Uri {url} -Credential {cred} -Body {body} -OutFile {output-path}`
  * :samp:`${resonse} = Invoke-RestMethod -Uri {url} -Method Post -Form {form}`

* ``Invoke-WebRequest``

  * :samp:`${response} = Invoke-WebRequest -uri {url}`: 得られるオブジェクトの
    属性が重要

GUI
----------------------------------------------------------------------

:samp:`Add-Type -AssemblyName {assembly}` で .NET Framework クラスを利用可能にな
る。これを利用して GUI を実現することが可能だ。

.. code:: pwsh

   Add-Type -AssemblyName System.Windows.Forms
   Add-Type -AssemblyName System.Drawing

   $form = New-Object Windows.Forms.Form -Property @{
       StartPosition = [Windows.Forms.FormStartPosition]::CenterScreen
       Size          = New-Object Drawing.Size 243, 260
       Text          = 'Hello world'
       Topmost       = $true
   }

   # ...

   $result = $form.ShowDialog()

配列とハッシュ表
----------------------------------------------------------------------

``help about_Arrays`` と ``help about_Hash_Tables`` を読め。Python や JavaScript
の文法と似ている気がするから急所だけ覚えればいい。生成方法だけ覚えておき、要素参
照やメソッドは補完機能を使えばやっているうちに覚える。たぶん .NET Framework のイ
ンターフェイスと同一だろう。

.. rubric:: 配列の生成方法

* ``$A = 22,5,10,8,12,9,80``: 要素すべてを指定して生成する例
* ``$B = ,7``: 単一要素を指定して生成する例
* ``$C = 5..8``: Bash 風
* ``[int32[]]$ia = 1500,2230,3350,4000``: 明示的に型を指定する例
* ``$a = @("Hello World")``: 単一要素を指定して生成する例
* ``$b = @()``: 空配列を生成する例

.. rubric:: ハッシュ表の生成方法

* ``$hash = @{}``: 空ハッシュ表を生成する
* ``$hash = @{ Number = 1; Shape = "Square"; Color = "Blue"}``: 中身を指定して生
  成する例

PowerShell Gallery
======================================================================

.. todo:: 便利なモジュール、スクリプトを発見できたら記す。

情報源
======================================================================

`PowerShell Documentation - PowerShell <https://learn.microsoft.com/en-us/powershell/>`__
   本ノートではこの文書群を PowerShell の基本情報源であるとする。

   PowerShell をインストールしたら `PowerShell 101
   <https://learn.microsoft.com/en-us/powershell/scripting/learn/ps101/00-introduction?view=powershell-7.3>`__
   から読んでもいいかもしれない。

Microsoft Learn
   PowerShell を習得するための訓練がいくつかある。アカウントを持っていたらログイ
   ンしてからページを閲覧して経験値を上げるのがよい。

   * `Get started with Windows PowerShell <https://learn.microsoft.com/en-us/training/paths/get-started-windows-powershell/>`__
   * `Work with PowerShell providers and PowerShell drives in Windows PowerShell <https://learn.microsoft.com/en-us/training/paths/work-powershell-providers-powershell-drives-windows-powershell/>`__
   * `Create and manage background jobs and scheduled jobs in Windows PowerShell <https://learn.microsoft.com/en-us/training/paths/create-manage-background-jobs-scheduled-windows-powershell/>`__
   * `Use variables, arrays, and hash tables in Windows PowerShell scripts <https://learn.microsoft.com/en-us/training/paths/use-variables-arrays-hash-tables-windows-powershell/>`__
   * `Work with the Windows PowerShell pipeline <https://learn.microsoft.com/en-us/training/paths/work-windows-powershell-pipeline/>`__
   * `Create and modify scripts by using Windows PowerShell <https://learn.microsoft.com/en-us/training/paths/create-modify-script-use-windows-powershell/>`__

   初級者向けの内容を見つけるのが難しかった。コマンドラインを実行するとエラーに
   なるものが複数あり、それぞれ原因がバラバラで解決するのに手間だった。

   * `Sample scripts for system administration - PowerShell <https://learn.microsoft.com/en-us/powershell/scripting/samples/sample-scripts-for-administration?view=powershell-7.3>`__

`Highest scored 'powershell' questions - Stack Overflow <https://stackoverflow.com/questions/tagged/powershell?tab=Votes>`__
   評価の高い質問を順に読んでいくといいことがありそうだ。
`command line - Copy to clipboard using Bash for Windows - Stack Overflow <https://stackoverflow.com/questions/43144008/copy-to-clipboard-using-bash-for-windows/>`__
   PowerShell 調査のついでに発見。
`GitHub - dlwyatt/WinFormsExampleUpdates: Updates to make TechNet PowerShell Windows Forms examples compatible with PowerShell 3.0 and later <https://github.com/dlwyatt/WinFormsExampleUpdates>`__
   GUI デモスクリプト四つ。
