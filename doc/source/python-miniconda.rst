======================================================================
Miniconda 利用ノート
======================================================================

Miniconda_ の利用に関する事実関係の覚え書きと、その利用について思うところを記す。

.. contents:: 目次見出し
   :local:

.. note::

   本稿執筆時の動作環境は次のとおり。

   :OS: Windows 10 Home (64 bit), WSL2
   :Cygwin: 2.5.2-1, 2.7.0 (64 bit)
   :bash: 4.3.42(4)-release, 4.4.12(3)-release (x86_64-unknown-cygwin), 5.1.16(1)-release (x86_64-pc-linux-gnu)
   :Miniconda_: 4.0.5, 4.1.11, 4.3.14, 4.7.5, 24.3.0

   Python 本体および Python 製パッケージのバージョンについては、必要に応じて本文
   で明記していく。

概要
======================================================================

まずは Conda が何であるかを説明する。 Conda とは、オープンソースパッケージの管理
システムであり、それらに対する環境管理システムである。すなわち、

* パッケージの複数のバージョンおよびそれらの間の依存関係をインストールしたり、
* それら（環境と呼ぶ）を容易に切り替えたり

する機能がある。Conda は Python プログラムについて製作されたものだったということ
だが、現在ではどのようなソフトウェアでもパッケージにしたり配布したりすることが可
能であるそうだ。

次に Conda を含むシステムとして Anaconda_ と Miniconda_ が存在することを一応述べ
る。本稿では後者のシステムのみを解説していく。Anaconda が既定の状態でかなりの
パッケージを自動的にインストールするのに対し、Miniconda は Conda, Python および
依存パッケージしか含まない。ドキュメントをすべて読んだわけではないが、両者の決定
的な違いはこれだけではないかと思う。

最後に Conda を表現するコマンドラインツール :program:`conda` について簡単に述べ
る。Conda の機能の一つである :code:`conda install` コマンドを使えば、720 を超え
る科学計算パッケージを Continuum リポジトリーというところから個別にインストール
することが可能であり、さらに 250 を超える科学計算パッケージを個別にインストール
することが可能だ。その他、:program:`conda` にはリポジトリーに所望のパッケージが
存在するかを問い合わせたり検索したりする機能や、当然ながらインストール済みのパッ
ケージの一覧表示、更新、削除といった機能がある。先に述べた環境切り替えについて
は、付録のシェルスクリプトまたはバッチファイルにて実現することが可能。

補足として、通常の Python 環境と同様に :code:`pip install` を併用することも可能
であることを記し添えておく。 :doc:`/python-pip` も参照。

環境構築手順
======================================================================

次の手順でよい。

#. インストーラーをダウンロードする
#. インストーラーを実行する
#. 30-minute test drive を実施する
#. パッケージをインストールする
#. 個別のパッケージについて動作確認をする
#. 構成ファイルを編集する
#. バックアップ or アップグレード用ファイルを作成する

Miniconda_ のダウンロードページにある Python 3.5 の 64-bit (exe installer) をク
リックして :file:`Miniconda3-latest-Windows-x86_64.exe` というファイル名のインス
トーラーを入手できる。

次にダウンロードしたインストーラーを実行する。選択肢はほとんどなく、せいぜいイン
ストールパスを好みで変更するくらいで、手なりでインストールを終了する。以下、イン
ストールパスを :file:`D:\\Miniconda3` としたものとする。

そして公式ドキュメントの `30-minute test drive <http://conda.pydata.org/miniconda.html>`_
を実施するのがよい。各種基本コマンドを習得するはずだ。この過程で Python 本体と
:program:`conda` 自身のアップグレードも場合によっては生じる。

さて、メインの作業である個々のパッケージのインストールおよびアップグレードだが、
状況に応じて手動による作業の内容が変わってくることが考えられる。ここでは対象パッ
ケージについて次の条件を仮定しておく。

* Python プログラミングの個人研究用という名目の環境を構築したい。暗に旧バージョ
  ンのパッケージの動作確認等は興味の対象外と言いたい。
