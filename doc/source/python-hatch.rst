======================================================================
Hatch 利用ノート
======================================================================

.. contents:: 章見出し
   :local:

概要
======================================================================

   Hatch is a modern, extensible Python project manager.

一言で表現すると確かにこれ以外のものが思いつかない。やれることがたくさんある。

   The high level value proposition of Hatch is that if one adopts all
   functionality then many other tools become unnecessary since there is support
   for everything one might require. Further, if one chooses to use only
   specific features then there are still benefits compared to alternatives.

例えば次の機能を備えている：

* Python 仮想環境管理
* クロスプラットフォーム
* 依存パッケージの導入や更新などの環境
* ビルド構成
* 製品バージョン更新
* テストおよびコード静的解析手順構成
* 成果物の配備

インストール・更新・アンインストール
======================================================================

愛用している仮想環境ツールがインストールコマンドを実装している場合にはそれを使え。
私ならば Miniconda_ であるから、例えば次のようにする：

.. sourcecode:: console
   :caption: 現在の conda 仮想環境に Hatch をインストールする
   :force:

   conda install -c conda-forge hatch

インストール手順の説明は以上だ。Hatch_ の更新、アンインストールの手順は、対応す
る条件におけるインストール手順に合致する手順を選べ。例えば :program:`conda` を
使っているのならば ``conda uninstall hatch`` を走らせる。

.. seealso::

   :doc:`/python-miniconda`

構成・カスタマイズ
======================================================================

使用方法・コツ
======================================================================

資料集
======================================================================

Hatch_
   公式。

.. include:: /_include/python-refs-core.txt
.. _Hatch: https://hatch.pypa.io/latest/
