======================================================================
PyQt5 利用ノート
======================================================================

本稿は PyQt_ の現時点での最新版、PyQt5 についての覚え書きである。

.. contents:: ノート目次

.. note::

   本稿執筆時の動作環境は次のとおり。

   * OS

     * Windows 7 Home Premium x64 SP1
     * Windows 10 Home x64

   * Python_

     * 3.4.1 (x64)
     * 3.5.2 (x64)

   * PyQt_

     * GPL v5.4.1 for Python v3.4 (x64)
     * 5.5.1 (mmcauliffe)

関連リンク
======================================================================

PyQt_
  PyQt 紹介ページ。
  リリースニュース、ダウンロード、ドキュメントへの各リンクを提供している。

`PyQt Download`_
  自分の環境の Python のバージョンに合ったインストーラーを選択するべし。

`Qt Documentation`_
  Qt (C++) のドキュメント。

`The PyQt Tutorial`_
  GUI をコーディングで実装するタイプのチュートリアル。最終的にテトリス簡易版を実
  装する。テトリス実装例は PyQt 配布物の :file:`examples` 内にもある。

目的
======================================================================

ノートを書いておいてなんだが、今後私が PyQt を本格的に利用することはないと思う。
数年前に PyQt に興味を持った理由は、所有していた私の貧弱な PC でも、Python での
GUI プログラミングならば難なく実現できると考えたからだった。

現在では最近買い替えた PC の性能が良く、自室からインターネットに接続したことと、
ディスク容量が格段に増えたことから、PyQt に頼る必要性がなくなった。むしろ
Microsoft Visual Studio 無料版をインストールしてC# による GUI プログラミングをす
るほうが Windows しか使わない私としては自然な選択だ。

それでも Qt/PyQt はクラスライブラリーを見ているとためになることが多い。ドキュメ
ントを参照するためだけにインストールしたとしても、得なのではないかと思う。

インストール
======================================================================

公式サイトが提供するバイナリーパッケージを利用してインストールする方法と、
Miniconda_ を利用してインストールする方法を記す。前者の方法は Python を標準イン
ストーラーによりインストールした場合に採用し、後者の方法は Miniconda で Python
環境を管理している場合に採用することになるはずだ。

インストーラーによる方法
----------------------------------------------------------------------

#. `PyQt Download`_ のページで利用環境に適した Windows 用のインストーラーをダウ
   ンロードする。本稿では :file:`PyQt5-5.4.1-gpl-Py3.4-Qt5.4.1-x64.exe` をインス
   トーラーとしている。
#. ダウンロード終了後、インストーラーを起動する。

   * 途中の選択肢はほとんどない。Full インストールを選択する程度。
   * 普通はインストールが無事に終了する。

Miniconda による方法
----------------------------------------------------------------------

こちらの方法は手動による設定作業を部分的に要するので自信がない。

以下、デフォルト環境に PyQt5 をインストールする手順を記すが、当然ながら PyQt5 動
作確認用の環境を :program:`conda` を用いて作成して、そこで構築してもよい。その場
合は以下に示す各種ファイルパス等を適宜読み替えて欲しい。

大まかな手順は次の通りだ。すべてコマンドライン処理になる。

#. コマンド :code:`conda install pyqt5` を実行する。
#. 環境変数 ``QT_QPA_PLATFORM_PLUGIN_PATH`` を設定する。

実行例を示す。言い忘れたが Cygwin :program:`bash` のセッションだ。

.. code:: console

   bash$ conda install -c mmcauliffe pyqt5
   Fetching package metadata ...........
   Solving package specifications: ..........

   Package plan for installation in environment D:\Miniconda3:

   The following packages will be downloaded:

       package                    |            build
       ---------------------------|-----------------
       icu-56.1                   |                0        11.1 MB  mmcauliffe
       qt5-5.5.1                  |                0        28.8 MB  mmcauliffe
       pyqt5-5.5.1                |           py35_0         3.9 MB  mmcauliffe
       ------------------------------------------------------------
                                              Total:        43.9 MB

   The following NEW packages will be INSTALLED:

       icu:   56.1-0       mmcauliffe
       pyqt5: 5.5.1-py35_0 mmcauliffe
       qt5:   5.5.1-0      mmcauliffe

   Proceed ([y]/n)?

   Fetching packages ...
   icu-56.1-0.tar 100% |###############################| Time: X:XX:XX XXX.XX kB/s
   qt5-5.5.1-0.ta 100% |###############################| Time: X:XX:XX XXX.XX kB/s
   pyqt5-5.5.1-py 100% |###############################| Time: X:XX:XX XXX.XX kB/s
   Extracting packages ...
   [      COMPLETE      ]|##################################################| 100%
   Linking packages ...
   INFO:progress.update:('pyqt5', 2)#######################                 |  66%
   [      COMPLETE      ]|##################################################| 100%
   INFO:progress.stop:None

   bash$ export QT_QPA_PLATFORM_PLUGIN_PATH='D:/Miniconda3/Library/lib/qt5/plugins/platforms/'

