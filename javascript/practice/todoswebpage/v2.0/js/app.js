// State
let todos = [];

const render = ()=>{
  document.querySelector('.todos').innerHTML = todos.map(({id,content,completed})=>{
    return `<li id='${id}' class="todo-item">
        <input id="ck-${id}" class="checkbox" type="checkbox"${completed ? "checked":""}>
        <label for="ck-${id}">${content}</label>
        <i class="remove-todo far fa-times-circle"></i>
      </li>`
  }).join('');
  document.querySelector('.completed-todos').textContent = todos.filter(todo => todo.completed).length + '';
  document.querySelector('.active-todos').textContent = todos.filter(todo => !todo.completed).length + '';
};

const getTodos = () => {
  todos = [
    { id: 1, content: 'HTML', completed: false },
    { id: 2, content: 'CSS', completed: true },
    { id: 3, content: 'Javascript', completed: false }
  ].sort((todo1, todo2) => todo2.id - todo1.id );  
  render();
};

document.addEventListener('DOMContentLoaded', getTodos);

const generateNextId = () => {
  return Math.max(...todos.map(todo => todo.id), 0) + 1;
};

const addTodo = content => {
  todos = [ { id: generateNextId(), content, completed: false }, ... todos ];
  render();
};

document.querySelector('.input-todo').onkeydown = e => {
  if ( e.key !== 'Enter') return;
  const content = document.querySelector('.input-todo').value;
  addTodo(content);
  document.querySelector('.input-todo').value = '';
};

const removeTodo = id => {
  todos = todos.filter(todo => todo.id !== +id);
  render();  
}

document.querySelector('.todos').onclick = e => {
  if (!e.target.matches('.remove-todo')) return;
  removeTodo(e.target.parentNode.id);
  // todos = todos.filter(todo => e.target.parentNode.id !== todo.id );
};

const toggleTodo = id => {
  todos = todos.map(todo => (todo.id === +id ? {...todo, completed: !todo.completed} : todo));
  render();
}

document.querySelector('.todos').onchange = e => {
  const {id} = e.target.parentNode;
  toggleTodo(id);
};

document.getElementById('ck-complete-all').onchange = e => {
  todos = todos.map(todo => ({ ... todo, completed: e.target.checked }));
  render();
};

document.querySelector('.clear-completed > .btn').onclick = () => {
  todos = todos.filter(todo => !todo.completed);
  render();
}