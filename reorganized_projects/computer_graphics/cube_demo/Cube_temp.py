import pygame
import math

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Perspective parameters
fov = 400

# Define cube vertices (centered at origin)
cube_vertices = [
    [-100, -100, -100],
    [100, -100, -100],
    [100, 100, -100],
    [-100, 100, -100],
    [-100, -100, 100],
    [100, -100, 100],
    [100, 100, 100],
    [-100, 100, 100],
]

# Each face is a list of 4 vertex indices
cube_faces = [
    (0, 1, 2, 3),  # back
    (4, 5, 6, 7),  # front
    (0, 1, 5, 4),  # bottom
    (2, 3, 7, 6),  # top
    (1, 2, 6, 5),  # right
    (0, 3, 7, 4),  # left
]

# Face colors
face_colors = [
    (255, 0, 0),     # red
    (0, 255, 0),     # green
    (0, 0, 255),     # blue
    (255, 255, 0),   # yellow
    (255, 0, 255),   # magenta
    (0, 255, 255),   # cyan
]

# Rotation angles
angle_x = 0
angle_y = 0
angle_z = 0

def rotate(vertex, ax, ay, az):
    x, y, z = vertex

    # X rotation
    cos_x, sin_x = math.cos(ax), math.sin(ax)
    y, z = y * cos_x - z * sin_x, y * sin_x + z * cos_x

    # Y rotation
    cos_y, sin_y = math.cos(ay), math.sin(ay)
    x, z = x * cos_y + z * sin_y, -x * sin_y + z * cos_y

    # Z rotation
    cos_z, sin_z = math.cos(az), math.sin(az)
    x, y = x * cos_z - y * sin_z, x * sin_z + y * cos_z

    return [x, y, z]

def project(vertex):
    x, y, z = vertex
    z += 500  # move cube in front of camera
    if z <= 0.1:
        z = 0.1
    scale = fov / z
    x_proj = int(x * scale + width // 2)
    y_proj = int(-y * scale + height // 2)
    return (x_proj, y_proj)

# ------------------ MAIN LOOP ------------------
running = True
while running:
    clock.tick(60)
    screen.fill((10, 10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rotate angles
    angle_x += 0.02
    angle_y += 0.015
    angle_z += 0.01

    # Rotate and project all vertices
    transformed = [rotate(v, angle_x, angle_y, angle_z) for v in cube_vertices]
    projected = [project(v) for v in transformed]

    # Draw faces (sorted by depth to simulate 3D overlap)
    face_depths = []
    for i, face in enumerate(cube_faces):
        z_avg = sum(transformed[idx][2] for idx in face) / 4
        face_depths.append((z_avg, i))

    # Draw from farthest to nearest
    for _, face_idx in sorted(face_depths):
        face = cube_faces[face_idx]
        point_list = [projected[i] for i in face]
        pygame.draw.polygon(screen, face_colors[face_idx], point_list)

    # Draw from farthest to closest
    for _, face_idx in sorted(face_depths):
        face = cube_faces[face_idx]
        point_list = [projected[i] for i in face]
        pygame.draw.polygon(screen, face_colors[face_idx], point_list)

    pygame.display.flip()
    pygame.display.set_caption(f"3D Cube - FPS: {int(clock.get_fps())}")

pygame.quit()
