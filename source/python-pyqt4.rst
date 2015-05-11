======================================================================
PyQt4 利用ノート
======================================================================

.. contents:: ノート目次

.. note::

   * OS: Windows XP Home Edition SP 3
   * 本稿執筆にあたり利用した各パッケージのバージョンは次のとおり。

     * Python_: 2.6.6, 2.7.3
     * PyQt_: GPL 4.8.4 for Python v 2.6 (x86),
       GPL v4.9.4 for Python v2.7 (x86)

関連リンクおよび参考サイト
======================================================================

PyQt_
  PyQt 紹介ページ。リリースニュース、ダウンロード、ドキュメントへの各リンクを提供している。

`PyQt Download`_
  自分の環境の Python のバージョンに合ったインストーラーを選択するべし。

`Qt Reference Documentation 4.7`_
  Qt 総本山のドキュメント。ここから調査スタートすればよかった。

`PyQt Wiki Tutorials`_
  チュートリアル文書へのリンクページ。
  全部はチェックしていない。

`The PyQt Tutorial`_
  GUI をコーディングで実装するタイプのチュートリアル。
  最終的にテトリス簡易版を実装する。
  テトリス実装例は PyQt 配布物の ``examples`` 内にもある。

インストール
======================================================================

インストール方法は、よくある Python パッケージとは異なる。
easy_install/pip を利用するわけではないし、
ソースコードの ``setup.py build``, ``setup.py install`` でもない。

`PyQt Download`_ のページで Windows 用のインストーラーをダウンロードし、
それを実行するだけで終了となる。

* インストールが無事に終了すると、
  Windows のスタートメニューから適当に辿っていくと
  ``PyQt GPL v4.8.4 for Python v2.6 (x86)`` のような項目ができているはずだ。

* まずは ``Examples`` > ``PyQt Examples and Demos`` を選択するとよい。
  PyQt で実装された様々なデモアプリのランチャーが出現する。
  画面左のリストから何か興味のあるものを選択して、
  画面下の ``Launch`` ボタンを押すと、デモが開始する。

ドキュメント
======================================================================
前述のスタートメニューの ``Documentation`` > ``Qt Documentation`` を選択すると、
オンラインヘルプがブラウザーで読める。

PyQt を利用したプログラムを作成する
======================================================================

* 事実関係

  * Qt Desinger は GUI を XML ファイルとして記述、保存するためのツール。
  * 記述ファイルの拡張子は ``.ui`` となる。
  * Qt Desinger 付属のバッチファイル :file:`pyuic4.bat` は
    ui ファイルから py コードを生成するものだ。
  * Python コードから ui ファイルに定義されている GUI を利用することができる。
    方法は二系統あり、ui ファイルを直接ロードするものと、
    バッチで生成した py モジュールのクラスをインスタンス化する方法にわかれる。

* コメント

  * まずは Qt Designer の利用方法を習得する。
    目標は次の方法を習得することとしよう。

    * ui ファイルを保存する方法。
    * ui ファイルから py ファイルを生成する方法。
    * ui ファイルで定義した Widget を自作プログラムが利用する方法。

Qt Desinger
----------------------------------------------------------------------

.. todo::

   Designer のチュートリアルを探す。

前述スタートメニューの ``Designer`` を選択する。

* Designer は GUI を設計するためのツール。
  設計内容は拡張子 ui のファイルに「上書き保存」または「名前を付けて保存」する。

* 新規 widget を作成すると、真っ白なウィンドウを画面中央に出す。
  あとは一般的な RAD ツールと同じように、子 widget をゴテゴテ盛っていく。

  * 各 widget 要素の変数名等のプロパティを変更するには、
    画面右のオブジェクトインスペクタやプロパティエディタを利用する。

* 「フォーム＞プレビュー」のショートカットキーは ``Ctrl + R`` のようだ。

* 「フォーム＞コードを表示」メニュー項目は使いものにならない。
  手動で ``ui`` ファイルから ``py`` ファイルを生成するしかない。

  PyQt4 インストールフォルダーにある ``pyuic4.bat``
  をパスの通ったフォルダーにコピーして、コンソールから同バッチを実行する。
  コマンドライン引数は Designer で保存した ``ui`` ファイル一丁。

  .. code-block:: console

     > pyuic4.bat myform.ui > ui_myform.py

* 一番親の widget にレイアウトを設定するにはコツが要る。
  ある程度子 widget を親 widget に搭載したら、親で右クリックメニュー表示。
  「レイアウト」のサブメニューに色々あるので、所望の配置スタイルを選択する。