* :program:`conda` でも :program:`pip` でも取得することになるパッケージのバー
  ジョンが同じであれば、 :program:`conda` のほうを優先する。さもなくば、より新し
  いバージョンを取得する手法のほうを優先する。たいていの場合それは
  :program:`pip` のほうだ。
* ローカルディスク上にある自作のパッケージは :program:`pip` で管理する。この場合
  は常に ``--edit`` コマンドラインフラグを指定する。

パッケージ P を :code:`conda install` によってインストールする場合、P が正常に動
作するかどうかを確認する作業をする。作業方法は P に依存して変化するわけだが、そ
れについては読書ノート内の各パートを参照する。インストールするパッケージ群に依存
関係が存在することがよくあるが、その場合の動作確認の順番は、依存ツリーの根から葉
の方向に進める。また、この作業に先立って従来環境における :file:`site-packages`
の状況を従来環境にあるほうのコマンド :code:`pip freeze` 等を活用して把握しておく
ことだ。必要なパッケージを

#. :code:`pip install` によって得られたものと、
#. 非公式版アーカイブからのインストールで得られたもの

とに分類しておき、整理結果を後の :code:`conda install` と :code:`pip install` の
使い分けの基準とする。

デフォルト環境用の次回以降のアップグレードに備えて
:command:`pip list --export` コマンドで要件文字列をファイル化しておくとよい。こ
れについては次節で述べる。

構成ファイルパスを変更する
----------------------------------------------------------------------

Conda の各種設定はホームディレクトリーに所定の書式で記述された構成ファイル
:file:`.condarc` を作成することでも可能だ。毎度特定のコマンドラインオプションを
指定するようなことがあれば、このテキストファイルにそのようなオプションを記述して
おけば、コマンドラインの入力作業の省力化になる。

:doc:`/xdg` に基づき、:file:`$HOME` 直下からドットファイルを配置するようにしたい。

.. code:: console

   $ mkdir -p $XDG_CONFIG_HOME/conda/
   $ mv ~/.condarc $XDG_CONFIG_HOME/conda/condarc

設定ファイルの中身をどのようにするかは調査中。現在のところは：

.. code:: console

   $ conda config --show-sources
   ==> /home/USERNAME/.config/conda/condarc <==
   auto_activate_base: False
   envs_dirs:
     - ${XDG_DATA_HOME}/conda/envs
   pkgs_dirs:
     - ${XDG_CACHE_HOME}/conda/pkgs
   conda-build:
     root-dir: ${XDG_DATA_HOME}/conda/conda-builds

コマンド ``conda config --show`` でその他も含むディレクトリーパスを確認可能だ。

.. admonition:: 利用者ノート

   その出力によると、値の一部が意図通りに設定されていないことが示される：

   .. code:: text

      envs_dirs:
        - /home/USERNAME/.local/share/conda/envs
        - /home/USERNAME/.local/share/miniconda3/envs
        - /home/USERNAME/.conda/envs

   :file:`/home/USERNAME/.conda` を :file:`$XDG_DATA_HOME/conda/envs` に指定し
   たはずなのだが？

ノート
======================================================================

* Anaconda ではなく Miniconda を選択した理由は、必要十分なパッケージを利用可能に
  したいからという、個人的な嗜好による。
* Python の利用者が Conda が何であるかを理解するには、 `conda vs. pip vs.
  virtualenv
  <http://conda.pydata.org/docs/_downloads/conda-pip-virtualenv-translator.html>`__
  の表を見るのが手っ取り早い。

  * 要するに :program:`pip` + :program:`virtualenv` である。

* Miniconda のインストーラーは正規版の Python のそれとは異なるのか、Windows の
  スタートメニューを変更しないのだろうか。 HTML Help ファイルの Python 3.5.x
  Documentation へのショートカットアイコンがスタートメニューにあるプログラムリス
  トに欲しい。
* 私はパッケージ環境切り替え機能を利用することはほぼないはずだ。Python のサード
  パーティー製パッケージおよび Python 自身を効率的に更新する道具として Miniconda
  を利用していくだろう。
