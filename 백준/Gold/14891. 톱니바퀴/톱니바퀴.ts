import readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input: string[] = [];
rl
  .on('line', line => input.push(line.trim()))
  .on('close', () => {
    solve();
    process.exit();
  });

function solve(): void {
  // 1) 초기 상태 파싱
  const wheels: number[][] = [
    input[0].split('').map(Number),
    input[1].split('').map(Number),
    input[2].split('').map(Number),
    input[3].split('').map(Number),
  ];
  const K = Number(input[4]);
  const ops: [number, number][] = [];
  for (let i = 5; i < 5 + K; i++) {
    const [wIdx, dir] = input[i].split(' ').map(Number);
    ops.push([wIdx - 1, dir]);
  }

  // 2) 단일 톱니 회전 함수
  function rotateWheel(idx: number, dir: number) {
    const w = wheels[idx];
    if (dir === 1) {
      // 시계 방향
      w.unshift(w.pop()!);
    } else if (dir === -1) {
      // 반시계 방향
      w.push(w.shift()!);
    }
  }

  // 3) 연쇄 회전 결정 및 적용
  function processOperation(startIdx: number, startDir: number) {
    // 3-1) 각 톱니바퀴의 회전 방향 저장 (0: 없음)
    const directions = new Array(4).fill(0);
    directions[startIdx] = startDir;

    // 왼쪽으로 체인 전파
    for (let i = startIdx; i > 0; i--) {
      if (
        directions[i] !== 0 &&
        wheels[i][6] !== wheels[i - 1][2] // 회전 전 원본 사용
      ) {
        directions[i - 1] = -directions[i];
      } else {
        break;
      }
    }
    // 오른쪽으로 체인 전파
    for (let i = startIdx; i < 3; i++) {
      if (
        directions[i] !== 0 &&
        wheels[i][2] !== wheels[i + 1][6]
      ) {
        directions[i + 1] = -directions[i];
      } else {
        break;
      }
    }

    // 3-2) 결정된 방향대로 실제 회전 적용
    for (let i = 0; i < 4; i++) {
      if (directions[i] !== 0) {
        rotateWheel(i, directions[i]);
      }
    }
  }

  // 4) 모든 명령 실행
  for (const [idx, dir] of ops) {
    processOperation(idx, dir);
  }

  // 5) 점수 계산
  let score = 0;
  for (let i = 0; i < 4; i++) {
    if (wheels[i][0] === 1) score += (1 << i);
  }
  console.log(score);
}
