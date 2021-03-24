const numbers = [1, 2, 3];
// let pows = [];

// numbers.forEach(item => pows.push(item ** 2));
// console.log(pows);

console.log(numbers.forEach((item, index, arr) => arr[index] = item ** 2));
console.log(numbers);
