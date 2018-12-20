.. csharp:namespace:: KRPC.Client.Services.SpaceCenter
.. cpp:namespace:: krpc::services::SpaceCenter
.. java:package:: krpc.client.services.SpaceCenter
.. lua:currentmodule:: SpaceCenter
.. py:currentmodule:: SpaceCenter

.. _tutorial-reference-frames:

参考框架
================

.. contents::
   :local:

简介
------------

在kRPC中所有的位置, 方向, 速度和旋转都与某物有关。
*参考框架*则定义了什么是某物。

参开框架指定:

* 原点位置为(0,0,0)
* 坐标轴 x, y, z的方向
* 原点的线速度(如果参考框架移动)
* 坐标轴的角速度(轴的旋转速度和方向)

.. note:: KSP和kRPC使用左手坐标系

原点位置和轴方向
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

下面给出了一些各种参考框架的原点位置和坐标轴方向的示例。

天体参考框架
""""""""""""""""""""""""""""""

.. figure:: /images/reference-frames/celestial-body.png
   :align: right
   :figwidth: 250

   比如Kerbin的天体参考框架。赤道用蓝色表示，本初子午线用红色。
   黑色箭头代表坐标轴,原点位于行星的中心。

此参考框架通过调用:attr:`CelestialBody.reference_frame`获得Kerbin的以下属性:

* 原点位于Kerbin的中心,

* y轴是从Kerbin的中心点指向北极,

* x轴是从Kerbin的中心点指向赤道与本初子午线的交点(地面位置为经度0°, 纬度0°),

* z轴是从Kerbin的中心点指向赤道的经度90°E(东经),

* 轴与行星一起旋转，即参考框架与Kerbin有同样的
  旋转/角速度。

这意味着参考框架相对于Kerbin是*固定的*--
它与行星的中心一起移动, 也与行星一起旋转。 因此,
这个参考框架内的位置参照于行星中心。
下面的代码输出活动飞船在Kerbin参考框架中的位置:

.. tabs::

   .. tab:: C#

      .. literalinclude:: /scripts/tutorials/reference-frames/VesselPosition.cs
         :language: csharp

   .. tab:: C++

      .. literalinclude:: /scripts/tutorials/reference-frames/VesselPosition.cpp
         :language: cpp

   .. tab:: C

      .. literalinclude:: /scripts/tutorials/reference-frames/VesselPosition.c
         :language: c

   .. tab:: Java

      .. literalinclude:: /scripts/tutorials/reference-frames/VesselPosition.java
         :language: java

   .. tab:: Lua

      .. literalinclude:: /scripts/tutorials/reference-frames/VesselPosition.lua
         :language: lua

   .. tab:: Python

      .. literalinclude:: /scripts/tutorials/reference-frames/VesselPosition.py
         :language: python

对于在发射台上的飞船,位置矢量的大小大约为600,000米
(等于Kerbin的半径)。 位置矢量也不会
随着时间变化，因为飞船是在Kerbin的地面上的，
参考框架还是会随着Kerbin旋转。

飞船轨道参考框架
""""""""""""""""""""""""""""""

.. figure:: /images/reference-frames/vessel-orbital.png
   :align: right
   :figwidth: 350

   The orbital reference frame for a vessel.

另一个是飞船的轨道参考框架， 通过调用
:attr:`Vessel.orbital_reference_frame`获得。 它固定在飞船上(原点随着飞船移动) 
并且定向， 以便轴点在轨道的
轴向/法线/径向方向.

* 原点在飞船的质量中心,

* y轴指向飞船轨道方向,

* x轴指向飞船轨道的反径向方向，

* z轴指向飞船轨道的法线方向，

* 并且3轴会旋转以匹配轴向/法线/径向方向的变化,
  例如飞船在轨道上时它的轴向会一直变化。

飞船表面参考框架
""""""""""""""""""""""""""""""

.. figure:: /images/reference-frames/vessel-aircraft.png
   :align: right
   :figwidth: 350

   The reference frame for an aircraft.

