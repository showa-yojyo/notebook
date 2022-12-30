======================================================================
基礎クラス群
======================================================================

ここでは Docutils_ の様々なテキスト処理クラス群のスーパークラスとして存在する
``TransformSpec``, ``SettingsSpec``, ``Component`` を見ていく。以下、この 3 クラ
スを基礎クラスと呼ぶことにする。本節の目的は、これらの基礎クラスがどのような機能
を Docutils 内のサブクラスやクライアントに提供しているのかを調査し、いずれ私が類
似のプログラムを書くときに参考にすることだ。

.. contents:: ノート目次

クラス図
======================================================================

本節で登場するクラスを図に示す。

.. mermaid:: ./docutils-base.mmd
   :align: center
   :alt: (class diagram)

クラス ``docutils.SettingsSpec``
======================================================================

* このクラスは実行時に何かの構成・設定値を指定するための枠組みを決める。Docutils
  のための設定ファイルやコマンドラインオプションから値を受け取り、オブジェクトに
  それをセットするという、一連のデータの流れを支える。
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
  設定ファイル群の相対パスを文字列の ``tuple`` で持つ。これは設定ファイルが複数
  ファイルに分割されていて、それらのファイルシステム上での、ある基点からの相対パ
  スということだろう。

  * サブクラスメンバーデータ ``self.relative_path_settings`` に ``extend`` され
    る。

``SettingsSpec.config_section = None``
  設定ファイルのセクション名そのもの。

  * サブクラスが上書きする。

``SettingsSpec.config_section_dependencies = None``
  上述のデータと同様だが、優先順位がより高い。

  * サブクラスが上書きする。

サブクラス
----------------------------------------------------------------------

* ``SettingsSpec`` の直接サブクラスは 2 つだけある。図に示す。

  .. mermaid::
     :align: center
     :alt: (class diagram)

     classDiagram
     direction TB
         SettingsSpec <|-- OptionParser
         SettingsSpec <|-- Component

     class SettingsSpec{
         +tuple settings_spec$
         +dict settings_defaults$
         +dict settings_default_overrides$
         +tuple relative_path_settings$
         +str config_section$
         +tuple config_section_dependencies$
     }

     class OptionParser{
         +tuple settings_spec$
         +dict settings_defaults$
         +tuple relative_path_settings$
         +str config_section$
     }

     class Component{
         +str component_type$
         #tuple supported$
         +supports(str) bool
     }

* ``Component`` では何もオーバーライドしないが、そこからのサブクラスは
  ``settings_spec`` と ``config_section`` を上書きするだけのことが多い。例::

    config_section = 'general'

クライアント
----------------------------------------------------------------------

主な参照箇所はモジュール ``docutils.core`` と ``docutils.frontend`` に集中してい
る。

* ``Component`` 系と ``OptionParser`` 系を読む。
* ``OptionParser.get_config_file_settings`` を読む。
* ``OptionParser.populate_from_components`` を読む。

クラス ``docutils.TransformSpec``
======================================================================

* ``TransformSpec`` はスーパークラスがない。
* メソッド ``get_transforms`` が一つだけある抽象クラスと大づかみに理解してよい。
  必要に応じてサブクラスがオーバーライドする。
* 他にも細かいクラスデータや格納データの約束事があるが、そこまで調査しなくてよい
  だろう。

メンバー
----------------------------------------------------------------------

``get_transforms(self)``
  クラス ``Transform`` のサブクラスを含む ``list`` を返すようにサブクラスがオー
  バーライドする。注意。サブクラスのオブジェクトではなく、あくまでもサブクラスを
  型として取り扱う。

サブクラス
----------------------------------------------------------------------

``TransformSpec`` をスーパークラスとしたクラス図を示す。

