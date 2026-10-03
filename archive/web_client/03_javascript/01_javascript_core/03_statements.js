/**
 * 제어문
 * - 조건문 if
 * - 분기처리문 switch..case
 * - 반복문
 *  - for
 *  - while
 *  - for..in
 *  - for..of
 * - 반복분기처리 break/continue
 */

// const { functionsIn } = require("lodash");

/**
 * if
 */

function test1(age) {
    if (age >= 20) {
        console.log('당신은 성인');
    }
    else if (age >= 0 && age < 20) {
        console.log('당신은 미성년자')
    }
    else {
        console.log('유효하지 않은 숫자')
    }
}

test1(30);
test1(19);
test1(-100);

function test2(en_color) {
    let ko_color = '';
    switch(en_color) {
        case 'red':
            ko_color = '빨강';
            break;
        case 'yellow':
            ko_color = '노랑';
            break;
        case 'blue':
            ko_color = '파랑';
            break;
        default:
            ko_color = '알 수 없는 색상';
    }

    return ko_color;
}

console.log(test2('sadf'));

function test3() {
    for (let i = 0; i < 5; i++) {
        console.log(i);
    }
    for (let i = 10; i > 0; i--) {
        if (i % 2 == 0) {
            console.log(i);
        }
    }

    const arr = ['a', 'b', 'c']
    for (let i = 0; i < arr.length; i++) {
        console.log(arr[i]);
    }
};

test3();

function test4() {
    let i = 0;
    // while (i < 5) {
    //     console.log(i);
    //     i++;
    // }
    while (true) {
        if(i >= 5) {break;}
        console.log(i);
        i++;
    }
};

test4();

function test5() {
    const arr = ['1', '2', '3']

    console.log(Object.getOwnPropertyDescriptor(arr, '0').enumerable)
    console.log(Object.getOwnPropertyDescriptor(arr, '1').enumerable)
    console.log(Object.getOwnPropertyDescriptor(arr, 'length').enumerable)

    for (let i in arr) {
        console.log(i, ':', arr[i]);
    };

    let pet = {
        petname: '햄토리',
        type: '햄스터',
        weight: 0.5
    };

    for (let name in pet) {
        console.log(name, ':', pet[name])
    };
};

test5();

/**
 * for..of문
 * - Iterable객체의 요소를 순회
 * - array등의 요소를 직접 순회
 */

function test6() {
    const arr = ['1', '2', '3'];
    for (let fruit of arr) {
        console.log(fruit);
    }
}

test6()