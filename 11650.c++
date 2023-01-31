// 좌표 정렬하기

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    ios_base::sync_with_stdio(0); //c,c++표준 스트림 동기화 끄기
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    vector<vector<int>> data (n,vector<int>(2,0)); //n*2 벡터 0 으로 초기화
    for(int i=0; i<n;i++ ){
        cin >>data[i][0] >> data[i][1]; //n개의 좌표 입력
    }

    sort(data.begin(),data.end()); //정렬
    //endl 은 시간이 느려짐
    for (int i =0;i<n;i++){
        cout << data[i][0] <<" "<<data[i][1]<<"\n";
        

    }
    return 0;

}