* :program:`conda` のオプション引数に :code:`-c` を追加して、パッケージをダウン
  ロードする channel を明示的に指定する必要があった。いずれ標準のパッケージサイ
  トから入手可能になれば、これは不要になると思われる。
* 最後は :program:`bash` の組み込みコマンドで環境変数を set しているが、恒久的に
  指定してよいのであれば、セッション外で定義する。例えば Windows の環境変数を追
  加するようなやり方で定義する。 PyQt5 稼働テスト用環境とスイッチしながら作業す
  る前提ならば、何か手軽に当該環境変数を set/unset するツールを自作しておくべき
  だろう。

.. note::

   Miniconda の基本利用法については :doc:`/python-miniconda` 参照。

.. note::

   PyQt4 との共存については調査中。特に Matplotlib のバックエンド関連での挙動に
   興味がある。

動作確認
----------------------------------------------------------------------

.. warning::

   本節の内容はインストーラーで PyQt5 をインストールした場合を前提とする。

Windows のスタートメニューから適当に辿っていくと
:guilabel:`PyQt GPL v5.4.1 for Python v3.4 (x64)` のような項目ができている。

まずは :menuselection:`Examples --> PyQt Examples` を選択するとよい。PyQt で実装
された様々なデモアプリのランチャーが出現する。画面左のリストから何か興味のあるも
のを選択して、画面下の :guilabel:`Launch` ボタンを押すと、デモが開始する。

* OpenGL のデモが 2D のもの以外動かない。画面が真っ黒か、描画イベントが来ないか。

  .. figure:: /_images/pyqt5-opengl.png
     :align: center
     :alt: PyQt OpenGL Examples
     :width: 808px
     :height: 627px
     :scale: 50%

ドキュメント
======================================================================

.. warning::

   本節の内容はインストーラーで PyQt5 をインストールした場合を前提とする。

前述のスタートメニューの :menuselection:`Documentation --> Qt Documentation` を
選択すると、`オンラインヘルプ <http://qt-project.org/doc/qt-5/>`_ がブラウザー
で読める。

PyQt を利用したプログラムを作成する
======================================================================

.. warning::

   本節の内容はインストーラーで PyQt5 をインストールした場合を前提とする。

* Qt Desinger は GUI を XML ファイルとして記述、保存するためのツール。

  * PyQt4 のときと同じように使える。

* 記述ファイルの拡張子は ``.ui`` となる。
* Qt Desinger 付属のバッチファイル :file:`pyuic5.bat` は ui ファイルから py コー
  ドを生成するものだ。
* Python コードから ui ファイルに定義されている GUI を利用することができる。方法
  は二系統あり、ui ファイルを直接ロードするものと、バッチで生成した py モジュー
  ルのクラスをインスタンス化する方法にわかれる。

まずは Qt Designer の利用方法を習得する。目標は次の方法を習得することとしよう。

* ui ファイルを保存する方法。
* ui ファイルから py ファイルを生成する方法。
* ui ファイルで定義した Widget を自作プログラムが利用する方法。

Qt Desinger
----------------------------------------------------------------------

前述スタートメニューの :menuselection:`Designer` を選択する。

* Designer は GUI を設計するためのツール。設計内容は拡張子 ui のファイルに
  :menuselection:`上書き保存` または :menuselection:`名前を付けて保存` する。
* 新規 widget を作成すると、真っ白なウィンドウを画面中央に出す。あとは一般的な
  RAD ツールと同じように、子 widget をゴテゴテ盛っていく。

  * 各 widget 要素の変数名等のプロパティを変更するには、画面右のオブジェクトイン
    スペクタやプロパティエディタを利用する。

* :menuselection:`フォーム --> プレビュー` のショートカットキーは :kbd:`Ctrl` +
  :kbd:`R` のようだ。
