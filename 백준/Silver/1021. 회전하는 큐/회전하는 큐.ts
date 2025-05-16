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
  const [N, M] = input[0].split(' ').map(Number);
  const targets = input[1].split(' ').map(Number);
  const deque: number[] = Array.from({ length: N }, (_, i) => i + 1);
  let count = 0;

  function leftPop() {
    deque.shift();
  }
  function leftRotate() {
    deque.push(deque.shift()!);
    count++;
  }
  function rightRotate() {
    deque.unshift(deque.pop()!);
    count++;
  }

  for (const target of targets) {
    const idx = deque.indexOf(target);

    if (idx === 0) {
      leftPop();
      continue;
    }

    const leftLen = idx;
    const rightLen = deque.length - idx;

    if (leftLen <= rightLen) {
      // 왼쪽 회전 여러 번
      for (let i = 0; i < leftLen; i++) {
        leftRotate();
      }
    } else {
      // 오른쪽 회전 여러 번
      for (let i = 0; i < rightLen; i++) {
        rightRotate();
      }
    }

    // 맨 앞이 target이므로 제거
    leftPop();
  }

  console.log(count);
}
