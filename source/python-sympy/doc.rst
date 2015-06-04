======================================================================
ドキュメントをビルドする
======================================================================
せっかく SymPy_ のソースコードを入手したのだから、ドキュメントを自分の環境で生成してみよう。
本稿は SymPy の利用ノートというよりは、軽い気分転換のための作業記録のようなものだ。

.. contents:: ノート目次

ビルド手順
======================================================================
SymPy のドキュメントは Sphinx_ を用いて生成する。
いつもブラウザーで見ているファイル群を生成する手順はこのようなものだろう。

.. code-block:: console

   $ cd ~/devel/sympy
   $ cd doc
   $ make html

前準備
======================================================================
私の場合は一発でビルドが通らず、少々の Cygwin パッケージの導入と
SymPy 専用 Sphinx 拡張モジュールコードの編集を必要とした。
本節ではこれらの作業について記す。

画像生成のための Cygwin パッケージ導入
----------------------------------------------------------------------
:file:`Makefile` を読むとわかるように、仮にコンソールから ``make html`` と入力すると、
Sphinx の既定の処理群を行う前に ``make logo`` 相当の処理が入る。
そこでは Python スクリプト :file:`generate_logos.py` を起動して、
次のタイプの画像ファイルを生成する。

* :file:`*.png`
* :file:`*.svg`
* :file:`*.ico`

スクリプトの冒頭にコメントされているように、次のパッケージが必要だ。

* rsvg-convert (:file:`rsvg-convert`)
* imagemagick (:file:`convert`)

私は Cygwin で Sphinx のビルド処理をするので、
これらを含むパッケージをインストーラー (:file:`setup-x86_64.exe`) でダウンロードかつインストールした。
ImageMagick くらい昔インストールしただろうと思っていたが、古い PC の話だったようだ。

Cygwin のインストーラーでパッケージ構成を更新したら、
これらの各ユーティリティーのパスを確認して、問題がないようにしておく。

.. code-block:: console

   $ which rsvg-convert
   /bin/rsvg-convert
   $ which convert
   /bin/convert

特に :file:`convert` は Windows のシステムフォルダーに同名の実行ファイルがあるので、
環境変数 ``PATH`` の設定によってはそちらを優先して参照してしまう。
こうなってしまうと :file:`generate_logos.py` は異常終了する。
こういう事態を上手に避けること。

コンソールから ``make logo`` して、無事に ``Logo generated.`` のメッセージが画面に出力されればここまでは成功だ。

.. todo::

   :file:`src/logo/sympy.svg` から各種画像ファイルを生成する具体的な方法に興味がわいたので、
   :file:`generate_logos.py` の行う処理を正確に把握しておく。
   いつか何かに応用できる気がする。

   特に SVG ファイルからコマンドラインでアイコンファイルが生成できるのならば、
   これはたいへん便利だ。

Sphinx 拡張モジュールの修正
----------------------------------------------------------------------
ロゴファイル群の生成が成功しても、ドキュメント本体のファイル生成で失敗した。

.. code-block:: console

   $ make html
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

これは Sphinx の不具合ではない。
単に拡張モジュールの構文が古いことから起こるエラーのようなので、
私の Python 環境に適合するようにコードをアップグレードする必要がある。
ここは :file:`2to3.py` の出番だ。
レポジトリーがあるので、遠慮なく ``-nw`` オプションで元ファイルを上書きしてしまう。
なんならローカルで適宜 branch を作成してここでの修正を commit するのもありだ。

.. code-block:: console

   $ cp D:/Python34/Tools/Scripts/2to3.py ext
   $ pushd ext
   $ ./2to3.py -nw *.py
   ...
   $ popd

私の場合は以上の修正作業のみで ``make html`` が通った。

ビルド完了
======================================================================
``make html`` の出力の最後の方に何やら警告めいたメッセージが出てくる。
今は気にしないでよさそうだ。

.. code-block:: text

   copying static files... done
   copying extra files... done
   dumping search index in English (code: en) ... done
   dumping object inventory... done
   build succeeded.
   d:\home\yojyo\devel\sympy\sympy\utilities\decorator.py:207: SymPyDeprecationWarning:

   bounded has been deprecated since SymPy 0.7.7. Use finite instead. See
   https://github.com/sympy/sympy/issues/9425 for more info.

     return self.fget.__get__(obj, klass)()
   d:\home\yojyo\devel\sympy\sympy\utilities\decorator.py:207: SymPyDeprecationWarning:

   infinity has been deprecated since SymPy 0.7.7. Use infinite instead.
   See https://github.com/sympy/sympy/issues/9426 for more info.

     return self.fget.__get__(obj, klass)()
   cp -r src/pics _build/html/

   Build finished. The HTML pages are in _build/html.

ビルドの結果、

* ディレクトリー :file:`doc/_build/html` に SymPy の HTML ドキュメントが生成されている。
  インターネットに接続しなくてもいつものドキュメントが読めるようになった。

  * ただし数式表示は外部サイトの JavaScript ファイルを参照しているようなので、ここは御免。
  * 画面左柱からのキーワード検索も可能。
  * <Run code block in SymPy Live> の実行も可能。

* ディレクトリー :file:`doc/_build/logo` に SymPy のロゴマーク画像ファイルが多数生成されている。
  これらの画像ファイル、特に SVG ファイルの構成を研究することができるようになった。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
