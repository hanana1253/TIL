let todos = [];
const $todos = document.querySelector('.todos');
const $inputTodo = document.querySelector('.input-todo');
const $nav = document.querySelector('.nav');
const $all = document.getElementById('all');
const $completed = document.getElementById('completed')
const render = () => {
  console.log('[TODOS] :', todos);
  // if ($all.classList.contains('active')) _todos = todos;
  // _todos = [...todos].filter(todo => $completed.classList.contains('active')? todo.completed: !todo.completed);

  $todos.innerHTML = _todos.map( ({ id, content, completed }) => {
    return `<li id="${id}" class="todo-item">
    <input id="ck-${id}" class="checkbox" type="checkbox" ${completed ? 'checked': ''}>
    <label for="ck-${id}">${content}</label>
    <i class="remove-todo far fa-times-circle"></i>
    </li>`
  }).join('');
};

const getTodos = () => {
  todos = [
    { id: 1, content: 'HTML', completed: false },
    { id: 2, content: 'CSS', completed: true },
    { id: 3, content: 'Javascript', completed: false }
  ].sort((todo1, todo2) => todo2.id - todo1.id);
  render();
};

document.addEventListener('DOMContentLoaded', getTodos);

const generateNextId = () => {
  return Math.max( ... todos.map(todo => todo.id), 0) + 1;
};

const addTodo = content => {
  todos = [ { id: generateNextId(), content, completed: false }, ... todos ];
  render();
};

$inputTodo.onkeydown = e => {
  if (e.key !== 'Enter') return;
  const content = e.target.value;
  e.target.value = '';
  e.target.focus();
  addTodo(content);
};

$nav.onclick = e => {
  [ ... $nav.children].forEach( viewItem => viewItem.classList.toggle('active', e.target===viewItem));
};