// 4. for문을 사용하여 0부터 10미만의 정수 중에서 홀수만을 큰수부터 출력하시오.
for (var i = 9; i >= 0; i--){
    if (i % 2 === 1) console.log(i);
}

// 3항조건연산문
for (var i = 9; i >= 0; i--){
    i % 2 === 1 ? console.log(i) : null;
}

// 단축평가문
for (var i = 9; i >= 0; i--){
    i % 2 === 1 && console.log(i);
}