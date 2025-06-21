#include<iostream>
bool gameOver;
const int width = 20;
const int height  = 20;
int x,y , fruitX, fruitY, score;
enum eDirection {STOP, LEFT, RIGHT, UP, DOWN};
eDirection dir;
void Setup()
{
    gameOver = false;
    dir = STOP;
    x = width/2;
    y = height/2;
    srand(time(NULL));
    fruitX = rand()% width;
    fruitY = rand() % height;
    score = 0;
}
void Draw()
{
    system("cls");

    // Top border
    for (int i = 0; i < width; i++)
    {
        std::cout << '#';
    }
    std::cout << std::endl;

    // Middle hollow part
    for (int i = 0; i < height - 2; i++) // height-2 because top and bottom are already handled
    {
        std::cout << '#'; // Left border
        for (int j = 0; j < width - 2; j++)
        {
            std::cout << ' '; // Hollow part
        }
        std::cout << '#' << std::endl; // Right border
    }

    // Bottom border
    for (int i = 0; i < width; i++)
    {
        std::cout << '#';
    }
    std::cout << std::endl;
}
void Input()
{
    
}
void Logic()
{
    
    }
int main()
{
    Setup();
    while (!gameOver)
    {
        Draw();
        Input();
        Logic();
    }

    return 0;
}