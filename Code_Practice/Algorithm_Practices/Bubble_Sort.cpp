#include<iostream>
int main(){
    int nums[] = {4, 6, 3, 7, 2, 9, 1, 10, 5, 8};
    int p = sizeof(nums) / sizeof(nums[0]);
    int a;
    int b;
    for(int i = 0; i < p; i++){
        for (int j = 0; j < p - 1; j ++){
            if (nums[j] > nums[j+1]){
                a = nums[j];
                b = nums[j+1];
                nums[j] = b;
                nums[j+1] = a;
            }
        }
    }
    for(const auto& num : nums){
        std::cout<<num<<std::endl;
    }
    return 0;
}