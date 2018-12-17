kRPC文档
==================

kRPC允许你从游戏外部运行脚本控制Kerbal Space Program。
它有许多流行语言的客户端库
:doc:`C# <csharp/client>`,
:doc:`C++ <cpp/client>`,
:doc:`Java <java/client>`,
:doc:`Lua <lua/client>` 和
:doc:`Python <python/client>`.
他人制作的客户端同样支持
`Ruby <https://github.com/TeWu/krpc-rb>`_ 和
`Haskell <https://github.com/Cahu/krpc-hs>`_.

 * :doc:`入门指南 <getting-started>`
 * :doc:`教程和示例 <tutorials>`
 * :doc:`他人制作的客户端、服务端和工具 <third-party>`

这个MOD开放了许多与控制和与火箭交互的KSP API,
也包括支持几个流行的MOD，有Ferram Aerospace
Research, Kerbal Alarm Clock 和 Infernal Robotics.

这个功能是客户端通过运行在游戏中的服务端实现的。 客户端连接到服务端并用它执行'remote
procedures'。 这个通信只能在本地计算机网络上完成, 配置正确的话还可以运行在局域网或者广域网上。 
服务端是可扩展的 - 额外的远程程序 (分组到"services") 可以用 :doc:`Service API <extending>` 添加到服务端。

.. toctree::
   :hidden:

   getting-started
   tutorials
   cnano
   csharp
   cpp
   java
   lua
   python
   third-party
   compiling
   extending
   communication-protocols
   internals
