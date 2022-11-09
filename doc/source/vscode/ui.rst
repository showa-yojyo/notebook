======================================================================
ユーザーインターフェイス
======================================================================

VS Code の UI について記す。メインウィンドウの構成は本家 Visual Studio と同様で、
大まかに言えば、左側にワークスペースで扱うファイルとフォルダーを表示する Explorer,
その右側に開いたファイルの内容を表示する Editor という配置を採用している。

.. attention::

   :doc:`./index` 冒頭の前提条件に留意すること。

.. contents::

基本レイアウト
======================================================================

まずは `Visual Studio Code User Interface <https://code.visualstudio.com/docs/getstarted/userinterface>`__
の最初の画像に用いられている用語を頭に叩き込むこと。VS Code の画面全体を次の五つ
に区分して理解する：

Activity Bar
    左端にある柱状の領域。アイコンをクリックしてビューを切り替えられるほか、Git
    が有効な場合に保留中のファイル数など、現況に応じてアイコン右下にバッヂが表示
    されることもある。
(Primary) Side Bar
    Activity Bar のすぐ右側の縦長領域。:guilabel:`EXPLORER` などのビュー各種を搭
    載する。
Editor/Editor Groups
    メイン領域。縦にも横にもいくつでも Editor を並べられる。各 Editor Group に
    Editor が一つ以上含まれ、各グループでタブをクリックするなどして現在の Editor
    を切り替える。開いているファイルは、Editor 領域の上部にタブで表示される。
Panels
    初期設定かつ表示されていれば Editor/Editor Groups 領域の下にある領域。
    出力、デバッグ情報、エラーや警告、端末など、さまざまなパネルを表示できる。
    テキスト編集領域をなるべく縦方向に確保したければ非表示にしたり、メインウィン
    ドウ右側に移動したりできる。
Status Bar
    床下にある領域。ワークスペースや現在の Editor に関する情報各種を表示する。

VS Code を開始するたびに、上記 UI 要素は前回終了時と同じ状態で配置される。レイア
ウトだけでなく、開いていたフォルダー、ファイルも Editor 領域に復元される。

.. admonition:: 利用者ノート

   各パーツに対して表示・非表示の切り替えコマンドが存在する。特に、Activity Bar,
   Side Bar, Panel のそれのショートカットキーがもし設定されていれば、覚えておく
   と編集をより快適に編集できる。

Editor Groups の配置
======================================================================

既存の Editor Group の横に別の Editor Group を横または縦に追加的に開くことが可能
だ。方法は複数ある：

* :kbd:`Ctrl` + :kbd:`\\` を押して、アクティブ Editor を二分割する。
* :guilabel:`EXPLORER` ビューで対象ファイルを :kbd:`Alt` キーを押しながらクリッ
  クする。
* :guilabel:`EXPLORER` ビューで対象ファイルにフォーカスを与えて次のいずれかを行
  う：

  * :kbd:`Ctrl` + :kbd:`Enter` を押す。
  * コンテキストメニューの :menuselection:`Open to the Side` を選択する。

* Editor 右上のアイコン :guilabel:`Split Editor Right` を押す。
* ファイルまたは Editor タブを Editor 領域に（どこでもいい）ドラッグ＆ドロップす
  る。
* Quick Open 一覧からファイルを選択するときに :kbd:`Ctrl` + :kbd:`Enter` を押
  す。

他のファイルを開くときはいつでも、アクティブになっている Editor がその内容を表示
する。例えば Editor が二つが並んでいて、ファイル ``foo.cs`` を右側の Editor で開
きたい場合、そちら側がアクティブであることを確実にしてから開くことだ。

初期設定では Editor はアクティブ Editor の右側に開かれる。設定項目
``workbench.editor.openSideBySideDirection`` の値がこの動作を変更する。
新しい Editor をアクティブ Editor の下に開くように設定することも可能だ：

.. code:: json

   {
       "workbench.editor.openSideBySideDirection": "down"
   }

複数の Editor Groups を開いている場合、:kbd:`Ctrl` キーを押しながら :kbd:`1`,
:kbd:`2`, :kbd:`3`, ... を押すことで Editor を素早く切り替えることができる。

.. todo::

   この事項は :doc:`./basics` で述べる程度に基本的である可能性が高い。本節の移転
   を検討する。

ミニマップ
======================================================================

ミニマップは、ソースコードの概要を表現するものだ。ミニマップは Editor の右側に表
示される。陰影のついた部分をクリックまたはドラッグすることで、当該部分にジャンプ
できる。

