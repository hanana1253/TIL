// const fruits = ['바나나', '사과', '감'];
// fruits.sort();
// console.log(fruits);
// fruits.reverse();
// console.log(fruits);

// sort 메서드는 요소가 숫자일 경우에도 유니코드 문자열로 변환 후 오름차순 정렬
// 숫자요소를 정렬할 때에는 sort 메서드에 정렬순서를 정의하는 비교함수를 인수로 전달해야.
// 비교함수는 음수, 양수, 0을 반환해야 한다. 비교함수의 반환값이 0보다 작으면 비교함수의 첫번째 인수를 우선하여 정렬, 0이면 정렬하지 않고, 0보다 크면 비교함수의 두 번째 인수를 우선하여 정렬

// const points = [40, 100, 1, 5, 2, 25, 10];
// points.sort((a, b) => a - b);
// console.log(points);

// console.log(points[0], points[points.length - 1]);
// points.sort((a, b) => b - a);
// console.log(points)

const todos = [
  { id: 4, content: 'JavaScript' },
  { id: 1, content: 'HTML' },
  { id: 2, content: 'CSS' }
];

function compare(key){
  return (a, b) => (a[key] > b[key] ? 1 : (a[key] < b[key] ? -1 : 0));
}

todos.sort(compare('id'));
console.log(todos);

todos. sort(compare('content'));
console.log(todos);
