======================================================================
Miniconda 利用ノート
======================================================================

.. |bashrc| replace:: :file:`.bashrc`
.. |conda| replace:: :program:`conda`
.. |condarc| replace:: :file:`.condarc`

Miniconda_ の利用に関する事実関係の覚え書きと、その利用について思うところを記す。

.. contents:: 見出し
   :local:

.. note::

   本稿執筆時の動作環境は次のとおり。

   :OS: Windows 10 Home (64 bit), WSL2, Ubuntu 24.04.1 LTS
   :Bash: GNU bash, version 5.2.21(1)-release (x86_64-pc-linux-gnu)
   :Miniconda_: 24.3.0

   Python 本体および Python 製パッケージのバージョンについては、必要に応じて本文
   で明記していく。

概要
======================================================================

Conda を含むシステムとして Anaconda_ と Miniconda_ が存在する。本稿では後者のシ
ステムのみを解説していく。

   Miniconda is a free, miniature installation of Anaconda Distribution that
   includes only |conda|, Python, the packages they both depend on, and a small
   number of other useful packages.

Conda とは、オープンソースパッケージの管理システムであり、それらに対する環境管理
システムだ。すなわち、

* パッケージの複数のバージョンおよびそれらの間の依存関係をインストールしたり、
* それら（環境と呼ぶ）を容易に切り替えたり

する機能がある。Conda は Python プログラムについて製作されたものだったということ
だが、現在ではどのようなソフトウェアでもパッケージにしたり配布したりすることが可
能であるそうだ。

   If you need more packages, use the ``conda install`` command to install from
   thousands of packages available by default in Anaconda's public repo, or from
   other channels, like conda-forge or bioconda.

Anaconda_ が既定の状態でかなりのパッケージを自動的にインストールするのに対し、
Miniconda_ は |conda|, Python および依存パッケージしか含まない。ドキュメントをす
べて読んだわけではないが、両者の決定的な違いはこれだけではないかと思う。

その他、|conda| にはレジストリーに所望のパッケージが存在するかを問い合わせたり検
索したりする機能や、当然ながら、インストール済みのパッケージの一覧表示、更新、削
除といった機能がある。

.. note::

   Miniconda_ 環境下で ``pip install`` を併用することも可能ではあるが、その場合は
   には後者の登録庫にしか当該パッケージが存在しないことを必ず確認しろ。

このノートを読み返すときに得られるようにしておく情報は次のとおり：

#. 必要なら古い Miniconda_ を環境ごとアンインストールする
#. Miniconda_ をインストールする
#. 所望の Python バージョンに対応する仮想環境を構築する
#. 仮想環境に所望のパッケージをインストールする

アンインストール手順
======================================================================

Anaconda documentation 内記事 `Uninstalling Miniconda
<https://docs.anaconda.com/miniconda/uninstall/>`__ の Linux プラットフォームの
手順に従え。

インストールをアレンジした場合、インストールディレクトリーは後述のように変更した
ならば ``rm -rf`` の引数をそれに合わせろ。仮想環境は本体と同時に消失する。

構成ファイルを完全に削除する場合は、どのディレクトリーに置いたのかを忘れても、コ
マンド ``conda info`` で確認しろ。構成ファイルについては後述する事項にも留意しろ。

インストール手順
======================================================================

Anaconda documentation 内記事 `Installing Miniconda
<https://docs.anaconda.com/miniconda/install/>`__ の Linux プラットフォームの手
順に従え。

本体
----------------------------------------------------------------------

本体のインストール手順は専用シェルスクリプトをダウンロードして実行するというもの
だ。

   These four commands download the latest 64-bit version of the Linux
   installer, rename it to a shorter file name, silently install, and then
   delete the installer:

   .. sourcecode:: console
      :caption: 当該記事 Quick command line install 節より
      :force:

      mkdir -p ~/miniconda3
      wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
      bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
      rm ~/miniconda3/miniconda.sh

