======================================================================
幾何
======================================================================
SymPy_ のサブパッケージ ``sympy.geometry`` に関わる覚え書きを記す。

.. contents:: ノート目次

主要クラス図
======================================================================
サブパッケージ ``sympy.geometry`` が提供する主要クラスの継承関係のみを図示するとこういう感じになる。

.. code-block:: text

   GeometryEntity
       Point
       Point3D
       LinearEntity
           Segment
           Ray
           Line
       LinearEntity3D
           Line3D
           Ray3D
           Segment3D
       Plane
       Polygon
           Triangle
           RegularPolygon
       Ellipse
           Circle
       Curve

* クラス GeometryEntity のスーパークラスはクラス Basic である。

クラス継承関係
======================================================================
* 基本的に 2 次元幾何。同じ幾何要素で次元が異なるものはクラスも別々に定義がある。
  例えば Point と Point3D が存在する。

  * ここにあるあらゆるメソッド、関数は 2D と 3D を混ぜて利用することを想定していない。

* RegularPolygon is-a Polygon だったり Circle is-a Ellipse だったりする。
  オブジェクト指向プログラミングの本からするとこういう設計はするなと言われそうだが、
  SymPy は記号数学のライブラリーなのでむしろアリということだろう。

共通機能
======================================================================
ここでは便宜上、次のものを共通機能と呼んで理解を深める。

#. クラス GeometryEntity のオブジェクトを引数に取る関数
#. クラス GeometryEntity の静的・クラスメソッド
#. クラス GeometryEntity のメソッド

クラス GeometryEntity のオブジェクトを引数に取る関数
----------------------------------------------------------------------
* 関数 :code:`intersection`

  * 引数は複数個の GeometryEntity オブジェクト。
  * 戻り値は list で、その要素は Point や Segment になるのだろう。

* 関数 :code:`convex_hull`

  * 複数個の Point, Segment, Polygon オブジェクトを引数に取る。
  * 戻り値は基本的には凸包を表現する Polygon オブジェクトだが、
    場合によっては Segment かもしれない。

* 関数 :code:`are_coplanar`

  * 引数は複数個の GeometryEntity オブジェクト。
  * 引数のすべての 3D オブジェクト全部がある平面上に乗っているかどうかをテストする。
  * そのような平面が Plane オブジェクトとして返るわけではないようだ？
  * 2D のオブジェクトは一応 3D 化してから計算してくれる。計算するまでもないだろう。

* 関数 :code:`are_similar`

  * ふたつの GeometryEntity オブジェクトが相似かどうかをテストする。
  * 単に :code:`entity1.is_similar(entity2)` よりも気が利いた処理をするに過ぎない。

* 関数 :code:`centroid`

  * 引数は複数個の GeometryEntity オブジェクト。
  * おそらく同型でなければならない。
  * 戻り値は Point オブジェクトで、オブジェクト全部が決定する重心の座標を表現する。

クラス GeometryEntity の静的・クラスメソッド
----------------------------------------------------------------------
クラス GeometryEntity の静的・クラスメソッドは存在しない。

クラス GeometryEntity のメソッド
----------------------------------------------------------------------
* メソッド :code:`intersection` は先述の同名関数を参照。
* メソッド :code:`is_similar` は先述の関数 :code:`are_similar` を参照。
* 変形系メソッド :code:`rotate`, :code:`scale`, :code:`translate`, :code:`reflect` が提供されている。

  * :code:`rotate`, :code:`scale` は変形の原点を指定できる。
  * :code:`reflect` には LinearEntity オブジェクトを渡すようだ。

* メソッド :code:`encloses`

  * 自身のオブジェクトの内側に与えられたオブジェクト全体を含むかどうかをテストする。
  * 実装にはサブクラスのメソッド :code:`encloses_point` を利用している。
  * 造りが美しくない。

