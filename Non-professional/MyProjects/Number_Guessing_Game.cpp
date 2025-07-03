#include<iostream>
#include<ctime>
int main(){
    int min;
    int max;
    min = 1;
    max = 99;
    int input_;
    bool state;
    while (true){
        srand(time(NULL));
        int rand_num = (rand()%99) + 1;
        state = true;
        int tries = 0;
        while(state){
            std::cout<<"Guess a number between " << min << " to " << max << " : ";
            std::cin>>input_;
            tries++;
            std::cout<<std::endl;
            if (input_ == rand_num){
                std::cout<<"You Win! # of tries : " << tries<<std::endl;
                state = false;
                break;
            }
            if (input_ < rand_num){
                std::cout<<"Too Small! Try Again";
            }
            if (input_ > rand_num){
                std::cout<<"Too Large! Try Again!";
            }
        }
    }      
    return 0;
}