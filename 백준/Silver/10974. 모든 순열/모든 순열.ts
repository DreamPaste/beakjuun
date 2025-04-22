const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on('line', line => {
  input.push(line.trim());
}).on('close', () => {
  solve();
  process.exit();
});



function solve() {
  const N = Number(input[0]);
  const used = Array(N + 1).fill(false);  
  const path = [];                        
  backtrack(0);  

  function backtrack(depth) {
    if (depth === N) {
      // 순열 완성 시 출력
      console.log(path.join(' '));
      return;
    }
    // 1부터 N까지 오름차순으로 시도
    for (let i = 1; i <= N; i++) {
      if (used[i]) continue;   
      used[i] = true;          // i 사용 표시
      path.push(i);            // 경로에 추가

      backtrack(depth + 1);    // 다음 깊이로

      path.pop();              
      used[i] = false;         // 사용 표시 해제
    }
  }
}
