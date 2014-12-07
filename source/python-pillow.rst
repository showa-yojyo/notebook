======================================================================
Pillow 利用ノート
======================================================================

Python で画像処理といえば、長い間 PIL_ が活躍していた。
だがここ最近は Pillow_ というフォークパッケージが主流になっているらしい。
とある別の作図パッケージのアップグレードの際に、
それが Pillow に依存していることに気付いて世代交代を知ったのだった。

そこで、本稿では Pillow の導入方法と、既存の PIL 利用コードの移行手順について記す。
なお、PyOpenGL や Pygame との連携で PIL を利用していた既存コードのそれについては、
各ノートにて言及していく（現在執筆中）。

.. contents:: ノート目次

.. note::

   * OS: Windows 7 Home Premium SP 1
   * 本稿において、利用した各パッケージのバージョンは次のとおり。

     * Python_: 3.4.1
     * Pillow_: 2.5.1

関連リンクおよび参考サイト
======================================================================
Pillow_
  公式パッケージ・インストーラー配布元。

`Python Extension Packages for Windows - Christoph Gohlke`_
  非公式インストーラー配布元。

インストール
======================================================================
筆者の場合は Windows 7 64 ビットなので、上記非公式インストーラーを利用する。
本稿執筆時は :file:`Pillow-2.5.1.win-amd64-py3.4.exe` を利用した。

それ以外の環境についてはいつもの ``pip install pillow`` で問題あるまい。

ちなみに PIL が既に環境に居座っている場合は、Pillow をインストールする前に
PIL をアンインストールする必要があるようだ。
公式サイトの Installation ページに PIL と Pillow が共存できない旨が明記されている。

ドキュメント
======================================================================
まずは Pillow_ 公式サイトの Guides を見たが、どうも PIL コードがそのまま使える雰囲気だ。
この後、昔のコードを引っ張りだして Pillow に与えて検証していこう。

画像処理基本
======================================================================
:doc:`python-pil` で試したコードがそのまま再利用できるかどうかを検証した。

画像ファイルフォーマット変換（単発）
----------------------------------------------------------------------
GIF 画像ファイル :file:`image.gif` を PNG 形式に変換して、ファイル :file:`image.png` として保存するコードを再掲する。

>>> import Image
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named 'Image'
>>> from PIL import Image
>>> im = Image.open("image.gif")
>>> im.save("image.png")

Pillow では ``from PIL import Image`` としてインポートする必要がある。他のモジュールも同様。

画像ファイルフォーマット変換（バッチ処理）
----------------------------------------------------------------------
カレントディレクトリー内の GIF ファイルを PNG ファイルに変換、保存する処理のコードはこうなる。

.. code-block:: python3

   import os.path
   import glob
   from PIL import Image

   for infile in glob.glob("*.gif"):
       file, ext = os.path.splitext(infile)
       im = Image.open(infile)
       im.save(file + ".png")

なんと :file:`pilconvert.py` を使う手も封じられていない。
Python の Scripts ディレクトリーに一連のスクリプト群がインストールされている。

簡易ビューワー
----------------------------------------------------------------------
PIL と同様にして、メソッド ``show`` を利用することができる。

>>> ...
>>> im = Image.open("image.gif")
>>> im.show()

筆者の環境では Windows のフォトビューワーが起動して、画像の内容が表示された。

ジャギー解消
----------------------------------------------------------------------
TBW

イメージモノクロ化
----------------------------------------------------------------------
:doc:`python-pil` ではコードを載せるのを忘れていた。
PIL 同様、メソッド ``convert`` を引数 ``"L"`` で呼び出す。

>>> ...
>>> im = Image.open("illvelo.png")
>>> im.convert("L").save("illvelo-monochrome.png")

元画像と処理後の画像は次のようになる。

.. image:: /_static/illvelo.png
   :scale: 50%
.. image:: /_static/illvelo-monochrome.png
   :scale: 50%

画像生成
----------------------------------------------------------------------
PIL 同様、メソッド ``Image.new`` を利用することができる。

>>> # 1024 x 768 の RGB イメージを初期化する。
>>> from PIL import Image
>>> img = Image.new('RGB', (1024, 768))

結果画像の掲載を割愛する。

色名指定
----------------------------------------------------------------------
PIL 同様、Pillow のメソッドで色を引数に取るものについては、
``ImageColor`` モジュールで決められている色名で指定することもできる。

