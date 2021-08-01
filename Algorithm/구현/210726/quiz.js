function solution(words) {
  const answer = [];
  const SH = new Map();
  let flag = true;
  words.sort((word1, word2) => word2.length - word1.length);
  console.log(words);
  for (let char of words[0]) {
    SH.set(char, SH.get(char) + 1 || 1);
  }
  for (let i = 1; i < words.length; i++) {
    for (let [key, value] of SH ){
      if (words[i].indexOf[key] === -1){
        flag = false
        break
      } else {
        SH.set(key, value - 1)
      }
    }
    if (flag) {

    }
  }
  return true;
}
console.log(solution(['longlong', 'longtong', 'longbig'])); //["l", "o", "n", "g", "g"]
// console.log(solution(['cool', 'rock', 'cook'])); //["c", "o"]
// console.log(solution(['a', 'aaa', 'aaaaa'])); //["a"]
// console.log(solution(['aabbss', 'bbbss', 'csc', 'asb'])); //["s"]
// console.log(solution(['abcde', 'edcba', 'cdeba', 'debac', 'acbed'])); //["a", "c", "b", "e", "d"]
