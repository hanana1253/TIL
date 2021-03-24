// 15. 정삼각형 출력하기
//     *
//    ***
//   *****
//  *******
// *********

var result = '';
for (var x = 0; x < 5; x++){
    for (var i = x; i < 4; i++) result += ' ';
    for (var j = 0; j < 2 * x + 1; j++) result += '*';
    result += '\n';
}
console.log(result);