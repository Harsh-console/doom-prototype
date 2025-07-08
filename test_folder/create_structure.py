import os

# Base directory to create everything in
BASE = "reorganized_projects"

# List of folders to create
folders = [
    "games/doom_prototype",
    "games/doom_full",
    "games/snake_game",
    "games/chess_game",
    "games/turn_based_battle",
    "games/misc_game_experiments",

    "visuals_animations/sorting",
    "visuals_animations/raycasts",

    "cpp_practice/sorting_algorithms",
    "cpp_practice/searching_algorithms",
    "cpp_practice/misc_algorithms",
    "cpp_practice/fibonacci",

    "computer_graphics/3d_renderer/resources",
    "computer_graphics/cube_demo",
    "computer_graphics/ppm_demo",

    "opengl_projects/Include/glad",
    "opengl_projects/Include/KHR",
    "opengl_projects/src",

    "web_projects/intro_html",
    "web_projects/snake_game_web",

    "numpy_experiments",

    "shared_assets/images"
]

# Create folders
for folder in folders:
    path = os.path.join(BASE, folder)
    os.makedirs(path, exist_ok=True)
    print(f"✅ Created: {path}")
