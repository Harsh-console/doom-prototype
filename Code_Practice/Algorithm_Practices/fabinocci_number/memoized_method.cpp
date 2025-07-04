#include<iostream>
#include<vector>
unsigned long long fib(int num, std::vector<unsigned long long>& memo){
    if(num<= memo.size()){
        return memo[num-1];
    }
    else{
        unsigned long long result = fib(num-1, memo) + fib(num-2, memo);
        memo.push_back(result);
        return result;
    }
}
int main(){
    std::vector<unsigned long long> memo = {1,1};
    int numb;
    while(true){
        std::cout<<"Please enter number at which you want to find out fibinocci number: ";
        std::cin>>numb;
        std::cout<<numb<<" th fabinocci number is "<<fib(numb, memo)<<std::endl;
    }
    return 0;
}