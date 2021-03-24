// 12. 삼각형 출력하기 - pattern 2
// 다음을 참고하여 *(별)로 트리를 문자열로 완성하라. 개행문자(‘\n’)를 사용하여 개행한다. 완성된 문자열의 마지막은 개행문자(‘\n’)로 끝나도 관계없다.
// *****
//  ****
//   ***
//    **
//     *

var result = '';
for (var x = 0; x < 5; x++){
    for (var i = 0; i < x; i++) result += ' ';
    for (var j = 5; j > x; j--) result += '*';
    result += '\n';
}
console.log(result);