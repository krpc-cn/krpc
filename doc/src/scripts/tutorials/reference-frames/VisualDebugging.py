import krpc
conn = krpc.connect(name='可视化调试')
vessel = conn.space_center.active_vessel

ref_frame = vessel.surface_velocity_reference_frame
conn.drawing.add_direction((0, 1, 0), ref_frame)
while True:
    pass
