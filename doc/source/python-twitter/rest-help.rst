======================================================================
ヘルプ関連
======================================================================

本節では help 系 API について述べる。 Twitter の利用者からすれば、これらの機能は
特に有用ではないが、万全を期すために記す。

名前が help で始める機能は四つあり、いずれもパラメーターを取らないという際立った
特徴がある。応答データの一部テキストがユーザーの言語設定に依存するとはいえ、本質
的には取得データは特定のユーザーに依存しない情報である。

サンプルコードは次のものを参照して欲しい。

`bin/twhelp.py <https://github.com/showa-yojyo/bin/blob/master/twhelp.py>`_

.. contents::

GET help/configuration
======================================================================

GET help/configuration を用いることで現在の Twitter の構成情報が得られる。次のよ
うな情報からなる。

* ダイレクトメッセージの文字数上限
* 画像サイズの上限
* 短縮 URL の文字数
* screen_name として禁じられている文字列

手許で試した結果、Twitter のドキュメントの出力例と一致したため、実行例を省く。

GET help/languages
======================================================================

GET help/languages を用いることで Twitter がサポートする言語の集合を得ることがで
きる。前述したように一部テキストが日本語で得られる。

先のデモコードによる実行例を示す（出力を一部省略する）。全部で 33 言語をサポート
していることがわかった。

.. code:: console

   bash$ ./twhelp.py help/languages
   [
       {
           "code": "fr",
           "name": "フランス語",
           "status": "production"
       },
       {
           "code": "en",
           "name": "英語",
           "status": "production"
       },
       {
           "code": "ar",
           "name": "アラビア語",
           "status": "production"
       },
       {
           "code": "ja",
           "name": "日本語",
           "status": "production"
       },
       ...
       {
           "code": "bn",
           "name": "ベンガル語"
           "status": "production",
       }
   ]

GET help/privacy
======================================================================

GET help/privacy を用いると Twitter の privacy policy の文言を得られる。私が実行
すると日本語の文章を含む JSON が返ってきた。それはこのドキュメントの文言と同じ文
章だった。

`Privacy Policy | Twitter <https://twitter.com/privacy?lang=ja>`_

GET help/tos
======================================================================

GET help/tos を用いると Twitter の利用規約の文言が上述のものと同様に得られる。

`Terms of Service | Twitter <https://twitter.com/tos?lang=ja>`_

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
