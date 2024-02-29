======================================================================
Calc Guide Chapter 10 Data Analysis ノート
======================================================================

.. contents::
   :local:

Introduction
======================================================================

関連機能はメインメニュー :menuselection:`&Data` と :menuselection:`&Tools` に分
散している。

Consolidating data
======================================================================

複数のワークシートに散在しているデータを結合して集計する機能として
:menuselection:`&Data --> &Consolidate...` コマンドがある。これを実行すると
:guilabel:`Consolidate` ダイアログが開く。この使い方が自力ではわからない。

* :guilabel:`&Function` ドロップダウンリストから所望の集計関数を指定する。
* :guilabel:`&Source data ranges` 欄を指定する。それから :guilabel:`Add` ボタン
  を押して選択範囲を :guilabel:`Consolidation ranges` 一覧に追加する。この追加処
  理を所望の範囲をカバーするまで反復する。
* :guilabel:`Copy results &to` 欄を指定する。

:guilabel:`OK` を押して処理を実行する。指定した場所にある値を集計関数に入力とし
て渡して評価し、指定した場所に出力する。

Consolidation settings
----------------------------------------------------------------------

ダイアログ上のプラスマークをクリックすると、詳細オプション項目群が現れる。

ラベル系オプションは選択範囲それぞれの最初の列や最初の行がフィールドである場合、
かつそれらがすべて一致している場合にはオンにするのが自然だろう。

:guilabel:`&Link to source data` をオンにすると、:guilabel:`&Source data ranges`
の値が変化すると :guilabel:`Copy results &to` の値も自動的に更新される。

Consolidation example
----------------------------------------------------------------------

ガイド本文のデータを手で再現して Consolidation コマンドの動作を体で理解しろ。

   The source ranges and target range are saved as part of the document. If you
   later open a document with consolidated ranges, they will still be available
   in the Consolidation ranges list of the Consolidate dialog.

Creating subtotals
======================================================================

小計を得る方法は二つだ：

* ``SUBTOTAL`` 関数
* :menuselection:`&Data --> Sub&totals...` コマンド

Using the ``SUBTOTAL`` function
----------------------------------------------------------------------

``SUBTOTAL`` 関数は Function Wizard の数学区分とサイドバーの関数デッキの下に一覧
されている。本関数はわずかな区分だけで使用する場合に効果的だ。

ガイド本文のデータを手で再現して Sales Value の列の下のセルに ``SUBTOTAL`` 呼び
出しを埋める。急所は、自動フィルターで例えば Employee を Brigitte に絞り込むと、
それに応じて ``SUBTOTAL`` の値が更新されることにある。

* ``SUBTOTAL`` の第一引数の謎数値が計算の種類を指す。
* 列の下に出力セルを設けると、当然だが自動フィルター適用時にそれが隠れる。
  ``SUBTOTAL`` の動作を試すときにはどう絞り込んでも隠れないセルに書け。

The Subtotals tool
----------------------------------------------------------------------

コマンドのほうはラベル付きの列に配置された高々三つの配列の小計を実行可能だ。さら
に、自動フィルターを適用し、手作業で絞り込む必要がないように機能する。

対象データ全体を選択（列見出しラベル含む）してからメインメニュー
:menuselection:`&Data --> Sub&totals...` を実行する。:guilabel:`Subtotals` ダイ
アログボックスが開く。項目を指定する：

* :guilabel:`&Group by` には小計グループフィールドを指定する
* :guilabel:`&Calculate subtotals for` には数値計算の対象フィールドを指定する
* 必要なら :guilabel:`2nd Group`, :guilabel:`3rd Group` タブの内容も指定する

----

実行直後、ワークシート行番号列の左にアウトラインが現れる。このアウトラインは小計
の階層構造を表す。

* アウトラインの上部にある番号
* またはプラス :guilabel:`+` とマイナス :guilabel:`-` 記号

を使用して、階層内の別階層データ表示を切り替える。アウトラインの表示切り替えには
次のコマンドがある：

* :menuselection:`&Data --> &Group and Outline --> &Remove Outline`
* :menuselection:`&Data --> &Group and Outline --> &AutoOutline`

アウトラインの左側ほど総計の、右側ほど小計の度合いがそれぞれ強まる。

