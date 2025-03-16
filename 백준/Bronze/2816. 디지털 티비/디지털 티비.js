const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
    lines.push(line);
}).on("close", () => {
    solution(lines);
    process.exit();
});

function solution(inputLines) {
    // 첫 줄: 채널 수
    const n = parseInt(inputLines[0], 10);
    // 이후 n개의 줄: 채널 이름
    const channels = inputLines.slice(1, n + 1);
    
    // "KBS1"과 "KBS2"의 인덱스 찾기
    let idx1 = channels.indexOf("KBS1");
    let idx2 = channels.indexOf("KBS2");
    
    // 만약 "KBS1"이 "KBS2"보다 아래에 있다면, KBS1 이동 과정에서 KBS2 인덱스가 한 칸 밀리므로 보정합니다.
    if (idx1 > idx2) {
        idx2++;
    }
    
    // 명령어 생성:
    // KBS1: "1" 버튼 idx1번, "4" 버튼 idx1번
    // KBS2: "1" 버튼 idx2번, "4" 버튼 (idx2 - 1)번
    const result = "1".repeat(idx1) + "4".repeat(idx1) + "1".repeat(idx2) + "4".repeat(idx2 - 1);
    
    console.log(result);
}
