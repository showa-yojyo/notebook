======================================================================
テーマ
======================================================================

テーマを使用すると VS Code の UI で使われる色合いやアイコンを趣味に合わせて変更
することができる。

.. admonition:: 利用者ノート

   テキスト編集の効率を直接上げるような特徴ではないはずなので、これに時間をあま
   り費やさないこと。

.. attention::

   :doc:`./index` 冒頭の前提条件に留意すること。

.. contents::

テーマを選ぶ
======================================================================

次のいずれかの方法でテーマ選択欄を画面に出す：

* メニュー :menuselection:`File --> Preferences --> Color Theme` を選択する
* Activity Bar 歯車アイコンから :menuselection:`Color Theme` を選択する
* コマンドパレットで :guilabel:`Preference: Colot Theme` を直接実行する
* キーバインド :kbd:`Ctrl` + :kbd:`K` :kbd:`Ctrl` + :kbd:`T` を押す

すると現在利用可能なテーマ一覧が現れる。ここで :kbd:`↑` キーと :kbd:`↓` キーを
使ってカーソルが乗っている項目のテーマをプレビューできる。:kbd:`Enter` を押すと
そのテーマに決まる。

現在適用されているテーマは、ユーザー設定に保存される：

.. code:: json

   {
       "workbench.colorTheme": "Default Dark+"
   }

普通はテーマはユーザー設定に保存され、すべてのワークスペースに適用される。ワーク
スペース固有のテーマを設定することも可能であり、その場合にはワークスペース設定
ファイルに設定すればいい。

Marketplace でテーマを入手する
======================================================================

VS Code には拡張機能のインストールなしで利用可能なテーマがいくつか用意されている。
まずはそれらを試す。

VS Code Extension Marketplace にはコミュニティーがアップロードした多くのテーマが
ある。欲しいテーマを見つけたら、それをインストールして VS Code を再起動すれば、
その新しいテーマが利用可能になる。

:guilabel:`EXTENSIONS` ビューの検索欄でテーマに絞って検索するには、フィルター
``@category:"themes"`` をかける。

OS 配色に基づく自動切替
======================================================================

Windows の VS Code は明るい色と暗い色の配色をサポートしている。
設定項目 ``window.autoDetectColorScheme`` と ``window.autoDetectHighContrast``
の値次第では、OS の配色の変化を感知して、それに即したテーマに切り替わるようにで
きる。

配色変更時に使用するテーマをカスタマイズするために、次の設定項目で望みのライト、
ダーク、ハイコントラストテーマを得られる：

``workbench.preferredDarkColorTheme``
    ダークテーマで使用する既定テーマ。
``workbench.preferredLightColorTheme``
    ライトテーマで使用する既定テーマ。
``workbench.preferredHighContrastColorTheme``
    ハイコントラストのダークモードで使用する既定テーマ。
``workbench.preferredHighContrastLightColorTheme``
    ハイコントラストのライトモードで使用する既定テーマ。

カラーテーマをカスタマイズする
======================================================================

Workbench 色
----------------------------------------------------------------------

設定項目 ``workbench.colorCustomizations`` および ``editor.tokenColorCustomizations``
により、アクティブなカラーテーマをカスタマイズすることができる。

設定項目 ``workbench.colorCustomizations`` が適用されるのは VS Code ウィンドウ内
におけるリスト、ツリー、スクロールバー、ボタン、等々の UI 要素だ。
この設定項目の値を設定する際に IntelliSense を利用することもできるし、
カスタマイズ可能な色の一覧について、次の資料を参照することもできる：

`Theme Color | Visual Studio Code Extension API <https://code.visualstudio.com/api/references/theme-color>`__

特定のテーマだけをカスタマイズする場合は、例えば以下のように指定する：

.. code:: json

   {
       "workbench.colorCustomizations": {
           "[Monokai]": {
               "sideBar.background": "#347890"
           }
       }
   }

複数のテーマに対して一つのカスタマイズを適用する場合には、カスタマイズにテーマ名
を複数付けるか、テーマ名にワイルドカードとして記号 ``*`` を使用することができる。

.. code:: json

   {
       "workbench.colorCustomizations": {
           "[Abyss][Red]": {
               "activityBar.background": "#ff0000"
           },
           "[Monokai*]": {
               "activityBar.background": "#ff0000"
           }
       }
   }

Editor の構文強調
----------------------------------------------------------------------

Editor の構文強調の色を調整するには、ユーザー設定ファイル :file:`settings.json`
で ``editor.tokenColorCustomizations`` を使う。一般的な構文に対する設定済み構文
字句 ``'comments'``, ``'strings'``, ... の集合は利用可能だ。さらに必要なら
ば、TextMate のテーマ色規則を直接指定することで調整可能だ。
直接設定するには、TextMate の文法に対する理解と高度な技能が要求される。

.. code:: json

   {
       "editor.tokenColorCustomizations": {
           "[Monokai]": {
               "comments": "#229977"
           },
           "[*Dark*]": {
               "variables": "#229977"
           },
           "[Abyss][Red]": {
               "keywords": "#f00"
           }
       },
       "textMateRules": [
           {
               "scope": "support.type.property-names.json",
               "settings": {
                   "foreground": "#7fb785"
               }
           }
       ]
   }

Editor の意味論的強調
======================================================================

