import fs = require('fs');

const input: string[] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const N: number = parseInt(input[0]);

const paper: number[][] = input.slice(1).map(line => line.split(' ').map(Number));
const result = {
    '-1':0,
    '0':0,
    '1':0
};

function solution(x: number, y: number, size: number){

    if(size === 1 ){
        const paperNum: string = paper[x][y].toString();
        result[paperNum as '-1' | '0' | '1'] += 1 ;
        return;
    }
    const firstNum: number = paper[x][y];
    let isAllSame: boolean = true;

    for(let i = x; i < x + size; i++){
        for(let j = y; j < y + size; j++){
            if( firstNum !== paper[i][j]){
                isAllSame = false;
                break;
            }
        }
        if(!isAllSame) break;
    }

    if(isAllSame){
        const paperNum: string = firstNum.toString();
        result[paperNum as '-1' | '0' | '1'] += 1;
    }
    else{
        const newSize: number =  Math.floor(size / 3);
        const directions =  [0, newSize, newSize*2];
        directions.forEach( i => {
            directions.forEach( j => {
                solution(x + i, y + j, newSize);
            })
        })
    }
}

solution(0, 0, N);

console.log(result['-1']);
console.log(result['0']);
console.log(result['1'])