* メソッド :code:`equals` が提供されており、オーバーライドがなければ :code:`e1 == e2` と同値。
* 演算子がいくつか定義されているが、これらの存在はひとまず忘れておく。

サブクラス
======================================================================
以下、クラス GeometryEntity の各サブクラスについての感想やら何やらを記す。

* クラス Point

  * 座標成分は具体的な数値でもよいし、シンボルでもよい。
    ただし、いくつかの判定モノの関数は具体的な Point で計算しないと意味がなくなる。

  * プロパティー :code:`length` は必ずゼロを返す。
  * メソッド :code:`is_collinear` と :code:`is_concyclic` はクラスメソッドである。

   * 類似したライブラリーを色々知っているが :code:`is_concyclic` 的なものは初めてお目にかかる。

  * メソッド :code:`evalf` は各座標を浮動小数点数で表現し直した Point を返す。
  * メソッド :code:`dot` でドット積を計算する。
  * 演算子で加算、減算、スカラー倍、etc. が実現できる。
    単項マイナスと絶対値もサポート。

  * メソッド :code:`transform` は行列を右から掛けるようだ。vM 方式。

* クラス Point3D

  * クラス Point にあるものは、だいたいその 3 次元版メンバーが存在する。
  * クラス Point にはない次のメソッドに注意。

    * メソッド :code:`direction_ratio`, :code:`direction_cosine`
    * クラスメソッド :code:`are_collinear`, :code:`are_coplanar`

  * メソッド :code:`is_collinear` と :code:`is_concyclic` は存在しない。

* クラス LinearEntity

  * 2 次元空間内のまっすぐな線のためのスーパークラス。
  * この手のクラスによくあるプロパティー、メソッドがやはりある。

  * メソッド :code:`parallel_line`, :code:`perpendicular_line` は Line オブジェクトを生成する。

    * 一方、メソッド :code:`perpendicular_segment` は Segment オブジェクトを生成する。

  * クラスメソッド :code:`are_concurrent` 的なものは初めてお目にかかる。
    すべての引数が「一点で交差する」かどうかをテストする。

  * メソッド :code:`intersection` の対象は Point か LinearEntity に限定している？
  * メソッド :code:`arbitrary_point` で線上の任意の一点を返す。

    * デフォルトでは線のパラメーターシンボルを :code:`t` とする。

  * メソッド :code:`random_point` で線上の勝手な一点を返す。
  * メソッド :code:`is_similar` は線の傾きを比較する。

  * メソッド :code:`contains` は形状を集合と見たときの包含関係のテストと思ってよい。
  * メソッド :code:`distance` はここにはなく、各サブクラスにある。

* クラス Segment

  * 有限の線分を表現する。
  * メソッド :code:`plot_interval` は :code:`list(t, 0, 1)` を返す。
  * メソッド :code:`perpendicular_bisector` の仕様が CAD の感覚だとやや不親切な気がする。
    指定点が bisector に乗らない場合は、直線ではなくて中点から投影点までの線分を生成するのかと思った。

* クラス Ray

  * 半直線を表現する。
  * メソッド :code:`plot_interval` は :code:`list(t, 0, 10)` を返す。
  * プロパティー :code:`xdirection`, :code:`ydirection` により、
    形状がどの座標軸に沿って無限なのかがわかる。

* クラス Line

  * 直線を表現する。
  * メソッド :code:`plot_interval` は :code:`list(t, -5, 5)` を返す。
  * こいつだけメソッド :code:`equation` を持っていて、
    直線の式 :code:`simplify(a*x + b*y + c)` を生成する。

* クラス LinearEntity3D およびそのサブクラス群が LinearEntity 系と同じ階層構造で存在する。

* クラス Plane

  * 平面を表現する。平面に期待するメンバーが存在する。
  * 平行、垂直のテストは LinearEntity3D または Plane に対するものだ。
  * メソッド :code:`distance` の対象は Point3D, LinearEntity3D または Plane のいずれか。
  * メソッド :code:`arbitrary_point`, :code:`random_point` がある。
  * クラスメソッド :code:`are_concurrent` は複数の平面が共通の直線で交わるかどうかをテストする珍しいものだ。
  * メソッド :code:`is_coplanar` で平面に乗るかどうかをテスト。

