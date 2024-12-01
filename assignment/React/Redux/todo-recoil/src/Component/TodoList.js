import React from 'react';
import { useRecoilValue } from 'recoil';
import { todoListState } from './recoilState';
import TodoItem from './TodoItem';
import TodoStats from './TodoStats';

const TodoList = () => {
  const todoList = useRecoilValue(todoListState);

  return (
    <div>
      <TodoStats />
      <ul>
        {todoList.map((todo, index) => (
          <TodoItem key={index} item={todo} index={index} />
        ))}
      </ul>
    </div>
  );
};

export default TodoList;
