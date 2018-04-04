======================================================================
整数論
======================================================================
SymPy_ の整数論モジュールについて記す。

.. contents:: ノート目次

.. note::

   本文中のすべての IPython セッション中のサンプルコードで、
   以下のインポートおよび出力書式設定が済んでいるものとする。

   .. code:: python3

      init_printing(pretty_print=False)

素数
======================================================================
クラス Sieve
----------------------------------------------------------------------
クラス Sieve は素数全体を表現する。または表現したい。
「エラトステネスのふるい」にちなんだクラス名は、
クラスの素数の管理方法をなんとなく示唆している。

* メソッド :code:`extend` で、指定素数までの全ての素数をオブジェクトが保持するようにできる。
* メソッド :code:`extend_to_no` で任意番目の素数までの以下同文。

ユーザーが自分でコンストラクター経由でオブジェクトを生成するのもよいが、
実は :code:`sympy` スコープにオブジェクト :code:`sieve` が存在している。
まずはこれを試すとよい。

* :code:`p in sieve` で :code:`p` が素数がどうかをテストできる。

  * テストまでにユーザーが :code:`sieve` を大きくする必要はない。
    オブジェクト自身が必要に応じて :code:`extend(p)` のようなことをする。

  * 運が悪いとメソッドが例外 MemoryError を送出する。

* :code:`sieve.primerange(a, b)` で :code:`a` 以上 :code:`b` 未満のすべての素数を列挙するジェネレーターを生成する。
* :code:`sieve.search(n)` が少しわかりづらい。
  ドキュメントによると :code:`i <= n < j` なる素数列の添字 :code:`(i, j)` を返すようだが、
  :code:`n` が素数ならば :code:`(i, i)` を返す。
  はて :code:`j` は常に :code:`i` または :code:`i + 1` ではないのだろうか。

素数に関連する関数
----------------------------------------------------------------------
素数に関連する関数は主にモジュール ``sympy.ntheory.generate`` に定義されている。
憶測だが（コードを読めば直ちに判明するが）、
これらの関数の内部では上述のオブジェクト :code:`sieve` を参照しているのではないだろうか。

関数 :code:`prime(i)`
  任意 :code:`i` 番目の素数を得られる。

関数 :code:`primepi(n)`
  指定した数よりも小さい素数の個数を返す。
  引数が素数の場合はそれも含んで計上する。

  * 10 億を試したら MemoryError で失敗。
  * 関数 :code:`integrate` の被積分関数として扱えない？

関数 :code:`nextprime(n, i=1)`, :code:`prevprime(n, i=1)`
  指定した数から大きい、または小さい :code:`i` 番目の素数を返す。

  * キーワード引数 :code:`i` に負の値を指定すると、直感に反する値が返る。
  * :code:`prevprime` のほうは例外 ValueError を送出することがある。

関数 :code:`primorial`
  どう使おう。
  引数の意味をキーワード引数 :code:`nth` で変えられることに注意。

次の素数に関連する関数はモジュール ``primetest`` に存在する。

関数 :code:`isprime(p)`
  指定した数が素数かどうかテストする。

  ただし、この関数が正確にテストするために :code:`p` に上限があるようだ。

素因数分解と約数
======================================================================
モジュール ``sympy.ntheory.factor_`` には素因数分解や約数にまつわる関数がある。
本当は 10 個を軽く超える関数が提供されているのだが、
私が理解できるものだけをここに記す。

関数 :code:`factorint(n)`
  正の整数 :code:`n` を素因数分解して、結果を通常は dict オブジェクトの形で返す。

  * 例えば :code:`factorint(2000)` は :code:`{2:4, 5:3}` を返す。
    キーが素因数、値が指数のペアの辞書。
  * キーワード引数がたくさんある。
  * 実装コードを見たらわけがわからない。

関数 :code:`primefactors(n)`
  因数のリストだけを返す。指数は捨てられる。

  内部で :code:`factorint` を利用しており、
  キーワード引数 :code:`limit` と :code:`verbose` が引き継がれる。

