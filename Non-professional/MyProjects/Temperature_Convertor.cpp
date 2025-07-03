#include <iostream>
int main(){
    while (true){
        double temp;
        char type_;
        std::cout<<"Enter the Temperature Unit(C/F) : "<<std::endl;
        std::cin>>type_;
        
        std::cout<<"Enter the Temperature : "<<std::endl;
        std::cin>>temp;

        type_ == 'C'
        ?
        std::cout<<"The Temperature is : " << (temp) * ( 1.8) + 32 << std::endl
        :
        std::cout<<"The Temperature is : " << (temp - 32) *(10.0/18)<<std::endl;
    }
    return 0;
}