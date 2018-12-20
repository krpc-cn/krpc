自动驾驶
=========

kRPC提供了用于将飞船固定指定方向的自动驾驶功能。
它会自动调整以适应不同大小和权限的飞船。
本教程演示了自动驾驶如何工作，
如何配置和其背后的数学原理。

概述
--------

自动驾驶需要输入的是:

* A reference frame defining where zero rotation is,
* 目标俯仰角和偏航角,
* 和(可选的)目标翻滚角。

如果翻滚角没有指定,自动驾驶会尝试将围绕翻滚角的任何旋转归零，
但是不会尝试保持固定的翻滚角。

下图显示了自动驾驶的高级概述。首先,
当前旋转和目标旋转用于计算需要旋转面向目标的
:rst:ref:`目标角速度<target-angular-velocity>`。
接下来,将飞船的俯仰，偏航和滚动轴的角速度分量
传递给3个PID控制器。
控制器的输出用作飞船的控制输入。

图示左边有几个参数影响自动驾驶的操作,
下一节介绍它们。

.. image:: /images/tutorials/autopilot-schematic.png
   :align: center

配置自动驾驶
-------------------------

有几个参数会影响自动驾驶仪的行为，
在大多数情况下，这些的默认值应该足够了，但可以根据您的需要进行调整。

* **stopping time** 是飞船需要完全停止的最久时间。
  这限制了飞船的最大角速度。
  它是3个停止时间的矢量,俯仰轴，偏航轴，滚转轴各一个。
  每个轴的默认值是0.5秒。

* **deceleration time** 是当飞船接近目标方向时需要减速的最短时间，
  这是最小值,因为如果飞船没有足够的角加速度，需要的时间会更多。
  它是俯仰轴，偏航轴和滚动轴三个减速时间的矢量，以秒为单位，
  默认值是每个轴5秒。一个小的值会使自动减速更加积极,
  飞船也能更快地朝向目标。
  但是,这个值调地太小会导致超调。（飞船在目标方向周围来回摆动）

* 为了避免超调,停止时间应该比减速时间要小。
  这给自动驾驶一点用于调整飞船滚动中的误差的"备用"加速度,
  比如空气动力导致的变化。

* **attenuation angle** 设定自动驾驶认为飞船与目标角度之间"封闭"的范围。
  在这个范围里,目标速度随着飞船与目标间的接近程度而衰减。 It is
  它是一个角度,每个俯仰，翻滚和偏航轴，
  默认值是每个轴1度。
  当飞船指向正确的方向时，这种衰减阻止了控制器的振荡。
  如果你发现飞船仍然在振荡，请试着增加这个值。

* **time to peak** 单位秒,PID控制器调整飞船的角速度到目标角速度。
  减小此值会使控制器更积极地匹配目标角速度。
  它是俯仰，翻滚，偏航轴3个时间的矢量,默认值是每个轴3秒。

* **overshoot** 是PID控制器允许超调目标角速度的百分比。
  增加这个值将使控制器试图更积极地匹配目标速度，但会导致更多的超调。
  它是一个3值矢量,0和1之间,每个轴一个。
  默认值是0.01每轴。

.. _target-angular-velocity:

计算目标角速度
-------------------------------------

目标角速度是飞船使其朝向目标方向旋转所需的角速度。
它是通过对每个俯仰，偏航和滚动轴的目标角速度求和来计算的。
如果未设置翻滚角，则翻滚轴中的目标角速度简单地设置为0。

给出的轴的目标角速度:math:`\omega`是
角度差:math:`\theta`用以下函数算得:

.. image:: /images/tutorials/autopilot-angular-speed.png
   :align: center

这个函数的方程是:

.. math::
   \omega &= -\frac{\theta}{\lvert\theta\rvert}
             \text{min} \big(
                 \omega_{max},
                 \sqrt{2 \alpha \lvert\theta\rvert} \cdot f_a(\theta)
             \big) \\
   \text{where} & \\
   \alpha &= \frac{\omega_{max}}{t_{decel}} \\
   \omega_{max} &= \frac{\tau_{max}t_{stop}}{I} \\
   f_a(\theta) &= \frac{1}{1 + e^{-6/\theta_a(\lvert\theta\rvert - \theta_a)}}

其推理和推导如下:

