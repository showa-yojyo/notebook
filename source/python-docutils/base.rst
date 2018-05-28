======================================================================
基礎クラス群
======================================================================
ここでは Docutils_ の様々なテキスト処理クラス群のスーパークラスとして存在する
``TransformSpec``, ``SettingsSpec``, ``Component`` を見ていく。
以下、この 3 クラスを基礎クラスと呼ぶことにする。
本節の目的は、これらの基礎クラスがどのような機能を Docutils 内の
サブクラスやクライアントに提供しているのかを調査し、
いずれ私が類似のプログラムを書くときに参考にすることだ。

.. contents:: ノート目次

クラス図
======================================================================
本節で登場するクラスを図に示す。

.. figure:: /_images/docutils-base.png
   :align: center
   :alt: (class diagram)
   :scale: 100%

クラス ``docutils.SettingsSpec``
======================================================================
* このクラスは実行時に何かの構成・設定値を指定するための枠組みを決める。
  Docutils のための設定ファイルやコマンドラインオプションから値を受け取り、
  オブジェクトにそれをセットするという、一連のデータの流れを支える。

* ``SettingsSpec`` にはスーパークラスがない。

メンバー
----------------------------------------------------------------------
* メンバーの種類はクラスデータしかない。

``SettingsSpec.settings_spec = ()``
  コマンドラインオプションの定義。
  次に示すような複雑なデータ構造体の ``tuple`` だ。
  ::

      (option-group-title, description, option-tuples)*;
      option-group-title ::= text;
      description ::= text;
      option-tuples ::= (help-text, option-strings, kwargs)*;
      help-text ::= text;
      option-strings ::= e.g. ['-Q', '--quux'];

``SettingsSpec.settings_defaults = None``
  サブクラスメンバーデータ ``self.defaults`` にマージ ``update`` される。

  * 外部からのアクセスを意図していない。

``SettingsSpec.settings_default_overrides = None``
  サブクラスメンバーデータ ``self.defaults`` にマージ ``update`` される。

  * サブクラスが上書きする。

``SettingsSpec.relative_path_settings = ()``
  設定ファイル群の相対パスを文字列の ``tuple`` で持つ。
  これは設定ファイルが複数ファイルに分割されていて、
  それらのファイルシステム上での、ある基点からの相対パスということだろう。

  * サブクラスメンバーデータ ``self.relative_path_settings`` に ``extend`` される。

``SettingsSpec.config_section = None``
  設定ファイルのセクション名そのもの。

  * サブクラスが上書きする。

``SettingsSpec.config_section_dependencies = None``
  上述のデータと同様だが、優先順位がより高い。

  * サブクラスが上書きする。

サブクラス
----------------------------------------------------------------------
* ``SettingsSpec`` の直接サブクラスは 2 つだけある。図に示す。

  .. figure:: /_images/docutils-settings-spec.png
     :align: center
     :alt: (class diagram)
     :scale: 100%

* ``Component`` では何もオーバーライドしないが、
  そこからのサブクラスは ``settings_spec`` と ``config_section`` を
  上書きするだけのことが多い。例::

    config_section = 'general'

クライアント
----------------------------------------------------------------------
主な参照箇所はモジュール ``docutils.core`` と ``docutils.frontend`` に集中している。

* ``Component`` 系と ``OptionParser`` 系を読む。
* ``OptionParser.get_config_file_settings`` を読む。
* ``OptionParser.populate_from_components`` を読む。

クラス ``docutils.TransformSpec``
======================================================================
* ``TransformSpec`` はスーパークラスがない。
* メソッド ``get_transforms`` が一つだけある抽象クラスと大づかみに理解してよい。
  必要に応じてサブクラスがオーバーライドする。
* 他にも細かいクラスデータや格納データの約束事があるが、
  そこまで調査しなくてよいだろう。

メンバー
----------------------------------------------------------------------
``get_transforms(self)``
  クラス ``Transform`` のサブクラスを含む ``list`` を返すようにサブクラスがオーバーライドする。
  注意。サブクラスのオブジェクトではなく、あくまでもサブクラスを型として取り扱う。

サブクラス
----------------------------------------------------------------------
``TransformSpec`` をスーパークラスとしたクラス図を示す。

  .. figure:: /_images/docutils-transform-spec.png
     :align: center
     :alt: (class diagram)
     :scale: 100%

* ``Input`` および ``Output`` は何もオーバーライドしていないことに注意。
  設計ミスか？

* メソッド ``get_transforms`` は ``Component`` のさらなるサブクラスがオーバーライドする傾向がある。

クライアント
----------------------------------------------------------------------
メソッド ``get_transforms`` を呼び出すのは何かということになる。

* サブクラス ``Transformer`` が自身のメンバーデータを
  組み立てるときのパラメーターとして参照する。

これぐらいしかないだろう。

クラス ``docutils.Component``
======================================================================
* ``Component`` は Docutils のテキスト処理系クラスのためのスーパークラス。
  言い換えると ``Reader``, ``Parser``, ``Writer`` がサブクラスとなる。

* ``Component`` のスーパークラスは前述の ``SettingsSpec``, ``TransformSpec`` だ。
  なお、この段階ではいずれのスーパークラスのどのメンバーもオーバーライドしないままだ。

メンバー
----------------------------------------------------------------------
クラスデータが 2 個とメソッドが 1 個ある。重要なものだけ記す。

``Component.component_type``
  コンポーネントの種別を示す文字列とする。
  各サブクラスで上書きする。つまりこのようなものだ。

  .. csv-table::
     :delim: :
     :header: サブクラス, ``component_type`` の値
     :widths: 8, 22

     ``Reader``:``'reader'``
     ``Parser``:``'parser'``
     ``Writer``:``'writer'``

  * 実は ``Component`` のサブクラスではないクラスである
    ``Input`` と ``Output`` にも同名のクラスデータがある。

``Component.supported = ()``
  種別名を集めたもの。
  意味は「このクラスがサポートしている種別の一覧」ぐらいだろう。

  * サブクラス側で上書き、実行時には変更なし。

``def supports(self, format)``
  問い合わせメソッド。
  意味は「このクラスは ``format`` をサポートしているか？」であり、
  この判定に先述のクラスデータを参照する。

  引数 ``format`` は文字列とする。

サブクラス
----------------------------------------------------------------------
``Component`` の直接のサブクラスは次の 3 つである。

* ``Reader``
* ``Parser``
* ``Writer``

Docutils のエンドユーザーが ``Component`` から直接サブクラスを定義することはなさそうだ。

クライアント
----------------------------------------------------------------------
主にモジュール ``docutils.transforms`` の機能が利用する。

* メソッド ``supports`` を利用するのは ``Filter`` という ``Transform`` 系のクラス。
  本節ではこの処理を解読しないでおく。

感想
======================================================================
* ``SettingsSpec`` の設計方針は理解できるが、何か複雑だ。

* ``TransformSpec`` を ``Input`` と ``Output`` が継承しているのは何かの間違いと思う。
  どの子孫クラスも ``get_transforms`` をオーバーライドしていない。

* ``TransformSpec.get_transforms`` のように、
  オブジェクトというよりは型を操作するやり方には馴染んでおきたい。

* Docutils はクラスデータを C++ 風に言えば ``static const`` のように扱うポリシーなのだろう。
  クラスデータをサブクラスで上書きするという方法は私はあまり採らないので、
  これは大いに参考にしたい。

.. include:: /_include/python-refs-core.txt
