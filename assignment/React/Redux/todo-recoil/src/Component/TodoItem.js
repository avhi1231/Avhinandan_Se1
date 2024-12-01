import React from 'react';
import { useSetRecoilState } from 'recoil';
import { todoListState } from './recoilState';

const TodoItem = ({ item, index }) => {
  const setTodoList = useSetRecoilState(todoListState);

  const toggleComplete = () => {
    setTodoList((oldTodoList) =>
      oldTodoList.map((todo, i) =>
        i === index ? { ...todo, isComplete: !todo.isComplete } : todo
      )
    );
  };

  const deleteTodo = () => {
    setTodoList((oldTodoList) => oldTodoList.filter((_, i) => i !== index));
  };

  return (
    <li>
      <input type="checkbox" checked={item.isComplete} onChange={toggleComplete} />
      <span>{item.text}</span>
      <button onClick={deleteTodo}>Delete</button>
    </li>
  );
};

export default TodoItem;
