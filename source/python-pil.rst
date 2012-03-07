======================================================================
Python PIL 利用ノート
======================================================================

.. note::

   * 体系的にまとめるまでの間は Q & A 形式でノートしておく。
   * 本稿において、利用した各パッケージのバージョンは次のとおり。

     * Python_: 2.6.6
     * PIL_: 1.1.6, 1.1.7 (both official and unofficial builds)

.. contents:: ノート目次

PIL 自身
==================================================

PIL のサイトはどこ？
--------------------------------------------------
PIL_ のサイトは http://www.pythonware.com/products/pil にある。

パッケージ入手方法とインストール方法は？
--------------------------------------------------
いつもならばインターネットに接続した環境で ``easy_install PIL`` するが、
本パッケージに関しては避けたほうが無難そうだ。

Windows 用には PIL の製品サイトがインストーラーを提供しているかもしれない。
しかし 少なくとも win32-py2.6 に関しては、
下記の非公式サイトで配布されているインストーラーを利用するほうがよいようだ。

* `Python Extension Packages for Windows - Christoph Gohlke`_

オフラインドキュメントはある？
--------------------------------------------------
手許に Python Imaging Library Overview というタイトルの PDF ファイルが存在する。
入手場所は忘れたが、おそらく上記サイトのはず。

ファイル名は :file:`pil-handbook.pdf` で、
Fredrik Lundh と Matthew Ellis という人物の共著になっている。

また、配布ソースコード一式からビルドできる HTML ドキュメント
"The Python Imaging Library" も極めて有用。

画像処理基本
==================================================

既存の画像ファイルのフォーマット変換の方法は？
--------------------------------------------------
``Image.save`` するときのファイル名の拡張子で PIL が勝手に変換してくれる。
GIF ファイル :file:`image.gif` を PNG に変換するには、例えば下のようにする。

>>> import Image
>>> im = Image.open("image.gif")
>>> im.save("image.png")

「特定のフォルダーにあるすべての GIF ファイルを PNG に変換する」のような作業は、こうする。

.. code-block:: python

   # pil-handbook の例を一部改変。動作未確認。
   import os.path
   import glob
   import Image

   for infile in glob.glob("*.gif"):
       file, ext = os.path.splitext(infile)
       im = Image.open(infile)
       im.save(file + ".png")

コードを書きたくないならば、コマンドラインから
:file:`pilconvert.py` を使う手もある（後述）。

加工した画像を目視で確認するのが面倒だ？
--------------------------------------------------
画像処理後の適当なタイミングで、メソッド ``show`` を最後に呼び出してみよう。
PIL が画像ビューワーを起動して、そこで処理画像を見せてくれる。

画像をいじっていたらジャギーが出て困るのだが？
--------------------------------------------------
関数によっては ``Image.ANTIALIAS`` を引数に指定すると具合がよくなるものもある。
特に、イメージを縮小してジャギーが生じる場合は、プログラム中の
``resize`` と ``thumbnail`` の実引数をチェックする。

イメージをモノクロにするには？
--------------------------------------------------
メソッド ``convert`` を使って L モードにするだけで OK のようだ。
内部的に各ピクセルの RGB 値をグレースケール化しているようだ。
次の式でスケールが決まる。

.. code-block:: text

   L = R * 299/1000 + G * 587/1000 + B * 114/1000

.. image:: /_static/illvelo.png
   :scale: 50%
.. image:: /_static/illvelo-monochrome.png
   :scale: 50%

画像ファイルがない状態からイメージを生成するには？
--------------------------------------------------
関数 ``Image.new`` を利用する。少なくともカラーモードと画像サイズを指定すればよい。

>>> # 1024 x 768 の RGB イメージを初期化する。
>>> import Image
>>> img = Image.new('RGB', (1024, 768))

このオブジェクトは、いわばまっさらなキャンヴァスだ。
ここに他のイメージオブジェクトを ``paste`` メソッド等を利用して描く。

色を指定するのに RGB 値直接指定はつらい
--------------------------------------------------
PIL の関数・メソッドで色を引数に取るものについては、
``ImageColor`` モジュールで決められている色名で指定することもできるようだ。
RGB, RGBA モードでこのやり方が認められている。

>>> # RGB イメージを赤色で初期化する。
>>> import Image
>>> img = Image.new('RGB', (1024, 768), 'red')

辞書 ``ImageColor.colormap`` のキーとなっている文字列ならば OK らしい。

より一般的には HTML/CSS 風に ``'#ff0000'`` と指示する方式もある。
これなら任意の 24 ビットカラー値を与えられる。