* 飞船需要转向:math:`\theta = 0`。这意味着
  当:math:`\theta`是负数时目标角速度:math:`\omega`必须是正数,
  :math:`\theta`是正数时为负数。This is done by
  当:math:`\theta < 0`时是1，:math:`\theta >= 0`时是-1，
  这是通过乘以项:math:`-\frac{\theta}{\lvert\theta\rvert}`做到的。

* 我们希望飞船以最大角速度:math:`\omega_{max}`旋转,
  这取决停止时间:math:`t_{stop}`。 
  使用恒加速运动（motion under constant acceleration）方程我们可以推出如下:

  .. math::
     \omega &= \alpha t \\
     \Rightarrow \omega_{max} &= \alpha_{max} t_{stop} \\
                              &= \frac{\tau_{max}t_{stop}}{I}

  :math:`\tau_{max}`是飞船可以产生的最大扭矩, 
  :math:`I`是它的惯性矩（moment of inertia）。

* 面对目标时我们希望飞船花费时间:math:`t_{decel}`(减速时间)
  从速度:math:`\omega_{max}`到静止。
  我们还希望用恒加速度:math:`\alpha`来完成。
  使用恒加速运动方程我们可以推出当前角度差:math:`\theta`和
  目标速度:math:`\omega`的关系:

  .. math::
     \omega &= \alpha t \\
     \Rightarrow \alpha &= \frac{\omega}{t}
                         = \frac{\omega_{max}}{t_{decel}} \\
     \theta &= \frac{1}{2} \alpha t^2
     \Rightarrow t = \sqrt{\frac{2 \theta}{\alpha}} \\
     \Rightarrow \omega &= \alpha \sqrt{\frac{2 \theta}{\alpha}}
                         = \sqrt{2 \alpha \theta}

* 为了防止飞船在指向目标方向时震荡，
  目标角速度曲线:math:`\theta = 0`的梯度(gradient)必须是0,并且随着:math:`\theta`的增大/减小
  而增大/减小。

  这与上面计算的目标角速度不同。为了修正这个问题，我们要乘以一个具有所需形状的衰减函数。
  下图为衰减函数的形状(红色线)、目标速度(蓝色线)以及它们相乘的结果(黑色虚线):

  .. image:: /images/tutorials/autopilot-attenuation.png
     :align: center

  衰减函数公式是一个逻辑函数，公式如下:

  .. math::
     f_a(\theta) &= \frac{1}{1 + e^{-6/\theta_a(\lvert\theta\rvert - \theta_a)}}

  Note that the original function, derived from the equations of motion under
  constant acceleration, is only affected by the attenuation function close to
  the attenuation angle. This means that autopilot will use a constant
  acceleration to slow the vessel, until it gets close to the target direction.
  注意，从恒定加速度下的运动方程导出的原始函数仅受到接近衰减角度的衰减函数的影响。这意味着自动驾驶仪将使用恒定加速度来使船舶减速，直到它接近目标方向。

.. _tuning-the-controllers:

调整控制器
----------------------

三个PID控制器,俯仰、偏航、翻滚控制轴一轴一个, are
都用来控制飞船。每个控制器将目标角速度的相关分量作为输入。
下面描述这些控制器的增益是如何根据容器可用扭矩和惯性矩自动调整的。

整个系统的原理图在单个控制轴上如下:

.. image:: /images/tutorials/autopilot-system.png
   :align: center

The input to the system is the angular speed around the control axis, denoted
:math:`\omega`. The error in the angular speed :math:`\omega_\epsilon` is
calculated from this and passed to controller :math:`C`. This is a PID
controller that we need to tune. The output of the controller is the control
input, :math:`x`, that is passed to the vessel. The plant :math:`H` describes
the physical system, i.e. how the control input affects the angular acceleration
of the vessel. The derivative of this is computed to get the new angular speed
of the vessel, which is then fed back to compute the new error.

For the controller, :math:`C`, we use a proportional-integral controller. Note
that the controller does not have a derivative term, so that the system behaves
like a second order system and is therefore easy to tune.

The transfer function for the controller in the :math:`s` domain is:

.. math::
   C(s) &= K_P + K_I s^{-1}

From the schematic, the transfer function for the plant :math:`H` is:

.. math::
   H(s) &= \frac{\omega_\epsilon(s)}{X(s)}

