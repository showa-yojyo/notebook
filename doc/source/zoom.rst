======================================================================
Zoom Cloud Meetings 利用ノート
======================================================================

本稿では私の部屋（曳舟某所）から遠隔地にある企業、事業所とインターネットを介した
面接をするための一連の情報を記す。主旨は、余計な銭を使わずに面接を実施すること
だ。

オンライン会議サービスは複数あるが、いちばん指定機会が多いのは Zoom_ なので、そ
れをまず利用可能にしておきたい。

.. contents::

当環境
======================================================================

私の面接環境は次のとおりだ：

* Windows ノート PC
* Android 携帯電話
* Softbank Air
* イヤホン

特徴はノート PC にカメラも付いていないし、マイクも持っていないことだ。これらの欠
損を携帯電話で補う。インターネット接続はさすがにまともな環境が必要だ。

イヤホンはおそらく不要だが、百円ショップで気軽に調達可能ゆえ環境に含める。イヤホ
ンを使わない場合には後述のオーディオ周りの設定を変更する必要があるはずだ。

環境準備
======================================================================

サービスへのアカウント登録とアプリケーションのインストール、設定を実施する。本節
に述べる準備は一度だけ実施すれば十分だ。

Zoom アカウント登録
----------------------------------------------------------------------

Zoom_ のページにアクセスして自分のアカウントを新規登録する。トップページのサイン
アップというボタンから自然な流れで登録完了させること。

.. tip::

   * 事業者との面接用アカウントということを踏まえ、フォーマルな内容にする。
   * 登録終了後、アクセスに必要なメールアドレスとパスワードを安全な場所に控えて
     おく。

インストール
----------------------------------------------------------------------

Windows と Android それぞれにアプリケーションをインストールしておく。

PC には次のアプリケーションをインストールする。いずれもインストーラーをダウン
ロードしてインストールするのがわかりやすい。ちなみに :program:`winget` 対応済み。

* Zoom Cloud Meetings
* `e2eSoft iVCam`_

携帯電話には iVCam だけをインストールする。Google Play でインストールする。こち
らは紛れがない。

偶然だがどちらも中華系の企業製品だ。

アプリケーション設定
----------------------------------------------------------------------

本節で述べる手順は面接ごとに確認する。実際はいったん設定が済めば変更しないで済む
ことが多い。先に iVCam を動くようにしてから Zoom Cloud Meetings を触るのが良い。

Windows 側 iVCam
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

例えば Windows メニューから :menuselection:`e2eSoft iVCam --> iVCam` を選択する
などして本アプリケーションを実行する。画面右下のハンバーガーアイコンをクリックし
て :guilabel:`設定` を選択。こちらは設定が少ない。

* :menuselection:`全般 --> オーディオ --> 録音デバイス` を :guilabel:`携帯電話`
  に設定する。

Android 側 iVCam
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

携帯電話のメイン画面で iVCam を実行する。PC 版と似たような感じで歯車アイコンを
タップして設定画面を開く。こちらは設定が多い。

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   項目 | 値
   :guilabel:`撮影時の画面の向き` | 環境に合わせて縦か横を決める
   :guilabel:`解像度` | 大き過ぎないようにする
   :guilabel:`フレームレート` | 大き過ぎないようにする
   :guilabel:`画質` | :guilabel:`低画質`
   :guilabel:`音声` | ON
   :guilabel:`自動接続` | ON

Zoom Cloud Meetings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

例えば Windows メニューから :menuselection:`Zoom --> Zoom` を選択するなどして
Zoom Cloud Meetings を実行する。

ウィンドウが出現するので、メールアドレスとパスワードを入力してログイン。次に現れ
るアプリケーションメインウィンドウ右上の歯車アイコンをクリックして設定画面を出
す。次のように設定する：

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   項目 | 値
   :menuselection:`ビデオ --> カメラ` | :guilabel:`e2eSoft iVCam`
   :menuselection:`ビデオ --> マイビデオ --> マイビデオをミラーリング` | オン
   :menuselection:`オーディオ --> スピーカー` | いつものスピーカー
   :menuselection:`オーディオ --> 音量` | 適当
   :menuselection:`オーディオ --> マイク` | :guilabel:`マイク (e2eSoft iVCam)`

会議準備
======================================================================

まず、PC と携帯電話とで利用するインターネット接続を同一にする。私の場合は Wi-Fi
5G を有効化する。特に携帯電話の状態の確認をしっかりやることだ。

