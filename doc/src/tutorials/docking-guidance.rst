.. currentmodule:: SpaceCenter

对接制导
================

下面的脚本输出对接制导信息。 It waits until the
飞船从对接口控制, 并将一个对接口设为当前目标。
current target. 然后输出相对于对接轴的速度和距离信息。
relative to the docking axis.

它使用`numpy <http://www.numpy.org>`_ 对kRPC返回的矢量做线性代数计算
-- 例如计算点积(数量积)或者矢量的长度
-- 并使用`curses <https://docs.python.org/2/howto/curses.html>`_ 作为终端输出

.. literalinclude:: /scripts/tutorials/DockingGuidance.py
   :language: python
