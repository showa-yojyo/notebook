======================================================================
Annex A: Diagrams
======================================================================

   This annex describes the general properties of UML diagrams and how they
   relate to a UML (repository) model and to elements of this. It also
   introduces the different diagram types of UML.

UML モデルはパッケージ、クラス、関連のような要素からなる。対応する UML 図式はそ
のモデルの部分を模式的に表現したものだ。UML 図には UML モデル内の要素を表現する
図像的な要素が含まれる。

   Figure A.1 UML Diagram

図のそれぞれには内容域がある。オプションとして、この図のように枠と見出しを持たせ
てもよい。

枠は矩形だ。枠は図式化された要素が、クラスや部品に対するポートや、状態機械の出入
口のような、図式の要素に図像的境界要素がある場合に主に用いられる。

必要とされていない場合には、枠は省略することが許され、ツールが与える図式領域の境
界で暗示される。枠が省略された場合には見出しも省略される。

   The diagram contents area contains the graphical symbols; the primary
   graphical symbols define the type of the diagram (e.g., a class diagram is a
   diagram where the primary symbols in the contents area are class symbols).

見出しは矩形の左上隅に置かれた名札（角を切り取られた矩形）に含まれる文字列だ。構
文は次のとおり：

.. code:: bnf

   [<kind>] <name> [<parameters>]

図式の見出しは名前空間が取り囲んでいる種類、名前、引数、内容域にある記号が表現す
る要素を所有するモデル要素を表現する。

   Most elements of a diagram contents area represent model elements that are
   defined in the namespace or are owned by another model element.

   Figure A.2 Class diagram of package P

パッケージ ``P`` のクラス図だ。クラス ``C1`` および ``C2`` はパッケージ ``P`` の
名前空間内に定義されている。

   Figure A.3 Two diagrams of packages

左の図は「パッケージ ``CP`` はパッケージ ``P`` を含む」ことを表している図表の記
号があるパッケージ ``CP`` を表すパッケージ図だ。

右の図はこのパッケージ ``P`` を表すクラス図だ。

現実的なモデルでは、パッケージ記号にはパッケージ名しか記述せず、パッケージに対す
るクラス図にはパッケージで定義されるクラスのクラス記号を記述するのがふつうだ。

   Figure A.4 A class diagram and a composite structure diagram

左の図はパッケージ ``Cars`` を示すクラス図で、パッケージ ``Cars`` にはクラス
``Car`` を含むことを表現する記号がある。

右の図はこのクラス ``Car`` を表す複合構造図だ。

左の図のクラス記号は区画内にクラスの構造を含める必要はない。より現実的なモデルで
は、クラス記号には普通は単にクラス名があるだけであるが、一方クラスを表す複合構造
図には複合構造を表す記号がある。

UML 図では見出しの一部として次の種類の枠名をつけてよい：

* ``activity``
* ``class``
* ``component``
* ``deployment``
* ``interaction``
* ``package``
* ``state machine``
* ``use case``

図式の見出し型の長い形式の名前に加えて、次の短縮形もまた用いられる：

* **act**
* **cmp**
* **dep**
* **sd**
* **pkg**
* **stm**
* **uc**

..

   Figure A.5 The taxonomy of structure and behavior diagrams

図の種類は構造図と挙動図の二種類に大別される。

構造図はシステム内のオブジェクトの静的な構造を示す。すなわち、時間とは無関係な仕
様の要素を描写する。

   The elements in a structure diagram represent the meaningful concepts of an
   application, and may include abstract, real-world and implementation
   concepts.

挙動図はシステム内のオブジェクトの動的な挙動を示すもので、それらのメソッド、協
調、活動、状態履歴などを含む。システムの動的な挙動は時間経過に伴うシステムの一連
の変化として記述することが可能だ。

この分類法はさまざまな種類の図式を論理的に整理するものだ。しかしながら、例えば内
部構造の入れ子になった状態機械を表示する場合などのように、異なる種類の図式を混在
することを排除するものではない。そうすると、さまざまな種類の図式の境界は厳密には
強要されない。

UML 図のおのおのに含まれる構成要素は次に示す章で記述されている：

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
