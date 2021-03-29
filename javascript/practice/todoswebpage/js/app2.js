let todos = [];
const $todos = document.querySelector('.todos');

const getTodos = () => {
  todos = [
    { id: 1, content: 'HTML', completed: false },
    { id: 2, content: 'CSS', completed: true },
    { id: 3, content: 'Javascript', completed: false }
  ].sort((todo1, todo2) => todo2.id - todo1.id );
  render();
}

const render = () => {
  $todos.innerHTML = todos.map( ({ id, content, completed }) => {
    return `<li id="${id}" class="todo-item">
        <input id="ck-${id}" class="checkbox" type="checkbox" ${completed? "checked" : ""}>
        <label for="ck-${id}">${content}</label>
        <i class="remove-todo far fa-times-circle"></i>
      </li>`
  }).join('');
  document.querySelector('.completed-todos').textContent = todos.filter(todo => todo.completed).length;
  document.querySelector('.active-todos').textContent = todos.filter(todo => !todo.completed).length;
};

document.addEventListener('DOMContentLoaded', getTodos);

const toggleTodo = id => {
  todos = todos.map(todo => todo.id === id ? ({ ... todo, completed: !todo.completed}) : todo);
  render();
}

$todos.onchange = e => {
  if (!e.target.classList.contains('checkbox')) return;
  const id = e.target.parentNode.id;
  toggleTodo(+id);
};

const generateNextId = () => {
  return Math.max( ... todos.map(todo => todo.id), 0) + 1;
};

const addTodo = content => {
  todos = [{ id: generateNextId(), content, completed: false }, ... todos];
  render();
};

document.querySelector('.input-todo').onkeydown = e => {
  if (e.key !== 'Enter') return;
  const content = e.target.value;
  e.target.value = '';
  addTodo(content);
};

const removeTodo = id => {
  todos = todos.filter(todo => todo.id !== id);
  render();
};

$todos.onclick = e => {
  if (!e.target.classList.contains('remove-todo')) return;
  const id = e.target.parentNode.id;
  removeTodo(+id);
};

const $completeAll = document.getElementById('ck-complete-all');

const checkAll = checkedAll => {
  todos = todos.map(todo => ({ ... todo, completed: checkedAll }))
  render();
};

$completeAll.onchange = e => {
  if ($completeAll.checked) $completeAll.setAttribute('checked', '');
  const checkedAll = e.target.checked;
  checkAll(checkedAll);
};

document.querySelector('.clear-completed > .btn').onclick = () => {
  todos = todos.filter(todo => !todo.completed);
  render();
}