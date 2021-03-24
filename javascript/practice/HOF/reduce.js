// Array.prototype.myReduce = function (callBack, initVal){
//   let acc;
//   for (let i = 0; i < this.length; i++){
//     if (i === 0) {
//       acc = callBack(initVal, this[i], i, this);
//     } else {
//       acc = callBack(acc, this[i], i, this);
//     }
//   }
//   return acc;
// }

Array.prototype.myReduce = function (fn, initVal = 0){
  if (typeof fn !== 'function'){
    throw new TypeError ('Lalala');
  };
  let res;
  for (let i = 0; i < this.length; i++){
    res = fn((i === 0? initVal: res), this[i], i, this);
  };
  return res;
};

const products = [
  { id: 1, price: 100 },
  { id: 2, price: 200 },
  { id: 3, price: 300 }
];

// 1번째 순회 시 acc는 { id: 1, price: 100 }, cur은 { id: 2, price: 200 }이고
// 2번째 순회 시 acc는 300, cur은 { id: 3, price: 300 }이다.
// 2번째 순회 시 acc에 함수에 객체가 아닌 숫자값이 전달된다. 이때 acc.price는 undefined다.
const priceSum = products.myReduce((acc, cur) => acc + cur.price, 0);

console.log(priceSum)
console.log([1, 2, 3, 4].myReduce((acc, cur) => acc * cur, 1));