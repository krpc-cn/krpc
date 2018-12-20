.. currentmodule:: SpaceCenter

与零件交互
======================

以下示例演示了使用:ref:`python-api-parts`功能
来完成各种任务。有关特定主题的更多详细资料也可以在
API文档中找到:

.. tabs::

   .. tab:: C#

      * :ref:`csharp-api-parts-trees-of-parts`
      * :ref:`csharp-api-parts-attachment-modes`
      * :ref:`csharp-api-parts-fuel-lines`
      * :ref:`csharp-api-parts-staging`

   .. tab:: C++

      * :ref:`cpp-api-parts-trees-of-parts`
      * :ref:`cpp-api-parts-attachment-modes`
      * :ref:`cpp-api-parts-fuel-lines`
      * :ref:`cpp-api-parts-staging`

   .. tab:: C

      * :ref:`cnano-api-parts-trees-of-parts`
      * :ref:`cnano-api-parts-attachment-modes`
      * :ref:`cnano-api-parts-fuel-lines`
      * :ref:`cnano-api-parts-staging`

   .. tab:: Java

      * :ref:`java-api-parts-trees-of-parts`
      * :ref:`java-api-parts-attachment-modes`
      * :ref:`java-api-parts-fuel-lines`
      * :ref:`java-api-parts-staging`

   .. tab:: Lua

      * :ref:`lua-api-parts-trees-of-parts`
      * :ref:`lua-api-parts-attachment-modes`
      * :ref:`lua-api-parts-fuel-lines`
      * :ref:`lua-api-parts-staging`

   .. tab:: Python

      * :ref:`python-api-parts-trees-of-parts`
      * :ref:`python-api-parts-attachment-modes`
      * :ref:`python-api-parts-fuel-lines`
      * :ref:`python-api-parts-staging`

展开所有降落伞
------------------------

有时事情会变得非常糟糕。以下代码通过展开所有的降落伞来
尽可能地拯救您的Kerbals:

.. tabs::

   .. tab:: C#

      .. literalinclude:: /scripts/tutorials/parts/DeployParachutes.cs
         :language: csharp

   .. tab:: C++

      .. literalinclude:: /scripts/tutorials/parts/DeployParachutes.cpp
         :language: cpp

   .. tab:: C

      .. literalinclude:: /scripts/tutorials/parts/DeployParachutes.c
         :language: c

   .. tab:: Java

      .. literalinclude:: /scripts/tutorials/parts/DeployParachutes.java
         :language: java

   .. tab:: Lua

      .. literalinclude:: /scripts/tutorials/parts/DeployParachutes.lua
         :language: lua

   .. tab:: Python

      .. literalinclude:: /scripts/tutorials/parts/DeployParachutes.py
         :language: python

对接口的'从此处控制'
-------------------------------------

以下代码会寻找一个标准尺寸的Clamp-O-Tron对接口,
然后从它这控制飞船:

.. tabs::

   .. tab:: C#

      .. literalinclude:: /scripts/tutorials/parts/ControlFromHere.cs
         :language: csharp

   .. tab:: C++

      .. literalinclude:: /scripts/tutorials/parts/ControlFromHere.cpp
         :language: cpp

   .. tab:: C

      .. literalinclude:: /scripts/tutorials/parts/ControlFromHere.c
         :language: c

   .. tab:: Java

      .. literalinclude:: /scripts/tutorials/parts/ControlFromHere.java
         :language: java

   .. tab:: Lua

      .. literalinclude:: /scripts/tutorials/parts/ControlFromHere.lua
         :language: lua

   .. tab:: Python

      .. literalinclude:: /scripts/tutorials/parts/ControlFromHere.py
         :language: python

综合比冲量
-------------------------

以下脚本计算当前火箭上激活并且正在燃烧的引擎的综合比冲量。
这里是计算方法的详细信息:
https://wiki.kerbalspaceprogram.com/wiki/Specific_impulse#Multiple_engines

.. tabs::

   .. tab:: C#

      .. literalinclude:: /scripts/tutorials/parts/CombinedIsp.cs
         :language: csharp

   .. tab:: C++

      .. literalinclude:: /scripts/tutorials/parts/CombinedIsp.cpp
         :language: cpp

   .. tab:: C

      .. literalinclude:: /scripts/tutorials/parts/CombinedIsp.c
         :language: c

   .. tab:: Java

      .. literalinclude:: /scripts/tutorials/parts/CombinedIsp.java
         :language: java

   .. tab:: Lua

      .. literalinclude:: /scripts/tutorials/parts/CombinedIsp.lua
         :language: lua

   .. tab:: Python

      .. literalinclude:: /scripts/tutorials/parts/CombinedIsp.py
         :language: python
