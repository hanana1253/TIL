// 10. 두 개의 주사위를 던졌을 때, 눈의 합이 6이 되는 모든 경우의 수를 출력하시오.

for (var i = 1; i <= 6; i++){
    for (var j = 1; j <= 6; j++){
        if (i + j === 6) console.log(i, j);
    }
}