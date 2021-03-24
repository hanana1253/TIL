// 6. while문을 사용하여 0 부터 10 미만의 정수 중에서 홀수만을 큰수부터 출력하시오.

var x = 9;
while (x >= 0){
    if (x % 2 === 1) console.log(x);
    x--;
}

// 3항조건연산문
var xTernary = 9;
while (xTernary >= 0){
    xTernary % 2 === 1 ? console.log(xTernary) : null;
    xTernary--;
}

// 단축평가문
var xShorthand = 9;
while (xShorthand >= 0){
    xShorthand % 2 === 1 && console.log(xShorthand);
    xShorthand--;
}