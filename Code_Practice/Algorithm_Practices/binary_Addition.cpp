#include<iostream>
int main(){
    int A[] = {0, 1, 0, 0, 1};
    int B[] = {0, 1, 1, 1, 1};
    int C[] = {0,0,0,0,0};
    int n = sizeof(A)/sizeof(A[0]);
    int carry =0;
    for(int i=n-1; i>=0; i--){
        int temp_num = carry + A[i]+B[i];
        C[i] = temp_num%2;
        temp_num>=2?carry =1:carry = 0;
    }
    for(const auto& num:C){
        std::cout<<num;
    }
    return 0;
}