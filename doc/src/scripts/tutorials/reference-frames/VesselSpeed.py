import time
import krpc

conn = krpc.connect(name='飞船速度')
vessel = conn.space_center.active_vessel
obt_frame = vessel.orbit.body.non_rotating_reference_frame
srf_frame = vessel.orbit.body.reference_frame

while True:
    obt_speed = vessel.flight(obt_frame).speed
    srf_speed = vessel.flight(srf_frame).speed
    print('轨道速度= %.1f m/s, 地面速度= %.1f m/s' %
          (obt_speed, srf_speed))
    time.sleep(1)
