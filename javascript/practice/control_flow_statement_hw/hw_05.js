// 5. while문을 사용하여 0 부터 10 미만의 정수 중에서 짝수만을 작은 수부터 출력하시오.
var x =  0;
while (x < 10) {
    if (x % 2 === 0) console.log(x);
    x++;
}

// 3항조건연산문
var xTernary = 0;
while (xTernary < 10){
    xTernary % 2 === 0 ? console.log(xTernary): null;
    xTernary++;
}

// 단축평가문
var xShorthand = 0;
while (xShorthand <10){
    xShorthand % 2 === 0 && console.log(xShorthand);
    xShorthand++;
}