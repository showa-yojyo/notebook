======================================================================
クラス ``AppBase`` の実装
======================================================================

単純な PyOpenGL のプログラムは、どれも構造と手続きが似通ったものになる。このノー
トではサンプルプログラムを多数書くつもりでいるので、それらに共通しているプログラ
ミング要素を、オブジェクト指向プログラミング的着想によってクラスとしてカプセル化
しておく。

ただし、歴史的な事情によりそのようなクラスを単一のクラスで表現し切ることは無理が
あるようだ。 OpenGL 3.0 以前と以後とで、プログラミングの方法論がまるで別物なの
で、以前、以後に対応するベースクラスをそれぞれ設計することになる。

本稿では、それらのベースクラスのベースクラス ``AppBase`` を設計する。

.. contents::

クラス ``AppBase``
======================================================================

先にクラス全景を次に示す。

.. literalinclude:: /_sample/pyopengl/appbase.py
   :language: python3

このクラスの目的は次のとおりだ：

* 新しいサンプルコードを書くときは、このクラスのサブクラスを定義する形にすること
  で、コードの重複を積極的に少なくする。特にメソッドのオーバーライドにより、描画
  や操作の「差分」の実装だけで済むようにする。
* サブクラスでコンテキストバージョンを指定することで、そのアプリケーションが
  deprecated features を採用するかどうかを明示する。
* コンテキスト情報の出力や FPS の表示等、全サンプルコードが利用しがちな機能を提
  供する。

このクラスの利用方法は後述のページで見ていくことになるので、このページの残りで
は、このクラス自体のポイントを記す。

機能概要
----------------------------------------------------------------------

クラス ``AppBase`` で実装する機能を述べる。

コンテキストバージョン指定機能
  OpenGL のコンテキストバージョンをコンストラクターで指定できる。サブクラスから
  指定することになる。
ウィンドウタイトル設定機能
  ウィンドウタイトルバーに表示するタイトル文字列を指定できる。ただし、アスキー文
  字のみのもよう。
FPS リアルタイム表示機能
  ウィンドウタイトルバーに FPS を表示する。0.25 秒ごとに更新。
ウィンドウサイズ・位置の指定機能
  ウィンドウの初期サイズ、初期表示位置をクラスのコンストラクターで指定できる。
OpenGL サポートバージョン情報表示機能
  ウィンドウ表示までに、次のような情報をコンソールに出力する。最後の GLSL に関す
  る情報については、プログラムが利用する OpenGL のバージョンが 2.0 以上のときし
  か表示しないし、することができない。

  .. code:: text

     Vendor: Intel
     Renderer: Intel(R) HD Graphics
     Version: 3.1.0 - Build 9.17.10.4101
     GLSL: 1.40 - Intel Build 9.17.10.4101

ウィンドウサイズ変更時ビューポート自動更新機能
  ウィンドウサイズ変更時に可能な限り OpenGL のビューポートをウィンドウの全クライ
  アント領域に更新する。
マウスドラッグによるズーム・回転機能
  左ボタンドラッグで描画モデルの回転、右ボタンドラッグでモデルにズームする。
  :doc:`view-navigation` も参照。
透視射影パラメーターの設定機能
  関数 ``gluPerspective`` またはそれと同等のパラメーターを任意に設定可能。
カメラパラメーターの設定機能
  関数 ``gluLookAt`` またはそれと同等のパラメーターを任意に設定可能。
GLSL オブジェクトの管理機能
  プログラムオブジェクトをシェーダーオブジェクトの生成、破棄処理を管理する。詳細
  は :doc:`program-manager` を参照。
アプリケーション終了機能
  :kbd:`Esc` キーを押すと、アプリケーションを終了する。

利用方法
----------------------------------------------------------------------

本クラスはオブジェクト化して利用するのではなく、ベースクラスとして利用する。サブ
クラスとしてアプリケーションを実装するサンプルのときに記す。

.. include:: /_include/python-refs-vision.txt
