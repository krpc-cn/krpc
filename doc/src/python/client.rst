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
   :param str address: 要连接的服务器的地址。 Can either be a hostname or an IP
                       address in dotted decimal notation. Defaults to '127.0.0.1'.
   :param int rpc_port: RPC服务器的端口号。 Defaults to 50000. This should match the
                           RPC port number of the server you want to connect to.
   :param int stream_port: 流服务器的端口号。 Defaults to 50001. This should
                           match the stream port number of the server you want to connect to.

.. class:: krpc.client.Client

   此类提供与服务器通信的接口。
   它动态填充服务器提供的所有功能。
   应该通过调用:func:`krpc.connect`获得此类的实例.

   .. method:: add_stream(func, *args, **kwargs)

      Create a stream for the function *func* called with arguments *args* and *kwargs*. Returns a
      :class:`krpc.stream.Stream` object.

   .. method:: stream(func, *args, **kwargs)

      Allows use of the ``with`` statement to create a stream and automatically remove it from the
      server when it goes out of scope. The function to be streamed should be passed as *func*, and
      its arguments as *args* and *kwargs*.

   .. attribute:: stream_update_condition

      A condition variable (of type ``threading.Condition``) that is notified whenever a stream
      update finishes processing.

   .. method:: wait_for_stream_update(timeout=None)

      This method blocks until a stream update finishes processing or the operation times out.

      The stream update condition variable must be locked before calling this method.

      If *timeout* is specified and is not ``None``, it should be a floating point number specifying
      the timeout in seconds for the operation.

   .. method:: add_stream_update_callback(callback)

      Adds a callback function that is invoked whenever a stream update finishes processing.

      .. note::

         The callback function may be called from a different thread to that which created the
         stream. Any changes to shared state must therefore be protected with appropriate
         synchronization.

   .. method:: remove_callback(callback)

      Removes a stream update callback function.

   .. method:: get_call(func, *args, **kwargs)

      Converts a call to function *func* with arguments *args* and *kwargs* into a message
      object. This allows descriptions of procedure calls to be passed to the server, for example
      when constructing custom events. See :ref:`python-client-events`.

   .. method:: close()

      Closes the connection to the server.

   .. attribute:: krpc

      The basic KRPC service, providing interaction with basic functionality of the server.

      :rtype: :class:`krpc.client.KRPC`

.. class:: krpc.client.KRPC

      This class provides access to the basic server functionality provided by the :class:`KRPC`
      service. An instance can be obtained by calling :attr:`krpc.client.Client.krpc`.

      See :class:`KRPC` for full documentation of this class.

      Some of this functionality is used internally by the python client (for example to create and
      remove streams) and therefore does not need to be used directly from application code.

.. class:: krpc.stream.Stream

   This class represents a stream. See :ref:`python-client-streams`.

   .. method:: start(wait=True)

      Starts the stream. When a stream is created by calling :meth:`krpc.client.Client.add_stream`
      it does not start sending updates to the client until this method is called.

      If wait is true, this method will block until at least one update has been received from the
      server.

      If wait is false, the method starts the stream and returns immediately. Subsequent calls to
      :meth:`__call__` may raise a ``StreamError`` exception if the stream does not yet contain a
      value.

   .. attribute:: rate

      The update rate of the stream in Hertz. When set to zero, the rate is unlimited.

   .. method:: __call__()

      Returns the most recent value for the stream. If executing the remote procedure for the stream
      throws an exception, calling this method will rethrow the exception. Raises a ``StreamError``
      exception if no update has been received from the server.

      If the stream has not been started this method calls ``start(True)`` to start the stream and
      wait until at least one update has been received.

   .. attribute:: condition

      A condition variable (of type ``threading.Condition``) that is notified whenever the value of
      the stream changes.

   .. method:: wait(timeout=None)

      This method blocks until the value of the stream changes or the operation times out.

      The streams condition variable must be locked before calling this method.

      If *timeout* is specified and is not ``None``, it should be a floating point number specifying
      the timeout in seconds for the operation.

      If the stream has not been started this method calls ``start(False)`` to start the stream
      (without waiting for at least one update to be received).

   .. method:: add_callback(callback)

      Adds a callback function that is invoked whenever the value of the stream changes. The
      callback function should take one argument, which is passed the new value of the stream.

      .. note::

         The callback function may be called from a different thread to that which created the
         stream. Any changes to shared state must therefore be protected with appropriate
         synchronization.

   .. method:: remove_callback(callback)

      Removes a callback function from the stream.

   .. method:: remove()

      Removes the stream from the server.

.. class:: krpc.event.Event

   This class represents an event. See :ref:`python-client-events`. It is wrapper around a stream of
   type ``bool`` that indicates when the event occurs.

   .. method:: start()

      Starts the event. When an event is created, it will not receive updates from the server until
      this method is called.

   .. attribute:: condition

      The condition variable (of type ``threading.Condition``) that is notified whenever the event
      occurs.

   .. method:: wait(timeout=None)

      This method blocks until the event occurs or the operation times out.

      The events condition variable must be locked before calling this method.

      If *timeout* is specified and is not ``None``, it should be a floating point number specifying
      the timeout in seconds for the operation.

      If the event has not been started this method calls ``start()`` to start the underlying
      stream.

   .. method:: add_callback(callback)

      Adds a callback function that is invoked whenever the event occurs. The callback function
      should be a function that takes zero arguments.

   .. method:: remove_callback(callback)

      Removes a callback function from the event.

   .. method:: remove()

      Removes the event from the server.

   .. attribute:: stream

      Returns the underlying stream for the event.
