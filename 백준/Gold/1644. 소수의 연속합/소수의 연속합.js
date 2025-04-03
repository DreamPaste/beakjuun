// fs 모듈을 이용해 입력을 받습니다.
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();

// 입력: 자연수 N
const N = Number(input);

// 에라토스테네스의 체를 이용하여 N 이하의 소수를 구하는 함수
function getPrimes(n) {
    // 0부터 n까지 모두 소수라고 가정하여 true로 초기화 (0, 1은 소수가 아님)
    const isPrime = new Array(n + 1).fill(true);
    isPrime[0] = isPrime[1] = false;
    
    // 2부터 sqrt(n)까지 검사
    for (let i = 2; i * i <= n; i++) {
        if (isPrime[i]) {
            // i의 배수들을 모두 소수가 아니라고 표시
            for (let j = i * i; j <= n; j += i) {
                isPrime[j] = false;
            }
        }
    }
    
    // 소수인 숫자들을 배열에 저장하여 반환
    const primes = [];
    for (let i = 2; i <= n; i++) {
        if (isPrime[i]) primes.push(i);
    }
    return primes;
}

// N이 1 이하인 경우 소수가 없으므로 0 출력
if (N < 2) {
    console.log(0);
    process.exit(0);
}

// N 이하의 소수 배열 생성
const primes = getPrimes(N);

// 슬라이딩 윈도우 기법을 이용하여 연속된 소수의 합이 N이 되는 경우의 수 구하기
let count = 0;      // 조건을 만족하는 경우의 수
let sum = 0;        // 현재 윈도우의 합
let left = 0, right = 0;

while (right < primes.length) {
    // right 포인터가 가리키는 소수를 합에 추가
    sum += primes[right];

    // 현재 합이 N 이상이면, left 포인터를 이동하며 조건을 확인
    while (sum >= N && left <= right) {
        if (sum === N) {
            count++;  // 합이 정확히 N이면 경우의 수 증가
        }
        // left 포인터에 해당하는 소수를 합에서 빼고, left 포인터 증가
        sum -= primes[left];
        left++;
    }
    // right 포인터를 이동하여 다음 소수를 포함
    right++;
}

// 최종적으로 구한 경우의 수 출력
console.log(count);