設定ファイル :file:`settings.json` でミニマップ表示位置を左側に変更したり、完全
に無効にすることも可能だ：

.. code:: json

   {
       "editor.minimap.side": "left",
       "editor.minimap.enabled": false
   }

パンクズ
======================================================================

Editor それぞれの上部にパンクズと呼ばれるナビゲーションバーがある。これは現在の
場所を表示し、フォルダー、ファイル、シンボル間を素早く移動することができる。

パンクズは次のように、現在キャレットがあるシンボルをルートから階層的に表現したパ
スのように表現している：

.. code:: text

   path > to > file > path > to > symbol

カスタマイズについては :doc:`./navigation` 内パンクズの節を参照。

EXPLORER
======================================================================

:guilabel:`EXPLORER` はプロジェクト内のファイルおよびフォルダーすべてを管理する
のに用いる。 VS Code は本家のようにワークスペースやプロジェクトを定義するファイ
ルがあるわけではなく、ファイルとフォルダーに基づく。

VS Code でフォルダーを開くと :guilabel:`EXPLORER` にその中身がツリーコントロー
ルで再帰的に表示される。ここでいろいろなことができる：

* ファイルおよびフォルダーの作成、削除、名前を変更する
* ドラッグ＆ドロップでファイルおよびフォルダを移動する

項目上のコンテキストメニューで可能な操作を確認できる。

VS Code は外部ツール、特にコマンドラインツールと非常によく連動している。
VS Code で現在開いているフォルダーのコンテキストでコマンドラインツールを実行したければ、
フォルダーを右クリックして :menuselection:`Open in Command Prompt` を選択する。

また、項目を右クリックして、:menuselection:`Reveal in Explorer` を選択すると、Windows
Explorer でその場所に移動することができる。

既定の設定では、VS Code は :guilabel:`EXPLORER` からいくつかのフォルダーを除外す
る。設定項目 ``files.exclude`` を使用して、:guilabel:`EXPLORER` からファイルや
フォルダーを隠すための規則を設定する（次の設定は既定値）：

.. code:: json

   {
       "files.exclude": {
           "**/.git": true,
           "**/.svn": true,
           "**/.hg": true,
           "**/CVS": true,
           "**/.DS_Store": true,
           "**/Thumbs.db": true
       }
   }

複数選択
----------------------------------------------------------------------

:guilabel:`EXPLORER` や :guilabel:`OPEN EDITORS` ビューで複数の項目を選択するこ
とができ、それらに対してコマンドを実行できる：

* :kbd:`Ctrl` キーを押しながらマウスクリックで個別ファイル選択
* :kbd:`Shift` キーを押しながらマウスクリックで範囲選択

特に、項目を二つ選択した場合、コンテキストメニューのコマンド
:menuselection:`Select for Compare` を使用して、ファイル二つの差分をすぐに見るこ
とができる。

ツリーコントロール
----------------------------------------------------------------------

わかりにくいが、:guilabel:`EXPLORER` のツリーコントロールには検索とフィルターが
混ざったようなナビゲーション機能がある。

ファイルをフィルターする：
:guilabel:`EXPLORER` にフォーカスがある状態で、:kbd:`Ctrl` + :kbd:`F` キーを押し
てツリーの検索コントロールを開き、一致させたいファイル名の一部を入力する。
すると :guilabel:`EXPLORER` 右上に、入力した内容を表示する検索コントロールが表示され、
一致するファイル名がハイライト表示される。

ここで :guilabel:`Filter` アイコンをクリックすると、モードがハイライトとフィル
ターの間を切り替わる。 :kbd:`↓` キーと :kbd:`↑` キーを押す度にマッチした要素間を
ジャンプする。

このナビゲーション機能は、VS Code のすべてのツリーコントロールで利用可能だ。

OUTLINE
----------------------------------------------------------------------

:guilabel:`OUTLINE` ビューは :guilabel:`EXPLORER` の下部にある独立したセクションだ。
展開すると、現在アクティブな Editor の内容を表現する木構造が表示される。

:guilabel:`OUTLINE` ビューには、さまざまな :menuselection:`Sort By` コマンドを実行でき、
オプションでカーソル追跡、タイプ別フィルターが操作できる。

.. todo::

   後者二つの機能である :menuselection:`Follow Cursor` と
   :menuselection:`Filter on Type` がまったく不明。

また、入力ボックスがあり、入力中にシンボルを検索したり、フィルターしたりすることができる。
エラーや警告も :guilabel:`OUTLINE` ビューに表示され、問題の場所を一目で確認することができる。

