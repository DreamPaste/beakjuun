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
  const [F, S, G, U, D]: number[] = input[0].split(' ').map(Number);
  const visited: boolean[] = new Array(F + 1).fill(false);
  const dist: number[] = new Array(F + 1).fill(0);

  const queue: number[] = [];
  queue.push(S);
  visited[S] = true;

  while (queue.length > 0) {
    const current = queue.shift()!;

    if (current === G) {
      console.log(dist[current]);
      return;
    }

    for (const next of [current + U, current - D]) {
      if (next >= 1 && next <= F && !visited[next]) {
        visited[next] = true;
        dist[next] = dist[current] + 1;
        queue.push(next);
      }
    }
  }

  console.log("use the stairs");
}