>>> # RGB イメージを濃いピンクで初期化する。
>>> from PIL import Image
>>> img = Image.new('RGB', (1024, 768), 'deeppink')

色名は ``colormap`` という ``dict`` インスタンスに保持されている。
興味があれば列挙してみるとよい。

>>> from PIL import ImageColor
>>> for i in sorted(ImageColor.colormap.items()): print(i)
...
('aliceblue', '#f0f8ff')
('antiquewhite', '#faebd7')
('aqua', '#00ffff')
... 略 ...
('yellowgreen', '#9acd32')
>>>

結果画像の掲載を割愛する。

透過イメージ生成
----------------------------------------------------------------------
PIL 同様。4 つ目の 0 がアルファー値であり、上限値の 0xFF に近いほど透過度が低くなる。

>>> img = Image.new('RGBA', (1024, 768), (0, 0, 0, 0))

結果画像の掲載を割愛する。

アルファチャンネルを持つ PNG 画像を青地背景上に重ねたい
----------------------------------------------------------------------
PIL のときのコードをほぼそのまま再利用できる。

.. code-block:: python3

   from PIL import Image

   # Photoshop で言うところのレイヤー 1 に置く画像。
   img = Image.open('illvelo.png')
   bands = img.split()

   # R, G, B, A の A だけが要る。
   alpha = bands[3]

   # Photoshop で言うところの背景レイヤーになる画像。
   bkgnd = Image.new('RGBA', img.size, 'blue')

   # これではダメ。
   #bkgnd.paste(img, None)
   # これが正解。
   bkgnd.paste(img, None, mask=alpha)

元画像と処理後の画像はこうなる。

.. image:: /_static/illvelo.png
   :scale: 50%
.. image:: /_static/illvelo-blueback.png
   :scale: 50%

グラデーション
======================================================================

線形グラデーション（透過なし）
----------------------------------------------------------------------
幅 :math:`1 \times 256` ピクセルのイメージを作成し、ピクセルカラーをその位置に応じてセットしていく方針で絵を描く。
まずは ``putpixel`` メソッドを利用してこれを行い、それから目的のサイズにイメージを拡縮する。

次に示すコードは、サイズが :math:`320 \times 240` で、
上部が赤で下部が青の線形グラデーションとなるイメージを作成する。
線形補間の計算コード記述の手間を少々省くため、NumPy を利用した。

.. code-block:: python3

   from PIL import Image, ImageColor
   import numpy as np

   COLOR_START = ImageColor.getrgb('antiquewhite')
   COLOR_STOP = ImageColor.getrgb('deeppink')
   IMAGE_WIDTH, IMAGE_HEIGHT = 320, 240
   WORK_SIZE = 0x100
   R, G, B = 0, 1, 2

   img = Image.new('RGB', (1, WORK_SIZE))
   colors = np.dstack(
       (np.linspace(COLOR_START[i], COLOR_STOP[i], num=SIZE) for i in (R, G, B)))[0]

   for i, color in enumerate(colors):
       img.putpixel((0, i), tuple(color.astype(int).tolist()))

   img = img.resize((IMAGE_WIDTH, IMAGE_HEIGHT))
   #img.save('gradient1.png')

結果画像の掲載を割愛する。

線形グラデーション（単色にグレースケール透過）
----------------------------------------------------------------------
``putalpha`` 利用版グラデーション。

.. code-block:: python3

   from PIL import Image

   BASE_COLOR = 'red'
   IMAGE_WIDTH, IMAGE_HEIGHT = 320, 240
   WORK_SIZE = 0x100

   img = Image.new('RGBA', (IMAGE_WIDTH, IMAGE_HEIGHT), BASE_COLOR)
   gradient = Image.new('L', (1, WORK_SIZE))

   for i in range(WORK_SIZE):
       gradient.putpixel((0, WORK_SIZE - i), i)

   img.putalpha(gradient.resize(img.size))
   #img.save('gradient2.png')

出力は上部が赤で、下部に至るにつれて透過していく線形グラデーションイメージとなる。
結果画像の掲載を割愛する。

線形グラデーション（さらなる応用）
----------------------------------------------------------------------
イメージ 3 枚重ね。

.. code-block:: python3

   from PIL import Image, ImageColor

   WORK_SIZE = 0x100

   img = Image.open('illvelo.png')
   assert img.mode == 'RGBA'

   gradient = Image.new('L', (1, WORK_SIZE))
   for i in range(WORK_SIZE):
       gradient.putpixel((0, i), i)

   alpha = gradient.resize(img.size, Image.ANTIALIAS)

   final = Image.new('RGBA', img.size, (0, 0, 0, 0))
   final.paste(img, None, mask=alpha)
   #final.save('illvelo-gradient.png')

