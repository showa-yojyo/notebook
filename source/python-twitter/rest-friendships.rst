======================================================================
ページ名未定 (friendships)
======================================================================
本節では friendships 系 REST API について記す。

.. contents::

POST friendships/create
======================================================================

.. literalinclude:: /_sample/ptt/friendships-create.py
   :language: python3

* [1]
* [2]

次に実行例を示す。

.. code-block:: console

   $ ./friendships-create.py

POST friendships/destroy
======================================================================

.. literalinclude:: /_sample/ptt/friendships-destroy.py
   :language: python3

* [1]
* [2]

次に実行例を示す。

.. code-block:: console

   $ ./friendships-destroy.py

GET friendships/incoming
======================================================================

.. literalinclude:: /_sample/ptt/friendships-incoming.py
   :language: python3

* [1]
* [2]

次に実行例を示す。

.. code-block:: console

   $ ./friendships-incoming.py

GET friendships/lookup
======================================================================

.. literalinclude:: /_sample/ptt/friendships-lookup.py
   :language: python3

* [1]
* [2]

次に実行例を示す。

.. code-block:: console

   $ ./friendships-lookup.py

GET friendships/no_retweets/ids
======================================================================

.. literalinclude:: /_sample/ptt/friendships-no_retweets-ids.py
   :language: python3

* [1]
* [2]

次に実行例を示す。

.. code-block:: console

   $ ./friendships-no_retweets-ids.py

GET friendships/outgoing
======================================================================

.. literalinclude:: /_sample/ptt/friendships-outgoing.py
   :language: python3

* [1]
* [2]

次に実行例を示す。

.. code-block:: console

   $ ./friendships-outgoing.py

GET friendships/show
======================================================================

.. literalinclude:: /_sample/ptt/friendships-show.py
   :language: python3

* [1]
* [2]

次に実行例を示す。

.. code-block:: console

   $ ./friendships-show.py

POST friendships/update
======================================================================

.. literalinclude:: /_sample/ptt/friendships-update.py
   :language: python3

* [1]
* [2]

次に実行例を示す。

.. code-block:: console

   $ ./friendships-update.py


.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-twitter.txt