* クラス Polygon

  * xy 平面上の多角形を表現する。
  * コンストラクターが気を利かせて、別のクラスのオブジェクトを生成することがある。
    極端な例を挙げると、一直線上に並ぶ任意の点列を Polygon のコンストラクターに与えると、
    得られるオブジェクトの型はなんと Segment である。

  * プロパティー :code:`area` で面積を計算する。符号付きの可能性がある。
  * プロパティー :code:`angles` で内角の list を返す。
  * プロパティー :code:`perimeter` は周長を返す。
  * プロパティー :code:`centroid` で重心に位置する Point オブジェクトを生成する。
  * プロパティー :code:`sides` で各辺を Segment で表現するオブジェクトの list を返す。

    * メソッド :code:`intersection` の計算はこれに基づく。

  * メソッド :code:`is_convex` でこの多角形が凸かどうかをテストする。
  * メソッド :code:`arbitrary_point` について

    * :code:`t=0` で始点
    * :code:`t=1` で終点

  * メソッド :code:`plot_interval` は :code:`list(t, 0, 1)` を返す。

* クラス Triangle

  * 三角形は多角形の中でも別格の存在ということで、専用クラスとして存在するようだ。
  * コンストラクターは色々な引数指定をサポートしている。
    使いやすいものを覚えておくこと。

    * 単に 3 頂点を Point オブジェクトで指定する。
    * キーワード引数 :code:`sss` 等と辺の長さ・角度を列挙を組み合わせて指定する。

      * オブジェクトの座標があらかじめ想像しづらい。

  * メソッド :code:`is_similar` の実装は、三辺の比をテストするだけ。
    辺の順序の組み合わせはすべて考慮する。

  * メソッド :code:`is_equilateral` で正三角形テスト。
  * メソッド :code:`is_isosceles` で二等辺三角形テスト。
  * メソッド :code:`is_right` で直角三角形テスト。

  * 五心

    .. csv-table::
       :delim: @
       :header: 名前, Point, Circle, 何の交点か
       :widths: 8, 8, 8, 24

       外心 (O)@:code:`circumcenter`@:code:`circumcircle`@:code:`sides().perpendicular_bisector()`
       垂心 (H)@:code:`orthocenter`@なし@:code:`altitudes`
       内心 (I)@:code:`incenter`@:code:`incircle`@:code:`bisectors`
       傍心 (J)@なし@なし@なし
       重心 (G)@:code:`centroid`@なし@:code:`medians`

* クラス RegularPolygon

  * 正多角形を表現するクラス。
  * 頂点の位置を直接指定してオブジェクトを生成するというよりは、半径と頂点数を指定する。
  * プロパティー :code:`length` の実装を見ると非効率的な印象を受けるが、記号数学演算的にはこれしかない。

    * これは :code:`perimeter` を利用しない。

  * プロパティー :code:`apothem` および :code:`inradius` で内接円の半径を得る。
  * プロパティー :code:`interior_angle` と :code:`exterior_angle` で多角形の内角、外角をそれぞれ得る。
  * プロパティー :code:`incircle` と :code:`circumcircle` で内接円、外接円を Circle オブジェクトとしてそれぞれ得る。

  * コンストラクターおよびメソッド :code:`spin` で多角形の中心点を軸に回転をかけられる。

