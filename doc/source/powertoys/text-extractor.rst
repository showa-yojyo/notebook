======================================================================
Text Extractor
======================================================================

Text Extractor は画面上の選択範囲からテキストを抽出する機能だ。

.. admonition:: 利用者ノート

   携帯電話でオンライン麻雀ゲームのスコア画面を撮影することがよくあるのだが、そ
   の数字を転写するのがたいへん面倒だ。画像を PC にインポートして画面に表示させ
   てこの機能でテキストを抽出したい。

.. attention::

   :doc:`./index` 冒頭の前提条件に留意すること。

.. contents::

稼働および停止方法
======================================================================

起動には :kbd:`Win` + :kbd:`Shift` + :kbd:`T` を押す。画面が薄暗くなる。このと
き、マウスドラッグで矩形選択して中に含まれている文字列をクリップボードにコピーす
る。選択領域のテキストが認識され、クリップボードにコピーされると、キャプチャー
モードが解除される。あるいは :kbd:`Esc` キーを押して終了することができる。

調整
======================================================================

矩形選択中に :kbd:`Shift` を押し始めると、操作モードが矩形移動に切り替わる。
:kbd:`Shift` を離すと矩形指定モードに再び戻る。

* 出力されたテキストが完璧でない場合もあるので、簡単な校正をする必要がある。
* このツールは OCR を応用したものだ。
* 既定の言語は :menuselection:`Windows のシステム言語 --> キーボード設定` に基づ
  く。OCR 言語パックをインストール可能。

対応言語
======================================================================

Text Extractor は OCR 言語パックがインストールされている言語しか認識できない。そ
の一覧を得るには、PowerShell で次のコマンドを実行する：

.. code:: pwsh

   PS > [Windows.Media.Ocr.OcrEngine, Windows.Foundation, ContentType = WindowsRuntime]

   IsPublic IsSerial Name      BaseType
   -------- -------- ----      --------
   True     False    OcrEngine System.Runtime.InteropServices.WindowsRuntime.RuntimeClass

   PS > [Windows.Media.Ocr.OcrEngine]::AvailableRecognizerLanguages

   DisplayName     : 日本語
   LanguageTag     : ja
   NativeName      : 日本語
   Script          : Jpan
   LayoutDirection : Ltr
   AbbreviatedName : 日本

対応言語パックの一覧を返すには、:program:`PowerShell` を管理者として開き、次のコ
マンドを実行する：

.. code:: pwsh

   > Get-WindowsCapability -Online | Where-Object { $_.Name -Like 'Language.OCR*' }

かなり長い出力となる。言語と場所は省略されるので、出力に使用できない言語がある場
合、その言語は OCR が対応しないことを意味する。

OCR 言語パック構成
----------------------------------------------------------------------

OCR 言語パックをインストールするコマンド例 (en-US) を以下に示す：

.. code:: pwsh

   > $Capability = Get-WindowsCapability -Online | Where-Object { $_.Name -Like 'Language.OCR*en-US*' }
   > $Capability | Add-WindowsCapability -Online

アンインストールは次のように実行する：

.. code:: pwsh

   > $Capability = Get-WindowsCapability -Online | Where-Object { $_.Name -Like 'Language.OCR*en-US*' }
   > $Capability | Remove-WindowsCapability -Online

トラブルシューティング
======================================================================

本家のトラブルシューティングは常識的であり過ぎる。当ノートでは独自の厄介事を記す。

公式文書の PowerShell コードで InvalidOperation 例外が生じる
----------------------------------------------------------------------

上記の Windows.Media.Ocr.OcrEngine を含むコードについては、PowerShell 7 で実行す
ると例外が送出する。これについては 古い PowerShell を利用することで解決する。

日本語をスキャンすると空白文字がインターリーブする
----------------------------------------------------------------------

このような感じになる。校正が必要になるとは断られているものの、これでは厳しい：

.. code:: text

   ト ラ づ ル シ ュ ー テ ィ ン ゲ
   日本語 を ス キ ャ ン す る と 空白文字 が イ ン タ ー リ ー づ す る

こうなるとクリップボードからテキストを抽出して空白文字を削除するコマンドにパイプ
するしかない。
