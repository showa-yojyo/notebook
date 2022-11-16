======================================================================
キーバインド
======================================================================

VS Code でもコマンドを実行するショートカットキーをユーザーが割り当てることが可能
だ。既定のキーバインドの確認方法、カブリの検出方法、カスタマイズ方法を習得した
い。

.. attention::

   :doc:`./index` 冒頭の前提条件に留意すること。

.. contents::

Keyboard Shortcuts Editor
======================================================================

:guilabel:`Keyboard Shortcuts` Editor は豊富で簡単なキーボードショートカットの編
集機能を提供する。キーバインドを持つコマンドも持たないコマンドも一覧表示され、利
用可能なコマンドを指定してキーバインドを容易に変更、削除、リセットすることができ
る。また、上部に検索欄があり、コマンドやキーバインドを見つける助けになる。この
UI は次のいずれかの方法で表示できる：

* コマンドパレットで :guilabel:`Preferences: Open Keyboard Shortcuts` を直接実行
  する
* メインメニューで :menuselection:`File --> Preferences --> Keyboard Shortcuts`
  を選択する
* Activity Bar 歯車アイコンで :menuselection:`Keyboard Shortcuts` を選択する
* ショートカットキー :kbd:`Ctrl` + :kbd:`K` :kbd:`Ctrl` + :kbd:`S` を押す

重要なのは、キーボードレイアウトに応じたキーバインドが表示されることだ。例えば
US キーボードレイアウトのキーバインドは、レイアウトがドイツ語に変更されると異な
るキーバインドが一般的には表示される。キーバインド入力ダイアログは、キーボードレ
イアウトに従ってキーバインドを割り当てる。

キーマップ拡張
======================================================================

メインメニューで :menuselection:`File --> Preferences --> Migrate Keyboard Shortcuts from...`
を選択すると、よその有力エディターで使われるキーマップ拡張機能
の一覧が表示される。これらの拡張機能は VS Code の、特に Editor 周りに関する
ショートカットを他のエディターのものと一致するように変更するものであり、キーボー
ドショートカットを新しく学ぶ必要はないとされる。また、Marketplace には拡張機能の
キーマップのカテゴリーがある。

.. admonition:: 利用者ノート

   実際には :guilabel:`EXTENSIONS: MARKETPLACE` ビューを表示させたら
   文字列 ``keymaps`` とエディターの名前を入力するのがいい。

ショートカットキー一覧表
======================================================================

メインメニューで :menuselection:`Help --> Keyboard Shortcut Reference` を選択す
ると、ショートカットキー一覧表を記した PDF ファイルが開く。ブラウザーで。

キーバインドの競合を検出する
======================================================================

多くの拡張機能をインストールしている場合や、キーボードショートカットをカスタマイ
ズしている場合、同じキーボードショートカットが複数のコマンドにバインドされている
ことがある。このようなキーバインド競合は混乱した動作を引き起こすことがある。

Keyboard Shortcuts Editor のコンテキストメニューにはコマンド
:menuselection:`Show Same Keybindings` があり、キーバインドが一致する項目に絞っ
て表示する。

多重定義されているキーバインド項目の :guilabel:`Source` や :guilabel:`When` を確
認して競合を解消するといい。

トラブルシューティング
======================================================================

キーバインドに関する問題のトラブルシューティングを行うにはコマンド
:guilabel:`Developer: Toggle Keyboard Shortcuts Troubleshooting` を実行する。
ショートカットキーのロギングが有効になると、対応するログファイルの
:guilabel:`OUTPUT` 出力パネルが現れる。対象のショートカットキーを押して、VS Code
がどのキーボードショートカットを検出し、どのコマンドが呼び出されるかを確認するこ
とができる。

.. admonition:: 利用者ノート

   実際にはショートカットキーが効かないとき使うとどうなるか試す。

変更したキーバインドを見る
======================================================================

Keyboard Shortcuts Editor 右上の詳細アイコンのメニューから
:menuselection:`Show User Keybindings` を選択すると、ユーザーが変更したキーバイ
ンドに絞って表示することができる。検索欄に ``@source:user`` と手動で入力してもい
い。

.. admonition:: 利用者ノート

   :guilabel:`Keybinding` が空欄の項目は、キーバインドが削除されていることを表
   す。

JSON を編集してカスタマイズする
======================================================================

ショートカットキーをカスタマイズするのは、設定ファイル :file:`keybindings.json`
を編集することでも可能だ。これを Editor で開くには、次の方法がある：

* Keyboard Shortcuts Editor の :menuselection:`Open Keyboard Shortcuts (JSON)`
  を選択する
