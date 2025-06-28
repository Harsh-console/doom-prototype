#include<iostream>
int main(){
    int lis[] = {5, 9, 8, 3, 1, 2, 7, 4, 6, 10, 0};
    int length = sizeof(lis) / sizeof(lis[0]);
    for (int i = 1; i < length; i++){
        int temp_num = lis[i];
        for(int j = i-1; j != -1; j--){
            if(lis[j] > temp_num){
                lis[j+1] = lis[j];
             }
            if (lis[j] < temp_num){
                break;
            }
        lis[j] = temp_num;
        }
    }
    for(const auto& num : lis){
        std::cout<<num<<std::endl;
    }  
    return 0;
}