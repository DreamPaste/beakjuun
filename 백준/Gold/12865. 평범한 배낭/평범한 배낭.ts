import fs = require('fs')

const input: string[] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, K]: number[] = input[0].split(' ').map(Number);

const items: {
    weight: number,
    value: number

}[] =[];

for(let i = 1; i <= N; i++){
    const [weight, value] = input[i].split(' ').map(Number);
    items.push({weight, value});
}

//K를 기준으로 하는 인덱스
const dp: number[] = Array(K+1).fill(0)

for(let i = 0; i<N; i++){
    const {weight, value} = items[i];
    
    //각 무게당 최대 가치합을 저장
    for(let w = K; w >= weight; w--){
        //console.log("dp[%d] %d AND dp[%d] %d  => %d + %d",w,dp[w],w-weight, dp[w - weight]+ value, dp[w - weight], value)
        dp[w] = Math.max(dp[w], dp[w - weight]+ value)
        
    }
    //console.log("\n\ndp : ",dp)
}
console.log(dp[K])