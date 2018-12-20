import math
import time
import krpc

conn = krpc.connect(name='攻角')
vessel = conn.space_center.active_vessel

while True:

    d = vessel.direction(vessel.orbit.body.reference_frame)
    v = vessel.velocity(vessel.orbit.body.reference_frame)

    # 计算d和v的数量积(点积)
    dotprod = d[0]*v[0] + d[1]*v[1] + d[2]*v[2]

    # 计算v的平方根
    vmag = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    # 注意: 不需要d的大小，因为它是一个单位向量
    
    print ('dotprod= %.5f , vmag= %.5f , 差= %.5f' %(dotprod,vmag,abs(dotprod-vmag)))

    # 计算两个向量之间的夹角,但是此处dotprod和vmag之间的差小于+-0.0001就会报错
    angle = 0
    if dotprod > 0:
        angle = abs(math.acos(dotprod / vmag) * (180.0 / math.pi))

    print('攻角= %.5f 度' % angle)

    time.sleep(1)
