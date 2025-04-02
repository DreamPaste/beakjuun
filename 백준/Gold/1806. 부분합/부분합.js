const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input =[];
rl.on('line', line => {
    input.push(line.trim());
}).on('close', () => {
    solve();
    process.exit();
})

function solve() {
    const [n, s] = input[0].split(' ').map(Number);
    let arr = input[1].split(' ').map(Number);
    let minLength = Infinity;
    let sum = 0;
    let left = 0, right = 0;

    for(;right < n; right++){
        sum += arr[right];
        
        while(sum >= s){
            minLength = Math.min(minLength, right - left + 1);
            sum -= arr[left];
            left++;
        }
    }
    
    console.log(minLength === Infinity ? 0 : minLength);
}   