另一个示例是:attr:`Vessel.reference_frame`. 与之前的示例一样,
它固定在飞船上(原点随着飞船移动),
但是坐标轴的方向不同。它们跟踪飞船的方向:

* 原点在飞船的质量中心,

* y轴指向飞船轴向,

* x轴指向飞船右侧,

* z轴指向飞船下方,

* 并且轴随着飞船的变化旋转。

线速度和角速度
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

参考框架相对于另一个移动和旋转。例如,
参考框架前面讨论的都是原点和位置固定在某个对象上
(比如飞船或行星)。这意味着它们移动和旋转来跟踪对象，
所以具有与它们相同的线速度和角速度。

例如, 参考框架通过调用Kerbin的
:attr:`CelestialBody.reference_frame` 获得相对于Kerbin固定的数据。
这意味着参考框架的角速度与Kerbin的角速度是完全相同的，线速度与Kerbin现在的轨道速度相同.

可用的参考框架
--------------------------

kRPC提供以下参考框架:

.. tabs::

   .. tab:: C#

      * :csharp:prop:`Vessel.ReferenceFrame`
      * :csharp:prop:`Vessel.OrbitalReferenceFrame`
      * :csharp:prop:`Vessel.SurfaceReferenceFrame`
      * :csharp:prop:`Vessel.SurfaceVelocityReferenceFrame`
      * :csharp:prop:`CelestialBody.ReferenceFrame`
      * :csharp:prop:`CelestialBody.NonRotatingReferenceFrame`
      * :csharp:prop:`CelestialBody.OrbitalReferenceFrame`
      * :csharp:prop:`Node.ReferenceFrame`
      * :csharp:prop:`Node.OrbitalReferenceFrame`
      * :csharp:prop:`Part.ReferenceFrame`
      * :csharp:prop:`Part.CenterOfMassReferenceFrame`
      * :csharp:prop:`DockingPort.ReferenceFrame`
      * :csharp:prop:`Thruster.ThrustReferenceFrame`

   .. tab:: C++

      * :cpp:func:`Vessel::reference_frame`
      * :cpp:func:`Vessel::orbital_reference_frame`
      * :cpp:func:`Vessel::surface_reference_frame`
      * :cpp:func:`Vessel::surface_velocity_reference_frame`
      * :cpp:func:`CelestialBody::reference_frame`
      * :cpp:func:`CelestialBody::non_rotating_reference_frame`
      * :cpp:func:`CelestialBody::orbital_reference_frame`
      * :cpp:func:`Node::reference_frame`
      * :cpp:func:`Node::orbital_reference_frame`
      * :cpp:func:`Part::reference_frame`
      * :cpp:func:`Part::center_of_mass_reference_frame`
      * :cpp:func:`DockingPort::reference_frame`
      * :cpp:func:`Thruster::thrust_reference_frame`

   .. tab:: C

      * :c:func:`krpc_SpaceCenter_Vessel_ReferenceFrame`
      * :c:func:`krpc_SpaceCenter_Vessel_OrbitalReferenceFrame`
      * :c:func:`krpc_SpaceCenter_Vessel_SurfaceReferenceFrame`
      * :c:func:`krpc_SpaceCenter_Vessel_SurfaceVelocityReferenceFrame`
      * :c:func:`krpc_SpaceCenter_CelestialBody_ReferenceFrame`
      * :c:func:`krpc_SpaceCenter_CelestialBody_NonRotatingReferenceFrame`
      * :c:func:`krpc_SpaceCenter_CelestialBody_OrbitalReferenceFrame`
      * :c:func:`krpc_SpaceCenter_Node_ReferenceFrame`
      * :c:func:`krpc_SpaceCenter_Node_OrbitalReferenceFrame`
      * :c:func:`krpc_SpaceCenter_Part_ReferenceFrame`
      * :c:func:`krpc_SpaceCenter_Part_CenterOfMassReferenceFrame`
      * :c:func:`krpc_SpaceCenter_DockingPort_ReferenceFrame`
      * :c:func:`krpc_SpaceCenter_Thruster_ThrustReferenceFrame`

   .. tab:: Java

      * :java:meth:`Vessel.getReferenceFrame`
      * :java:meth:`Vessel.getOrbitalReferenceFrame`
      * :java:meth:`Vessel.getSurfaceReferenceFrame`
      * :java:meth:`Vessel.getSurfaceVelocityReferenceFrame`
      * :java:meth:`CelestialBody.getReferenceFrame`
      * :java:meth:`CelestialBody.getNonRotatingReferenceFrame`
      * :java:meth:`CelestialBody.getOrbitalReferenceFrame`
      * :java:meth:`Node.getReferenceFrame`
      * :java:meth:`Node.getOrbitalReferenceFrame`
      * :java:meth:`Part.getReferenceFrame`
      * :java:meth:`Part.getCenterOfMassReferenceFrame`
      * :java:meth:`DockingPort.getReferenceFrame`
      * :java:meth:`Thruster.getThrustReferenceFrame`

   .. tab:: Lua

      * :lua:attr:`Vessel.reference_frame`
      * :lua:attr:`Vessel.orbital_reference_frame`
      * :lua:attr:`Vessel.surface_reference_frame`
      * :lua:attr:`Vessel.surface_velocity_reference_frame`
      * :lua:attr:`CelestialBody.reference_frame`
      * :lua:attr:`CelestialBody.non_rotating_reference_frame`
      * :lua:attr:`CelestialBody.orbital_reference_frame`
      * :lua:attr:`Node.reference_frame`
      * :lua:attr:`Node.orbital_reference_frame`
      * :lua:attr:`Part.reference_frame`
      * :lua:attr:`Part.center_of_mass_reference_frame`
      * :lua:attr:`DockingPort.reference_frame`
      * :lua:attr:`Thruster.thrust_reference_frame`

   .. tab:: Python

      * :py:attr:`Vessel.reference_frame`
      * :py:attr:`Vessel.orbital_reference_frame`
      * :py:attr:`Vessel.surface_reference_frame`
      * :py:attr:`Vessel.surface_velocity_reference_frame`
      * :py:attr:`CelestialBody.reference_frame`
      * :py:attr:`CelestialBody.non_rotating_reference_frame`
      * :py:attr:`CelestialBody.orbital_reference_frame`
      * :py:attr:`Node.reference_frame`
      * :py:attr:`Node.orbital_reference_frame`
      * :py:attr:`Part.reference_frame`
      * :py:attr:`Part.center_of_mass_reference_frame`
      * :py:attr:`DockingPort.reference_frame`
      * :py:attr:`Thruster.thrust_reference_frame`

