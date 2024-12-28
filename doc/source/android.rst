======================================================================
Android 利用ノート
======================================================================

いつもならこの辺にバージョン情報などを記すのだが、この分野は進歩が激しいので意味
がないだろう。ノート内容も公式記述へのリンク一覧で構成することにする。

.. contents::

基本知識
======================================================================

次のヘルプを読み、破壊的でないものをすべて実践しておく：

* `デバイス メーカーや携帯通信会社のサポートを利用する <https://support.google.com/android/answer/3094742?hl=ja&ref_topic=7313011&sjid=4050075676267591976-AP>`__
* `Android デバイスで画面の画像（スクリーンショット）または動画を撮影する <https://support.google.com/android/answer/9075928?hl=ja&ref_topic=7313240&sjid=4050075676267591976-AP>`__
* `Android デバイスでアプリを見つける、開く、閉じる <https://support.google.com/android/answer/9079646?hl=ja&ref_topic=7311596&sjid=4050075676267591976-AP>`__
* `Android デバイスにアプリをダウンロードする <https://support.google.com/android/answer/9457058?hl=ja&ref_topic=7311596&sjid=4050075676267591976-AP>`__
* `Android デバイスでアプリを削除する <https://support.google.com/android/answer/13627402?hl=ja&ref_topic=13627086&sjid=4050075676267591976-AP>`__
* `Android デバイスを Wi-Fi ネットワークに接続する <https://support.google.com/android/answer/9075847?hl=ja&ref_topic=7651297&sjid=4050075676267591976-AP>`__
* `Android デバイスを Bluetooth 経由で接続する <https://support.google.com/android/answer/9075925?hl=ja&ref_topic=7651297&sjid=4050075676267591976-AP>`__
* `Android でアクセス ポイントやテザリングを使用してモバイル接続を共有する <https://support.google.com/android/answer/9059108?hl=ja&ref_topic=7651297&sjid=4050075676267591976-AP>`__
* `Android デバイスと Windows パソコンの間でファイルを共有する <https://support.google.com/android/answer/13801258?hl=ja&ref_topic=7651297&sjid=4050075676267591976-AP>`__
* `Android デバイスのデータをバックアップ、復元する <https://support.google.com/android/answer/2819582?hl=ja&ref_topic=7650590&sjid=4050075676267591976-AP>`__
* `音量、音、バイブレーションの設定を変更する <https://support.google.com/android/answer/9082609?hl=ja&ref_topic=7650590&sjid=4050075676267591976-AP>`__
* `Android デバイスの電池を長持ちさせる <https://support.google.com/android/answer/7664692?hl=ja&ref_topic=7650590&sjid=4050075676267591976-AP>`__
* `Android で通知を管理する <https://support.google.com/android/answer/9079661?hl=ja&ref_topic=7651002&sjid=4050075676267591976-AP>`__
* `Android デバイスを紛失した場合に見つけられるようにしておく <https://support.google.com/android/answer/3265955?hl=ja&ref_topic=7651004&sjid=4050075676267591976-AP>`__
* `他人に無断で使用されないようにデバイスを保護する <https://support.google.com/android/answer/9459346?hl=ja&ref_topic=7340889&sjid=4050075676267591976-AP>`__
* `Android のバージョンを確認して更新する <https://support.google.com/android/answer/7680439?hl=ja&ref_topic=7311597&sjid=4050075676267591976-AP>`__

私の携帯電話（二代目）は OPPO A55s 5G だ。メーカーへのリンクがここにないので、自
分で探して `OPPO製品のユーザーガイド <https://www.oppojapan.com/userguide/>`__
をブックマークする。

スクリーンショットの操作はむしろ意図せぬ電源ボタンと音量ボタンの同時押しで発動す
るのが不愉快なので、この動作を設定で無効化することが可能であることを知っておく。

Bluetooth 経由で PC に接続する方法を習得しておく。PC をケーブルで接続するのを避
けたい場合に行うかもしれない。

テザリングはインターネット接続が身近になかった頃の携帯電話（初代）で多用、電池が
パンパンになって難儀したことがある。あれは勉強になった。

Windows PC と Android 携帯電話との間でニアバイシェアという技法でファイルを共有す
ることが可能だ。Windows にプログラムを一つインストールする必要がある。Bluetooth
とも関係する。

Android のバックアップ方法は自動と手動がある。Google アカウントが急所だというこ
とを理解しておくだけで済むか。

音量と振動量は設定対象が細分化されていて、意識して設定しないと意図せぬ状況でア
ラームが鳴ったり本体が震えたりして驚かされる。修練したい。

電池を持続させるために細かい設定をしておく。すぐにできるのはこれくらい：

* すぐに画面がオフになるようにする。
* 画面の明るさを下げる。
* キー操作音やバイブレーションをオフにする。
* バッテリー消費量が多いアプリを制限する。
* 自動調整バッテリーをオンにする。

通知管理はわかりやすさを優先する。オプションによっては電池に響くかもしれない。

紛失対策は携帯電話を二台持っていると万全にできるが、一台しかなくても「デバイスを
探す」をインストールして動作確認するくらいは行いたい。そして無断使用を防止するべ
く画面ロックを必ず有効にしておけ。

ユーザー補助機能はとても大切
----------------------------------------------------------------------

ユーザー補助項目は時間をかけて設定をチェックしておいて損はない。

* `テキストとディスプレイの設定を変更する <https://support.google.com/accessibility/android/answer/11183305?hl=ja&ref_topic=9079043&sjid=4050075676267591976-AP>`__
* `バイブレーションの設定を変更する <https://support.google.com/accessibility/android/answer/9078946?hl=ja&ref_topic=9079844&sjid=4050075676267591976-AP>`__

