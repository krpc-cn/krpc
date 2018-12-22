.. default-domain:: py
.. highlight:: py

Python客户端
=============

此客户端提供Python API与kRPC服务器交互。它支持Python 2.7+和
3.x

安装库
----------------------

该库可在`PyPI<https://pypi.python.org/pypi/krpc>`_或
:github-download-zip:`GitHub下载<krpc-python>`.

Linux下用pip安装:

.. code-block:: bash

   pip install krpc

Windows:

.. code-block:: none

   C:\Python27\Scripts\pip.exe install krpc

连接到服务器
------------------------

:func:`krpc.connect`函数用于打开一个与服务器的连接。
它返回一个连接对象(of type :class:`krpc.client.Client`)，你可以用此对象与服务器交互。
以下示例连接到在本地计算机上运行的服务器,获取版本并打印:

.. literalinclude:: /scripts/client/python/Connecting1.py

此函数同样接受指定地址和端口号的连接, and
并且可在游戏中的kRPC窗口显示连接的描述性名称。
例如:

.. literalinclude:: /scripts/client/python/Connecting2.py

调用远程过程
-------------------------

kRPC服务器支持客户端可运行的*程序*。这些程序被安排在称为*services*的组中保持井然有序。
连接时,Python客户端询问服务器以发现它提供的程序,
并动态创建类类型,方法,
属性等。来调用它们。

以下示例演示如何用Python客户端调用远程过程。
它调用:attr:`SpaceCenter.active_vessel`获取活动飞船(类型
:class:`SpaceCenter.Vessel`)的对象。
设置飞船的名称并打印其高度:

.. literalinclude:: /scripts/client/python/RemoteProcedures.py