----

:guilabel:`Options` タブに小計オプションがいろいろある。

----

:guilabel:`Subtotals` ダイアログボックスで、

* 現在のタブで行った変更を元に戻すには :guilabel:`Reset` ボタンを押す。
* 作成済みの小計を削除するには :guilabel:`Remove` ボタンを押す。

Using scenarios
======================================================================

計算に対する異なる条件の影響を検査する必要があるが、反復する手動データ入力を処理
したくない場合に有用な機能だ。

Creating scenarios
----------------------------------------------------------------------

対象セル（最低二つ）を選択してメインメニュー :menuselection:`&Tools -->
Sc&enario...` を実行すると :guilabel:`Create Scenario` ダイアログボックスが開
く。

* シナリオは通常複数作成するので、名前はまともに付けろ。
* どの計算がシナリオに依存しているかを追跡するには、シナリオセル上でメインメ
  ニュー :menuselection:`&Tools --> &Detective --> &Trace Depenendents` を実行す
  ると良い。
* 対象セルはどこにあってもかまわない。散在していてもいい。

Scenario settings
----------------------------------------------------------------------

:guilabel:`Create Scenario` ダイアログボックスのオプション項目はそれほど使わな
い？

:guilabel:`&Display border` をオフにするとワークシート内で紛れる。オンにするべき
だろう。

Changing scenarios
----------------------------------------------------------------------

シナリオ関連の記述では、ワークシートとセルの保護という言葉が何度も述べられている
ことに注意。次の四項目のオンオフ状態の組み合わせで、変更が許可されるかどうかが決
まる：

* ワークシートに対する保護
* シナリオセルに対する保護
* :guilabel:`Copy &back`
* :guilabel:`&Prevent changes`

いちばんわかりやすいのはワークシート保護がオフの場合だ。シナリオセルの値は変更可
能で、シナリオは :guilabel:`Copy &back` の設定次第で更新可能性が決まる。残りの組
み合わせはガイド本文を参照するしかない。

Working with scenarios using the Navigator
----------------------------------------------------------------------

ワークシートにシナリオを追加した後、特定のシナリオを表示するには、まず
:guilabel:`Navigator` ダイアログボックスを次のいずれかの方法で開く：

* :menuselection:`&View --> Na&vigator`
* :kbd:`F5`

それから :guilabel:`Scenarios` 図像をクリックしろ。

現在のワークシートにシナリオを適用するには、当該シナリオ名をダブルクリックしろ。
動作が遅いのが気になる。

シナリオを削除する方法は次のいずれか：

* シナリオ名の右クリックメニューから :menuselection:`&Delete` を実行する。
* シナリオ名を選択し :kbd:`Del` を押す。

シナリオを編集するには、シナリオ名の右クリックメニューから
:menuselection:`&Properties...` を実行する。シナリオ作成時のものとよく似た
:guilabel:`Edit Scenario` ダイアログボックスが開く。

Using the Multiple Operations tool
======================================================================

データを単一ワークシートにまとめ、数式、変数、表の範囲をラベルで識別するようにす
ると、このコマンドは使いやすいとある。

Multiple Operations with one formula and one variable
----------------------------------------------------------------------

一数式一変数の場合が基本だ。:menuselection:`&Data --> &Multiple Operations...`
コマンドを実行する準備手順はこうだ：

#. ワークシートのセルに、数式と、それが用いる変数を一つ以上入力する。
#. 同じワークシートで、列または行を占めるセル範囲（変数範囲）に値を入力する。
#. 今定義した変数範囲と、それに続く隣接した空セルの両方を含む範囲を選択する。変
   数範囲がどのように配列されているかによって、これらの空セルは、右の列（範囲
   が列の場合）か、すぐ下の行（行の場合）のいずれかになる。

これで :guilabel:`Multiple Operations` ダイアログボックスが開く。

* :guilabel:`Formulas` には上述の最初手順で定義した（数式への）セル参照を指定す
  る。
* 上述の変数範囲が列型ならば :guilabel:`&Column input cell` に、行型ならば
  :guilabel:`&Row input cell` に使用したい変数へのセルを指定する。

