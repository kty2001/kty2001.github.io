const test1 = () => {
    const li1 = document.getElementById('li1');
    console.log(li1);
    console.dir(li1);
    
    console.dir(li1.innerText);

    const notExist = document.getElementById('asdfasfasfsadf');
    console.log(notExist)
};

const test2 = () => {
    const lis = document.getElementsByTagName('li');
    console.log(lis);

    for (let tag of lis) {
        console.log(tag.innerText);
        tag.style.backgroundColor = 'hotpink';
        tag.style.color = 'white';
    }

    const brs = document.getElementsByTagName('br');
    console.log(brs)
};

const test3 = () => {
    const group1 = document.getElementsByClassName('group1');
    console.log(group1)
    for (let tag of group1) {
        tag.innerHTML += '[group1]'
    }
};

const test4 = () => {
    const li3 = document.querySelector('#li3');
    li3.style.fontSize = '24px';

    const group2 = document.querySelector('.group2');
    console.log(group2);
};

const test5 = () => {
    const group2 = document.querySelectorAll('.group2');
    console.log(group2);

    group2.forEach((tag) => {
        console.log(tag);
        tag.innerHTML = tag.innerHTML.replace('HelloJS', '안녕 JS');
    });
};

const test6 = () => {
    const hobbies = document.getElementsByName('hobby');
    console.log(hobbies);

    let hobbyChecked = '';
    hobbies.forEach((tag) => {
        console.log(tag.checked);
        if (tag.checked) {
            hobbyChecked += tag.value + ' '
        }
    });
    alert(`[${hobbyChecked.trim()}] 선택`);
}

const test7 = () => {
    const hobbyAll = document.querySelector('#all');

    const hobbies = document.getElementsByName('hobby');
    hobbies.forEach((tag) => {
        tag.checked = hobbyAll.checked;
    });
};

const test8 = () => {
    const user_name = document.querySelector('#name');
    alert(user_name.value)
};

const test9 = () => {
    const score = document.querySelector('#score');
    const display_score = document.querySelector('#display-score');

    display_score.innerHTML = score.value;
};