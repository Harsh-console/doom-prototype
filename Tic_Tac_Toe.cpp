#include<iostream>
//user input -
char user_in;
char comp_in;
bool gameOver;
gameOver = false;
char a = 'a';
char b = 'b';
char c = 'c';
char d = 'd';
char e = 'e';
char f = 'f';
char g = 'g';
char h = 'h';
char i = 'i';
void Setup()
{
    std::string Row1 = "  " + a + "  |  " + b + "  |  c  ";
    std::string Row2 = "  " + d + "  |  e  |  f  ";
    std::string Row3 = "  g  |  h  |  i  ";
    std::string Gap1 = "_____|_____|_____";
    std::string Gap2 = "_____|_____|_____";
    std::string Gap3 = "         |         |         ";
    std::cout<<Row1<<std::endl<<Gap1<<std::endl<<Row2<<std::endl
             <<Gap2<<std::endl<<Row3<<std::endl<<Gap3<<std::endl;

}
void draw()
{
    system("cls");
}
int main(){
    Setup();
    while (!gameOver)
    {

    }

    return 0;
}