このスクリプトは 140 MB 程度の巨大なファイルであり、内容を確認するのは控えざるを
得ない。この例で用いられているインストーラーのコマンドラインオプションは次のとお
り：

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   オプション @ 動作
   ``-b``        @ バッチモード（対話的操作なし）でインストールを実行する
   ``-p PREFIX`` @ パス ``PREFIX`` にインストールする
   ``-u``        @ 既存のインストールを更新する

これらのコマンドをそのまま実行しない。使用者が自分なりにアレンジするのが通例だ。
例：

* 専用作業ディレクトリーでコマンドを実行する
* 本文が勧めるように、ダウンロードファイル名を紛れのない名前にする
* インストール先を ``$HOME`` 直下にしない (e.g. ``-p $XDG_DATA_HOME/miniconda3``)

仮想環境を作成する
======================================================================

インストール時点で ``base`` という仮想環境が用意されているが、それだけをそのまま
使い続けるのでは何のために Miniconda_ を利用しているのかわからない。少なくとも、
Python のマイナーバージョンごとに仮想環境を構築することを考える。

ゼロから構築する
----------------------------------------------------------------------

仮想環境を構築するには ``conda create`` コマンドを実行する。仮想環境にはわかりや
すい名前をなるべくつけろ。安直でかまわない。例えば Python 3.13 が入手可能の最新
版ならば次のような手順が自然だ：

.. sourcecode:: console
   :caption: ``conda create``
   :force:

   conda create -c conda-forge -n python-3.13 "python>=3.13"
   conda activate python-3.13

仮想環境を作成したら、何かしらのパッケージをただちにインストールするのが普通だ。
インストール時のコマンドライン引数を減らすために、対象環境を activate しておく。

仮想環境作成と同時にパッケージも導入する
----------------------------------------------------------------------

あらかじめ利用したいサードパーティー製パッケージが判明している場合には、仮想環境
作成コマンドライン引数にパッケージ名を列挙すればよい。必要最低限に絞っておくのが
コツだ：

.. sourcecode:: console
   :caption: 仮想環境 `myenv` を作成すると当時に Scrapy をインストールする
   :force:

   conda create -c conda-forge -n myenv "python>=3.13" scrapy "pyopenssl>=24"

Python パッケージ
======================================================================

Python パッケージをインストールするのは、戦術の手順を実施して Miniconda_ 本体が
所望のパスにインストールされたことを検証してからにしろ。また、構成ファイルでダウ
ンロードチャンネルを適切に指定するのを済ませてからにしろ。

仮想環境からパッケージをアンインストールする
----------------------------------------------------------------------

仮想環境 `myenv` から例えば Scrapy をアンインストールするには次のようにする：

.. sourcecode:: console
   :caption: ``conda remove`` 実行例
   :force:

   conda remove -n myenv scrapy

* このとき、Scrapy に依存する別のパッケージも併せてアンインストールされる。
* パッケージを一度に複数アンインストールすることも可能。引数にパッケージ名を並べ
  れば良い。

すべてのインストール済みパッケージをアンインストールするならば、次のようにするの
がよい：

.. sourcecode:: console
   :caption: ``conda remove --all`` 実行例
   :force:

   conda remove -n myenv --all --keep-env

仮想環境 `myenv` 自体が不要というのならばオプション ``--keep-env`` を与えなけれ
ばよい。

仮想環境にパッケージをインストールする
----------------------------------------------------------------------

仮想環境 `myenv` に例えば Scrapy をインストールしたいとする。次のようにしろ：

.. sourcecode:: console
   :caption: ``conda install`` 実行例
   :force:

   conda install -c conda-forge -n myenv scrapy "pyopenssl>=24"

仮想環境におけるパッケージ一覧を示す
----------------------------------------------------------------------

仮想環境におけるパッケージ一覧を示すにはコマンド ``conda list`` を使う。

:samp:`conda list -n {myenv}`
   仮想環境 ``myenv`` にインストールしたパッケージすべてを確認する。
:samp:`conda list -n {myenv} --export`
   コマンド ``coda create`` オプション ``--file`` の引数ファイルの内容として有効
   な書式で出力する。出力をファイルに保存しておき、後で新しい仮想環境を構築する
   ときの入力として使用することが可能だ。
