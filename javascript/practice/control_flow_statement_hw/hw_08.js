// 8. 1부터 20 미만의 정수 중에서 2 또는 3의 배수가 아닌 수의 총합을 구하시오.

var result = 0;
for (var x = 1; x < 20; x++){
    if (x % 2 !== 0 && x % 3 !== 0) result += x;
}
console.log(result);