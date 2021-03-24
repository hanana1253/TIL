// 3. for문을 사용하여 0부터 10미만의 정수 중에서 짝수만을 작은 수부터 문자열로 출력하시오.
var result = ''
for (var i = 0; i < 10; i++){
    if (i % 2 === 0) result += i;
}
console.log(result);

// 3항조건연산문
var resultTernary = '';
for (var i = 0; i < 10; i++){
    resultTernary = i % 2 === 0 ? resultTernary + i : resultTernary;
}
console.log(resultTernary);

// 단축평가문
var resultShorthand = '';
for (var i = 0; i < 10; i++){
    i % 2 === 0 && (resultShorthand += i);
}
console.log(resultShorthand);