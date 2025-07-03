#include<iostream>
int main()
{ 
    int x;
    int count = 0;
    while(true)
    {
        std::cin>>x;
        count++;
        std::cout<<"Attempt No. " << count<<'\n';
        if (std::cin.fail())
        {
            std::cout<<"Invalid Input!\n";
            std::cin.clear();
            std::cin.ignore(1000, '\n');
        }
        else
        {
            std::cout<<"Success\n";
        }
    }
        return 0;
}