* Signal/Slot の編集はかなり直感的に設定できる。

  * ``F4`` キーで Signal/Slot 編集モードに移行。
    ``connect`` 関係を定義したい widget 間をドラッグアンドドロップ。
    ドロップ直後にわかりやすい入力フォームが現れるので、そこで指示。

  * なお ``F3`` キーで GUI 編集モードに移行。

以降の説明では、各ファイル名を次のように決めたものとする。

.. csv-table::
   :header: "ファイルの名前","ファイルの意味"

   :file:`myform.ui`,Qt Designer での GUI 設計内容を保存した XML ファイル。
   :file:`ui_myform.py`,上記 ui ファイルを :file:`pyuic4.bat` でコンバートした内容を保存したもの。
   :file:`myapp.py`,設計した GUI を利用する Python スクリプトファイル。

ui ファイルから生成した py ファイルの利用法
----------------------------------------------------------------------
ファイル :file:`ui_myform.py` をそのまま実行しても、
Qt Designer で設計した Widget が出てくるわけではない。
別のコード（ここでは :file:`myapp.py` としている）から ``import`` して利用する。

色々な流儀があるので、以下に記す。

myform.Ui_Form インスタンスを作成する方法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import sys
   from PyQt4.QtGui import QApplication, QWidget

   # pyuic4.bat myform.ui > ui_myform.py
   from ui_myform import Ui_Form

   if __name__ == '__main__':
       app = QApplication(sys.argv)
       window = QWidget()
       ui = Ui_Form()
       ui.setupUi(window)

       window.show()
       sys.exit(app.exec_())


QWidget のサブクラスで UI_Form.setupUI を利用する方法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # インポートは先程と同様。

   class Form(QWidget):
       def __init__(self):
           QWidget.__init__(self)

           # Set up the user interface from Designer.
           self.ui = Ui_Form()
           self.ui.setupUi(self)

           # Connect up the buttons.
           self.ui.pushButton.clicked.connect(self.accept)

       def accept(self):
           pass

   if __name__ == '__main__':
       app = QApplication(sys.argv)
       window = Form()

       window.show()
       sys.exit(app.exec_())


QWidget と Ui_Form のサブクラスで setupUI を利用する方法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # インポートは先程と同様。

   class Form(QWidget, Ui_Form):
       def __init__(self):
           QWidget.__init__(self)
           self.setupUi(self)
           self.pushButton.clicked.connect(self.accept)

   # main は先程と同様。


ui ファイルから直接 Widget をロードする方法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
関数 ``uic.loadUI`` を利用する。

.. code-block:: python

   import sys
   from PyQt4 import QtGui, uic

   if __name__ == '__main__':
       app = QtGui.QApplication(sys.argv)
       window = uic.loadUi('myform.ui')

       window.show()
       sys.exit(app.exec_())

サブクラスに差し替える方法
----------------------------------------------------------------------
例えば ``QTextBrowser`` を自分でこれから作成する予定のサブクラス
``QMyTextBrowser`` に差し替えたい場合は次の手順をとる。

1. デザイナー画面の ``QTextBrowser`` アイテム上で右クリックメニューを表示し、
   <格上げ先を指定...> を選択する。

2. 入力フォームが出現する。
   下部にある <格上げされたクラス名> に ``QMyTextBrowser`` と入力する。

3. <追加> を押す。
4. <格上げ> を押す。

5. デザイナーで ui ファイルを保存する。
6. ``pyuic4.bat`` で ui ファイルから py ファイルを生成すると、
   ファイルの下の方に ``import qmytextbrowser`` という行が入っているハズ。

7. :file:`qmytextbrowser.py` ファイルを作成し、
   自分でクラスを実装すればよい。

   .. code-block:: python

      from PyQt4 import QtGui

      class QMyTextBrowser(QtGui.QTextBrowser):
          ...

.. include:: /_include/python-refs-core.txt
.. _PyQt: http://www.riverbankcomputing.co.uk/software/pyqt/intro
.. _`PyQt Download`: http://www.riverbankcomputing.co.uk/software/pyqt/download/
.. _`Qt Reference Documentation 4.7`: http://doc.qt.nokia.com/4.7/
.. _`PyQt Wiki Tutorials`: http://www.diotavelli.net/PyQtWiki/Tutorials
.. _`The PyQt Tutorial`: http://zetcode.com/tutorials/pyqt4/
