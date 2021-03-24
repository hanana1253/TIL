// const values = [1, 2, 3, 4, 5, 6];

// const average = values.reduce((acc, cur, i, { length }) => {
//   return i === length - 1? (acc + cur) / length : acc + cur;
// }, 0);

// console.log(average);

// const maxValue = values.reduce((acc, cur) => ( acc > cur ? acc : cur ), 0);
// console.log(maxValue);

// const max = Math.max( ... values);
// console.log(max);

// const fruits = ['banana', 'apple', 'orange', 'orange', 'apple'];

// const count = fruits.reduce((acc, cur)=>{
//   acc[cur] = ( acc[cur] || 0 ) + 1;
//   return acc;
// }, {});
// console.log(count);

// const values = [1, [2, 3], 4, [5, 6]];

// const flat_values = values.reduce((acc, cur) => acc.concat(cur), []);
// console.log(flat_values);

// const values = [1, 2, 1, 3, 5, 4, 5, 3, 4, 4];

// const onlyOne = values.reduce((acc, cur) => acc.indexOf(cur) === -1 ? acc.concat(cur) : acc, []);
// console.log(onlyOne);

// const result = values.filter((v, i, arr) => i === arr.indexOf(v));
// console.log(result);