:guilabel:`&OK` をクリックして実行する。指定の空セルに結果が得られる。各結果値
は、それに隣接する変数値に対応し、一緒になって結果表を形成する。

----

ガイド本文の例の状況：

* B1: 単価 10 ドルで販売する玩具を生産しているとする
* B2: 各項目の製造費用は 2 ドル
* B3: 年間固定コストは 10,000 ドル
* B4: 販売数量の最初の見積もりは 2,000 個

だとしている。問題は、収支を均衡させるために何個の玩具を販売する必要があるか、
だ。この問題を解く手順はこうなる：

#. セル B5 に数式 ``=B4*(B1-B2)-B3`` を入力する。単純な一次式だ。
#. 例えばセル D2:D11 に 500 から 5000 までの値を 500 刻みで入力しておく。
#. セル D2:E11 を選択して :menuselection:`&Data --> &Multiple Operations...` を
   実行する

ダイアログボックスの指定はこのようにする：

* :guilabel:`&Formulas` にはセル B5 を指定
* :guilabel:`&Column input cell` にはセル B4 を指定

:guilabel:`&OK` をクリックすると空セルが埋まり、損益分岐が目視確認可能になる。

Calculating with several formulas simultaneously
----------------------------------------------------------------------

数式を複数にすることも可能だ。

* 数式の個数ぶんだけ対応する列・行を出力表に用意する必要がある。
* たとえば、数式 A, B, C をこの順序で一行に並べた場合、出力は表の一列目、二列
  目、三列目に A, B, C の順で格納される。

----

本文では、直前の販売データの例に年間全体の利益に加え、販売した商品ごとの年間利益
を計算する問題を解いている。

* セル C5 に ``=B5/B4`` を入力
* セル D2:F11 を選択して :menuselection:`&Data --> &Multiple Operations...` を実
  行する

ダイアログボックスの指定はこのようにする：

* :guilabel:`&Formulas` にはセル B5:C5 を指定
* :guilabel:`&Column input cell` にはセル B4 を指定（変わらず）

.. admonition:: 利用者ノート

   :guilabel:`&Column input cell` の指定を間違いやすい。

Multiple operations with two variables
----------------------------------------------------------------------

二変数で Multiple Operations を使用すると、二次元の結果表が得られる。変数それぞ
れが表の次元の一つを定義し、両方の変数の交代値がそれぞれ表の行見出しと列見出しに
なる。表の各セルは、行見出し値と列見出し値の個別の対に対応する。

順序が重要であって、:guilabel:`&Column input cell` 欄は行見出しの値に対応
し、:guilabel:`&Row input cell` 欄は列見出しの値に対応する。

二変数を使用する場合、Multiple Operations は複数の数式では機能しない。

----

最後の例では販売数と販売単価を変数にする。手順の変更点をまとめる：

* セル E1:H1 に直に値 8, 10, 15, 20 を入力する
* セル D1:H11 を選択してコマンドを起動

ダイアログボックスの指定が増える：

* :guilabel:`&Row input cell` に B1 を指定する。これにより、8, 10, 15, 20 が B1
  で定義された単価変数と連動する。
* :guilabel:`&Column input cell` には従来どおり B4 を指定する。これは 500, ...,
  5000 のセルが販売量変数 B4 に連動することを意味する。

Using Goal Seek
======================================================================

Goal Seek は、出力を与えて逆算して、どのような入力ならばその結果を生み出すかを発
見する手法の一つだ。欲しい結果はすでに知っているが、それに到達する方法や、条件を
変更した場合にどのように変化するかなどを見出すのに有用な機能だ。

Goal Seek example
----------------------------------------------------------------------

本文では年利計算を例に説明している。年利は資本金、利息期間、金利の積で与えられ
る。

* 金利 7.5% (B3)
* 期間 1 (B2)

が一定であるとする。15,000 ドルの年間益を達成するために必要な投資資本がいくらか
知りたい。そこでまずは初期資本を 100,000 ドル (B1) と見積もるという話だ。ワーク
シート上での手順例：

1. セル B1, B2, B3 に上述の定数を入力する
2. セル B4 に数式 ``=B1*B2*B3`` を入力する
3. メインメニューから :menuselection:`&Tools --> &Goal Seek...` を実行する

