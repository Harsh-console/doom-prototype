# we will draw cube using draw polygon from four given vertices
import pygame
import math
pygame.init()
#constants
RES = WIDTH, HEIGHT = 1200, 600
WHITE = (255, 255, 255)
BLACK = (0,0,0)
side = 200
s = side//2
FPS = 60
pi = math.pi
screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

#Cube Parameters
A, B, C = 0.1, 0.1, 0.1 # in radians
vertices = [] # contain lis [x, y, z]
faces = [] # contains [[x,y,z], color]


vertices = [
    [-s, -s, -s],  # 0
    [ s, -s, -s],  # 1
    [ s,  s, -s],  # 2
    [-s,  s, -s],  # 3
    [-s, -s,  s],  # 4
    [ s, -s,  s],  # 5
    [ s,  s,  s],  # 6
    [-s,  s,  s],  # 7
]

#angle memo
sin_lis = []
step = 0.05 # in radians
for i in range(int(2*pi / step) + 1):
    sin_lis.append(math.sin(i*step))
def rotate_x(x, y, z, angle):
    sinAngle = sin_lis[int(angle//step)]
    cosAngle = sin_lis[int(((pi/2) - angle) // step)]
    return (y*cosAngle - z*sinAngle, y*sinAngle + z*cosAngle)
def rotate_y(x, y, z, angle):
    sinAngle = sin_lis[int(angle//step)]
    cosAngle = sin_lis[int(((pi/2) - angle) // step)]
    return (x*sinAngle + z*cosAngle, x*cosAngle - z*sinAngle)  
def rotate_z(x, y, z, angle):
    sinAngle = sin_lis[int(angle//step)]
    cosAngle = sin_lis[int(((pi/2) - angle) // step)]
    return (x*cosAngle - y*sinAngle, x*sinAngle+y*cosAngle)

while True:
    rotated_vertices = []
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #find updated coordinate of vertices
    for vertex in vertices:
        x, y, z = vertex
        y_, z_ = rotate_x(x, y, z, A)
        x_, z__ = rotate_y(x, y_, z_, B)
        x__, y__ = rotate_z(x_, y_, z__, C)
        rotated_vertices.append([x__, y__, z__])


    rotated_faces = [
        [rotated_vertices[0], rotated_vertices[1], rotated_vertices[2], rotated_vertices[3], (255, 0, 0)],
        [rotated_vertices[4], rotated_vertices[5], rotated_vertices[6], rotated_vertices[7], (0, 255, 0)],
        [rotated_vertices[0], rotated_vertices[1], rotated_vertices[5], rotated_vertices[4], (0, 0, 255)],
        [rotated_vertices[2], rotated_vertices[3], rotated_vertices[7], rotated_vertices[6], (255, 255, 0)],
        [rotated_vertices[1], rotated_vertices[2], rotated_vertices[6], rotated_vertices[5], (0, 255, 255)],
        [rotated_vertices[0], rotated_vertices[3], rotated_vertices[7], rotated_vertices[4], (255, 0, 255)]
    ]


    def project(x, y, z):
        factor = 400 / (z + 400)  # Perspective scaling
        screen_x = int(x * factor + WIDTH // 2)
        screen_y = int(-y * factor + HEIGHT // 2)
        return (screen_x, screen_y)

    for vertex in vertices:
        x, y, z = vertex
        y, z = rotate_x(x, y, z, A)
        z, x = rotate_y(x, y, z, B)
        x, y = rotate_z(x, y, z, C)
        rotated_vertices.append([x, y, z])

    for face in rotated_faces:
        screen_face = [project(*v) for v in face[:4]]
        pygame.draw.polygon(screen, face[4], screen_face)

    A += 0.01
    B += 0.01
    C += 0.01

    if A > 2 * pi: A -= 2 * pi
    if B > 2 * pi: B -= 2 * pi
    if C > 2 * pi: C -= 2 * pi

    pygame.display.flip()
    clock.tick(FPS)
    pygame.display.set_caption(f"FPS: {clock.get_fps():.1f}")
    