1. 会議時に自分の耳にはめるイヤホンを PC に接続する。
2. 携帯電話のカメラレンズを PC モニターの中央上部から自分の顔にめがける位置に固
   定する。適当な厚みのある本をモニター裏の空間に台のように配置して、その上に携
   帯電話を立てる。

次に各機器でアプリケーションの動作を有効にする。

1. PC で Zoom Cloud Meetings を起動し、メールアドレスとパスワードを入力、sign in
   する。
2. Zoom ウィンドウから :menuselection:`設定 --> ビデオ` を開いてカメラ画面を開い
   ておく。
3. PC の iVCam を開く。
4. 充電に自信がない場合には携帯電話をケーブルで PC に接続する。逆に余裕がある場
   合にはむしろケーブルを接続しないようにする。
5. Android の Wi-Fi をオンにして PC のそれと同じものを有効にする。
6. Android の iVCam を開く。
7. 再び PC の Zoom ウィンドウから :menuselection:`設定 --> ビデオ` で映像を目視
   で確認する。
8. :menuselection:`設定 --> オーディオ` でスピーカー（イヤホン）とマイクのテスト
   をする。

動作確認をしたら Zoom Cloud Meetings と iVCam のウィンドウをスタンバイして本番ま
で待つ。

.. tip::

   * 会議のかなり前までに Zoom Cloud Meetings の更新をチェックしておくべきだ。会
     議寸前になって自動更新が始まろうものなら目も当てられない。時間ギリギリに先
     されている URL を使って Zoom からログインする
   * 会議時間 40 分の枠があるので下手に接続できないことを意識することだ。ギリギ
     リに入室するほうがいい。
   * 時刻は Zoom メイン画面に表示されているものを基準にする。

以上の手順を上手くこなせば、面接直前には次のスクリーンショットのような状態になっ
ているだろう：

.. image:: /_images/zoom-screenshot.png
   :align: center
   :alt: Zoom 利用中のデスクトップ
   :width: 100%

面接
======================================================================

時間ギリギリに先方から提供されている URL とパスコードを使って Zoom Cloud
Meetings からログインする。

面接の内容自体は己でなんとかする。

面接が終了したら接続をただちに切断し、アプリケーションをすべて終了する。

おまけ：スクリーンキャプチャー
======================================================================

Zoom を全画面撮影ツールとして利用することも可能だ。XBox Game Bar と違って、デス
クトップ全体を撮影可能なのがありがたい。

収録開始手順の概略を示す：

1. Zoom にログインしておく
2. :guilabel:`新規ミーティング` を押す
3. :guilabel:`コンピュータ オーディオに参加する` を押す
4. 画面下部 :guilabel:`画面共有` を押す

   1. :guilabel:`画面` を選択
   2. :guilabel:`サウンドを共有` ドロップダウンから :guilabel:`ステレオ` を
      チェックし、その上でドロップダウンリストをチェック

5. :guilabel:`共有` を押し、画面共有中モードに移行する
6. 画面上部バー :menuselection:`詳細 --> このコンピュータにレコーディング` を押
   す

収録終了手順：

1. 画面上部にある収録停止ボタンを押す
2. 会議を終了、退出する
3. Zoom のメッセージボックスにより、エンコードが開始する

Zoom メイン設定からそれらしい項目を自分好みに前もって変えておくといい。

リンク
======================================================================

`Zoom: One platform to connect <https://zoom.us/>`__
  このサイトでやることは二つある。アカウント登録と Zoom Cloud Meetings インス
  トーラーのダウンロードだ。
`iVCam - Use mobile phone as a PC webcam | E2ESOFT <https://www.e2esoft.com/ivcam/>`__
  携帯電話を PC に接続してカメラ・マイクの代用にするためのアプリケーションを入手
  できる。二つの機器のどちらにもインストールすることに注意。
`パソコンの内蔵カメラやスマホをWebカメラとして使用する方法 <https://jp.norton.com/internetsecurity-etc-pc-camera.html>`__
  この文書の iVCam 周りの記述にたいへん助けられた。これを知ったので私は職探しを
  転職サイトとオンライン面接主体に移行した。
`💻 5 Best FREE Screen Recorders - no watermarks or time limits - YouTube <https://www.youtube.com/watch?v=nCNri04lHaI>`__
  Zoom を画面収録ツールとして利用する方法を紹介している。

.. _Zoom: https://zoom.us/
.. _e2eSoft iVCam: https://www.e2esoft.com/ivcam
