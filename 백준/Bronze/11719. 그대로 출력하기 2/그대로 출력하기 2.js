const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
let input =[];
rl.on('line', line => {
    input.push(line);
}).on('close', ()=> {
    solution();
    process.exit();
});

function solution() {
    input.forEach(e => {
        console.log(e)
    });
    
    
}