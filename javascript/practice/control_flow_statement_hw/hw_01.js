// 1. 변수 x가 10보다 크고 20보다 작을 때 변수 x를 출력하는 조건식을 완성하라
var x = 15;

// if문 사용
if (x > 10 && x < 20) console.log(x);

// 3항조건연산자
x > 10 && x < 20 ? console.log(x) : null;

// 단축평가문
console.log((x > 10 && x < 20) && x);