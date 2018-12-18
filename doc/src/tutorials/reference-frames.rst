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

* the y轴指向飞船轴向,

* the x轴指向飞船右侧,

* the z轴指向飞船下方,

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

相对和混合参考框架都可以用上面的构造。

自定义参考框架
-----------------------

自定义参考框架 can be constructed from the built in frames listed
above. They come in two varieties: 'relative' and 'hybrid'.

A relative reference frame is constructed from a parent reference frame, a fixed
position offset and a fixed rotation offset. For example, this could be used to
construct a reference frame whose origin is 10m below the vessel as follows, by
applying a position offset of 10 along the z-axis to
:attr:`Vessel.reference_frame`. Relative 参考框架 can be constructed by
calling :meth:`ReferenceFrame.create_relative`.

A hybrid reference frame inherits its components (position, rotation, velocity
and angular velocity) from the components of other 参考框架. Note that
these components need not be fixed. For example, you could construct a reference
frame whose position is the center of mass of the vessel (inherited from
:attr:`Vessel.reference_frame`) and whose rotation is that of the planet being
orbited (inherited from :attr:`CelestialBody.reference_frame`). Relative
参考框架 can be constructed by calling
:meth:`ReferenceFrame.create_hybrid`.

The parent reference frame(s) of a custom reference frame can also be other
custom 参考框架. For example, you could combine the two example frames
from above: construct a hybrid reference frame, centered on the vessel and
rotated with the planet being orbited, and then create a relative reference that
offsets the position of this 10m along the z-axis. The resulting frame will have
its origin 10m below the vessel, and will be rotated with the planet being
orbited.

Converting Between 参考框架
-----------------------------------

kRPC provides utility methods to convert 位置, 方向,旋转 and
速度 between the different 参考框架:


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

Visual Debugging
----------------

References frames can be confusing, and choosing the correct one is a challenge
in itself. To aid debugging, kRPCs drawing functionality can be used to
visualize direction vectors in-game.

:meth:`Drawing.add_direction` will draw a direction vector, starting from the
origin of the given reference frame. For example, the following code draws the
direction of the current vessels velocity relative to the surface of the body it
is orbiting:

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

.. note:: The client must remain connected for the line to continue to be drawn,
          hence the infinite loop at the end of this example.

Examples
--------

The following examples demonstrate various uses of 参考框架.

Navball 方向
^^^^^^^^^^^^^^^^^^

This example demonstrates how to make the vessel point in various 方向 on
the navball:

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

The code uses the vessel's surface reference frame
(:attr:`Vessel.surface_reference_frame`), pictured below:

.. image:: /images/reference-frames/vessel-surface.png
   :align: center

The first part instructs the auto-pilot to point in direction ``(0,1,0)``
(i.e. along the y-axis) in the vessel's surface reference frame. The y-axis of
the reference frame points in the north direction, as required.

The second part instructs the auto-pilot to point in direction ``(1,0,0)``
(along the x-axis) in the vessel's surface reference frame. This x-axis of the
reference frame points upwards (away from the planet) as required.

Finally, the code instructs the auto-pilot to point in direction ``(0,0,-1)``
(along the negative z axis). The z-axis of the reference frame points east, so
the requested direction points west -- as required.

Orbital 方向
^^^^^^^^^^^^^^^^^^

This example demonstrates how to make the vessel point in the various orbital
方向, as seen on the navball when it is in 'orbit' mode. It uses
:attr:`Vessel.orbital_reference_frame`.

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

This code uses the vessel's orbital reference frame, pictured below:

.. image:: /images/reference-frames/vessel-orbital.png
   :align: center

Surface 'prograde'
^^^^^^^^^^^^^^^^^^

This example demonstrates how to point the vessel in the 'prograde' direction on
the navball, when in 'surface' mode. This is the direction of the vessels
velocity relative to the surface:

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

This code uses the :attr:`Vessel.surface_velocity_reference_frame`, pictured
below:

.. image:: /images/reference-frames/vessel-surface-velocity.png
   :align: center

.. _tutorial-reference-frames-vessel-speed:

Vessel Speed
^^^^^^^^^^^^

This example demonstrates how to get the orbital and surface speeds of the
vessel, equivalent to the values displayed by the navball.

To compute the orbital speed of a vessel, you need to get the velocity relative
to the planet's *non-rotating* reference frame
(:attr:`CelestialBody.non_rotating_reference_frame`). This reference frame is
fixed relative to the body, but does not rotate.

For the surface speed, the planet's reference frame
(:attr:`CelestialBody.reference_frame`) is required, as this reference frame
rotates with the body.

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

Vessel Velocity
^^^^^^^^^^^^^^^

This example demonstrates how to get the velocity of the vessel (as a vector),
relative to the surface of the body being orbited.

To do this, a hybrid reference frame is required. This is because we want a
reference frame that is centered on the vessel, but whose linear velocity is
fixed relative to the ground.

We therefore create a hybrid reference frame with its rotation set to the
vessel's surface reference frame (:attr:`Vessel.surface_reference_frame`), and
all other properties (including position and velocity) set to the body's
reference frame (:attr:`CelestialBody.reference_frame`) -- which rotates with
the body.

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

Angle of attack
^^^^^^^^^^^^^^^

This example computes the angle between the direction the vessel is pointing in,
and the direction that the vessel is moving in (relative to the surface):

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

Note that the orientation of the reference frame used to get the direction and
velocity vectors does not matter, as the angle between two vectors is the same
regardless of the orientation of the axes. However, if we were to use a
reference frame that moves with the vessel, the velocity would return
``(0,0,0)``. We therefore need a reference frame that is not fixed relative to
the vessel. :attr:`CelestialBody.reference_frame` fits these requirements.

Landing Site
^^^^^^^^^^^^

This example computes a reference frame that is located on the surface of a body
at a given altitude, which could be used as the target for a landing auto pilot.

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