* コマンドパレットから :guilabel:`Preferences: Open Keyboard Shortcuts (JSON)`
  を直接実行する

キーボード規則
======================================================================

規則は、次の要素からなる：

``key``
    押されたキー。
``command``
    実行するコマンドの識別子。
``when``
    コンテキストに応じて評価される真偽値を返す式。オプション。

Chord を記述することも可能。キーストロークを空白文字で分離して記述する。例：

.. code:: text

   "Ctrl+K Ctrl+C"

キーが押されると、

1. 規則が下から上に評価される。
2. ``key`` と ``when`` の双方が合致する最初の規則が受け入れられる。
3. それ以上の規則は処理されない。
4. 見つかった規則にコマンドが設定されているならば、それが実行される。

の場合、キーとタイミングの両方で一致する最初のルールが受け入れられます。

評価順が下から上である理由は、UI を使ってキーバインド規則を追加したときに
:file:`keybindings.json` の JSON オブジェクトの下部に新しい規則が入るからだ。
結果的に、新しい規則が古いものを上書きすることになる。

受理されるキー
======================================================================

要素 ``key`` は修飾キーとキー自身からなる。修飾キーは Windows の場合、次が使用可
能だ：

* ``Ctrl+``
* ``Shift+``
* ``Alt+``
* ``Win+``

キー自身としては次のものが使用可能だ：

.. code:: text

   {a..z}
   {0..9}
   f{1..19}
   [
   ]
   , - = [ ] \ ; ', , . /
   {left,up,right,down,pageup,pagedown,end,home}
   {tab,enter,escape,space,backspace,delete}
   {pausebreak,capslock,insert}
   numpad{0..9}
   numpad_{multiply,add,separator,subtract,decimal,divide}

コマンド引数
======================================================================

コマンドに引数をつけて起動することができる。カスタムキーバインドを追加してそれを
実行する。次の例は :kbd:`Enter` キーを上書きしてテキストを出力する：

.. code:: json

   {
       "key": "enter",
       "command": "type",
       "args": { "text": "Hello World" },
       "when": "editorTextFocus"
   }

コマンド ``type`` は ``{"text": "Hello World"}`` を第一引数として受け取り、既定
コマンドを生成するのではなく、現在の Editor に ``"Hello World"`` を追加する。

引数を取るコマンドの詳細については、次の資料を参照：
`Built-in Commands | Visual Studio Code Extension API <https://code.visualstudio.com/api/references/commands>`__

指定のキーバインドを削除する
======================================================================

キーバインドカスタマイズは追加だけではなく、削除も可能だ。追加規則ではなく、削除
規則というものを定義する。対象となるキーバインドを削除するには、設定ファイル
:file:`keybindings.json` を直接編集し、コマンド名の先頭に ``-`` を追加する。例：

.. code:: json

   { "key": "tab", "command": "-jumpToNextSnippetPlaceholder" }

キーボードレイアウト
======================================================================

上述のキーは仮想キーに対する文字列表現であり、押したときに生成される文字とは一般
的には関係がない。より正確には：
`Virtual-Key Codes (Winuser.h) - Win32 apps | Microsoft Learn <https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes?redirectedfrom=MSDN>`__

.. admonition:: 利用者ノート

   Win32 API でプログラムを作成するときに、キーイベントハンドラーで書くアレだ。

キーボードレイアウトが異なると、上記の仮想キーの位置が変更されたり、キーが押され
たときに生成される文字が変更されたりするのだ通例だ。標準の US とは異なるキーボー
ドレイアウトを使用する場合、VS Code は次のように動作する：すべてのキーバインド
は、現在のシステムのキーボードレイアウトを考慮して UI 上に示される。例えば、フラ
ンス語のキーボードレイアウトを使用しているときの:guilabel:`Split Editor` は
``Ctrl+*`` と示される。

設定ファイル :file:`keybindings.json` 編集中、Editor は誤解を招くキーバインドを
強調表示する。標準的な US キーボードレイアウトでは文字で表現されるが、現在のシス
テムのキーボードレイアウトでは異なるラベルのキーを押す必要があるものだ。本文の画
面キャプチャーは、フランス語キーボードレイアウトを使用する場合に
:guilabel:`Default Keyboard Shortcuts` がどのように見えるかを示している。

設定ファイル :file:`keybindings.json` 編集中、キーバインド規則の入力を支援する
UI も用意されている。これを起動するには :kbd:`Ctrl` + :kbd:`K` :kbd:`Ctrl` +
:kbd:`K` を押す。