関数 :code:`divisors(n, generator=False)`
  整数 :code:`n` の約数を 1 から :code:`n` までソートして list オブジェクトで返す。

  ただしキーワード引数で :code:`generator=True` とするとき、動きが全く異なる。
  関数が約数を列挙するジェネレーターを返す。
  さらに yield する値の順番は関数のそれとは異なる。

関数 :code:`divisor_count(n, modulus=1)`
  整数 :code:`n` の約数の個数を返す。

  実装は関数 :code:`factorint` の返す各素因数の指数を利用している。

* 関数 :code:`udivisors`, :code:`udivisor_count` というものもある。
* 関数 :code:`antidivisors`, :code:`antidivisor_count` というものもある。

クラス :code:`totient`
  オイラーの totient 関数を計算するクラス。
  実装で関数 :code:`factorint` の結果をフル活用している。

  * クラス Function のサブクラスなので、
    評価をするには :code:`totient(n)` のようにする。

    .. code:: ipython

       In [1]: [totient(10 ** i) for i in range(10)]
       Out[1]: [1, 4, 40, 400, 4000, 40000, 400000, 4000000, 40000000, 400000000]

関数 :code:`digits(n, p=10)`
  任意整数 :code:`n` を :code:`p` 進数表現して、その各桁をリストする。
  戻り値は list オブジェクトだが、
  最初の要素は :code:`p` そのものなので捨ててよい。

合同式
======================================================================
モジュール ``sympy.ntheory.modular`` は合同式に関係する機能を提供する。
使えそうなものをピックアップしていこう。

関数 :code:`crt(m, v, symmetric=False, check=True)`
  中国剰余定理に基づく問題を解くのに利用できる。
  例を示す。

  .. code:: ipython

     In [1]: crt([3, 5, 7], [2, 3, 2])
     Out[1]: (23, 105)

  23 + 105k を 3, 5, 7 でそれぞれ割ると余りが 2, 3, 2 になるという解が得られた。

  * キーワード引数 :code:`symmetric=True` とすると、
    剰余が対称になるように、解が必要に応じて非負で得られる。

  * キーワード引数 :code:`check=False` の使いどころが不明。

    .. code:: ipython

       In [1]: crt([6, 10], [1, 2], check=True)

       In [2]: crt([6, 10], [1, 2], check=False)
       Out[2]: (14, 60)

関数 :code:`solve_congruence(*remainder_modulus_pairs, **hint)`
  合同式を解くわけだが、前述の関数 :code:`crt` と同様だと思う。
  ただし引数の順序が異なる。

  * :code:`solve_congruence((2, 3), (3, 5), (2, 7))`
  * :code:`solve_congruence(*zip((2, 3, 2), (3, 5, 7)))`
  * :code:`crt` が :code:`solve_congruence` を利用している。

二項係数と多項係数
======================================================================
モジュール ``sympy.ntheory.multinomial`` にある関数について記す。
モジュール名は多項係数だが、二項係数に特化した関数も存在する。

関数 :code:`binomial_coefficients(n)`
  パスカルの三角形の n 段目を dict で返す。

  辞書のキーは tuple オブジェクト :code:`(0, n)`, :code:`(1, n - 1)`, ... , :code:`(n, 0)` である。
  分母に来る階乗ふたつの引数と覚えられる。
  辞書の値は、それぞれのキーに対応する二項係数を表す。

関数 :code:`binomial_coefficients_list(n)`
  パスカルの三角形の n 段目を全部得る。戻り値は list である。

  こちらは単に二項係数が一列に並んだものが得られる。

関数 :code:`multinomial_coefficients(m, n)`
  二項係数を得る関数 :code:`binomial_coefficients(n)` の一般化版。

  二項係数は :math:`(a_1 + a_2) ^ n` の各項の係数だが、多項係数は
  :math:`(a_1 + a_2 + ... + a_k) ^ n` の各項の係数を表現する。

