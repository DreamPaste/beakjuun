import fs = require('fs');

const input: string[] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N: number = parseInt(input[0]);

const A: number[] = input[1].split(' ').map(Number);

// 수열 A의 크기 N이 1,000,000,000 정도로 매우 클 수 있고, LIS 문제이므로 이분 탐색을 활용가능
const LIS: number[] = [A[0]]

// 이분 탐색을 통해 LIS 배열에서 필요한 인덱스를 반환
function search(target: number){
    
    let start : number = 0;
    let end : number = LIS.length - 1;
    let mid : number ;
    while(start < end){
        
        mid = Math.floor( (start + end) / 2);
        if (target > LIS[mid]){
            start = mid + 1;
        }
        else {
            end = mid;
        }
    }
    return start;
}

for(let i = 1; i < N; i++) {
    if (A[i] > LIS[LIS.length - 1]){
        LIS.push(A[i]);
    }
    else {
        const index = search(A[i]);
        LIS[index] = A[i];
    }
}
console.log(LIS.length)