パレットモードについて詳しく
--------------------------------------------------
TBW

某ロムイメージからのイメージリッピングの際にこの知識が必要になるだろう。

Band の考え方について教えてくれ
--------------------------------------------------
例えば、手許にある PNG ファイルから読み込んだイメージデータは RGBA モードだ。
これは R, G, B, A という色プラスアルファに関する情報を持っている。
このようなものを PIL では multi-band であると表現する。

イメージオブジェクトの ``split`` メソッドでこの band を
L モードのイメージとして抽出できる。

.. code-block:: python

   # RGBA なイメージだと仮定する。
   img = Image.open('illvelo.png')
   assert img.mode == 'RGBA'

   # split メソッドで R, G, B, A 各成分をイメージの形で抽出する。
   img.load()
   bands = img.split()
   #bands[0].show() # R 成分のグレースケールが拝める。

アルファチャンネルを持つ PNG 画像を青地背景上に重ねたい
-----------------------------------------------------------
PIL では Photoshop で言うところのチャンネルのことをバンドと呼んでいる。
両者の意味は同じと考えてよさそうだ。

``paste`` メソッドの ``mask`` 引数として、対象となる画像のアルファを与えるのが正解。
アルファは元イメージに対する ``split`` メソッドの戻り値から得る。

.. code-block:: python

   import Image
   
   # Photoshop で言うところのレイヤー 1 に置く画像。
   img = Image.open('illvelo.png')
   img.load()
   bands = img.split()

   # R, G, B, A の A だけが要る。
   alpha = bands[3]
   
   # Photoshop で言うところの背景レイヤーになる画像。
   bkgnd = Image.new('RGBA', img.size, 'blue')
   
   # これではダメ。
   #bkgnd.paste(img, None)
   # これが正解。
   bkgnd.paste(img, None, mask=alpha)

.. image:: /_static/illvelo.png
   :scale: 50%
.. image:: /_static/illvelo-blueback.png
   :scale: 50%

テキスト関連
==================================================

テキストを描画する一番簡単なコードは？
--------------------------------------------------
とりあえず ``ImageDraw`` モジュールの機能を利用する。

.. code-block:: python

   import Image
   import ImageDraw

   # デフォルト背景色の 128x128 サイズのキャンヴァスを用意する。
   img = Image.new('RGBA', (128, 128))

   # Draw 関数でオブジェクトを作成。
   draw = ImageDraw.Draw(img)

   # 画面の左上隅にテキストを赤く描画する。
   draw.text((0, 0), u'Hello, world', fill='red')

日本語のテキストを描画するには？
--------------------------------------------------
コツは 3 つある。

* 関数 ``ImageFont.truetype`` で日本語対応のフォントオブジェクトを作成する。
* その際に ``encoding`` 引数に適切なエンコーディングを指示する。
* ``text`` メソッドの引数にそのフォントを与える。

.. code-block:: python

   import Image
   import ImageDraw
   import ImageFont

   # 大きめのキャンヴァスを用意しておく。
   img = Image.new('RGB', (1024, 256), 'black')
   dr = ImageDraw.Draw(img)
   # HG 明朝体を使ってみる。
   fnt = ImageFont.truetype('hgrme.ttc', 24, encoding='utf-8')

   # 長めのテキストを用意する。
   text = u'''どうしても会ってもらえませんか？
   私はこんなにあなたに会いたいのに…。
   お金には余裕があるので心配しないで
   ください。
   コード780の1102番で、
   あなたを待っています。
   '''
   
   width = 0
   height = 0
   for line in text.splitlines():
       ext = dr.textsize(line, fnt)
       dr.text((0, height), line, font=fnt, fill='white')
       width = max(ext[0], width)
       height += ext[1]
   
   # 余白をトリムする。
   img = img.crop((0, 0, width, height))

.. image:: /_static/karous-paradise.png

ImportError: DLL load failed になるのはなぜ？
--------------------------------------------------
* 事実関係

  * 前項のコード実行時に ``import ImageFont`` で表題のエラーが出た。
    エラーメッセージを真に受けると :file:`_imagingft.pyd` が何らかの理由でおかしい。
  * 調べてみると PIL 1.1.7 だけで起こる現象のようだ。

* コメント

  * このファイルは Windows 用の PIL 「公式」インストーラーに含まれているのだが、
    ビルドしたときに何かの外部ライブラリーの参照をしていなかったのではないだろうか。

  * 対策方法をふたつ見つけた。
    まずは PIL 1.1.7 をアンインストールする。そして、

    * 1.1.7 をアンインストールして、公式サイト配布の 1.1.6 に戻すか、

    * `Python Extension Packages for Windows - Christoph Gohlke`_
      で入手できる PIL 1.1.7 の非公式インストーラーを利用するか。

