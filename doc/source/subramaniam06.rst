======================================================================
アジャイルプラクティス 読書ノート
======================================================================

ソフトウェア開発本として Joel 本の次に買った記憶がある。

.. include:: /_include/book-details/subramaniam06.txt

.. contents:: ノート目次

目次以前のローマ数字ページ
======================================================================

* 扉ページの絵画はヒエロニムス・ボスあたりの作品か。
* ティルヴァックヴァルとやらの警句。これは何国語の文字だろうか。

第 1 章
======================================================================

この短い章は、本書のイントロダクションの役割を果たす。

* アジャイルは <重要度の高い事柄に注力し、重要度の低い事柄（略）には労力を割かな
  いようにする方法論> (p. 2) である。
* <ソフトウェア開発は継続的なものなんだ。フィードバックも継続的だ> (p. 3)
* 囲み記事「アジャイルツールキット」は必読。 Wiki を筆頭にバージョン管理、ユニッ
  トテスト、ビルド自動化を挙げている。以前読んだ Joel Test と主張の方向性は同じ
  だと思う。

第 2 章
======================================================================

* 冒頭から <ソフトウェア開発の方法論をテーマとした従来の書籍でよくある説明の流れ
  はこうだ。 （略）本書はこうした流れに従わない> (p. 11) と、威勢がよい。
* <ソフトウェア開発が本当に行われる場所は、チャートや IDE や設計ツールの中ではな
  い。人の頭の中だ> (p. 11)

1
----------------------------------------------------------------------

* <チームの多数の振る舞いがプロ意識に欠けていて、チームの運営に無関心な場合は、
  自分自身がチームを離れてよそで成功を目指すべきだ> (p. 15)

2
----------------------------------------------------------------------

* <実際に髪が薄くなった開発者が何人もいた> (p. 16)
* <差し迫った状況で問題の本質や起こり得る結果をきちんと理解することなく、手っ取
  り早く加えた修正> (p. 17)
* <単独行動は危険だ。開発者が独りきりでコードを書くことがないようにしよう>
  (p. 17) これを予防するにはやはりバージョン管理、コードレビュー、ユニットテスト。
* <ユニットテストに慣れれば、コードは自然と扱いやすい単位で構造化される> (p. 17)

3
----------------------------------------------------------------------

セクション冒頭でいきなり悪魔が話しかけてくる。斬新な演出だ。

* <思いついたアイデアをチームの誰もが自由に表現できる雰囲気が必要> (p. 21)
* 囲み記事のタイトル <全員一致でラクダが生まれた> (p. 21) がインパクト大。

  * <とりわけ優れた斬新なアイデアというものは 1 人の頭脳、
    すなわち確固たるヴィジョンを持った個人から出てくるものだ> (p. 21)

* <設計とは妥協の連続だ> (p. 22)
* <主張している事態がどれだけ可能性があることなのかを併せて評価しなければならな
  い。主張を裏付けたり、反論したりするためにプロトタイプや調査が必要であれば、そ
  うすればいい> (p. 23) やはり裏は取りたいものだ。
* メンバー全員の「その状況におけるベストとは何か」の認識を合わせておく。

4
----------------------------------------------------------------------

* どうしてもコードをゼロから作り直したければ、<今のコードを捨てて書き直したほう
  が費用対効果が高いことを明確に示そう（口頭で伝えるだけでは不十分だ）> (p. 24)

  * 著者の例が囲み記事内に挙げられている：<こんなコードではすぐにメンテナンスの
    コストが大きくなりすぎて保守できなくなります> (p. 24)
  * <「コードがすっきりするから」では、経営陣や事業家に納得してもらえる理由にな
    らない。費用の節約、投資収益率の向上、訴訟の回避、顧客基盤の拡張といった理由
    のほうが適切だ> (p. 26) 意思決定者がビジネス寄りの人間ならば、こういう毛色の
    用語を駆使して丸め込むるのがコツか。

第 3 章
======================================================================

時代に乗り遅れないようにアジャイル。

* <ほとんどの考え方はあっという間に時代遅れになってしまう> (p. 27)
* <時代遅れの古びた手法と決別することも重要だ> (p. 27)

5
----------------------------------------------------------------------

