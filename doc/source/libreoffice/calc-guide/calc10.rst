======================================================================
Calc Guide Chapter 10, Data Analysis ノート
======================================================================

.. include:: ./calc-inc.txt

.. contents:: 章見出し
   :local:

Introduction
======================================================================

Calc には数式や関数のほかに、データを処理するためのツールをいくつか搭載してい
る。これらのツールにはデータのコピーと再利用、小計の作成、「もしも」分析の実行、
統計分析の実行などの機能がある。これらのツールは |MenuBar| の
:menuselection:`&Data` と :menuselection:`&Tools` に分散している。これらのツール
は大規模なデータセットの処理にかかる時間と労力を節約したり、将来の査読のために作
業を保存したりするのに役立つ

.. note::

   関連ツールであるピボットテーブルは独自の章が必要なほど複雑であるためここでは
   触れない。|Calc09| を見ろ。

Consolidating data
======================================================================

複数のシートに散在しているデータを結合して集計する機能として
:menuselection:`&Data-->&Consolidate...` コマンドがある。散在する大きなデータを
素早くまとめて査読する必要がある場合に便利だ。例えば、異なるシートにある部門予算
を総合シートにある全社予算に統合することができる。

これを実行すると
:guilabel:`Consolidate` ダイアログが開く。この使い方が自力ではわからない。

* :guilabel:`&Function` ドロップダウンリストから所望の集計関数を指定する。
* :guilabel:`&Source data ranges` 欄を指定する。それから :guilabel:`Add` ボタン
  を押して選択範囲を :guilabel:`Consolidation ranges` 一覧に追加する。この追加処
  理を所望の範囲をカバーするまで反復する。
* :guilabel:`Copy results &to` 欄を指定する。

To consolidate data:

#. 統合する升目範囲を含む文書を開く。
#. |MenuBar| から :menuselection:`&Data-->&Consolidate...` を選択して
   :guilabel:`Consolidate` ダイアログボックスを開く。
#. :guilabel:`&Source data ranges` 欄をクリックし、原データ範囲、名前付き範囲へ
   の参照を入力するか、マウスで選択する。
#. :guilabel:`&Add` ボタンを押して選択範囲を :guilabel:`Consolidation ranges` 一
   覧に追加する。
#. この追加処理を所望の範囲をカバーするまで反復する。
#. 統合範囲一覧の登録項目を削除するには、その項目を選択し、:guilabel:`&Delete`
   ボタンを押す。削除は確認なしで実行される。
#. :guilabel:`Copy results &to` 欄をクリックし、対象範囲の最初の升目への参照を入
   力するか、マウスで選択する。フィールドの左側にあるドロップダウンリストで名前
   付き範囲を選択することも可能。
#. :guilabel:`&Function` ドロップダウンリストからデータを集計関数を選択する。既
   定は `Sum` だ。その他の使用可能な関数は `Count`, `Average`, `Max`, `Min`,
   `Product`, `Count`, `StdDev`, `StDevP`, `Var`, `VarP` だ。
#. |OK| を押して処理を実行する。指定した場所にある値を集計関数に入力として渡して
   評価し、指定した場所に出力する。

.. tip::

   同じ升目範囲を繰り返し統合する場合は、再利用可能な名前付き範囲に変換して、処
   理を簡単にすることを検討しろ。名前付き範囲については |Calc14| を見ろ。

Consolidation settings
----------------------------------------------------------------------

ダイアログ上のプラスマークをクリックすると、詳細オプション項目群が現れる。

ラベル系オプションは選択範囲それぞれの最初の列や最初の行がフィールドである場合、
かつそれらがすべて一致している場合にはオンにするのが自然だろう。

:guilabel:`&Link to source data` をオンにすると、:guilabel:`&Source data ranges`
の値が変化すると :guilabel:`Copy results &to` の値も自動的に更新される。

.. rubric:: Consolidate by

この区画では原データ範囲をそれらの範囲位置で統合するか、ラベル合致により統合する
かを選択する。統合ラベルが各範囲内に含まれている必要があり、行または列自体を統合
するには、対応する行または列ラベルのテキストが一致する必要がある。

:guilabel:`&Row labels`
   合致ラベルで行を連結する。これをオフにすると位置で連結する。
:guilabel:`C&olumn labels`
   行ラベルと同じ働きをするが、代わりに列を使用する。

.. rubric:: Options

:guilabel:`&Link to source data` をオンにすると、原範囲の値にリンクする数式が対
象範囲に追加される。これをオンにすると原範囲に加えた変更により、対象範囲の値が自
動的に更新される。

.. note::

   原データへの Link をオンにすると、原リンクそれぞれが対象範囲に入り、並べ替え
   られ、ビューから見えなくなる。既定では統合の最終結果しか表示されない。

Consolidation example
----------------------------------------------------------------------

ガイド本文のデータを手で再現して Consolidation コマンドの動作を体で理解しろ。

   The source ranges and target range are saved as part of the document. If you
   later open a document with consolidated ranges, they will still be available
   in the Consolidation ranges list of the Consolidate dialog.

