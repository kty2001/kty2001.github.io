/*
js 함수 작성법
1. 함수선언식 Function Declaration
    - hoisting 처리
2. 함수표현식 Function Expression
    - hoisting 처리 안됨

hoisting이란? 끌어올려져 처리.
*/

foo();
console.log(k);

function foo() {
    console.log('foooooooooooo');
}

var k = 10; // hosting
let m = 20; // non-hosting

const bar = function () {
    console.log('baaaaaaaa');
}
bar();


/**
 * IIFE:
 * - Immediately Invoked Function Expression
 * - 함수를 정의/호출하는 방식
 * - 전역변수 대신 지역변수를 선언하고, 보호하는 방식
 */

// 즉시 실행 함수
(function() {
    console.log('IIFE test');
})();

(function(name) {
    console.log(`Hello ${name}`);
})('홍길동');

let app_name = 'MyFantasticApp';
(() => {
    let pet_name = '햄토리';
})();
// console.log(pet_name);
app_name = 'YourFantasticApp'
console.log(app_name)

const test1 = function(a, b) {
    console.log(a, b);
    console.log(arguments);
}
test1(10, 20);
test1(10);
test1();
test1(10, 20, 30);

const test2 = function() {}
console.log(test2());

/**
 * 화살표함수 Arrow Function
 * - 파이썬 lambda와 같이 함수를 간결하게 작성하는 문법
 */
const f1 = function(a, b) {
    console.log(a, b);
    return a + b;
}
console.log(f1(10, 20));

const f2 = (a, b) => a + b;
console.log(f2(10, 20));

/**
 * 파이썬 *, **: 
 * - packing: def foo(*args), def foo(**kwargs) 매개변수
 * - unpacking: foo(*mylist), foo(**mydict) 매개인자
 * 
 * JS ...
 * - 나머지파라미터(rest parameter): 함수선언자리에서 매개인자 묶어 처리. 매개변수(공간)
 * - 전개연산자(spread operator): 배열/객체의 요소를 나열. 매개인자(값)
 */
const test3 = (year, ...names) => {
    console.log(names, typeof(names));

    for(let name of names) {
        console.log(names);
    }
};

test3(1990, '홍길동');
test3(2000, '홍길동', '신사임당');
test3(2010, '홍길동', '신사', '임당');

const names = ['홍길동', '신사임당']
test1(2026, names);
test1(2026, ...names);

(() => {
    const a = [1, 2, 3];
    const b = ['a', 'b', 'c'];

    const c = a.concat(b);
    console.log(c);

    const d = [...a, ...b];
    console.log(d);
})();

/**
 * 자바스크립트 함수는 1급시민객체이다!
 * 
 * 1급시민객체란?
 * - 무명의 리터럴로 생성가능해야 한다. 
 * - 변수 또는 자료구조(배열/객체)에 저장가능해야 한다.
 * - 함수의 매개인자로 사용이 가능해야 한다.
 * - 함수의 리턴값으로 사용이 가능해야 한다.
 */
const test4 = (k) => {
    console.log(`123 ${k}`)
}
test4('안녕');
const test5 = test4;
test5('반가워')

const obj_funcs = {
    test4: test4
}

obj_funcs['test4']('abc');

const funcs = [test1, test2, test3, test4]
funcs[3]('이것도 되나');

const runner = (f, n) => {
    for(let i = 0; i < n; i++) {
        f('안녕');
    }
}
runner(test4, 3);

const test6 = (emoji) => {
    return () => console.log(emoji);
}

const dog_emoji = test6('🐶');
dog_emoji();
const cat_emoji = test6('🐈');
cat_emoji();

const getDessert = (dessert) => {
    return (name) => `${name}이/가 ${dessert} 먹음`;
}

const getCake = getDessert('🎂');
const getDonut = getDessert('🍩');

console.log(getCake('철수'))
console.log(getDonut('은희'))

const getDessert2 = (dessert) => (name) => `${name}이/가 ${dessert} 먹음`;
const getCarrot = getDessert2('🥕');
console.log(getCarrot('토끼'));

const friends = ['길동', '순신', '관순'];
const getCorn = getDessert('🌽');

friends.forEach((friends) => console.log(getCorn(friends)))

const results = friends.map((friend) => getCorn(friends));
console.log(results);