相对和混合参考框架都可以用上面的构建。

自定义参考框架
-----------------------

可以从上面列出的框架构建自定义参考框架。
它们包含: '相对'和'混合'两种。

一个相对参考框架构建自一个父参考框架，
是固定位置偏移和固定旋转偏移的关系。
例如,沿着z轴应用一个位置偏移10到
:attr:`Vessel.reference_frame`，
这可以构建原点在飞船下方10m的参考框架。
相对参考框架可以通过调用
:meth:`ReferenceFrame.create_relative`构建。

混合参考框架的构成(位置,旋转,速度
和角速度)是继承自其它参考框架的构成。注意
这些构成不是必须固定的。例如,你可以构建这样一个参考框架：
位置是飞船质量中心(继承自
:attr:`Vessel.reference_frame`)，旋转是其环绕的行星
(继承自:attr:`CelestialBody.reference_frame`)。
混合参考框架可以通过调用
:meth:`ReferenceFrame.create_hybrid`构建。

自定义参考框架的父参考框架也可以是其它
自定义参考框架。例如，你可以组合上面两个自定义参考框架
:构建一个混合参考框架, 以飞船为中心且随着其环绕的行星旋转,
然后创建一个沿着z轴偏移10m的相对参考框架。
这样就得到一个原点在飞船下方10m并随着其环绕的行星旋转的框架。

在参考框架之间转换
-----------------------------------

kRPC提供了在不同的参考框架之间转换位置, 方向,旋转和
速度的实现方法:


