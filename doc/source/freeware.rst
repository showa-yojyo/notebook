================================================================================
Windows 用フリーウェア利用ノート
================================================================================

.. |WSL| replace:: :abbr:`WSL (Windows Subsystem for Linux)`
.. |winget| replace:: :program:`winget`

私が作業する Windows (64 bit) コンピューターにインストールするべきソフトウェアを
ここに記録する。ソフトウェアによっては、さらにモジュール、プラグイン、拡張機能な
どを追加的にインストールすることになる。それらについては、ソフトウェア個別の利用
ノートを綴り、そちらに重要事項を記す。

Windows 用ということで、必然的に GUI を備えるソフトが主になる。本稿と対になる感
じで CLI 編をいずれ執筆したい。

.. contents:: 見出し一覧
   :local:

ソフトウェア一覧
================================================================================

このソフトウェア一覧は環境を点検する際に参照する用途を想定している。したがって、
通称をアルファベット順に列挙する。

* CPU-Z
* DeepL
* Draw.io
* FastStone Image Viewer
* GIMP
* Google 日本語入力
* Inkscape
* LibreOffice
* Mozilla Thunderbird
* OBS Studio
* pCloud Drive
* PowerToys
* Rapid Environment Editor
* Sleipnir
* SumatraPDF
* Visual Studio Code
* VLC media player
* Windows Package Manager CLI (|winget|)
* |WSL|
* Windows Terminal
* Zoom Workplace

各ソフトウェアについての見解は後述することにして、これらの効率的なインストール手
順を先に述べる。

効率的なインストール手順
================================================================================

1. Windows Package Manager CLI (|winget|) を優先的にインストールする
2. Windows Package Manager CLI を使って自動インストールできるものをする
3. 優先度の高いソフトウェアを手動インストールする
4. その他を必要に応じて手動インストールする

Windows Package Manager CLI をインストールする
--------------------------------------------------------------------------------

.. seealso::

   :doc:`/winget`

資料 <https://docs.microsoft.com/ja-jp/windows/package-manager/winget/> による
と、モダンな Windows 環境には既定で利用可能になっている。まずはコンソールを開い
て |winget| が存在するかどうかをテストする。

.. sourcecode:: ps1con
   :caption: |winget| のバージョンを確認する

   PS> winget --version
   v1.29.380

Windows Package Manager CLI を使って自動インストールする
--------------------------------------------------------------------------------

ここで個別にインストールするコマンドは言及しない。現行環境から出力したインストー
ル済みソフトウェア一覧を記した JSON ファイルから |winget| に入力してインストール
させるのが最も復元効率が良い。

.. sourcecode:: ps1con
   :caption: |winget| による一括インポートコマンド例
   :force:

   PS> winget import -i winget.json

ファイル :file:`winget.json` は旧環境で ``winget export -o winget.json`` により
得られたものとする。現環境で定期的にこのコマンドを実行して、JSON ファイルを安全
な場所にバックアップしておく。

インポートではなく、ソフトウェアを一つずつインストールする場合にはコマンド
``winget install`` を実行することになる。このとき、ユーザーインストールではなく、
システムインストールが望ましい。オプション ``--scope machine`` を可能な限り付けろ。

以下、この手順終了によりシステムにインストールされていることを期待するソフトウェ
アを記す。状況に応じて適宜調整する。

`CPU-Z <https://www.cpuid.com/softwares/cpu-z.html>`__
    CPU-Z は次のシステムの主要器機に関する情報を収集するフリーウェアだ：
    CPU の名前と番号、コードネーム、プロセス、パッケージ、キャッシュレベル、メイ
    ンボード、チップセット、等々。

    ノート PC を新調した直後に、メモリーを増設する際の情報を得るのに本ソフトを
    チェックする。
`DeepL Translator <https://www.deepl.com/ja/app/>`__
    DeepL と単に呼ぶときはこのサービスを意味することが多い。ショートカットキー一
    発で選択テキストを翻訳するプログラムだ。

    英語を日本語に翻訳させる用途でインストールしている。

    .. seealso::

       :doc:`/deepl-translator`
`Draw.io <https://www.drawio.com/>`__
    図式製図ツール。モダンな UML 図式をどうしても描画したい場合に使い物になる
    ツールがこれしかなかった。
`FastStone Image Viewer <https://www.faststone.org/FSViewerDetail.htm>`__
    FastStone Image Viewer は、画像閲覧・変換・編集ソフトウェアだ。部分的に
    Photoshop 並の画像調整機能を備えている。主要なグラフィックフォーマットおよび
    一般的なデジタルカメラ RAW フォーマットに対応している。

    携帯電話で撮影した写真群をバッチ処理するのに利用したり、インターネットから
    crawling でダウンロートした大量の画像ファイルを目視でチェックするのにたいへ
    ん便利だ。
`GIMP <https://www.gimp.org/>`__
    GIMP は Photoshop のようなソフトウェアだ。ベクトル的ではない、ビットマップ的
    な画像の編集に用いる。

    2025 年になって GIMP のメジャーバージョンが 3 に上がった。

    .. seealso::

       `GIMP 3 利用ノート <https://gist.github.com/showa-yojyo/92e9935e7b13b06c324607136174baa2>`__
`Google 日本語入力 <https://www.google.co.jp/ime/>`__
    Google 日本語入力は Windows 組み込みの IME よりも使いやすい。日本語で記述す
    るどんなテキスト作業においてもこちらを有効にするべきだ。本稿では扱わないが、
    本体とは別に辞書もセットアップするのが普通だ。

    .. seealso::

       :doc:`/google-ime`
