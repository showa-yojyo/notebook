======================================================================
Python からはじめる数学入門 読書ノート
======================================================================

Python で数学を「やる」本。標準パッケージに加え、
Matplotlib_ と SymPy_ を使っていろいろやってみるという趣旨の本。

.. include:: /_include/book-details/saha16.txt

.. contents:: ノート目次

1 章 数を扱う
======================================================================
ウォーミングアップ。

* 分数と複素数は Python 標準で扱える。虚数単位は ``j`` または ``J`` とする。
* それらのオブジェクトを関数 ``input`` で生成することもできる。
  ただし、文字列を実引数とするコンストラクターの処理が空白文字に不寛容だ：

  .. code:: ipython

     In [155]: Fraction(input('Enter a fraction: '))
     Enter a fraction: 1 / 273
     ---------------------------------------------------------------------------
     ValueError                                Traceback (most recent call last)
     <ipython-input-155-a5ccacbc5a9b> in <module>()
     ----> 1 Fraction(input('Enter a fraction: '))
     
     D:\Miniconda3\lib\fractions.py in __new__(cls, numerator, denominator, _normalize)
         136                 if m is None:
         137                     raise ValueError('Invalid literal for Fraction: %r' %
     --> 138                                      numerator)
         139                 numerator = int(m.group('num') or '0')
         140                 denom = m.group('denom')
     
     ValueError: Invalid literal for Fraction: '1 / 273'

* 複素数を扱う機能を提供するモジュールとして ``cmath`` がある。

  IPython でインポートして ``dir`` して、基本的な解析関数、
  二数の比較用関数、座標系変換関数、定数などが提供されていることを確認した。
  例えば偏角を得るには関数 ``cmath.phase`` を用いるようだ。

  複素数のオブジェクトとしての属性は共役、実部、虚部くらいしかないようだ。

* 二次方程式の判別式を得るための平方根の取り方は、本書では
  ``math.sqrt`` ではなく ``** 0.5`` を採用している。

2 章 データをグラフで可視化する
======================================================================
早くもプロットを扱う。

* クラス ``list`` および ``tuple`` の基本。

  * 本書では両者の違いを要素を追加できるかどうかの一点に絞って述べている。
  * 要素の反復を ``for`` ループで実行でき、要素そのものだけでなく添字も
    得る場合には ``enumerate()`` 関数を用いることに触れている。

* Matplotlib を使ってプロットする。キャンバスの制御方法。

  * 本書のコードを試すときは IPython で pylab を有効にしておくと手っ取り早い。
  * ``marker='o'`` と単に ``o`` を指定するときの違い。
  * ``plot`` 関数は y 列データだけを指定することも、
    x 列と y 列の両方を指定することもできる。
  * 複数データセットを一度にプロットできる。こういう場合は ``legend()`` を活用する。
  * ``months = range(1, 13)`` を引数に 3 回渡すのでプロット時に ValueError を生じる？
  * プロットをインクリメンタルに装飾できることに早く気付きたかった。

* インタラクティブシェルでは pylab を、ふつうのスクリプトでは pyplot を使うのが効率的だ。
* ``pyplot`` の ``savefig`` で画像をファイルに保存できる。

* パラメーター表示される曲線のプロット（例：万有引力、投射軌跡）。

  * 浮動小数点数版 ``range`` がない問題は NumPy で片付けたい。
    この場合は ``np.linspace(0, 0.72, 720)`` だ。

  * サンプルコードを見て思うのだが、本書はリストの内包表現を紹介するべきだった。
    こちらのほうがわかりやすいだろう：

    .. code:: python3

       x_data = [u * np.cos(theta) * t for t in intervals]
       y_data = [u * np.sin(theta) * t - 0.5 * g * t**2 for t in intervals]
       draw_trajectory(x_data, y_data)

  * 投擲問題の複数版、タイトル変更コードが抜けている。