.. tabs::

   .. tab:: C#

      * :csharp:meth:`SpaceCenter.TransformPosition`
      * :csharp:meth:`SpaceCenter.TransformDirection`
      * :csharp:meth:`SpaceCenter.TransformRotation`
      * :csharp:meth:`SpaceCenter.TransformVelocity`

   .. tab:: C++

      * :cpp:func:`SpaceCenter::transform_position`
      * :cpp:func:`SpaceCenter::transform_direction`
      * :cpp:func:`SpaceCenter::transform_rotation`
      * :cpp:func:`SpaceCenter::transform_velocity`

   .. tab:: C

      * :c:func:`krpc_SpaceCenter_TransformPosition`
      * :c:func:`krpc_SpaceCenter_TransformDirection`
      * :c:func:`krpc_SpaceCenter_TransformRotation`
      * :c:func:`krpc_SpaceCenter_TransformVelocity`

   .. tab:: Java

      * :java:meth:`SpaceCenter.transformPosition`
      * :java:meth:`SpaceCenter.transformDirection`
      * :java:meth:`SpaceCenter.transformRotation`
      * :java:meth:`SpaceCenter.transformVelocity`

   .. tab:: Lua

      * :lua:meth:`SpaceCenter.transform_position`
      * :lua:meth:`SpaceCenter.transform_direction`
      * :lua:meth:`SpaceCenter.transform_rotation`
      * :lua:meth:`SpaceCenter.transform_velocity`

   .. tab:: Python

      * :py:meth:`SpaceCenter.transform_position`
      * :py:meth:`SpaceCenter.transform_direction`
      * :py:meth:`SpaceCenter.transform_rotation`
      * :py:meth:`SpaceCenter.transform_velocity`

可视化调试
----------------

参考框架可能令人困惑, 选择正确的框架本身就是一项挑战。
为了帮助调试, kRPC的绘图函数可以用来
在游戏中可视化方向向量。

:meth:`Drawing.add_direction`会绘出方向向量，从指定的参考框架的原点开始。
例如, 下面的代码绘出了
当前飞船相对于其环绕星体表面的速度方向:

.. tabs::

   .. tab:: C#

      .. literalinclude:: /scripts/tutorials/reference-frames/VisualDebugging.cs
         :language: csharp

   .. tab:: C++

      .. literalinclude:: /scripts/tutorials/reference-frames/VisualDebugging.cpp
         :language: cpp

   .. tab:: C

      .. literalinclude:: /scripts/tutorials/reference-frames/VisualDebugging.c
         :language: c

   .. tab:: Java

      .. literalinclude:: /scripts/tutorials/reference-frames/VisualDebugging.java
         :language: java

   .. tab:: Lua

      .. literalinclude:: /scripts/tutorials/reference-frames/VisualDebugging.lua
         :language: lua

   .. tab:: Python

      .. literalinclude:: /scripts/tutorials/reference-frames/VisualDebugging.py
         :language: python

.. note:: 客户端必须保持连线才能持续绘图,
          因此在示例的最后是无限循环。

示例
--------

以下示例演示了参考框架的各种用法。

导航球方向
^^^^^^^^^^^^^^^^^^

这个示例演示了如何在导航球上使飞船指向各个方向:

.. tabs::

   .. tab:: C#

      .. literalinclude:: /scripts/tutorials/reference-frames/NavballDirections.cs
         :language: csharp

   .. tab:: C++

      .. literalinclude:: /scripts/tutorials/reference-frames/NavballDirections.cpp
         :language: cpp

   .. tab:: C

      .. literalinclude:: /scripts/tutorials/reference-frames/NavballDirections.c
         :language: c

   .. tab:: Java

      .. literalinclude:: /scripts/tutorials/reference-frames/NavballDirections.java
         :language: java

   .. tab:: Lua

      .. literalinclude:: /scripts/tutorials/reference-frames/NavballDirections.lua
         :language: lua

   .. tab:: Python

      .. literalinclude:: /scripts/tutorials/reference-frames/NavballDirections.py
         :language: python

代码使用飞船的地面参考框架
(:attr:`Vessel.surface_reference_frame`), 如下图所示:

.. image:: /images/reference-frames/vessel-surface.png
   :align: center

