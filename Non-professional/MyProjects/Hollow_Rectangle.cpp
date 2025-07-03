#include<iostream>
int main(){
    int length, breadth;
    char Symbol = '#';

   while(true){
        std::cout<<"Give length of Required Rectangle : ";
        std::cin>>length;

        std::cout<<"Give breadth of Required Rectangle : ";
        std::cin>>breadth;
 
        for (int j = 1; j <= length; j++){
            for (int i = 1; i <= breadth; i++){
                if (i == 1 || i == breadth || j == 1 || j == length){
                    std::cout<<Symbol;
                }         
                else{
                    std::cout<<' ';
                }
                }
                std::cout<<"\n";
            }
        }
    return 0;
    }
          

