#include <iostream>      // for cout
#include <thread>        // for threads
#include <vector>        // for vector (array)
#include <chrono>        // for sleeping

// Function to be run by each thread
void sleep_and_print(int n) {
    std::this_thread::sleep_for(std::chrono::milliseconds(n * 100));  // sleep n*100 milliseconds
    std::cout << n << " ";
}

int main() {
    // 1. Create a list of numbers
    std::vector<int> numbers = {4, 2, 7, 1, 3};

    // 2. Vector to store threads
    std::vector<std::thread> threads;

    // 3. Launch a thread for each number
    for (int num : numbers) {
        threads.push_back(std::thread(sleep_and_print, num));
    }

    // 4. Wait for all threads to finish
    for (std::thread &t : threads) {
        t.join();
    }

    std::cout << "\nDone!" << std::endl;
    return 0;
}
