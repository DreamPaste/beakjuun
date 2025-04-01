const readline = require('readline');
const rl = readline.createInterface({
    
    input: process.stdin,
    output: process.stdout
}
);

let input = [];
rl.on('line', line => {
    input.push(line.trim());
}).on('close', () => {
    solution();
    process.exit();
});

function solution() {
    const n = Number(input[0]);
    let arr = input[1].split(' ').map(Number).sort((a, b) => a - b);
    const x = Number(input[2]);
    let cnt = 0;
    let left = 0, right = n - 1;

    while(left < right) {
        const sum = arr[left] + arr[right];
        if (sum === x) {
            cnt++;
            left++;
            right--;
        }
        else if(sum < x) {
            left++;
        }
        else {
            right--;
        }
    }
    console.log(cnt);
    
}