第一部分命令自动驾驶仪指向飞船地面参考框架的``(0,1,0)``方向
(即沿y轴方向)。 按照规定，
参考框架的y轴指向北方。

第二部分命令自动驾驶仪指向飞船地面参考框架的``(1,0,0)``方向
(即沿x轴方向)。按照规定，
参考框架的x轴指向上方(从行星向外辐射)。

最后,代码命令自动驾驶仪指向``(0,0,-1)``方向
(即沿z轴的反向)。参考框架的z轴指向东方,
所以按照规定，要求的方向为西方。

轨道方向
^^^^^^^^^^^^^^^^^^

这个示例演示了当看到导航球上显示'轨道'模式时如何让飞船指向轨道的不同
方向。它使用
:attr:`Vessel.orbital_reference_frame`函数。

.. tabs::

   .. tab:: C#

      .. literalinclude:: /scripts/tutorials/reference-frames/OrbitalDirections.cs
         :language: csharp

   .. tab:: C++

      .. literalinclude:: /scripts/tutorials/reference-frames/OrbitalDirections.cpp
         :language: cpp

   .. tab:: C

      .. literalinclude:: /scripts/tutorials/reference-frames/OrbitalDirections.c
         :language: c

   .. tab:: Java

      .. literalinclude:: /scripts/tutorials/reference-frames/OrbitalDirections.java
         :language: java

   .. tab:: Lua

      .. literalinclude:: /scripts/tutorials/reference-frames/OrbitalDirections.lua
         :language: lua

   .. tab:: Python

      .. literalinclude:: /scripts/tutorials/reference-frames/OrbitalDirections.py
         :language: python

该代码使用飞船的轨道参考框架，如下图所示:

.. image:: /images/reference-frames/vessel-orbital.png
   :align: center

地面'顺行'
^^^^^^^^^^^^^^^^^^

此示例演示了在导航球处于'地面'模式时上如何使飞船指向'顺行'方向，
这是飞船相对地面的速度方向:

.. tabs::

   .. tab:: C#

      .. literalinclude:: /scripts/tutorials/reference-frames/SurfacePrograde.cs
         :language: csharp

   .. tab:: C++

      .. literalinclude:: /scripts/tutorials/reference-frames/SurfacePrograde.cpp
         :language: cpp

   .. tab:: C

      .. literalinclude:: /scripts/tutorials/reference-frames/SurfacePrograde.c
         :language: c

   .. tab:: Java

      .. literalinclude:: /scripts/tutorials/reference-frames/SurfacePrograde.java
         :language: java

   .. tab:: Lua

      .. literalinclude:: /scripts/tutorials/reference-frames/SurfacePrograde.lua
         :language: lua

   .. tab:: Python

      .. literalinclude:: /scripts/tutorials/reference-frames/SurfacePrograde.py
         :language: python

此代码使用:attr:`Vessel.surface_velocity_reference_frame`函数,如下图所示:

.. image:: /images/reference-frames/vessel-surface-velocity.png
   :align: center

.. _tutorial-reference-frames-vessel-speed:

飞船速度（Speed）
^^^^^^^^^^^^

这个示例演示了如何获取飞船的地面和轨道速度，
相当于导航球上显示的值。

要计算飞船的轨道速度，你需要获得相对于
行星的*无旋转*参考框架
(:attr:`CelestialBody.non_rotating_reference_frame`)的速度。
这个参考框架相对于天体固定，但不旋转。

对于地面速度，行星的参考框架
(:attr:`CelestialBody.reference_frame`)是必须的，
因为这个参考框架随着天体旋转。

.. tabs::

   .. tab:: C#

      .. literalinclude:: /scripts/tutorials/reference-frames/VesselSpeed.cs
         :language: csharp

   .. tab:: C++

      .. literalinclude:: /scripts/tutorials/reference-frames/VesselSpeed.cpp
         :language: cpp

   .. tab:: C

      .. literalinclude:: /scripts/tutorials/reference-frames/VesselSpeed.c
         :language: c

   .. tab:: Java

      .. literalinclude:: /scripts/tutorials/reference-frames/VesselSpeed.java
         :language: java

   .. tab:: Lua

      .. literalinclude:: /scripts/tutorials/reference-frames/VesselSpeed.lua
         :language: lua

   .. tab:: Python

      .. literalinclude:: /scripts/tutorials/reference-frames/VesselSpeed.py
         :language: python

