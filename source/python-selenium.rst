======================================================================
Selenium 利用ノート
======================================================================

Python での Selenium_ の利用について記す。

.. contents:: ノート目次

目的
======================================================================

私が Selenium_ を利用する目的を記す。

Selenium_ はウェブブラウザーの操作を自動化する基板となる一連のツールやライブラリー群だ。
例えば Twitter や GitHub にログインするときの定番の UI 操作手順を自動化したり、
インターネットと連動したゲームのプレイヤーデータを scraping したりするのに応用することが考えられる。
事実、ひじょうに便利な Python スクリプトが作れる。

ちなみに、Python には `BeautifulSoup`_ という有力な scraping パッケージが存在する。
これは静的な HTML の解析には向いているものの、JavaScript を駆使した動的な HTML には弱い。
一方 Selenium は逆に動的な処理のための API が提供されているが、いちいちブラウザーのプロセスを介在する必要がある。
したがって用途に応じてこれらのパッケージを選択するのが現実的な戦略だ。

導入
======================================================================

Python 3.7 以上が動作している Windows 10 環境に Selenium_ をインストールする手順を記す。
なお、ブラウザーは MS Edge を想定する。

Selenium_ の構成要素は大別して二つある。プログラミングに関するものとウェブブラウザーに関するものだ。
私はもっぱら Python しか書かないので言語を Python に絞って導入手順を記す。
ウェブブラウザーについては、Chrome, Firefox, Safari, Internet Explorer, Microsoft Edge などの
ドライバーがあるので、自分の利用するブラウザーに対応するドライバーを一つ（あるいは複数）ダウンロードして適宜インストールする。

Python 用パッケージを導入する
----------------------------------------------------------------------

Selenium_ の Python パッケージをインストールする手順を記す。

手順はひじょうに簡単で、他のサードパーティー製 Python パッケージと同様だ。すなわち：

.. code:: console

   bash$ pip install selenium

アップグレードやアンインストールも標準の手順に従う。

.. code:: console

   bash$ pip install -U selenium
   bash$ pip uninstall selenium

MS Edge 用 WebDriver を導入する
----------------------------------------------------------------------

WebDriver のインストール手順を述べる。MS Edge の WebDriver のインストールは OS の機能を用いて行う。

+ Windows の設定画面を開く。
+ :guilabel:`アプリと機能` に進み :guilabel:`オプション機能` を選択する。
+ :guilabel:`Microsoft WebDriver` を選択する。

いったん上記の手順を実施すると、これ以上 Windows Update のタイミングで
MS Edge のバージョンと WebDriver のそれが同調することが期待できる。

初回動作確認
======================================================================

Selenium_ の一連の構成部品をインストールしたら、公式文書にある Getting Started
のコードを真似たものを実行して様子を見るといい。ブラウザーが新規に開いて、
指定の HTML ファイルが表示されるというようなもので十分だ。

それが終わったら本ページの末端にある参考資料を一読することを勧める。

コード例
======================================================================

ここでは私が実際に使い物になる、パターン化されていると感じたコードを挙げていく。
基本的なものから、私しか使わなそうな特別なものまで無差別に列挙する。

これ以降にあげるコード片は次の文を事前に実行しているものと仮定する：

.. code:: python

   from selenium import webdriver

   driver = webdriver.Edge()


HTML ファイルをブラウザーで開く
----------------------------------------------------------------------

URL またはローカルファイルパスを指定してブラウザーを開く。

.. code:: python

   driver.get('http://www.python.org')
   driver.get('file://C:/Temp/tmp.html')

AJAX をふんだんに用いているページを開くときは、呼び出し直後に完全にロードし切れていないと思ったほうがいい。
そういう状況では後述の技法を併用する。

ドライバー管理下のブラウザーを閉じる
----------------------------------------------------------------------

ブラウザーごと終了するのであれば ``quit()`` を、タブを閉じるのであれば ``close()`` を呼ぶ。
ただしタブが一つの場合は事実上ブラウザーが終了する。

.. code:: python

   driver = ...
   driver.get(...)
   try:
       ...
   finally:
       driver.close() or driver.quit()