* チュートリアルの 30-minute test drive は無難な作業ばかりなので、これは問題にな
  り得ないはずだった。ところが、私が Cygwin の :program:`bash` でコマンドライン
  操作のすべてを行うのだが、それに関係して一点だけ問題があった。
  :file:`activate` スクリプトによる環境を切り替える処理が失敗していることになか
  なか気付かなかったことだ。

  例えば :file:`activate` スクリプトの処理の本質は「環境変数 ``PATH`` に対して、
  対応する Python 関係のパスを先頭のほうに追加する」ことだ。:file:`deactivate`
  スクリプトはこれと反対のことを行う。今、スクリプトと書いたが、実際には
  :program:`bash` の組み込み関数 ``source`` で実施するものだ。

  このスクリプトは :file:`/d/Miniconda3/envs/myenv` のようなパスを環境変数
  ``PATH`` の先頭付近に「追加」する。ところが私の Cygwin 環境では未だに
  ``/cygdrive`` prefix が生きていたので、全然意味を成さない。Cygwin の
  :file:`/etc/fstab` あるいは :file:`/etc/fstab.d/$USER` の内容を次のように編集
  する必要が生じていた。

  .. code:: text

     # For a description of the file format, see the Users Guide
     # http://cygwin.com/cygwin-ug-net/using.html#mount-table

     # This is default anyway:
     #none /cygdrive cygdrive binary,posix=0,user,noacl 0 0

     # Remove /cygdrive/ prefix:
     none / cygdrive          binary,posix=0,user,noacl 0 0

  この編集作業は本件がなかったとしても、厄介な cygdrive 問題の解決はもっと昔に実
  施してしかるべきだった。反省。
* 非 Miniconda ベースの Python 環境で築いてきた :file:`site-packages` 下を
  Miniconda において再現するとなると、正規環境のそれにおける作業時間よりも長くな
  るのかもしれない。 Matplotlib_ のインストールを実施したところ、何やら依存パッ
  ケージのインストールが絡んできて、そのコストが某サイトの非公式 Wheel を用いた
  インストールよりも明らかに高く付いた。

  * なお、完全移行達成までは元の正規 Python 環境を解体せぬことだ。環境変数
    ``PATH`` の単純な書き換えでいつでも新旧 Python 間の切り替えが可能だ。動作の
    比較も容易い。元の環境を放棄する必要性は一般にはない。私にとっては本物は一つ
    でいいので捨てる。
  * 元の Python 環境での :command:`pip freeze` の出力結果を控えておくこと。
    :doc:`/python-pip` 参照。
* :program:`conda` のコマンドライン操作の設計がドキュメントに頼る必要がないほど
  質素であるため、当ノートでは「呪文表」を作成しない。いつでも
  :command:`conda --help` なり :command:`conda command --help` の出力メッセージ
  で事足りる。
* Conda の ``install`` コマンドによる Matplotlib_ を用いて、バックエンドを既定の
  ``TkAgg`` にしたときのウィンドウの表示時に Segmentation fault が発生する不具合
  が私の環境で現在発生している。この不具合のために、元の Python 環境を削除するの
  を躊躇している。

  * 応急処置としてはバックエンドを ``Qt4Agg`` にセットすることだ。これにより
    :code:`plt.show()` などの呼び出しで落ちることはなくなる。設定方法については
    :doc:`/python-matplotlib/basic` および :doc:`/python-matplotlib/config` を参
    照。
  * 仮に :command:`conda install matplotlib` ではなく、いつもの非公式バイナリー
    を :command:`pip install` したらおそらく動作すると思われる。そのためには先に
    別途非公式版をダウンロードしておく必要があるのだが、何のために Miniconda を
    導入したのかわからなくなる。
