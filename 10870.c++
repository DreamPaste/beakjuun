//피보나치 수
#include <iostream>
using namespace std;

int fibo(int a){
    if(a==0) return 0;
    else if(a==1) return 1;
    else return fibo(a-1)+fibo(a-2) ;
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;
    cout << fibo(n);
}