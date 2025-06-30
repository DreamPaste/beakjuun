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
  const n = Number(input[0]);
  const board: string[][] = input.slice(1).map(line => line.split(''));

  const dx = [0, 0, -1, 1];
  const dy = [-1, 1, 0, 0];

  const dfs = (
    x: number,
    y: number,
    visited: boolean[][],
    color: string,
    map: string[][]
  ) => {
    visited[x][y] = true;

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];

      if (
        nx >= 0 &&
        nx < n &&
        ny >= 0 &&
        ny < n &&
        !visited[nx][ny] &&
        map[nx][ny] === color
      ) {
        dfs(nx, ny, visited, color, map);
      }
    }
  };

  const countAreas = (map: string[][]): number => {
    const visited = Array.from({ length: n }, () => Array(n).fill(false));
    let count = 0;

    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (!visited[i][j]) {
          dfs(i, j, visited, map[i][j], map);
          count++;
        }
      }
    }
    return count;
  };

  const normalCount = countAreas(board);

  const colorBlindMap = board.map(row =>
    row.map(cell => (cell === 'R' ? 'G' : cell))
  );

  const colorBlindCount = countAreas(colorBlindMap);

  console.log(`${normalCount} ${colorBlindCount}`);
}