私は Selenium を使うときしか MS Edge を使わないのでどちらでもいい。

特定の HTML 要素を発見する
----------------------------------------------------------------------

画面に表示されているページの HTML ソースが含む ``a``, ``input``, ``img`` などの
各種要素にアクセスするためのコードは重要だ。
ページ末端に挙げるマニュアルで各インターフェイスの特性を把握しておくこと。

要点をまとめておく。

* ``driver.find_element_by_`` 系メソッドは指定条件を満たす要素を表現するオブジェクト一つを返すか、
  見つからないときは例外を送出する。一方、
  ``driver.find_elements_by_`` 系メソッドは指定条件を満たす要素を表現するオブジェクトを
  0 個以上含む `list` オブジェクトの形で返す。

* 要素の指定方法は次のものになる：

  * 要素のタグ名による
  * 要素の ``id`` 属性の値による
  * 要素の ``name`` 属性の値による
  * 要素の場所を指定する CSS セレクターによる
  * 要素の場所を指定する XPath による

  最初の三つについては HTML をツールなしで書ける者であれば説明不要だと思う。
  CSS セレクターによる要素の場所特定は `BeautifulSoup`_ でもサポートしている。
  Selenium は XPath による指定も提供している。

  次に Selenium の非公式文書で紹介されているリンクを引用する。
  CSS セレクターと XPath に馴染みがないのであれば、リンク先で学習することだ：

  * `W3Schools XPath Tutorial <https://www.w3schools.com/xml/xpath_intro.asp>`__
  * `W3C XPath Recommendation <http://www.w3.org/TR/xpath>`__
  * `XPath Tutorial <http://www.zvon.org/comp/r/tut-XPath_1.html>`__

.. code:: python

   images = driver.find_elements_by_css_selector('div#porno-album > a > img')

HTML 要素の指定する属性の値を得る
----------------------------------------------------------------------

HTML 要素から属性の値を得るには ``elem.get_attribute()`` を用いる。
例えば、次の要素 ``elem`` から ``src`` を得たいとする：

.. code:: html

   <img name="porno-001" src="/path/to/porno-001.jpg" />

このときは次のようにする：

.. code:: python

   jpeg_url = elem.get_attribute('src')

もっと現実的な例を示す。今、画像が一列に並んでいるページを開いたものと仮定する。
それらの画像の要素 ``img`` から属性 ``src`` の値、すなわち画像の URL を取得して
``list`` オブジェクト ``image_paths`` を作成するというものだ。

このコード作成者は URL 一覧をテキストファイルに出力し、
コンソールで別途 :program:``wget`` を実行することでポルノ画像の一括ダウンロードを企んでいる。

.. code:: python

   images = driver.find_elements_by_css_selector('div#porno-album > a > img')
   image_paths = [i.get_attribute('src') for i in images]

HTML 要素の値を得る
----------------------------------------------------------------------

HTML 要素の値を得るには ``elem.text`` を参照する。開始タグと終了タグに挟まれた部分の
ブラウザーに描画されているテキスト内容と同等の ``str`` オブジェクトが得られる。

キー操作
----------------------------------------------------------------------

Selenium はキーボードのキー操作を再現するインターフェイスを提供している。
それを利用するには次の ``import`` 文が必要だ：

.. code:: python

   from selenium.webdriver.common.keys import Keys

現在の画面にキーイベントを送るには例えば次のようにする。
もっと自然なコードがあるかもしれない。

.. code:: python

   from selenium.webdriver.common.action_chains import ActionChains

   ...

   actions = ActionChains(driver)
   actions.send_keys(Keys.HOME)
   actions.send_keys(Keys.END)
   actions.perform()

特定の HTML 要素に対してキーイベントを送るには例えば次のようにする：

.. code:: python

   user_name = driver.find_elements_by_css_selector('input[id="user_name"]')
   user_name.send_keys('showa_yojyo')

フォーム操作
----------------------------------------------------------------------

ボタン系 GUI のマウスクリックとフォーム送信のコード例を示す。
ページの HTML のフォーム部分はこのようになっていると仮定する：