:guilabel:`Goal Seek` ダイアログボックス上での指定例：

* :guilabel:`&Formula cell` に年間益であるセル B4 を指定する
* :guilabel:`&Variable cell` に初期資本であるセル B1 を指定する
* :guilabel:`&Target value` に希望額である 15000 を入力する

:guilabel:`&OK` を押すとメッセージボックスが開き、解が得られる。ここで
:guilabel:`&Yes` で終わると、変数セル B1 が解で上書きされる。

Goal Seek アルゴリズムは、内部的に数回反復して目標に収束する。 計算が失敗した場
合、失敗を報告するメッセージボックスが開く（最も近い値を変数セルに挿入するかどう
かを選択可能）。

Using the Solver
======================================================================

数理計画問題や最適化問題を解くことができる。与えた制約条件の下で関数を最小化した
り最大化したりする問題だ。

Calc には現在、数種類の solver が備わっている。

問題を解くのに solver を用いるのであれば、問題を次のように定式化しないといけな
い。通常、目的は制約条件を満たし、目的関数の結果を最大化または最小化する決定変数
の値を見つけることだ。

決定変数
   :math:`n` 個の非負変数 :math:`{x_1, ..., x_n}` の集合
制約
   決定変数を含む一次等式または不等式の集合
目的関数
   決定変数を含む一次式

Solver 設定は ODS ファイルに保存されて、各タブは独自のモデルを持つことが可能だ。

Solver dialog
----------------------------------------------------------------------

:menuselection:`&Tools --> Sol&ver...` 実行でダイアログボックスを開く。JRE が無
効の場合にはメッセージボックスが現れる。とりあえず :guilabel:`&No` で進んで様子
見とする。

:guilabel:`Solver` ダイアログボックスが開く。

* Solver 設定が完了したら :guilabel:`&Solve` を押して値の調整と結果の計算を開始
  する。
* やり直す場合には :guilabel:`&Reset All` を押してダイアログボックス上をクリアす
  る。

DEPS Evolutionary Algorithm または SCO Evolutionary Algorithm を使用している場
合、エンジンの実行は定期的に中断して :guilabel:`Solver Status` ダイアログボックス
が開くことがある。

* このダイアログはエンジンの計算の現在の状態に関する診断情報を示すもので、専門家
  にとって興味がある。

  * :guilabel:`&OK` を押せばこのダイアログを閉じて計算を終了する。
  * :guilabel:`&Continue` 押せば次のエンジン処理が中断するところまで待機する。
* ダイアログボックスの表示は :guilabel:`Solver Options` ダイアログボックスの
  :guilabel:`Show enhanced solver status` をオフにすると生じない。

成功裡に完了すると、:guilabel:`Solving Result` が開く。これにはボタンが二つある：

* :guilabel:`&Keep Result` を押せば結果を保存する。
* :guilabel:`&Restore Previous` を押せば結果を破棄して直前の値を復元する。

Solver options
----------------------------------------------------------------------

:guilabel:`Solver dialog` 下部の :guilabel:`O&ptions...` ボタンを押すと
:guilabel:`Options` ダイアログボックスが開き、エンジンそれぞれに関する設定を行え
る。

Solver example
----------------------------------------------------------------------

10,000 ドルを投資信託二つに一年間投資するとする。

* ファンド X は金利 8% の低リスクファンドで、
* ファンド Y は金利 12% の高リスクファンドだ。

合計 1,000 ドルの利息を得るためには、それぞれのファンドにいくら投資すればよい
か。この問題を solver を用いて解く。

ワークシートを本文のように埋めて :menuselection:`&Tools --> Sol&ver...` を実行。
ダイアログを開く。

* :guilabel:`&Target cell` には利子総額である B4 を指定
* ラジオボタン :guilabel:`&Value of` を選択し、テキストボックスに得たい利息額で
  ある 1000 を入力