:samp:`conda list -n {myenv} --show-channel-urls`
   チャンネル URL と共に出力する。パッケージが conda-forge からインストールした
   ものであるかを確認するのに使える。

仮想環境にあるパッケージを更新する
----------------------------------------------------------------------

パッケージを更新するにはコマンド ``conda update`` を用いる。ここで言う更新とは、
互換性のある最新版に置き換えることを意味する。パッケージ名（一般には複数）を受け
取り、環境内の他のすべてのパッケージと互換性のあるバージョンをダウンロードして置
き換えるのだ。

最新版をインストールすることを達成するために、インストール済みのパッケージを更新
したり、他のパッケージを追加的にインストールしたりすることがある。

:samp:`conda update -c conda-forge -n {myenv} pyopenssl`
   パッケージ pyOpenSSL を更新する。仮想環境 `myenv` にインストールされているも
   のとする。
:samp:`conda update -c conda-forge -n {myenv} --all`
   パッケージすべてを更新する。パッケージ名を列挙する手間が省略できている。

パッケージを集約庫から検索する
----------------------------------------------------------------------

目当てのパッケージを検索するというより、その最新バージョンを確認するほうが主な目
的としてコマンド ``conda search`` を実行する。基本的には conda-forge からしか検
索しないのが望ましい：

.. sourcecode:: console
   :caption: ``conda search`` 実行例
   :force:

   conda search -c conda-forge 'python>=3.14'
   conda search conda-forge::python[version='>=3.14']

構成
======================================================================

Miniconda_ の動作や配置をカスタマイズしたい。インストールパスは既定のものとは変
更することは前述した。

Bash 起動ファイルに関連コードを追加する
----------------------------------------------------------------------

Bash 使用者おなじみの |bashrc| に |conda| がシェルとうまく相互作用するためのコー
ドを ``conda init`` コマンドを実行することで挿入する：

.. sourcecode:: console
   :caption: ``conda init`` 実行例
   :force:

   conda init -d -v --user
   conda init

プレビューを確認してからオプションを外してコマンドを実行することで |bashrc| を変
更するのが堅実だろう。このコマンドが生成するコードが少々悪いので、定数を適宜宣言
し、リテラル表現を置き換えるなどして保守性を高めてもよいが、どうせ ``conda init``
を再実行する機会はもうないので不要とも考えられる。

.. sourcecode:: bash
   :caption: ``conda init`` が生成するコード片
   :force:

   # >>> conda initialize >>>
   # !! Contents within this block are managed by 'conda init' !!
   __conda_setup="$('/path/to/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
   if [ $? -eq 0 ]; then
       eval "$__conda_setup"
   else
      if [ -f "/path/to/miniconda3/etc/profile.d/conda.sh" ]; then
          . "/path/to/miniconda3/etc/profile.d/conda.sh"
      else
          export PATH="/path/to/miniconda3/bin:$PATH"
      fi
   fi
   +unset __conda_setup
   # <<< conda initialize <<<

この作業により、特にコマンド ``conda activate`` と ``conda deactiate`` が
Miniconda_ の想定どおりに機能するようになる。

ユーザー構成ファイルパスを変更する
----------------------------------------------------------------------

複雑な事情により、次の手順のようにするのが最善であることを述べるのは割愛する。

.. rubric:: 事前条件

* 環境変数 :envvar:`XDG_CONFIG_HOME` がいつものように設定されている
* ディレクトリー :file:`$XDG_CONFIG_HOME/conda/condarc.d` が存在する
* 上記ディレクトリーにファイル |condarc| が存在する

.. rubric:: 構成ファイルパス設定手順

#. Bash 起動ファイル |bashrc| に環境変数 :envvar:`CONDARC` を定義する。
   値は |condarc| への絶対パスとする。
#. ファイル :file:`$HOME/.condarc` が生成されていたら、それをファイル
   :file:`$CONDARC` に上書きしてしまう。
