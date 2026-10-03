/**
 * 단축평가 
 * - 표현식 평가중에 결과가 확정된 경우, 이후 연산을 수행하지 않음
 * - ||: 좌항이 true인 경우 우항을 검사하지 않음.
 * - &&: 좌항이 false인 경우 우항을 검사하지 않음.
 */
import readline from 'node:readline';

function test1() {
    console.log('apple' || 'banana');
    console.log('' || 'banana');

    const fruit = 'apple' || 'banana'
    console.log(fruit);

    console.log('apple' && 'orange');
    console.log('' && 'orange');
}

test1();

function get_user_num() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    rl.question('숫자 하나 입력', (answer) => {
        answer = Number(answer) || 1000;
        console.log(`입력 숫자는 ${answer}`);
        rl.close();
    });
}

// get_user_num();

/**
 * 단축평가를 이용한 if문 처리
 * - 조건식 && 실행문: true경우만 실행 
 * - 조건식 || 실행문: false경우만 실행
 */

function test2(num) {
    num % 2 == 0 && console.log(`${num}은 짝수`)
    num % 2 == 0 || console.log(`${num}은 홀수`)
}
test2(3)

// optional chaining
function test3(user) {
    // user객체가 존재하면, username 속성값을 사용
    // user객체가 존재하지 않으면, null값을 대입
    // const username = user && user.username
    const username = user?.username;
    console.log(username)
}
test3({username: 'sinsa'})
test3({})
test3(null)