* :guilabel:`&By changing cells` にはファンド X への投資額である C2 を指定
* :guilabel:`&Limiting conditions` を与える

  * C2≦C4`: ファンド X への投資額が利用可能額を超えてはならない
  * C2≧0: ファンド X への投資額は非負でなければならない
  * C2 は整数である（便宜上）

Using Statistics tools
======================================================================

メインメニュー :menuselection:`&Data --> Statistics -->` に統計分析コマンド各種
が並んでいる。今見たら 13 コマンドもある。

Sampling tool
----------------------------------------------------------------------

:menuselection:`&Data --> Statistics --> &Sampling...` コマンドは表から標本抽出
して別の表を作成する。

* 抽出はランダムに、または周期的になされる。
* 抽出は行単位で行われる。

.. admonition:: 利用者ノート

   試してみるとテキストデータがゼロになるようだ？

Descriptive Statistics tool
----------------------------------------------------------------------

:menuselection:`&Data --> Statistics --> &Descriptive Statistics...` コマンドは
指定データ集合の主な統計的特性（平均、標準偏差、等々）の報告表を作成する。確率統
計の教科書で出てくる概念と同じだろう。

.. admonition:: 利用者ノート

   こういうダイアログボックスが開くところから始まるコマンドは、実行直前にフィー
   ルドセルを含むデータ集合全体を選択状態にしておくと良い。

.. seealso::

   `Descriptive statistics - Wikipedia
   <https://en.wikipedia.org/wiki/Descriptive_statistics>`__

Analysis of Variance (ANOVA) tool
----------------------------------------------------------------------

:menuselection:`&Data --> Statistics --> &Analysis of Variance (ANOVA)` コマンド
は標本中の複数グループの平均を比較する。

実行するとダイアログボックスが開いて、:guilabel:`&OK` を押すと分析するという流れ
だ。

* 結果にセル領域を相当費やすので、:guilabel:`&Results to` の指定に気をつけろ。
* :guilabel:`Rows &per sample` UI は現在無効。

.. seealso::

   `Analysis of variance - Wikipedia
   <https://en.wikipedia.org/wiki/Analysis_of_variance>`__

Correlation tool
----------------------------------------------------------------------

:menuselection:`&Data --> Statistics --> &Correlation...` コマンドは数値データの
組の相関を計算し、相関係数を求める。

本書の例では数学、物理、生物の得点間の相関を検証するものということになる。出力を
見ればどう理解すればいいかわかるだろう。

.. seealso::

   `Correlation - Wikipedia <https://en.wikipedia.org/wiki/Correlation>`__

Covariance tool
----------------------------------------------------------------------

:menuselection:`&Data --> Statistics --> &Covariance...` コマンドは共分散、数値
データセットが共にどれだけ変化するかを測定する。

ダイアログボックスの UI は相関係数コマンドと同じだ。

.. seealso::

   `Covariance - Wikipedia <https://en.wikipedia.org/wiki/Covariance>`__

Exponential Smoothing tool
----------------------------------------------------------------------

:menuselection:`&Data --> Statistics > Exponential Smoothing...` コマンドは、平
滑化された結果を生成するようにデータ集合をいじる。株式市場分析や標本測定などの分
野で用いられる機能とのことだ。

ダイアログボックス上の減衰係数 :guilabel:`&Smoothing factor` はコマンド実行後で
も対応するセルの値を編集することで結果を更新することが可能だ。

.. seealso::

   `Exponential smoothing - Wikipedia
   <https://en.wikipedia.org/wiki/Exponential_smoothing>`__

Moving Average tool
----------------------------------------------------------------------

:menuselection:`&Data --> Statistics --> &Moving Average...` コマンドは時系列
データ集合の移動平均を計算する。コマンドを実行するとダイアログボックスが開く。

* :guilabel:`&Trim input range to actual data content` をオンにすると、計算前に
  入力範囲を実際のデータ内容に刈り取ることを許可する。処理性能に影響する。

.. seealso::

   `Moving average - Wikipedia <https://en.wikipedia.org/wiki/Moving_average>`__

Regression tool
----------------------------------------------------------------------

:menuselection:`&Data --> Statistics --> &Regression...` コマンドは独立変数複数
個と従属変数一個からなるデータセットの線形回帰、対数回帰、累乗回帰のいずれかの分
析を行う。

ダイアログボックス上では：

* :guilabel:`Con&fidence level` には信頼度数を 0 から 1 までの値で指定する。
* :guilabel:`Calc&ulate residuals` をオンにすると残差の計算を行う。傾きと切片の
  推定値とその統計量にしか興味がない場合に有益だ。

