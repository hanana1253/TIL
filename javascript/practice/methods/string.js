const str = 'Hello World';
// console.log(str.indexOf('l', 7));
// console.log(str.substring(0, str.indexOf('d')+1));
// console.log(str.slice(-5, -3));
// console.log(str.toUpperCase());
// console.log(str.toLowerCase());
// console.log(str.slice(5).trim());
// console.log(str.repeat(2));
// console.log(str.replace(/l/g, 'e'));

const camelCase = 'helloWorldLullabyLove';
const pascalCase = camelCase.replace(/^[a-z]/, (item) => item.toUpperCase());
const snakeCase = camelCase.replace(/[A-Z]/g, item => '_' + item.toLowerCase());

console.log(snakeCase);

const snakeToCamel = snakeCase.replace(/[\_]+./g, match => match[1].toUpperCase());
console.log(snakeToCamel);