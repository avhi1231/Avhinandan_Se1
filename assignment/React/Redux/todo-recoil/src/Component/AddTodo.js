import React, { useState } from 'react';
import { useSetRecoilState } from 'recoil';
import { todoListState } from './recoilState';

const AddTodo = () => {
  const [inputValue, setInputValue] = useState('');
  const setTodoList = useSetRecoilState(todoListState);

  const addTodo = () => {
    if (inputValue.trim()) {
      setTodoList((oldTodoList) => [
        ...oldTodoList,
        { text: inputValue, isComplete: false },
      ]);
      setInputValue('');
    }
  };

  return (
    <div>
      <input
        type="text"
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        placeholder="Add a todo"
      />
      <button onClick={addTodo}>Add</button>
    </div>
  );
};

export default AddTodo;
