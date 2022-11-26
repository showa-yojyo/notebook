======================================================================
Pylint 利用ノート
======================================================================

本稿では Pylint_ の利用について記す。

Pylint は Python で書かれたコードを解析して、構文エラーの有無、コーディング規約
違反（特に PEP8_ に対する）の有無、設計のまずそうなところを発見するためのコマン
ドラインツールである。

同種のパッケージは他にも有名なものがあるが、Pylint は出力のうるささに定評がある
ようなので、当サイトはこれを採用している。

.. contents:: ノート目次

.. note::

   * OS

     * Windows 7 Home Premium x64 SP1
     * Windows 10 Home x64

   * 本稿において、利用した各パッケージのバージョンは次のとおり。

     * Python_: 3.4.1, 3.5.0, 3.5.2
     * Pylint_: 1.3.1, 1.4.4, 1.5.4

関連リンク
======================================================================

Pylint_
  公式サイト。インストール方法から基本的な利用方法、応用等が文書化されている。

インストール
======================================================================

:ref:`python-pkg-proc` を参照してインストールする。

フォルダー :file:`$PYTHONDIR/Scripts` に、ファイル名が ``pylint`` で拡張子が異な
るものが 3 つあるのが確認できる。内容は次のようなものだ：

* :file:`pylint`: Python スクリプト。単に ``pylint.run_pylint()`` を実行するだ
  け。
* :file:`pylint.bat`: Windows のバッチスクリプト。
  Python に上記スクリプトをコマンドライン引数として渡して実行するだけ。
* :file:`pylint.exe`: Windows の実行ファイル。

私は Python を利用する際には原則的に Cygwin のコマンドライン (Bash) から呼び出す
ことにしている。環境変数 ``$PATH`` には既に :file:`$PYTHONDIR/Scripts` を含ませ
てあるゆえ、私が Pylint をコマンドラインから呼び出すときの記法は次のようになる。

.. code:: console

   bash$ pylint.bat args
   # or
   bash$ pylint.exe args

:file:`.pylintrc` を作成する
----------------------------------------------------------------------

Pylint の設定ファイルについて記す。デフォルトでは Pylint はファイル
:file:`$HOME/.pylintrc` の内容を設定として取り扱う（実際は他にも候補がある）。
このファイルが存在しない場合、Pylint は出力の最初に警告

  ``No config file found, using default configuration.``

を発する。設定ファイルの有無は Pylint の機能に支障はないが、この警告文が毎度目に
つくと煩わしいので、まずはダミーの設定ファイルを作成しておく。

.. code:: console

   bash$ pylint --generate-rcfile > ~/.pylintrc

次にこの設定ファイルのスケルトンに対して構文チェックをしておこう。単に
:command:`pylint --version` をすることで、:file:`.pylintrc` のチェックをさせるこ
とにもなる。

.. code:: console

   bash$ pylint --version
   Warning: option ignore-iface-methods is obsolete and it is slated for removal in Pylint 1.6.
   Warning: option zope is obsolete and it is slated for removal in Pylint 1.6.
   pylint-script.py 1.5.4,
   astroid 1.4.4
   Python 3.5.2 |Continuum Analytics, Inc.| (default, Jul  5 2016, 11:41:13) [MSC v.1900 64 bit (AMD64)]

上記のような Warning が出力されていれば、:file:`.pylintrc` をエディターで開い
て、対応する項目を削除しておくとよい。

Pylint の設定ファイルはプロジェクトごとにコーディングルールに沿って微調整したも
のを用意するのが普通だろう。自動テストの一環としてコード解析を行う工程が想像でき
る。しかし、本稿は私個人の用途を想定しているので、その点については深入りしない。
深入りしないが、Pylint が設定ファイルを指定する機能があることは承知している。

実践例
======================================================================

ここでは私が実際に行っている Pylint の利用例を示していく。とは言え、利用目的が冒
頭で述べたように単純であるがゆえに、利用例の幅はかなり狭い。

よく使うコマンドラインパターン
----------------------------------------------------------------------

私が実際の作業で使う Pylint のコマンドラインを紹介する。サンプルでは Python の
コードファイル名をすべて :file:`mymodule.py` として記すが、モジュールでなくスク
リプトでも同じである。

