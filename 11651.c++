
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
bool cmp(pair<int,int> a, pair<int,int> b){
if (a.second == b.second){
    return a.first <b.first;
}
else{
    return a.second < b.second;
}
}
int main(){
    ios_base::sync_with_stdio(0); //c,c++표준 스트림 동기화 끄기
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    vector<pair<int,int>> data ; //n*2 벡터 pair로 선언
    for(int i=0; i<n;i++ ){
        int x,y;
        cin >> x >> y; //n개의 좌표 입력
        data.push_back(make_pair(x,y)); // 벡터에 넣기
    }

    sort(data.begin(),data.end(),cmp); //정렬 (cmp함수로 정렬 방식 직접 정의)
    //endl 은 시간이 느려짐
    for (int i =0;i<n;i++){
        cout << data[i].first <<" "<<data[i].second<<"\n";
        

    }
    return 0;

}