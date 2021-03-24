// 1. 변수 x가 10보다 크고 20보다 작을 때 변수 x를 출력하는 조건식을 완성하라
console.log('Q1');
var x = 15;

if (x > 10 && x < 20) {
    console.log(x);
}

// 2. for문을 사용하여 0부터 10미만의 정수 중에서 짝수만을 작은 수부터 출력하시오.
console.log('Q2');
for (var x = 0; x < 10; x++){
    if (x%2 === 0) console.log(x);
}

// 3. for문을 사용하여 0부터 10미만의 정수 중에서 짝수만을 작은수부터 문자열로 출력하시오.
console.log('Q3');
var str_even_x = '';
for (var x = 0; x < 10; x++){
    if (x%2 === 0) str_even_x = str_even_x + x;
}
console.log(str_even_x);

// 4. for문을 사용하여 0부터 10 미만의 정수 중에서 홀수만을 큰수부터 출력하시오.
console.log('Q4');
for (var x = 9; x >= 0; x--){
    if(x%2===1) console.log(x);
}

// 5. while문을 사용하여 0부터 10 미만의 정수 중에서 짝수만을 작은 수부터 출력하시오.
console.log('Q5');
var x_even = 0;
while (x_even < 10) {
    if (x_even%2===0) console.log(x_even);
    x_even++;
}

// 6. while문을 사용하여 0부터 10 미만의 정수 중에서 홀수만을 큰수부터 출력하시오.
console.log('Q6');
var x_odd = 9;
while (x_odd>=0){
    if (x_odd%2 ===1) console.log(x_odd);
    x_odd--;
}

// 7. for문을 사용하여 0부터 10 미만의 정수의 합을 출력하시오.
console.log('Q7');
var result_q7 = 0;
for (var x = 0; x < 10; x++){
    result_q7 = result_q7 + x;
}
console.log(result_q7);

// 8. 1부터 20 미만의 정수 중에서 2 또는 3의 배수가 아닌 수의 총합을 구하시오.
console.log('Q8');
var result_q8 = 0;
for (var x = 1; x < 20; x++){
    if (x%2 !== 0 && x%3 !== 0) result_q8 = result_q8 + x;
}
console.log(result_q8);

// 9. 1부터 20 미만의 정수 중에서 2 또는 3의 배수인 수의 총합을 구하시오.
console.log('Q9');
result_q9 = 0;
for (var x = 1; x < 20; x++){
    if (x%2 === 0 || x%3 === 0) result_q9 = result_q9 + x;
}
console.log(result_q9);

// 10. 두 개의 주사위를 던졌을 때, 눈의 합이 6이 되는 모든 경우의 수를 출력하시오.
console.log('Q10');
for (var i = 1; i <= 6; i++){
    for (var j = 1; j <=6; j++){
        if (i+j===6) console.log(i, j);
    }
}
