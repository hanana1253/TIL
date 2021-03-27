let todos = '';

const getTodos = () => {
  todos = [
    { id: 3, content: 'HTML', completed: false },
    { id: 2, content: 'CSS', completed: true },
    { id: 1, content: 'Javascript', completed: false }
  ];
  render();
}

const render = () => {
  document.querySelector('.todos').innerHTML = todos.map(({id, content, completed}) => {
    return `<li id=${id}>
    <input type="checkbox" ${completed ? 'checked' : ''}>${content}
    <button class='deleteButton'>X</button>
    </li>`
  }).join('')
}

document.addEventListener('DOMContentLoaded', getTodos);
