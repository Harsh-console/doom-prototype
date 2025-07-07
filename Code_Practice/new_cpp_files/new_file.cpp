#include<iostream>
#include<vector>
void func(std::vector<int> &v){
    v.push_back(5);
    return;
}
int main(){
    std::vector<int> a = {1};
    func(a);
    for(const auto& num:a){
        std::cout<<num<<std::endl;
    }
    return 0;
}