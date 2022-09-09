======================================================================
モジュール ``docutils.core``
======================================================================
モジュール ``docutils.core`` は名前に反してむしろエンドユーザー寄りの場所にある。
これまで見てきた低階層のクラス群を統べるクラス ``Publisher`` と、
それを用いてドキュメントを生成する関数群が定義されている。

.. contents:: ノート目次

クラス ``Publisher``
======================================================================
クラス ``Publisher`` は今まで見てきた入出力、読み込み、構文解析、変換、書き出し等の
処理を一箇所に閉じ込めて、クライアントとの窓口にして機能するように設計されている。
クライアントというのは、後述する関数 ``publish_xxxx`` 系がまさに相当する。

.. figure:: /_images/docutils-publisher-od.png
   :align: center
   :alt: (component diagram)
   :scale: 100%

メンバー
----------------------------------------------------------------------
主要なメンバーデータを調べてみよう。

メソッド
----------------------------------------------------------------------
エラー処理や単純なアクセッサーは省いて、主要なメソッドを調べてみよう。
呼びだされそうな順序で挙げていく。

``__init__(self, ...)``
  ``Publisher`` オブジェクトを生成する。

  * 指定した引数がそのままメンバーデータにセットされる。

  * ``reader``, ``parser``, ``writer`` はそれぞれ文字列であってはならない。
    変数名が示すようなクラスのオブジェクトである必要がある。

  * ``settings`` は後で述べるメソッドでも指定する機会がある。
    生成時は無指定で構わないだろう。

``set_components(self, reader_name, parser_name, writer_name)``
  ``Component`` 系のメンバーデータを文字列によってセットする。

  * ``self.reader``, ``self.parser``, ``self.writer`` が確実にセットされて、
    Reader と Writer のオブジェクト間の関連付けも担保される。
    下記ページも参照。

    * :doc:`./readers`
    * :doc:`./parsers`
    * :doc:`./writers`

``process_programmatic_settings(self, settings_spec, ...)``
  これはよくわからない。

  * ``self.settings`` が設定済みの場合は特に機能しない。
  * これは ``traceback`` というオプションを ON になるため（だけ）の機能か。
    メインの処理でエラー発生時にデバッグダンプが出るようになる？

``get_settings(self, usage=None, ...)``
  ``OptionParser`` オブジェクトを生成したあと、
  そのメソッド ``get_default_values`` を呼び出した戻り値を
  ``self.settings`` にセットする。

  * 名前は get だが内容は set を兼ねているので注意。

``setup_option_parser(self, usage=None, ...)``
  ``OptionParser`` オブジェクトを生成して返すメソッド。

  * クラス ``OptionParser`` については :doc:`./frontend` 参照。

  * 引数の指定状況によっては ``SettingsSpec`` オブジェクトを自力で生成する。
    抽象クラスかと思っていたが、オブジェクトとして用いる場合があるとは。

  * このメソッドの事前条件の一つに ``Component`` 系のメンバーデータがセットアップ済みであるというものがある。
    ``OptionParser`` のコンストラクターがそれらを要求する。

  * このメソッドは ``get_settings`` と ``process_command_line`` から呼び出される。

``publish(self, argv=None, ...)``
  このメソッドが「実行」役を果たす。
  文書生成のパイプライン、次に示すステージからなる一連の手続きそのものの実装となる。

  #. コマンドライン解析 ``self.process_command_line``
  #. 入出力設定 ``self.set_io``
  #. 読み込み処理 ``self.reader.read``
  #. 構文木の変換 ``self.apply_transforms``
  #. 書き出し処理 ``self.writer.write``

  .. mermaid:: ./docutils-publisher-sd.mmd
     :align: center
     :alt: (component diagram)

``process_command_line(self, argv=None, ...)``
  コマンドライン引数を解析して、メンバーデータ ``self.settings`` をセットする。

  * 引数 ``argv`` が ``None`` のとき、
    実際のコマンドライン引数を自動的に解析対象として適用する。

  * 引数 ``argv`` 以外のものはすべて次に説明するメソッドに渡される。

``set_io(self, source_path=None, destination_path=None)``
  メソッド ``set_source`` と ``set_destination`` を同時に呼び出す。
  後述のメモを参照。

  * それぞれの型は ``docutils.io.Input`` と ``docutils.io.Output`` の何らかのサブクラスだ。
    :doc:`./io` 参照。

