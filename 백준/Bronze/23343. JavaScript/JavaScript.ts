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

function solve(): void {
  const [a, b] = input[0].split(' ').map(Number);

  console.log(Number(a) - Number(b));
}
