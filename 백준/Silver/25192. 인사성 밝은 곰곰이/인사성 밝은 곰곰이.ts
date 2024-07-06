import * as fs from 'fs';
//테스트  input : 제출시 주석처리

const input = fs.readFileSync('/dev/stdin', 'utf8').trim().split('\n');

//총 입력의 수
const n = parseInt(input[0]);

// 유저 추적을 위한 Set과 인사 카운트 변수 초기화
let user_logs = new Set<string>();
let count = 0;
//i=1은 ENTER
for (let i =1; i<= n; i++) {
    if(input[i] == 'ENTER'){
        user_logs = new Set<string>();
    }
    else{
        if(!user_logs.has(input[i])){
            user_logs.add(input[i]);
            count++
        }
    }
}
console.log(count)