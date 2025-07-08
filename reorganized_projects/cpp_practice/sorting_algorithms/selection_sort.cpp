#include<iostream>
int min_index(int lis[], int p, int n){
    int min_index = p;
    int min_val = lis[min_index];
    for(int i = p; i < n; i++){
        if(lis[i] < lis[min_index]){
            min_index = i;
        }
    }
    return min_index;
}
int main(){
    int lis[] = {5,6,3,4,7,2,1,9,8,0};
    int n = sizeof(lis)/sizeof(lis[0]);
    std::cout<<"minimim element of list is : "<<lis[min_index(lis, 0, n)]<<std::endl;
    for(int i=0;i<n;i++){
        int a = lis[i];
        int b = min_index(lis, i, n);
        int c = lis[b];
        lis[i] = c;
        lis[b] = a;
        std::cout<<i+1<<" th data : a = "<< a<<" , b = "<<b<<" , c = " <<c<<" and list is : {";
        for(const auto& num:lis){
            std::cout<< num<<" ";
        }
        std::cout<<"}"<< " and the minimum element from " << i+1<<"th element is "<<lis[min_index(lis, i, n)]<<std::endl;
    }
    for(const auto& num:lis){
        std::cout<<num<<std::endl;
    }
    return 0;
}