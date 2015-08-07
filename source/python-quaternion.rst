======================================================================
Quaternion 利用ノート
======================================================================
本稿では Python_ パッケージ Quaternion_ について記す。
このパッケージを利用する目的、導入方法、私が興味のある機能の利用方法について調べる。

.. contents:: ノート目次

.. note::

   * OS

     * Windows 7 Home Premium SP 1

   * 本稿において、利用した各パッケージのバージョンは次のとおり。

     * Python_: 3.4.1
     * Quaternion_: 0.03.1
     * NumPy_: 1.8.2

関連リンク
======================================================================
Quaternion_
  パッケージ配布元。

`Quaternions and spatial rotation`_
  ここに書いてあるようなことを Python のプログラムでやりたいのだ。

関連ノート
======================================================================
* :doc:`/python-numpy/index`: Quaternion は NumPy_ を利用して実装されている。
* :doc:`/python-pyopengl/index`: 私が Quaternion を利用したいのは、
  空間内での回転を制御するのに便利なはずだからと思うから。

目的
======================================================================
Hamilton の四元数を扱える Python パッケージがあれば、
とりあえず何かインストールしておきたい。
その理由は、PyOpenGL で色々な 3D グラフィックスの描画をする際に、
ほとんどすべてのプログラムでプリミティブの回転を取り扱う予定があるからだ。

四元数を用いることで、3 次元の点を

#. 指定の回転軸（3 次元の単位ベクトル）周りに
#. 指定角度（スカラー）だけ

回転させるという記述を手軽に表現できることを期待している。

インストール
======================================================================
まず、私がこのパッケージを知った経緯について記す。
単に pip の検索機能で知ったに過ぎない。

.. code-block:: console

   $ pip search quaternion
   qmath                     - qmath provides a class for deal with quaternion algebra and 3D rotations.
     Root evaluations and Moebius transformations are implemented.
   Quaternion                - Quaternion object manipulation
   quaternion-algebra        - Quaternion algebra for Python.
   quaternionarray           - Python package for fast quaternion arrays math
   mathutils                 - A general math utilities library providing Matrix, Vector, Quaternion, Euler and Color classes, written in C for speed.
   Pyternion                 - Pythonic Quaternion library including Euclidean geometry calculations
   euclid                    - 2D and 3D vector, matrix, quaternion and geometry module
   euclid3                   - 2D and 3D vector, matrix, quaternion and geometry module. updated to python 3.
   pypoints.py               - Classes to represent points, pointsets, anisotropic arrays, and quaternions

このように多数の候補が出力されるが、ここから私は一番名前が素直な Quaternion をインストールすることに決めた。

.. code-block:: console

   $ pip install Quaternion
   Downloading/unpacking Quaternion
     Downloading Quaternion-0.03.1.tar.gz
     Running setup.py (path:D:\Temp\pip_build_work\Quaternion\setup.py) egg_info for package Quaternion

   Installing collected packages: Quaternion
     Running setup.py install for Quaternion

   Successfully installed Quaternion
   Cleaning up...

インストールの成功は、当モジュールを無事にインポートできるかどうかの確認を以って代える。

インストール後のコピーライトによると、このパッケージは Smithsonian Astrophysical Observatory の作品だ。

使いたい機能を確認する
======================================================================
``np.array`` ベースで実装されているので、使い勝手のよいことを期待している。

インポート
----------------------------------------------------------------------
Quaternion を利用する最も普通の形態は、次のインポート文だけを書いて済ませることではないだろうか。

.. code-block:: python3

   from Quaternion import Quat

クラス ``Quat`` をインポートするだけで済ませ、
あとはオブジェクトを自分で生成して、それについて各種演算をメソッド利用により実現すればよい。

クラス ``Quat`` のコンストラクター
----------------------------------------------------------------------
クラス ``Quat`` のコンストラクターは、次のような特徴がある。

* デフォルトコンストラクター的な利用はできない。
  つまり、引数なしで ``Quat`` オブジェクトを生成することはできない。

* コピーコンストラクター的な利用ができる。

  * これ以外にオブジェクトのコピーの手段がなさそうだ。
    メソッドによるコピーは提供されていない。

* 私が想定する通常のコンストラクター利用法は、次のふたつだ。

  * 四元数成分の直接指定による生成

    * ``q = Quat([x, y, z, w])`` の形式で生成する。
      ただし、最初の 3 成分がベクトル成分で、最後の成分がスカラー成分である。
      私は当初、教科書の式に引っ張られて順序を間違えた。

    * 従って、デフォルト回転状態を表現するには ``Quat([0, 0, 0, 1])`` とする。

    * 引数は、各成分の平方の和が 1 である必要がある。
      どうもこのクラスは単位四元数だけをサポートしているようだ。

    * 生成後、プロパティー ``.q`` で成分を確認すると、符号が逆転していることがままある。
      これは、内部的には四元数のスカラー成分を正で表現する規約があるらしいためだ。

  * （回転）変換行列からの生成

    * ``q = Quat(m)`` の形式で生成する。
      ここで ``m`` は ``m.shape == (3, 3)`` を満たす ``np.array`` オブジェクトである。

    * 従って、無変換状態を表現するには単位行列を与える。
      例えば ``Quat(np.identity(3))`` とする。

    * おそらく無条件で ``q.transform == m`` となる。

* 他にも赤道座標系の表現を用いて ``Quat`` コンストラクターのパラメーターにする生成のやり方もある。
  本稿では取り扱わない。

