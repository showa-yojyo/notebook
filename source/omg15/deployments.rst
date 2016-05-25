======================================================================
19 Deployments
======================================================================
UML 2.5 pp. 651-666 に関するノート。

.. contents:: ノート目次

19.1 Summary
======================================================================
.. todo:: ノート作成

19.2 Deployments
======================================================================
.. todo:: ノート作成

19.2.1 Summary
----------------------------------------------------------------------

19.2.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 19.1 Deployments

19.2.3 Semantics
----------------------------------------------------------------------

19.2.4 Notation
----------------------------------------------------------------------

19.2.5 Examples
----------------------------------------------------------------------
* Figure 19.2 A visual representation of the deployment location of artifacts, (...)
* Figure 19.3 Alternative deployment representation of using a dependency (...)
* Figure 19.4 Textual list based representation of DeployedArtifacts
* Figure 19.5 DeploymentSpecification for an artifact (...)
* Figure 19.6 DeploymentSpecifications related to the DeployedArtifacts that they parameterize
* Figure 19.7 A DeploymentSpecification for a DeployedArtifact

19.3 Artifacts
======================================================================
.. todo:: ノート作成

19.3.1 Summary
----------------------------------------------------------------------

19.3.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 19.8 Artifacts

19.3.3 Semantics
----------------------------------------------------------------------

19.3.4 Notation
----------------------------------------------------------------------

19.3.5 Examples
----------------------------------------------------------------------
* Figure 19.9 An Artifact instance
* Figure 19.10 A Manifestation relationship between an Artifact and a Component

19.4 Nodes
======================================================================
.. todo:: ノート作成

19.4.1 Summary
----------------------------------------------------------------------

19.4.2 Abstract Syntax
----------------------------------------------------------------------
* Figure 19.11 Nodes

19.4.3 Semantics
----------------------------------------------------------------------

19.4.4 Notation
----------------------------------------------------------------------

19.4.5 Examples
----------------------------------------------------------------------
* Figure 19.12 Notation for a Device containing an ExecutionEnvironment and (...)
* Figure 19.13 Notation for a ExecutionEnvironment
* Figure 19.14 An instance of a Node
* Figure 19.15 CommunicationPath between AppServer with deployed Artifacts and a DBServer
* Figure 19.16 Deployed component Artifacts on a Node

19.5 Classifier Descriptions
======================================================================
機械生成による節。

.. 19.5.1 Artifact [Class]
.. 19.5.2 CommunicationPath [Class]
.. 19.5.3 DeployedArtifact [Abstract Class]
.. 19.5.4 Deployment [Class]
.. 19.5.5 DeploymentSpecification [Class]
.. 19.5.6 DeploymentTarget [Abstract Class]
.. 19.5.7 Device [Class]
.. 19.5.8 ExecutionEnvironment [Class]
.. 19.5.9 Manifestation [Class]
.. 19.5.10 Node [Class]

19.6 Association Descriptions
======================================================================
機械生成による節。

.. 19.6.1 A_configuration_deployment [Association]
.. 19.6.2 A_deployedArtifact_deploymentForArtifact [Association]
.. 19.6.3 A_deployedElement_deploymentTarget [Association]
.. 19.6.4 A_deployment_location [Association]
.. 19.6.5 A_manifestation_artifact [Association]
.. 19.6.6 A_nestedArtifact_artifact [Association]
.. 19.6.7 A_nestedNode_node [Association]
.. 19.6.8 A_ownedAttribute_artifact [Association]
.. 19.6.9 A_ownedOperation_artifact [Association]
.. 19.6.10 A_utilizedElement_manifestation [Association]

.. include:: /_include/uml-refs.txt
