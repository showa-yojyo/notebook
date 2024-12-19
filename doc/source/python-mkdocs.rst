======================================================================
MkDocs 利用ノート
======================================================================

.. contents:: 章見出し
   :local:

概要
======================================================================

MkDocs_ による自己紹介：

   MkDocs is a **fast**, **simple** and **downright gorgeous** static site
   generator that's geared towards building project documentation. Documentation
   source files are written in Markdown, and configured with a single YAML
   configuration file.

原稿が Markdown 書式で記述され、文書構築構成を YAML ファイルで行うという様式は
Jekyll_ と同じだが、MkDocs_ は Ruby ではなく Python で実装されている。コマンド実
行で HTTP サーバーが走り出し、HTML ファイルを供給するようになるという動作も共通
している：

   MkDocs comes with a built-in dev-server that lets you preview your
   documentation as you work on it. Make sure you're in the same directory as
   the :file:`mkdocs.yml` configuration file, and then start the server by
   running the ``mkdocs serve`` command

このコマンドで作動しているサーバーは自動リロードに対応している。構築構成、文書
ディレクトリー、テーマーディレクトリーに変更が生じた場合、生で再構築する。

.. seealso::

   :doc:`/python-sphinx`
      MkDocs_ とは異なり、Sphinx_ は Markdown ではなく reStructuredText を既定の
      原稿書式とする。また、HTTP サーバーを自前で持っていない。
   :doc:`/ruby-jekyll`
      MkDocs_ は、上述のように Jekyll_ とは共通点が多い。

インストール・更新・アンインストール
======================================================================

複数人で共用するプロジェクトの開発環境に MkDocs_ をインストールする事例では、そ
のプロジェクトの定める手順に従え。README や :file:`pyproject.toml` を読めば判明
する。

自分が所有する作業用仮想環境にインストールするならば、愛用している仮想環境ツール
がインストールコマンドを実装している場合にはそれを使え。私ならば Miniconda_ であ
るから、例えば次のようにする：

.. sourcecode:: console
   :caption: 現在の conda 仮想環境に MkDocs をインストールする
   :force:

   conda install -c conda-forge mkdocs

インストール手順の説明は以上だ。MkDocs_ の更新、アンインストールの手順は、対応す
る条件におけるインストール手順に合致する手順を選べ。例えば :program:`conda` を
使っているのならば ``conda uninstall mkdocs`` を走らせる。

.. seealso::

   :doc:`/python-miniconda`

構成・カスタマイズ
======================================================================

テーマに関しては次の節。

使用方法・コツ
======================================================================

.. todo::

   * テーマ
   * 生編集サーバー
   * プラグイン

資料集
======================================================================

MkDocs_ は難しいツールではないので、機能を詳細に解説することを目的とする記事は多
くは存在しない。

MkDocs_
   公式文書。これだけを熟読することで習得は十分可能だ。
`MkDocs - Full Stack Python <https://www.fullstackpython.com/mkdocs.html>`__
   MkDocs_ をどう発音するのかがわかる。
`GETTING STARTED WITH MKDOCS: A BEGINNER'S GUIDE <https://medium.com/@TemitopeVictoria/getting-started-with-mkdocs-a-beginners-guide-e6dcdcc98493>`__
   入門記事。内容はバランス良くまとまっている。開発環境は Windows を想定。
`System Health Lab Mkdocs Tutorial and Template <https://tutorial-mkdocs.systemhealthlab.com/>`__
   入門記事。チュートリアルで構成。GitHub テンプレリポジトリーから作業を始める。
   この手の Markdown 仕様の解説は初めて見た。
`A beginner guide to using MKDocs <https://coreyodonis.hashnode.dev/a-beginner-guide-to-using-mkdocs>`__
   入門記事。プラグインに関する記述が少々ある。
`MKDocs: The Ideal Tool for Effective Documentation <https://medium.com/cranecloud/mkdocs-the-ideal-tool-for-effective-documentation-31da0666bb05>`__
   なぜ MkDocs_ が良いのかを説明している。
`Learn / MkDocs <https://learn.openwaterfoundation.org/owf-learn-mkdocs/>`__
   MkDocs_ 利用環境のセットアップと、利用に必要な情報や作業を順序立てて述べてい
   る。

.. include:: /_include/python-refs-core.txt
.. _Jekyll: https://jekyllrb.com/
.. _MkDocs: https://www.mkdocs.org/
