import math
import time
import krpc
conn = krpc.connect(name='俯仰/偏航/滚动')
vessel = conn.space_center.active_vessel


def cross_product(u, v):
    return (u[1]*v[2] - u[2]*v[1],
            u[2]*v[0] - u[0]*v[2],
            u[0]*v[1] - u[1]*v[0])


def dot_product(u, v):
    return u[0]*v[0] + u[1]*v[1] + u[2]*v[2]


def magnitude(v):
    return math.sqrt(dot_product(v, v))


def angle_between_vectors(u, v):
    """ 计算矢量u和v之间的夹角 """
    dp = dot_product(u, v)
    if dp == 0:
        return 0
    um = magnitude(u)
    vm = magnitude(v)
    return math.acos(dp / (um*vm)) * (180. / math.pi)


while True:

    vessel_direction = vessel.direction(vessel.surface_reference_frame)

    # 获取飞船在水平面上的方向
    horizon_direction = (0, vessel_direction[1], vessel_direction[2])

    # 计算俯仰角
    # - 飞船朝向与水平面之间的夹角
    pitch = angle_between_vectors(vessel_direction, horizon_direction)
    if vessel_direction[0] < 0:
        pitch = -pitch

    # 计算偏航角
    # - 在水平面上飞船和北方之间的夹角
    north = (0, 1, 0)
    heading = angle_between_vectors(north, horizon_direction)
    if horizon_direction[2] < 0:
        heading = 360 - heading

    # 计算滚动角
    # 计算飞船朝向和向上方向之间的平面
    # 
    up = (1, 0, 0)
    plane_normal = cross_product(vessel_direction, up)
    # 计算飞船的向上方向
    vessel_up = conn.space_center.transform_direction(
        (0, 0, -1), vessel.reference_frame, vessel.surface_reference_frame)
    # 计算飞船向上方向和标准面之间的夹角
    # 
    roll = angle_between_vectors(vessel_up, plane_normal)
    # 调整其为-180到180之间的数值，
    # 右滚是+ve左滚是-ve。
    if vessel_up[0] > 0:
        roll *= -1
    elif roll < 0:
        roll += 180
    else:
        roll -= 180

    print('俯仰 = % 5.1f, 偏航 = % 5.1f, 滚动 = % 5.1f' %
          (pitch, heading, roll))

    time.sleep(1)
