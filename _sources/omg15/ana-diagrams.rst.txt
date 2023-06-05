======================================================================
Annex A: Diagrams
======================================================================

.. admonition:: 読者ノート

   現在ノート修正中。

* この付録では UML 図の一般的な特徴および、それらがどのように UML モデルとこの要
  素に関係するのかをを述べる。
* UML モデルはパッケージ、クラス、関連のような要素からなる。

  * 対応する UML 図は UML モデルの部分の図表による表現である。
  * UML 図はパスにより連結されるノードという UML モデルの要素を表現する図表要素
    を含む。

* Figure A.1 UML Diagram

  * 図のそれぞれには contents area がある。オプションとして、枠と表題があっても
    よい。

* 枠は矩形である。

  * 枠は図式化された要素が、例えばクラスやコンポーネントに対するポートや、状態機
    械上の出入口のような境界要素がある場合に主に用いられる。
  * 必要とされていない場合には、枠は省略することが許され、ツールによって与えられ
    た図の領域の境界によってほのめかされる。
  * 枠が省略された場合には表題も省略される。

* 図の contents area は図表の記号を含む。主な図表の記号は図の方を定義する。例え
  ば、クラス図とは contents area にある主な記号がクラス記号である図のことであ
  る。
* 表題は矩形の左上隅に置かれた名札（角を切り取られた矩形）に含まれた文字列であ
  る。
* 図の表題は包囲している名前空間の種類、名前、引数またはcontents area にある記号
  が表現する要素を所有しているモデル要素を表現する。

  * 図の contents area の要素のほとんどは名前空間で定義されたか、別のモデル要素
    が所有するモデル要素を表現する。

* Figure A.2 Class diagram of package P

  * パッケージ ``P`` のクラス図である。
  * クラス ``C1`` および ``C2`` はパッケージ ``P`` の名前空間内に定義されてい
    る。

* Figure A.3 Two diagrams of packages

  * 左の図は「パッケージ ``CP`` はパッケージ ``P`` を含む」ことを表している図表
    の記号があるパッケージ ``CP`` を表すパッケージ図である。
  * 右の図はこのパッケージ ``P`` を表すクラス図である。
  * 補足事項だが、左図のパッケージ記号はクラス記号も関連記号も含む必要はない。よ
    り現実にありそうなモデルでは、パッケージ記号には通常パッケージの名前だけがあ
    る。一方、パッケージを表すクラス図にはパッケージで定義されるクラスを表す記号
    がある。

* Figure A.4 A class diagram and a composite structure diagram

  * 左の図はパッケージ ``Cars`` を示すクラス図で、パッケージ ``Cars`` にはクラス
    ``Car`` を含むことを表現する記号がある。
  * 右の図はこのクラス ``Car`` を表す合成構造図である。
  * 左の図のクラス記号は区画内にクラスの構造を含める必要はない。より現実的なモデ
    ルでは、クラス記号には普通は単にクラス名があるだけであるが、一方クラスを表す
    合成構造図には合成構造を表す記号がある。

* UML 図は次の種類の枠名を表題の一部としてよい：

 * ``activity``
 * ``class``
 * ``component``
 * ``deployment``
 * ``interaction``
 * ``package``
 * ``state machine``
 * ``use case``

* 図の表題の種類を示す長い形式の名前に加えて、次の短縮形式もまた用いられる：

  * **act**
  * **cmp**
  * **dep**
  * **sd**
  * **pkg**
  * **stm**
  * **uc**

* Figure A.5 The taxonomy of structure and behavior diagrams

  * ちなみに taxonomy は classification の意。
  * 図の種類は構造図と挙動図の二種類に大別される。

* 構造図はシステム内のオブジェクトの静的な構造を示す。すなわち、時間を考慮しない
  仕様におけるそれらの要素を描写する。
* 挙動図はシステム内のオブジェクトの動的な挙動を示すもので、それらのメソッド、協
  調、活動、動静履歴を含んでいる。
* この分類は図の主要な種類に対する論理的な組織化を与えるものである。しかしなが
  ら、異なる種類の図を混ぜることを排除しない。
* UML 図のおのおのに含まれる構成要素は下に示す章で記述されている：

  * Activity Diagram - :doc:`./ch15-activities`
  * Class Diagram - :doc:`./ch11-structured-classifiers`
  * Communication Diagram - :doc:`./ch17-interactions`
  * Component Diagram - :doc:`./ch11-structured-classifiers`
  * Composite Structure Diagram - :doc:`./ch11-structured-classifiers`
  * Deployment diagram - :doc:`./ch19-deployments`
  * Interaction Overview Diagram - :doc:`./ch17-interactions`
  * Object Diagram - :doc:`./ch09-classification`
  * Package Diagram - :doc:`./ch12-packages`
  * Profile Diagram - :doc:`./ch12-packages`
  * State Machine Diagram - :doc:`./ch14-statemachines`
  * Sequence Diagram - :doc:`./ch17-interactions`
  * Timing Diagram - :doc:`./ch17-interactions`
  * Use Case Diagram - :doc:`./ch18-usecases`

.. include:: /_include/uml-refs.txt
