.. currentmodule:: SpaceCenter

亚轨道飞行
==================

这个入门教程教你用kRPC送几个Kerbals(坎星人)到亚轨道, 并(但愿)将它们安全的返回Kerbin。
这涵盖以下几个主题:

* 控制一个火箭 (激活阶段, 设置油门)
* 使用自动驾驶将飞船指向指定方向
* 用游戏中发生的事触发事件
* 跟踪飞船上的资源值
* 跟踪飞行和轨道数据 (例如海拔和远拱点)

.. note:: 如何编写脚本和连接kRPC的详细资料请参阅 :ref:`getting-started`。

这个教程使用下图的二级火箭。飞船文件可以
:download:`在这下载 </crafts/SubOrbitalFlight.craft>`.

此教程包含kRPC支持的主要客户端语言的源码示例。
从此选择下载语言的完整程序:

:download:`C#</scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.cs>`,
:download:`C++</scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.cpp>`,
:download:`Java</scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.java>`,
:download:`Lua</scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.lua>`,
:download:`Python</scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.py>`

.. image:: /images/tutorials/SubOrbitalFlight.png
   :align: center

第一步: 准备发射
------------------------------

我们要做的第一步是打开与服务器的连接。 我们还可以为脚本传递一个描述性名字， 它会显示在游戏内的服务端窗口:

.. tabs::

   .. group-tab:: C#

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.cs
         :language: csharp
         :lines: 10
         :lineno-start: 10
         :linenos:

   .. group-tab:: C++

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.cpp
         :language: cpp
         :lines: 9-11
         :lineno-start: 9
         :linenos:

   .. group-tab:: Java

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.java
         :language: java
         :lines: 20-22
         :lineno-start: 20
         :linenos:

   .. group-tab:: Lua

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.lua
         :language: lua
         :lines: 1-3
         :linenos:

   .. group-tab:: Python

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.py
         :language: python
         :lines: 3
         :lineno-start: 3
         :linenos:

下面我们需要获取一个代表活动飞船的对象。 我们将通过这个对象向火箭发送指令:

.. tabs::

   .. group-tab:: C#

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.cs
         :language: csharp
         :lines: 12
         :lineno-start: 12
         :linenos:

   .. group-tab:: C++

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.cpp
         :language: cpp
         :lines: 13
         :lineno-start: 13
         :linenos:

   .. group-tab:: Java

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.java
         :language: java
         :lines: 24
         :lineno-start: 24
         :linenos:

   .. group-tab:: Lua

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.lua
         :language: lua
         :lines: 5
         :lineno-start: 5
         :linenos:

   .. group-tab:: Python

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.py
         :language: python
         :lines: 5
         :lineno-start: 5
         :linenos:

现在准备火箭的发射。下面的代码把油门设置为最大，并指示自动驾驶仪保持俯仰角和偏航角在90° (垂直向上)。
然后等待1秒设置生效。

.. tabs::

   .. group-tab:: C#

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.cs
         :language: csharp
         :lines: 14-17
         :lineno-start: 14
         :linenos:

   .. group-tab:: C++

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.cpp
         :language: cpp
         :lines: 15-18
         :lineno-start: 15
         :linenos:

   .. group-tab:: Java

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.java
         :language: java
         :lines: 26-29
         :lineno-start: 26
         :linenos:

   .. group-tab:: Lua

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.lua
         :language: lua
         :lines: 7-10
         :lineno-start: 7
         :linenos:

   .. group-tab:: Python

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.py
         :language: python
         :lines: 7-10
         :lineno-start: 7
         :linenos:

第二步: 升空!
-------------------

现在激活第一阶段发射 (相当于按空格键):

.. tabs::

   .. group-tab:: C#

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.cs
         :language: csharp
         :lines: 19-20
         :lineno-start: 19
         :linenos:

   .. group-tab:: C++

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.cpp
         :language: cpp
         :lines: 20-21
         :lineno-start: 20
         :linenos:

   .. group-tab:: Java

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.java
         :language: java
         :lines: 31-32
         :lineno-start: 31
         :linenos:

   .. group-tab:: Lua

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.lua
         :language: lua
         :lines: 12-13
         :lineno-start: 12
         :linenos:

   .. group-tab:: Python

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.py
         :language: python
         :lines: 12-13
         :lineno-start: 12
         :linenos:

火箭有一个会快速燃尽的固体燃料阶段需要抛弃。 我们可以用事件监视火箭中固体燃料的值，
它会在火箭中固体燃料很少的时候触发，当事件触发时激活下一阶段抛弃固体助推器:

.. tabs::

   .. group-tab:: C#

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.cs
         :language: csharp
         :lines: 23-29
         :lineno-start: 23
         :linenos:

   .. group-tab:: C++

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.cpp
         :language: cpp
         :lines: 26-32
         :lineno-start: 26
         :linenos:

   .. group-tab:: Java

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.java
         :language: java
         :lines: 34-47
         :lineno-start: 34
         :linenos:

   .. group-tab:: Lua

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.lua
         :language: lua
         :lines: 15-19
         :lineno-start: 15
         :linenos:

   .. group-tab:: Python

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.py
         :language: python
         :lines: 15-23
         :lineno-start: 15
         :linenos:

