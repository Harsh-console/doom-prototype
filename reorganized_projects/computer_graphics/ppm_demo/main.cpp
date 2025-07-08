#include <fstream>
#include <iostream>
#include <iomanip>
#include <cmath>  // for sin, cos

// 3D rotation matrices
void rotateX(float x, float y, float z, float angle, float& outY, float& outZ) {
    outY = y * cos(angle) - z * sin(angle);
    outZ = y * sin(angle) + z * cos(angle);
}

void rotateY(float x, float y, float z, float angle, float& outX, float& outZ) {
    outX = x * cos(angle) + z * sin(angle);
    outZ = -x * sin(angle) + z * cos(angle);
}

void rotateZ(float x, float y, float z, float angle, float& outX, float& outY) {
    outX = x * cos(angle) - y * sin(angle);
    outY = x * sin(angle) + y * cos(angle);
}

// Draw a line between two points (Bresenham's algorithm)
void drawLine(int x0, int y0, int x1, int y1, unsigned char r, unsigned char g, unsigned char b, 
              unsigned char* image, int width, int height) {
    int dx = abs(x1 - x0), sx = x0 < x1 ? 1 : -1;
    int dy = -abs(y1 - y0), sy = y0 < y1 ? 1 : -1;
    int err = dx + dy, e2;

    while (true) {
        if (x0 >= 0 && x0 < width && y0 >= 0 && y0 < height) {
            int index = (y0 * width + x0) * 3;
            image[index] = r;
            image[index + 1] = g;
            image[index + 2] = b;
        }
        if (x0 == x1 && y0 == y1) break;
        e2 = 2 * err;
        if (e2 >= dy) { err += dy; x0 += sx; }
        if (e2 <= dx) { err += dx; y0 += sy; }
    }
}

int main() {
    int width = 800;
    int height = 800;
    std::ofstream out("cube.ppm", std::ios::binary);
    out << "P6\n" << width << " " << height << "\n255\n";

    // Allocate image buffer (initialized to black)
    unsigned char* image = new unsigned char[width * height * 3]();

    float side = 100.00;
    float vertices[8][3] = {
        {0, 0, 0},      // Vertex 0
        {side, 0, 0},   // Vertex 1
        {side, side, 0}, // Vertex 2
        {0, side, 0},    // Vertex 3
        {0, 0, side},    // Vertex 4
        {side, 0, side}, // Vertex 5
        {side, side, side}, // Vertex 6
        {0, side, side}  // Vertex 7
    };

    int edges[12][2] = {
        {0, 1}, {1, 2}, {2, 3}, {3, 0}, // Bottom
        {4, 5}, {5, 6}, {6, 7}, {7, 4}, // Top
        {0, 4}, {1, 5}, {2, 6}, {3, 7}  // Vertical
    };

    // Rotation angles (in radians)
    float anglex = 0.5f;  // Tilt around X-axis
    float angley = 0.5f;  // Spin around Y-axis
    float anglez = 0.0f;  // No Z rotation for simplicity

    // Rotate and project vertices to 2D
    float projected[8][2];
    for (int i = 0; i < 8; i++) {
        float x = vertices[i][0] - side / 2;  // Center cube
        float y = vertices[i][1] - side / 2;
        float z = vertices[i][2] - side / 2;

        // Apply rotations
        float tempY, tempZ;
        rotateX(x, y, z, anglex, tempY, tempZ);
        y = tempY; z = tempZ;

        float tempX, tempZ2;
        rotateY(x, y, z, angley, tempX, tempZ2);
        x = tempX; z = tempZ2;

        // Orthographic projection (ignore Z for simplicity)
        projected[i][0] = x + width / 2;
        projected[i][1] = y + height / 2;
    }

    // Draw edges (white lines)
    for (int i = 0; i < 12; i++) {
        int v0 = edges[i][0];
        int v1 = edges[i][1];
        drawLine(
            projected[v0][0], projected[v0][1],
            projected[v1][0], projected[v1][1],
            255, 255, 255, image, width, height
        );
    }

    // Write image buffer to file
    out.write(reinterpret_cast<char*>(image), width * height * 3);
    out.close();
    delete[] image;

    std::cout << "Done. Saved as cube.ppm\n";
    return 0;
}