木構造は Editor に対する言語モード拡張機能が持っている情報に依存する。
例えば組み込みの Markdown モードは文書のヘッダー階層を返す。

:guilabel:`OUTLINE` には次のような設定項目があり、アイコンの有効無効、エラーと警
告の表示の制御が可能だ。

``outline.icons``
  項目先頭のアイコンを描くかどうか
``outline.problems.enabled``
  項目にエラーと警告を示すかどうか
``outline.problems.badges``
  エラーと警告に対してバッヂを使うかどうか
``outline.problems.colors``
  エラーと警告に対して色を使うかどうか

OPEN EDITORS
======================================================================

:guilabel:`EXPLORER` の上部には :guilabel:`OPEN EDITORS` と表示されたビューがあ
る。アクティブなファイルまたはプレビューの一覧だ。これらは最近 VS Code で開いた
作業中のファイルだ。例えば、次のような場合、:guilabel:`OPEN EDITORS` の一覧に
ファイルが現れる：

* ファイルに変更を加える
* ファイルのヘッダをダブルクリックする
* エクスプローラでファイルをダブルクリックする
* 現在のフォルダにないファイルを開く

このビューの項目をクリックすると、そのファイルを内容とする Editor がアクティブに
なる。

作業が完了したら、:guilabel:`OPEN EDITORS` からファイルを個別に削除するか、次の
いずれかのコマンドを実行してすべてのファイルを削除する：

* :guilabel:`View: Close All Editors`
* :guilabel:`View: Close All Editors in Group`

このビューを表示したくない場合は設定を編集する：

.. code:: json

   {
       "explorer.openEditors.visible": 0
   }

ビュー
======================================================================

VS Code には :guilabel:`EXPLORER` 以外にも次のようなビューがある：

:guilabel:`SEARCH`
  ワークスペース全体の検索と置換処理
:guilabel:`SOURCE CONTROL`
  Git 操作
:guilabel:`RUN AND DEBUG`
  変数、コールスタック、ブレイクポイントなどのデバッグ
:guilabel:`EXTENSIONS`
  VS Code 拡張機能に対するインストールと構成

その他、拡張機能が独自のビューを与えることもある。

コマンド :guilabel:`View: Open View` を実行すればどのビューでも開ける。

メインビューの中からビューの表示状態を切り替えたり、ドラッグ＆ドロップで並び替え
たりすることが可能だ。

Activity Bar
----------------------------------------------------------------------

ビュー左側にある Activity Bar にあるアイコンをクリックするとビューをすばやく切り
替えられる。また、Activity Bar 上でアイコンをドラッグ＆ドロップして並び替えたり、
アイコンのコンテキストメニューからビューを削除することも可能だ。

Activity Bar 自身を :menuselection:`Hide from Activity Bar` で非表示にすることも可能だ。

.. admonition:: 利用者ノート

   Activity Bar を完全に隠蔽して、主要なビュー表示を切り替えるのにショートカット
   キーを押すのが通好みだろう。

.. csv-table::
   :delim: @
   :header: キーバインド,ビュー

   :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`D` @ :guilabel:`RUN AND DEBUG`
   :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`E` @ :guilabel:`EXPLORER`
   :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`F` @ :guilabel:`SEARCH`
   :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`G` @ :guilabel:`SOURCE CONTROL`
   :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`X` @ :guilabel:`EXTENSIONS`

コマンドパレット
======================================================================

VS Code で最も重要なキーバインドは、:kbd:`Ctrl` + :kbd:`Shift` + :kbd:`P` だ。
これはコマンド :guilabel:`Show All Commands` を実行するショートカットであり、
この操作により画面上部に現れる入力欄をコマンドパレットと呼ぶ。
ここから VS Code のコマンドすべてを一覧したり選択することが可能であり、定義があ
ればコマンドを呼び出すキーバインドも表示される。

.. todo::

   コマンドパレットは掛け値なしに重要な要素なので、VS Code 利用ノートの可能な限
   り早い位置に移動する。

コマンドパレットは次のコマンドなどでも入力を受け付けるために用いられる：