キーが押されたことをリスニングし、JSON コードをテキストボックスに出力し、その下
に現在のキーボードレイアウトの下で VS Code が検出したキーをレンダリングする。必
要なキーの組み合わせを入力して :kbd:`Enter` キーを押すと、規則コード片が挿入され
る。

キーボードレイアウトに依存しないキーバインド
======================================================================

スキャンコードを使用すると、キーボードレイアウトを変更しても変わらないキーバイン
ドを定義することができる。例：

.. code:: json

   {
       "key": "cmd+[Slash]",
       "command": "editor.action.commentLine",
       "when": "editorTextFocus"
   }

受理されるキーコードは次の文字列だ：

.. code:: text

   [F{1..19}]
   [Key{A..Z}],
   [Digit{0..9}]
   [Backquote]
   [Minus]
   [Equal]
   [Bracket{Left,Right}]
   [Backslash]
   [Semicolon]
   [Quote]
   [Comma]
   [Period]
   [Slash]
   [Arrow{Left,Up,Right,Down}]
   [Page{Up,Down}]
   [End]
   [Home]
   [Tab]
   [Enter]
   [Escape]
   [Space]
   [Backspace]
   [Delete]
   [Pause]
   [CapsLock]
   [Insert]
   [Numpad{0..9}]
   [Numpad{Multiply,Add,Comma,Subtract,Decimal,Divide}]

``when`` 節
======================================================================

オプションの ``when`` 節によって、キーバインドを有効にするタイミングを細かく制御
することが可能だ。キーバインドに ``when`` 節がない場合、そのキーバインドはグロー
バルに使用可能となる。 ``when`` 節は、キーバインドを有効にするために Boolean 値
で評価される。

UI のどの要素が表示され、アクティブになっているかによって、VS Code は色々なコン
テキストキーと特定の値を設定する。例えば、組み込みコマンド
:guilabel:`Start Debugging` には、ショートカットキー :kbd:`F5` があるが、これは
適切なデバッガーがあり (``debuggersAvailable``) Editor がデバッグモードでない
(``!inDebugMode``) ときに有効になる。

キーバインドの ``when`` 節は、コマンド
:guilabel:`Preferences: Open Default Keyboard Shortcuts (JSON)` 実行などで直接確
認することが可能だ。

.. code:: json

   {
       "key": "f5",
       "command": "workbench.action.debug.start",
       "when": "debuggersAvailable && !inDebugMode"
   }

条件演算子
----------------------------------------------------------------------

``when`` 節では ``==``, ``&&``, ``||`` などの条件演算子が利用可能だ。参照：
`when clause contexts | Visual Studio Code Extension API <https://code.visualstudio.com/api/references/when-clause-contexts#conditional-operators>`__

利用可能コンテキスト
----------------------------------------------------------------------

利用可能な ``when`` 節コンテキストについても上記リンク先を参照。ただし、この一覧
表は完全なものではなく、Keyboard Shortcuts Editor やコマンド
:guilabel:`Preferences: Open Default Keyboard Shortcuts (JSON)` 実行後に表示され
る JSON で他の ``when`` 節コンテキストを見つけることが可能だ。

リファクタリングのためのカスタムキーバインド
======================================================================

コマンド ``editor.action.codeAction`` は特定のリファクタリング (Code Actions)
に対するキーバインドを設定することが可能だ。例えば、次のキーバインド定義は
:menuselection:`Extract function` リファクタリング Code Actions を実行する：

.. code:: json

   {
       "key": "ctrl+shift+r ctrl+e",
       "command": "editor.action.codeAction",
       "args": {
           "kind": "refactor.extract.function"
       }
   }

詳しくはリファクタリングの章で述べられる。

Default Keyboard Shortcuts
======================================================================

三点アイコンメニューの :menuselection:`Show Default Keybindings` を使用すると、
VS Code の既定キーボードショートカットすべてを Keyboard Shortcuts Editor で表示
できる。検索欄に ``@source:default`` フィルターを適用するのと同じだ。
:guilabel:`Source` の値が :guilabel:`Default` のものだ。

この一覧表を JSON 表示するには、コマンドパレットから
:guilabel:`Preferences: Open Default Keyboard Shortcuts (JSON)` を直接実行する。

以下のいくつかのコマンドは、デフォルトのキーボードショートカットがないため、未割
り当てとして表示されますが、独自のキーバインドを割り当てることができます。

初期設定では既定キーバインドがコマンドがいくつもある。上述のように、キーバインド
を独自に割り当てることもできる。
