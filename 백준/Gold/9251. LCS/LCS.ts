import fs = require('fs')

const input: string[] = fs.readFileSync('/dev/stdin').toString().split('\n')

const str1: string = input[0].trim()
const str2: string = input[1].trim()

//dp 배열 생성 1000*1000 => 문자열 길이로 설정
const dp: number[][] = Array(str1.length + 1).fill(null).map(() => Array(str2.length + 1).fill(0));

// DP 배열 채우기
for(let i = 1; i <= str1.length; i++){
    for(let j = 1; j <= str2.length; j++){
        if(str1[i-1] === str2[j-1]){
            dp[i][j] = dp[i-1][j-1] + 1
        }
        else{
            dp[i][j] = Math.max(dp[i][j-1], dp[i-1][j])
        }
    }
}
console.log(dp[str1.length][str2.length])
