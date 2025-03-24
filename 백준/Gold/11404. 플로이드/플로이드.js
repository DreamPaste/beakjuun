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
    const n = Number(input[line++]);
    const m = Number(input[line++]);
    let dist = Array.from({length: n + 1}, () => Array(n + 1).fill(Infinity));
    // 그래프에 값 추가
    for(;line < input.length; line++) {
        let [a, b, c] = input[line].split(' ').map(Number);
        //시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있음
        if (c < dist[a][b]) {
            dist[a][b] = c;
        }
    }
    //플로이드 워샬 알고리즘 실행
    dist = floyd(n, dist);

    for(let i = 1; i <= n; i++) {
        let result = [];
        for(let j = 1; j <= n; j++) {
            if(dist[i][j] === Infinity){
                result.push(0);
            }
            else {
                result.push(dist[i][j]);
            }
        }
        console.log(result.join(' '));
    }
    
}

function floyd(n, dist){
    
    for(let node = 1; node <= n; node ++) {
        for(let i = 1; i <= n; i++) {
            for(let j = 1; j <= n; j++) {
                if (i == j) {
                    dist[i][j] = 0;
                }
                dist[i][j] = Math.min(dist[i][j], dist[i][node] + dist[node][j]);
            }
        }
    }
    return dist
}