.. code:: html

   <form method="post" action="...">
       <input type="checkbox" id="agree" value="1" />
       <label for="agree">利用上の注意に同意する</label>
       <div>
           <button type="submit" id="sign-in">確認画面へ</button>
       </div>
   </form>

ユーザーは通常この画面をブラウザーで開いてチェックボックス「利用上の注意に同意する」をクリックしてチェックを入れる。
それからボタン「確認画面へ」をクリックするなどしてフォームを送信する。
これを WebDriver で自動化するとこうなる：

.. code:: python

   agree = driver.find_element_by_id('agree')
   agree.click()
   assert agree.is_selected()

   sign_in = driver.find_element_by_id('sign-in')
   sign_in.click() or sign_in.submit()

``.submit()`` に関しては当該フォーム内のコントロールであれば何でもいい。
``form`` 本体でも構わない。

待機
----------------------------------------------------------------------

Selenium プログラミングで最初の壁となる待機処理について簡単に記す。

基本的には ``driver.get(URL)`` の呼び出し直後には指定アドレスのページがロードされた直後だと考えるべきだ。
しかし、先述のように AJAX バリバリのページにおいては、ブラウザーに画面が出たかたとはいえ、
その内容のすべてがロードされているとは限らない。

あるいはボタンをクリックすることにより別のページに移動するようなサイトにおいては、
``button.click()`` の呼び出し直後では、むしろ次のページは部分的にしかロードされていないと考えるべきだ。

ページが不完全な状態で WebDriver の ``find_element`` 系メソッドを呼び出すと失敗することがある。
それを回避する手段が待機だ。

Selenium は「指定要素が指定状態になるまでプログラム実行を進行しない」機能を提供している。
これを待機と呼ぶことにする。待機は明示的待機と暗黙的待機の二つに分類される。

明示的待機
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

明示的待機を説明する。例えば登録画面、プログレスバー表示画面、終了画面という遷移を考える。
終了画面が出る前に ``.close()`` したくないはずなので、次のようにする：

.. code:: python

   from selenium.webdriver.common.by import By
   from selenium.webdriver.support import expected_conditions
   from selenium.webdriver.support.ui import WebDriverWait

   ...

   # 登録画面終了

   # 進捗表示画面 - ここを正常に抜けないと登録手続きが破壊される

   wait = WebDriverWait(driver, 60)
   wait.until(expected_conditions.title_contains('受付終了'))

   # 仮にここで driver.find_element_by_tag_name('title') を実行すれば
   # 例外は送出されないはずだ

   # ユーザーの目的は進捗表示画面が完全終了の時点で達せられた
   # ブラウザーを閉じる
   driver.close()

これにより（実際の処理が 60 秒で収まれば）ユーザーの期待する手続きは
Selenium が代わりに達成する。

暗黙的待機
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

暗黙的待機を説明する。これは待機可能な構成要素すべてに関して待機時間上限の既定値を設定するものだ。
指定後は上記のような ``.until()`` をしなくても ``.until()`` 相当のことをしてくれる。

.. code:: python

   driver = Edge()
   driver.implicitly_wait(60)

テスト・デバッグ例
======================================================================

TBW: 職人的な技法がありそうだ。

実例
======================================================================

TODO: 私の GitHub repository の bin にいくつか使用例があるので紹介する。

* ``wifiota.py``: 大田区図書館の Free Wi-Fi 再接続を要求する際に実行するスクリプト。
* ``mjnet.py``: セガ MJ Arcade ユーザーサイト MJ.NET のゲームスコアを自動的に取得するスクリプト。

参考資料
======================================================================

Selenium_ を用いた簡単なコードを書けるようになったら、次の二つの文書を順に読むとよい。

* `Selenium with Python <https://selenium-python.readthedocs.io/>`_
* `Selenium クイックリファレンス <https://www.seleniumqref.com/>`_

悩んだときは Google で適当にキーワードを検索する。Stack Overflow でだいたい解決済みだ。

.. _BeautifulSoup: http://www.crummy.com/software/BeautifulSoup/bs4/
.. _Selenium: https://github.com/SeleniumHQ/selenium/