* パッケージ P について、:command:`conda install P` してから
  :command:`pip install P` することが可能であることがある。可能な場合には、これ
  らが同一環境下に共存する。

  * 環境にある全パッケージを単にアップグレードするには、次のコマンドでよい。

    .. code:: console

       bash$ conda update --all --yes

  * 困ったことに :program:`pip` によってインストールしたパッケージのバージョンが
    :program:`conda` のものより新しい傾向がある。例えば上記コマンドの実行直後に
    :command:`pip list -o` すると、なおパッケージ名が列記されることがある。この
    ようなパッケージは :program:`conda` での管理とは別に「手動で」管理するハメに
    なる。インストールもアップグレードもなるべく :program:`conda` で統一したいの
    だが。
  * 一括アップグレードを実現する場合、このことが重要である。
    つまり、次のような手順を採用することになるだろう。

    .. code:: console

       bash$ conda update --all --yes
       bash$ pip install --upgrade --requirement reqpip.txt

    ここで、パッケージ一覧ファイル :file:`reqpip.txt` はあらかじめ用意する必要が
    あるものである。

  * パッケージ間の依存関係とインストール時に用いたツールの違いが問題になることは
    あるだろうか。
* 初回のパッケージ調達が一段落したら、上記の自動化に備えて :file:`reqconda.txt`
  と :file:`reqpip.txt` を作成しておくとよい。アップグレード目的のため、バージョ
  ン文字列はカットしたい。こうだろうか。

  .. code:: console

     bash$ conda list --export --no-pip | cut -d= -f1 > reqconda.txt
     bash$ conda list | grep '<pip>' | cut -f1 -d' ' > reqpip.txt

* Conda を利用することの（私にとっての）利点は、どのパッケージでもインストールと
  アップグレードの方法が統一化できるということだ。当ノートではいろいろな Python
  パッケージについての考察があるが、それらのどれにも書くハメになっていた、インス
  トールおよびアップグレードの云々をする必要がなくなったのも大きい。
* 一般のサードパーティー製 Python パッケージのインストール手順は次の図のようにす
  ることにした。ここではローカルにあるソースコードを :command:`pip install -e`
  でインストールする状況は考慮していない。

  .. _python-pkg-proc:

  .. figure:: /_images/python-pkg-proc.png
     :figwidth: image
     :scale: 100%

     一般のサードパーティー製 Python パッケージのインストール手順

3.5 から 3.6 への移行手順ノート
======================================================================

この節では ``root`` として Python 3.5 系の環境を構築してあるところに、そのバック
アップ環境を残しながらも Python 3.6 系の環境を構築するときの手順の一例を記す。基
本方針を列挙すると次のようになる：

* 旧 ``root`` 環境を ``3.5`` という名前の環境にバックアップする。
* 旧 ``root`` 環境にあるサードパーティー製パッケージを可能な限り新 ``root`` 環境
  にも導入する。
* 新 ``root`` 環境は Python 3.6 で動作するものとする。

バックアップ
----------------------------------------------------------------------

現在の ``root`` 環境とそっくり同じものを ``3.5`` として作成し、管理されている
パッケージ群を専用コマンドでテキストファイルに出力する。

.. code:: console

   bash$ conda create -n 3.5
   bash$ conda env export -n 3.5 > 3.5.yml

新 ``root`` 環境を構築
----------------------------------------------------------------------

まずは ``root`` 環境の Python を 3.6 にアップグレードする。これには ``update``
コマンドではなく ``install`` を用いる必要がある：

.. code:: console

   bash$ conda install python=3.6
   Fetching package metadata ...........
   Solving package specifications: .

   UnsatisfiableError: The following specifications were found to be in conflict:
     - nbpresent -> _nb_ext_conf -> nb_anacondacloud -> python 2.7*
     - python 3.6*
   Use "conda info <package>" to see the dependencies for each package.

すると上記のようなエラーが発生した。これは人によっては異なるだろう。いったん指摘
されたパッケージを取り除いて、後で再インストールを試みるという作戦でいきたい：

.. code:: console

   bash$ conda uninstall nbpresent
   Fetching package metadata ...........
   Solving package specifications: .

   Package plan for package removal in environment D:\Miniconda3:

   The following packages will be REMOVED:

       _nb_ext_conf:     0.3.0-py35_0
       nb_anacondacloud: 1.2.0-py35_0
       nb_conda:         2.0.0-py35_0
       nb_conda_kernels: 2.0.0-py35_0
       nbpresent:        3.0.2-py35_0

   Proceed ([y]/n)?

