// 좌표 압축
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    int N;
    cin >> N;
    vector<int> invec(N);
    for (int i = 0; i < N; i++)
    {

        cin >> invec[i];
    }
    vector<int> svec(invec);
    sort(svec.begin(), svec.end());
    svec.erase(unique(svec.begin(), svec.end()), svec.end()); // 연속된 중복 제거

    for (auto x : invec)
    {
        cout << lower_bound(svec.begin(), svec.end(), x) - svec.begin() << ' '; //lower_bound는 이진탐색으로 찾는 값의 주소값 반환(배열인점을 활용에 인덱스 추출 가능)
    }
}