何はさておきフォントサイズの設定がたいへん重要だ。スライダーで数段階から選択可能
なので、一画面に表現可能な情報量を極大化するならば左端、眼精疲労にこりごりである
ならば右端、という具合に決めてかまわない。使い勝手が全然異なってくる。

「アニメーションを無効化」するとさまざまな操作において体感速度が向上する。

「画面を暗くする」も軽視できない。起床間際に画面を確認するときにこの設定が効いて
くる。

`時計アプリ <https://support.google.com/android/topic/3453450?hl=ja&ref_topic=7083807&sjid=4050075676267591976-AP>`__
は右上メニューから設定ができる。わかりやすい。

当面は無視する項目
======================================================================

以下の項目は積極的に設定することはしない。何度か試しても設定できなかったというも
のもある：

* `Android スマートフォンを使用して緊急時に助けを求める <https://support.google.com/android/answer/9319337?hl=ja&ref_topic=7313240&sjid=4050075676267591976-AP>`__
* `画面の固定と固定解除 <https://support.google.com/android/answer/9455138?hl=ja&ref_topic=7340889&sjid=4050075676267591976-AP>`__
* `不明なトラッカーを検出する <https://support.google.com/android/answer/13658562?hl=ja&ref_topic=7311597&sjid=4050075676267591976-AP>`__
* `Android デバイスで画面ロックを設定する <https://support.google.com/android/answer/9079129?hl=ja&ref_topic=7340889&sjid=4050075676267591976-AP>`__

画面ロックは本体とは異なるパスワード（推奨は六文字）を別途設定して、特定のタイミ
ングでそれを操作者に入力させるものだ。混乱しそうなのでやめておきたい。

まだ調査対象が残っていそうな項目
======================================================================

* `パスキーでアプリやウェブサイトにログインする <https://support.google.com/android/answer/14124480?hl=ja&ref_topic=7340889&sjid=4050075676267591976-AP>`__
* `Android に関する問題のトラブルシューティング <https://support.google.com/android/topic/7651524?hl=ja&ref_topic=7311597&sjid=4050075676267591976-AP>`__

PC で GitHub にログインするときには利用しているものの、パスキーは説明ビデオを視
聴したがよくわからない。

* `Google カメラ ヘルプ <https://support.google.com/googlecamera/?sjid=4050075676267591976-AP#topic=6164365>`__

カメラレンズが前面と後面の二つあることを知る。位置情報はオフにしたい。バックアッ
プは PC でやるので重複が嫌ならオフにする。

* `Gboard ヘルプ <https://support.google.com/gboard?sjid=4050075676267591976-AP#topic=9023832>`__

Gboard はテキスト欄をアクティブにすると画面下部に現れる仮想キーボードのことだと
思っていいだろう。この文字盤天井中央の歯車ボタンで設定に入れる。キー操作オン、振
動、絵文字をオフするなど、単純にするのが好ましい。単語リストの削除機能は存在だけ
でも覚えておく。携帯電話を買い替えるときなどに店員に渡す前に消去したい。

翻訳は Gboard の機能ではなく Android 版 DeepL を利用する。Google Play ストアから
インストール可能だ。

キーボードのツールバー部分はカスタマイズ可能。いらないボタンを下のパレットへド
ラッグしておくと良い。

* `Google フォト ヘルプ <https://support.google.com/photos/?sjid=4050075676267591976-AP#topic=6128818>`__

主に携帯電話に保存されている写真やビデオを一覧するだけでなく、簡単な編集までも行
える。先述の方法を用いて写真やビデオを PC にインポートして、ImageMagick や
FFmpeg で腰を据えて編集する場合もある。写真は寸法変更機能がないらしいのが残念。

* `Google Play ヘルプ <https://support.google.com/googleplay/?sjid=4050075676267591976-AP#topic=3364260>`__

銭がないので支払いが発生する商品をダウンロードしないように注意する。自動更新の条
件を Wi-Fi 接続時に限定する。

* `Google ドキュメントの使い方 <https://support.google.com/docs/answer/7068618?sjid=4050075676267591976-AP&co=GENIE.Platform%3DAndroid&oco=1>`__
* `Google スプレッドシートの使い方 <https://support.google.com/docs/answer/6000292?sjid=4050075676267591976-AP&co=GENIE.Platform%3DAndroid&oco=1>`__

とりあえずインストールしておく。携帯電話の環境で履歴書、手紙、論文などをまともに
執筆するのはどうしても厳しい。ビューワーとして利用できないものか。

PC で作成した LibreOffice Calc ファイルを Android 携帯電話にインポート。Googleス
プレッドシートで開こうとしたらなぜかアップロードが必要だという。メッセージ内容か
ら察するに、ローカルの外部フォーマットファイルは読み込めず、固有フォーマットに変
換するのがアップロード先だと考えられる。

* `Google 検索 ヘルプ <https://support.google.com/websearch/?sjid=4050075676267591976-AP#topic=3378866>`__

  * `検索履歴を管理、削除する <https://support.google.com/websearch/answer/6096136?hl=ja&ref_topic=9255574&sjid=14512694331345300003-AP&co=GENIE.Platform%3DAndroid&oco=1>`__
  * `Google 検索の結果を絞り込む <https://support.google.com/websearch/answer/2466433?hl=ja&ref_topic=3081620&sjid=14512694331345300003-AP>`__

いい機会だから祖業である検索機能の活用技術を向上しよう。

以上
