======================================================================
Chapter 15. Clipping and Masking
======================================================================

.. contents::

クリップとマスクはオブジェクトの見える部分を制限するという振る舞いが共通してい
る。では前者と後者の違いは何か：

   Clipping and masking are methods for restricting what part of an object (or
   *Group* of objects) is visible. For clipping, a *clipping path* defines the
   visible part of the object, while for masking, the *transparency* or
   *lightness* of one object determines the opacity of a second object. In both
   cases, the target object is not changed and can be unclipped or unmasked if
   needed.

どちらの操作もいつでもキャンセル可能であるというのは安心だ。

   Example of clipping and masking.

マスクには馴染みがないのでここで概要をつかみたい。暗い部分がより透明になるという
理解で今はいいことにする。

クリップまたはマスク対象のオブジェクトはいつでも編集可能だ：

   A clipped or masked object can be edited (transformed, style changed, nodes
   edited, etc.) while clipped or masked. Objects within a clipped or masked
   *Group* can also be moved relative to the clipping path or masking object if
   the *Group* is entered.

反対に、クリップまたマスクを定義するパスのほうも後から編集可能だ：

   The clipping or masking path can be edited without unclipping or unmasking.
   With the clipped or masked object selected and the *Node Tool* active, click
   on either the (clipping) or (masking) icons in the *Tool Controls*. New in
   v0.48: The clip or mask path and the object can be edited at the same time.
   (This only works if the mask path is an actual path and not a shape.)

複数オブジェクトが選択されたとき、クリップまたはマスク操作は個別に機能する。この
挙動を設定画面で変更できる：

   By default, Inkscape will clip or mask each object separately if several
   objects are selected. In the Clippaths and masks section of the Inkscape
   :guilabel:`Preferences` dialog you can change this to have Inkscape first
   group the objects before applying a single clip or mask.

既定値至上主義者でもこれに関しては設定を変更する可能性があるので、ノートにつづっ
ておく。

Clipping
======================================================================

クリップパスとして使えるものは、基本的には普通のオブジェクトが何でも使える：

   Any path, regular shape, or regular text object can be used as a clipping
   path.

クリップの設定と解除の方法をセットで習得する。設定時には関係オブジェクトをいっぺ
んに選択してコマンドを実行する。このとき、オブジェクト間の z-order が本質的だ：

   To clip an object (or *Group*), select both the object and the clipping path.
   The clipping path must be above the object to be clipped in z-order. Then use
   the :menuselection:`Object --> Clip --> Set` command.

クリップ解除を実行すると、設定直前の状態が復元されると期待していい：

   To unclip a clipped object, select the object and use the
   :menuselection:`Object --> Clip --> Release` command. The clipping path is
   then restored as a regular object, placed just above the formerly clipped
   object in z-order.

前述のとおり、複数オブジェクト（グループ）を対象にクリップすることも可能
だ。:abbr:`SVG` ファイルでの構成が述べられている：

   More than one object (or *Group*) can be clipped at the same time. Just
   follow the above instructions but include all the objects to be clipped in
   the selection (with the clipping path on top). Inkscape will store one copy
   of the clipping path in the ``<defs>`` section of the :abbr:`SVG` file for
   each clipped object; thus, the clipped objects can be edited separately.

クリップ済みオブジェクトの BB は、元オブジェクトの BB とクリッピングパスの BB の
$\cap$ となる。

   The bounding box of the clipped object is defined by the intersection of the
   bounding box of the unclipped object with the bounding box of the clipping
   path. (However, if an object inside a clipped *Group* is selected, the
   unclipped bounding box of that object will be displayed.)

クリップ済みグループの内部のオブジェクトを選択して、クリップ前の BB が表示されて
も混乱しないこと。

Masking
======================================================================

マスクの概要から。まず、マスクパスとなるオブジェクトは何でもいい。マスクパスで重
要なのは遮光度と明度も影響するという点にある：

   Any object can be used to mask another object. The opacity and lightness of
   the mask determines the opacity of the masked objects.

マスク済みオブジェクトで色が完全に発色する部分を理解する：

   A masked object will be fully opaque only at places that are: inside the mask
   path, where the mask has maximum lightness (i.e., white), and the mask has
   maximum *Alpha*.

反対に、完全に見えなくなる部分を理解する：

   * Regions with minimum lightness (i.e., black) will be fully transparent.
   * Regions with minimum Alpha (zero alpha) will be fully transparent.
   * Regions outside the mask will be fully transparent.

操作としては、マスク設定もマスク解除もクリップにおける対応物それぞれと同じだ：

   To mask an object (or *Group*), select both the object to be masked and the
   object to be used as a mask. The mask must be above the object to be masked
   in z-order. Then use the :menuselection:`Object --> Mask --> Set` command. To
   unmask a masked object, select the object and use the :menuselection:`Object
   --> Mask --> Release` command. The mask is then restored as a regular object
   and is placed just above the formerly masked object in z-order.

複数オブジェクトに対するマスクがあるときの :abbr:`SVG` ファイルでの表現もクリッ
プの事情と同様だ。

   The bounding box of the masked object is the same as that of the unmasked
   object.

とあるが、手許の Inkscape 1.2 ではそんなことはないように見える。
