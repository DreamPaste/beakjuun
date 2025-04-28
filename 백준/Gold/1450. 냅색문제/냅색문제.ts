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
  const [n, c] = input[0].split(' ').map(Number);
  const weights: number[] = input[1].split(' ').map(Number);
  let count: number = 0;
  const mid: number = Math.floor(n / 2);
  const leftArr = weights.slice(0, mid);
  const rightArr = weights.slice(mid);

  const leftSums: number[] = [];
  const rightSums: number[] = [];
  //부분집합의 sum을 구하는 dfs
  function dfs(idx: number, sum: number, arr: number[], res: number[]): void {
    if (idx == arr.length) {
      // 배열 끝에 도착하면 지금까지 누적된 sum을 결과에 추가;
      res.push(sum);
      return;
    }
    dfs(idx + 1, sum, arr, res);
    dfs(idx + 1, sum + arr[idx], arr, res);
  }

  dfs(0, 0, leftArr, leftSums);
  dfs(0, 0, rightArr, rightSums);

  rightSums.sort((a, b) => a - b);

  // x보다 작거나 같은 원소의 개수(처음으로 작거나 같은 idx)를 이분 탐색으로 구함
  function binarySearch(arr: number[], x: number): number {
    let left = 0;
    let right = arr.length;

    while (left < right) {
      const mid = Math.floor((left + right) / 2);
      if (arr[mid] <= x) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    return left;
  }

  for (const ls of leftSums) {
    const remain = c - ls;
    count += binarySearch(rightSums, remain);
  }

  console.log(count);
}