* 章末問題で棒グラフ（ヒストグラムではない）を紹介。
  これは pyplot ベースのコードなので、あえて IPython で pylab ベースで試す。

  .. code:: ipython

     In [236]: steps = (6534, 7000, 8900, 10786, 3467, 11045, 5095)
     
     In [237]: labels = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
     
     In [238]: positions = range(1, len(steps)+1)
     
     In [239]: pylab.barh(positions, steps, align='center')
     Out[239]: <BarContainer object of 7 artists>
     
     In [240]: pylab.yticks(positions, labels)
     Out[240]:
     ([<matplotlib.axis.YTick at 0x241d1860358>,
       <matplotlib.axis.YTick at 0x241d1b79c50>,
       <matplotlib.axis.YTick at 0x241d088ea20>,
       <matplotlib.axis.YTick at 0x241d189a898>,
       <matplotlib.axis.YTick at 0x241d189ae80>,
       <matplotlib.axis.YTick at 0x241d1cc0390>,
       <matplotlib.axis.YTick at 0x241d1cc0860>],
      <a list of 7 Text yticklabel objects>)
     
     In [241]: pylab.xlabel('Steps')
     Out[241]: Text(0.5,23.3022,'Steps')
     
     In [242]: pylab.ylabel('Day')
     Out[242]: Text(33.5972,0.5,'Day')
     
     In [243]: pylab.title('Number of steps walked')
     Out[243]: Text(0.5,1,'Number of steps walked')
     
     In [244]: pylab.grid()

* 章末問題最後の Fibonacci 数の隣接項の比のプロット、
  下手にコードを書くとべらぼうに時間がかかって面白いとみた。

  お手本コードを改造して、比も同時に返すようなジェネレーターを書くのが楽だ：

  .. code:: ipython

     In [272]: def fibo(n):
          ...:     f1 = f2 = 1
          ...:     yield f1, 0
          ...:     if n == 1: return
          ...:     yield f2, 1
          ...:     if n == 2: return
          ...:     for i in range(3, n + 1):
          ...:         next = f1 + f2
          ...:         yield next, next / f2
          ...:         f1, f2 = f2, next
          ...:

.. note:: 関連ノート

   * :doc:`python-matplotlib/index`

3 章 データを統計量で記述する
======================================================================
統計。

* 本章では母集団全体の統計量を考慮する。

  * つまり Python 標準の ``statistics.pvariance()`` と ``statistics.pstdev()`` を使えば、
    本書の計算と一致する。

* 算術平均、中央値、最頻値等、分散、標準偏差を自分で実装する。
  クラス ``collections.Counter`` の使い方がわかる。

  * 算術平均は自作しなくても ``statistics.mean()`` で得られる。
  * 中央値は ``statistics.median()`` で得られる。さらにその仲間もいる。
  * 最頻値は ``statistics.mode()`` で得られる。
    本書では ``collections.Counter.most_common()`` を利用していて、
    これはこれでおもしろい。
    最頻値が複数ある場合に StatisticsError が送出されるのが嫌な場合に有益。

* 図 3-1 (p. 80) のプロットはあやしい。

* あとは Peason 相関、散布図の描き方、CSV ファイルの読み込み方など。

  * 単に相関関係といったら Peason のそれを意味することにする。
    線形関係の強さを測る指標だ。
  * 相関係数の式 (p. 82) を実現するのに Python 組み込みの ``zip()`` と ``sum()`` を駆使する。
  * Anscombe のデータセットが散布図の重要性に一定の説得力を持たせている。
    平均、分散、相関係数がすべて同じであっても、
    データセットとしてはまったく異なることがふつうだ。

4 章 SymPy で代数と式を計算する
======================================================================
ここから SymPy を利用していく。

* ``Symbol`` オブジェクトによる数式表現。
* 数式の変形には ``factor()`` や ``expand()`` などを用いる。
* 数式を出力する際の関数 ``pprint()`` の制御方法。
  本書では <人が式を紙に書く場合に近い形式で出力> するものだと述べている。

  * ``init_printing()`` の ``order`` 指定がまったく効かない？

* 数式オブジェクトのメソッド ``subs()`` によるシンボルへの値の代入。

  * ここにきてようやく辞書の出番だ。

* 文字列を SymPy の数式オブジェクトにするのには関数 ``sympify()`` を利用する。

  * 変換失敗時に送出される例外が SympifyError だ。
  * 中学生の代数の宿題を解くツールとか作れそうだ。

* 方程式を ``solve()`` で解く。けっこうな種類の方程式を解くことができる。

  * 脚注でも説明があるように、Windows で p. 115 の方程式の解の辞書オブジェクトを
    出力すると、ここに載せるのもはばかられるような見苦しい形のアスキーアートが得られる。

