import readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input: string[] = [];
rl.on('line', line => {
  input.push(line.trim());
}).on('close', () => {
  solve();
  process.exit();
});

function solve() {
  let sum: number = 0;
  let idx: number = 0;
  for (let i = 0; i < 5; i++) {
    const cur: number = input[i]
      .split(' ')
      .map(Number)
      .reduce((acc, el) => (acc += el));
    if (cur > sum) {
      sum = cur;
      idx = i + 1;
    }
  }
  console.log(idx, sum);
}