.. admonition:: 読者ノート

   私のスプレッドシートでやるならば家計簿がいい。各月を統合しよう。

Creating subtotals
======================================================================

小計を得る方法は二つだ：

* `SUBTOTAL` 関数
* :menuselection:`&Data-->Sub&totals...` コマンド

Using the `SUBTOTAL` function
----------------------------------------------------------------------

`SUBTOTAL` 関数は |FunctionWizard| の Mathematical 区分と |Sidebar|
|FunctionsDeck| の下に一覧されている。|Calc08| 参照。本関数はわずかな区分だけで
使用する場合に効果的だ。

A `SUBTOTAL` example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

本文のデータを手で再現して `Sales Value` の列の下の升目に `SUBTOTAL` 呼び出しを
埋める。急所は、自動フィルターで例えば Employee を Brigitte に絞り込むと、それに
応じて `SUBTOTAL` の値が更新されることにある。

|FunctionWizard| を使用して `Sales Value` の小計を作成する手順：

#. 小計を出力する升目を選択する。通常、この升目は小計される列のいちばん下にあ
   り、この例では `Sales Value` 列だ。
#. |FunctionWizard| を開く。
#. :guilabel:`&Function` 一覧から `SUBTOTAL` を選択し、|Next| を押す。
#. ダイアログの右側にある :guilabel:`Function` 欄に関数の数値コードを入力する。
   このコードは 1 から 11 または 101 から 111 の範囲の値でなければならない。各値
   の意味は本書表 1 に示されている。

   .. todo:: 時間があれば表を転載

   .. note::

      値 1 から 11 には計算された小計に隠れ値が含まれるが、値 101 から 111 には
      含まれない。データの表示切り替えについては |Calc02| を見ろ。絞り込まれて消
      える升目は `SUBTOTAL` 関数によって常に除外される。

#. :guilabel:`Range` 欄をクリックし、`Sales Value` 範囲への参照を入力するか、マ
   ウスで升目を選択する。その間、ダイアログを一時的に最小化する必要があれば
   :guilabel:`Shrink` / :guilabel:`Expand` ボタンを使用する。
#. |OK| を押して |FunctionWizard| を閉じる。先ほど選択した升目に売上合計が出力さ
   れる。
#. `Employee` 列の上部にある AutoFilter の▼をクリックし、`Brigitte` と `(empty)`
   を除いてオフにする。出力升目に `Brigitte` の売上合計が表示される。

.. note::

   小計に使用される升目範囲に他の小計が含まれている場合、これらの小計は最終的な
   小計の勘定に入らない。同様に、AutoFilter でこの機能を使用すると現在の絞り込み
   を満たすデータのみが表示される。絞り込まれて除外されたデータは無視される。

.. admonition:: 読者ノート

   * `SUBTOTAL` の第一引数の謎数値が計算の種類を指す。
   * 列の下に出力セルを設けると、当然だが自動フィルター適用時にそれが隠れる。
     `SUBTOTAL` の動作を試すときにはどう絞り込んでも隠れないセルに書け。

The Subtotals tool
----------------------------------------------------------------------

Calc では `SUBTOTAL` 関数のより包括的な代替手段として Subtotal ツールを供給して
いる。単一の配列に対してのみ機能する `SUBTOTAL` とは対照的に、ラベル付きの列に配
置された最大三つの配列の小計を作成できる。また、区分別に小計をグループ化し、自動
的に並び替えるため、AutoFilter を適用し、区分を手作業で絞り込む必要がない。

Using the Subtotals tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |SubtotalsDlg| replace:: :guilabel:`Subtotals` ダイアログボックス

対象データ全体を選択（列見出しラベル含む）してから |MenuBar| から
:menuselection:`&Data-->Sub&totals...` を実行する。|SubtotalsDlg| が開く。項目を
指定する：

* :guilabel:`&Group by` には小計グループフィールドを指定する
* :guilabel:`&Calculate subtotals for` には数値計算の対象フィールドを指定する
* 必要なら :guilabel:`2nd Group`, :guilabel:`3rd Group` タブの内容も指定する

シートに小計値を入れる手順：

.. |1stGroupTab| replace:: :guilabel:`1st Group` タブ

#. 計算したい小計のセル範囲を選択する。列見出しラベルを忘れずに含める。または、
   データ内のセルを一つクリックして、Calc が自動的に範囲を識別できるようにする。
#. |MenuBar| から :menuselection:`&Data-->Sub&totals...` を選択して
   |SubtotalsDlg| を開く。
#. |1stGroupTab| の :guilabel:`&Group by` ドロップダウンリストで、ラベルにより列
   を選択する。手順 1. の升目範囲の項目がグループ化され、この列の合致する値で並
   び替わる。
#. |1stGroupTab| の :guilabel:`&Calculate subtotals for` ボックスで、小計する値
   を含む列を選択する。この列の値を後で変更すると小計が自動的に再計算される。
#. |1stGroupTab| の :guilabel:`Use function` 欄で、手順 4. で選択した列の小計を
   計算する関数を選択する。
