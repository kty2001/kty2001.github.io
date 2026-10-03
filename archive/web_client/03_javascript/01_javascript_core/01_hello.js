console.log("Hello Node.js");

function add(a, b) {
    return a + b;
}

const result = add(10, 20);
console.log(result);

// 한 줄 주석
/*
여러 줄 주석
여러 줄 주석
여러 줄 주석
*/

// package.json의 "type": "commonjs"면 require() 문법, "type": "module"이면 import/export 문법
import fs from 'fs'
import { fileURLToPath } from 'url';

const filename = fileURLToPath(import.meta.url)
console.log(import.meta.url)
console.log(filename)

// 파일 읽기 작업 끝난 뒤 자동 실행되는 콜백 함수
fs.readFile(filename, 'utf-8', function(err, data){
    if(err){
        console.error('파일 읽기 실패: ', err);
        return;
    }
    console.log('파일 내용: \n', data)
});