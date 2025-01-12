import fs = require('fs');
const input: string[] = fs.readFileSync('/dev/stdin')
    .toString().trim().split(' ');

const [A, B, C] = input.map(BigInt);

//10 11 12
//10^11 % 12
//[(10^5 % 12) * (10^5 % 12) * 10 ] % 12
//{[(10^2 % 12) * (10^2 % 12) * 10] % 12} * {[(10^2 % 12) * (10^2 % 12) * 10] % 12} * 10 % 12
//10^2 % 12 == (10 % 12) * (10 % 12) % 12 

function mod(a: bigint, b: bigint, c: bigint): bigint {
   
    if(b === BigInt(1)) return a % c;

    const half: bigint = mod(a, b / BigInt(2), c)
    //짝수일 경우
    if(b % BigInt(2) == BigInt(0)) return (half * half) % c;
    
    //홀수일 경우
    return (half * half * a ) % c ;
    
}

console.log(mod(A, B, C).toString());