import React from 'react';
import { useRecoilValue } from 'recoil';
import { todoListStatsState } from './recoilState';

const TodoStats = () => {
  const { totalNum, totalCompletedNum, totalUncompletedNum } = useRecoilValue(todoListStatsState);

  return (
    <div>
      <p>Total Todos: {totalNum}</p>
      <p>Completed: {totalCompletedNum}</p>
      <p>Uncompleted: {totalUncompletedNum}</p>
    </div>
  );
};

export default TodoStats;
