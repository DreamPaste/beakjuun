import fs = require('fs')

const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const n: number = parseInt(input[0]);
const paper: number[][] = input.slice(1).map(line => line.split(' ').map(Number))

const colorCount = {
    white: 0,
    blue: 0
}

function countPapers(x: number, y: number, size: number){

    const firstColor = paper[x][y];
    let sameColor: boolean = true
    for(let i = x; i < x+size; i++){
        for(let j = y; j < y+size; j++){
            if (paper[i][j] != firstColor){
                sameColor = false;
                break;
            }
        }
        if(!sameColor) break;

    }

    if(sameColor) {
        if(firstColor === 0 ){
            colorCount.white++;
        }
        else{
            colorCount.blue++;
        }
    }
    else{
        const newSize = size / 2;
        countPapers(x, y, newSize); //1사분면
        countPapers(x, y + newSize, newSize); // 2사분면
        countPapers(x + newSize, y, newSize); // 3사분면
        countPapers(x + newSize, y + newSize, newSize); //4사분면

    }

}

countPapers(0, 0, n);
console.log(colorCount.white);
console.log(colorCount.blue);