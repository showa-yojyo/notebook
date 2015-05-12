======================================================================
環境設定
======================================================================
Matplotlib_ を利用するための環境をもっと細かく整備してみよう。

.. todo::

   細かく。もっと細かく。

.. contents::

設定ファイル :file:`$HOME/.matplotlib/matplotlibrc`
======================================================================
ファイル名からわかるように、Matplotlib 環境のユーザー設定ファイルだ。
ドキュメントのセクション 5.1 "The matplotlibrc file" に詳しく記述がある。

* Windows 環境でもユーザーがわざわざ環境変数 ``HOME`` を設定している場合は、
  Matplotlib はきちんとそのパスを参照してくれる。

* 一度でも Matplotlib を利用すると、
  ``$HOME`` にフォルダー :file:`.matplotlib` ができている。
  そこにテキストファイル :file:`matplotlibrc` を作成する。

* テンプレは :file:`$PYTHONHOME/lib/site-packages/matplotlib/mpl-data/matplotlibrc` を使う。

  テンプレは基本的に設定コマンド？のコメントアウトで埋め尽くされている。
  ここを眺めていればカスタマイズの方法は直感できる仕組みになっている。

* :file:`matplotlibrc` は python-mode で編集するのが吉。

.. include:: /_include/python-refs-sci.txt
