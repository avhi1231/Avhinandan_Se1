import React from 'react';
import AddTodo from './Component/AddTodo';
import TodoList from './Component/TodoList';


const App = () => {
  return (
    <div>
      <h1>Recoil Todo List</h1>
      <AddTodo />
      <TodoList />
    </div>
  );
};

export default App;
