======================================================================
Environment Variables 利用ノート
======================================================================

.. |ev| replace:: `Environment Variables`_

本稿は PowerToys の |ev| 機能に関する記述だ。

.. attention::

   :doc:`./index` 冒頭の前提条件に留意すること。

.. contents:: 見出し一覧
   :local:

概要
======================================================================

|ev| は当然ながら環境変数を操作するツールだ。GUI で環境変数を追加、編集、削除す
るほかにも、プロファイルという環境変数集合を扱う機能がある。

.. admonition:: 利用者ノート

   私の持っているツールでは `Rapid Environment Editor`_ がこれに近い用途だ。

プロファイル
----------------------------------------------------------------------

プロファイル一つを環境変数の集合のように扱える。

プロファイルを適用すると、そこで定義されている変数がバックグラウンドでユーザー環
境変数に追加される。重要なのは同名のユーザー変数がすでに存在する場合だ。このと
き、ユーザー変数にバックアップ変数が作成され、プロファイルの適用解除時にオリジナ
ルの値が復元される。プロファイルをスタックのように考えればいい。

プロファイル環境変数は通常の環境変数（ユーザーおよびシステム）に優先する。

Environment Variables ウィンドウ
======================================================================

:guilabel:`New profile`
   このボタンを押すと :guilabel:`New profile` ダイアログボックスが現れる。そこで
   プロファイルを作成する。
:guilabel:`Profiles`
   プロファイルの一覧。各項目に On/Off スイッチと三点メニューボタンがある。

   プロファイル項目のスイッチはプロファイルが保持する環境変数すべての有効と無効
   の状態に対応する。

   プロファイル項目の三点ボタンを押すと、そのプロファイルを操作するメニューを開
   く。内容は次のとおり：

   :menuselection:`Edit`
      対象プロファイルに対する :guilabel:`Edit profile` ダイアログボックスを開く。
   :menuselection:`Remove`
      対象プロファイルを削除する。確認ダイアログボックスあり。
:guilabel:`Default variables`
   ユーザーおよびシステム環境変数の、PowerToys 未使用時における一覧。

   :guilabel:`User` と :guilabel:`System` それぞれで次の操作が可能だ：

   :guilabel:`Add variable`
      同名のダイアログボックスを開く。そこで新規環境変数を追加する。追加後、この
      ボタンの下にある一覧でその変数を確認できる。

   各環境変数の三点ボタンをクリックすると、次の操作への UI が現れる：

   :menuselection:`Edit`
      対象環境変数の名前 and/or 値を変更することが可能だ。
   :menuselection:`Remove`
      対象環境変数を削除する。確認ダイアログボックスあり。
:guilabel:`Applied variables`
   最終的な環境変数集合の一覧。

New / Edit profile ダイアログボックス
----------------------------------------------------------------------

プロファイル一つの特性を定義するダイアログボックスだ。

:guilabel:`Name`
   対象プロファイルに名前を与える。任意の文字が使えるはずだ。
:guilabel:`Enable`
   On にすれば対象プロファイルを活かす。
:guilabel:`Variables`
   対象プロファイルが保持する環境変数の集合。
:guilabel:`Add variable`
   環境変数を追加するためのタイトルなしダイアログボックスを開く。

   :guilabel:`New` タブは見ればわかる。

   :guilabel:`Existing` タブは既存の環境変数一覧であり、加工したいものにチェック
   を入れて :guilabel:`Add` を押すと、選択項目すべてが :guilabel:`Variables` 一
   覧に含まれている。

Add / Edit variable ダイアログボックス
----------------------------------------------------------------------

見ればわかる UI であるので割愛。

設定
======================================================================

まずは :guilabel:`Enable Environment Variables` を On にする。これにより、システ
ムは上述の :guilabel:`Applied variables` の内容が効いている状態になる。

Activation
----------------------------------------------------------------------

:guilabel:`Open Environment Variables`
   クリックすると :guilabel:`Environment Variables` ウィンドウが開く。
:guilabel:`Open as administrator`
   ツールの目的を考慮すれば On でなければならない。グレーアウトされているから
   誤って Off にする心配は無用だ。

.. _Environment Variables: https://learn.microsoft.com/en-us/windows/powertoys/environment-variables
.. _Rapid Environment Editor: https://www.rapidee.com/

.. 以上
