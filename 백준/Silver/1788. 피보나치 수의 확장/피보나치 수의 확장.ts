import * as readline from 'readline';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const MOD = 1_000_000_000;

rl.on('line', (line) => {
  const n = Number(line.trim());

  const absN = Math.abs(n);
  const dp: number[] = new Array(absN + 2).fill(0);

  // 피보나치 초기값
  dp[0] = 0;
  dp[1] = 1;

  // Bottom-up 계산
  for (let i = 2; i <= absN; i++) {
    dp[i] = (dp[i - 1] + dp[i - 2]) % MOD;
  }

  const fib = dp[absN];

  if (n === 0) {
    console.log(0);
    console.log(0);
  } else {
    // 음수인 경우 부호 조절
    const sign = n < 0 && absN % 2 === 0 ? -1 : 1;
    console.log(sign);
    console.log(fib);
  }

  rl.close();
});