いつか役に立つかもしれない諸機能
==================================================

スクリーンショット
--------------------------------------------------
Windows のみ対応らしい。

.. code-block:: python

   import Image
   import ImageGrab
   
   # スクリーンショットをキャプチャー。
   img = ImageGrab.grab()

   # そのままだと面白くないので、
   # 縮小して表示する。
   img.thumbnail((256, 256), Image.ANTIALIAS)
   #img.show()

.. image:: /_static/grab.png
   :scale: 100%

上下左右ループ壁紙パターン作成
--------------------------------------------------
よくあるアルゴリズムを PIL で実装すればよい。

* 元画像を 2 x 2 分割して対角線上の区域を入れ替える。
* そこへ元画像をブレンドなりオーバーレイなりして重ね合わせる。

左右方向ループのための区域入れ替えの処理は、pil-handbook 参照。

.. code-block:: python

   # Example: Rolling an image を改造
   def roll_horz(image, delta):
       xsize, ysize = image.size

       delta = delta % xsize
       if delta == 0: return image

       part1 = image.crop((0, 0, delta, ysize))
       part2 = image.crop((delta, 0, xsize, ysize))
       image.paste(part2, (0, 0, xsize-delta, ysize))
       image.paste(part1, (xsize-delta, 0, xsize, ysize))
       return image

.. image:: /_static/illvelo.png
   :scale: 50%
.. image:: /_static/illvelo-wallpaper.png
   :scale: 50%

モジュール ImageDraw2 が気になる
--------------------------------------------------
:file:`ImageDraw2.py` なるものがある。
中身を覗いたら、けっこうすっきりしていていい感じだ。

モジュール ImageGL の使い方がわからない
--------------------------------------------------
名前からして OpenGL 関係なのだが、コードを見ても用途不明。

モジュール ImagePath の使い方がわからない
--------------------------------------------------
コードを見ても用途不明。

コマンドラインユーティリティー
==================================================
PIL をインストールすると :file:`Scripts` フォルダーに何個かスクリプトが入る。
以降の例コードは、Cygwin (Bash) での入力を想定している。
Python 自体は Cygwin のものではなく、Windows 用のものを利用する。
Cygwin 版の Python はそもそもインストールしていない。

フォーマット変換を行うには？
--------------------------------------------------
コマンドラインで :file:`pilconvert.py` を利用する。
ImageMagick の ``convert`` から画像操作オプションを全部取り去ったようなツールだ。

``sample.gif`` から PNG 形式のファイル ``sample.png`` を作成するには次のように入力するだけだ。

.. code-block:: console

   $ pilconvert.py sample.gif sample.png

カレントディレクトリーのすべての GIF ファイルから PNG ファイルに変換したいならばこうなる。

.. code-block:: console

   $ for name in *.gif ; do \
   >   pilconvert.py $name ${name%.*}.png ; \
   > done

画像リサイズ等の操作を行うには？
--------------------------------------------------
コマンドラインで :file:`pildriver.py` を利用する。
ImageMagick の ``convert`` とよく似たツールだ。

ただし、コマンドラインで最初にすべての操作を指定して実行するケースと、
引数を与えずに実行して対話モードに入り、そこで操作を順次指示するケースがある。
対話モードでは操作の途中で ``show`` コマンドで途中経過を確認できる。

.. code-block:: console

   $ pildriver.py
   PILDriver says hello.
   pildriver> open illvelo.png
   [<PIL.PngImagePlugin.PngImageFile image mode=RGBA size=256x252 at 0xBEF800>]
   pildriver> thumbnail 64 64
   [<PIL.PngImagePlugin.PngImageFile image mode=RGBA size=64x63 at 0xBEF800>]
   pildriver> show
   []
   pildriver>

対話モードから抜けるコマンドがあるわけではないようなので、
``Ctrl-C`` で終了してしまおう。

関連リンク
==================================================
* PIL_: Python Imaging Library (PIL) 公式ウェブサイト。
* `Python Extension Packages for Windows - Christoph Gohlke`_: 非公式インストーラー配布ページ。

.. _Python: http://www.python.org/
.. _PIL: http://www.pythonware.com/products/pil
.. _Python Extension Packages for Windows - Christoph Gohlke: http://www.lfd.uci.edu/~gohlke/pythonlibs/