再度 ``install`` コマンドを試す：

.. code:: console

   bash$ conda install python=3.6
   Fetching package metadata ...........
   Solving package specifications: .

   Package plan for installation in environment D:\Miniconda3\:

   The following packages will be UPDATED:

       anaconda-client:     1.6.2-py35_0        --> 1.6.2-py36_0
       astroid:             1.4.9-py35_0        --> 1.4.9-py36_0
       bleach:              1.5.0-py35_0        --> 1.5.0-py36_0
       cffi:                1.9.1-py35_0        --> 1.9.1-py36_0
       clyent:              1.2.2-py35_0        --> 1.2.2-py36_0
       colorama:            0.3.7-py35_0        --> 0.3.7-py36_0
       cryptography:        1.7.1-py35_0        --> 1.7.1-py36_0
       cycler:              0.10.0-py35_0       --> 0.10.0-py36_0
       decorator:           4.0.11-py35_0       --> 4.0.11-py36_0
       entrypoints:         0.2.2-py35_1        --> 0.2.2-py36_1
       html5lib:            0.999-py35_0        --> 0.999-py36_0
       idna:                2.2-py35_0          --> 2.2-py36_0
       ipykernel:           4.5.2-py35_0        --> 4.5.2-py36_0
       ipython:             5.3.0-py35_0        --> 5.3.0-py36_0
       ipython_genutils:    0.1.0-py35_0        --> 0.1.0-py36_0
       ipywidgets:          6.0.0-py35_0        --> 6.0.0-py36_0
       isort:               4.2.5-py35_0        --> 4.2.5-py36_0
       jinja2:              2.9.5-py35_0        --> 2.9.5-py36_0
       jsonschema:          2.5.1-py35_0        --> 2.5.1-py36_0
       jupyter:             1.0.0-py35_3        --> 1.0.0-py36_3
       jupyter_client:      5.0.0-py35_0        --> 5.0.0-py36_0
       jupyter_console:     5.1.0-py35_0        --> 5.1.0-py36_0
       jupyter_core:        4.3.0-py35_0        --> 4.3.0-py36_0
       lazy-object-proxy:   1.2.2-py35_0        --> 1.2.2-py36_0
       markupsafe:          0.23-py35_2         --> 0.23-py36_2
       matplotlib:          2.0.0-np112py35_0   --> 2.0.0-np112py36_0
       menuinst:            1.4.4-py35_0        --> 1.4.4-py36_0
       mistune:             0.7.4-py35_0        --> 0.7.4-py36_0
       nbconvert:           5.1.1-py35_0        --> 5.1.1-py36_0
       nbformat:            4.3.0-py35_0        --> 4.3.0-py36_0
       networkx:            1.11-py35_0         --> 1.11-py36_0
       nose:                1.3.7-py35_1        --> 1.3.7-py36_1
       notebook:            4.4.1-py35_0        --> 4.4.1-py36_0
       numpy:               1.12.0-py35_0       --> 1.12.0-py36_0
       olefile:             0.44-py35_0         --> 0.44-py36_0
       pandocfilters:       1.4.1-py35_0        --> 1.4.1-py36_0
       path.py:             10.1-py35_0         --> 10.1-py36_0
       pickleshare:         0.7.4-py35_0        --> 0.7.4-py36_0
       pillow:              4.0.0-py35_1        --> 4.0.0-py36_1
       pip:                 9.0.1-py35_1        --> 9.0.1-py36_1
       prompt_toolkit:      1.0.13-py35_0       --> 1.0.13-py36_0
       pyasn1:              0.2.3-py35_0        --> 0.2.3-py36_0
       pycosat:             0.6.1-py35_1        --> 0.6.1-py36_1
       pycparser:           2.17-py35_0         --> 2.17-py36_0
       pycrypto:            2.6.1-py35_5        --> 2.6.1-py36_5
       pygments:            2.2.0-py35_0        --> 2.2.0-py36_0
       pylint:              1.6.4-py35_1        --> 1.6.4-py36_1
       pyopengl:            3.1.1a1-np112py35_0 --> 3.1.1a1-np112py36_0
       pyopengl-accelerate: 3.1.1a1-np112py35_0 --> 3.1.1a1-np112py36_0
       pyopenssl:           16.2.0-py35_0       --> 16.2.0-py36_0
       pyparsing:           2.1.4-py35_0        --> 2.1.4-py36_0
       pyqt:                5.6.0-py35_2        --> 5.6.0-py36_2
       python:              3.5.3-0             --> 3.6.0-0
       python-dateutil:     2.6.0-py35_0        --> 2.6.0-py36_0
       pytz:                2016.10-py35_0      --> 2016.10-py36_0
       pywin32:             220-py35_2          --> 220-py36_2
       pyyaml:              3.12-py35_0         --> 3.12-py36_0
       pyzmq:               16.0.2-py35_0       --> 16.0.2-py36_0
       qtconsole:           4.2.1-py35_2        --> 4.2.1-py36_2
       requests:            2.13.0-py35_0       --> 2.13.0-py36_0
       ruamel_yaml:         0.11.14-py35_1      --> 0.11.14-py36_1
       scipy:               0.19.0-np112py35_0  --> 0.19.0-np112py36_0
       setuptools:          27.2.0-py35_1       --> 27.2.0-py36_1
       simplegeneric:       0.8.1-py35_1        --> 0.8.1-py36_1
       sip:                 4.18-py35_0         --> 4.18-py36_0
       six:                 1.10.0-py35_0       --> 1.10.0-py36_0
       testpath:            0.3-py35_0          --> 0.3-py36_0
       tornado:             4.4.2-py35_0        --> 4.4.2-py36_0
       traitlets:           4.3.2-py35_0        --> 4.3.2-py36_0
       wcwidth:             0.1.7-py35_0        --> 0.1.7-py36_0
       wheel:               0.29.0-py35_0       --> 0.29.0-py36_0
       widgetsnbextension:  2.0.0-py35_0        --> 2.0.0-py36_0
       win_unicode_console: 0.5-py35_0          --> 0.5-py36_0
       wrapt:               1.10.8-py35_0       --> 1.10.8-py36_0

   Proceed ([y]/n)?

