const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl
  .on('line', line => input.push(line.trim()))
  .on('close', () => {
    solve();
    process.exit();
  });

// 좌표를 문자열 키로 변환하는 함수
const key = p => `${p.x},${p.y}`;

// BFS 함수: 시작점(start), 물 높이(height), 지도(maps), 크기(n), 방문 집합(visited)
function bfs(start, height, maps, n, visited) {
  const queue = [start];
  visited.add(key(start));

  while (queue.length > 0) {
    const { x: cx, y: cy } = queue.shift();

    for (const [dx, dy] of [
      [-1, 0],
      [1, 0],
      [0, -1],
      [0, 1],
    ]) {
      const next = { x: cx + dx, y: cy + dy };

      // 경계 검사
      if (
        next.x < 0 || next.x >= n ||
        next.y < 0 || next.y >= n
      ) continue;

      const k = key(next);
      // 잠기지 않고 미방문인 경우에만 이동
      if (!visited.has(k) && maps[next.x][next.y] > height) {
        visited.add(k);
        queue.push(next);
      }
    }
  }
}

function solve() {
  const n = Number(input[0]);
  const maps = input
    .slice(1, n + 1)
    .map(line => line.split(' ').map(Number));

  const high = Math.max(...maps.flat());
  let maxArea = 0;

  for (let h = 0; h <= high; h++) {
    const visited = new Set();
    let areaCnt = 0;

    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (maps[i][j] > h && !visited.has(`${i},${j}`)) {
          bfs({ x: i, y: j }, h, maps, n, visited);
          areaCnt++;
        }
      }
    }

    if (areaCnt > maxArea) maxArea = areaCnt;
  }

  console.log(maxArea);
}
