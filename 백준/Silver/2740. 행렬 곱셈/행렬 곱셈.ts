import fs = require('fs');

const input: string[] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number);
const matA: number[][] = [];
for (let i = 0; i < N; i++){
    matA.push(input[1 + i].split(' ').map(Number));
}

const [_, K] = input[N + 1].split(' ').map(Number);
const matB: number[][] = [];
for (let i = 0; i < M; i++){
    matB.push(input[i + N + 2].split(' ').map(Number));
}


for (let i =  0; i < N; i++) {
    const line: number[] = Array(K).fill(0);
    for (let j = 0; j < K; j++) {
        let sum: number = 0;
        for (let r = 0; r < M; r++) {
            sum += matA[i][r] * matB[r][j];
        }
        line[j] = sum;
    }
    console.log(line.join(' '))
}