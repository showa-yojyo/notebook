======================================================================
Entity Relationship Diagrams
======================================================================

.. contents::
   :depth: 2

..

  Mermaid can render ER diagrams

  .. mermaid::
     :align: center

     ---
     title: Order example
     ---
     erDiagram
         CUSTOMER ||--o{ ORDER : places
         ORDER ||--|{ LINE-ITEM : contains
         CUSTOMER }|..|{ DELIVERY-ADDRESS : uses

他の図式同様に、Markdown 式記法でタイトルを指定することが可能になった。

  Relationships between entities are represented by lines with end markers
  representing cardinality. Mermaid uses the most popular crow's foot notation.
  The crow's foot intuitively conveys the possibility of many instances of the
  entity that it connects to.

カラスの足の爪側のほうがインスタンスの複数存在性を示唆する。

  It can be useful to include attribute definitions on ER diagrams to aid
  comprehension of the purpose and meaning of entities. These do not necessarily
  need to be exhaustive; often a small subset of attributes is enough. Mermaid
  allows to be defined in terms of their *type* and *name*.

  .. code:: text

     erDiagram
      CUSTOMER ||--o{ ORDER : places
      CUSTOMER {
          string name
          string custNumber
          string sector
      }
      ORDER ||--|{ LINE-ITEM : contains
      ORDER {
          int orderNumber
          string deliveryAddress
      }
      LINE-ITEM {
          string productCode
          int quantity
          float pricePerUnit
      }

  When including attributes on ER diagrams, you must decide whether to include
  foreign keys as attributes. This probably depends on how closely you are trying
  to represent relational table structures. If your diagram is a *logical* model
  which is not meant to imply a relational implementation, then it is better to
  leave these out because the associative relationships already convey the way
  that entities are associated.

ER 図に属性を記載するかどうかを決定するのは、図式で説明したいことが設計と実装の
どちらにより軸足を置くのかということか。

ここまでが ER 図が何であるかについての記述だ。名前は大文字で記すことや、単数
形名詞であることなどを語っている。

Syntax
======================================================================

Entities and Relationships
----------------------------------------------------------------------

  Mermaid syntax for ER diagrams is compatible with PlantUML, with an extension
  to label the relationship. Each statement consists of the following parts:

  .. code:: text

     <first-entity> [<relationship> <second-entity> : <relationship-label>]

  Where:

  * ``first-entity`` is the name of an entity. Names must begin with an alphabetic
    character and may also contain digits, hyphens, and underscores.
  * ``relationship`` describes the way that both entities inter-relate. See below.
  * ``second-entity`` is the name of the other entity.
  * ``relationship-label`` describes the relationship from the perspective of the
    first entity.

ER 図に関しては PlantUML 用に書いた図式を Mermaid で描画できるということになる。
関係性にラベルを付加した場合、逆にその Mermaid コードを PlantUML が処理すること
は不能ということだ。

  For example:

  .. code:: text

         PROPERTY ||--|{ ROOM : contains

  This statement can be read as *a property contains one or more rooms, and a
  room is part of one and only one property*. You can see that the label here
  is from the first entity's perspective: a property contains a room, but a
  room does not contain a property. When considered from the perspective of the
  second entity, the equivalent label is usually very easy to infer. (Some ER
  diagrams label relationships from both perspectives, but this is not
  supported here, and is usually superfluous).

上記の関係 ``contains`` は対称律を満たさないと解釈するのだ。反対に ``ROOM`` から
すれば ``PROPERTY`` は be contained という関係性があると自然に推論できる。
両側の立場から関係性を示すラベルがある ER 図もあるが、通常は余計だ。

  Only the ``first-entity`` part of a statement is mandatory. This makes it
  possible to show an entity with no relationships, which can be useful during
  iterative construction of diagrams. If any other parts of a statement are
  specified, then all parts are mandatory.

関係性のない実体に意味はある。

Relationship Syntax
----------------------------------------------------------------------

  The relationship part of each statement can be broken down into three
  sub-components:

  * the cardinality of the first entity with respect to the second,
  * whether the relationship confers identity on a 'child' entity
  * the cardinality of the second entity with respect to the first

関係性自身にも属性があるわけだ。まずは cardinarity から述べられる：

  Cardinality is a property that describes how many elements of another entity
  can be related to the entity in question. In the above example a ``PROPERTY``
  can have one or more ``ROOM`` instances associated to it, whereas a ``ROOM``
  can only be associated with one ``PROPERTY``.

とあるのだが、集合の要素数というよりは「一対一」「一対他」などを表すクラスだと解
釈するほうが理解しやすい。

  In each cardinality marker there are two characters. The outermost character
  represents a maximum value, and the innermost character represents a minimum
  value. The table below summarises possible cardinalities.

  ============ ============= =============================
  Value (left) Value (right) Meaning
  ============ ============= =============================
  ``|o``       ``o|``        Zero or one
  ``||``       ``||``        Exactly one
  ``}o``       ``o{``        Zero or more (no upper limit)
  ``}|``       ``|{``        One or more (no upper limit)
  ============ ============= =============================

UML と比較するとこの多重度の表記法はピンと来ない。覚えにくい。

Identification
----------------------------------------------------------------------

関係の分類について重要なことを説明している。

  Relationships may be classified as either *identifying* or *non-identifying*
  and these are rendered with either solid or dashed lines respectively. This is
  relevant when one of the entities in question can not have independent
  existence without the other.

Class diagram の用語でいう composition と aggrigation の概念と類似しているように
思う。エッジのスタイルで見分ける。実線で描かれている関係は、両側の実体は同時にし
か存在しないと解釈できる。

  For example a firm that insures people to drive cars might need to store data
  on ``NAMED-DRIVER`` s. In modelling this we might start out by observing that
  a ``CAR`` can be driven by many ``PERSON`` instances, and a ``PERSON`` can
  drive many ``CAR`` s - both entities can exist without the other, so this is a
  non-identifying relationship that we might specify in Mermaid as:
  ``PERSON}|..|{CAR : "driver"``. Note the two dots in the middle of the
  relationship that will result in a dashed line being drawn between the two
  entities.

車の保険のことは全く知らないので何とも言えないが、この状況は一般的なのか。

  But when this many-to-many relationship is resolved into two one-to-many
  relationships, we observe that a ``NAMED-DRIVER`` cannot exist without both a
  ``PERSON`` and a ``CAR`` - the relationships become identifying and would be
  specified using hyphens, which translate to a solid line:

  .. code:: text

     erDiagram
         CAR ||--o{ NAMED-DRIVER : allows
         PERSON ||--o{ NAMED-DRIVER : is

多対多を一対多に分解したい。これにより相方がないインスタンスというものがなくな
る。

Attributes
----------------------------------------------------------------------

  Attributes can be defined for entities by specifying the entity name followed by
  a block containing multiple ``type name`` pairs, where a block is delimited by
  an opening ``{`` and a closing ``}``. For example:

  .. code:: text

     erDiagram
         CAR ||--o{ NAMED-DRIVER : allows
         CAR {
             string registrationNumber
             string make
             string model
         }
         PERSON ||--o{ NAMED-DRIVER : is
         PERSON {
             string firstName
             string lastName
             int age
         }

  The attributes are rendered inside the entity boxes.

RDB におけるテーブル設計を意識した記法だ。

Attribute Keys and Comments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

主キー、外部キー、一意キーも使える。

  Attributes may also have a ``key`` or comment defined. Keys can be ``PK``,
  ``FK`` or ``UK``, for Primary Key, Foreign Key or Unique Key.

キーを複合させても構わない：

  To specify multiple key constraints on a single attribute, separate them with
  a comma (e.g. ``PK, FK``).

コメントはいつもの ``%%`` ではなく、属性宣言の終端に文字列のようにして記す：

  And a ``comment`` is defined by double quotes at the end of an attribute.
  Comments themselves cannot have double-quote characters in them.

本書ではやや実践的な例を挙げている：

  .. code:: text

     erDiagram
         CAR ||--o{ NAMED-DRIVER : allows
         CAR {
             string registrationNumber PK
             string make
             string model
             string[] parts
         }
         PERSON ||--o{ NAMED-DRIVER : is
         PERSON {
             string driversLicense PK "The license #"
             string(99) firstName "Only 99 characters are allowed"
             string lastName
             string phone UK
             int age
         }
         NAMED-DRIVER {
             string carRegistrationNumber PK, FK
             string driverLicence PK, FK
         }
         MANUFACTURER only one to zero or more CAR : makes

Other Things
----------------------------------------------------------------------

  * If you want the relationship label to be more than one word, you must use
    double quotes around the phrase
  * If you don't want a label at all on a relationship, you must use an empty
    double-quoted string

ラベル文字列に関する、わりと自明な制限だ。

Styling
======================================================================

Config options
----------------------------------------------------------------------

単純に、``fill`` と ``stroke`` という、色指定のための二種類しかない。

Classes used
----------------------------------------------------------------------

CSS クラスセレクターの形式でユーザーが独自にスタイリングを指定することが可能だ。
`Wikipedia の ER 図のページ
<https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model>`__ にあるよう
な図式を描画したいときにこれらを指定する。

セレクター名一覧は本書参照。