``set_source(self, source=None, source_path=None)``
  メンバーデータ ``self.source`` を生成する。

  * 代入とは異なる。
    クラス ``self.source_class`` のコンストラクターを適用する。
    このメソッドの引数はそのままこのコンストラクターに渡される。

``set_destination(self, destination=None, destination_path=None)``
  メンバーデータ ``self.destination`` を生成する。

  * 代入とは異なる。
    クラス ``self.destination_class`` のコンストラクターを適用する。
    このメソッドの引数はそのままこのコンストラクターに渡される。

  * 後半の例外処理のコードに違和感がある。
    どうも try 節と except 節の内容が同一に見える。

``apply_transforms(self)``
  ``self.document.transformer`` のメソッドを連発するメソッド。

  * 変換オブジェクトは ``Publisher`` の ``TransformSpec`` 系メンバーデータすべてから得る。
  * ``Transformer`` については :doc:`./transforms` 参照。

関数
======================================================================
ここまで書いてきて何だが、実のところユーザーはクラス ``Publisher`` を直接用いる必要はない。
代わりに関数 ``publish_xxxx`` 系を呼ぶことで、原稿から各種文書ファイルを生成できる。

以下、各関数の仕様を述べる。
ユーザーは用途に合ったものを一つ選んで単に呼び出すとよい。

``publish_cmdline``
  コマンドラインを読んで、文書オブジェクトを出力する。

``publish_file``
  入出力ファイルを指定して、文書オブジェクトを出力する。
  処理を ``publish_programmatically`` に委譲する。

  * その際、引数 ``source_class`` と ``destination_class`` を
    ``docutils.io.FileInput`` および ``docutils.io.FileOutput`` にそれぞれ固定する。

``publish_string``
  入力を reStructuredText 書式の文字列として、文書オブジェクトを出力する。

  * 実際は関数 ``publish_programmatically`` が働く。
    その際、引数 ``source_class`` と ``destination_class`` を
    ``docutils.io.StringInput`` および ``docutils.io.StringOutput`` にそれぞれ固定する。

  * さらに引数 ``destination`` は指定なし、すなわち標準出力となる。

``publish_parts``
  文書情報を辞書オブジェクトの形で返す。

  * 実際は関数 ``publish_programmatically`` が働く。
    引数 ``destination_class`` を ``docutils.io.StringOutput`` に固定する。

``publish_doctree``
  文書情報をいつもの構文木オブジェクトの形で返す。

``publish_from_doctree``
  既存の構文木オブジェクトから文字列を出力する。

  * 読み取りオブジェクトが空構文解析オブジェクトを利用する。
  * ``Publisher`` オブジェクトの ``source`` が ``docutils.io.DocTreeInput`` 型を固定。

``publish_cmdline_to_binary``
  ほとんど ``publish_cmdline`` と同じだが、
  出力クラスが ``docutils.io.BinaryFileOutput`` に固定となる。

``publish_programmatically``
  すべての ``publish_xxxx`` 系の基本形の関数。

  * デフォルト引数は一つもない。全て呼び出し元が明示的に値を渡す必要がある。
    ただし ``None`` を渡すことで、デフォルト値を内部的に決めさせることはある。

  * エンドユーザーはこの関数を直接呼び出すべきではないと但し書きが付いている。

  * この関数の docstring がたいへん丁寧なので、必要な仕様情報はここから得たい。

各関数に共通するデフォルト値をまとめておく。

* 引数 ``argv`` に指定がない場合は実際のコマンドライン引数 ``sys.argv[1:]`` が適用される。
* 引数 ``source`` に指定がない場合は標準入力 ``sys.stdin`` が適用される。
* 引数 ``destination`` に指定がない場合は標準出力 ``sys.stdout`` が適用される。
* 読み取りクラスのデフォルトは ``docutils.readers.standalone.Reader`` になる。
* 構文解析クラスのデフォルトは ``docutils.parsers.rst.Parser`` になる。
* 書き出しクラスのデフォルトは ``docutils.writers.pseudoxml.Writer`` になる。

感想
======================================================================
Docutils の構成要素を一箇所で捌き切っている感じ。

.. include:: /_include/python-refs-core.txt