``SpaceCenter``服务提供的所有功能都可以通过
``conn.space_center``访问。要查看服务提供的功能,您在交互式终端中可使用
``help()`函数。例如,运行``help(conn.space_center)``
会列出``SpaceCenter``服务提供的所有类,列举,过程和属性
对类类型同样,例如:
``help(conn.space_center.Vessel)``.

.. _python-client-streams:

从服务器流式传输数据
------------------------------

kRPC的一个常见用例是从游戏中连续提取数据。
执行此操作的天真方法是重复调用远程过程，
例如在下面重复打印活动飞船的位置:

.. literalinclude:: /scripts/client/python/Streaming1.py

由于在客户端和服务器之间重复发送请求/响应消息，
因此该方法需要大量的通信开销。
kRPC提供了一种更有效的机制来实现这一点，
称为"数据流"。

数据流重复执行服务器上的过程（具有一组固定的参数值）
并将结果发送到客户端。
它只需要将一条消息发送到服务器以建立流，
然后该数据流将继续向客户端发送数据，直到数据流关闭。

以下示例使用数据流执行与上述相同的操作:

.. literalinclude:: /scripts/client/python/Streaming2.py

它在程序运行之初调用:meth:`krpc.client.Client.add_stream`一次建立数据流，
然后重复打印数据流传回的位置。
客户端断开连接时数据流会自动关闭。

也可以用``with``语法创建数据流,可以确保离开块后数据流关闭:

.. literalinclude:: /scripts/client/python/Streaming3.py

可以为任何返回值的过程创建流，这包括方法调用和属性访问。
上面的示例演示了如何流式传输方法调用。
属性可以按如下方式流式传输:

.. literalinclude:: /scripts/client/python/Streaming4.py

可以为任何函数调用(除了属性设置)建立数据流。
调用:func:`krpc.stream.Stream.__call__`可以获得数据流的最新值。
在数据流对象调用:func:`krpc.stream.Stream.remove`可以停止并删除数据流。
断开连接时所有客户端数据流都会自动停止。

与数据流更新同步
---------------------------------

kRPC的一个常见用例是等到方法或属性返回的值发生更改，然后执行某些操作。
kRPC提供了两种有效执行此操作的机制: *条件变量*
和*回调函数*。

条件变量
^^^^^^^^^^^^^^^^^^^

每个流都有一个与之关联的条件变量，只要流的值发生变化就会通知该变量。
条件变量是Python标准库中``threading.Condition``的实例
这些可用于阻止当前执行的线程，直到流的值发生更改。

以下示例一直等到游戏中的终止按钮按下, 
``vessel.control.abort``的值变为true:

.. literalinclude:: /scripts/client/python/ConditionVariables1.py

此代码创建一个数据流，取得对条件变量的锁定(使用``with``
语句)反复检查``abort``的值。
当它变为真时退出循环。

流中循环主题调用``wait``,它会引起程序阻塞，直到值发生变化。
这可以防止循环空转，因此在等待时不会消耗处理资源。

.. note::

   在调用``wait``之前数据流还没开始更新。 This means that the
   这意味着示例代码不会错过数据流值的任何更新,
   因为它在收到第一个流更新前就锁定了条件变量。

上述示例代码使用``with``语句获取条件变量的锁定。
这也可以用``acquire``和``release``明确地达到目的:

.. literalinclude:: /scripts/client/python/ConditionVariables2.py

回调函数
^^^^^^^^^

数据流允许您注册一个回调函数，每当数据流发生变化时调用。
回调函数应该采用单个参数,数据流的新值,
不应返回任何内容。

例如，以下程序注册了两个在``vessel.conrol.abort``
发生变化时调用的回调:

.. literalinclude:: /scripts/client/python/Callbacks.py

.. note::

   创建的数据流直到``start``调用前不会开始就收更新. This is
   这里访问流的值时是隐式调用,但在示例中需要显示调用``start``
   就没这么做。

.. note::

   在调用``start``之前注册回调就不会错过流更新。

.. note::

   回调函数可以被创建流的不同线程调用。 
   因此，对共享状态的任何更改都必须通过适当的同步进行保护。

.. _python-client-events:

自定义事件
-------------

某些程序返回:class:`krpc.event.Event`类型的事件对象。
调用:class:`krpc.event.Event.wait`可以等你到事件出现。
其原理是用流和条件变量实现的。

自定义事件也可以创建。表达式API允许您创建在服务器上运行的代码，
这可以用于构建自定义事件。例如,
以下创建表达式``mean_altitude > 1000``
然后创建一个表达式返回为真时触发的事件:

.. literalinclude:: /scripts/client/python/Event.py

客户端API引用
--------------------

.. function:: krpc.connect([name=None], [address='127.0.0.1'], [rpc_port=50000], [stream_port=50001])

   此函数创建与kRPC服务器的连接。它返回一个:class:`krpc.client.Client`对象,
   通过该对象可以与服务器进行通信。

   :param str name: 连接的描述性名称。这将传递到服务器并显示在游戏内服务器窗口中。
   :param str address: 要连接的服务器的地址。 可以写主机名(hostname)或者
                       十进制的IP地址。默认是'127.0.0.1'。
   :param int rpc_port: RPC服务器的端口号。默认50000。这里应该与你要连接服务器的
                           RPC端口一样。
   :param int stream_port: 流服务器的端口号。默认50001。这里应该与你要连接服务器的
                           数据流端口一样。

.. class:: krpc.client.Client

   此类提供与服务器通信的接口。
   它动态填充服务器提供的所有功能。
   应该通过调用:func:`krpc.connect`获得此类的实例.

   .. method:: add_stream(func, *args, **kwargs)

      调用参数*args*和*kwargs*为函数*func*创建数据流。
      返回一个:class:`krpc.stream.Stream`对象。

   .. method:: stream(func, *args, **kwargs)

      允许使用``with``语句创建数据流并在它超出范围时从服务器删除。
      此函数应以*func*传递创建数据流,
      以*args*和*kwargs*作为参数。

   .. attribute:: stream_update_condition

      每当流更新完成处理则通知条件变量(类型``threading.Condition``)。

   .. method:: wait_for_stream_update(timeout=None)

      此方法将阻塞，直到流更新完成处理或操作超时.

      在调用此方法之前，必须锁定流更新条件变量。

      如果*timeout*已指定并不为``None``,它应该是一个浮点数
      指定操作的超时时间。

   .. method:: add_stream_update_callback(callback)

      添加一个回调函数，每当流更新完成处理就调用。

      .. note::

         回调函数可以被创建的流的不同线程调用。
         因此，必须用占用同步保护共享状态的任何更改。

   .. method:: remove_callback(callback)

      删除一个回调函数的流更新。

   .. method:: get_call(func, *args, **kwargs)

      转换带有参数*args*和*kwargs*的函数*func*调用为消息对象。
      这允许把过程调用的描述传递给服务器,例如
      在构建自定义事件时。参考:ref:`python-client-events`.

   .. method:: close()

      关闭与服务器的连接。

   .. attribute:: krpc

      基本KRPC服务,提供与服务器的基本交互功能。

      :rtype: :class:`krpc.client.KRPC`

.. class:: krpc.client.KRPC

      此类提供对访问:class:`KRPC`服务器基本服务功能的支持
      调用:attr:`krpc.client.Client.krpc`获取实例。

      参阅:class:`KRPC`查看此类完整文档。

      其中一些功能由Python客户端内部使用(如创建和删除流)
      因此不用再在代码中使用。

.. class:: krpc.stream.Stream

   此类代表数据流，参阅:ref:`python-client-streams`。

   .. method:: start(wait=True)

      开始流传输。当通过调用:meth:`krpc.client.Client.add_stream`创建流，
      在调用此方法之前不会向客户端更新信息。

      如果wait为true,此方法从服务器返回至少一个更新前会一直阻塞程序。

      如果wait为false,此方法会启动流并立即返回。 如果流尚未包含值则后续调用
      :meth:`__call__`可能会引发一个``StreamError``异常。

   .. attribute:: rate

      流更新的频率-赫兹(Hertz)。设为零时不受限制。

   .. method:: __call__()

      返回流的最新值，如果执行流的远程过程时抛出异常，
      ,调用此方法可以重新抛出异常。
      如果服务器没有返回任何更新，则引发``StreamError``异常。

      如果流还没启动，此方法调用``start(True)``启动流
      并一直等到服务器返回第一个更新。

   .. attribute:: condition

      每当流的值发生变化通知条件变量(类型``threading.Condition``)。

   .. method:: wait(timeout=None)

      此方法在流的值发生变化或设置的超时时间超时之前会一直阻塞程序。

      调用此方法前必须锁定数据流的条件变量。

      如果*timeout*指定并且不为``None``,必须用浮点数指定超时秒数。

      如果流还没启动，此方法调用``start(False)``启动流
      (不用等着返回至少一个更新)。

   .. method:: add_callback(callback)

      添加一个回调函数，只要流的值发生变化就调用该函数。 The
      回调函数必须有一个参数，用于传递流的新值。

      .. note::

         回调函数可以被创建流的不同线程调用。
         stream. 因此必须占用同步保护共享状态的任何变化。

   .. method:: remove_callback(callback)

      从流中删除回调函数。

   .. method:: remove()

      从服务器中删除流。

.. class:: krpc.event.Event

   此类代表一个事件。参阅:ref:`python-client-events`。
   它包装一个类型``bool``的流来指示事件发生。

   .. method:: start()

      启动事件。创建事件时,在调用此方法前不会从服务器收到流更新。

   .. attribute:: condition

      事件发生时通知的条件变量(类型``threading.Condition``)。

   .. method:: wait(timeout=None)

      此方法在事件发生或超时前阻塞程序。

      调用此方法前必须锁定事件的条件变量。

      如果*timeout*指定并且不为``None``,则必须用浮点数指定超时秒数。

      如果事件还未启动，此方法调用``start()``来启动基础流。

   .. method:: add_callback(callback)

      添加一个事件发生时调用的回调函数。
      回调函数必须是一个没有参数的函数。

   .. method:: remove_callback(callback)

      从事件删除回调函数。

   .. method:: remove()

      从服务器删除事件。

   .. attribute:: stream

      返回事件的基础流。
