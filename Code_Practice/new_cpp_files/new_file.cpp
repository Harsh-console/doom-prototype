#include <iostream>

struct Node {
    int data;      // stores the value
    Node* next;    // pointer to next node

    // Constructor to initialize node
    Node(int value) {
        data = value;
        next = nullptr;
        std::cout<<next<<std::endl;
    }
};

int main() {
    Node* first = new Node(10);  // creates a new node with value 10
    std::cout<<first<<std::endl;
    std::cout<<new Node(10)<<std::endl;
    std::cout << "Data: " << first->data << std::endl;
    std::cout << "Next: " << first->next << std::endl;

    delete first;  // good practice to free memory
    return 0;
}
