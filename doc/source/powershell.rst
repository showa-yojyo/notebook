======================================================================
PowerShell 利用ノート
======================================================================

PowerShell を試す。意外な自動化用途を発見したい。

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

   Set-PSReadLineOption -EditMode Emacs
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

``Format-List`` は出力が縦に長い。

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

反復
----------------------------------------------------------------------

このようなループよりはパイプで済ませるほうが効率的な処理だと考えられる。

``ForEach-Object``, ``foreach``, ``%``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``help about_Foreach`` と ``help ForEach-Object`` を読め。

* :samp:`{collection} | ForEach-Object {statement-list}`
* :samp:`foreach(${item} in ${collection})\{{statement-list}\}``

なお、C 言語のような ``for`` ループもある。

``do`` 文
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

他の言語にあるものと同様の構造だ。``help about_Do`` を読め。

* :samp:`do\{ {statement-list} \}until({condition})``
* :samp:`do\{ {statement-list} \}while({condition})``

``while`` 文
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

他の言語にあるものと同様の構造だ。``help about_While`` を読め。

* :samp:`while({condition})\{statement-list\}`

反復制御文
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

以上のループ構造では C 言語のような ``break``, ``continue`` が使え、さらにラベル
指定機能がある。また、構造自体がコマンドなので ``return`` 文が使える。詳しくはそ
れぞれのヘルプ記事を読め。

Providers: よくわからない概念
----------------------------------------------------------------------

まずは ``help about_Provides`` を読め。

* ``Get-PSProvider``: その一覧を出力
* ``Get-PSDrive``: ドライブ一覧だが、ファイルシステムとしてのドライブよりも抽象
  度が一段高い。
* :samp:`Get-PSDrive {drive-letter}`
* ``Get-PSDrive -PSProvider FileSystem``
* ``Get-PSDrive -PSProvider Registry``
* :samp:`Remove-PSDrive -Name {usb}`

``Get-CimInstance``
----------------------------------------------------------------------

* ``Get-CimInstance Win32_BIOS``
* ``Get-CimInstance Win32_Environment`` 環境変数と値
* ``Get-CimInstance Win32_LogicalDisk``
* ``Get-CimInstance Win32_NetworkAdapterConfiguration -Filter IPEnabled=$true``
* ``Get-CimInstance Win32_OperatingSystem``
* ``Get-CimInstance Win32_Printer``
* ``Get-CimInstance Win32_Process`` は ``Get-Process`` と同様か
* ``Get-CimInstance Win32_Service`` は ``Get-Service`` と同様か
* ``Get-CimInstance Win32_SystemDriver``
* ``Get-CimInstance Win32_UserAccount``
* ``Get-CimInstance Win32_VideoController``
* ``Get-CimInstance Win32_OperatingSystem | Format-List *``

``-Class`` の適切な実引数を ``Get-CimClass`` で知ることができる：

.. code:: pwsh

   Get-CimClass -Namespace root/CIMV2 | Sort-Object CimClassName

関数
----------------------------------------------------------------------

* いちばん単純な定義形式は :samp:`function {function-name}\{{statements}\}`
* 引数リストの定義形式は一つではない
* 引数自体を細かく指定することがある
* ``help about_Functions*`` を全部読む
* ``help about_*Parameters`` を全部読む

モジュール
----------------------------------------------------------------------

* ``Import-Module``
* ``$env:PSModulePath``
* ``$env:PSModulePath -split ';'`` が読みやすい

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

* ``Get-ChildItem`` は UNIX の :program:`ls` に相当

  * :samp:`Get-ChildItem -Path {path}`
  * :samp:`Get-ChildItem -Path {path} -Name`
  * :samp:`Get-ChildItem -Path {path} -Force -Recurse` 隠し項目をも出力
  * :samp:`Get-ChildItem -Path * -Include {glob}` マッチのみ出力
  * :samp:`Get-ChildItem -Path * -Exclude {glob}` マッチを除外

Item Properties (``Get-Command -Noun ItemProperty``)
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

.. code:: pwsh

   Get-Process | Group-Object -Property Name -NoElement | Where-Object {$_.Count -gt 1}

* :samp:`Stop-Process -Name {process} -Confirm`
* ``Get-Process | Where-Object -FilterScript {-not $_.Responding} | Stop-Process``
* :samp:`Start-Process -FilePath {executable}` は PATH が通っていれば OK
* :samp:`Start-Process -FilePath {executable} -Wait -WindowStyle Maximized`
* :samp:`Start-Process {process} -Verb RunAs`
* :samp:`Start-Process -FilePath {executable} -ArgumentList {arguments}`

サービス
----------------------------------------------------------------------

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

* :samp:`{object} | Out-Null` 出力を捨てる
* :samp:`{object} | Out-Default` パイプラインの最後に来る暗黙の出力コマンドと考えられる
* :samp:`{object} | Out-Host | -Paging`
* :samp:`{object} | Out-Printer -Name {printer-name}`
* :samp:`{object} | Out-File -Path {output-path}`
* :samp:`{object} | Out-File -Path {output-path} -Width {columns}`
* :samp:`{object} | Out-GridView`: 数ソート不能
* :samp:`{object} | Out-String`` 今のところ用途不明

位置 (``Get-Command -Noun Location``)
----------------------------------------------------------------------

* ``Get-Location`` は Bash で言う :command:`pwd` に相当
* ``Set-Location`` は Bash で言う :command:`cd` に相当
* :samp:`Set-Location -Path {path}`
* ``Push-Location``, ``Pop-Location`` はそれぞれ :command:`pushd`,
  :command:`popd` に相当

Bash :command:`dirs` 相当が不明。

キーバインド
----------------------------------------------------------------------

* ``Get-PSReadLineKeyHandler`` または :kbd:`Ctrl` + :kbd:`Alt` + :kbd:`?` で確認
* ``Get-PSReadLineOption`` でオプション設定値を確認
* ``Set-PSReadLineOption -EditMode Emacs`` で Bash に近いキーバインドに変更
  （プロファイルに書いておく）

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
* :samp:`{first-id}..{last-id} | ForEach \{Invoke-History -Id $_ \}`
* :samp:`Get-History -Id {id} -Count {num} | ForEach {Invoke-History -Id $_.Id}`
* 余裕があれば ``Add-History`` の活用を考える

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

TBW
----------------------------------------------------------------------

* ``PS`` から始まる変数（と値）を ``Get-Variable | Where-Object { $_.Name
  -like 'PS*' }`` で確認できる。

* 環境変数は :samp:`$env:{name}` で参照する
* ``Find-Module`` と ``Install-Module`` にはまともなヘルプがない
* ``Invoke-Command``
* ``Get-Verb``

  * PowerShell にはコマンド名を構成する動詞を限定したいという思想がある。
  * ``Get-Verb | Sort-Object -Property Verb``

.. todo::

   * フィルター残り

     * ``Get-Process`` や ``Get-WinEvent`` をテキストデータの源として利用する。
   * 文字列 String
   * 正規表現
   * Session
   * Import
   * Export
   * JSON, CSV, XML
   * ``Get-Content``
   * ``Get-Random``
   * ``Invoke-RestMethod``

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
