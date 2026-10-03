import _ from 'lodash'

/**
 * 객체(object)
 * - python dict와 유사
 * - (속성명: 속성값) 모음 객체
 * - 속성명: 식별자/문자열 (모든 타입 가능)
 * - 속성값: 모든 타입 가능
 */

const test1 = () => {
    const obj = {
        name: 'HGD',
        age: 33,
        married: true,
        hobby: ['Netflix', 'Yasik', 'Health'],
        pet: {
            name: 'Nuguri',
            breed: 'puddle'
        },
        123: 456,
        'user-id': 'honggd',
        123: 789
    };
    console.log(obj);

    const obj2 = new Object();
    obj2.kor = 90;
    obj2.eng = 85;
    obj2.math = 80;
    console.log(obj2);
}

test1();

/**
 * 메소드: 객체의 속성값이 함수인 경우
 * 메소드에서 객체의 다른 속성을 참조하려면 this 참조 사용해야 함.
 */

const test2 = () => {
    const user = {
        username: '홍길동',
        run: function() {
            console.log(`${this.username} 달린다`);
        },
        work: function() {
            console.log(`${this.username} 일한다`);
        },
        eat: function() {
            console.log(`${this.username} 먹는다`);
        },
    }
    user.run();
    user['run']();
    user.work();
    user.eat();

}

test2();

const claculator = {
    plus(a, b) {
        return  a + b;
    },
    minus(a, b) {
        return  a - b;
    },
    multiply(a, b) {
        return  a * b;
    },
    divide(a, b) {
        return  a / b;
    },
    remainder(a, b) {
        return  a % b;
    }
}

/**
 * 반복순회 처리
 * - for..in
 * - Object.keys()
 * - Object.values()
 * - Object.entries()
 */
const test4 = () => {
    const dish = {
        name: 'chung',
        price: 15000,
        ingredients: ['chung', 'yang', 'dae', 'ma', 'du']
    }

    for (let attr in dish) {
        console.log(attr, '->', dish[attr]);
    }

    console.log(Object.keys(dish));
    Object.keys(dish).forEach((key, index, _arr) => {
        console.log(key, '->', dish[key]);
    })
}

test4();


/**
 * 얕은 복사
 * 깊은 복사 
 */

// 얕은 복사와 깊은 복사의 차이를 확인하는 함수
const test6 = () => {
    
    const obj1 = {
        name: '홍길동',  // 이름 속성
        tel: ['010-1234-1234', '010-5678-5678']  // 전화번호 배열
    };
    const obj2 = obj1; // 얕은 복사
    obj2.name = '고길동';  // obj2 변경
    console.log(obj2);  // obj2 출력
    console.log(obj1);  // 같은 객체를 참조하므로 obj1도 영향받음

    const obj3 = {...obj1};  // 전개연산자로 얕은 복사
    obj3.name = '이길동';  // 최상위 속성 변경
    obj3.tel[0] = '010-8888-8888';  // 중첩 배열 내부 값 변경
    console.log(obj3);  // obj3 출력
    console.log(obj1);  // 중첩 객체/배열은 공유되어 obj1도 영향받음

    const obj4 = _.cloneDeep(obj1);  // 깊은 복사 수행
    obj4.name = '황길동';  // obj4 이름 변경
    obj4.tel[0] = '010-7777-7777';  // obj4 전화번호 변경
    console.log(obj4);  // obj4 출력
    console.log(obj1);  // obj1은 영향받지 않음

    const extra = {
        name: '고길동',  // 추가 이름 속성
        address: '서울 금천구 독산동'  // 주소 속성
    };
    
    const newObj = {...obj1, ...extra}; // 속성값이 배열/객체에 대해서는 얕은 복사처리
    newObj.tel[0] = '010-4444-4444';  // 중첩 배열 값 변경
    console.log(newObj);  // 병합 객체 출력
    console.log(obj1);  // 얕은 복사이므로 obj1도 영향받음

    const newObj2 = _.merge({}, obj1, extra); // 깊은 복사처리됨.
    newObj2.tel[0] = '031-1234-1234';  // 병합 객체 내부 값 변경
    console.log(newObj2);  // 병합 결과 출력
    console.log(obj1);  // obj1은 영향받지 않음

};
test6();  // 함수 실행