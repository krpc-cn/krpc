import krpc
conn = krpc.connect(name='地面顺行')
vessel = conn.space_center.active_vessel
ap = vessel.auto_pilot
ap.reference_frame = vessel.surface_velocity_reference_frame

# 将飞船指向地面参考框架的顺行方向
ap.target_direction = (0, 1, 0)
ap.engage()
ap.wait()
ap.disengage()