* SymPy はプロット機能も提供している。

  * 先述の ``sympify()`` と組み合わせるとインタラクティブなプロッターが作れる。
  * 複数プロットを定義するときの、Matplotlib とのやり方の違いに注意。

* 章末問題で不等式や有理式を扱う。

  * 多項式の不等式を解くのには ``solve_poly_inequality()`` 関数を使う。
    解となる集合を範囲のリストの形で返すようだ。

  * 有理式の不等式を解くのには ``solve_rational_inequality()`` 関数を使う。

    * すごく使いにくい。分子と分母をそれぞれ Poly オブジェクトとして与えるのが面倒だ。
    * 解となる集合を集合の形で返すようだ。なぜ先ほどと流儀が違うのだ。

  * わけのわからない不等式は ``solve_univariate_inequality()`` 関数を使う。
    名前の示すように一変数専用なのだろう。

  * 章末問題の意図は、上記 3 種類の Adapter パターンを実装した
    不等式ソルバー関数 ``isolve()`` を設計、実装しろということだ。
    そのためにいくつかの問い合わせ関数が有用だと言っている：

    * ``is_polynomial()``
    * ``is_rational_function()``

.. note:: 関連ノート

   * :doc:`python-sympy/index`

5 章 集合と確率を操作する
======================================================================
集合と確率。

* 脚注を見ると訳者は確かな数学的知識の持ち主であることが窺える。
* クラス ``FiniteSet`` およびそのメソッドの紹介。
* 一様分布（自力）。
* 乱数。Python 標準の関数ももちろん利用できる。
* 章末問題にベン図 (matplotlib_venn) がある。あとは大数の法則を検証したり、
  シャッフルしたり、モンテカルロ法みたいなことをする。

6 章 幾何図形とフラクタルを描画する
======================================================================
Matplotlib のより高度な API を利用する。

* Patch と呼ばれる簡単な図形を描画する。
* Animation もサポート。一時変数が未使用に見えるかもしれないが、
  早過ぎるガベージコレクションを回避するために必要。
* `フラクタル <http://mathworld.wolfram.com/Fractal.html>`__、
  `ランダムウォーク <http://mathworld.wolfram.com/RandomWalk.html>`__、
  `シェルピンスキーギャスケット <http://mathworld.wolfram.com/SierpinskiCarpet.html>`__、
  `バーンズレイのシダ <http://mathworld.wolfram.com/BarnsleysFern.html>`__
  `エノン写像 <http://mathworld.wolfram.com/HenonMap.html>`__
* `マンデルブロ集合 <http://mathworld.wolfram.com/MandelbrotSet.html>`__ のために
  ``imshow`` を用いる。

7 章 初等解析問題を解く
======================================================================
極限、微分、積分、そしてなぜか確率密度関数を扱う。

* 標準の ``math`` パッケージが有用な関数を提供している。
* 極限は SymPy クラス ``Limit`` が使える。例題である種の複利計算の極限値を求める。
* 微分は SymPy クラス ``Derivative`` が使える。常微分も偏微分も同じインターフェイス。
* 極値の計算には :math:`f'(x) = 0` や :math:`f''(x) = 0` を ``solve`` することが重要だ。
* 勾配上昇法を自力で実装する。このアルゴリズムは初期値の選定がたいへん重要だ。
* 積分は SymPy クラス ``Integral`` が使える。原始関数と定積分の両方を求めるのに利用できる。
* 確率密度関数各種。いわゆるグラフの面積が確率の値を意味する。
* 章末問題に曲線の長さを求める主題のものがある。

付録 A ソフトウェアのインストール
======================================================================
Windows だけ読んだ。本書は Anaconda の使用を推奨している。
どうもこの記述の内容からすると、Matplotlib も SymPy も勝手にインストールされるようだ。

* ただし明示的にアップグレードする方法があるので、それを紹介している。
* 前述したベン図のパッケージは pip でインストール可能だ。訳者は失敗したらしいが。

あとがき
======================================================================
`Project Euler <https://projecteuler.net/>`__ について言及している。

訳者あとがき
======================================================================
Computer Based Math について述べられている。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
