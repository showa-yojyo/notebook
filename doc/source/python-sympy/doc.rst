======================================================================
ドキュメントをビルドする
======================================================================

せっかく SymPy_ のソースコードを入手したのだから、ドキュメントを自分の環境で生成
してみよう。本稿は SymPy の利用ノートというよりは、軽い気分転換のための作業記録
のようなものだ。

.. contents:: ノート目次

ビルド手順
======================================================================

SymPy のドキュメントは Sphinx_ を用いて生成する。いつもブラウザーで見ているファ
イル群を生成する手順はこのようなものだろう：

.. code:: console

   bash$ make -C ~/devel/sympy/doc html

前準備
======================================================================

私の場合は一発でビルドが通らず、少々の Cygwin パッケージの導入とSymPy 専用
Sphinx 拡張モジュールコードの編集を必要とした。本節ではこれらの作業について記
す。

画像生成のための Cygwin パッケージ導入
----------------------------------------------------------------------

:file:`Makefile` を読むとわかるように、仮にコンソールから :command:`make html`
と入力すると、Sphinx の既定の処理群を行う前に :command:`make logo` 相当の処理が
入る。そこでは Python スクリプト :file:`generate_logos.py` を起動して、次のタイ
プの画像ファイルを生成する：

* :file:`*.png`
* :file:`*.svg`
* :file:`*.ico`

スクリプトの冒頭にコメントされているように、次のパッケージが必要だ：

* rsvg-convert (:program:`rsvg-convert`)
* imagemagick (:program:`convert`)

私は Cygwin で Sphinx のビルド処理をするので、これらを含むパッケージをインストー
ラー (:file:`setup-x86_64.exe`) でダウンロードかつインストールした。ImageMagick
くらい昔インストールしただろうと思っていたが、古い PC の話だったようだ。

Cygwin のインストーラーでパッケージ構成を更新したら、これらの各ユーティリティー
のパスを確認して、問題がないようにしておく。

.. code:: console

   bash$ which rsvg-convert
   /bin/rsvg-convert
   bash$ which convert
   /bin/convert

特に :file:`convert` は Windows のシステムフォルダーに同名の実行ファイルがあるの
で、環境変数 ``PATH`` の設定によってはそちらを優先して参照してしまう。こうなって
しまうと :file:`generate_logos.py` は異常終了する。こういう事態を上手に避けるこ
と。

コンソールから :command:`make logo` して、無事に ``Logo generated.`` のメッセー
ジが画面に出力されればここまでは成功だ。

.. todo::

   :file:`src/logo/sympy.svg` から各種画像ファイルを生成する具体的な方法に興味が
   わいたので、:file:`generate_logos.py` の行う処理を正確に把握しておく。いつか
   何かに応用できる気がする。特に SVG ファイルからコマンドラインでアイコンファイ
   ルが生成できるのならば、これはたいへん便利だ。

Sphinx 拡張モジュールの修正
----------------------------------------------------------------------

.. note::

   この修正作業は現在不要と思われる。

ロゴファイル群の生成が成功しても、ドキュメント本体のファイル生成で失敗した。

.. code:: console

   bash$ make html
   ...略...
   Logo generated.
   mkdir -p src/.static
   mkdir -p _build/html
   mkdir -p _build/doctrees
   mkdir -p src/modules
   PYTHONPATH=..:D:/home/yojyo/devel/pylib sphinx-build -b html -d _build/doctrees  src _build/html
   Running Sphinx v1.3.1

   Exception occurred:
     File "D:\Python34\lib\site-packages\sphinx\application.py", line 429, in setup_extension
       mod = __import__(extension, None, None, ['setup'])
     File "ext\numpydoc.py", line 41
       title_re = re.compile(ur'^\s*[#*=]{4,}\n[a-z0-9 -]+\n[#*=]{4,}\s*',
                                                                        ^
   SyntaxError: invalid syntax
   The full traceback has been saved in D:\cygwin64\tmp\sphinx-err-9tvw236x.log, if you want to report the issue to the developers.
   Please also report this if it was a user error, so that a better error message can be provided next time.
   A bug report can be filed in the tracker at <https://github.com/sphinx-doc/sphinx/issues>. Thanks!
   Makefile:50: ターゲット 'html' のレシピで失敗しました
   make: *** [html] エラー 1

これは Sphinx の不具合ではない。単に拡張モジュールの構文が古いことから起こるエ
ラーのようなので、私の Python 環境に適合するようにコードをアップグレードする必要
がある。ここは :program:`2to3.py` の出番だ。レポジトリーがあるので、遠慮なく
``-nw`` オプションで元ファイルを上書きしてしまう。なんならローカルで適宜 branch
を作成してここでの修正を commit するのもありだ。

.. code:: console

   bash$ cp D:/Python34/Tools/Scripts/2to3.py ext
   bash$ pushd ext
   bash$ ./2to3.py -nw *.py
   ...
   bash$ popd

私の場合は以上の修正作業のみで :command:`make html` が通った。

ビルド完了
======================================================================

ビルド :command:`make html` の結果、次のようになる。

* ディレクトリー :file:`doc/_build/html` に SymPy の HTML ドキュメントが生成され
  ている。インターネットに接続しなくてもいつものドキュメントが読めるようになっ
  た。

  * ただし数式表示は外部サイトの JavaScript ファイルを参照しているようなので、こ
    こは御免。
  * 画面左柱からのキーワード検索も可能。
  * :guilabel:`Run code block in SymPy Live` の実行も可能。

* ディレクトリー :file:`doc/_build/logo` に SymPy のロゴマーク画像ファイルが多数
  生成されている。これらの画像ファイル、特に SVG ファイルの構成を研究することが
  できるようになった。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
