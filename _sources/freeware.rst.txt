======================================================================
Windows 用フリーウェア 利用ノート
======================================================================

私が作業する Windows 10 Home (64bit) コンピューターにインストールするべきソフトウェアをここに記録する。
ソフトウェアによっては、さらにモジュール、プラグイン、拡張機能などを追加的にインストールすることになる。
それらについては、ソフトウェア個別の利用ノートを綴り、そちらに重要事項を記す。

Windows 用ということで、必然的に GUI を備えるソフトが主になる。
CLI 編を本稿と対になる感じで別途作成したい。

.. contents::

ソフトウェア一覧
======================================================================

このソフトウェア一覧は環境を点検する際に参照する用途を想定している。
したがって、通称をアルファベット順に列挙する。ハイパーリンクは後ほど付与する。

* CPU-Z
* DeepL
* Dropbox
* FastStone Image Viewer
* GIMP
* Google 日本語入力
* Inkscape
* LibreOffice
* Mozilla Thunderbird
* PowerToys
* Rapid Environment Editor
* Sleipnir
* Visual Studio Code
* VLC media player
* Windows Package Manager CLI (winget)
* Windows Subsystem for Linux
* Windows Terminal
* 圧縮解凍ソフト Noah

各ソフトウェアについての見解は後述することにして、これらの効率的なインストール手順を先に述べる。

効率的なインストール手順
======================================================================

1. Windows Package Manager CLI を優先的にインストールする
2. Windows Package Manager CLI を使って自動インストールできるものをする
3. 優先度の高いソフトウェアを手動インストールする
4. その他を必要に応じて手動インストールする

Windows Package Manager CLI をインストールする
----------------------------------------------------------------------

.. note::

   関連ノート：:doc:`/winget`

資料 <https://docs.microsoft.com/ja-jp/windows/package-manager/winget/> によると、
モダンな Windows 環境には既定で利用可能になっているとあり、本節は蛇足かもしれない。
だから、まずはコンソールを開いて ``winget`` が存在するかどうかをテストする。

.. code:: doscon

   > winget --version
   v1.1.13405

ない場合はスタートメニューから Microsoft Store を起動。
『アプリ インストーラー』を選択してインストールするのだろう。

Windows Package Manager CLI を使って自動インストールする
----------------------------------------------------------------------

ここで個別にインストールするコマンドは言及しない。
現行環境から出力したインストール済みソフトウェア一覧を記した JSON ファイルから
:command:`winget` に入力してインストールさせるのが最も復元効率が良い。

.. code:: doscon

   > winget import -i winget.json

ファイル ``winget.json`` は旧環境で :command:`winget export -o winget.json`
により得られたものとする。現環境で定期的にこのコマンドを実行して、
JSON ファイルを安全な場所にバックアップしておく。

以下、この手順終了によりシステムにインストールされていることを期待するソフトウェアを記す。
状況に応じて適宜調整する。

`CPU-Z <https://www.cpuid.com/softwares/cpu-z.html>`__
    CPU-Z は次のシステムの主要器機に関する情報を収集するフリーウェアだ：
    CPU の名前と番号、コードネーム、プロセス、パッケージ、キャッシュレベル、
    メインボード、チップセット、等々。

    ノート PC を新調した直後に、メモリーを増設する際の情報を得るのに本ソフトをチェックする。

`DeepL Translator <https://www.deepl.com/ja/app/>`__
    DeepL と単に呼ぶときはこのサービスを意味することが多い。
    ショートカットキー一発で選択テキストを翻訳するプログラムだ。

    英語を日本語に翻訳させる用途でインストールしている。

`Dropbox <https://www.dropbox.com/>`__
    プログラムとしての Dropbox は、当局固有のオンラインストレージを利用するためのインターフェイスだ。
    家計簿や履歴書などの非テキストデータファイル、または機微に触れる情報を暗号化したファイルをバックアップするのに利用する。
    私はこのソフトのおかげで、ホームレスのときにノート PC を盗まれても、職探しを比較的円滑に開始することができた。

`FastStone Image Viewer <https://www.faststone.org/FSViewerDetail.htm>`__
    FastStone Image Viewer は、画像閲覧・変換・編集ソフトウェアだ。
    部分的に Photoshop 並の画像調整機能を備えている。主要なグラフィックフォーマット
    および一般的なデジタルカメラ RAW フォーマットに対応している。

    携帯電話で撮影した写真群をバッチ処理するのに利用したり、
    インターネットから crawling でダウンロートした大量の画像ファイルを目視でチェックするのにたいへん便利だ。

`GIMP <https://www.gimp.org/>`__
    GIMP は Photoshop のようなソフトウェアだ。
    ベクトル的ではない、ビットマップ的な画像の編集に用いる。

`Google 日本語入力 <https://www.google.co.jp/ime/>`__
    Google 日本語入力は Windows 組み込みの IME よりも使いやすい。
    日本語で記述するどんなテキスト作業においてもこちらを有効にするべきだ。
    本稿では扱わないが、本体とは別に辞書もセットアップするのが普通だ。

`LibreOffice <https://www.libreoffice.org/>`__
    MS Office が高くて購入できないので、フリーウェアである LibreOffice をインストールすることを余儀なくされる。
    家計簿、履歴書、職務経歴書、業務報告書などを Calc や Writer で作成し、
    MS Office 対応の各ファイル形式や PDF に変換し、人に送信したり印刷したりするという運用をしている。

