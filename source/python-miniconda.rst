======================================================================
Miniconda 利用ノート
======================================================================
Miniconda_ の利用に関する事実関係の覚え書きと、
その利用について思うところを記す。

.. contents:: ノート目次

.. note::

   本稿執筆時の動作環境は次のとおり。

   * OS: Windows 10 Home (64 bit)
   * Cygwin: 2.5.2-1, 2.7.0 (64 bit)
   * bash: 4.3.42(4)-release, 4.4.12(3)-release (x86_64-unknown-cygwin)
   * Miniconda_: 4.0.5, 4.1.11, 4.3.14

   Python 本体および Python 製パッケージのバージョンについては、
   必要に応じて本文で明記していく。

概要
======================================================================
まずは Conda が何であるかを説明する。
Conda とは、オープンソースパッケージの管理システムであり、
それらに対する環境管理システムである。
すなわち、

* パッケージの複数のバージョンおよびそれらの間の依存関係をインストールしたり、
* それら（環境と呼ぶ）を容易に切り替えたり

する機能がある。
Conda は Python プログラムについて製作されたものだったということだが、
現在ではどのようなソフトウェアでもパッケージにしたり配布したりすることが可能であるそうだ。

次に Conda を含むシステムとして Anaconda_ と Miniconda_ が存在することを一応述べる。
本稿では後者のシステムのみを解説していく。
Anaconda が既定の状態でかなりのパッケージを自動的にインストールするのに対し、
Miniconda は Conda, Python および依存パッケージしか含まない。
ドキュメントをすべて読んだわけではないが、
両者の決定的な違いはこれだけではないかと思う。

最後に Conda を表現するコマンドラインツール :program:`conda` について簡単に述べる。
Conda の機能の一つである :code:`conda install` コマンドを使えば、
720 を超える科学計算パッケージを Continuum リポジトリーというところから
個別にインストールすることが可能であり、
さらに 250 を超える科学計算パッケージを個別にインストールすることが可能だ。
その他、:program:`conda` にはリポジトリーに所望のパッケージが存在するかを
問い合わせたり検索したりする機能や、
当然ながらインストール済みのパッケージの一覧表示、更新、削除といった機能がある。
先に述べた環境切り替えについては、付録のシェルスクリプトまたはバッチファイルにて
実現することが可能。

補足として、通常の Python 環境と同様に :code:`pip install` を併用することも可能であることを
記し添えておく。
:doc:`/python-pip` も参照。

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

Miniconda_ のダウンロードページにある Python 3.5 の 64-bit (exe installer) をクリックして
:file:`Miniconda3-latest-Windows-x86_64.exe` というファイル名のインストーラーを入手できる。

次にダウンロードしたインストーラーを実行する。
選択肢はほとんどなく、せいぜいインストールパスを好みで変更するくらいで、
手なりでインストールを終了する。
以下、インストールパスを :file:`D:\\Miniconda3` としたものとする。

そして公式ドキュメントの `30-minute test drive <http://conda.pydata.org/miniconda.html>`_ を実施するのがよい。
各種基本コマンドを習得するはずだ。
この過程で Python 本体と :program:`conda` 自身のアップグレードも場合によっては生じる。

さて、メインの作業である個々のパッケージのインストールおよびアップグレードだが、
状況に応じて手動による作業の内容が変わってくることが考えられる。
ここでは対象パッケージについて次の条件を仮定しておく。

* Python プログラミングの個人研究用という名目の環境を構築したい。
  暗に旧バージョンのパッケージの動作確認等は興味の対象外と言いたい。

* :program:`conda` でも :program:`pip` でも取得することになるパッケージのバージョンが同じであれば、
  :program:`conda` のほうを優先する。
  さもなくば、より新しいバージョンを取得する手法のほうを優先する。
  たいていの場合それは :program:`pip` のほうだ。

* ローカルディスク上にある自作のパッケージは :program:`pip` で管理する。
  この場合は常に ``--edit`` コマンドラインフラグを指定する。

パッケージ P を :code:`conda install` によってインストールする場合、
P が正常に動作するかどうかを確認する作業をする。
作業方法は P に依存して変化するわけだが、それについては読書ノート内の各パートを参照する。
インストールするパッケージ群に依存関係が存在することがよくあるが、
その場合の動作確認の順番は、依存ツリーの根から葉の方向に進める。
また、この作業に先立って従来環境における :file:`site-packages` の状況を
従来環境にあるほうのコマンド :code:`pip freeze` 等を活用して把握しておくことだ。
必要なパッケージを

#. :code:`pip install` によって得られたものと、
#. 非公式版アーカイブからのインストールで得られたもの

とに分類しておき、整理結果を
後の :code:`conda install` と :code:`pip install` の使い分けの基準とする。

Conda の各種設定はホームディレクトリーに所定の書式で記述された
構成ファイル :file:`.condarc` を作成することでも可能である。
毎度特定のコマンドラインオプションを指定するようなことがあれば、
このテキストファイルにそのようなオプションを記述しておけば、
コマンドラインの入力作業の省力化になる。

