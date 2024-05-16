======================================================================
環境設定
======================================================================

Matplotlib_ を利用するための環境をもっと細かく整備してみよう。

.. contents:: 見出し一覧
   :local:

.. note::

   このページの一部に関しては次の動作環境を使用：

   :OS: Windows 10 Home x64 上の WSL2
   :Python: 3.12.3
   :Matplotlib: 3.8.4

設定ファイル :file:`matplotlibrc` 概要
======================================================================

Matplotlib 環境のユーザー設定ファイルについて記す。

* Matplotlib が扱う、図式の寸法や図形の色といった、性質のほとんどを指定するため
  に設定ファイルというものを利用することができる。
* 設定ファイル名は :file:`matplotlibrc` だ。
* この設定ファイルによる設定のことを **rc settings** とか **rc parameters** とか
  と呼ぶ。
* その設定ファイルのあるディレクトリーは次の優先度で決まる。

  #. 作業ディレクトリー。
  #. ユーザーの環境依存のディレクトリー。

     * Windows 環境でもユーザーがわざわざ環境変数 ``HOME`` を設定している場合は
       Matplotlib はきちんとそのパスを参照してくれる。
     * 一度でも Matplotlib を利用すると、:file:`$HOME` にフォルダー
       :file:`.matplotlib` ができている。そこにテキストファイル
       :file:`matplotlibrc` を自分で作成する。

       WSL2 などの Linux 系環境では XDG 環境変数を利用するのが定石となっている。
       Matplotlib の場合はこのようにしたい：

       .. code:: bash

          # E.g. in .bashrc:
          export MATPLOTLIBRC="$XDG_CONFIG_HOME/matplotlib"

       次の状態にしたい：

       .. code:: console

          $ python -c 'import matplotlib as mpl; print(mpl.get_configdir())'
          /home/USERNAME/.config/matplotlib

       この運用では環境変数 ``MATPLOTLIBRC`` の定義を明示的に与える必要はない
       が、コンソールで :command:`cd` するときに便利だ。

       既定の設定ファイルをそこへ移す：

       .. code:: console

          $ mkdir -p $MATPLOTLIBRC
          $ mv ~/.matplotlib/* $MATPLOTLIBRC

       .. seealso::

          :doc:`/xdg`

  #. Matplotlib インストール場所から決まるディレクトリー。

     Matplotlib のアップグレードの度に上書きされると思っていたほうがよい。した
     がって、この設定ファイルを編集するような状況はまれだと思う。

* 実際に参照される設定ファイルは、関数 ``mpl.matplotlib_fname`` の呼び出しで確認
  可能。
* インストール場所から決まるディレクトリーに置いてある設定ファイルをコピー、編集
  して使う。

  テンプレは基本的に設定コマンド？のコメントアウトで埋め尽くされている。ここを眺
  めていればカスタマイズの方法は直感できる仕組みになっている。

* 設定ファイル :file:`matplotlibrc` をテキストエディターで編集するときには、もし
  python-mode 的な機能をサポートするエディターを使うのならば、それを ON にする。
  コードの見通しがよくなる（コメント文字列がコメント色になるだけだが）。

カスタマイズする
======================================================================

先述の方法でユーザー設定ファイルを生成し、次のように編集して手持ちのプロットの表
示がどのように変化するのかを検証した。

* PyQt5 が使用可能な環境では試しに ``backend : Qt5Agg`` としてみる。

  * 経験則だが ``backend`` の項目だけは他の項目とは異なり、コメントアウトによる
    デフォルト値適用の解釈がなされないようだ。何らかのバックエンドを明示的に指定
    する必要があるもよう。

* Miniconda_ 管理下における Python 3.5.2 環境では既定のバックエンドである TkAgg
  が指定されたままであると、私の環境では実行時に Segmentation fault を引き起こす。
  そのため、唯一動作確認できたバックエンドである ``backend : Qt4Agg``を、PyQt5
  を利用可能な環境にあれば ``backend : Qt5Agg`` を設定してしのぎたい。
* ``plt.plot`` の線の色は ``axes.prop_cycle`` で指定する。

  * カンマ区切りで数色を一度に指定する。プロットを ``plt.plot`` 呼び出しで追加す
    るたびに、カンマで区切られた色が cyclic に適用されるのだろう。これを確認する
    には :doc:`./basic` で示したポリライン複数本描画スクリプトを利用できる。下記
    のリスト内の内容を修正すると、それにつれて曲線の色が変わることがわかる：

    .. code:: text

       axes.prop_cycle: cycler('color', ['deeppink', 'pink', 'b', 'g', 'r', 'c', 'm', 'y', 'k'])

* LaTeX 周りの設定は要研究。特にフォントの指定は大切そうだ。
* ハードコピーバックエンドのデフォルト値を ``savefig.format`` で設定できる。

  .. code:: text

     savefig.format: png # png, ps, pdf, svg

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