这段代码中, ``vessel.resources`` 返回一个 :class:`Resources` 对象用来获取有关飞船资源的信息。
代码在服务端创建表达式``vessel.resources.amount('SolidFuel') < 0.1``，此处使用表达式API。
这个表达式用来在返回值为true时驱动抛弃助推器事件。

第三步: 达到远拱点
-----------------------------

接下来我们会在飞船达到足够海拔时进行重力转向。下面使用一个事件等待飞船达到海拔10km:

.. tabs::

   .. group-tab:: C#

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.cs
         :language: csharp
         :lines: 36-42
         :lineno-start: 36
         :linenos:

   .. group-tab:: C++

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.cpp
         :language: cpp
         :lines: 39-45
         :lineno-start: 39
         :linenos:

   .. group-tab:: Java

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.java
         :language: java
         :lines: 50-58
         :lineno-start: 50
         :linenos:

   .. group-tab:: Lua

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.lua
         :language: lua
         :lines: 21-23
         :lineno-start: 21
         :linenos:

   .. group-tab:: Python

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.py
         :language: python
         :lines: 25-31
         :lineno-start: 25
         :linenos:

这段代码中, 调用``vessel.flight()``返回一个:class:`Flight`对象来获取火箭的所有类型的信息，
例如它的方向和速度。

现在我们要把火箭的俯仰角调到60°，维持偏航角90° (西)。
只需要重新配置自动驾驶仪:

.. tabs::

   .. group-tab:: C#

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.cs
         :language: csharp
         :lines: 45-46
         :lineno-start: 45
         :linenos:

   .. group-tab:: C++

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.cpp
         :language: cpp
         :lines: 48-49
         :lineno-start: 48
         :linenos:

   .. group-tab:: Java

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.java
         :language: java
         :lines: 61-62
         :lineno-start: 61
         :linenos:

   .. group-tab:: Lua

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.lua
         :language: lua
         :lines: 25-26
         :lineno-start: 25
         :linenos:

   .. group-tab:: Python

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.py
         :language: python
         :lines: 33-34
         :lineno-start: 33
         :linenos:

现在一直等到远拱点为100km(再次使用事件),降低油门到0,
抛弃发射阶段并关闭自动驾驶仪:

.. tabs::

   .. group-tab:: C#

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.cs
         :language: csharp
         :lines: 48-62
         :lineno-start: 32
         :linenos:

   .. group-tab:: C++

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.cpp
         :language: cpp
         :lines: 51-65
         :lineno-start: 51
         :linenos:

   .. group-tab:: Java

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.java
         :language: java
         :lines: 64-81
         :lineno-start: 64
         :linenos:

   .. group-tab:: Lua

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.lua
         :language: lua
         :lines: 28-35
         :lineno-start: 28
         :linenos:

   .. group-tab:: Python

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.py
         :language: python
         :lines: 36-48
         :lineno-start: 36
         :linenos:

这段代码中, ``vessel.orbit``返回一个:class:`Orbit`包含火箭轨道的所有信息的对象。

第四步: 安全地返回Kerbin
-------------------------------------

我们的Kerbals现在正朝着一个会与地面碰撞的亚轨道抛物线上航行着。
剩下要做的就是等它们与地面高度到了1km展开降落伞。
如果你想，可以使用时间加速跳过中间过程 - 脚本仍会运行。

.. tabs::

   .. group-tab:: C#

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.cs
         :language: csharp
         :lines: 64-74
         :lineno-start: 64
         :linenos:

   .. group-tab:: C++

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.cpp
         :language: cpp
         :lines: 67-77
         :lineno-start: 67
         :linenos:

   .. group-tab:: Java

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.java
         :language: java
         :lines: 83-96
         :lineno-start: 83
         :linenos:

   .. group-tab:: Lua

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.lua
         :language: lua
         :lines: 37-40
         :lineno-start: 37
         :linenos:

   .. group-tab:: Python

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.py
         :language: python
         :lines: 50-58
         :lineno-start: 50
         :linenos:

现在降落伞应该展开了，下端代码会重复输出返回舱的地面高度一直到它的速度为0--这会发生在着陆时:

.. tabs::

   .. group-tab:: C#

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.cs
         :language: csharp
         :lines: 76-81
         :lineno-start: 76
         :linenos:

   .. group-tab:: C++

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.cpp
         :language: cpp
         :lines: 79-83
         :lineno-start: 79
         :linenos:

   .. group-tab:: Java

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.java
         :language: java
         :lines: 98-103
         :lineno-start: 98
         :linenos:

   .. group-tab:: Lua

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.lua
         :language: lua
         :lines: 42-
         :lineno-start: 42
         :linenos:

   .. group-tab:: Python

      .. literalinclude:: /scripts/tutorials/sub-orbital-flight/SubOrbitalFlight.py
         :language: python
         :lines: 60-63
         :lineno-start: 60
         :linenos:

这段代码使用``vessel.flight()``函数,如前所述,但这次传递了一个
:class:`ReferenceFrame`参数。我们想要获得返回舱相对于Kerbin星球地面的垂直速度，所以要飞行对象相对于Kerbin地面的值。
我们传递``vessel.orbit.body.reference_frame``给``vessel.flight()``，因为这个
参考框架的起点在Kerbin的中心并且和星球一起旋转。
有关更多信息，请查看:ref:`tutorial-reference-frames`.

你的Kerbals现在应该安全地降落到地面了吧。