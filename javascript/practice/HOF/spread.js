const obj1 = { x: 1, y: 2 };
const obj2 = { y: 20, z: 3 };

const objMerged = { ... obj1, ... obj2 };
console.log(objMerged);