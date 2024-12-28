======================================================================
Microsoft SQL Server 利用ノート
======================================================================

:Since: 1989
:Official site: <https://www.microsoft.com/sql-server>
:Version: TBW

現状、SQL Server を学習する気がないが、その時に備えて環境を整える手順くらいは記
しておく。

.. rubric:: 以前の SQL Server 環境の残滓を一掃する

何かのチュートリアルで WSL Ubuntu に SQL Server をおそらく :program:`apt` でイン
ストールしたらしいのだが、どこかで勝手に独自の手順を入れたのか、``apt list`` を
実行すると関連パッケージが表示されてしまう。これをまず解決する。

こういう問題がある場合は :program:`apt-add-repository` を使うことを覚えておけ：

.. sourcecode:: console
   :caption: よくある :program:`apt-add-repository` 用例

   $ apt-add-repository -L | grep mssql-server
   deb [arch=amd64,armhf,arm64] https://packages.microsoft.com/ubuntu/20.04/mssql-server-preview focal main
   $ sudo apt-add-repository -r deb [arch=amd64,armhf,arm64] https://packages.microsoft.com/ubuntu/20.04/mssql-server-preview focal main

.. todo::

   この手順を要するパッケージが他にもあるので、専用ノートを設けるのがいい。
