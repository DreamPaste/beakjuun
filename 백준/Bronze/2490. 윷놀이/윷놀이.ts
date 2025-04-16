import readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input: string[] = [];
rl.on('line', line => {
  input.push(line.trim());
}).on('close', () => {
  solve();
  process.exit();
});

function solve() {
  for (let i = 0; i < 3; i++) {
    const results = ['D', 'C', 'B', 'A', 'E']; 
    const arr = input[i].split(' ').map(Number);
    const sum = arr.reduce((acc, cur) => acc + cur, 0);
    console.log(results[sum]);
  }
}
