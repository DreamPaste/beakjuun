import fs = require('fs');

const input: string[] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N: number = parseInt(input[0])
const array : number[][] = input.slice(1).map(line => line.split('').map(Number))
let result: string = ""

function calculate(x: number, y: number, size: number){
   
    if (size === 1) { // 크기가 1일 때 종료
        result += array[x][y].toString();
        return;
    }
    
    const firstColor: number = array[x][y];
    let sameColor: boolean = true;

    
    for(let i = x; i < x + size; i++){
        for(let j = y; j < y + size; j++){
            
            if(firstColor !== array[i][j]){
                sameColor = false;
                break;
            }
        }
        if(!sameColor) break;
    }
    if(sameColor){
        result += firstColor.toString();
    }
    else{
        //시작 괄호 추가
        result += "("
        //각 사분면 순서에 따라 새로운 압축 실행
        const newSize = size / 2;
        calculate(x, y, newSize);
        calculate(x, y + newSize, newSize)
        calculate(x + newSize, y, newSize)
        calculate(x + newSize, y + newSize, newSize)

        // 끝 괄호 추가
        result += ")"
    }
    
}

calculate(0, 0, N);
console.log(result)