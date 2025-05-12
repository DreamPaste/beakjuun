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
  const [n, m]: number[] = input[0].split(' ').map(Number);
  const arr: number[] = input[1].split(' ').map(Number);

  arr.sort((a, b) => a - b);
  //N개의 자연수 중에서 M개를 고른 수열
  //중복가능
  const seq: number[] = [];

  function dfs(start: number) {
    if (seq.length === m) {
      console.log(seq.join(' '));
      return;
    }
    for (let i = 0; i < n; i++) {
      const target: number = arr[i];
      if (start <= target) {
        seq.push(target);
        dfs(target);
        seq.pop();
      }
    }
  }
  dfs(arr[0]);
}