プロパティー
----------------------------------------------------------------------
私がクラス ``Quat`` のプロパティーでよく利用するのは ``.q`` と ``.transform`` だけなので、
それらだけを記す。

* プロパティー ``.q`` で、四元数の成分を ``np.array`` の形でアクセスできる。

  * 最初の 3 成分がベクトル成分で、最後の成分がスカラー成分である。
  * 先述したが、内部的にはスカラー成分が正で表現されていることがわかる。

* プロパティー ``.transform`` で、この四元数の表現する回転変換を
  ``np.array`` の形でアクセスできる。

  * 3 次正方行列の shape である。
  * PyOpenGL のインターフェイスに渡す際には、これを 4 次正方行列に直す必要がある。

    .. code-block:: python3

       quat = Quat(...)
       rotation_matrix = np.identity(4)
       rotation_matrix[:3, :3] = q.transform
       glUniformMatrix4fv(location_of_matrix, 1, GL_TRUE, rotation_matrix)

四元数体の元としての演算
----------------------------------------------------------------------
四元数の乗法は可換ではないことに注意するとよい。

* 加法、減法はサポートされていない。

  数学的には四元数には加減乗除が定義可能なのだが、
  利用目的が目的であることと、単位四元数だけを取り扱う方針があるらしいことから、
  作者は実装しないことを決めたのだろう。

* 演算子 ``*`` による乗法が ``__mul__`` によりサポートされている。
* 演算子 ``/`` による除法が ``__div__`` によりサポートされている。
  ただし ``lhs / rhs`` の意味は ``lhs * rhs.inv()`` である。
  いわば「右からの除法」ということだ。

グラフィックスのプログラムでの応用としては、
ひとつの ``Quat`` オブジェクトにひとつの「ある軸周りの、ある角度だけの回転操作」の意味を持たせることを考える。
複数の ``Quat`` オブジェクトの積は、複数の連続回転操作の意味を持たせることができるはずだ。
回転の順番に注意を要するのと同様に、四元数同士の積の順番にも注意を要する。

逆元
----------------------------------------------------------------------
* メソッド ``.inv()`` を用いる。ソースコードを見ると一瞬面食らうが、
  ノルムが 1 の四元数だけをサポートすることになっているからこれでよい。

* 採り上げておいてなんだが、これはおそらく利用しないで済む。

共役
----------------------------------------------------------------------
メソッドとしてはサポートされていない。必要があればすぐに安全に自作できる。

演習
======================================================================
ここでひとつ四元数を用いた回転変換を計算する例を試そう。
`Quaternions and spatial rotation`_ の Example の回転をコード化してみよう。
ただし、ここでは conjugation ではなく回転行列を用いる。つまり：

#. 与えられた角度 ``alpha`` と回転軸 ``axis`` に対して、
   四元数オブジェクト ``q`` を返す関数を作成する。
#. プロパティー ``q.transform`` を用いて、いろいろな 3 次元ベクトルの回転を試す。

回転用四元数生成関数を実装する
----------------------------------------------------------------------
次のようなテキスト片をテキストエディターに書きつける。

.. code-block:: python3

   def make_quat(alpha, axis):
       alpha_half = alpha / 2
       cosa = np.cos(alpha_half)
       sina = np.sin(alpha_half)
       v = sina * (axis / norm(axis))
       return Quat([v[0], v[1], v[2], cosa])

IPython のセッションでコードを試すつもりでいるので、各種 import 文を省略している。
それから関数全体をおもむろにクリップボードにコピーし、IPython のセッションで ``%paste`` する。

.. code-block:: ipython

   In [1]: %paste
   def make_quat(alpha, axis):
       def make_quat(alpha, axis):
       alpha_half = alpha / 2
       cosa = np.cos(alpha_half)
       sina = np.sin(alpha_half)
       v = sina * (axis / norm(np.array(axis, copy=False)))
       return Quat([v[0], v[1], v[2], cosa])

   ## -- End pasted text --

それでは Wikipedia の The conjugation operation の状況を再現してみよう。

.. code-block:: ipython

   In [2]: q1 = make_quat(np.pi * 2/3, np.array([1, 1, 1]))

   In [3]: q1.q
   Out[3]: array([ 0.5,  0.5,  0.5,  0.5])

所望の四元数が得られたようだ。

行列による回転変換を試す
----------------------------------------------------------------------
まずはプロパティー ``q.transform`` を用いた 3 次元ベクトルの回転を確認したい。
これがうまくいけば、当初の計画通りに PyOpenGL のプログラムに応用できる。

.. code-block:: ipython

   In [4]: t = q1.transform

   In [5]: t
   Out[5]:
   array([[  0.00000000e+00,  -1.11022302e-16,   1.00000000e+00],
          [  1.00000000e+00,   0.00000000e+00,  -1.11022302e-16],
          [ -1.11022302e-16,   1.00000000e+00,   0.00000000e+00]])

適当に 3D ベクトルを与えて、成分が軸 ``[1, 1, 1]`` 周りに 120 度回転するかテストしよう。

.. code-block:: ipython

   In [6]: dot(t, [1, 2, 3])
   Out[6]: array([ 3.,  1.,  2.])

問題なさそうだ。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
.. _Quaternion: http://cxc.harvard.edu/mta/ASPECT/tool_doc/pydocs/Quaternion.html
.. _Quaternions and spatial rotation: http://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation
