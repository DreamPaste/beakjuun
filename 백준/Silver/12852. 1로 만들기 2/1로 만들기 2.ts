import readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input: string[] = [];
rl.on('line', line => input.push(line.trim())).on('close', () => {
  solve();
  process.exit();
});

function solve() {
  const n: number = Number(input[0]);

  const dp: number[] = Array(n + 1).fill(0);
  const prev: number[] = Array(n + 1).fill(0);

  for (let i = 2; i <= n; i++) {
    //이전 결과의 최소 비용
    let minCost = dp[i - 1] + 1;
    let next = i - 1;

    if (i % 2 === 0 && dp[i / 2] + 1 < minCost) {
      minCost = dp[i / 2] + 1;
      next = i / 2;
    }
    if (i % 3 === 0 && dp[i / 3] + 1 < minCost) {
      minCost = dp[i / 3] + 1;
      next = i / 3;
    }

    dp[i] = minCost;
    prev[i] = next;
  }

  const path: number[] = [];
  for (let cur = n; cur !== 0; cur = prev[cur]) {
    path.push(cur);
  }

  console.log(dp[n]);
  console.log(path.join(' '));
}
