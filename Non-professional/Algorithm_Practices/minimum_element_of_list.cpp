#include<iostream>
int main(){
    int lis[] = {3,1,2};
    int min_index=0;
    int min_val = lis[min_index];
    for(int i=0; i<3; i++){
        std::cout<<"In "<<i+1<<" th step lis[i] = "<<lis[i]<<" and min_val = "<<lis[min_index]<<std::endl;
        if(lis[i]<lis[min_index]){
            min_index = i;
        }
        std::cout<<"Min Index after "<<i+1<<"th step is "<<min_index<<std::endl;
    }
    std::cout<<min_index<<std::endl;
    std::cout<<"minimum value in list is : "<<lis[min_index];
    return 0;
}