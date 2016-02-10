======================================================================
サブパッケージ ``docutils.languages``
======================================================================
Docutils_ における多言語対応のフレームワークとして、
サブパッケージ ``docutils.languages`` およびその構成モジュールがある。
これらのコードを読んでいく。

.. contents:: ノート目次

利用側
======================================================================
このサブパッケージの利用者は ``transforms`` と ``writers`` だ。
これらが行う処理の手順は次のとおり。

#. 欲しい言語を決める。
   例えば英語化したければ文字列 ``en`` を、
   日本語化したければ文字列 ``ja`` を用いる。

#. サブパッケージ ``docutils.languages`` から関数 ``get_language`` をインポートする。

   .. code-block:: python3

      from docutils.languages import get_language

#. 関数を呼び出す。
   このとき、上記の言語コードを入力とする。
   戻り値は Python のモジュールそのものとなる。

   .. code-block:: python3

      languages = get_language('ja')

#. 必要に応じて受け取ったモジュールから何らかのデータを得る。
   例えば caution タグ用のラベルテキストを得るにはこうする。

   .. code-block:: python3

      label_caution = self.language.labels['caution']

   もっとも、インポートモジュールから直接得られるオブジェクトは次のものだけだ。
   各オブジェクトの意味は本節では割愛する。

   * ``labels``: 辞書オブジェクト。
   * ``bibliographic_fields``: 辞書オブジェクト。
   * ``author_separators``: リストオブジェクト。

実装簡易版
======================================================================
関数 ``get_language`` を解読する。
本物ではなく、処理の本質と関わらないコードを取り除いた版を示す。

.. code-block:: python3

   _languages = {}

   def get_languages(tag):
       """Return module with language localizations."""

       if tag in _languages:
            return _languages[tag]

       try:
           module = __import__(tag, globals(), locals(), level=1)
           _languages[tag] = module
           return module
       except ImportError:
           # ...

       module = __import__('en', globals(), locals(), level=1)
       _languages[tag] = module
       return module

* ``__import__`` という、Python のドキュメントが使用を推奨したくない関数を利用している。

  * ``level`` は基本は 1 を指定する。
    どうもこのモジュールのディレクトリーに対しての、
    検索する親ディレクトリーの数の意味らしい。

* 一度 ``__import__`` が成功した言語モジュールは、キャッシュしておくのがコツのようだ。
* Docutils がデフォルトでサポートしていない言語が指定された場合は、
  自動的に英語版 ``en`` モジュールを当関数の出力とする。

感想
======================================================================
* 設計の着想としては二つある。
  言語データごとに Python のモジュールを専用のサブパッケージに用意することと、
  実行時に特定の言語用モジュールをインポートする（させる）ということだ。

* モジュールを動的にインポートするには、Python の組み込み関数 ``__import__`` を利用する。
  いつもの静的インポート文と使い分ける。

* 各言語用モジュールの作成は人力による。
  イタリア語を知らなければまともな ``it.py`` を提供することはできない。

* ここで実現されている方法論はどちらかというと容易な部類に入る。
  是非モノにしたい。

.. include:: /_include/python-refs-core.txt
