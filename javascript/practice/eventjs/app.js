let todos = []; // 전역으로 만들어주며 초기값을 통해 값의 타입을 유추할 수 있게 해준다.
const $todoInput = document.querySelector('.todo-input');
const $todos = document.querySelector('.todos');
const render = () => {
  console.log('[TODOS]', todos);
  // let html = '';
  // todos.forEach( todo => {
  //   html += `<li id="${todo.id}">
  //   <input type="checkbox" ${todo.completed ? 'checked' : ''}>
  //   <span>${todo.content}</span>
  //   <button class="remove">X</button>
  //   </li>`;
  // });
  // document.querySelector('.todos').innerHTML = html;

  $todos.innerHTML = todos.map( todo => {
    return `<li id="${todo.id}">
   <input type="checkbox" ${todo.completed ? 'checked' : ''}>
   <span>${todo.content}</span>
   <button class="remove">X</button>
   </li>`;
  }).join('');
};

const getTodos = () => { //todos라는 데이터를 서버로부터 받은 걸로 치자.
  todos = [
    { id: 1, content: 'Javascript', completed: false },
    { id: 2, content: 'CSS', completed: true },
    { id: 3, content: 'HTML', completed: false },
  ].sort((todo1, todo2) => todo2.id - todo1.id );
  render();
};
const toggleTodo = id => {
  todos = todos.map(todo => todo.id === +id ? { ... todo, completed: !todo.completed } : todo );
  render();
};

document.addEventListener('DOMContentLoaded', getTodos);

const addTodo = (content) => {
  todos = [{ id: generateNextId(), content, completed: false }, ... todos ];
  render();
};
const generateNextId = () => {
  return Math.max( ... todos.map(todo => todo.id), 0) + 1;
}
// document.querySelector('.add').onclick = () => {
//   const content = $todoInput.value;
//   $todoInput.value = '';
//   $todoInput.focus();

//   addTodo(content);
// };

// $todoInput.onkeyup = e => {
//   if (e.key !== 'Enter') return;
//   const content = $todoInput.value;
//   $todoInput.value = '';
//   $todoInput.focus();

//   addTodo(content);
// }

document.querySelector('form').onsubmit = (e) => {
  // const content = $todoInput.value;
  e.preventDefault();
  const content = $todoInput.value;
  $todoInput.value = '';
  $todoInput.focus();
  addTodo(content);
};

const removeTodo = id => {
  todos = todos.filter(todo => todo.id !== +id);
  render();
};

$todos.onclick = e => {
  if(!e.target.classList.contains('remove')) return;

  const { id } = e.target.parentNode;    
  removeTodo(id);
};


$todos.onchange = e => {
  const { id } = e.target.parentNode;
  // console.log(e.target);
  toggleTodo(id);
};