* :menuselection:`フォーム --> コードを表示` メニュー項目は使いものにならない。
  PyQt4 からこの不具合が解消されていないとは？
  手動で ui ファイルから py ファイルを生成するしかない。

  .. figure:: /_images/pyqt5-designer-uic.png
     :align: center
     :alt: Qt Designer
     :width: 918px
     :height: 651px
     :scale: 50%

  PyQt5 インストールフォルダーにある :file:`pyuic5.bat` をパスの通ったフォルダー
  にコピーして、コンソールから同バッチを実行する。コマンドライン引数は Designer
  で保存した ui ファイル一丁。

  .. code:: console

     bash$ pyuic5.bat myform.ui > ui_myform.py

* 一番親の widget にレイアウトを設定するにはコツが要る。ある程度子 widget を親
  widget に搭載したら、親で右クリックメニュー表示。 :menuselection:`レイアウト`
  のサブメニューに色々あるので、所望の配置スタイルを選択する。

* シグナル/スロットの編集はかなり直感的に設定できる。

  * :kbd:`F4` キーでシグナル/スロット編集モードに移行。connect 関係を定義したい
    widget 間をドラッグアンドドロップ。ドロップ直後にわかりやすい入力フォームが
    現れるので、そこで指示。
  * なお :kbd:`F3` キーで GUI 編集モードに移行。

以降の説明では、各ファイル名を次のように決めたものとする。

.. csv-table::
   :delim: |
   :header-rows: 1
   :widths: auto

   ファイルの名前 | ファイルの意味
   :file:`myform.ui`    | Qt Designer での GUI 設計内容を保存した XML ファイル
   :file:`ui_myform.py` | 上記 ui ファイルを :file:`pyuic5.bat` でコンバートした内容を保存したもの
   :file:`myapp.py`     | 設計した GUI を利用する Python スクリプトファイル

ui ファイルから生成した py ファイルの利用法
----------------------------------------------------------------------

ファイル :file:`ui_myform.py` をそのまま実行しても、 Qt Designer で設計した
Widget が出てくるわけではない。別のコード（ここでは :file:`myapp.py` としてい
る）から import して利用する。

色々な流儀があるので、以下に記す。

``myform.Ui_Form`` インスタンスを作成する方法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: /_sample/pyqt5/myapp1.pyw
   :language: python3

``QWidget`` のサブクラスで ``UI_Form.setupUI`` を利用する方法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: /_sample/pyqt5/myapp2.pyw
   :language: python3
   :lines: 11-

インポートは先程と同様。

``QWidget`` と ``Ui_Form`` のサブクラスで ``setupUI`` を利用する方法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: /_sample/pyqt5/myapp3.pyw
   :language: python3
   :lines: 14-17

インポートと :code:`main` は先程と同様。

ui ファイルから直接 ``Widget`` をロードする方法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

関数 :code:`uic.loadUI` を利用する。

.. literalinclude:: /_sample/pyqt5/myapp4.pyw
   :language: python3

サブクラスに差し替える方法
----------------------------------------------------------------------

例えば ``QTextBrowser`` を自分でこれから作成する予定のサブクラス
``QMyTextBrowser`` に差し替えたい場合は次の手順をとる。

#. デザイナー画面の ``QTextBrowser`` アイテム上で右クリックメニューを表示し、
   :menuselection:`格上げ先を指定...` を選択する。
#. 入力フォームが出現する。下部にある :guilabel:`格上げされたクラス名` に
   ``QMyTextBrowser`` と入力する。
#. :guilabel:`追加` を押す。
#. :guilabel:`格上げ` を押す。
#. デザイナーで ui ファイルを保存する。
#. :file:`pyuic5.bat` で ui ファイルから py ファイルを生成すると、ファイルの下の
   方に :code:`import qmytextbrowser` という行が入っているハズ。

#. :file:`qmytextbrowser.py` ファイルを作成し、自分でクラスを実装すればよい。

   .. code:: python3

      from PyQt5 import QtWidgets

      class QMyTextBrowser(QtWidgets.QTextBrowser):
          ...

.. include:: /_include/python-refs-core.txt
.. _PyQt: http://www.riverbankcomputing.co.uk/software/pyqt/intro
.. _`PyQt Download`: http://www.riverbankcomputing.co.uk/software/pyqt/download/
.. _`Qt Documentation`: http://doc.qt.io/qt-5/reference-overview.html
.. _`The PyQt Tutorial`: http://zetcode.com/gui/pyqt5/
