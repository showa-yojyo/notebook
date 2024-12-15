======================================================================
Ruff 利用ノート
======================================================================

.. contents:: 章見出し
   :local:

概要
======================================================================

公式文書冒頭によると、Ruff_ は自らを次のように規定している：

   An extremely fast Python linter and code formatter, written in Rust.

静的解析や書式整形を超高速に実行するのはありがたい。Ruff_ はさらに、先行する同種
の道具の上を行くと豪語している：

   Ruff can be used to replace Flake8 (plus dozens of plugins), Black, isort,
   pydocstyle, pyupgrade, autoflake, and more, all while executing tens or
   hundreds of times faster than any individual tool.

Ruff_ が比較対象に挙げているものを現在利用しているのであれば、乗り換えを検討する
価値がある。

.. seealso::

   :doc:`/python-pylint`

インストール・更新・アンインストール
======================================================================

複数人で共用するプロジェクトの開発環境に Ruff_ をインストールする事例では、その
プロジェクトの定める手順に従え。README や :file:`pyproject.toml` を読めば判明す
る。

自分が所有する作業用仮想環境にインストールするならば、愛用している仮想環境ツール
がインストールコマンドを実装している場合にはそれを使え。私ならば Miniconda_ であ
るから、例えば次のようにする：

.. sourcecode:: console
   :caption: 現在の conda 仮想環境に Ruff をインストールする
   :force:

   conda install -c conda-forge ruff

インストール手順の説明は以上だ。Ruff_ の更新、アンインストールの手順は、対応する
条件におけるインストール手順に合致する手順を選べ。例えば :program:`conda` を使っ
ているのならば ``conda uninstall ruff`` を走らせる。

.. seealso::

   :doc:`/python-miniconda`

構成・カスタマイズ
======================================================================

使用方法・コツ
======================================================================

資料集
======================================================================

Ruff_
   公式文書。
`lint - What is "Linting"? <https://stackoverflow.com/questions/8503559/what-is-linting>`__
   Stack Overflow 内の質疑応答スレ。

.. include:: /_include/python-refs-core.txt
.. _Ruff: https://docs.astral.sh/ruff/
