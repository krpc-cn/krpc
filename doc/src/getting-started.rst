.. _getting-started:

简介
===============

这个简单的指南解释了设置和运行 kRPC 服务端的基本知识, 再写一个基本的 Python 脚本与游戏互动。

服务端插件
-----------------

安装
^^^^^^^^^^^^

1. 从下面下载并安装kRPC服务端插件:

 * :github-download-zip:`Github <krpc>`
 * `SpaceDock <https://spacedock.info/mod/69/kRPC>`_
 * `Curse <https://mods.curse.com/ksp-mods/kerbal/220219-krpc-control-the-game-using-c-c-java-lua-python>`_
 * 或者使用 `CKAN <https://forum.kerbalspaceprogram.com/index.php?/topic/90246-the-comprehensive-kerbal-archive-network-ckan-package-manager-v1180-19-june-2016/>`_

2. 启动 KSP 并加载一个存档。

3. 服务端窗口应该和你打招呼了:

   .. image:: /images/getting-started/server-window.png

4. 单机 "Start server" 来, 额... 启动服务端! 如果一切顺利, 灯应该变成欢快的绿色。

5. 你可以单机右上角的关闭按钮隐藏窗口，也能单机右上角的图标 显示/隐藏 窗口:

   .. image:: /images/getting-started/applauncher.png

   服务端联机时这个图标也会变成绿色。

配置
^^^^^^^^^^^^^

点击窗口上的 "Edit" 按钮配置服务端:

1. **Protocol**: 这是服务端使用的协议，它影响到可以链接服务端的客户端类型。 
   Python 和大多数客户端通过 TCP/IP 协议链接，这里你需要选择 "Protobuf over TCP"。
2. **Address**: 这是服务端要监听的 IP 地址，只允许本地连接就选 'localhost' (默认)。 
   要允许网络连接就选择你电脑的本地 IP 地址，或者选择 'Manual' 手动输入 IP 地址。
3. **RPC and Stream port numbers**: 这里设置为你电脑上可用的端口号，一般保持默认就可以了。

还有些高级设置默认是隐藏的， 可以选中 "Show advanced settings" 查看:

1. **Auto-start server**: 开启此项会使服务端在游戏载入完毕后自动运行。
2. **Auto-accept new clients**: 开启此项会自动允许新的客户端连接。禁用此项会在新的客户端连接时弹出窗口询问是否允许。

其它高级设置是控制 :ref:`服务器性能 <server-performance-settings>`.

Python 客户端
-----------------

.. note:: kRPC 同时支持 Python 2.7 和 Python 3.x.

Windows系统
^^^^^^^^^^

1. 如果你还没装python,下载python安装程序并运行:
   https://www.python.org/downloads/windows 
   安装时要确保勾选pip一起安装。

2. 打开命令提示符运行以下命令安装kRPC python模块:
   ``C:\Python27\Scripts\pip.exe install krpc`` 
   你或许要把``C:\Python27``替换成你的python安装目录。

3. 运行Python IDLE (或者你最爱的编辑器)开始编程吧！

Linux系统（用linux系统的人应该不需要我翻译吧-译者注）
^^^^^^^^

1. Your linux distribution likely already comes with python installed. If not, install python using
   your favorite package manager, or get it from here: https://www.python.org/downloads

2. You also need to install pip, either using your package manager, or from here:
   https://pypi.python.org/pypi/pip

3. Install the kRPC python module by running the following from a terminal:
   ``sudo pip install krpc``

4. Start coding!

'Hello World'脚本
--------------------

打开KSP并用默认设置启动服务端，然后运行以下python脚本。


.. code-block:: python
   :linenos:

   import krpc
   conn = krpc.connect(name='Hello World')
   vessel = conn.space_center.active_vessel
   print(vessel.name)

按照下面做: 第一行加载kRPC python模块,第二行打开与服务器的新连接,第三行获取活动飞船，第四行输出飞船的名字。
然后你看到的应该是下面这样:

.. image:: /images/getting-started/hello-world.png

恭喜! 你刚刚写了第一个与KSP通信的脚本。

更进一步...
----------------

 * 更多你可以通过kRPC做的有趣示例,请点击 :doc:`教程 <tutorials>`.
 * 客户端库也可用于其它语言，包括 :doc:`C# <csharp>`,
   :doc:`C++ <cpp>`, :doc:`Java <java>` 和 :doc:`Lua <lua>`.
 * 您也可以用任何喜欢的语言 :doc:`手动与服务器通信 <communication-protocols>`。
