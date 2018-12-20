import krpc
conn = krpc.connect(name='轨道方向')
vessel = conn.space_center.active_vessel
ap = vessel.auto_pilot
ap.reference_frame = vessel.orbital_reference_frame
ap.engage()

# 将飞船指向顺行方向prograde direction
ap.target_direction = (0, 1, 0)
ap.wait()

# 将飞船指向轨道法线方向orbit normal direction
ap.target_direction = (0, 0, 1)
ap.wait()

# 将飞船指向轨道径向方向orbit radial direction
ap.target_direction = (-1, 0, 0)
ap.wait()

ap.disengage()
