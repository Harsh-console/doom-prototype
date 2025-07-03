#include<iostream>
#include<vector>
int inf = 10000;
void merge(std::vector<int>& v, int start, int mid, int end){
    std::vector<int> v1 = {};
    std::vector<int> v2 = {};
    for(int i = 0; i< mid - start+1; i++){
        v1.push_back(v[start+i]);
    }
    for(int i = 0; i < end - mid; i++){
        v2.push_back(v[mid+i+1]);
    }
    int i=0;
    int j=0;
    int k = start;
    while(i < v1.size() && j < v2.size()){
        if(v1[i] < v2[j]){
            v[k] = v1[i];
            i++;
        }
        else{
            v[k] = v2[j];
            j++;
        }
        k++;
    }
    while(j < v2.size()){
        v[k] = v2[j];
        j++;
        k++;
    }
    while(i < v1.size()){
        v[k] = v1[i];
        i++;
        k++;
    }

}
void mergeSort(std::vector<int>& v, int i, int j){
    if(i>=j){
        return;
    }
    int mid = i + ((j - i) / 2);
    mergeSort(v, i, mid);
    mergeSort(v, mid+1, j);
    merge(v, i, mid, j);
}

int main(){
    std::vector<int> v = {5,1,4,2,8,7,0,9,3,6};
    mergeSort(v, 0, v.size()-1);
    for(const auto& num:v){
        std::cout<<num<<std::endl;
    }
    return 0;
}
