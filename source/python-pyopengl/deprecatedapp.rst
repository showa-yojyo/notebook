======================================================================
クラス ``DeprecatedApp`` の実装
======================================================================
本稿で述べるクラス ``DeprecatedApp`` は、あくまでも過去に制作した
OpenGL 3.0 以前の機能で実装した PyOpenGL プログラムをリファクタリングするためのみに利用する。

もう少し具体的に説明すると、そのような古臭いソースコードが何十枚とある。
そこでの処理で似通った部分、例えば

* 描画処理開始直後のモデルビュー行列設定、
* ウィンドウサイズ変更時におけるビューポートの更新処理

は deprecated features を用いた実装方法で共通化したい。
言い換えると、OpenGL 3.0 以降の API と混在したコードを持ちたくないので、
クラス ``DeprecatedApp`` とクラス ``ModernApp`` のようなものを設けることにした。

.. contents::

クラス ``DeprecatedApp``
======================================================================
まずクラス全景を示す。

.. literalinclude:: /_sample/pyopengl/rc/deprecatedapp.py
   :language: python3

各メソッドはほぼすべてベースクラス ``AppBase`` からのオーバーライドとなるが、
その実装は OpenGL 3.0 以前の機能で実現する。

以下、特徴的なメソッドの説明をする。

メソッド ``__init__``
----------------------------------------------------------------------
.. literalinclude:: /_sample/pyopengl/rc/deprecatedapp.py
   :language: python3
   :lines: 25-31

* コンテキストバージョンを未指定の場合 ``(2, 1)`` にしておく。
  この値は、私の環境で認められているバージョン値の最大値で、 3.0 を超えない値、という意味だ。

* モデル回転用の行列として、メンバーデータ ``self.rotation_matrix`` を導入する。
  ベースクラスに同じ目的のメンバーデータ ``self.quat`` が既にあるので本来は要らないものだが、
  四元数オブジェクトから行列オブジェクトを生成する処理が高くつく可能性があるので、
  キャッシュ的に置く。

メソッド ``update_projection``
----------------------------------------------------------------------
.. literalinclude:: /_sample/pyopengl/rc/deprecatedapp.py
   :language: python3
   :lines: 41-47

ご覧のとおり、古典的な射影行列の設定処理である。

メソッド ``update_rotation``
----------------------------------------------------------------------
.. literalinclude:: /_sample/pyopengl/rc/deprecatedapp.py
   :language: python3
   :lines: 49-57

外部で計算した回転量を受け取って、メンバーデータ ``self.rotation_matrix`` に保存しておく。

クラス ``Quat`` のプロパティー ``transform`` で回転変換を表現する 3 次正規直交行列にアクセスする。
これをマウスドラッグ時の優位な移動が発生する都度、OpenGL 形式の 4 次行列に作り変える。

最後の転置処理は、この ``self.rotation_matrix`` を
``GL.glMultMatrixf`` にそのまま渡したいため行う。

メソッド ``set_modelview_matrix``
----------------------------------------------------------------------
.. literalinclude:: /_sample/pyopengl/rc/deprecatedapp.py
   :language: python3
   :lines: 59-67

メソッド ``set_modelview_matrix`` だけは、ベースクラスからのオーバーライドではない。
処理は古典的なモデルビュー行列の適用である。

造りが悪いのだが、サブクラスのメソッド ``do_render`` からの呼び出しを想定している。
その際には ``GL.glMatrixMode(GL.GL_MODELVIEW)`` を伴う。

.. include:: /_include/pyopengl-refs.txt