#. 手順 4. と 5. を繰り返して、|1stGroupTab| で他の列の小計を作成する。
#. :guilabel:`2nd Group` タブと :guilabel:`3rd Group` タブを使い手順 3. から 6.
   を繰り返すことでさらに二つの小計区分を作成可能。グループを増やしたくない場合
   は 各ページの :guilabel:`&Group by` を `- none -` のままにしておく。
#. |OK| を押す。升目範囲に小計行と総計行が加わる。

Subtotal outline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Subtotals ツールを使用すると行番号列の左にアウトラインが付与される。このアウトラ
インは小計の階層構造を表し、アウトラインの上部にある番号付き列指示標、プラス記号
とマイナス記号で示されるグループ指示標を使用して、階層内の異なる階のデータ表示を
切り替えるのに使用できる。

この機能は小計が多い場合に有用だ。個々の項目などの低水準の詳細を隠すだけでデータ
の高高水準の概略を作成できる。アウトラインの使用方法については |Calc02| を見ろ。

を使用して、階層内の別階層データ表示を切り替える。アウトラインの表示切り替えには
次のコマンドがある：

* :menuselection:`&Data-->&Group and Outline-->&Remove Outline`
* :menuselection:`&Data-->&Group and Outline-->&AutoOutline`

アウトラインの左側ほど総計の、右側ほど小計の度合いがそれぞれ強まる。

Subtotals tool options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|SubtotalsDlg| の |OptionsTab| をクリックして、以下の設定にアクセスする：

.. rubric:: Groups

小計データの整理方法を定義する。

:guilabel:`&Page break between groups`
   各小計グループの間に改頁を入れ、データを印刷するときに各グループが別々のペー
   ジに表示されるようにする。
:guilabel:`&Case sensitive`
   大文字と小文字が異なるデータラベルによって登録項目がグループ化されるのを防ぐ。
   `Sales Value` の例では、このオプションがオンの場合、`Employee` 列の下に
   `Brigitte` と `brigitte` がある登録項目は合致しない。
:guilabel:`Pre-&sort area according to groups`
   小計を計算する前に登録項目をグループ別に並び替える。このオプションをオフにす
   ると合致する項目がグループにならない。その結果、合致する項目が連続した行に表
   示されない場合、異なる小計が作成される。たとえば、`Golf` 区分の二つの項目は、
   その間に `Tennis` 項目がある場合、同じグループ小計として勘定されない。

.. rubric:: Sort

小計データの並び替え方法を定義する。Pre-sort がオフ場合、この区画が無効になる。

:guilabel:`&Ascending` または :guilabel:`D&escending`
   それぞれ、昇順、降順並び替え。これらの並び替え規則は |MenuBar| の |SortM| で
   変更できる。|Calc02| を見ろ。
:guilabel:`I&nclude formats`
   通貨形式などの書式設定をデータから対応する小計に引き継ぐ。
:guilabel:`C&ustom sort order`
   |OptionsDlg| |SortListsPage| にある定義済みのカスタム並べ替えのいずれかに従っ
   てデータを並べ替える。|Calc02| を見ろ。

Reset and Remove
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|SubtotalsDlg| で、現在のタブで行った変更を元に戻すには |ResetButton| を押す。作
成済みの小計を削除するには |RemoveButton| を押す。

Using scenarios
======================================================================

シナリオは、データに関する「もしも」の質問に答えるために使用できる、名前が付いた
保存された升目範囲だ。同じ計算集合に対して複数のシナリオを作成し、素早く入れ替え
てそれぞれの結果を見ることができる。計算に対する異なる条件の影響を試験する必要が
あるが、繰り返しの手動データ入力を処理したくない場合に便利な機能だ。例えば、投資
に対して異なる金利を試行したい場合、各金利のシナリオを作成し、それらを切り替え
て、どの金利が最も効果的かを調べるという具合だ。

Creating scenarios
----------------------------------------------------------------------

新しいシナリオを作成するには

#. シナリオ間で変化する値を含む升目を選択する。少なくとも二つ選択する必要がある。
#. |MenuBar| から :menuselection:`&Tools-->Sc&enario...` を選択する。
   :guilabel:`Create Scenario` ダイアログボックスが開く。
#. 新しいシナリオの名前を :guilabel:`Name of Scenario` 欄に入力する。

   .. tip::

      作成するシナリオには明確に識別できる一意の名前をつけろ。Calc が提案する既
      定の名前は勧められない。

#. オプションとして、:guilabel:`Co&mment` 欄に情報を追加する。
#. |OK| を押してダイアログを閉じる。新規シナリオは作成と同時に自動的に活動中にな
   る。
#. 以上の手順を繰り返して追加のシナリオを作成する。同じ計算のシナリオを複数作成
   するには、最初のシナリオに使用したのと同じ升目範囲を選択する。

.. tip::

   どの計算がシナリオに依存しているかを追跡するには、シナリオ升目を強調表示した
   後、|MenuBar| から :menuselection:`&Tools-->&Detective-->&Trace Depenendents`
   を実行する。矢印は、シナリオ升目から依存する数式升目を指す。|Calc08| を見ろ。

Scenario settings
----------------------------------------------------------------------

:guilabel:`Create Scenario` ダイアログボックスの :guilabel:`Settings` 区間にある
オプション：

:guilabel:`&Display border`
   シナリオを含む升目範囲の周囲に色付き境界を配置する。

   境界の色を選択するには、このオプションの右にあるドロップダウンリストを使用す
   る。境界には活動中のシナリオ名を表示する表題棒と現在の升目範囲に定義されてい
   るシナリオ全てのドロップダウンリストを開く▼がある。この一覧からシナリオを選択
   することで、別のものに切り替えることができる。
:guilabel:`Copy &back`
   シナリオのセル値に加えられた変更を活動中のシナリオに戻す。このオプションをオ
   フにすると、シナリオの初期値は上書き不可となる。当設定の実際の動作は、現在の
   升目とシートの保護と、:guilabel:`&Prevent changes` オプションに依存する。

   .. caution::

      :guilabel:`Copy &back` をオンにしたシナリオの升目から新しいシナリオを作成
      する場合、古いシナリオを上書きしないように気をつけろ。このような状況を避け
      るためには、:guilabel:`Copy &back` をオンにした新しいシナリオを最初に作成
      し、活動中になってから値を変更しろ。

:guilabel:`Copy &entire sheet`
   新しい活動中シナリオでシートのコピーを作成する。シートにはこのシナリオの名前
   が付けられる。コピーシートでシナリオの値を変更しても、:guilabel:`Copy &back`
   が有効になっていても、活動中シナリオには影響しない。
:guilabel:`&Prevent changes`
   シートは保護されているが升目は保護されていない場合に、:guilabel:`Copy &back`
   を有効にしたシナリオへの変更を防ぐ。また、シートが保護されている間、シナリオ
   の設定の変更を防ぐ。次の節を見ろ。

.. admonition:: 読者ノート

   :guilabel:`&Display border` をオフにするとシート内で紛れる。オンにするべきだ
   ろう。

Changing scenarios
----------------------------------------------------------------------

シナリオには、独立して変更できる側面が二つある：

* シナリオの設定
* シナリオ升目の値

これらの側面をどの程度変更できるかは、活動中シナリオの性質と、現在のシートと升目
の保護に依存する。シートとセルの保護については |Calc02| を見ろ。

Changing scenario properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

シートの保護と :guilabel:`&Prevent changes` オプションがシナリオ性質を変更する能
力にどのように影響するかをまとめると：

.. list-table:: シナリオ性質変更
   :align: left
   :header-rows: 1
   :stub-columns: 0
   :widths: auto

   * - シート保護
     - 変化防止
     - 性質変化
   * - On
     - On
     - シナリオ性質は変更できない。
   * - On
     - Off
     - 境界表示と戻しコピーは変更可能。変更禁止もシート全体コピーも変更不可。
   * - Off
     - どれでも
     - シート全体コピー以外のシナリオ引数はすべて変更可。この場合、変更防止オプ
       ションは効果なし。

Changing scenario cell values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

シナリオ升目の値を変更する際の様々な設定の相互作用をまとめると：

.. list-table:: シナリオ升目値変更
   :align: left
   :header-rows: 0
   :stub-columns: 0
   :widths: auto

   * - Sheet protection
     - Scenario cell protection
     - Prevent changes
     - Copy back
     - 変更可
   * - On
     - Off
     - On
     - On
     - シナリオ升目の値は変更不可。
   * - On
     - Off
     - Off
     - On
     - シナリオ升目の値は変更可。シナリオ更新可。
   * - On
     - Off
     - どれでも
     - Off
     - シナリオ升目の値は変更可だが、コピー戻しの設定によりシナリオは更新されな
       い。
   * - On
     - On
     - どれでも
     - どれでも
     - シナリオ升目の値は変更不可。
   * - Off
     - どれでも
     - どれでも
     - どれでも
     - シナリオ升目の値は変更可で、シナリオはコピー戻しの設定によって更新された
       りされなかったりする。

Working with scenarios using the Navigator
----------------------------------------------------------------------

スプレッドシートにシナリオを追加した後、Navigator を使って特定のシナリオを見るこ
とができる。