#. ディレクトリー :file:`$HOME/.conda` が生成されていたら、それを
   ディレクトリー :file:`$XDG_CONFIG_HOME/conda` として移転する。
#. シンボリックリンクを下記のように二つ作成する。

.. sourcecode:: bash
   :caption: |bashrc| で :envvar:`CONDARC` を定義する例

   export CONDARC="$XDG_CONFIG_HOME/conda/condarc.d/.condarc"

.. sourcecode:: console
   :caption: 構成ファイルパス設定手順例
   :force:

   mv ~/.condarc "$CONDARC"
   mv ~/.conda/* $XDG_CONFIG_HOME/conda
   ln -s "$CONDARC" ~/.condarc
   ln -s ~/$XDG_CONFIG_HOME/conda ~/.conda

このようなシンボリックリンクを使用者が用意する必要がないように Miniconda_ が設計
されていて然るべきなのだが、動作を見る限りではそうなっていない。

.. seealso::

   * :doc:`/xdg`
   * `Using the .condarc conda configuration file
     <https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html>`__

チャンネルを変更する
----------------------------------------------------------------------

コマンド ``conda install`` や ``conda update`` など、パッケージをどの置場から取
得するかを指定するにはオプション :samp:`-c {CHANNEL}` が基本的だ。この値を構成
ファイルから指定することが可能だ。コマンド ``conda config`` を実行する：

.. sourcecode:: console
   :caption: ``conda config --add channels`` の例
   :force:

   conda config --add channels conda-forge
   conda config --show channels

コマンド ``conda config --show`` でその他も含むディレクトリーパスを確認可能だ。

呪文一覧
======================================================================

基本
----------------------------------------------------------------------

``conda --help``
   |conda| の使用法を示す。コマンド一覧を確認可能。
:samp:`conda {COMMAND} --help``
    コマンド :samp:`conda {COMMAND}` の用途、引数、オプションを示す。
``conda --version``
   |conda| のバージョンを示す。

* オプション :samp:`-n {ENVIRONMENT}` があるコマンドでは作用する仮想環境を指定可
  能。指定しない場合には active な仮想環境が適用される。
* オプション :samp:`-c {CHANNEL}` があるコマンドでは、パッケージ取得源となるチャ
  ンネルを指定可能。指定しない場合には |condarc| に基づいて決定される。
* オプション ``-d``, ``--dry-run`` があるコマンドでは、その実行結果を下見可能だ。

Miniconda 構成を変更・表示する
----------------------------------------------------------------------

コマンド ``conda config`` でファイル |condarc| に記載した項目を操作する。Git で
言うところのコマンド ``git config`` を意識したものだという。

.. rubric:: 確認

``conda config``
   何も起こらない。
``conda config --show``
   最終的な構成値すべてを示す。
``conda config --show channels``
   構成項目 ``channels`` の内容を出力する。本ノートの立場では ``conda-forge`` が
   ただ一つの登録項目として示されて欲しい。
``conda config --show envs_dirs``
   仮想環境が収納されるディレクトリー一覧を出力する。なぜ複数あるのか？
``conda config --show-sources``
   |conda| が認識している構成ファイルすべての一覧を出力する。
``conda config --describe``
   ファイル |condarc| の雛形を出力する。
``conda config --validate``
   |condarc| すべてを検証する（構成ファイルの書式エラーを調べる）。

.. rubric:: 変更

項目変更操作では対象となる |condarc| を明示的に選択するのが良い：

.. csv-table::
   :delim: @
   :header-rows: 1
   :widths: auto

   オプション @ 対象構成ファイルパス
   ``--system`` @ :file:`$CONDA_ROOT/.condarc`
   ``--env`` @ :file:`$CONDA_PREFIX/.condarc`

``CONDA_ROOT`` および ``CONDA_PREFIX`` の値は次の節で述べるコマンドで得られる。
どちらも指定しない場合にはユーザー |condarc| が対象となる。

コマンド ``conda config`` は仮想環境を指定するオプションを備えていない。

``conda config --env --remove channels defaults``
   現在の仮想環境のパッケージ登録庫から ``defaults`` を外す。
``conda config --env --add channels conda-forge``
   現在の仮想環境のパッケージ登録庫に ``conda-forge`` を加える。この二つのコマン
   ドを実行しておくことにより、現在の仮想環境を対象とする |conda| コマンド実行時
   にオプション ``-c conda-forge`` を明示的に指定する手間が省ける。
``conda config --set channel_priority strict``
   |condarc| に記載したチャンネルを記載順に優先するように指定する。チャンネル一
   覧に ``defaults`` を残している場合にこの指定は重要だ。

Miniconda 自体の情報を示す
----------------------------------------------------------------------

``conda info``
   目的に合わせてオプション ``--json`` を指定し、JSON 書式で出力することも考えろ。
``conda info --base``
   仮想環境 ``base`` のルートディレクトリーパスしか示さない。
``conda info --envs``
   仮想環境一覧。米印の付くものは現在の仮想環境を示す。
``conda info --system``
   |conda| が用いる環境変数の一覧を含む情報各種を示す。このコマンド出力から意図
   せぬパスが値になっていないことを確認しろ。

   上の表にある ``CONDA_ROOT`` などはこのコマンドで得られる。

未使用パッケージやキャッシュを消去する
----------------------------------------------------------------------

コマンド ``conda clean`` は掃除操作に使う。仮想環境を指定しない。

``conda clean --all``
   インデックスキャッシュ、ロックファイル、未使用のキャッシュパッケージ、tar
   ファイル、ログファイルを削除する。

   書き込み可能なパッケージを込めてすべてを消去したい場合にはオプション
   ``--force-pkgs-dirs`` を付けろ。

仮想環境を指定して実行形式を走らせる
----------------------------------------------------------------------

他の仮想環境ツールにも同等の機能があるように、コマンド ``conda run`` を使うと、
指定した仮想環境において指定したコマンドを走らせる。利点は ``activate`` と
``deactivate`` を前後に実行する手間が省けることだ。

:samp:`conda run -n {myenv} {COMMAND}`
   仮想環境 `myenv` にあるものとしてコマンド `COMMAND` を実行させる。

資料集
======================================================================

`Miniconda <https://docs.anaconda.com/miniconda/>`__
   Miniconda 公式文書。
`conda-forge documentation <https://conda-forge.org/docs/>`__
   conda-forge 公式文書。User Documentation の章をまずは読め。

雑多なノート
======================================================================

* Anaconda_ ではなく Miniconda_ を選択した理由は、必要十分なパッケージを利用可能
  にしたいからという、個人的な嗜好による。
* Miniconda_ を利用することの（私にとっての元々の）利点は、どのパッケージでもイ
  ンストールとアップグレードの方法が統一化されるということだ。当ノートではいろい
  ろな Python パッケージについての学習事項をつづってきたが、それぞれに記すハメに
  なっていた、インストールおよびアップグレードの手順記載云々をする必要がなくなっ
  たのも大きい。
* Miniforge_ というツールが存在するようだ。本稿では手作業でパッケージチャンネル
  を defaults から conda-forge に置き換えた。これがあらかじめ施されているなどの
  特徴がある。

.. _miniconda-anchor-pip:

:program:`pip` との兼ね合い
----------------------------------------------------------------------

ソースインストールでない ``pip install`` を使えるかどうかを判定したい。

インストールしたいパッケージの公式文書がその手順としてコマンド ``pip install``
を記している場合、まずはコマンド :samp:`conda search -c conda-forge {PKG}` を確
認する。結果が望ましいならば、そのまま ``conda install`` に移行すればいい。

* チャンネル conda-forge にパッケージがない
* パッケージのバージョンが旧版である

など、最善とは言えない条件であるならば、仕方なく ``pip install`` コマンド、また
はプロジェクト指定のパッケージ管理ツールでインストールするしかない。

.. include:: /_include/python-refs-core.txt
.. _Miniforge: https://github.com/conda-forge/miniforge
