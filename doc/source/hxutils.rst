======================================================================
HTML-XML-utils 利用ノート
======================================================================

ウェブスクレイピングでは HTML ファイルから特定の条件を満たす要素を抽出することが
重要だ。とくに CSS セレクターで指定することが私は多い。その目的にかなう標準的
ツールであろう `HTML-XML-utils`_ パッケージを導入して利用したい。

.. contents:: ノート目次

インストール
======================================================================

私の環境は Cygwin だ。ソースからビルドしてインストールする必要がある。
記憶によると次のような手順で `HTML-XML-utils`_ をインストールすることができた：

.. code:: console

   bash$ cd /tmp
   bash$ wget https://www.w3.org/Tools/HTML-XML-utils/html-xml-utils-7.8.tar.gz
   bash$ mv html-xml-utils-7.8.tar.gz html-xml-utils-7.8.tar
   bash$ tar xvf html-xml-utils-7.8.tar.gz
   bash$ cd html-xml-utils-7.8
   bash$ ./configure
   bash$ make
   bash$ make install

:file:`Makefile` からビルドをするために :program:`make` や :program:`gcc` が使え
る状態でなければならない。これらは Cygwin のパッケージマネージャー
:file:`setup-x86_64.exe` からインストール可能だ。

ツール各種が :file:`/usr/local/bin` にインストールされれば成功とみなす。

.. code:: console

   bash$ which hxselect
   /usr/local/bin/hxselect

インストールのときに注意する点が少しはある：

* ``.tar.gz`` といいつつ中身は ``.tar`` だった。これは :program:`file` で確認で
  きる。
* :command:`configure` の出力をよく観察して、足りないパッケージを把握する必要が
  ある。欠けているもののパッケージ名を調べて Cygwin のマネジャーでインストールす
  る必要がある。

利用価値の高いツール
======================================================================

スクレイピング用途ならばまずは次の 4 つだけ使いこなせれば十分だと思われる。どの
ツールも XML 形式にも対応しているが、私は HTML しか扱わないので以下 HTMLしか取り
上げない。

* :program:`hxextract`
* :program:`hxclean`
* :program:`hxnormalize`
* :program:`hxremove`
* :program:`hxselect`
* :program:`hxwls`

コマンド共通メモ
----------------------------------------------------------------------

どのコマンドも最後の引数与えられていれば URL またはローカルファイルパスとして処
理する。それが存在しない場合は標準入力を処理する。

エラー表示が邪魔なのでコマンドラインに ``2>/dev/null`` を追加しておく。

:program:`hxextract`: 指定要素抽出
----------------------------------------------------------------------

:program:`hxextract` は文法通り書かれた HTML テキストから指定要素（タグ）を抽出
するコマンドだ。実際には指定していない要素を取り除いた残りの HTML を出力するよう
な振る舞いをするようだ。

使い方は欲しい要素のタグ名またはクラス名を指定する。

.. code:: console

   bash$ hxextract img $URL_OR_FILE
   bash$ hxextract img.thumbnail $URL_OR_FILE

ただし出力がテキスト処理向けでないので、使い勝手は悪い。代わりにいきなり
:program:`hxselect` を使ってしまっていいと思われる。

:program:`hxclean`: 修正
----------------------------------------------------------------------

このツールは文法が汚い HTML テキストを修正するのに利用するコマンドだ。コマンドラ
インオプションが何もないので、使い方に迷うことはない。

処理対象の HTML ファイルを :program:`hxclean` してパイプに流すのが典型的な用途と
思われる。

.. code:: console

   bash$ wget --output-file - $URL | hxclean | some-command ...
   bash$ # or
   bash$ hxclean $URL_OR_FILE | some-command ...

品質の保証がない HTML ファイルを扱うときにはこのコマンドからパイプラインを組むの
が良いだろう。

:program:`hxnormalize`: pretty-print
----------------------------------------------------------------------

:program:`hxnormalize` は HTML テキストの内容であるテキストを整形して出力する
ツールだ。一行あたりの文字数を制限したり、インデントの桁数を指定したりする。

整形の過程で小さな文法上のエラーを修正する性質があるようで、むしろこちらのほうが
利用価値が高い。場合によっては :program:`hxclean` をせずに済む。

どちらの機能もパイプによるテキスト処理の前工程になじむ。

.. code:: console

   bash$ wget -O $FILE $URL
   bash$ hxnormalize $FILE -l 80 | some-command ...

:program:`hxremove`: 指定要素削除
----------------------------------------------------------------------

:program:`hxremove` は CSS セレクター形式の文字列を指定すると、それらにマッチす
る要素を HTMLから取り去ったものを出力するコマンドだ。処理ファイルを単純化するの
に利用できる。

.. code:: console

   bash$ hxremove script < $FILE

:program:`hxselect`: 指定要素抽出
----------------------------------------------------------------------

:program:`hxselect` は CSS セレクター形式の文字列を指定すると HTML テキストの要
素を抽出するコマンドだ。これを使いたかった。

.. code:: console

   bash$ hxselect -s '\n' 'h2>a' $FILE_OR_URL | grep -oP "(?<=href=\").+html(?=\")"
   bash$ hxselect -s '\n' 'img[class="thumbnail_image]' $FILE_OR_URL | grep -oP "(?<=src=\").+jpg(?=\")"

オプション ``-c`` を指定すると :command:`hxselect` は要素の中身しか出力しないよ
うになる。例えば ``<A>`` タグに対してはふつうはリンクテキストしか出力しなくな
る。

ここでだいじなのは、セレクターとして属性を抽出するように指定すると、属性値のみを
出力するになる。:command:`grep -oP` にパイプする手間が省ける可能性が高い。上の例
は次のようにも書ける：

.. code:: console

   bash$ hxselect -c -s '\n' 'h2>a::attr(href)' $FILE_OR_URL
   bash$ hxselect -c -s '\n' 'img[class="thumbnail_image"]::attr(src)' $FILE_OR_URL

オプション ``-s`` を指定すると抽出する要素同士を Python でいうところの
``str.join()`` する。テキストエディターで出力をチェックしたいときに有用だ。

:program:`hxwls`: リンク抽出
----------------------------------------------------------------------

:program:`hxwls` は HTML テキスト中の各種リンクのリンク先（つまり ``href`` や
``src`` の値）のみを一覧するコマンドだ。場合によってはこれで事足りるだろう。

.. code:: console

   bash$ hxwls $URL_OR_FILE | awk '/archives/ && /jpg/'

関連ノート
======================================================================

この他のスクレイピングの技法をまとめたノートの一覧。

* :doc:`/css-selector`
* :doc:`/python-bs4`
* :doc:`/python-selenium`

セレクターを試すのならブラウザーの開発者ツールで事足りるかもしれない。

* :doc:`/chrome`

.. _`HTML-XML-utils`: https://www.w3.org/Tools/HTML-XML-utils/
