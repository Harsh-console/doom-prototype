import pygame
import math
import numpy as np
from pygame.locals import *

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Rotating Colored Cube")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)

# Cube parameters
CUBE_SIZE = 100
HALF_SIZE = CUBE_SIZE // 2

# Cube vertices (3D coordinates)
vertices = np.array([
    [-HALF_SIZE, -HALF_SIZE, -HALF_SIZE],
    [HALF_SIZE, -HALF_SIZE, -HALF_SIZE],
    [HALF_SIZE, HALF_SIZE, -HALF_SIZE],
    [-HALF_SIZE, HALF_SIZE, -HALF_SIZE],
    [-HALF_SIZE, -HALF_SIZE, HALF_SIZE],
    [HALF_SIZE, -HALF_SIZE, HALF_SIZE],
    [HALF_SIZE, HALF_SIZE, HALF_SIZE],
    [-HALF_SIZE, HALF_SIZE, HALF_SIZE]
], dtype=float)

# Cube faces
faces = [
    {"indices": [0, 1, 2, 3], "color": RED},     # Front
    {"indices": [4, 5, 6, 7], "color": GREEN},   # Back
    {"indices": [0, 1, 5, 4], "color": BLUE},    # Bottom
    {"indices": [2, 3, 7, 6], "color": YELLOW},  # Top
    {"indices": [0, 3, 7, 4], "color": MAGENTA}, # Left
    {"indices": [1, 2, 6, 5], "color": CYAN}     # Right
]

# Camera
zoom = 5
camera_distance = CUBE_SIZE * zoom
fov = math.radians(60)
aspect_ratio = WIDTH / HEIGHT

# Rotation
angle_x, angle_y, angle_z = 0, 0, 0
rotation_speed = 0.01

# Rotation matrices
def rotation_matrix_x(angle):
    return np.array([
        [1, 0, 0],
        [0, math.cos(angle), -math.sin(angle)],
        [0, math.sin(angle), math.cos(angle)]
    ])

def rotation_matrix_y(angle):
    return np.array([
        [math.cos(angle), 0, math.sin(angle)],
        [0, 1, 0],
        [-math.sin(angle), 0, math.cos(angle)]
    ])

def rotation_matrix_z(angle):
    return np.array([
        [math.cos(angle), -math.sin(angle), 0],
        [math.sin(angle), math.cos(angle), 0],
        [0, 0, 1]
    ])

# Projection
def project_point(point):
    x, y, z = point
    z += camera_distance
    if z > 0:
        x_ndc = (x * math.tan(fov / 2)) / (z * aspect_ratio)
        y_ndc = (y * math.tan(fov / 2)) / z
        screen_x = (x_ndc + 0.5) * WIDTH
        screen_y = (0.5 - y_ndc) * HEIGHT
        return (screen_x, screen_y, z)
    return None

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False

    screen.fill(BLACK)

    # Update angles
    angle_x += rotation_speed
    angle_y += rotation_speed * 1.5
    angle_z += rotation_speed * 0.5

    # Combined rotation matrix
    rotation = rotation_matrix_z(angle_z) @ rotation_matrix_y(angle_y) @ rotation_matrix_x(angle_x)
    
    # Rotate vertices
    rotated_vertices = [rotation @ v for v in vertices]

    # Project vertices
    projected_vertices = [project_point(v) for v in rotated_vertices]

    # Draw faces
    faces_to_draw = []
    for face in faces:
        idx = face["indices"]
        verts_3d = [rotated_vertices[i] for i in idx]
        verts_2d = [projected_vertices[i] for i in idx]
        
        if None in verts_2d:
            continue

        # Calculate face normal
        normal = np.cross(
            verts_3d[1] - verts_3d[0],
            verts_3d[2] - verts_3d[0]
        )
        view_vector = verts_3d[0] - np.array([0, 0, -camera_distance])
        
        if np.dot(normal, view_vector) < 0:  # Face is visible
            avg_depth = sum(v[2] for v in verts_2d) / 4
            faces_to_draw.append({
                "points": [(v[0], v[1]) for v in verts_2d],
                "color": face["color"],
                "depth": avg_depth
            })

    # Draw sorted faces
    faces_to_draw.sort(key=lambda f: -f["depth"])
    for f in faces_to_draw:
        pygame.draw.polygon(screen, f["color"], f["points"])
        pygame.draw.polygon(screen, WHITE, f["points"], 1)

    # UI text
    font = pygame.font.SysFont("Arial", 16)
    text = font.render("Rotating 3D Cube - Multiple Faces Visible", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