デフォルト環境用の次回以降のアップグレードに備えて
:code:`pip list --export` コマンドで要件文字列をファイル化しておくとよい。
これについては次節で述べる。

ノート
======================================================================
* Anaconda ではなく Miniconda を選択した理由は、
  必要十分なパッケージを利用可能にしたいからという、
  個人的な嗜好による。

* Python の利用者が Conda が何であるかを理解するには、
  `conda vs. pip vs. virtualenv <http://conda.pydata.org/docs/_downloads/conda-pip-virtualenv-translator.html>`_
  の表を見るのが手っ取り早い。

  * 要するに :program:`pip` + :program:`virtualenv` である。

* Miniconda のインストーラーは正規版の Python のそれとは異なるのか、
  Windows のスタートメニューを変更しないのだろうか。
  HTML Help ファイルの Python 3.5.x Documentation へのショートカットアイコンが
  スタートメニューにあるプログラムリストに欲しい。

* 私はパッケージ環境切り替え機能を利用することはほぼないはずだ。
  Python のサードパーティー製パッケージおよび Python 自身を
  効率的に更新する道具として Miniconda を利用していくだろう。

* チュートリアルの 30-minute test drive は無難な作業ばかりなので、
  これは問題になり得ないはずだった。
  ところが、私が Cygwin の bash でコマンドライン操作のすべてを行うのだが、
  それに関係して一点だけ問題があった。
  :file:`activate` スクリプトによる
  環境を切り替える処理が失敗していることになかなか気付かなかったことだ。

  例えば :file:`activate` スクリプトの処理の本質は
  「環境変数 ``PATH`` に対して、対応する Python 関係のパスを先頭のほうに追加する」ことだ。
  :file:`deactivate` スクリプトはこれと反対のことを行う。
  今、スクリプトと書いたが、実際には bash の組み込み関数 ``source`` で実施するものだ。

  このスクリプトは
  :file:`/d/Miniconda3/envs/myenv` のようなパスを環境変数 ``PATH`` の先頭付近に「追加」する。
  ところが私の Cygwin 環境では未だに ``/cygdrive`` prefix が生きていたので、
  全然意味を成さない。
  Cygwin の :file:`/etc/fstab` あるいは :file:`/etc/fstab.d/$USER` の内容を
  次のように編集する必要が生じていた。

  .. code-block:: text

     # For a description of the file format, see the Users Guide
     # http://cygwin.com/cygwin-ug-net/using.html#mount-table

     # This is default anyway:
     #none /cygdrive cygdrive binary,posix=0,user,noacl 0 0

     # Remove /cygdrive/ prefix:
     none / cygdrive          binary,posix=0,user,noacl 0 0

  この編集作業は本件がなかったとしても、厄介な cygdrive 問題の解決は
  もっと昔に実施してしかるべきだった。反省。

* 非 Miniconda ベースの Python 環境で築いてきた :file:`site-packages` 下を
  Miniconda において再現するとなると、
  正規環境のそれにおける作業時間よりも長くなるのかもしれない。
  Matplotlib_ のインストールを実施したところ、
  何やら依存パッケージのインストールが絡んできて、
  そのコストが某サイトの非公式 Wheel を用いたインストールよりも明らかに高く付いた。

  * なお、完全移行達成までは元の正規 Python 環境を解体せぬことだ。
    環境変数 ``PATH`` の単純な書き換えでいつでも新旧 Python 間の切り替えが可能だ。
    動作の比較も容易い。
    元の環境を放棄する必要性は一般にはない。
    私にとっては本物は一つでいいので捨てる。

  * 元の Python 環境での :code:`pip freeze` の出力結果を控えておくこと。
    :doc:`/python-pip` 参照。

* :program:`conda` のコマンドライン操作の設計が
  ドキュメントに頼る必要がないほど質素であるため、
  当ノートでは「呪文表」を作成しない。
  いつでも :code:`conda --help` なり
  :code:`conda command --help` の出力メッセージで事足りる。

* Conda の ``install`` コマンドによる Matplotlib_ を用いて、
  バックエンドを既定の ``TkAgg`` にしたときのウィンドウの表示時に
  Segmentation fault が発生する不具合が私の環境で現在発生している。
  この不具合のために、元の Python 環境を削除するのを躊躇している。

  * 応急処置としてはバックエンドを ``Qt4Agg`` にセットすることだ。
    これにより :code:`plt.show()` などの呼び出しで落ちることはなくなる。
    設定方法については :doc:`/python-matplotlib/basic` および
    :doc:`/python-matplotlib/config` を参照。

  * 仮に :code:`conda install matplotlib` ではなく、
    いつもの非公式バイナリーを :code:`pip install` したら
    おそらく動作すると思われる。
    そのためには先に別途非公式版をダウンロードしておく必要があるのだが、
    何のために Miniconda を導入したのかわからなくなる。

* :program:`conda` の設定ファイル :file:`.condarc` は今のところ用意しないで済みそうだ。
  各コマンドのオプション引数についての既定値が優秀であるところが大きい。

