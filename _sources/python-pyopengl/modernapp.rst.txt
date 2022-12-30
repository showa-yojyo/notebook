======================================================================
クラス ``ModernApp`` の実装
======================================================================

本稿で採り上げるクラス ``ModernApp`` こそが、今後制作する PyOpenGL プログラムの
「ベース」となるものだ。 OpenGL 3.0 以降の新機能と、古参かつ現役の機能とから何か
を描画するためのクラスだ。

.. contents::

.. warning::

   :doc:`./program-manager` 参照。

クラス ``ModernApp``
======================================================================

まずクラス全景を示す。

.. literalinclude:: /_sample/pyopengl/modernapp.py
   :language: python3

各メソッドはすべてベースクラス ``AppBase`` からのオーバーライドとなる。以下、主
要メソッドの実装を解説する。

メソッド ``init_program``
----------------------------------------------------------------------

.. literalinclude:: /_sample/pyopengl/modernapp.py
   :language: python3
   :lines: 31-39

サブクラスでオーバーライドされているメソッド ``get_shader_sources`` を呼び出し、
シェーダータイプとシェーダーコードのペアからなる辞書オブジェクトを受け取り、クラ
ス ``ProgramManager`` のオブジェクトを生成し、それに初期化処理を委ねる。

詳細は :doc:`program-manager` を参照。

メソッド ``init_transform``
----------------------------------------------------------------------

.. literalinclude:: /_sample/pyopengl/modernapp.py
   :language: python3
   :lines: 41-53

初回にシェーダーオブジェクトに行列データを送信する処理である。モデル回転用行列、
カメラ用行列、投影用行列すべてを設定する。

* 関数 ``lookat`` については :doc:`transform` 参照。
* ``GL.glUniformMatrix4fv`` の転置フラグを ON にすることで、OpenGL に行列の
  column-major 化をさせる。

言い忘れたが、頂点シェーダーでの各行列の名前は次のとおりとする：

.. code:: glsl

   #version 330 core

   uniform mat4 camera;
   uniform mat4 projection;
   uniform mat4 rotation;

   ...

決め打ちなのはいかにも手抜きだが、当面これでいく。

メソッド ``update_projection``
----------------------------------------------------------------------

.. literalinclude:: /_sample/pyopengl/modernapp.py
   :language: python3
   :lines: 59-73

直接呼び出すというよりは、ベースクラスでウィンドウサイズ変更時に呼び出すメソッド
だ。

* 関数 ``perspective`` については :doc:`transform` 参照。

メソッド ``update_rotation``
----------------------------------------------------------------------

.. literalinclude:: /_sample/pyopengl/modernapp.py
   :language: python3
   :lines: 75-90

前半部はほぼ :doc:`deprecatedapp` でのオーバーライドと同じだ。外部で計算した回転
量を受け取って、直接メンバーデータ ``self.quat`` に保存しておく。後半はシェー
ダーオブジェクトへの行列送信である。

メソッド ``cleanup``
----------------------------------------------------------------------

.. literalinclude:: /_sample/pyopengl/modernapp.py
   :language: python3
   :lines: 92-96

シェーダー関連の後始末を行う。詳細は :doc:`program-manager` を参照。

なお、サブクラスではこのメソッドをオーバーライドし、この処理に加えて、バッファー
オブジェクトやテクスチャーオブジェクトの破棄をすることになる。

.. include:: /_include/python-refs-vision.txt
