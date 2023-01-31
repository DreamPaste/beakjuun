// 나이순 정렬


#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp(pair<int,string> a,pair<int,string> b){

    return a.first < b.first;
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    vector <pair<int,string>> v;
    int N;
    cin >> N;
    for (int i =0; i<N; i++){

        int age;
        string name;

        cin >> age >> name ;
        v.push_back(make_pair(age,name));
    }
    stable_sort(v.begin(),v.end(),cmp); //안정 정렬(동일한 값에 대해 기존 순서 보장)
    
    for(int i=0; i<N;i++){
        cout << v[i].first <<' '<<v[i].second <<'\n' ;

    }


}