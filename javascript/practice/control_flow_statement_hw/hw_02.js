// 2. for문을 사용하여 0부터 10미만의 정수 중에서 짝수만을 작은 수부터 출력하시오.
for (var i = 0; i < 10; i++){
    if (i % 2 === 0) console.log(i);
}

// 3항조건연산자 사용
for (var i = 0; i < 10; i++){
    i % 2 === 0 ? console.log(i) : null;
}

// 단축평가문 사용
for (var i = 0; i < 10; i++){
    i % 2 === 0 && console.log(i);
}