`Inkscape <https://inkscape.org/>`__
    Inkscape はベクトルデータベースの描画ツールで、主に SVG 形式の画像を作成する
    ために用いられる。他の形式フォーマットのインポートおよびエクスポートも可能
    だ。HTML 文書に添える画像を整えるのに有用だ。

    .. seealso::

       :doc:`/inkscape/index`
`LibreOffice <https://www.libreoffice.org/>`__
    MS Office が高くて購入できないので、フリーウェアである LibreOffice をインス
    トールすることを余儀なくされる。家計簿、履歴書、職務経歴書、業務報告書などを
    Calc や Writer で作成し、 MS Office 対応の各ファイル形式や PDF に変換し、人
    に送信したり印刷したりするという運用をしている。

    .. seealso::

       `LibreOffice 関連ノート <https://showa-yojyo.github.io/libreoffice-notes/>`__
`Mozilla Thunderbird <https://www.thunderbird.net/>`__
    Thunderbird は有名なメールクライアントだ。設定やカスタマイズが簡単であり、環
    境の移行作業にも考慮がなされている。仕事探しにメールをどうしても利用するの
    で、手放せない。
`OBS Studio <https://obsproject.com/>`__
    デスクトップ録画ソフトウェアとして利用する。

    .. seealso::

       `OBS Studio 利用ノート <https://gist.github.com/showa-yojyo/6bdb84aafa72e0a43214e0be4bc531e2>`__
`pCloud Drive <https://www.pcloud.com/>`__
    Dropbox のようなオンラインストレージサービス。無料使用者でも努力次第では容量
    を 10 GB まで拡大可能。

    以前は pCloud と Dropbox を併用していたが、後者の Windows サービスプログラム
    がメモリーを食い、それを改善することができなかったので前者に一本化した。
`PowerToys <https://docs.microsoft.com/ja-jp/windows/powertoys/>`__
    PowerToys は Microsoft 製上級利用者向け便利ツール詰め合わせソフトウェアだ。
    特に Peek のビューワーを気に入っている。File Locksmith も障害狙撃時に有用
    だ。他にも、上級者でなくても常用できそうな機能が何かとある。ぜひインストール
    したい。

    .. seealso::

       :doc:`/powertoys/index`
`Rapid Environment Editor <https://www.rapidee.com/en/about>`__
    Windows 環境変数編集ソフトウェア。インターフェイスがとにかく秀でている。パス
    の編集が容易という理由だけで導入する価値がある。

    最近は |WSL| 環境で各種開発をすることが激増し、Windows の環境変数を編集する
    機会が激減したため、当ソフトウェアをインストールする優先度は以前より下がった。
`SumatraPDF <https://www.sumatrapdfreader.org/free-pdf-reader>`__
    軽量 PDF ビューワー。一度これを使うと Adobe Acrobat Reader を使う気にならな
    くなる。
`Visual Studio Code <https://azure.microsoft.com/ja-jp/products/visual-studio-code/>`__
    私の現時点でのメインテキストエディター。本プログラムについても注意点が多数あ
    るので、専用ノートに要点を述べていく。

    .. seealso::

       :doc:`/vscode/index`
`VLC media player <https://www.videolan.org/>`__
    VLC media player はマルチメディアファイルのほとんどと、さまざまなストリーミ
    ングプロトコルを再生できる、無料でオープンソースのプレーヤーでありフレーム
    ワークだ。主に MP3 や MP4 などのオーディーオやビデオファイルのプレイリストを
    作成、視聴するのに活躍している。

    .. seealso::

       :doc:`/vlc-media-player`
`Zoom Workplace <https://zoom.us/>`__
    略称は Zoom だ。これはオンライン会議ツールだ。転職サイトの求人応募時には面接
    でこれを使いがちだ。画面撮影ツールとして応用することもある。

    .. seealso::

       :doc:`/zoom`

優先度の高いソフトウェアを手動インストールする
--------------------------------------------------------------------------------

ソフトウェアを自動的にインストールできないということは、配布ページにアクセスし、
用意されているインストーラーを手動でダウンロードして実行することを意味する。この
場合、なるべく 64 ビット版を見つけて実行すること。それが提供されていない場合にの
み 32 ビット版を使う。

繰り返しになるが、ここに列挙されるソフトウェアの順序はインストール優先度を意味し
ない。

`Sleipnir <https://www.fenrir-inc.com/jp/sleipnir/>`__
    愛用のウェブブラウザー。Google Chrome を子ウィンドウとするタブブラウザーと解
    釈される。ブックマークを作り込み過ぎて、本家 Google Chrome や Mozilla
    Firefox などの有力ブラウザーに乗り換えらるのが億劫だ。それゆえ、インストール
    の優先度は私の中では相当高い。RSS ビューワーもあるし、当分このままでいるのが
    吉だろう。

    .. seealso::

       * `Sleipnir 6 よくある質問ノート
         <https://gist.github.com/showa-yojyo/e5005e744e79258d0a23969eba93c3e7>`__
       * `Sleipnir 6 障害狙撃ノート
         <https://gist.github.com/showa-yojyo/d39db3230d8baefc2b3bcaa897d55596>`__
`Windows Subsystem for Linux <https://docs.microsoft.com/ja-jp/windows/wsl/install>`__
    |WSL| と略称で呼称するのが一般的だ。Windows で Linux を使えるようになる何か
    だと考えていればいい。

    テキストベースの執筆物および創作物をこの上でバージョン管理するため、インス
    トールの優先度はきわめて高い。Cygwin 利用時代から使い込んできたドットファイ
    ルや関数群を流用できているのもうれしい。

    .. seealso::

       * :doc:`/wsl`
       * `WSL Documentation 読書ノート
         <https://gist.github.com/showa-yojyo/07644b4ded83b434589affdf6dcccfb4>`__
