import fs = require('fs');

const [N, K] = fs.readFileSync('/dev/stdin')
    .toString().trim().split(' ').map(Number);

const p: number = 1000000007;


//factorial을 구하기 위한 연산 dp 는 메모리 초과 오류 발생
function factorial(target: number): bigint {

    let result = BigInt(1);
    for (let i = 2; i <= target; i++) {
        result = (result * BigInt(i)) % BigInt(p);
    }
    return result;
}
// 거듭제곱과 해당 나머지를 빠르게 구하기 위한 분할정복을 활용한 로직
function powmod(base: bigint, exponent: bigint, modulus: bigint){

    if (exponent === BigInt(1)) return base % modulus; 

    const half: bigint = powmod(base, exponent / BigInt(2), modulus);
    //even
    if (exponent % BigInt(2) == BigInt(0)){
        return (half * half) % modulus;
    }
    //odd
    return (half * half * base) % modulus;

}

// 페르마의 소정리를 활용한 `N! * ((N - K)! * K!)^p-2 % p ` 계산
function binomial(): bigint {


    
    const fact_K = factorial(K);
    const fact_NK = factorial(N - K);
    const fact_N = factorial(N);
    

    //base 값 계산 
    const base: bigint = BigInt((fact_NK * fact_K) % BigInt(p));
    // 분모의 역원 계산
    const inverse: bigint = powmod(base, BigInt(p - 2), BigInt(p));

    return (fact_N * inverse) % BigInt(p);

}

console.log(binomial().toString())

