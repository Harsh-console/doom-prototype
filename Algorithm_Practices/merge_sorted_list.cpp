#include<iostream>
int main(){
    int infinity = 1000;
    int lis1[]  = {1,3,5,7,9, infinity};
    int lis2[] = {2,4,6,8, infinity};
    int lis3[] = {0,0,0,0,0,0,0,0,0};
    int i = 0;
    int j = 0;
    int n1 = sizeof(lis1)/sizeof(lis1[0]) - 1;
    int n2 = sizeof(lis1)/sizeof(lis1[0]) - 1;
    for(int k = 0; k < n1+n2; k++){
        if(lis1[i] < lis2[j]){
            lis3[k] = lis1[i];
            i+=1;
        }
        else{
            lis3[k] = lis2[j];
            j+=1;
        }
    }
    for(const auto& num:lis3){
        std::cout<<num<<std::endl;
    }
    return 0;
}