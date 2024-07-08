import sys
n, k = map(int, input().split())
arr = list(map(int,sys.stdin.readline().split()))
cnt=1
ans= -1
def mergeSort(arr, first, end):
    if(first < end):
        mid = (first + end)//2
        mergeSort(arr, first, mid)
        mergeSort(arr, mid+1, end)
        merge(arr, first, mid, end)
        

def merge(arr, first, mid, end):
    global cnt,ans
    i =first; j = mid+1
    temp=[]
    while(i <= mid and j <= end):
        if(arr[i] <= arr[j]):
           temp.append(arr[i])
           i+=1 
        else :
            temp.append(arr[j])
            j+=1 
        
    
    while(i <= mid): # 왼쪽이 남은 경우
        temp.append(arr[i])
        i+=1 
    while(j<= end): #오른쪽 남은 경우
        temp.append(arr[j])
        j+=1 
    
    #결과저장
    i = first; t =0
    while(i<=end):
        arr[i] = temp[t]
        if k == cnt :
            ans =arr[i]
        t+=1; i+=1
        cnt+=1

mergeSort(arr,0,n-1)
print(ans)