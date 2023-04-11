======================================================================
Requirement Diagram
======================================================================

.. contents::
   :depth: 2

..

  A Requirement diagram provides a visualization for requirements and their
  connections, to each other and other documented elements. The modeling specs
  follow those defined by SysML v1.6.

SysML は UML と同じく OMG が策定する言語仕様の一つだ。

  Rendering requirements is straightforward.

  .. mermaid::./r-first.mmd
     :align: center
  .. literalinclude::./r-first.mmd

この図式だけ見れば「要素 ``test_entity`` は要求 ``test_req`` を満足する」と読め
る。

Syntax
======================================================================

  There are three types of components to a requirement diagram: requirement,
  element, and relationship.

  The grammar for defining each is defined below. Words denoted in angle
  brackets, such as ``<word>``, are enumerated keywords that have options
  elaborated in a table. ``user_defined_...`` is use in any place where user
  input is expected.

  An important note on user text: all input can be surrounded in quotes or not.
  For example, both ``Id: "here is an example"`` and ``Id: here is an example``
  are both valid. However, users must be careful with unquoted input. The parser
  will fail if another keyword is detected.

諸注意は自然なものだ。特段問題はない。

Requirement
-----------------------------------------------------------------------

  A requirement definition contains a requirement ``type``, ``name``, ``id``,
  ``text``, ``risk``, and ``verification`` method. The syntax follows:

  .. code:: text

     <type> user_defined_name {
         id: user_defined_id
         text: user_defined text
         risk: <risk>
         verifymethod: <method>
     }

おそらくこれらの要素全てを指定する必要がある。

  Type, risk, and method are enumerations defined in SysML.

  +---------------------+---------------------------------------+
  | Keyword             | Options                               |
  +=====================+=======================================+
  | Type                | requirement, functionalRequirement,   |
  |                     | interfaceRequirement,                 |
  |                     | performanceRequirement,               |
  |                     | physicalRequirement, designConstraint |
  +---------------------+---------------------------------------+
  | Risk                | Low, Medium, High                     |
  +---------------------+---------------------------------------+
  | VerificationMethod  | Analysis, Inspection, Test,           |
  |                     | Demonstration                         |
  +---------------------+---------------------------------------+

大文字小文字は区別されないようだ。

Element
-----------------------------------------------------------------------

  An element definition contains an element name, type, and document reference.
  These three are all user defined. The element feature is intended to be
  lightweight but allow requirements to be connected to portions of other
  documents.

  .. code:: text

     element user_defined_name {
         type: user_defined_type
         docref: user_defined_ref
     }

おそらくこれらの要素全てを指定する必要がある。

Relationship
-----------------------------------------------------------------------

  Relationships are comprised of a source node, destination node, and
  relationship type.

  Each follows the definition format of

  .. code:: text

     {name of source} - <type> -> {name of destination}

  or

  .. code:: text

     {name of destination} <- <type> - {name of source}

実際は左向きか右向きかを一つの図式の中で統一して用いるのが整合性があり良いと考え
られる。

  "name of source" and "name of destination" should be names of requirement or
  element nodes defined elsewhere.

  A relationship type can be one of contains, copies, derives, satisfies,
  verifies, refines, or traces.

英語の SVO を意識する。

  Each relationship is labeled in the diagram.

矢印の線部分に重なり合うようにラベルが示される。

Larger Example
======================================================================

  This example uses all features of the diagram.

  .. mermaid::./r-all-features.mmd
     :align: center
  .. literalinclude::./r-all-features.mmd

内容が実践的だともっとありがたい。
