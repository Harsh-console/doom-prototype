#include<iostream>
int main(){
    int lis[] = {5, 9, 8, 3, 1, 2, 7, 4, 6, 10, 0};
    int val;
    std::cout<<"Please Enter Required Number : "<<std::endl;
    std::cin>>val;
    int length = sizeof(lis) / sizeof(lis[0]);
    bool state = true;
    for(int i=0; i< length; i++){
        if (lis[i] == val){
            state = false;
            std::cout<<val <<" is there in the list and index = "<<i<<std::endl;
            break;
        }
    }
    if (state){
        std::cout<<val<<" is not there in the list!"<<std::endl;
    }
    return 0;
}