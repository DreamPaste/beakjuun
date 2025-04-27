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
  let cnt: number = 0;
  for (let i = 0; i < 8; i++) {
    for (let j = 0; j < 8; j++) {
      if ((i + j) % 2 === 0 && input[i][j] === 'F') {
        cnt++;
      }
    }
  }
  console.log(cnt);
}