* <何やらインターネットとかいう代物も話題になっていた> (p. 29) 1995 年が懐かしい
  ような。
* <**イテレーティブかつインクリメンタルに学習する**> (p. 30)
* <定評のある技術系ブログ> (p. 30) はみんな見ているから、
  自分だけ見ていないと思うと恐ろしいことになる？
* <非技術系の良書> (p. 30) どこから外側が非技術系なのだろうか。関係ないが、本を
  読む以前に、身銭を切って本を買うのを避けている。
* <新技術は、採用を決める前にそのメリットをきちんと評価しなければならない>
  (p. 31)

6
----------------------------------------------------------------------

* <もし自分が一番上手いんだとしたら、それは別のバンドに移る時だ> (p. 32) という
  某ジャズギタリストの至言は心を打つねえ。
* <『一週間でおぼえる XYZ 入門―パターンと UML で完璧マスター！』といったタイトル
  の書籍は十中八九、読書会向きじゃない> (p. 32) いかにもありそうなタイトルで笑え
  る。あくまで読書会向きじゃないだけで、読むなとは言っていない、はず。

7 時が来たら習慣を捨てる
----------------------------------------------------------------------

* <変化への対応> (p. 35)
* <現代では開発者の時間こそが貴重な（しかも高くつく）リソースなのだ> (p. 36)
* <古い習慣に気づくのはそれに輪をかけて難しい> (p. 36)
* <例えば、新しいプログラミング言語を学ぶとしよう。この場合は、その言語用の新し
  い IDE を使うようにする> (p. 37) まったく耳が痛い。
* <これまで経験した言語で使い慣れた独特の特徴にはとりわけ注意を払い、新しい言語
  や新バージョンでは、互いの類似点や同意点を学ぼう> (p. 37)

8 わかるまで質問する
----------------------------------------------------------------------

* <質問をする前に、そう問う根拠を考えておくこと。事前に考えておくことには、質問
  と問題との関連を確実にする効果もある> (p. 40)

9
----------------------------------------------------------------------

* <アジャイルプロジェクトにはリズムと周期がある。このおかげで物事を進めやすく
  なっている> (p. 41)
* <一日の終わりにチェックインされているコードはすべてテストされているように計画
  を立てよう> (p. 43) チェックインというのはコミットのことだと思うが、これは難し
  い。

第 4 章
======================================================================

* <避けて通れない敵とは、変化だ> (p. 45)

10 顧客に決断してもらう
----------------------------------------------------------------------

* <自分たちが決定すべきでないことは何かを決定する> (p. 48)

11
----------------------------------------------------------------------

* <こうした作業を経てはじめて、コーディングに着手できるレベルの構造にたどり着け
  るのだ。事前に考える手間を省いてしまったら、いざコーディングに取りかかるや否
  や、想定外の問題に圧倒されてしまうかもしれない> (p. 50)
* <川岸にたどり着かないうちから、川の浅瀬を渡る方法の詳細を考えるなんて時間の無
  駄だ。実際に川岸にたどり着いてからのほうが適切に判断できるだろう> (p. 52) 一瞬
  わけがわからなかったが、川岸というのは手前側の川岸か。
* <「設計する」という行為そのものに、何者にも代えがたい価値がある> (p. 53)

12 技術の採用根拠を明らかにする
----------------------------------------------------------------------

* <職務経歴書駆動設計> (p. 54) とはいい言い方だ。
* <あまりにもごった煮すぎた> (p. 55)
* <ダウンロードできるものを開発するな> (p. 55)

13 いつでもリリースできるようにしておく
----------------------------------------------------------------------

* <チェックイン済みのコードは常に動作可能な状態にする> (p. 57) システム開発の本
  ならば必ずこの一文が書いてあるとみた。
* <継続的インテグレーションといっても、小難しく考えることはない。要するに、コー
  ドのチェックアウト、ビルド、テストをバックグラウンドで定期的に実行するだけのア
  プリケーションだ。スクリプトを書いて自作するのも簡単だが、既存のフリーでオープ
  ンソースなツールを使ったほうが、動作も安定しているし機能も充実している>
  (p. 58)

14
----------------------------------------------------------------------

* <統合はソフトウェア開発で特にリスクが大きい領域のひとつだ> (p. 61)

