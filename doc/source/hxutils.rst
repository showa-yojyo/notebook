======================================================================
HTML-XML-utils 利用ノート
======================================================================

ウェブスクレイピングでは HTML ファイルから特定の条件を満たす要素を抽出することが重要だ。
とくに CSS セレクターで指定することが私は多い。
その目的にかなう標準的ツールであろう `HTML-XML-utils`_ パッケージを導入して利用したい。

.. contents:: ノート目次

インストール
======================================================================

私の環境は Cygwin だ。ソースからビルドしてインストールする必要がある。
記憶によると次のような手順で `HTML-XML-utils`_ をインストールすることができた：

.. code:: shell

   bash$ cd /tmp
   bash$ wget https://www.w3.org/Tools/HTML-XML-utils/html-xml-utils-7.8.tar.gz
   bash$ mv html-xml-utils-7.8.tar.gz html-xml-utils-7.8.tar
   bash$ tar xvf html-xml-utils-7.8.tar.gz
   bash$ cd html-xml-utils-7.8
   bash$ ./configure
   bash$ make
   bash$ make install

Makefile からビルドをするために ``make`` や ``gcc`` が使える状態でなければならない。
これらは Cygwin のパッケージマネージャー setup-x86_64.exe からインストール可能だ。

ツール各種が ``/usr/local/bin`` にインストールされれば成功とみなす。

.. code:: shell

   bash$ which hxselect
   /usr/local/bin/hxselect

インストールのときに注意する点が少しはある：

* ``.tar.gz`` といいつつ中身は ``.tar`` だった。これは ``file`` コマンドで確認できる。
* ``configure`` の出力をよく観察して、足りないパッケージを把握する必要がある。
  欠けているもののパッケージ名を調べて Cygwin のマネジャーでインストールする必要がある。

利用価値の高いツール
======================================================================

スクレイピング用途ならばまずは次の 4 つだけ使いこなせれば十分だと思われる。
どのツールも XML 形式にも対応しているが、私は HTML しか扱わないので以下 HTML
しか取り上げない。

* ``hxextract``
* ``hxclean``
* ``hxnormalize``
* ``hxremove``
* ``hxselect``
* ``hxwls``

コマンド共通メモ
----------------------------------------------------------------------

どのコマンドも最後の引数与えられていれば URL またはローカルファイルパスとして処理する。
それが存在しない場合は標準入力を処理する。

エラー表示が邪魔なのでコマンドラインに ``2>/dev/null`` を追加しておく。

``hxextract``: 指定要素抽出
----------------------------------------------------------------------

``hxextract`` は文法通り書かれた HTML テキストから指定要素（タグ）を抽出するコマンドだ。
実際には指定していない要素を取り除いた残りの HTML を出力するような振る舞いをするようだ。

使い方は欲しい要素のタグ名またはクラス名を指定する。

.. code:: shell

   bash$ hxextract img $URL_OR_FILE
   bash$ hxextract img.thumbnail $URL_OR_FILE

ただし出力がテキスト処理向けでないので、使い勝手は悪い。
代わりにいきなり ``hxselect`` を使ってしまっていいと思われる。

``hxclean``: 修正
----------------------------------------------------------------------

このツールは文法が汚い HTML テキストを修正するのに利用するコマンドだ。
コマンドラインオプションが何もないので、使い方に迷うことはない。

処理対象の HTML ファイルを ``hxclean`` してパイプに流すのが典型的な用途と思われる。

.. code:: shell

   bash$ wget --output-file - $URL | hxclean | some-command ...
   bash$ # or
   bash$ hxclean $URL_OR_FILE | some-command ...

品質の保証がない HTML ファイルを扱うときにはこのコマンドからパイプラインを組むのが良いだろう。

``hxnormalize``: pretty-print
----------------------------------------------------------------------

``hxnormalize`` は HTML テキストの内容であるテキストを整形して出力するツールだ。
一行あたりの文字数を制限したり、インデントの桁数を指定したりする。

整形の過程で小さな文法上のエラーを修正する性質があるようで、むしろこちらのほうが利用価値が高い。
場合によっては ``hxclean`` をせずに済む。

どちらの機能もパイプによるテキスト処理の前工程になじむ。

.. code:: shell

   bash$ wget -O $FILE $URL
   bash$ hxnormalize $FILE -l 80 | some-command ...

``hxremove``: 指定要素削除
----------------------------------------------------------------------

``hxremove`` は CSS セレクター形式の文字列を指定すると、それらにマッチする要素を HTML
から取り去ったものを出力するコマンドだ。処理ファイルを単純化するのに利用できる。

.. code:: shell

   bash$ hxremove script < $FILE

``hxselect``: 指定要素抽出
----------------------------------------------------------------------

``hxselect`` は CSS セレクター形式の文字列を指定すると HTML テキストの要素を抽出するコマンドだ。
これを使いたかった。

.. code:: shell

   bash$ hxselect -s '\n' 'h2>a' $FILE_OR_URL | grep -oP "(?<=href=\").+html(?=\")"
   bash$ hxselect -s '\n' 'img[class="thumbnail_image]' $FILE_OR_URL | grep -oP "(?<=src=\").+jpg(?=\")"

オプション ``-c`` を指定すると ``hxselect`` は要素の中身しか出力しないようになる。
例えば ``<A>`` タグに対してはふつうはリンクテキストしか出力しなくなる。

ここでだいじなのは、セレクターとして属性を抽出するように指定すると、属性値のみを出力するになる。
``grep -oP`` にパイプする手間が省ける可能性が高い。上の例は次のようにも書ける：

.. code:: shell

   bash$ hxselect -c -s '\n' 'h2>a::attr(href)' $FILE_OR_URL
   bash$ hxselect -c -s '\n' 'img[class="thumbnail_image"]::attr(src)' $FILE_OR_URL

オプション ``-s`` を指定すると抽出する要素同士を Python でいうところの
``str.join()`` する。
テキストエディターで出力をチェックしたいときに有用だ。

``hxwls``: リンク抽出
----------------------------------------------------------------------

``hxwls`` は HTML テキスト中の各種リンクのリンク先（つまり ``href`` や
``src`` の値）のみを一覧するコマンドだ。場合によってはこれで事足りるだろう。

.. code:: shell

   bash$ hxwls $URL_OR_FILE | awk '/archives/ && /jpg/'

関連ノート
======================================================================

この他のスクレイピングの技法をまとめたノートの一覧。

* :doc:`/css-selector`
* :doc:`/python-bs4`
* :doc:`/python-selenium`

.. _`HTML-XML-utils`: https://www.w3.org/Tools/HTML-XML-utils/
