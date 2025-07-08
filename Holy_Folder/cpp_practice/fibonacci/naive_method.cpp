#include<iostream>
int fib(int n){
    if(n<=2){
        return 1;
    }
    else{
        return fib(n-1)+fib(n-2);
    }
}
int main(){
    int num;
    while(true){
        std::cout<<"Enter fabinocci number you want to find out : ";
        std::cin>>num;
        std::cout<<num << " th fabinocci number is " << fib(num)<<std::endl;
    }
    return 0;
}