======================================================================
Chapter 21. Connectors
======================================================================

.. contents::

Inkscape には木構造グラフを描くための描画要素が用意されている：

   Connectors are lines that “connect” objects, useful for drawing organization
   charts or flow diagrams. Connectors remain connected even if the objects they
   connect are moved. Individual objects can be given an *avoid* property that
   causes connectors to be routed dynamically around them.

コネクターの描画が間違っている、追随しないと思ったらそれに接続しているオブジェク
トを小突くといい：

   Nudging a connected object up and down may cause the connectors to be
   rerouted correctly.

Creating Connectors
======================================================================

*Connector Tool* の起動方法は次のいずれか：

* :guilabel:`Toolbox` からアイコンをクリックする
* :kbd:`Ctrl` + :kbd:`F2` を押すか :kbd:`O` を押す

配線操作は次のように、オブジェクト同士に関係を指示する自然なものだ：

   Then click-drag the mouse from one point on the canvas to another. When the
   pointer is over an object, a Connection handle is shown in the center of the
   object. Beginning or ending the click-drag on one of these handles will
   attach the connector to the corresponding object. Alternatively, one can
   begin a connector by clicking on an empty point on the canvas or on a
   Connection handle and end the connector by a second click. Connectors are
   drawn so they begin on the edge of the attached object.

テキストにはコネクターが直には付かない。なぜかというと：

   This facilitates connections between boxes that frame text.

この振る舞いを :guilabel:`Preferences` ダイアログで変更することもできる。

Modifying Connectors
======================================================================

   Connectors can be modified several ways. The connectors can be connected or
   disconnected from objects, the connector line style can be changed, and the
   routing of the connectors can be changed.

興味があるのは配線変更だろう。

Connecting and Disconnecting
----------------------------------------------------------------------

コネクターの端点を一時的に背景に固定することができるようだ：

   A connector can be disconnected from an object by dragging an end point away
   from the object. To do so, first select the connector by clicking on it. Two
   handles should appear at each end. Drag one of the handles away. The handle
   will then be fixed to the background.

改めてオブジェクトにコネクターを接続し直すには：

   To reconnect a handle (or to move a handle from one object to another), drag
   the handle to the connection handle that will appear at the center of the
   object when the cursor is above the object.

Line Style
----------------------------------------------------------------------

   All the normal line (path) styles can be applied to a connector, including
   adding arrows or using a dashed line.

方法はいつもの :guilabel:`Fill and Stroke` ダイアログ利用でよい。

   Changing the :guilabel:`Cap` style to :guilabel:`Square Cap` may improve the
   look of a connection to a stroked object.

コネクターを使うときはオブジェクトの輪郭線をなしにするか実線にするかにしたほうが
無難なようだ。

Routing
----------------------------------------------------------------------

*Connector Tool* UI を見ていく。最初の二つのボタンは本書と Inkscape 1.2 で順序が
入れ替わっている。

:guilabel:`Make connectors avoid selected objects`
   オブジェクトを選択した状態でこのボタンが押されると、配線時にオブジェクトをま
   たがるコネクターが禁止されるようにマークされる。
:guilabel:`Make connectors ignore selected objects`
   オブジェクトを選択した状態でこのボタンが押されると、配線時にオブジェクトをま
   たがるコネクターが許可するようにマークされる。
:guilabel:`Make connectors orthogonal or polyline`
   水平線と垂直線のみの配線コネクターのオンオフを切り替える。コネクターを選択し
   ているときにこのボタンを押すと、コネクターが他のモードに切り替わる。
:guilabel:`Curvature`
   コネクターの直線二箇所間の曲率を制御する値。
:guilabel:`Spacing`
   コネクターが通過しないオブジェクト周辺の空き具合を制御する値。
:guilabel:`Nicely arrange selected connector network`
   このオプションがよくわからない。

      The placement is based on the Kamada-Kawai_ algorithm that treats the
      connectors as springs so that the distance between the connector handles
      are evenly spaced.

   ハンドルを等間隔にしたいときに試すか。

      Only selected objects and connectors will be changed (use :kbd:`Ctrl` +
      :kbd:`A` to select all objects and connectors).

   選択的にオプションを採用することができる。

      The following parameters/options control this layout.

:guilabel:`Length`
   オブジェクトとコネクターを自動的に再配置する際のコネクターの理想的な長さを制
   御する値。
:guilabel:`Make connectors with end-markers (arrows) point downwards`
   端点マーカー（矢印など）を持つコネクターが下を向くようにするオプションのオン
   オフを切り替える。
:guilabel:`Do not allow overlapped shapes`
   移動時にオブジェクトが重ならないようにする要件のオンオフを切り替える。

.. _Kamada-Kawai: https://www.boost.org/libs/graph/doc/kamada_kawai_spring_layout.html
