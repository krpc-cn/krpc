自动驾驶
=========

kRPC提供了用于将飞船固定指定方向的自动驾驶功能。
它会自动调整以适应不同大小和权限的飞船。
本教程演示了自动驾驶如何工作，
如何配置和其背后的数学原理。

概述
--------

自动驾驶需要输入的是:

* 定义零旋转位置的参考框架,
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
输入系统的是控制轴的角速度，用:math:`\omega`表示。
The input to the system is the angular speed around the control axis, denoted
计算出的角速度差:math:`\omega_\epsilon`传递给控制器:math:`C`。
:math:`\omega`. The error in the angular speed :math:`\omega_\epsilon` is
calculated from this and passed to controller :math:`C`. This is a PID
这是我们需要协调的PID控制器。控制器的输出用于控制输入，
controller that we need to tune. The output of the controller is the control
:math:`x`传递给飞船。装置:math:`H`模拟物理系统，
input, :math:`x`, that is passed to the vessel. The plant :math:`H` describes
就是控制输入是如何影响飞船的角加速度。
the physical system, i.e. how the control input affects the angular acceleration
算得的导数用于获取新的飞船角速度，再返回去计算新的角速度差。
of the vessel. The derivative of this is computed to get the new angular speed
of the vessel, which is then fed back to compute the new error.

对于控制器:math:`C`，我们使用比例积分控制器。
注意，控制器没有导数项，所以系统的行为就像一个二阶系统，因此很容易进行优化。

:math:`s`域中控制器的传递函数为:

.. math::
   C(s) &= K_P + K_I s^{-1}

由示意图可知，装置:math:`H`的传递函数为:

.. math::
   H(s) &= \frac{\omega_\epsilon(s)}{X(s)}

:math:`x`是飞船的控制输入，可用扭矩的百分比:math:`\tau_{max}`
应用在飞船上。用:math:`\tau`表示当前扭矩。 
用数学方式写成:

.. math::
   \tau &= x \tau_{max}

将此与角运动方程相结合，得到控制输入的角加速度:

.. math::
   I &= \text{moment of inertia of the vessel} \\
   \tau &= I \omega_\epsilon \\
   \Rightarrow \omega_\epsilon &= \frac{x\tau_{max}}{I}

对它做拉普拉斯变换(laplace transform)得到:

.. math::
   \mathcal{L}(\omega_\epsilon(t)) &= s\omega_\epsilon(s) \\
                                &= \frac{sX(s)\tau_{max}}{I} \\
   \Rightarrow \frac{\omega_\epsilon(s)}{X(s)} &= \frac{\tau_{max}}{I}

现在我们可以把:math:`H`的传递函数重写为:

.. math::
   H(s) = \frac{\tau_{max}}{I}

整个系统的开环传递函数是:

.. math::
   G_{OL}(s) &= C(S) \cdot H(s) \cdot s^{-1} \\
             &= (K_P + K_I s^{-1}) \frac{\tau_{max}}{Is}

闭环传递函数是:

.. math::
   G(s) &= \frac{G_{OL}(s)}{1 + G_{OL}(s)} \\
        &= \frac{a K_P s + a  K_I}{s^2 + a K_P s + a K_I}
           \text{ where } a = \frac{\tau_{max}}{I}

因此，该系统的特征方程是:

.. math::
   \Phi &= s^2 + \frac{\tau_{max}}{I} K_P s + \frac{\tau_{max}}{I} K_I

标准二阶系统的特征方程是:

.. math::
   \Phi_{standard} &= s^2 + 2 \zeta \omega_0 s + \omega_0^2 \\

:math:`\zeta`:阻尼比，:math:`\omega_0`:系统的固有频率.

将方程之间的系数相等，并重新排列，得到PI控制器的增益，
项:math:`\zeta`和:math:`\omega_0`:

.. math::
   K_P &= \frac{2 \zeta \omega_0 I}{\tau_{max}} \\
   K_I &= \frac{I\omega_0^2}{\tau_{max}}

现在我们选择一些性能要求给系统,
就可以确定:math:`\zeta`和
:math:`\omega_0`的值,还有控制器的增益。

二阶系统超调的百分比是:

.. math::
   O &= e^{-\frac{\pi\zeta}{\sqrt{1-\zeta^2}}}

输出第一个峰值所需时间是:

.. math::
   T_P &= \frac{\pi}{\omega_0\sqrt{1-\zeta^2}}

These can be rearranged to give us :math:`\zeta` and :math:`\omega_0` in terms
重新排列超调和达峰时间可以得到:math:`\zeta`和:math:`\omega_0`:

.. math::
   \zeta = \sqrt{\frac{\ln^2(O)}{\pi^2+\ln^2(O)}} \\
   \omega_0 = \frac{\pi}{T_P\sqrt{1-\zeta^2}}

kRPC使用的默认值为:math:`O = 0.01`和:math:`T_P = 3`。

个别案例
------------

在发射台上
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

这种情况下,自动驾驶不能旋转飞船。
这意味着控制器中的积分项会累积到一个很大的值。
如果飞船指向正确的方向这甚至是正确的，
因为计算误差中的小浮点变化也会导致积分项的增加。
因此，积分项在零处固定以克服这个问题。

可用角加速度为零
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

这是能造成的，例如，在一个没电的飞船上反作用轮不能用
导致飞船没有扭矩。

这种情况下,自动驾驶只有一点或彻底失去对飞船的控制。
这意味着随着时间的推移，控制器中的积分项将累积到一个很大的值。
当可用的角加速度低于一个小阈值时，
通过将积分项固定为零来克服这个问题。

这种情况也会导致控制器增益自动调整的问题: as the
当可用的角加速度趋于零时，控制器增益倾向于无穷大。
当它等于零时，自动调整将导致除数为零。
因此，当可用加速度低于阈值时，也可禁用自动调整。
这使控制器获得其当前值，直到可用加速度再次增加。