元画像と処理後の画像はこうなる。

.. image:: /_static/illvelo.png
   :scale: 50%
.. image:: /_static/illvelo-gradient.png
   :scale: 50%

テキスト
======================================================================

Hello, world
----------------------------------------------------------------------

.. code-block:: python3

   from PIL import Image, ImageDraw

   IMAGE_WIDTH, IMAGE_HEIGHT = 320, 240
   TEXT_COLOR = 'red'

   # デフォルト背景色のキャンヴァスを用意する。
   img = Image.new('RGBA', (IMAGE_WIDTH, IMAGE_HEIGHT))

   # Draw 関数でオブジェクトを作成。
   draw = ImageDraw.Draw(img)

   # 画面の左上隅にテキストを描画する。
   draw.text((0, 0), 'Hello, world', fill=TEXT_COLOR)
   #img.show()

結果画像の掲載を割愛する。
上のコードのとおりに動作させると、黒地に赤字の ``Hello, world`` が見える。

日本語テキスト
----------------------------------------------------------------------
コツは 3 つある。

* 関数 ``ImageFont.truetype`` で日本語対応のフォントオブジェクトを作成する。
* その際に ``encoding`` 引数に適切なエンコーディングを指示する。
* ``text`` メソッドの引数にそのフォントを与える。

.. code-block:: python3

   from PIL import Image
   from PIL import ImageDraw
   from PIL import ImageFont

   img = Image.new('RGB', (1024, 256), 'black')
   dr = ImageDraw.Draw(img)
   fnt = ImageFont.truetype('hgrme.ttc', 24, encoding='utf-8')

   text = '''どうしても会ってもらえませんか？
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
   img.show()
   #img.save('karous-paradise.png')

処理後の画像はこうなる。PIL のときと同一のように見える。
出力イメージの大きさはテキストにフィットする最小の矩形になるはずだ。

.. image:: /_static/karous-paradise.png

応用
======================================================================

スクリーンショット
----------------------------------------------------------------------
スクリーンショット取得機能が Windows のみ対応なのは PIL も Pillow も同じようだ。

.. code-block:: python3

   from PIL import Image, ImageGrab

   # スクリーンショットをキャプチャーして
   img = ImageGrab.grab()
   # テキトーに縮小、表示する。
   img.thumbnail((256, 256), Image.ANTIALIAS)
   img.show()

処理後の画像の一例を掲載する。

.. image:: /_static/grab.png
   :scale: 100%

上下左右ループ壁紙パターン生成
----------------------------------------------------------------------
* 元画像を :math:`2 \times 2` 分割して対角線上の区域を入れ替える。
* そこへ元画像をブレンドなりオーバーレイなりして重ね合わせる。
* 左右方向ループのための区域入れ替えの処理は、 :file:`pil-handbook.pdf` 参照。

.. code-block:: python3

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

元画像と処理後の画像はこうなる。

.. image:: /_static/illvelo.png
   :scale: 50%
.. image:: /_static/illvelo-wallpaper.png
   :scale: 50%

モジュール ImageDraw2
----------------------------------------------------------------------
TBW

モジュール ImageGL
----------------------------------------------------------------------
TBW

モジュール ImagePath
----------------------------------------------------------------------
TBW

コマンドラインユーティリティー
======================================================================
PIL と同じスクリプトファイル群が Pillow のインストール時も :file:`Scripts` フォルダーに格納される。

フォーマット変換
----------------------------------------------------------------------
コマンドラインで :file:`pilconvert.py` を利用する。

.. code-block:: console

   $ pilconvert.py sample.gif sample.png

.. code-block:: console

   $ for name in *.gif ; do \
   >   pilconvert.py $name ${name%.*}.png ; \
   > done

リサイズ
----------------------------------------------------------------------
コマンドラインで :file:`pildriver.py` を利用する。
以前にも記したが、バッチモードとインタラクティブモードがある。

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

.. _Python: http://www.python.org/
.. _Python Extension Packages for Windows - Christoph Gohlke: http://www.lfd.uci.edu/~gohlke/pythonlibs/
.. _PIL: http://www.pythonware.com/products/pil
.. _Pillow: https://pillow.readthedocs.org/en/latest/
