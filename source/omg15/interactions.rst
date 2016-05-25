======================================================================
17 Interactions
======================================================================
UML 2.5 pp. 563-636 に関するノート。

.. contents:: ノート目次

17.1 Summary
======================================================================
.. todo:: ノート作成

17.1.1 Overview
----------------------------------------------------------------------

17.1.2 Basic trace model
----------------------------------------------------------------------

17.1.3 Partial ordering constraints on valid and invalid traces
----------------------------------------------------------------------

17.1.4 Interaction Diagram Variants
----------------------------------------------------------------------

17.2 Interactions
======================================================================
.. todo:: ノート作成

17.2.1 Summary
----------------------------------------------------------------------

17.2.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 17.1 Interactions

17.2.3 Semantics
----------------------------------------------------------------------

17.2.4 Notation
----------------------------------------------------------------------
* Figure 17.2 Overlapping ExecutionSpecifications

17.2.5 Examples
----------------------------------------------------------------------
* Figure 17.3 An example of an Interaction in the form of a Sequence Diagram
* Figure 17.4 OccurrenceSpecification
* Figure 17.5 Sequence Diagram with time and timing concepts

17.3 Lifelines
======================================================================
.. todo:: ノート作成

17.3.1 Summary
----------------------------------------------------------------------

17.3.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 17.6 Lifelines

17.3.3 Semantics
----------------------------------------------------------------------

17.3.4 Notation
----------------------------------------------------------------------

17.3.5 Examples
----------------------------------------------------------------------

17.4 Messages
======================================================================
.. todo:: ノート作成

17.4.1 Summary
----------------------------------------------------------------------

17.4.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 17.7 Messages

17.4.3 Semantics
----------------------------------------------------------------------

17.4.4 Notation
----------------------------------------------------------------------
* Figure 17.8 DestructionOccurrenceSpecification symbol

17.4.5 Examples
----------------------------------------------------------------------

17.5 Occurrences
======================================================================
.. todo:: ノート作成

17.5.1 Summary
----------------------------------------------------------------------

17.5.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 17.9 Occurrences

17.5.3 Semantics
----------------------------------------------------------------------

17.5.4 Notation
----------------------------------------------------------------------

17.5.5 Examples
----------------------------------------------------------------------
* Figure 17.10 Example showing GeneralOrdering in a sequence diagram

17.6 Fragments
======================================================================
.. todo:: ノート作成

17.6.1 Summary
----------------------------------------------------------------------

17.6.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 17.11 Fragments

17.6.3 Semantics
----------------------------------------------------------------------

17.6.4 Notation
----------------------------------------------------------------------

17.6.5 Examples
----------------------------------------------------------------------
* Figure 17.12 Critical Region
* Figure 17.13 Loop CombinedFragment
* Figure 17.14 CombinedFragment
* Figure 17.15 Continuation
* Figure 17.16 Continuation interpretation
* Figure 17.17 Ignore, consider, assert with StateInvariants

17.7 Interaction Uses
======================================================================
.. todo:: ノート作成

17.7.1 Summary
----------------------------------------------------------------------

17.7.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 17.18 InteractionUses

17.7.3 Semantics
----------------------------------------------------------------------

17.7.4 Notation
----------------------------------------------------------------------

17.7.5 Examples
----------------------------------------------------------------------
* Figure 17.19 InteractionUse
* Figure 17.20 InteractionUse with value return
* Figure 17.21 PartDecomposition - the decomposed part
* Figure 17.22 PartDecomposition - the decomposition
* Figure 17.23 Sequence Diagrams where two Lifelines refer to (...)
* Figure 17.24 Describing Collaborations and their binding

17.8 Sequence Diagrams
======================================================================
.. todo:: ノート作成

17.8.1 Sequence Diagram Notation
----------------------------------------------------------------------

17.8.2 Example Sequence Diagram
----------------------------------------------------------------------
* Figure 17.25 Overview of Metamodel elements of a Sequence Diagram

17.9 Communication Diagrams
======================================================================
.. todo:: ノート作成

17.9.1 Communication Diagram Notation
----------------------------------------------------------------------

17.9.2 Example Communication Diagram
----------------------------------------------------------------------
* Figure 17.26 Communication diagram

17.10 Interaction Overview Diagrams
======================================================================
.. todo:: ノート作成

17.10.1 Interaction Overview Diagram Notation
----------------------------------------------------------------------

17.10.2 Examples of Interaction Overview Diagrams
----------------------------------------------------------------------
* Figure 17.27 Interaction Overview Diagram representing a High Level Interaction diagram