15 早いうちにデプロイを自動化する
----------------------------------------------------------------------

* <少し時間をとってプロセスの自動化を検討してみよう。これはエンドユーザ向けの本
  格的なインストールシステムを作るときのベースにもなる> (p. 64)
* 囲み記事で本項目の主張を補強する。

  * <初日どころかプロジェクトの開始前に、全面的に自動化されたインストール手順を
    用意してしまうプロジェクトすら実在する> (p. 65)

* <ユーザがいつでもインストール内容を安全かつ完全に削除できるようにしておくこと>
  (p. 66)

16
----------------------------------------------------------------------

* 囲み記事 (p. 70) のプロジェクト用語集の有意性についての議論は説得力がある。
  チームのメンバー同士でも専門用語の解釈が違っていることがある。
* <仕事の都合で月に 1 回しか打ち合わせできないなら、その頻度でやるしかない>
  (p. 71)

17
----------------------------------------------------------------------

* <大規模なプロジェクトのほうが失敗しやすい> (p. 72)
* <だったら単一の大規模アプリケーション開発をやめればいい！アプリケーションを使
  える単位で小さく分けて作る――つまり、インクリメンタルに開発するんだ> (p. 73)
* <プロジェクトの完了まであと 1 年あると言われたら、なんだか余裕があるような気が
  するだろう？> (p. 74)
* <メンテナンスを済ませてから、次のイテレーションを開始するのだ> (p. 75)

18 定額契約は守れない約束
----------------------------------------------------------------------

このタイトルは傑作。

* 見積もりは実作業を基準に見積もるしかない。

第 5 章
======================================================================

19
----------------------------------------------------------------------

* <変数が期待値どおりであることをテストするコードは共通化できる。テストをどれだ
  け実行したか管理するコードも共通化できる。こうしたテストの作成や構成といった低
  レベルの雑多な処理には、標準的なフレームワークを使えばいい> (p. 81)
* <ビルド用マシンでは、常に最新バージョンのソースコードを取得してコンパイルし、
  ユニットテストを実行させる。実行結果が想定外のものだった場合には、直ちに通知さ
  せるようにする。この作業をバックグラウンドで実行できるようにしておく> (p. 82)
* <自動化されたユニットテストを習慣にしなさい> (p. 84) ああ、エンジェルの言うと
  おりだ。
* <アクセサや、結果が自明なメソッドのテストには、そんなに時間をかけなくてもいい
  だろう> (p. 84)

20 作る前から使う
----------------------------------------------------------------------

冒頭のドッグフードの話に既視感を覚えた。何だったかな。

* TDD は Test Driven Development - テスト駆動開発の略。<TDD では、コードを書くこ
  とが許されるのは、失敗するユニットテストを書いた後だけだ。そして、必ずテストを
  先に書かなければならない（テストファースト）> (p. 86)
* <真のポイントは、「目的の機能をきちんと果たす実装に必要な最小限の作業」を見つ
  けだすことだ> (p. 89)
* <TDD では（略）どれぐらい便利なのかや、使い勝手についても考えることになるの
  で、結果としてより実用的な設計にたどり着けるというわけだ> (p. 89)

21
----------------------------------------------------------------------

* <どうにかして突き止めた犯人は、プラットフォームによる .NET API の挙動の違い
  だった。 Windows XP と Windows Server 2003 とでは挙動が異なるのだ> (p. 91)
  Win32 API ではあるが、まさにここに書いてあるような経験をした。これを読む前だっ
  たら、こういうことが起こるものだと知らずに、パニックになっていたかもしれない。
* <複数のプラットフォームでテストしたければ、プラットフォームごとに継続的インテ
  グレーションツールをセットアップすればいい> (p. 92)
* <いまどきビルド用マシンのハードウェアの価格なんて、開発者の時給に換算すれば
  たったの数時間分だ。VMWare や Virtual PC のような製品を使って複数バージョンの
  オペレーティングシステム、VM、CLR を単一のマシンで走らせて、さらにハードウェア
  コストを節約してもいい> (p. 92) とあるが、マシンを置く場所がない。
* <ハードウェアよりも開発者の時間のほうが貴重だ> (p. 93)

