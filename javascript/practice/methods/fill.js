// const arr = new Array(3);
// console.log(arr);

// const result = arr.fill(1);
// console.log(result);
// console.log(arr);

const sequences = (length = 0) => Array.from({ length }, (_, i) => i);
console.log(sequences(3));