.. _tutorial-reference-frames-vessel-velocity:

飞船的速度（Velocity）
^^^^^^^^^^^^^^^

这个示例演示了如何获取飞船相对于其环绕的天体地面
的速度(矢量),

为此需要混合参考框架。这是因为我们想要一个以飞船为中心，
但是线速度又和地面是相对固定的参考框架。

因此我们需要创建一个其旋转设置为飞船
地面参考框架(:attr:`Vessel.surface_reference_frame`), 
其它属性(包括位置和速度)设置为
天体参考框架(:attr:`CelestialBody.reference_frame`)的混合参考框架
 -- 与天体一起旋转。

.. tabs::

   .. tab:: C#

      .. literalinclude:: /scripts/tutorials/reference-frames/VesselVelocity.cs
         :language: csharp

   .. tab:: C++

      .. literalinclude:: /scripts/tutorials/reference-frames/VesselVelocity.cpp
         :language: cpp

   .. tab:: C

      .. literalinclude:: /scripts/tutorials/reference-frames/VesselVelocity.c
         :language: c

   .. tab:: Java

      .. literalinclude:: /scripts/tutorials/reference-frames/VesselVelocity.java
         :language: java

   .. tab:: Lua

      .. literalinclude:: /scripts/tutorials/reference-frames/VesselVelocity.lua
         :language: lua

   .. tab:: Python

      .. literalinclude:: /scripts/tutorials/reference-frames/VesselVelocity.py
         :language: python

攻角
^^^^^^^^^^^^^^^

这个示例计算飞船所指方向和
飞船移动方向(相对于地面)之间的角度:

.. tabs::

   .. tab:: C#

      .. literalinclude:: /scripts/tutorials/reference-frames/AngleOfAttack.cs
         :language: csharp

   .. tab:: C++

      .. literalinclude:: /scripts/tutorials/reference-frames/AngleOfAttack.cpp
         :language: cpp

   .. tab:: C

      .. literalinclude:: /scripts/tutorials/reference-frames/AngleOfAttack.c
         :language: c

   .. tab:: Java

      .. literalinclude:: /scripts/tutorials/reference-frames/AngleOfAttack.java
         :language: java

   .. tab:: Lua

      .. literalinclude:: /scripts/tutorials/reference-frames/AngleOfAttack.lua
         :language: lua

   .. tab:: Python

      .. literalinclude:: /scripts/tutorials/reference-frames/AngleOfAttack.py
         :language: python

注意：用于获得位置和速度矢量的参考框架的方向不重要，
因为无论轴的角度如何，两个矢量之间的角斗士相同的。
但是, 
如果我们用随飞船移动的参考框架，速度就会归``(0,0,0)``。
因此我们需要一个不与飞船相对固定的参考框架
:attr:`CelestialBody.reference_frame`正符合这个要求。

着陆地点
^^^^^^^^^^^^

这个示例计算位于指定高度的星球表面的参考框架。
它可以作为自动着陆的目标。

.. tabs::

   .. tab:: C#

      .. literalinclude:: /scripts/tutorials/reference-frames/LandingSite.cs
         :language: csharp

   .. tab:: C++

      .. literalinclude:: /scripts/tutorials/reference-frames/LandingSite.cpp
         :language: cpp

   .. tab:: C

      .. literalinclude:: /scripts/tutorials/reference-frames/LandingSite.c
         :language: c

   .. tab:: Java

      .. literalinclude:: /scripts/tutorials/reference-frames/LandingSite.java
         :language: java

   .. tab:: Lua

      .. literalinclude:: /scripts/tutorials/reference-frames/LandingSite.lua
         :language: lua

   .. tab:: Python

      .. literalinclude:: /scripts/tutorials/reference-frames/LandingSite.py
         :language: python