.. mermaid::
   :align: center
   :alt: (class diagram)

   classDiagram
       direction TB

       TransformSpec <|-- Component
       TransformSpec <|-- Transformer

       class Component{
           str component_type$
       }

       class Transformer{
           -int serialno
           +add_transform(Transform)
           +add_transforms(...)
           +add_pending(...)
           +apply_transforms()
           +get_priority_string(int) str
           +populate_from_components(components)
       }

       class TransformSpec{
           +get_transforms()
       }

       Transformer o-- Transform: transforms

       Transformer o-- Component: components
       Transformer --> document: document
       %%Node --* document

       class Transform{
           #int default_priority$
           +apply()*
       }

       Transform --> document: document
       Transform --> Node: start_node
       Node <|-- document
       Transform <|-- ConcreteTransform

       class ConcreteTransform{
           #int default_priority$
           +apply()
       }

* ``Input`` および ``Output`` は何もオーバーライドしていないことに注意。設計ミス
  か？
* メソッド ``get_transforms`` は ``Component`` のさらなるサブクラスがオーバーラ
  イドする傾向がある。

クライアント
----------------------------------------------------------------------

メソッド ``get_transforms`` を呼び出すのは何かということになる。

* サブクラス ``Transformer`` が自身のメンバーデータを組み立てるときのパラメー
  ターとして参照する。

これぐらいしかないだろう。

クラス ``docutils.Component``
======================================================================

* ``Component`` は Docutils のテキスト処理系クラスのためのスーパークラス。言い換
  えると ``Reader``, ``Parser``, ``Writer`` がサブクラスとなる。

* ``Component`` のスーパークラスは前述の ``SettingsSpec``, ``TransformSpec``
  だ。なお、この段階ではいずれのスーパークラスのどのメンバーもオーバーライドしな
  いままだ。

メンバー
----------------------------------------------------------------------

クラスデータが 2 個とメソッドが 1 個ある。重要なものだけ記す。

``Component.component_type``
  コンポーネントの種別を示す文字列とする。各サブクラスで上書きする。つまりこのよ
  うなものだ。

  .. csv-table::
     :delim: :
     :header: サブクラス, ``component_type`` の値
     :widths: auto

     ``Reader``:``'reader'``
     ``Parser``:``'parser'``
     ``Writer``:``'writer'``

  * 実は ``Component`` のサブクラスではないクラスである ``Input`` と ``Output``
    にも同名のクラスデータがある。

``Component.supported = ()``
  種別名を集めたもの。意味は「このクラスがサポートしている種別の一覧」ぐらいだろ
  う。

  * サブクラス側で上書き、実行時には変更なし。

``def supports(self, format)``
  問い合わせメソッド。意味は「このクラスは ``format`` をサポートしているか？」で
  あり、この判定に先述のクラスデータを参照する。

  引数 ``format`` は文字列とする。

サブクラス
----------------------------------------------------------------------

``Component`` の直接のサブクラスは次の 3 つである。

* ``Reader``
* ``Parser``
* ``Writer``

Docutils のエンドユーザーが ``Component`` から直接サブクラスを定義することはなさ
そうだ。

クライアント
----------------------------------------------------------------------

主にモジュール ``docutils.transforms`` の機能が利用する。

* メソッド ``supports`` を利用するのは ``Filter`` という ``Transform`` 系のクラ
  ス。本節ではこの処理を解読しないでおく。

感想
======================================================================

* ``SettingsSpec`` の設計方針は理解できるが、何か複雑だ。
* ``TransformSpec`` を ``Input`` と ``Output`` が継承しているのは何かの間違いと
  思う。どの子孫クラスも ``get_transforms`` をオーバーライドしていない。
* ``TransformSpec.get_transforms`` のように、オブジェクトというよりは型を操作す
  るやり方には馴染んでおきたい。
* Docutils はクラスデータを C++ 風に言えば ``static const`` のように扱うポリシー
  なのだろう。クラスデータをサブクラスで上書きするという方法は私はあまり採らない
  ので、これは大いに参考にしたい。

.. include:: /_include/python-refs-core.txt
