================================================================================
Python 全般に関するノート
================================================================================

.. contents:: 見出し一覧
   :local:

パッケージの取り扱い関連
================================================================================

.. _python-pkg-install-anchor:

インストール・更新・アンインストール
--------------------------------------------------------------------------------

サードパーティー製のパッケージをインストール・更新・アンインストールする手順は
パッケージによらずほとんど同一だ。共通手順をここに記す。

PyPI_ に識別子 ``PKG_NAME`` で登録されている Python パッケージをインストールする
には、使用している管理プログラム (:program:`pip`, :program:`conda`,
:program:`mamba`, :program:`uv`, etc.) に応じて、シェルで次のように実行する：

.. sourcecode:: bash
   :caption: インストール命令例

   pip install PKG_NAME
   conda install -n ENV_NAME PKG_NAME
   mamba install -n ENV_NAME PKG_NAME
   uv add PKG_NAME
   uv pip install PKG_NAME

ここで、``ENV_NAME`` とあるのは、管理プログラムが認識可能な仮想環境の名前とす
る。上の例で ``ENV_NAME`` が見えないものについては、呼び出し時点で活動中の仮想環
境が対象となるか、システムに ``PKG_NAME`` がインストールされることになる。

また、実践ではさまざまなオプションや semantic version 指定が加わるはずだ。

更新、削除についても対応する道具の更新、削除命令を実行しろ。おそらく ``update``,
``upgrade``, ``remove``, ``uninstall`` のような名前の命令があるはずだ。

.. seealso::

   * :doc:`/python-pip`
   * :doc:`/python-micromamba`

.. _PyPI: https://pypi.org/
