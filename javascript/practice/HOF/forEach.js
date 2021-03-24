// Array.prototype.myForEach = function(fn){
//   if(typeof fn !== 'function') {
//     throw new TypeError(`${fn} is not a function.`)
//   };

//   for (let i = 0; i < this.length; i++){
//     fn(this[i], i, this)
//   };
// };

// [1, 2, 3].myForEach();

// Array.prototype.myMap = function(fn){
//   if (typeof fn !== 'function'){
//     throw new TypeError (`${fn} is not a function.`)
//   };

//   const res = [];
//   for (let i = 0; i < this.length; i++){
//     res.push(fn(this[i], i, this));
//   }
//   return res;
// }

// console.log([1, 2, 3].myMap(v => v ** 2));

// Array.prototype.myFilter = function(fn){
//   if (typeof fn !== 'function'){
//     throw new TypeError (`${fn} is not a function.`)
//   };
//   const res = [];
//   for (let i = 0; i < this.length; i++){
//     if (fn(this[i], i, this)) res.push(this[i]);
//   };
//   return res;
// }

// console.log([1,2,3].myFilter(v => v>2));

Array.prototype.myReduce = function (fn, initVal){
  if (typeof fn !== 'function'){
    throw new TypeError ('Lalala');
  };
  for (let i = 0; i < this.length; i++){
    res = fn(i === 0? initVal: res, this[i], i, this);
  };
  return res;
};

console.log([1, 2, 3, 4].myReduce((acc, cur) => acc * cur, 1));