.. csv-table::
   :delim: @
   :header: キーバインド,コマンド,操作

   :kbd:`Ctrl` + :kbd:`P` @ :guilabel:`Go to File...` @ 名前を指定してファイルへジャンプ
   :kbd:`Ctrl` + :kbd:`Tab` @ :guilabel:`View: Quick Open Previous Recently Used Editor in Group` @ 現在の Editor Group 内で直前のものにジャンプ
   :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`P` @ `Show All Commands` @ 上述
   :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`O` @ `Go to Symbol in Editor` @ 指定シンボルへジャンプ
   :kbd:`Ctrl` + :kbd:`G` @ :kbd:`Go to Line/Column...` @ 指定行へジャンプ

入力欄先頭に ``?`` を入力すると、ここから実行できるコマンド一覧が出る。これは別
の機会に調べる。

タブ
======================================================================

Editor Group のタブについて記す。Editor にはタブが一対一対応する。タブをクリック
すると対応する Editor がアクティブになる。タブを用いれば Editor 間をすばやく移動
できる。タブをドラッグ＆ドロップして順序を変更することができる。Editor Group を
またぐ移動さえ可能だ。

Editor Group 右上の詳細ボタンメニューから :menuselection:`Show Opened Editors`
を選択すると、当グループに含まれる Editor すべての一覧が現れる。

タブを使いたくない場合は次のように設定する：

.. code:: json

   {
       "workbench.editor.showTabs": false
   }

タブ順序
----------------------------------------------------------------------

新しいタブは既存のタブの右側に順次追加されるが、この挙動を設定項目
``workbench.editor.openPositioning`` の値で制御可能だ。例えば、新しいタブを左側
に表示させたいならば：

.. code:: json

   {
       "workbench.editor.openPositioning": "left"
   }

プレビューモード
----------------------------------------------------------------------

:guilabel:`EXPLORER` でシングルクリックでファイルを選択すると、そのファイルはプ
レビューモードで表示される。このとき、既存の Editor を再利用する。ファイルを素早
く閲覧しているときに、訪問したファイルすべてに独自の Editor を持たせたくない場合
には有用だ。ファイルの編集を開始したり、ダブルクリックでファイルを開いたりする
と、そのファイル専用の新しい Editor が生成する。

プレビューモードの Editor では、タブのラベルがイタリックで描画される。

プレビューモードを使用せず、常に新しい Editor を作成したい場合、次の設定で挙動を
制御する：

``workbench.editor.enablePreview``
  プレビューモードの有効性を指定する。
``workbench.editor.enablePreviewFromCodeNavigation``
  コードナビゲーションが開始するときに、Editor をプレビューモードのままにしてお
  くかどうかを指定する。プレビューは開いたままにはならず、明示的に開きっぱなしに
  されない限りはその Editor は再利用されることになる。
``workbench.editor.enablePreviewFromQuickOpen``
  Quick Open からファイルを開くときのプレビュー Editor の有効性を指定する。

下二つの設定は ``workbench.editor.enablePreview`` を ``false`` にしているときに
はまったく無視される。

.. admonition:: 利用者ノート

   複数ファイルを同時に閲覧したい利用状況を考慮していない概念のようなので、無効
   にしているがどうだろう。

Editor Groups
======================================================================

Editor を分割すると、Editor Group という Editor のコンテナーが新たに生成する。
このグループが占める領域を、縦方向と横方向にいくつでも並べて形成することが可能だ。

:guilabel:`EXPLORER` ビューの上部にある :guilabel:`OPEN EDITORS` セクションでこ
れらを確認することができる。

.. admonition:: 利用者ノート

   :guilabel:`OPEN EDITORS` が見当たらない場合、次の設定項目の値を確認すること：

   * ``explorer.openEditors.minVisible``
   * ``explorer.openEditors.visible``

Editor Group をワークベンチにドラッグ＆ドロップしたり、グループ間で個々の Editor
を移動したり、グループ全体を素早く閉じたりすることが可能だ。

VS Code ではタブを有効にしているかどうかに関わらず、Editor Group が成立する。
タブがない場合、Editor Group は開いている Editor のスタックとなり、最近選択され
たものが Editor 区域に表示される。

Editor に対するグリッドレイアウト
======================================================================

Editor を分割すると横に開くので、Editor Groups は水平方向に増えていく。これは既
定の挙動であり、Editor Groups は縦にも横にも好きにレイアウト可能だ。

柔軟なレイアウトを実現するために、空の Editor Group を作成することができる。通常
は、Editor Group にある最後の Editor を閉じるとグループ自体も閉じるが、設定項目
``workbench.editor.closeEmptyGroups`` の値で閉じないように動作を変更できる。

メニュー :menuselection:`View --> Editor Layout` を見ると、定義済みレイアウト各
種を確認できる。

