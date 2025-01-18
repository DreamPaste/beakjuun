import fs = require('fs');

// n <= 1,000,000,000,000,000

const n: bigint  = BigInt(fs.readFileSync('/dev/stdin').toString().trim());
const mod: bigint = BigInt(1000000007);

calculateFibo(n);

//--------------------------

//mod가 적용된 행렬 곱셈
function  mulMatrix(matA: bigint[][], matB: bigint[][]) {

    const returnMatrix = [[BigInt(0), BigInt(0)], [BigInt(0), BigInt(0)]];
    for(let i = 0; i < 2; i++){
        for(let j = 0;  j < 2; j++){
            let sum = BigInt(0);
            for(let k = 0; k < 2; k++){
                sum += (matA[i][k] * matB[k][j]) % mod;
            }
            returnMatrix[i][j] = sum % mod;
        }
    }
    return returnMatrix;
}

//분할 정복을 이용한 행렬 거듭제곱
function matrixPower(matrix: bigint[][], exponent: bigint): bigint[][] {
    
    if (exponent === BigInt(1)) {
        return matrix;
    }
    
    let half = matrixPower(matrix, exponent / BigInt(2));

    let half_square = mulMatrix(half, half);
    

    if (exponent % BigInt(2) === BigInt(0)) {
        return half_square;
    }
    return  mulMatrix(half_square, matrix);
}
//피보니치 구하기
function calculateFibo(n: bigint){
    const baseMat = [[BigInt(1), BigInt(1)], [BigInt(1), BigInt(0)]];
    
    if(n === BigInt(0)){
        console.log(0);
    }
    else{
        const resultMat =  matrixPower(baseMat, n);
        console.log((resultMat[0][1] % mod).toString());
    }
}