17.11 Timing Diagrams
======================================================================
.. todo:: ノート作成

17.11.1 Timing Diagram Notation
----------------------------------------------------------------------

17.11.2 Examples of Timing Diagrams
----------------------------------------------------------------------
* Figure 17.28 A Lifeline for a discrete object
* Figure 17.29 Compact Lifeline with States
* Figure 17.30 Timing Diagram with more than one Lifeline and with Messages

17.12 Classifier Descriptions
======================================================================
機械生成による節。

.. 17.12.1 ActionExecutionSpecification [Class]
.. 17.12.2 BehaviorExecutionSpecification [Class]
.. 17.12.3 CombinedFragment [Class]
.. 17.12.4 ConsiderIgnoreFragment [Class]
.. 17.12.5 Continuation [Class]
.. 17.12.6 DestructionOccurrenceSpecification [Class]
.. 17.12.7 ExecutionOccurrenceSpecification [Class]
.. 17.12.8 ExecutionSpecification [Abstract Class]
.. 17.12.9 Gate [Class]
.. 17.12.10 GeneralOrdering [Class]
.. 17.12.11 Interaction [Class]
.. 17.12.12 InteractionConstraint [Class]
.. 17.12.13 InteractionFragment [Abstract Class]
.. 17.12.14 InteractionOperand [Class]
.. 17.12.15 InteractionOperatorKind [Enumeration]
.. 17.12.16 InteractionUse [Class]
.. 17.12.17 Lifeline [Class]
.. 17.12.18 Message [Class]
.. 17.12.19 MessageEnd [Abstract Class]
.. 17.12.20 MessageKind [Enumeration]
.. 17.12.21 MessageOccurrenceSpecification [Class]
.. 17.12.22 MessageSort [Enumeration]
.. 17.12.23 OccurrenceSpecification [Class]
.. 17.12.24 PartDecomposition [Class]
.. 17.12.25 StateInvariant [Class]

17.13 Association Descriptions
======================================================================
機械生成による節。

.. 17.13.1 A_action_actionExecutionSpecification [Association]
.. 17.13.2 A_action_interaction [Association]
.. 17.13.3 A_actualGate_interactionUse [Association]
.. 17.13.4 A_argument_interactionUse [Association]
.. 17.13.5 A_argument_message [Association]
.. 17.13.6 A_before_toAfter [Association]
.. 17.13.7 A_behavior_behaviorExecutionSpecification [Association]
.. 17.13.8 A_cfragmentGate_combinedFragment [Association]
.. 17.13.9 A_connector_message [Association]
.. 17.13.10 A_covered_coveredBy [Association]
.. 17.13.11 A_covered_events [Association]
.. 17.13.12 A_covered_stateInvariant [Association]
.. 17.13.13 A_decomposedAs_lifeline [Association]
.. 17.13.14 A_execution_executionOccurrenceSpecification [Association]
.. 17.13.15 A_finish_executionSpecification [Association]
.. 17.13.16 A_formalGate_interaction [Association]
.. 17.13.17 A_fragment_enclosingInteraction [Association]
.. 17.13.18 A_fragment_enclosingOperand [Association]
.. 17.13.19 A_generalOrdering_interactionFragment [Association]
.. 17.13.20 A_guard_interactionOperand [Association]
.. 17.13.21 A_invariant_stateInvariant [Association]
.. 17.13.22 A_lifeline_interaction [Association]
.. 17.13.23 A_maxint_interactionConstraint [Association]
.. 17.13.24 A_message_considerIgnoreFragment [Association]
.. 17.13.25 A_message_interaction [Association]
.. 17.13.26 A_message_messageEnd [Association]
.. 17.13.27 A_minint_interactionConstraint [Association]
.. 17.13.28 A_operand_combinedFragment [Association]
.. 17.13.29 A_receiveEvent_endMessage [Association]
.. 17.13.30 A_refersTo_interactionUse [Association]
.. 17.13.31 A_represents_lifeline [Association]
.. 17.13.32 A_returnValueRecipient_interactionUse [Association]
.. 17.13.33 A_returnValue_interactionUse [Association]
.. 17.13.34 A_selector_lifeline [Association]
.. 17.13.35 A_sendEvent_endMessage [Association]
.. 17.13.36 A_signature_message [Association]
.. 17.13.37 A_start_executionSpecification [Association]
.. 17.13.38 A_toBefore_after [Association]

.. include:: /_include/uml-refs.txt
