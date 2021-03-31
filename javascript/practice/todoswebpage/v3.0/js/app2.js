let todos = [];
let navState = 'all';

const $todos = document.querySelector('.todos');
const $inputTodo = document.querySelector('.input-todo');
const $nav = document.querySelector('.nav');
const $completeAll = document.getElementById('ck-complete-all');
const $completedTodos = document.querySelector('.completed-todos');
const $activeTodos = document.querySelector('.active-todos');
const $clearCompleted = document.querySelector('.clear-completed > .btn')


const getTodos = () => {
  todos = [
    { id: 1, content: 'HTML', completed: false },
    { id: 2, content: 'CSS', completed: true },
    { id: 3, content: 'Javascript', completed: false }
  ].sort((todo1, todo2) => todo2.id - todo1.id );
  render();
}

const render = () => {
  console.log('[TODOS] :', todos);
  const _todos = todos.filter(todo => navState === 'completed' ? todo.completed : (navState === 'active' ? !todo.completed : true ))
  $todos.innerHTML = _todos.map( ({ id, content, completed }) => {
    return `<li id="${id}" class="todo-item">
        <input id="ck-${id}" class="checkbox" type="checkbox" ${completed? "checked" : ""}>
        <label for="ck-${id}">${content}</label>
        <i class="remove-todo far fa-times-circle"></i>
        </li>`
  }).join('');

  $completedTodos.textContent = todos.filter(todo => todo.completed).length;
  $activeTodos.textContent = todos.filter(todo => !todo.completed).length;
};

document.addEventListener('DOMContentLoaded', getTodos);

const toggleTodo = id => {
  todos = todos.map(todo => todo.id === id ? ({ ... todo, completed: !todo.completed}) : todo);
  render();
}

$todos.onchange = e => {
  // if (!e.target.classList.contains('checkbox')) return; 걸러주지 않아도, change를 일으키는 요소는 input밖엔 없다.
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

$inputTodo.onkeydown = e => {
  const content = e.target.value;
  if (e.key !== 'Enter' || !content) return;
  e.target.value = '';
  e.target.focus();
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

const checkAll = completed => {
  todos = todos.map(todo => ({ ... todo, completed }))
  render();
};

$completeAll.onchange = e => {
  if ($completeAll.checked) $completeAll.setAttribute('checked', '');
  const checkedAll = e.target.checked;
  checkAll(checkedAll);
};

$clearCompleted.onclick = () => {
  todos = todos.filter(todo => !todo.completed);
  render();
};

$nav.onclick = e => {
  if (e.target === $nav) return;
  [... $nav.children].forEach( $navItem => {
    // if (e.target === $navItem) $navItem.classList.add('active')
    // else $navItem.classList.remove('active');
    $navItem.classList.toggle('active', $navItem === e.target);
  });

  navState = e.target.id;
  render();
};
