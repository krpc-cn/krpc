import krpc
conn = krpc.connect(name='导航球方向')
vessel = conn.space_center.active_vessel
ap = vessel.auto_pilot
ap.reference_frame = vessel.surface_reference_frame
ap.engage()

#此处有未知错误，建议在ap.wait()之前加上time.sleep(1)之类的
# 在导航球上将船指向北方，俯仰角0度
ap.target_direction = (0, 1, 0)
ap.wait()

# 在导航球上将飞船指向垂直向上
ap.target_direction = (1, 0, 0)
ap.wait()

# 将飞船指向西方(航向270度)，俯仰角0度
ap.target_direction = (0, 0, -1)
ap.wait()

ap.disengage()