キーボードだけで Editor レイアウトを調整するキーボードコマンドはたくさんあるもの
の、タブのドラッグ＆ドロップで Editor を望む方向に分割するのが手っ取り早い。

Editor Group 右上の分割アイコンに :kbd:`Alt` キーを押しながらマウスホバーすると、
アイコンイメージの水平と垂直が切り替わり、発動するコマンドもそれに対応して変化する。

ショートカットキー
----------------------------------------------------------------------

Editor および Editor Group 間を迅速にナビゲートするコマンドに対する既定キーバイ
ンドを記す。マウスでタブをクリックするよりも早い場合が多い。

.. csv-table::
   :delim: @
   :header: キーバインド,操作

   :kbd:`Ctrl` + :kbd:`PageDown` @ 次の Editor へ行く
   :kbd:`Ctrl` + :kbd:`PageUp` @ 前の Editor へ行く
   :kbd:`Ctrl` + :kbd:`Tab` @ Editor Group で最近使われた Editor へ行く
   :kbd:`Ctrl` + :kbd:`1` @ いちばん左の Editor Group へ行く
   :kbd:`Ctrl` + :kbd:`2` @ 中央の Editor Group へ行く
   :kbd:`Ctrl` + :kbd:`3` @ いちばん右の Editor Group へ行く
   :kbd:`Ctrl` + :kbd:`W` @ 現在いる Editor を閉じる
   :kbd:`Ctrl` + :kbd:`K` :kbd:`W` @ Editor Group にある Editor すべてを閉じる
   :kbd:`Ctrl` + :kbd:`K` :kbd:`Ctrl` + :kbd:`W` @ Editor すべてを閉じる

タブを一切使わずに作業する
======================================================================

タブを画面から抹消して作業しているときの話題を記す。

.. admonition:: 利用者ノート

   上級者向けのスタイルなので、真似しなくていい。

プレビューモードを無効にする
----------------------------------------------------------------------

タブなしで済ます場合、:guilabel:`EXPLORER` の :guilabel:`OPEN EDITORS` セクショ
ン上の操作がファイルナビゲーションを行うための素早い方法となる。プレビューモード
では、シングルクリックでファイルを開いても、:guilabel:`OPEN EDITOR` 内にも
Editor Group にもそれは追加されない。次の設定項目でこの挙動を無効にできる：

* ``workbench.editor.enablePreview``
* ``workbench.editor.enablePreviewFromQuickOpen``

全 Editor 履歴上ナビゲーション
----------------------------------------------------------------------

:kbd:`Ctrl` + :kbd:`Tab` のキーバインドを変更し、Editor Group とは関係なく、
履歴から開いているすべての Editor を一覧表示することができる。次のコマンドにバイ
ンドする：

* ``workbench.action.openPreviousEditorFromHistory``
* ``workbench.action.quickOpenNavigateNext``

単一 Editor というより Editor Group 全体を閉じる
----------------------------------------------------------------------

Editor を一つを閉じるときに Editor Group 全体を閉じるという動作が気に入った場合
は、コマンド ``workbench.action.closeEditorsInGroup`` を実行する。

メインウィンドウ
======================================================================

プロセス間でウィンドウ（インスタンス）を開いたり復元したりする方法を制御する。
以下、VS Code 起動時にコマンドラインオプション ``--new-window`` も
``--reuse-window`` も指定されないとする。

設定項目 ``window.openFoldersInNewWindow`` や ``window.openFilesInNewWindow`` は
ファイルやフォルダーに対して新しいウィンドウを開くか、最後にアクティブだったウィ
ンドウを再利用するかを決定する。可能な値は ``default``, ``on``, ``off`` のいずれかだ。

値が ``default`` に設定されている場合、ウィンドウを開く要求が行われた場所のコンテキスト
に基づいて、ウィンドウを再利用するかどうかが決定される。

値を ``on`` または ``off`` に設定すると、常に同じ動作をするようになる。例えば、
ファイルメニューからファイルやフォルダを選ぶといつでも新しいウィンドウでなるべく
開く場合は、値を ``on`` にすればいい。

設定項目 ``window.restoreWindows`` は、以前のセッションで開いたウィンドウをどの
ように復元するかを VS Code に指示する。既定では VS Code は前回のセッションで作業
したすべてのウィンドウを復元する。この設定を ``none`` に変更すると、ウィンドウを
一切開かず、常に空の VS Code インスタンスで開始する。1 に変更すると、最後に開い
たウィンドウやフォルダーを開き、フォルダーが開いているウィンドウしか復元しない。
