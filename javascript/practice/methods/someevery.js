// console.log([5, 10, 15].some((item) => typeof(item) === typeof('1') ));

// console.log([5, 10, 15].every( item => item % 5 === 0));

const users = [
  { id: 1, name: 'Lee' },
  { id: 2, name: 'Kim' },
  { id: 2, name: 'Choi' },
  { id: 3, name: 'Park' }
];

console.log(users.findIndex(item => item.name === 'Park'));