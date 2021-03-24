// 16. 역정삼각형 출력하기
// *********
//  *******
//   *****
//    ***
//     *

var result = '';
for (var x = 0; x < 5; x++){
    for (var i = 0; i < x; i++) result += ' ';
    for (var j = 2 * x + 1; j < 10; j++) result += '*';
    result += '\n';
}
console.log(result);