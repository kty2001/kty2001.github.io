/*
js의 8가지 자료형
1. undefined
2. string
3. number
4. boolean
5. null
6. object(array, object, function)
7. bigint 큰수/정밀한수를 제어하기 위한 숫자형
8. symbol 고유하고 수정불가능한 자료형형
*/

/*
변수선언 키워드
- let: 변수 선언
- const: 상수 선언
- var: (legacy) 예전 브라우져 실행하는 경우
*/

let a;
console.log(a, typeof(a));

a = 3;
let b = 3.2;
console.log(a + b);
console.log(a - b);
console.log(a * b);
console.log(a / b);
console.log(a % b);

const username = "홍길동";
console.log(username, typeof(username))
console.log(`안녕하세요! 제 이름은 ${username}입니다.`)

let bool = true;
console.log(bool, typeof(bool));
console.log(!bool);

let k = 100;
k = null;
console.log(k, typeof(k));

const arr = [1, 2, 3]
console.log(arr, typeof(arr));
console.log(arr[0], arr[1], arr[100]);

const obj = {
    username: 'honggd',
    age: 20,
    scores: [90, 80, 100]
};
console.log(obj, typeof(obj));
console.log(obj['username'], obj['age'], obj['scores']);
console.log(obj.username, obj.age, obj.scores);

function foo(k) {
    console.log('fooooooooo', k);
};
console.log(foo, typeof(foo));
console.dir(foo);