:math:`x` is the control input to the vessel, which is the percentage of the
available torque :math:`\tau_{max}` that is being applied to the vessel. Call
this the current torque, denoted :math:`\tau`. This can be written
mathematically as:

.. math::
   \tau &= x \tau_{max}

Combining this with the angular equation of motion gives the angular
acceleration in terms of the control input:

.. math::
   I &= \text{moment of inertia of the vessel} \\
   \tau &= I \omega_\epsilon \\
   \Rightarrow \omega_\epsilon &= \frac{x\tau_{max}}{I}

Taking the laplace transform of this gives us:

.. math::
   \mathcal{L}(\omega_\epsilon(t)) &= s\omega_\epsilon(s) \\
                                &= \frac{sX(s)\tau_{max}}{I} \\
   \Rightarrow \frac{\omega_\epsilon(s)}{X(s)} &= \frac{\tau_{max}}{I}

We can now rewrite the transfer function for :math:`H` as:

.. math::
   H(s) = \frac{\tau_{max}}{I}

The open loop transfer function for the entire system is:

.. math::
   G_{OL}(s) &= C(S) \cdot H(s) \cdot s^{-1} \\
             &= (K_P + K_I s^{-1}) \frac{\tau_{max}}{Is}

The closed loop transfer function is then:

.. math::
   G(s) &= \frac{G_{OL}(s)}{1 + G_{OL}(s)} \\
        &= \frac{a K_P s + a  K_I}{s^2 + a K_P s + a K_I}
           \text{ where } a = \frac{\tau_{max}}{I}

The characteristic equation for the system is therefore:

.. math::
   \Phi &= s^2 + \frac{\tau_{max}}{I} K_P s + \frac{\tau_{max}}{I} K_I

The characteristic equation for a standard second order system is:

.. math::
   \Phi_{standard} &= s^2 + 2 \zeta \omega_0 s + \omega_0^2 \\

where :math:`\zeta` is the damping ratio and :math:`\omega_0` is the natural
frequency of the system.

Equating coefficients between these equations, and rearranging, gives us the
gains for the PI controller in terms of :math:`\zeta` and :math:`\omega_0`:

.. math::
   K_P &= \frac{2 \zeta \omega_0 I}{\tau_{max}} \\
   K_I &= \frac{I\omega_0^2}{\tau_{max}}

We now need to choose some performance requirements to place on the system,
which will allow us to determine the values of :math:`\zeta` and
:math:`\omega_0`, and therefore the gains for the controller.

The percentage by which a second order system overshoots is:

.. math::
   O &= e^{-\frac{\pi\zeta}{\sqrt{1-\zeta^2}}}

And the time it takes to reach the first peak in its output is:

.. math::
   T_P &= \frac{\pi}{\omega_0\sqrt{1-\zeta^2}}

These can be rearranged to give us :math:`\zeta` and :math:`\omega_0` in terms
of overshoot and time to peak:

.. math::
   \zeta = \sqrt{\frac{\ln^2(O)}{\pi^2+\ln^2(O)}} \\
   \omega_0 = \frac{\pi}{T_P\sqrt{1-\zeta^2}}

By default, kRPC uses the values :math:`O = 0.01` and :math:`T_P = 3`.

Corner Cases
------------

When sitting on the launchpad
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this situation, the autopilot cannot rotate the vessel. This means that the
integral term in the controllers will build up to a large value. This is even
true if the vessel is pointing in the correct direction, as small floating point
variations in the computed error will also cause the integral term to
increase. The integral terms are therefore fixed at zero to overcome this.

When the available angular acceleration is zero
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This could be caused, for example, by the reaction wheels on a vessel running
out of electricity resulting in the vessel having no torque.

In this situation, the autopilot also has little or no control over the
vessel. This means that the integral terms in the controllers will build up to a
large value over time. This is overcome by fixing the integral terms to zero
when the available angular acceleration falls below a small threshold.

This situation also causes an issue with the controller gain auto-tuning: as the
available angular acceleration tends towards zero, the controller gains tend
towards infinity. When it equals zero, the auto-tuning would cause a division by
zero. Therefore, auto-tuning is also disabled when the available acceleration
falls below the threshold. This leaves the controller gains at their current
values until the available acceleration rises again.
