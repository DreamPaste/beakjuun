const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];
rl.on('line', line => {
    input.push(line.trim());
}).on('close', () => {
    solution();
    process.exit();
});

function solution() {
    let line = 0;
    const [V, E] = input[line++].split(' ').map(Number);

    // 최단 경로 테이블 생성 (Infinity 로 초기화)
    let dist = Array.from({length: V + 1}, () => Array(V + 1).fill(Infinity));

    // 간선 정보 입력
    for (; line < input.length; line++) {
        const [a, b, c] = input[line].split(' ').map(Number);
        dist[a][b] = c;
    }

    // 플로이드 워셜 알고리즘 실행
    dist = floyd(V, dist);

    // 대각선(dist[i][i]) 중 최솟값이 사이클의 비용
    let answer = Infinity;
    for (let i = 1; i <= V; i++) {
        answer = Math.min(answer, dist[i][i]);
    }

    console.log(answer === Infinity ? -1 : answer);
}

function floyd(n, dist) {
    for (let k = 1; k <= n; k++) {
        for (let i = 1; i <= n; i++) {
            for (let j = 1; j <= n; j++) {
                if (dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }
    return dist;
}
