.. currentmodule:: SpaceCenter

发射入轨
=================

本教程发射一个二级火箭到150km的圆形轨道。
该程序假设您正在使用:download:`这个火箭模型
</crafts/LaunchIntoOrbit.craft>`。

该程序有多种语言版本:

:download:`C#</scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.cs>`,
:download:`C++</scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.cpp>`,
:download:`Java</scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.java>`,
:download:`Lua</scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.lua>`,
:download:`Python</scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.py>`

下面的代码连接到服务端,获取当前飞船,
设置一组信息流获取飞行遥测数据以准备火箭发射。

.. tabs::

   .. group-tab:: C#

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.cs
         :language: csharp
         :lines: 1-39
         :linenos:

   .. group-tab:: C++

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.cpp
         :language: cpp
         :lines: 1-35
         :linenos:

   .. group-tab:: Java

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.java
         :language: java
         :lines: 1-50
         :linenos:

   .. group-tab:: Lua

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.lua
         :language: lua
         :lines: 1-28
         :linenos:

   .. group-tab:: Python

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.py
         :language: python
         :lines: 1-31
         :linenos:

程序的下一部分是发射火箭。 主循环连续不断地
更新自动驾驶仪将火箭逐渐朝向地平线。
它还监测助推器中剩余固体燃料的数量，
在助推器耗尽时将其分离。
当火箭的远拱点接近目标远拱点时，循环退出。

.. tabs::

   .. group-tab:: C#

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.cs
         :language: csharp
         :lines: 41-78
         :lineno-start: 41
         :linenos:

   .. group-tab:: C++

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.cpp
         :language: cpp
         :lines: 37-71
         :lineno-start: 37
         :linenos:

   .. group-tab:: Java

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.java
         :language: java
         :lines: 52-89
         :lineno-start: 52
         :linenos:

   .. group-tab:: Lua

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.lua
         :language: lua
         :lines: 30-64
         :lineno-start: 30
         :linenos:

   .. group-tab:: Python

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.py
         :language: python
         :lines: 33-62
         :lineno-start: 33
         :linenos:

接下来，该程序用10%的推力对远拱点进行微调，
然后等待火箭离Kerbin的大气层。

.. tabs::

   .. group-tab:: C#

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.cs
         :language: csharp
         :lines: 80-90
         :lineno-start: 80
         :linenos:

   .. group-tab:: C++

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.cpp
         :language: cpp
         :lines: 73-83
         :lineno-start: 73
         :linenos:

   .. group-tab:: Java

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.java
         :language: java
         :lines: 91-101
         :lineno-start: 91
         :linenos:

   .. group-tab:: Lua

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.lua
         :language: lua
         :lines: 66-76
         :lineno-start: 66
         :linenos:

   .. group-tab:: Python

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.py
         :language: python
         :lines: 64-74
         :lineno-start: 64
         :linenos:

现在是计划环化轨道燃烧的时候了。
首先,我们用`vis-viva方程
<https://en.wikipedia.org/wiki/Vis-viva_equation>`_计算环化轨道所需的delta-v。
再用`Tsiolkovsky火箭方程
<https://en.wikipedia.org/wiki/Tsiolkovsky_rocket_equation>`_计算达到此delta-v所需的燃烧时间。

.. tabs::

   .. group-tab:: C#

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.cs
         :language: csharp
         :lines: 92-110
         :lineno-start: 92
         :linenos:

   .. group-tab:: C++

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.cpp
         :language: cpp
         :lines: 85-103
         :lineno-start: 85
         :linenos:

   .. group-tab:: Java

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.java
         :language: java
         :lines: 103-121
         :lineno-start: 103
         :linenos:

   .. group-tab:: Lua

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.lua
         :language: lua
         :lines: 78-95
         :lineno-start: 78
         :linenos:

   .. group-tab:: Python

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.py
         :language: python
         :lines: 76-94
         :lineno-start: 76
         :linenos:

接下来,我们需要旋转太空船等待环化燃烧。 We
ship沿着机动节点参考框架
的y轴(就是燃烧方向)，然后时间加速到燃烧前5秒。

.. tabs::

   .. group-tab:: C#

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.cs
         :language: csharp
         :lines: 112-122
         :lineno-start: 112
         :linenos:

   .. group-tab:: C++

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.cpp
         :language: cpp
         :lines: 105-115
         :lineno-start: 105
         :linenos:

   .. group-tab:: Java

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.java
         :language: java
         :lines: 123-135
         :lineno-start: 123
         :linenos:

   .. group-tab:: Lua

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.lua
         :language: lua
         :lines: 97-107
         :lineno-start: 97
         :linenos:

   .. group-tab:: Python

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.py
         :language: python
         :lines: 96-106
         :lineno-start: 96
         :linenos:

下一步是执行燃烧。设置最大油门， then throttles down
然后在预测燃烧结束前的1/10秒把油门降至5%。 It then
监视剩余的delta-v直到它翻转到节点的反方向
(已经执行完的节点).

.. tabs::

   .. group-tab:: C#

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.cs
         :language: csharp
         :lines: 124-
         :lineno-start: 124
         :linenos:

   .. group-tab:: C++

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.cpp
         :language: cpp
         :lines: 117-
         :lineno-start: 115
         :linenos:

   .. group-tab:: Java

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.java
         :language: java
         :lines: 137-
         :lineno-start: 137
         :linenos:

   .. group-tab:: Lua

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.lua
         :language: lua
         :lines: 109-
         :lineno-start: 109
         :linenos:

   .. group-tab:: Python

      .. literalinclude:: /scripts/tutorials/launch-into-orbit/LaunchIntoOrbit.py
         :language: python
         :lines: 108-
         :lineno-start: 108
         :linenos:

现在火箭应该在Kerbin的150km圆形轨道上了吧。
