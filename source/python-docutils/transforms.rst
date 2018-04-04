======================================================================
サブパッケージ ``docutils.transforms``
======================================================================
Docutils_ のサブパッケージ ``docutils.transforms`` について記す。
モジュールの docstring によるとこのサブパッケージの機能は次のようなものだ。

* 初回構文解析の残作業を仕上げる
* 文書中のハイパーリンクを自動で生成する
* 文書データから情報を抽出し、索引や目次を生成する

.. contents:: ノート目次

クラス図
======================================================================
クラス ``Transformer`` と ``Transform`` を中心に据えた簡素なクラス図を以下に示す。
ただし、本節の考察対象外のクラスは掲載を省略したり、
クラスを意味する矩形を灰色に塗りつぶしたりしてある。

* クラス ``TransformSpec`` および ``Component`` については
  :doc:`./base` を参照。
* クラス ``Node`` と ``document`` には継承関係があるが矢印を省略した。
  :doc:`./nodes` を参照。
* ``module`` の意味については :doc:`./languages` を参照。

.. figure:: /_images/docutils-transforms.png
   :align: center
   :alt: (class diagram)
   :scale: 100%

クラス ``Transform``
======================================================================
スーパークラスはなく、代わりにサブクラスが多数派生しているというクラスだ。

データ
----------------------------------------------------------------------
クラススコープのメンバーデータが一つある。

``default_priority``
  0 以上 999 以下の数値で、この変換オブジェクトの処理優先順位を表現するもの。
  サブクラスで上書きする。

オブジェクトデータは次の三つだ。

``document``
  この変換オブジェクトの対象となる構文木オブジェクト。

  * ``Transformer`` オブジェクトと共有。

``startnode``
  この変換処理の開始ノード。
  おそらくこのノードを根に見立てた部分木の全ノードが処理対象。

  * 構文木すべてのノードを対象とする変換もあり得る。
    その際は ``startnode = None`` としてもよい。

``language``
  言語モジュール。詳しくは :doc:`./languages` 参照。

メソッド
----------------------------------------------------------------------
``apply(self, **kwargs)``
  構文木を変換するためのメソッドだが、実装はサブクラス側になる。
  サブクラスでこのメソッドを上書きしないと ``NotImplementedError`` が送出されることになる。

サブクラス
----------------------------------------------------------------------
クラス ``Transform`` のサブクラスは多数存在し、
このサブパッケージ内にあるモジュールで定義されている。
::

  Transform
      components.Filter
      frontmatter.TitlePrompter
      frontmatter.DocInfo
      misc.CallBack
      misc.ClassAttribute
      misc.Transitions
      parts.SectNum
      parts.Contents
      peps.Headers
      peps.Contents
      peps.TargetNotes
      peps.PEPZero
      references.PropagateTargets
      etc.

一つ例を見よう。
次のコードはモジュール ``docutils.transforms.peps`` から改変引用したものだ。
サブクラス ``Contents`` は空の TOC をドキュメントの適切な位置に挿し込むような変換を施す。
メソッド ``apply`` を上書きして、
構文木ノードのサブクラス ``title``, ``topic``, ``pending`` それぞれのオブジェクトを生成する。
最後にドキュメントの然るべき場所に収める。

.. code:: python3

   from docutils import nodes, languages
   from docutils.transforms import Transform, parts

   class Contents(Transform):

       default_priority = 380

       def apply(self):
           language = languages.get_language(...)
           name = language.labels['contents']
           title = nodes.title('', name)
           topic = nodes.topic('', title, classes=['contents'])

           ...

           pending = nodes.pending(parts.Contents)
           topic += pending
           self.document.insert(1, topic)
           self.document.note_pending(pending)

クラス ``Transformer``
======================================================================
* スーパークラスは ``TransformSpec`` 一つ。
* サブクラスはない。このクラスは継承を目的としていない。
* クラス ``document`` の初期化メソッドで ``Transformer`` オブジェクトを生成して、
  メンバーデータ ``self.transformer`` に収める。
* モジュール ``docutils.core`` のクラス ``Publisher`` に
  ``Transformer`` のメソッドを利用する処理例が見られる。

データ
----------------------------------------------------------------------
メンバーデータはすべてオブジェクトの属性だ。

``self.transforms``
  次の 4-tuple アイテムを格納するリスト。

  * ``str``: 優先度を示す文字列。後述の ``get_priority_string`` の説明を参照。
  * ``transform_class``: ``Transform`` のサブクラスの型。
  * ``node``: 変換処理を施すノードオブジェクト。
  * ``kwargs``: メソッド ``transform_class.apply`` のパラメーター。

``self.unknown_reference_resolvers``
  不明。調べる気がしない。

``self.document``
  この変換オブジェクトの対象となる構文木オブジェクト。

``self.applied``
  変換処理が済んだものを格納するリスト。
  アイテムの型は ``self.transforms`` と同じ。

``self.sorted``
  フラグ。
  メソッド ``apply_transforms`` 内で ``transforms`` のソートが済んだかどうかをマークする。

``self.components``
  辞書オブジェクト。キーはコンポーネントタイプを意味する文字列で、
  値は ``Component`` のサブクラスのオブジェクト。

``self.serialno``
  ソートキーの管理用。
  後述の ``get_priority_string`` の説明を参照。

メソッド
----------------------------------------------------------------------
``add_transform(self, transform_class, priority=None, **kwargs)``
  変換処理を一つだけ登録する。

  * ``transform_class`` は ``Transform`` のサブクラスを型として渡す。
  * ``priority`` は優先度。未指定ならば ``default_priority`` が適用される。
    以降のメソッドでも同様。

  * ``kwargs`` は変換メソッド ``apply`` のパラメーター。
  * ``self.transforms`` にデータが登録されるが、ここではソートし直さない。
    以降のメソッドでも同様。

``add_transforms(self, transform_list)``
  上述メソッドの複数オブジェクト版。

  * 変換処理の優先度は各 ``Transform`` オブジェクトの ``default_priority`` に基いて決まる。
  * 変換処理の対象ノードとパラメーターは両方とも空。

``add_pending(self, pending, priority=None)``
  変換保留になったノードに対する変換処理の登録という、やや複雑な手続きを行う。

  * ``pending`` はノードオブジェクト。
    このメンバーデータの ``transform`` が採用される。

``get_priority_string(self, priority)``
  メソッド ``add_xxxx`` 系の補助メソッド。
  優先度のキーは次の形式の文字列である。
  ::
  
     '{priority:03d}-{serialno:03d}'

  * このメソッドを呼び出す度に self.serialno をインクリメントする。

``populate_from_components(self, components)``
  詳細不明。というより見る気がしない。

``apply_transforms(self)``
  格納されている変換処理を優先順位に従い適用する。

  * ``self.transforms`` から変換データを順次 ``pop`` して ``apply`` していく。
  * 変換処理が済んだら ``self.applied`` に変換データを移す。
  * ループの途中で ``self.transforms`` を再ソートすることがあるようだ。
    ということは、どこかの ``apply`` が間接的に ``self.transforms`` を更新するということか。

感想
======================================================================
構文木を構成するノードを「変形」する処理のための枠組みを与える機能群ということだろう。
個々のノードの属性を更新するような変形も、
ノードの構成を追加したり削除したり置換したり順序を入れ替えたりする変形もあり得る。

.. include:: /_include/python-refs-core.txt
