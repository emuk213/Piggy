import add
from add import rectangle3D, cube

def body(center, size, a, color):
    volume = size[0] * size[1] * size[2]
    cube_size = (volume / a) ** (1 / 3)

    # kiek kubu
    num_x = int(size[0] / cube_size)
    num_y = int(size[1] / cube_size)
    num_z = int(size[2] / cube_size)

    #pakoreguoja staciakampio dydi kad normaliai tilptu visi kubeliai
    effective_size = [num_x * cube_size, num_y * cube_size, num_z * cube_size]

    #apskaiciuojama staciakampio kairio sono (apacioj) koord, nuo ten delios kubelius
    start_x = center[0] - effective_size[0] / 2
    start_y = center[1] - effective_size[1] / 2
    start_z = center[2] - effective_size[2] / 2

    #staciakampi uzpildo kubeliais
    for i in range(num_x):
        for j in range(num_y):
            for k in range(num_z):
                cube_center = [
                    start_x + (i + 0.5) * cube_size,
                    start_y + (j + 0.5) * cube_size,
                    start_z + (k + 0.5) * cube_size
                ]
                cube(cube_center, cube_size, color)

#veidas:
def face(center):
    x = center[0]
    y = center[1]
    z = center[2]

    n1 = 0

    #nosis:
    for i in range(2):
        rectangle3D([x, y + n1, z], [0.7, 0.2, 0.1], [255, 198, 197])
        n1 = 0.4
    rectangle3D([x, y + 0.2, z], [0.32, 0.202, 0.1], [255, 173, 172])

    n2 = 0.255

    for j in range(2):
        rectangle3D([x - n2, y + 0.2, z], [0.19, 0.202, 0.1], [81, 21, 21])
        n2 = -0.255

    #akys
    e1 = 0.6
    e2 = -0.445
    e3 = 0.19
    for k in range(2):
        rectangle3D([x + e2, y+e1, z],[0.19, 0.19, 0.1], [255, 255, 255])
        rectangle3D([x + e2 - e3, y + e1, z], [0.19, 0.19, 0.1], [0, 0, 0])
        e2 = -e2
        e3 = -e3

def keupre(center):
    x = center[0]
    y = center[1]
    z = center[2]
    add.cylinder([x, y, z], [x, y + 0.365, z],0.5,100, [255, 255, 255])
    add.cone([x, y + 0.365, z],[x, y + 1.5, z],0.5,100, [255, 0, 0])
    add.sphere([x, y + 1.5, z], 0.15, 100, [255, 255, 255])


#kojos:
x1 = 0.7
xn1 = 0.9
for i in range(2):
    body([x1, -1.4, -1.2], [1, 1.3, 1], 50, [255, 140, 138])
    rectangle3D([xn1, -1.9, -0.8], [0.19, 0.19, 0.1], [82, 38, 37])
    rectangle3D([xn1 - 0.4, -1.9, -0.8], [0.19, 0.19, 0.1], [82, 38, 37])
    x1 = x1 - 1.4
    xn1 = xn1 - 1.4


z1 = -1.2 + 2.4
x2 = 0.7
xn2 = 0.9
zn1 = 1.6
for a in range(2):
    body([x2, -1.4, z1], [1, 1.3, 1], 50, [255, 140, 138])
    rectangle3D([xn2, -1.9, zn1], [0.19, 0.19, 0.1], [82, 38, 37])
    rectangle3D([xn2 - 0.4, -1.9, zn1], [0.19, 0.19, 0.1], [82, 38, 37])
    x2 = x2 - 1.4
    xn2 = xn2 - 1.4

body([0, 0, 0], [2.5, 1.8, 3.6], 6000, [255, 140, 138])
body([0, 0.5, 2], [1.6, 1.6, 1.6], 4000, [255, 140, 138])
face([0, 0.1, 2.8])
keupre([0, 1.1, 2])

add.off("piggy.off")



