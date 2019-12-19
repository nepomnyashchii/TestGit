loadEvents();
// load every event in the page
function loadEvents(){
  const myForm = document.querySelector('form')
  myForm.addEventListener('submit',eventHandler);
}
// subit data function
function eventHandler(e){
  e.preventDefault();
  let myInput = document.querySelector('input');
  if(myInput.value != ''){
    addTask(myInput.value);
    myInput.value = '';
  }
}

// add tasks
function addTask(task){
  let ul = document.querySelector('ul');
  let li = document.createElement('li');
  li.innerHTML = `<span class="delete">×</span> <input type="checkbox"><label>${task}</label>`;
  ul.appendChild(li);
  const tasks=  document.querySelector('.tasksBoard')
  tasks.style.display = 'block';
}