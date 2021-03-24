let todos = [];

const getTodos = () => {
  todos = [
    { id: 3, content: 'HTML', completed: false },
    { id: 2, content: 'CSS', completed: true },
    { id: 1, content: 'Javascript', completed: false }
  ];
  render();
};

const $todos = document.querySelector('.todos');

const render = () => {
  $todos.innerHTML = todos.map(({id, content, completed}) => 
  `<li id="${id}">
  <label><input type="checkbox" ${completed ? 'checked' : ''}>${content}</label>
  <button class='deleteButton'>X</button>
  </li>`).join('');
}

document.addEventListener('DOMContentLoaded', getTodos);

const $lis = document.querySelector('.todos').children;
console.dir($lis);
console.log($lis);