22
----------------------------------------------------------------------

開発中に、顧客の「実データ」が喉から手が出るほど欲しいことはよくある。しかし、ま
ずそのようなものは貸してくれない。その理由は単純だった。<もう既に正しいデータを
入手できるのだとしたら、新しいシステムなんで別に必要ないのだから> (p. 95)

23
----------------------------------------------------------------------

* <「今日の進捗率は 80 パーセントです」みたいな報告を耳にしたことはないだろう
  か？何日たっても何週間たっても、ずっと進捗率は 80 パーセントのまま> (p. 97)
  確かにこういう構成員がいる。報告書が前回のコピペだったりする。
* <バックログは複数あっていい> (p. 98) 本物は一つでいい。

24
----------------------------------------------------------------------

なぜ開発者は <ユーザーの声にきちんと耳を傾ける> (p. 101) のを忘れがちなのか。そ
の辺の見解が欲しい。

第 6 章
======================================================================

コーディングに関連するトピックをあつめた章だ。

25 意図を明確に表現するコードを書く
----------------------------------------------------------------------

* <じゃあ、2 は何だろう？ 2 杯？ 2 ショット？それともカップのサイズ？> (p. 106)
* <小賢しいコード> (p. 108) というフレーズが気に入った。

26
----------------------------------------------------------------------

* <ソースコードのわかりやすさとはコメントによるものではない。コード自身のエレガ
  ントさと明瞭さによるものであるべきだ> (p. 110)

27 トレードオフを積極的に考慮する
----------------------------------------------------------------------

* <とはいえ、そこそこ性能の出ているアプリケーションの速度をさらに追求する必要は
  あるだろうか？たぶんない> (p. 115)
* <予断は禁物だ。実際に確認すること> (p. 117)

28 インクリメンタルにコードを書く
----------------------------------------------------------------------

「インクリメンタルにホニャララする」という見出しがいい。

* エンジェルが <コードを書くときは編集・ビルド・テストのサイクルを短くしなさい>
  (p. 118) と言っているが、そんなことは承知している。短くできないから困るンだ。

29
----------------------------------------------------------------------

* <何か引っかかるものを感じたら、それは「どこか間違っているからだ」と考えるんだ>
  (p. 121)

30 凝集度の高いコードを書く
----------------------------------------------------------------------

右ページの家具のお化けみたいなイラストがインパクト大。

* <例えば、洋服がすべて同じ引き出しに放り込まれているとしよう。靴下を探すにも、
  ズボンやら下着やら T シャツやら、ほかの衣類を引っかき回さなければならない。こ
  れは非常にいらいらする> (p. 122)
* <このアプリケーションでは、画面のそれぞれは HTML だが、データベースにアクセス
  するための埋め込み SQL 文といっしょに、相当な量の VBScript が組み込まれていた>
  (p. 123)
* 「単一責任の原則」と「再利用の単位とリリースの単位の等価性」を調べること。

32
----------------------------------------------------------------------

* リスコフの置換原則とは <要するに、基底クラスのメソッドを使っているコードは、
  コードの修正なしに派生クラスのオブジェクトを扱えなければいけない> (p. 129)
* <「委譲だとメソッド呼び出しを転送する小さなメソッドを大量に書かないといけなく
  なる」という意見もあるだろう。（略）しかし、だからといってそんな理由で継承を使
  うのは間違いだ> (p. 131)

第 7 章
======================================================================

<デバッグは時間を読めない> (p. 133)

33
----------------------------------------------------------------------

* <古来、エンジニアはそうやってきたのだ。彼らはそれを **開発メモ** と呼んでいる>
  (p. 134)

34
----------------------------------------------------------------------

* <どんな警告も無視されないように、一番厳しい設定にしよう。 GCC には ``-Werror``
  オプションがある。Visual Studio なら、プロジェクト設定を変更すれば警告をエラー
  として扱える> (p. 137) 趣旨には大賛成だが、実際はよそのライブラリーをインク
  ルードするところで警告が出るのでやらない。
* 当節の助言・忠告にすべて従うと、<警告が（略）警告のように感じられる> (p. 138)
  ようになる。
* <インタープリタ言語にも通常は実行時の警告を有効にするオプションがある> (p. 138)