言語によっては（といっても現在は TypeScript, JavaScript, Java しかないようだが）
意味論的字句を用意している。意味論的字句は言語サービスのシンボル理解に基づいてお
り、正規表現によって駆動する TextMate 文法由来の構文字句よりも正確だ。意味論的字
句から計算される意味論的強調は構文強調の上に乗りかかり、強調を修正し、質を高める。

.. admonition:: 利用者ノート

   本文の比較キャプチャー例と解説を参照。

設定項目 ``editor.semanticHighlighting.enabled`` は意味論的強調が適用されるかど
うかのスイッチとして機能する。値は ``true``, ``false``, ``configuredByTheme`` を
取り得る。

設定値 ``true`` と ``false`` は、すべてのテーマに対して意味論的強調のオンかオフ
かを指定する。

既定値は ``configuredByTheme`` だ。これはテーマそれぞれに意味論的強調を有効にす
るかどうかを制御できるようにする。VS Code に同梱されているすべてのテーマは、既定
で意味論的強調が有効になっている。

次の方法でテーマ設定を上書きできる：

.. code:: json

   {
       "editor.semanticTokenColorCustomizations": {
           "[Rouge]": {
               "enabled": true
           }
       }
   }

ある言語モードで意味論的強調が有効かつ利用可能である場合、意味論的字句がどのよう
に着色されるかはテーマによって異る。意味論的字句のうちいくつかは標準化されてお
り、確立された TextMate 作用域に対応している。そのテーマがこれらの TextMate 作用
域の着色規則を持っている場合、追加の着色規則は必要なく、意味論的字句はその色を
使って記される。

その他のスタイル規則は設定項目 ``editor.semanticTokenColorCustomizations`` 中に
ユーザーが構成することができる：

.. code:: json

   {
       "editor.semanticTokenColorCustomizations": {
           "[Rouge]": {
               "enabled": true,
               "rules": {
                   "*.declaration": { "bold": true }
               }
           }
       }
   }

どのような意味論的字句が計算され、どのようにスタイル付けされているかを確認するに
は、現在のキャレット位置のテキスト情報を表示するコマンド
:guilabel:`Developer: Inspect Editor Tokens and Scopes` を実行するといい。

指定された位置の言語で意味論的字句が利用可能で、テーマによって有効化されている場
合、検査ツールは意味論的字句型の区画を表示する。そこには、意味論的字句情報（型お
よび修飾子）と、適用されるスタイリング規則が示される。

意味論的字句とスタイリング規則の構文に関する詳細は、次を参照：
`Semantic Highlight Guide | Visual Studio Code Extension API <https://code.visualstudio.com/api/language-extensions/semantic-highlight-guide>`__

独自の色テーマを創作する
======================================================================

テーマ拡張機能の創作と公開は簡単だ。ユーザー設定で色をカスタマイズし、コマンド
:guilabel:`Developer: Generate Color Theme From Current Settings` でテーマ定義
ファイルを生成する。

VS Code の Yeoman 拡張機能生成装置は、拡張機能の残りの部分を生成するのを助ける。
詳しくは：
`Create a new Color Theme <https://code.visualstudio.com/api/extension-guides/color-theme#_create-a-new-color-theme>`__

既定の色テーマを削除する
======================================================================

既定テーマを色テーマ選択欄から削除したいならば場合、:guilabel:`EXPLORER` ビュー
から無効にできる。ビューの上部にある漏斗アイコンをクリックし、
:menuselection:`Built-in` を選択すると、 :guilabel:`THEMES` 区画が表示され、そこ
に既定テーマが並ぶ。

組み込みテーマは一般の VS Code 拡張と同様、ミニ歯車のコンテキストメニューの
コマンド :menuselection:`Disable` を選択して無効にできる。

ファイルアイコンテーマ
======================================================================

ファイルアイコンテーマは拡張機能が提供し、ユーザーがお気に入りのファイルアイコン
の集合として選択することができる。ファイルアイコンは :guilabel:`EXPLORER` やタブ
ラベルに現れる。

ファイルアイコンテーマを選ぶ
----------------------------------------------------------------------

ファイルアイコン選択欄は次のいずれかの方法で開く：

* :menuselection:`File > Preferences > File Icon Theme`
* :guilabel:`Preferences: File Icon Theme`

:kbd:`↑` キーと :kbd:`↓` キーでアイコンプレビューが発動する。テーマを選択して
:kbd:`Enter` キーを押す。

既定では Seti ファイルアイコン集合が使用される。:guilabel:`EXPLORER` で表示され
るアイコンだ。いったんファイルアイコンテーマを選択すると、VS Code を再起動するた
びにそのテーマで表示される。ファイルアイコンを無効にすることもでき、それには
:guilabel:`None` を選択する。

VS Code には Minimal と Seti のファイルアイコンテーマが同梱されている。他の
ファイルアイコンテーマをインストールするには、選択欄で項目
:guilabel:`Install Additional File Icon Themes` を選択すると、
:guilabel:`EXTENSIONS` ビューにファイルアイコンテーマ用の検索キーワード
``tag:icon-theme`` が表示される。

また、VS Code Marketplace を直接閲覧して利用可能なテーマを見つけることもできる。

アクティブなファイルアイコンテーマは、ユーザー設定に記録される：

.. code:: json

   {
       "workbench.iconTheme": "vs-seti"
   }

独自のファイルアイコンテーマを創作する
======================================================================

アイコン（SVG が望ましい）から独自のファイルアイコンテーマを創作することができる：
`File Icon Theme | Visual Studio Code Extension API <https://code.visualstudio.com/api/extension-guides/file-icon-theme>`__