出力については、例によってスペースをたくさん消費するので出力先指定に注意しろ。
Confidence level の値はワークシート上に分析結果が生じてからでも変更、更新可能
だ。

.. seealso::

   `Regression analysis - Wikipedia
   <https://en.wikipedia.org/wiki/Regression_analysis>`__

Paired t-test tool
----------------------------------------------------------------------

:menuselection:`&Data --> Statistics --> Paired &t-test...` コマンドは t 検定を
実行する。関連する標本集合二つの母平均を比較し、それらの差を決定する。

ダイアログボックスは統計コマンドでよくある単純なものだ。

* 出力表では、アルファと仮説平均差に異なる値を挿入可能。t 値各種は自動更新。

.. seealso::

   `Student's t-test - Wikipedia
   <https://en.wikipedia.org/wiki/Student's_t-test>`__

F-test tool
----------------------------------------------------------------------

:menuselection:`&Data --> Statistics --> &F-test...` コマンドは標本二つの F 検定
を行う。母集団二つの分散が等しいという仮説を検定する。

.. seealso::

   `F-test - Wikipedia <https://en.wikipedia.org/wiki/F-test>`__

Z-test tool
----------------------------------------------------------------------

:menuselection:`&Data --> Statistics --> &Z-test...` コマンドは標本二つの Z 検定
を行う。帰無仮説を検定する。

ダイアログボックスで :menuselection:`&OK` を押すだけでは検定は完了しない。各標本
の Known Variance 欄を手動で埋める必要がある。本文の例を再現する場合は次を入力し
ろ：

* ``=VAR(A1:A13)``
* ``=VAR(B1:B13)``

Z 検定は標本数 30 を超える大きな標本に対してよりよく働く。

* Alpha と Hypothesized Mean Difference の入力に異なる値を挿入することも可能だ。
  後続の z 値と P 値が自動更新される。
* 選択した Alpha と適切な計算 P 値を比較する分析をしろ。これは片側検定か両側検定
  かによって異なる。計算 P 値が Alpha より小さければ仮説は棄却される。

.. seealso::

   `Z-test - Wikipedia <https://en.wikipedia.org/wiki/Z-test>`__

Chi-Square Test tool (Test of Independence)
----------------------------------------------------------------------

:menuselection:`&Data --> Statistics --> &Chi-square Test...` コマンドは標本の
:math:`\xi^2` 検定を計算し、測定値集合が対応する期待値集合にどの程度適合するかを
決定する。

例によってワークシートの Alpha 値を手動で変更して、関連項目を自動更新することが
可能だ。本コマンドでは Critical Value 欄がそうなる。

.. seealso::

   `Chi-squared test - Wikipedia
   <https://en.wikipedia.org/wiki/Chi-squared_test>`__

Fourier Analysis tool
----------------------------------------------------------------------

:menuselection:`&Data --> Statistics --> F&ourier Analysis...` コマンドは複素数
の入力配列の離散 Fourier 変換を計算することにより、データ集合の Fourier 解析を行
う。

ダイアログボックス上では：

* :guilabel:`&Input range` では変換元データを含むセル範囲を指定する。通常は、変
  換する複素数の配列を表す 2 x N または N x 2 の範囲であり、配列はそれぞれデータ
  の実部と虚部を表す。
* :guilabel:`In&verse` をオンにすると、逆離散 Fourier 変換を計算する。
* :guilabel:`Output in &polar form` をオンにすると、出力が極形式になる。
* 出力を極形式にする場合、さらに :guilabel:`&Minimum magnitude for polar form
  output` をオンにすると、dB 単位で指定した値より小さい成分が抑制される。信号の
  大きさと位相のスペクトルを見るときに有用だ。

  FFT アルゴリズムを実行すると、わずかな丸め誤差がつねに発生し、存在しない周波数
  の位相がゼロにならない。この引数に適切な値を指定することで、このような成分を抑
  制する。

本文の例を見ると、実数列の分析は単に虚部をゼロに埋めた列を添えれば動作するよう
だ。

.. seealso::

   `Fourier analysis - Wikipedia
   <https://en.wikipedia.org/wiki/Fourier_analysis>`__