スクリプト単体の構文チェック
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pylint はオプションなしで実行すると、どんなに品の良いコードを与えたとしても、た
いへんな量のテキストを出力することで知られている。特に出力後半の統計部分が個人的
には用がないので常に ``-rn``, (or ``--reports=n``) を指示する習慣を身につけた。
興味があるのは、コードのどの行がどのような「まずさ」を有するかということだけなの
だ。

.. code:: console

   # Suppress statistics, i.e. display only
   # R: refactor, C: convention, W: warning, and E: error.
   bash$ pylint -rn mymodule.py

   # Display only errors (E).
   bash$ pylint -E mymodule.py

Pylint の出力はコード解析結果と統計結果のふたつの部分からなる。前述のとおり後者
はカットする。解析結果は与えたモジュール名に対して、問題のタイプ、行番号、メッ
セージのリストという構成だ。一回見ればだいたい理解できるはずなので、ここに出力例
を掲載することは差し控える。

パッケージ単位での構文チェック
----------------------------------------------------------------------

コマンドラインでの呼び出し方法に変わりはない。モジュールを示すファイル名の代わり
にパッケージ名を与えればよい。公式ドキュメントによると、開発版の（＝確かめたい）
パッケージと、環境変数 ``$PYTHONPATH`` にあるそれとを Pylint に混同させないよう
に注意する必要があるそうだ。

.. code:: console

   # Specify the package name.
   bash$ pylint -rn mypackage

Python コード修正
----------------------------------------------------------------------

Pylint のコード解析結果（私は RCWE リストと呼んでいる）にらめっこしながら、対応
しよう。修正のやり方には二通りあり、ひとつは忠告に従って素直にコードを修正するこ
とで、もう一つのやり方は、Pylint に勘弁してもらうというものだ。ここではこれらを
順に説明していく。

地道にコードのほうを修正する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

例えば :samp:`C:155, 0: Line too long (81/80) (line-too-long)` というコード解析
結果が出たとしよう。このときコードを修正するのであれば、テキストエディターで対象
のモジュールファイルを開いて、

#. 155 行目にジャンプする。
#. 適宜テキストを編集し、行の長さを 81 文字から 80 字以下に切り詰める。
   おそらく、行の途中で（Python の構文として違法にならぬように）改行することにな
   る。

という手順を踏むのがひとつの解法だ。テキスト編集で解決できるならば、それが単純で
よさそうだ。

Pylint を黙らせる
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pylint の忠告に従いたいが、難しい場合もある。あるいは、Pylint が勘違いして不当な
エラーを報告する場合もある。このような場合は、対応するコードの近所に「抑止命令」
コメントを追加することでしのぐ。

例を説明する。次のような E が出てしまった：

  :samp:`E:242,34: Class 'AbstractMapper' has no '__subclasses__' member (no-member)`

状況はこうだ。私は自作のモジュールで ``AbstractMapper`` という抽象クラスを定義し
た。冒頭だけ引用すると次のような構成になっている。``ABCMeta`` 等については
Python のマニュアルを参照して欲しいが、こうすることで私のクラスには
``__subclasses__`` というメンバーが確かに存在する。

.. code:: python3

   from abc import ABCMeta
   from abc import abstractmethod

   class AbstractMapper(metaclass=ABCMeta):
       """The abstract class that represents the SNES ROM layout."""
       ...

しかたがないので、このクラスの宣言の直前に次のコメントを追加しておく。

.. code:: python3

   # pylint: disable=no-member
   class AbstractMapper(metaclass=ABCMeta):
       ...

こうすることで、次からの Pylint のメッセージは次のように変わり、やや安心できる。

  :samp:`I: 242, 0: Locally disabling no-member (E1101) (locally-disabled)`

なお、出力抑止をしたいエラー項目はエラー名だけでなく、エラー番号でも指定できる。
カンマ区切りで複数のエラー項目を指示することもできるし、抑止コメントを抑止する項
目数だけ書いてもよい。

.. include:: /_include/python-refs-core.txt
.. _Pylint: http://www.pylint.org/