* パッケージ P について、
  :code:`conda install P` してから :code:`pip install P` することが可能であることがある。
  可能な場合には、これらが同一環境下に共存する。

  * 環境にある全パッケージを単にアップグレードするには、次のコマンドでよい。

    .. code-block:: console

       $ conda update --all

  * 困ったことに :program:`pip` によってインストールしたパッケージのバージョンが
    :program:`conda` のものより新しい傾向がある。
    例えば上記コマンドの実行直後に :code:`pip list -o` すると、
    なおパッケージ名が列記されることがある。
    このようなパッケージは :program:`conda` での管理とは別に「手動で」管理するハメになる。
    インストールもアップグレードもなるべく :program:`conda` で統一したいのだが。

  * 一括アップグレードを実現する場合、このことが重要である。
    つまり、次のような手順を採用することになるだろう。

    .. code-block:: console

       $ conda update --all
       $ pip install --upgrade --requirement reqpip.txt

    ここで、パッケージ一覧ファイル :file:`reqpip.txt` は
    あらかじめ用意する必要があるものである。

  * パッケージ間の依存関係とインストール時に用いたツールの違いが
    問題になることはあるだろうか。

* 初回のパッケージ調達が一段落したら、上記の自動化に備えて
  :file:`reqconda.txt` と :file:`reqpip.txt` を作成しておくとよい。
  アップグレード目的のため、バージョン文字列はカットしたい。
  こうだろうか。

  .. code-block:: console

     $ conda list --export --no-pip | cut -d= -f1 > reqconda.txt
     $ conda list | grep '<pip>' | cut -f1 -d' ' > reqpip.txt

* Conda を利用することの（私にとっての）利点は、
  どのパッケージでもインストールとアップグレードの方法が統一化できるということだ。
  当ノートではいろいろな Python パッケージについての考察があるが、
  それらのどれにも書くハメになっていた、
  インストールおよびアップグレードの云々をする必要がなくなったのも大きい。

* 一般のサードパーティー製 Python パッケージのインストール手順は
  次の図のようにすることにした。
  ここではローカルにあるソースコードを :code:`pip install -e` でインストールする状況は
  考慮していない。

  .. _python-pkg-proc:

  .. figure:: /_images/python-pkg-proc.png
     :width: 657px
     :height: 407px
     :scale: 100%

     一般のサードパーティー製 Python パッケージのインストール手順

3.5 から 3.6 への移行手順ノート
======================================================================
この節では ``root`` として Python 3.5 系の環境を構築してあるところに、
そのバックアップ環境を残しながらも Python 3.6 系の環境を構築するときの手順の一例を記す。
基本方針を列挙すると次のようになる：

* 旧 ``root`` 環境を ``3.5`` という名前の環境にバックアップする。
* 旧 ``root`` 環境にあるサードパーティー製パッケージを可能な限り新 ``root`` 環境にも導入する。
* 新 ``root`` 環境は Python 3.6 で動作するものとする。

バックアップ
----------------------------------------------------------------------
現在の ``root`` 環境とそっくり同じものを ``3.5`` として作成し、
管理されているパッケージ群を専用コマンドでテキストファイルに出力する。

.. code:: console

   $ conda create -n 3.5
   $ conda env export -n 3.5 > 3.5.yml

新 ``root`` 環境を構築
----------------------------------------------------------------------
まずは ``root`` 環境の Python を 3.6 にアップグレードする。
これには ``update`` コマンドではなく ``install`` を用いる必要がある：

.. code:: console

   $ conda install python=3.6
   Fetching package metadata ...........
   Solving package specifications: .


   UnsatisfiableError: The following specifications were found to be in conflict:
     - nbpresent -> _nb_ext_conf -> nb_anacondacloud -> python 2.7*
     - python 3.6*
   Use "conda info <package>" to see the dependencies for each package.

すると上記のようなエラーが発生した。これは人によっては異なるだろう。
いったん指摘されたパッケージを取り除いて、後で再インストールを試みるという作戦でいきたい：

.. code:: console

   $ conda uninstall nbpresent
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

   $ conda install python=3.6
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

この画面まで行けば問題はない。
ここからは :program:`conda` が自動でパッケージを大量にダウンロード、インストールしてくれる。
まだ ``UnsatisfiableError`` が生じるようならば、再度対象パッケージの ``remove`` を都度実行する。
なお :program:`conda` 以外の方法で導入したパッケージは別途インストールすること。

補足
----------------------------------------------------------------------
``UnsatisfiableError`` を引き起こしたパッケージを改めてインストールしたい場合に注意が要る。
:code:`conda install` の予告リストのパッケージバージョンが 3.6 に一致するか指差し確認したい。

せっかく作った 3.6 環境に 3.5 のパッケージをインストールすると、
それ以外のパッケージも 3.5 のものにダウングレードしてしまうようだ。
そのことについては :program:`conda` は警告しない。

欲しいパッケージの 3.6 版がない場合は、それ以上の作業は見送るのがよい。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
