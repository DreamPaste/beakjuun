//병합 정렬 1
#include <iostream>
#include <vector>
using namespace std;
int *tmp;
void merge_sort(int a[],int p, int r,int k){
    if(p < r){
        int q = a[(p+r) /2];
        merge_sort(a, p, q, k);
        merge_sort(a, q+1, r, k);
        merge(a, p, q, r, k);
    }

}
void merge(int a[], int p, int q, int r, int k){
    int i = p;
    int j = q +1;
    int t = 1;
    

    while ((i<= q) && (j<=r))
    {
        if(a[i] <= a[j]){
            tmp[t++] = a[i++];
        }
        else{
            tmp[t++] = a[j++];
        }
        }
    
    while(i<=q){
        tmp[t++] = a[i++];
    }
    while(j<=r){
        tmp[t++] = a[j++];
    }
    i=p;
    t=1;
    while(i<=r){
        a[i++] = tmp[t++];
    }
    

}

int main(){
    int n,k;
    
    cin >> n >> k ;
    int *a = new int [n];
    for(int i=0;i<n;i++){
        cin >> a[i];
    }
    merge_sort(a,0,n-1,k);

}