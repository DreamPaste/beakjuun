// 단어 정렬
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
bool cmp(string a,string b){
    if(a.length() == b.length()){
        return a<b;
    }
    else{
        return a.length() < b.length();
    }

}
int main(){
    ios_base::sync_with_stdio(0); //c,c++표준 스트림 동기화 끄기
    cin.tie(0);
    cout.tie(0);

    vector <string> v;

    int n;
    
    cin >> n;
    
    
    for(int i=0;i<n;i++){
        string s;
        cin >> s;
        if(find(v.begin(),v.end(),s) == v.end())//중복제거
            v.push_back(s);
    }
    

    sort(v.begin(),v.end(),cmp);
    
    for(int i=0;i<v.size();i++){
        cout << v[i] <<"\n" ;
    }

}