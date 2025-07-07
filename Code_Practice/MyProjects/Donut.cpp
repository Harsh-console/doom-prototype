#include <iostream>
#include <cmath>
#include <windows.h>
#include <algorithm>

int main() {
    float step = 0.02f;
    int Screen_width = 80;
    int Screen_height = 24;
    float scale = 0.3f;
    float K2 = 5.0f;
    float R1 = 1.0f;
    float R2 = 2.0f;
    float A = 0.0f, B = 0.0f;
    float K1 = Screen_width * K2 * scale / (R1 + R2);
    float sqrt2 = sqrt(2.0f);

    int num_elements = int(2 * M_PI / step);
    float sin_[num_elements], cos_[num_elements];
    for (int i = 0; i < num_elements; i++) {
        sin_[i] = sin(i * step);
        cos_[i] = cos(i * step);
    }

    char Char_buffer[Screen_width * Screen_height];
    float z_buffer[Screen_width * Screen_height];
    const char* brightness = ".,-~:;=!*#$@";

    // Precompute trig lookup tables
    const int angle_steps = 3600;
    static float cos_table[angle_steps], sin_table[angle_steps];
    static bool tables_initialized = false;
    if (!tables_initialized) {
        for (int i = 0; i < angle_steps; ++i) {
            float angle = (2 * M_PI * i) / angle_steps;
            cos_table[i] = cos(angle);
            sin_table[i] = sin(angle);
        }
        tables_initialized = true;
    }
    auto quantize = [](float angle) {
        int idx = int(angle / (2 * M_PI) * angle_steps) % angle_steps;
        if (idx < 0) idx += angle_steps;
        return idx;
    };

    // Timing setup
    LARGE_INTEGER frequency;
    LARGE_INTEGER t_start, t_end;
    QueryPerformanceFrequency(&frequency);

    while (true) {
        QueryPerformanceCounter(&t_start);

        // Clear buffers
        for (int i = 0; i < Screen_width * Screen_height; i++) {
            Char_buffer[i] = ' ';
            z_buffer[i] = -INFINITY;
        }

        // Precompute angles
        int quantizedA = quantize(A);
        int quantizedB = quantize(B);
        float cosA = cos_table[quantizedA];
        float sinA = sin_table[quantizedA];
        float cosB = cos_table[quantizedB];
        float sinB = sin_table[quantizedB];

        for (int i = 0; i < num_elements; i++) {
            float cos_theta = cos_[i];
            float sin_theta = sin_[i];
            for (int j = 0; j < num_elements; j++) {
                float cos_phi = cos_[j];
                float sin_phi = sin_[j];

                float circle = R2 + R1 * cos_theta;
                float x = circle * (cosB * cos_phi + sinA * sinB * sin_phi) - R1 * cosA * sinB * sin_theta;
                float y = circle * (cos_phi * sinB - cosB * sinA * sin_phi) + R1 * cosA * cosB * sin_theta;
                float z = cosA * circle * sin_phi + R1 * sinA * sin_theta;

                float D = 1.0f / (z + K2);
                int xp = int(Screen_width / 2 + K1 * D * x);
                int yp = int(Screen_height / 2 - K1 * D * y * 0.5f);

                int idx = xp + Screen_width * yp;

                float L = cos_phi * cos_theta * sinB
                        - cosA * cos_theta * sin_phi
                        - sinA * sin_theta
                        + cosB * (cosA * sin_theta - cos_theta * sinA * sin_phi);

                L = (L + sqrt2) / (2.0f * sqrt2);
                L = std::max(0.0f, std::min(1.0f, L));
                int luminance_index = int(L * 11);

                if (xp >= 0 && xp < Screen_width && yp >= 0 && yp < Screen_height && D > z_buffer[idx]) {
                    z_buffer[idx] = D;
                    Char_buffer[idx] = brightness[luminance_index];
                }
            }
        }

        std::cout << "\x1b[H"; // Move cursor to top-left
        for (int i = 0; i < Screen_width * Screen_height; i++) {
            putchar(i % Screen_width ? Char_buffer[i] : '\n');
        }

        // Rotation update
        A += 0.03f;
        B += 0.02f;
        if (A > 2 * M_PI) A -= 2 * M_PI;
        if (B > 2 * M_PI) B -= 2 * M_PI;

        QueryPerformanceCounter(&t_end);
        double elapsed = double(t_end.QuadPart - t_start.QuadPart) / frequency.QuadPart;
        double fps = 1.0 / elapsed;

        // Save and restore cursor to avoid scrolling
        std::cout << "\x1b[sFPS: " << fps << "\n\x1b[u";

        //Sleep(30); // Optional delay to reduce CPU usage
    }

    return 0;
}
