import fs= require('fs');

const input: string[] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [N, M]: number[] = input[0].split(' ').map(Number);

const items: number[] = input[1].split(' ').map(Number);

// 누적 합 배열 생성
const prefix: number[] = new Array(N + 1).fill(0);
for (let i = 1; i <= N; i++) {
    prefix[i] = prefix[i - 1] + items[i - 1];
}

//console.log(items)
const results: string[] = [];
for(let x = 2; x < M+2; x++){
    const [I, J] = input[x].split(' ').map(Number);
    const sum = prefix[J] - prefix[I - 1];
    results.push(sum.toString());
        
    }
    
console.log(results.join('\n'));