ジェネレーター :code:`multinomial_coefficients_iterator(m, n)`
  関数 :code:`multinomial_coefficients(m, n)` のジェネレーター版。
  関数版よりも空間的にも時間的にも効率的であることが期待できる。

剰余
======================================================================
モジュール ``sympy.ntheory.residue_ntheory`` にある関数について記す。
ただしインポートは :code:`from sympy.ntheory import ...` で可能。

関数 :code:`n_order(a, n)`
  乗積順序を求める。
  :code:`a ** k % n == 1` を満たす最小の整数 :code:`k` を返す。
  これを <the order of `a` modulo `n`> と英語では言うらしい。
  日本語なら「`a` の法 `n` の位数」か。

  .. code:: ipython

     In [1]: n_order(10**100 + 1, prime(1000))
     Out[1]: 3959

     In [2]: Pow(Pow(10, 100), 3959) % prime(1000)
     Out[2]: 1

関数 :code:`is_primitive_root(a, p)`
  :code:`a` が :code:`p` の原始根であるかをテストする。

  意味としては :code:`a` と :code:`p` が互いに素であり、
  かつ :code:`p` が :code:`a ** totient(p) % p == 1` を満たす最小の :code:`p` であるかどうかをテストする。
  言い換えると :code:`a` の位数が :code:`p - 1` であるかどうかをテストする。

関数 :code:`primitive_root(p)`
  存在するときに限り :code:`p` の最小の原始根を返す。
  つまり :code:`p` と互いに素で、かつ :code:`p` を法とする整数の乗法群の生成元を求める。

  .. code:: ipython

     In [1]: primitive_root(27)
     Out[1]: 2

     In [2]: any([(2**i) % 27 for i in range(30)])
     Out[2]: True

     In [3]: n_order(primitive_root(27), 27) == totient(27)
     Out[3]: True

他にも色々あるので、アレがないかコレがないかというときはドキュメントを当たるべし。

連分数
======================================================================
モジュール ``sympy.ntheory.continued_fraction`` に置いてある、
連分数を扱う関数各種について記す。

ジェネレーター :code:`continued_fraction_iterator(x)`
  引数 :code:`x` の連分数展開（分子は全部 1 とする）を求め、その分母をひとつずつ yield する。

  一度実装を見ておいたほうがよい。

  * これは微妙に使いにくい。
    値によっては自分でループを書く必要があるだろう。

    .. code:: ipython

       In [1]: from itertools import islice

       In [2]: list(islice(continued_fraction_iterator(coth(1)), 20))
       Out[2]: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]

       In [3]: list(islice(continued_fraction_iterator(S.Pi), 20))
       Out[3]: [3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2, 2, 2, 2]

ジェネレーター :code:`continued_fraction_convergents(cf)`
  連分数 :code:`cf` の「真の値」に収束する数列の数をひとつずつ yield する。

  * :code:`cf` は連分数の各項（分母）を list オブジェクト等に収容したもの。
  * :code:`cf` の各項の分子が 1 であるという条件は特に課せられていない。

関数 :code:`continued_fraction_periodic(p, q, d=0)`
  整数係数二次方程式の根となる無理数の循環連分数展開を返す。
  単に :code:`(p + sqrt(d)) / q` の連分数を返すと覚えておいて支障はない。

  * 戻り値は入れ子の list オブジェクトで、内側のそれが循環部分を示す。
  * 根号の中 :code:`d` が平方数の場合は連分数は循環しない。
    戻り値はフラットな list オブジェクトとなる。

関数 :code:`continued_fraction_reduce(cf)`
  連分数 :code:`cf` を連分数でない形で返す。

  .. code:: ipython

     In [1]: from sympy.abc import a, b, c

     In [2]: continued_fraction_reduce([a, b, c])
     Out[2]: (a + c*(a*b + 1))/(b*c + 1)

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
