// const target = 'Is this all there is?';
// const target = 'A AA B BB Aa Bb AAA AB';
// const target = '9839 AA BB 12,345';
// const target = 'https://poiemaweb.com';
// const url = 'https://example.com';
// const fileName = 'index.html';

// console.log(/html$/.test(fileName));
// console.log(url.match(regExp));

// const target = '12345';

// console.log(/^\d+$/.test(target));

// const target = ' Hi!';
// console.log(/^\s+/.test(target));

// const id = 'abc123';
// console.log(/^[0-9A-Za-z]{4,10}$/.test(id));
// const email = 'ungmo2@gmail.com';
// console.log(/^[\w]+@[a-z]+\.[a-z]+$/.test(email));

// const cellphone = '010-1234-5678';

// console.log(/^\d{3}-\d{4}-\d{4}$/.test(cellphone));

const target = 'abc#123';
console.log(/[\W]+/gi.test(target));