ワークシートにシナリオを追加した後、特定のシナリオを表示するには、まず Navigator
を開く。[#calc10-footer-1]_ それから :guilabel:`Scenarios` 図像をクリックしろ。
定義されたシナリオは、各シナリオの作成時に入力されたコメントと共に一覧表示される。
|Sidebar| |NavigatorDeck| でも同等の機能を使用することができる。

現在のワークシートにシナリオを適用するには、Navigator で当該シナリオ名をダブルク
リックしろ。

.. admonition:: 読者ノート

   動作が遅いのが気になる。

シナリオを削除する方法は次のいずれか：

* シナリオ名の右クリックメニューから :menuselection:`&Delete` を実行する。
* シナリオ名を選択し |Del| を押す。

シナリオを編集するには、シナリオ名の右クリックメニューから
:menuselection:`&Properties...` を実行する。シナリオ作成時のものとよく似た
:guilabel:`Edit Scenario` ダイアログボックスが開く。

Using the Multiple Operations tool
======================================================================

シナリオと同様に、Multiple Operations ツールは計算の「もしも」分析を実行する。複
数の計算式変数の値の集合を表すシナリオとは異なり、このツールは、一つまたは二つの
変数の値の全範囲を使用する。そして、数式を使用して一致する解の範囲を作成する。各
解は一つか二つの変数値に対応するので、変数と解の範囲の両方を表形式で簡単に配列す
ることができる。Multiple Operations ツールは読みやすく、共有しやすい、またはグラ
フを使用して視覚化しやすいデータを生成するのに適している。

.. tip::

   データを単一ワークシートにまとめ、数式、変数、表の範囲をラベルで識別するよう
   にすると、このコマンドは使いやすい。

Multiple Operations with one formula and one variable
----------------------------------------------------------------------

Muitiple Operations ツールの使い方を学ぶ最も簡単な方法は一数式一変数の場合だ。
複数の数式または二つの変数を使ったツールの使い方については、それぞれ後述の

* :ref:`calc10-anchor-several`
* :ref:`calc10-anchor-two`

を見ろ。

:menuselection:`&Data-->&Multiple Operations...` コマンドを実行する準備手順はこ
うだ：

#. シートの升目に、数式と、それが用いる変数を一つ以上入力する。
#. 同じシートで、列または行を占める升目範囲（変数範囲）に値を入力する。
#. 今定義した変数範囲と、それに続く隣接した空升目の両方を含む範囲を選択する。変
   数範囲がどのように配列されているかによって、これらの空升目は右の列（範囲が列
   の場合）か、すぐ下の行（行の場合）のいずれかになる。

これで :guilabel:`Multiple Operations` ダイアログボックスが開く。

* :guilabel:`Formulas` には上述の最初手順で定義した（数式への）升目参照を指定す
  る。
* 上述の変数範囲が列型ならば :guilabel:`&Column input cell` に、行型ならば
  :guilabel:`&Row input cell` に使用したい変数への升目を指定する。

|OK| をクリックして実行する。指定の空セルに結果が得られる。各結果値はそれに隣接
する変数値に対応し、一緒になって結果表を形成する。

An example with one formula and one variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ガイド本文の例の状況：

* B1: 単価 10 ドルで販売する玩具を生産しているとする
* B2: 各項目の製造費用は 2 ドル
* B3: 年間固定コストは 10,000 ドル
* B4: 販売数量の最初の見積もりは 2,000 個

だとしている。問題は、収支を均衡させるために何個の玩具を販売する必要があるか、
だ。この問題を解く手順はこうなる：

#. 升目 B5 に数式 ``=B4*(B1-B2)-B3`` を入力する。単純な一次式だ。
#. 例えばセル D2:D11 に 500 から 5000 までの値を 500 刻みで入力しておく。
#. 升目 D2:E11 を選択して :menuselection:`&Data-->&Multiple Operations...` を実
   行する

ダイアログボックスの指定はこのようにする：

* :guilabel:`&Formulas` には升目 B5 を指定
* :guilabel:`&Column input cell` には升目 B4 を指定

|OK| を押すと空升目が埋まり、損益分岐が目視確認可能になる。

.. _calc10-anchor-several:

Calculating with several formulas simultaneously
----------------------------------------------------------------------

複数の数式で Multiple Operations ツールを使用する場合は一数式を使用する場合とほ
ぼ同じ手続きになるが、重要な違いが二つある：

* 数式の個数ぶんだけ対応する列・行を出力表に用意する必要がある。
* たとえば、数式 A, B, C をこの順序で一行に並べた場合、出力は表の一列目、二列
  目、三列目に A, B, C の順で格納される。

.. note::

   Multiple Operations ツールは、結果表の向きによって、一行または一列に並んだ数
   式しか受け付けない。表が列指向の場合、つまり、売上データの例では、数式は行に
   配置する必要がある。表が行指向の場合は数式を列に配置する必要がある。

.. caution::

   数式と数式の間に空升目を追加すると、結果表に隙間ができ、表の行や列を十分に
   選択しないと結果が表示されないことがあるので気をつけろ。

An example with two formulas and one variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

本文では、直前の販売データの例に年間全体の利益に加え、販売した商品ごとの年間利益
を計算する問題を解いている。

* 升目 C5 に ``=B5/B4`` を入力
* 升目 D2:F11 を選択して :menuselection:`&Data-->&Multiple Operations...` を実
  行する

ダイアログボックスの指定はこのようにする：

* :guilabel:`&Formulas` には升目 B5:C5 を指定
* :guilabel:`&Column input cell` には升目 B4 を指定（変わらず）

.. admonition:: 利用者ノート

   :guilabel:`&Column input cell` の指定を間違いやすい。

.. _calc10-anchor-two:

Multiple operations with two variables
----------------------------------------------------------------------

二変数で Multiple Operations を使用すると、二次元の結果表が得られる。変数それぞ
れが表の次元の一つを定義し、両方の変数の代替値がそれぞれ表の行見出しと列見出しに
なる。表の各セルは、行見出し値と列見出し値の個別の対に対応する。変数を二つ使うの
で、それらを定義するために :guilabel:`&Column input cell` と :guilabel:`&Row
input cell` 両方を使うことになる。

.. tip::

   列見出しが表の一番上の行にあるので、:guilabel:`&Column input cell` 欄は行見出
   しの値に対応する。同様に、行見出しが列にあるので :guilabel:`&Row input cell`
   欄は列見出しの値に対応する。

.. note::

   二変数を使用する場合、Multiple Operations は複数の数式では機能しない。余分な
   数式を入力することは許されるが、最初の数式以上の数式に対して期待される結果は
   生じない。

Calculating with two variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

最後の例では販売数と販売単価を変数にする。手順の変更点をまとめる：

* 升目範囲 E1:H1 に直に値 8, 10, 15, 20 を入力する
* 升目範囲 D1:H11 を選択してコマンドを起動

ダイアログボックスの指定が増える：

* :guilabel:`&Row input cell` に B1 を指定する。これにより、8, 10, 15, 20 が B1
  で定義された単価変数と連動する。
* :guilabel:`&Column input cell` には従来どおり B4 を指定する。これは 500, ...,
  5000 の升目が販売量変数 B4 に連動することを意味する。

Using Goal Seek
======================================================================

Goal Seek は出力を与えて逆算して、どのような入力ならばその結果を生み出すかを発見
する「もしも」手法の一つだ。欲しい結果はすでに知っているが、それに到達する方法
や、条件を変更した場合にどのように変化するかなどを見出すのに有用な機能だ。複数の
引数を試行する必要がある場合は、それぞれについて別の Goal Seek を実行する必要が
ある。

.. note::

   一度の Goal Seek で変更できる引数は一つしかない。複数の引数を試行する場合は、
   それぞれの引数に対して個別に Goal Seek を実行する必要がある。

Goal Seek example
----------------------------------------------------------------------

本文では年利計算を例に説明している。年利は資本金、利息期間、金利の積で与えられ
る。

* 金利 7.5% (B3)
* 期間 1 (B2)

が一定であるとする。15,000 ドルの年間益を達成するために必要な投資資本がいくらか
知りたい。そこでまずは初期資本を 100,000 ドル (B1) と見積もるという話だ。ワーク
シート上での手順例：

1. 升目 B1, B2, B3 に上述の定数を入力する
2. 升目 B4 に数式 ``=B1*B2*B3`` を入力する
3. |MenuBar| から :menuselection:`&Tools-->&Goal Seek...` を実行する

:guilabel:`Goal Seek` ダイアログボックス上での指定例：

* :guilabel:`&Formula cell` に年間益である升目 B4 を指定する
* :guilabel:`&Variable cell` に初期資本である升目 B1 を指定する
* :guilabel:`&Target value` に希望額である 15000 を入力する

|OK| を押すとメッセージボックスが開き、解が得られる。ここで |Yes| で終わると、変
数升目 B1 が解で上書きされる。


.. note::

   Goal Seek アルゴリズムは、内部的に数回反復して目標に収束する。計算が失敗した
   場合、失敗を報告するメッセージボックスが開く（最も近い値を変数升目に入れるか
   どうかを選択可能）。

Using the Solver
======================================================================

Solver は Goal Seek をより精巧にしたもので、数理計画問題や最適化問題を解くことが
できる。数理計画問題は、制約条件の下で関数を最小化・最大化する問題だ。

Calc には現在、数種類のエンジンが備わっている：

* :abbr:`DEPS (Differential Evolution & Particle Swarm Optimization)`
  Evolutionary Algorithm
* :abbr:`SCO (Social Cognitive Optimization)` Evolutionary Algorithm
* LibreOffice CoinMP Linear Solver
* LibreOffice Linear Solver
* LibreOffice Swarm Non-Linear Solver (experimental)

.. caution::

   Swarm Non-Linear Solver は実験的であり、Calc の将来の版では消える可能性があ
   る。

DEPS および SCO Evolutionary Algorithms は非線形問題を解くためのもので、計算機に
Java ランタイム環境がインストールされており、|OptionsDlg|
|LibreOfficeAdvancedPage| で :guilabel:`Use a Java runtime environment` がオンで
ある場合に限り使用可能だ。DEPS Evolutionary Algorithm が利用可能である場合、
LibreOffice CoinMP Linear Solver が既定となる。

問題を解くのに solver を用いるのであれば、問題を次のように定式化しないといけな
い：

決定変数
   :math:`n` 個の非負変数 :math:`{x_1, ..., x_n}` の集合
制約
   決定変数を含む一次等式または不等式の集合
目的関数
   決定変数を含む一次式

通常、目的は制約条件を満たし、目的関数の結果を最大化または最小化する決定変数の値
を見つけることだ。

.. note::

   Solver 設定は ODS ファイルに保存されて、各タブは独自のモデルを持つことが可能
   だ。

Solver dialog
----------------------------------------------------------------------

:menuselection:`&Tools-->Sol&ver...` 実行で :guilabel:`Solver` ダイアログボック
スが開く。

.. note::

   計算機の構成によっては、Calc を起動してから初めてこれを実施するとメッセージが
   表示される場合がある。メッセージ内容は、システム上の Java 実行環境 (JRE) の存
   在によって変わる。JRE が検出されない場合、メッセージは単にその旨の警告だ。
   JRE が検出されたが、|OptionsDlg| |LibreOfficeAdvancedPage| で :guilabel:`Use
   a Java runtime environment` がオフである場合は、それをオンにするためのボタン
   が表示される。

:guilabel:`&Target cell`
   目的関数への升目参照を打ち込むかマウスで選択する。
:guilabel:`Optimize result to`
   目的関数の最大結果を求めるには :guilabel:`&Maximum` を、最小結果を求めるには
   :guilabel:`Minim&um` を、特定の値に設定するには :guilabel:`&Value of` を選択
   する。:guilabel:`Value of` を選択する場合は必要な値またはその値を含む升目への
   参照を入力する。
:guilabel:`&By changing cells`
   決定変数を定義する升目の位置を入力する。
:guilabel:`&Limiting Conditions`
   この区画に制約を入力する。

   :guilabel:`&Cell reference`
      決定変数への升目参照を入力する。
   :guilabel:`&Operator`
      制約に対する引数を定義する。
   :guilabel:`V&alue`
      制約式に値または升目参照を入力する。
   :guilabel:`Remove button`
      現在定義されている制約を取り除く。

Solver 設定が完了したら :guilabel:`&Solve` を押して値の調整と結果の計算を開始す
る。やり直す場合には :guilabel:`&Reset All` を押してダイアログボックス上をクリア
する。

DEPS Evolutionary Algorithm または SCO Evolutionary Algorithm を使用している場
合、エンジンの実行は定期的に中断して :guilabel:`Solver Status` ダイアログボックス
が開くことがある。

* このダイアログはエンジンの計算の現在の状態に関する診断情報を示すもので、専門家
  にとって興味がある。

  * |OK| を押せばこのダイアログを閉じて計算を終了する。
  * :guilabel:`&Continue` 押せば次のエンジン処理が中断するところまで待機する。
* ダイアログボックスの表示は :guilabel:`Solver Options` ダイアログボックスの
  :guilabel:`Show enhanced solver status` をオフにすると生じない。

成功裡に完了すると、:guilabel:`Solving Result` が開く。これにはボタンが二つある：

* :guilabel:`&Keep Result` を押せば結果を保存する。
* :guilabel:`&Restore Previous` を押せば結果を破棄して直前の値を復元する。

Solver options
----------------------------------------------------------------------

:guilabel:`Solver` 下部の :guilabel:`O&ptions...` ボタンを押すと |OptionsDlg| が
開き、エンジンそれぞれに関する設定を行える。

:guilabel:`&Solver engine`
   標準の LibreOffice をダウンロードし、Java 実行環境を有効にすると、ドロップダ
   ウンリストに選択肢が表示される。

   * `DEPS Evolutionary Algorithm`
   * `SCO Evolutionary Algorithm`
   * `LibreOffice CoinMP Linear Solver`
   * `LibreOffice Linear Solver`
   * `LibreOffice Swarm Non-Linear Solver (experimental)`
:guilabel:`Se&ttings`
   選択エンジンの詳細な処理引数を調整する。選択肢はエンジンによって異なる。

Solver example
----------------------------------------------------------------------

10,000 ドルを投資信託二つに一年間投資するとする。

* ファンド X は金利 8% の低リスクファンドで、
* ファンド Y は金利 12% の高リスクファンドだ。

合計 1,000 ドルの利息を得るためには、それぞれのファンドにいくら投資すればよいか。
この問題を solver を用いて解く。

ワークシートを本文のように埋めて :menuselection:`&Tools-->Sol&ver...` を実行。
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

|MenuBar| :menuselection:`&Data-->Statistics-->` に統計分析コマンド各種が並んで
いる。今見たら 13 コマンドもある。

Sampling tool
----------------------------------------------------------------------

:menuselection:`&Data-->Statistics-->&Sampling...` コマンドは表から標本抽出して
別の表を作成する。

* 抽出はランダムに、または周期的になされる。
* 抽出は行単位で行われる。

.. admonition:: 利用者ノート

   試してみるとテキストデータがゼロになるようだ？

Descriptive Statistics tool
----------------------------------------------------------------------

:menuselection:`&Data-->Statistics-->&Descriptive Statistics...` コマンドは指定
データ集合の主な統計的特性（平均、標準偏差、等々）の報告表を作成する。確率統計の
教科書で出てくる概念と同じだろう。

.. admonition:: 利用者ノート

   こういうダイアログボックスが開くところから始まるコマンドは、実行直前にフィー
   ルドセルを含むデータ集合全体を選択状態にしておくと良い。

.. seealso::

   `Descriptive statistics - Wikipedia
   <https://en.wikipedia.org/wiki/Descriptive_statistics>`__

Analysis of Variance (ANOVA) tool
----------------------------------------------------------------------

:menuselection:`&Data-->Statistics-->&Analysis of Variance (ANOVA)` コマンドは標
本中の複数グループの平均を比較する。

実行するとダイアログボックスが開いて、:guilabel:`&OK` を押すと分析するという流れ
だ。

* 結果にセル領域を相当費やすので、:guilabel:`&Results to` の指定に気をつけろ。
* :guilabel:`Rows &per sample` UI は現在無効。

.. seealso::

   `Analysis of variance - Wikipedia
   <https://en.wikipedia.org/wiki/Analysis_of_variance>`__

Correlation tool
----------------------------------------------------------------------

:menuselection:`&Data-->Statistics-->&Correlation...` コマンドは数値データの組の
相関を計算し、相関係数を求める。

本書の例では数学、物理、生物の得点間の相関を検証するものということになる。出力を
見ればどう理解すればいいかわかるだろう。

.. seealso::

   `Correlation - Wikipedia <https://en.wikipedia.org/wiki/Correlation>`__

Covariance tool
----------------------------------------------------------------------

:menuselection:`&Data-->Statistics-->&Covariance...` コマンドは共分散、数値デー
タセットが共にどれだけ変化するかを測定する。

ダイアログボックスの UI は相関係数コマンドと同じだ。

.. seealso::

   `Covariance - Wikipedia <https://en.wikipedia.org/wiki/Covariance>`__

Exponential Smoothing tool
----------------------------------------------------------------------

:menuselection:`&Data-->Statistics > Exponential Smoothing...` コマンドは、平滑
化された結果を生成するようにデータ集合をいじる。株式市場分析や標本測定などの分野
で用いられる機能とのことだ。

ダイアログボックス上の減衰係数 :guilabel:`&Smoothing factor` はコマンド実行後で
も対応するセルの値を編集することで結果を更新することが可能だ。

.. seealso::

   `Exponential smoothing - Wikipedia
   <https://en.wikipedia.org/wiki/Exponential_smoothing>`__

Moving Average tool
----------------------------------------------------------------------

:menuselection:`&Data-->Statistics-->&Moving Average...` コマンドは時系列データ
集合の移動平均を計算する。コマンドを実行するとダイアログボックスが開く。

* :guilabel:`&Trim input range to actual data content` をオンにすると、計算前に
  入力範囲を実際のデータ内容に刈り取ることを許可する。処理性能に影響する。

.. seealso::

   `Moving average - Wikipedia <https://en.wikipedia.org/wiki/Moving_average>`__

Regression tool
----------------------------------------------------------------------

:menuselection:`&Data-->Statistics-->&Regression...` コマンドは独立変数複数個と
従属変数一個からなるデータセットの線形回帰、対数回帰、累乗回帰のいずれかの分析を
行う。

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

:menuselection:`&Data-->Statistics-->Paired &t-test...` コマンドは t 検定を実行
する。関連する標本集合二つの母平均を比較し、それらの差を決定する。

ダイアログボックスは統計コマンドでよくある単純なものだ。

* 出力表では、アルファと仮説平均差に異なる値を挿入可能。t 値各種は自動更新。

.. seealso::

   `Student's t-test - Wikipedia
   <https://en.wikipedia.org/wiki/Student's_t-test>`__

F-test tool
----------------------------------------------------------------------

:menuselection:`&Data-->Statistics-->&F-test...` コマンドは標本二つの F 検定を行
う。母集団二つの分散が等しいという仮説を検定する。

.. seealso::

   `F-test - Wikipedia <https://en.wikipedia.org/wiki/F-test>`__

Z-test tool
----------------------------------------------------------------------

:menuselection:`&Data-->Statistics-->&Z-test...` コマンドは標本二つの Z 検定を行
う。帰無仮説を検定する。

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

:menuselection:`&Data-->Statistics-->&Chi-square Test...` コマンドは標本の
:math:`\xi^2` 検定を計算し、測定値集合が対応する期待値集合にどの程度適合するかを
決定する。

例によってワークシートの Alpha 値を手動で変更して、関連項目を自動更新することが
可能だ。本コマンドでは Critical Value 欄がそうなる。

.. seealso::

   `Chi-squared test - Wikipedia
   <https://en.wikipedia.org/wiki/Chi-squared_test>`__

Fourier Analysis tool
----------------------------------------------------------------------

:menuselection:`&Data-->Statistics-->F&ourier Analysis...` コマンドは複素数の入
力配列の離散 Fourier 変換を計算することにより、データ集合の Fourier 解析を行う。

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

----

.. rubric:: 章末注

.. [#calc10-footer-1] Navigator については |Calc01| を見ろ。
