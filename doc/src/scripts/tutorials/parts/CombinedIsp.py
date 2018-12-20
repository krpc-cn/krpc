import krpc
conn = krpc.connect()
vessel = conn.space_center.active_vessel

active_engines = [e for e in vessel.parts.engines if e.active and e.has_fuel]

print('已激活引擎:')
for engine in active_engines:
    print('   %s在阶段%d' % (engine.part.title, engine.part.stage))

thrust = sum(engine.thrust for engine in active_engines)
fuel_consumption = sum(engine.thrust / engine.specific_impulse
                       for engine in active_engines)
isp = thrust / fuel_consumption

print('综合真空比冲(Isp) = %d 秒' % isp)