* クラス Ellipse

  * コンストラクターが色々ある。

    * 長軸・短軸ではなく :code:`hradius`, :code:`vradius` のような扱いをする。

  * プロパティー :code:`minor`, :code:`major` で長軸、短軸の半分の長さを得る。
  * プロパティー :code:`circumference` で楕円の周長が得られる。定積分オブジェクトかもしれない。
  * プロパティー :code:`periapsis`, :code:`apoapsis` で楕円の焦点から近点、
    焦点から遠点の距離がそれぞれ得られる。

  * メソッド :code:`tangent_lines` である点から楕円上に接線を求める。

    * たいていの場合、戻り値は Line オブジェクト 2 個の list となる。

  * メソッド :code:`is_tangent` は Ellipse にも対応している。
  * メソッド :code:`normal_lines` はある点から楕円に垂直に交差する Line を求める。

    * 要素数は 1, 2, 4 のいずれか。
    * キーワード引数 :code:`prec` の存在に注意。

  * メソッド :code:`plot_interval` は :code:`list(t, -S.Pi, S.Pi)` を返す。
  * メソッド :code:`equation` で楕円の方程式（の左辺）を得る。
  * メソッド :code:`evolute` で楕円の縮閉線の方程式（の左辺）を得る。

* クラス Circle

  * コンストラクターは次のどちらかの引数リストを受け付ける。

    * 通過点を表現する Point オブジェクト 3 つ。
    * 中心を表現する Point と半径。

  * メソッド :code:`scale` で Ellipse オブジェクトが生成することがある。

* クラス Curve

  * 平面的なパラメトリック曲線を表現するクラス。
  * コンストラクターの例： :code:`Curve((sin(t), cos(t)), (t, 0, 2))`
  * プロパティー

    * :code:`limits` は曲線のパラメーター定義域を表現する tuple である。
    * :code:`parameter` は曲線のパラメーターのためのシンボルである。
    * :code:`functions` は各座標成分の関数の tuple である。

デモ
======================================================================

メネラウスの定理
----------------------------------------------------------------------
.. literalinclude:: /_sample/sympy/menelaus.py
   :language: python3

* 本当は数値的でないほうの座標で検証したかったが、
  私の環境では :code:`simplify(numer/denom)` が返って来なかった。
* 具体的な座標を与えた方の検証はうまくいく。

  .. code-block:: console 

     $ ./menelaous.py
     P= Point(-346.683333333333, -346.683333333333)
     Q= Point(170.682926829268, 170.682926829268)
     R= Point(-241.237623762376, -241.237623762376)
     numer= 41999675.9784931
     denom= 41999675.9784931
     1.00000000000000

チェバの定理
----------------------------------------------------------------------
.. literalinclude:: /_sample/sympy/ceva.py
   :language: python3

* 本当は数値的でないほうの座標で検証したかったが、
  私の環境では :code:`simplify(numer/denom)` が返って来なかった。
* 具体的な座標を与えた方の検証はうまくいく。

  .. code-block:: console 

     $ ./ceva.py
     P= Point(13.9279086822051, 228.152408889456)
     Q= Point(280.783950617284, 43.1975308641975)
     R= Point(104.14656234152, 529.558791567051)
     numer= 20374326.3842940
     denom= 20374326.3842940
     1.00000000000000

方べきの定理
----------------------------------------------------------------------
具体的な座標を与えないとどうも上手くいかないようなので、数値計算に切り替えて様子見だ。
さらに難易度？を落とし、方べきの定理を再現してみたい。

.. literalinclude:: /_sample/sympy/circle_power.py
   :language: python3

円を単位円に固定する代わり、円周上の 4 点をランダムにとり、
それらを結ぶ 2 弦の交点に対する方べきの定理を検証しよう。

.. code-block:: console

   $ ./circle_power.py
   PA * PB = 0.245325501000245
   PC * PD = 0.245325501000245
   $ ./circle_power.py
   PA * PB = 0.0519999915840500
   PC * PD = 0.0519999915840500

----

.. todo::

   * プロットは実現したい。
   * 上の例で :code:`distance` を多用しているが、
     値一致テストの目的なら :code:`dot` を用いるのが常識的か。
   * もっとサンプルを作りたい。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt
