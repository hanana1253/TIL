var x = 1;
var y = 2;
var temp = x;

// x = y;
// y = temp;
// 현업에서는 이렇게 한다.

[x, y] = [y, x]; 

console.log(x, y);