`Inkscape <https://inkscape.org/>`__
    Inkscape はベクトルデータベースの描画ツールで、主に SVG 形式の画像を作成するために用いられる。
    他の形式フォーマットのインポートおよびエクスポートも可能だ。HTML 文書に添える画像を整えるのに有用だ。
    :doc:`/inkscape/index` 参照。

    このノートを書くために久しぶりに公式ページを当たったところ、メジャーバージョンがついに
    1 になっていて驚く。

`Mozilla Thunderbird <https://www.thunderbird.net/>`__
    Thunderbird は有名なメールクライアントだ。
    設定やカスタマイズが簡単であり、環境の移行作業にも考慮がなされている。
    仕事探しにメールをどうしても利用するので、手放せない。

`PowerToys <https://docs.microsoft.com/ja-jp/windows/powertoys/>`__
    PowerToys は Microsoft 製上級利用者向け便利ツール詰め合わせソフトウェアだ。
    本稿執筆時点では Always on Top, Awake, Color Picker, FancyZones, File
    Explorer add-ons, Image Resizer, Keyboard Manager, Mouse Utility,
    PowerRename, PowerToys Run, Quick Accent, Screen Ruler, Shortcut Guide, Text
    Extractor, Video Conference Mute の連合ソフトだ。

    これだけあれば、上級者でなくても常用できそうな機能が何かあるのが自然だ。
    ぜひインストールしたい。

`Rapid Environment Editor <https://www.rapidee.com/en/about>`__
    Windows 環境変数編集ソフトウェア。インターフェイスがとにかく秀でいている。
    パスの編集が容易という理由だけで導入する価値がある。

    最近は WSL 環境で各種開発をすることが激増し、Windows の環境変数を編集する機会が激減したため、
    当ソフトウェアをインストールする優先度は以前より下がった。

`Ubuntu (WSL) <https://releases.ubuntu.com/>`__
    ここでいう Ubuntu は WSL を有効化してからの Linux ディストリビューションとしてのそれだ。
    本環境については考慮する点が多数あるため、専用のノートを設けてそこで詳述する予定だ。

`Visual Studio Code <https://azure.microsoft.com/ja-jp/products/visual-studio-code/>`__
    私の現時点でのメインテキストエディター。
    本プログラムについても注意点が多数あるので、専用ノートに要点を述べていく予定だ。

`VLC media player <https://www.videolan.org/>`__
    VLC media player はマルチメディアファイルのほとんどと、さまざまなストリーミングプロトコルを再生できる、
    無料でオープンソースのプレーヤーでありフレームワークだ。
    主に MP3 や MP4 などのオーディーオやビデオファイルのプレイリストを作成、視聴するのに活躍している。

`Windows Terminal <https://docs.microsoft.com/ja-jp/windows/terminal/>`__
    Windows Terminal はタブブラウザーならぬタブコンソールだ。
    かつて私が愛用していた ConEmu と目的意識を共有していると思われる。

優先度の高いソフトウェアを手動インストールする
----------------------------------------------------------------------

ソフトウェアを自動的にインストールできないということは、配布ページにアクセスし、
用意されているインストーラーを手動でダウンロードして実行することを意味する。この
場合、なるべく 64 ビット版を見つけて実行すること。それが提供されていない場合にの
み 32 ビット版を使う。

繰り返しになるが、ここに列挙されるソフトウェアの順序はインストール優先度を意味しない。

`Sleipnir <https://www.fenrir-inc.com/jp/sleipnir/>`__
    愛用のウェブブラウザー。Google Chrome を子ウィンドウとするタブブラウザーと解釈される。
    ブックマークを作り込み過ぎて、本家 Google Chrome や Mozilla Firefox
    などの有力ブラウザーに乗り換えらるのが億劫だ。
    それゆえ、インストールの優先度は私の中では相当高い。
    RSS ビューワーもあるし、当分このままでいるのが吉だろう。

`Windows Subsystem for Linux <https://docs.microsoft.com/ja-jp/windows/wsl/install>`__
    WSL と略称で呼称するのが一般的だ。Windows で Linux を使えるようになる何かだ。
    私はテキストベースの執筆物および創作物をこの上でバージョン管理しているため、
    インストールの優先度はきわめて高い。

    Cygwin 利用時代のドットファイルや関数群を流用できているのもうれしい。

    このシステムについてはまだまだ理解が不足しているので、別途学習してノートにする予定だ。

その他を必要に応じて手動インストールする
----------------------------------------------------------------------

以下のソフトウェアは急いでインストールする必要はないものだ。

`圧縮解凍ソフト Noah <http://www.kmonos.net/lib/noah.ja.html>`__
    エクスプローラーのコンテキストメニューから圧縮ファイルを解凍したり、
    逆にファイルやフォルダーを圧縮できたりする。
    あくまでも利便性があるというだけであって、解凍・圧縮操作をするだけならば
    WSL 環境で実現できる。そのための別名定義なり、シェル関数なりを用意してあるはずで、
    そちらを採用するほうが便利である場合もある。
    そういう意味で、本ツールのインストール優先度は高くない。

ゲームプログラムについては、セーブデータなどがあるため一からダウンロードすることは稀だ。
一般論をバックアップノートで述べる。