この画面まで行けば問題はない。ここからは :program:`conda` が自動でパッケージを大
量にダウンロード、インストールしてくれる。まだ ``UnsatisfiableError`` が生じるよ
うならば、再度対象パッケージの ``remove`` を都度実行する。なお :program:`conda`
以外の方法で導入したパッケージは別途インストールすること。

補足
----------------------------------------------------------------------

``UnsatisfiableError`` を引き起こしたパッケージを改めてインストールしたい場合に
注意が要る。:command:`conda install` の予告リストのパッケージバージョンが 3.6 に
一致するか指差し確認したい。

せっかく作った 3.6 環境に 3.5 のパッケージをインストールすると、それ以外のパッ
ケージも 3.5 のものにダウングレードしてしまうようだ。そのことについては
:program:`conda` は警告しない。

欲しいパッケージの 3.6 版がない場合は、それ以上の作業は見送るのがよい。

V4.7.5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* これまで ``root`` と書いたものは ``base`` と呼ばれるように変更されたらしい。
* どうやら :command:`conda update` 系のコマンド実行に OS の管理者権限が必要と
  なったらしい。通常権限のコンソールで更新系のコマンドを実行すると、最後に例外が
  発生して正しくファイルが配置されない。これは Windows のスタートメニュー
  :menuselection:`Anaconda Prompt` を右クリックして :guilabel:`管理者として実行`
  してから更新コマンドを実行することで免れる。以下に一例を示す：

  .. code:: console

     bash$ conda --version
     conda 4.7.5
     bash$ conda update --all --yes
     Collecting package metadata (current_repodata.json): done
     Solving environment: done
     ...
     Downloading and Extracting Packages
     ...
     Preparing transaction: done
     Verifying transaction: failed

     EnvironmentNotWritableError: The current user does not have write permissions to the target environment.
       environment location: D:\Miniconda3

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