35 問題を切り分けて攻める
----------------------------------------------------------------------

* <コードが他のモジュールに依存しているなら、モックオブジェクトを使って余計なモ
  ジュールから分離する> (p. 140) と、ユニットテストしやすいコードとなる。ピンと
  こない説明だ。

36 あらゆる例外を報告する
----------------------------------------------------------------------

* <もし回復できなかったとしても、何が悪かったのかをコードの呼び出し元へと適切に
  知らせることができたら、それもやっぱりすばらしい。しかし、いつもそうであるとは
  限らない> (p. 143)
* <この例外を空の ``catch`` ブロックで握りつぶし、代わりに null を返していた。こ
  れではヴェンカットの呼び出し元コードからは、何が起きているのか知りようがない>
  (p. 143)
* <対処できない例外は伝播させること> (p. 144)

どの言語でも例外のハンドリング方針は同じようだ。

37
----------------------------------------------------------------------

* <ログだけでは十分ではない> (p. 145) ユーザーにもメッセージを送る。
* 囲み記事のエラー種類の分類は、「解決できるのが誰なのか」による分類になってい
  る。

第 8 章
======================================================================

再びチームワークの話題。

38
----------------------------------------------------------------------

* つっ立ったままでミーティングを進めると、短時間で済ませられる。
* ミーティングの各参加者の発言内容は、きのうの作業内容、今日の作業予定、問題点の
  三つに絞る。さらに、発言時間を定数時間に制限する。これで会議が長引かない。
* <出勤時間の 30 分から 1 時間後に始めるのが適切だろう> (p. 154)
* <スタンドアップミーティングが待ち遠しい> (p. 155) そんなヤツはいないだろう。

39
----------------------------------------------------------------------

* <PowerPoint でコードは書けない> (p. 157) には笑った。
* <こういう設計者は現場では役に立たないことが多いしね> (p. 157) 「現場で」役に立
  たないなら、どこで役に立つのだ。

40
----------------------------------------------------------------------

* <大規模プロジェクトでは、全員がてんでバラバラに変更していては大混乱を招くこと
  になる> (p. 161)
* <コードの共同所有を避けたほうがいい特殊な状況もある。（略）コードを書くのに専
  門的で特別な知識が要求される場合がそうだ> (p. 161) 専門的で特別な知識が要求さ
  れない場合とは？

41
----------------------------------------------------------------------

* <質問に答えられなければ、そこが自分の不得意な分野だとわかる。その分野こそ、自
  分がもっとよく学ばねばならない分野だ> (p. 162)

43
----------------------------------------------------------------------

* <開発者が分散していたりオフショアだったりするので、バージョン管理システムへの
  アクセスが遅い、というのはよくある言い訳だ> (p. 166)
* ちょっと長いが、正確にノートしておこう。<通常、チェックインするファイルは特定
  のタスクや修正済みのバグに関係している。チェックインは意味のあるまとまりで行
  う。チェックイン時には意味のあるログメッセージを書くこと。ログメッセージは将来
  の誰かに向けたものだ。どのファイルを変更したか、そしてなぜ変更したのか（これが
  重要）を伝えるためだ。コミットをアトミックに、すなわち論理的にはこれ以上分割で
  きない最小単位でコミットしていれば、変更をロールバックする必要に迫られたとして
  も困らない。コードをチェックインする前には、すべてのユニットテストが通ることを
  確認しておこう。継続的インテグレーションを実践していれば、バージョン管理システ
  ムに登録されているコードが正常かどうかを簡単に確認できる> (p. 167)

44
----------------------------------------------------------------------

* <コードレビューをやりっぱなしにしないこと> (p. 171)

第 9 章
======================================================================

9.3
----------------------------------------------------------------------

* <取り入れるプラクティスは、スタンドアップミーティングから始めよう> (p. 178)
* 開発インフラの整備として「達人プログラマースターターキット」三点セットを採用す
  る (p. 178):

  * バージョン管理
  * ユニットテスト
  * ビルドの自動化

付録以降のページ
======================================================================

* [GHJV95] の著者陣リストで、Ralph Johnson と Erich Gamma の間にカンマが要る。
* 天使の助言集だが、もう少し活字が大きいと読みやすい。
