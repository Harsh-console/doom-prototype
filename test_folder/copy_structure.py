import os
import shutil

OLD_BASE = "."  # adjust if running from a different root
NEW_BASE = "reorganized_projects"

copy_plan = {
    "games/doom_prototype": [
        "Code_Practice/python_files_harsh/DOOM_prototype/main.py",
        "Code_Practice/python_files_harsh/DOOM_prototype/rough_.py",
    ],
    "games/doom_full": [
        "Code_Practice/python_files_harsh/DOOM/main.py",
        "Code_Practice/python_files_harsh/DOOM/map.py",
        "Code_Practice/python_files_harsh/DOOM/player.py",
        "Code_Practice/python_files_harsh/DOOM/settings.py",
    ],
    "games/snake_game": [
        "Code_Practice/python_files_harsh/Games/1_Snake_game.py",
        "Code_Practice/python_files_harsh/Games/2_Snake_game.py",
    ],
    "games/chess_game": [
        "Code_Practice/python_files_harsh/Games/chess_.py",
    ],
    "games/turn_based_battle": [
        "Code_Practice/python_files_harsh/turn_based_battle/main.py",
        "Code_Practice/python_files_harsh/turn_based_battle/game.py",
        "Code_Practice/python_files_harsh/turn_based_battle/grid.py",
        "Code_Practice/python_files_harsh/turn_based_battle/unit.py",
        "Code_Practice/python_files_harsh/turn_based_battle/constants.py",
    ],
    "visuals_animations/sorting": [
        "Code_Practice/python_files_harsh/Games/sorting_random_lines.py",
        "Code_Practice/python_files_harsh/Games/random_lsorted_lines_animation.py",
    ],
    "visuals_animations/raycasts": [
        "Code_Practice/python_files_harsh/Games/rotating_circle_with ray.py",
    ],
    "cpp_practice/sorting_algorithms": [
        "Code_Practice/Algorithm_Practices/Bubble_Sort.cpp",
        "Code_Practice/Algorithm_Practices/Insertion_Sort.cpp",
        "Code_Practice/Algorithm_Practices/merge_sort.cpp",
        "Code_Practice/Algorithm_Practices/selection_sort.cpp",
        "Code_Practice/Algorithm_Practices/sleep_sort.cpp",
    ],
    "cpp_practice/searching_algorithms": [
        "Code_Practice/Algorithm_Practices/liner_search.cpp",
        "Code_Practice/Algorithm_Practices/peak_finder.cpp",
        "Code_Practice/Algorithm_Practices/minimum_element_of_list.cpp",
    ],
    "cpp_practice/misc_algorithms": [
        "Code_Practice/Algorithm_Practices/merge_sortedlist.cpp",
        "Code_Practice/Algorithm_Practices/binary_Addition.cpp",
        "Code_Practice/Algorithm_Practices/Dijkstra's Algorithm.py",
    ],
    "cpp_practice/fibonacci": [
        "Code_Practice/Algorithm_Practices/fabinocci_number/memoized_method.cpp",
        "Code_Practice/Algorithm_Practices/fabinocci_number/naive_method.cpp",
    ],
    "computer_graphics/3d_renderer": [
        "Code_Practice/Computer_Graphics/Rendering_System/3D_Renderer/main.py",
        "Code_Practice/Computer_Graphics/Rendering_System/3D_Renderer/camera.py",
        "Code_Practice/Computer_Graphics/Rendering_System/3D_Renderer/matrix_functions.py",
        "Code_Practice/Computer_Graphics/Rendering_System/3D_Renderer/object_3d.py",
        "Code_Practice/Computer_Graphics/Rendering_System/3D_Renderer/projection.py",
    ],
    "computer_graphics/3d_renderer/resources": [
        "Code_Practice/Computer_Graphics/Rendering_System/3D_Renderer/resources/t_34_obj.obj",
    ],
    "computer_graphics/cube_demo": [
        "Code_Practice/Computer_Graphics/Rendering_System/Cube/Cube.py",
        "Code_Practice/Computer_Graphics/Rendering_System/Cube/Cube_temp.py",
        "Code_Practice/Computer_Graphics/Rendering_System/Cube/main_Cube.py",
    ],
    "computer_graphics/ppm_demo": [
        "Code_Practice/Computer_Graphics/finclude_with_ppm/main.cpp",
        "Code_Practice/Computer_Graphics/finclude_with_ppm/view_image.py",
        "Code_Practice/Computer_Graphics/finclude_with_ppm/cube.ppm",
    ],
    "opengl_projects": [
        "Code_Practice/openGL/main.cpp",
    ],
    "opengl_projects/Include/glad": [
        "Code_Practice/openGL/Include/glad/glad.h",
    ],
    "opengl_projects/Include/KHR": [
        "Code_Practice/openGL/Include/KHR/khrplatform.h",
    ],
    "opengl_projects/src": [
        "Code_Practice/openGL/src/glad.c",
    ],
    "web_projects/intro_html": [
        "Code_Practice/Web_Development/Introduction/main_html.html",
    ],
    "web_projects/snake_game_web": [
        "Code_Practice/Web_Development/Snake_Game/index.html",
        "Code_Practice/Web_Development/Snake_Game/script.js",
        "Code_Practice/Web_Development/Snake_Game/style.css",
    ],
    "shared_assets/images": [
        "Code_Practice/python_files_harsh/man.png",
        "Code_Practice/python_files_harsh/player_walk_1.png",
        "Code_Practice/python_files_harsh/Games/ground.png",
        "Code_Practice/python_files_harsh/Games/sky.png",
        "Code_Practice/python_files_harsh/Games/snail1.png",
    ]
}

# Run the copy operation
for dest_folder, file_list in copy_plan.items():
    dest_full = os.path.join(NEW_BASE, dest_folder)
    os.makedirs(dest_full, exist_ok=True)
    for file in file_list:
        src = os.path.join(OLD_BASE, file)
        dst = os.path.join(dest_full, os.path.basename(file))
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"✅ Copied: {src} -> {dst}")
        else:
            print(f"❌ File not found: {src}")
