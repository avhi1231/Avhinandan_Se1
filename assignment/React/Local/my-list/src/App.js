import React, { useState } from 'react';
import ListView from './components/ListView';

const App = () => {
  const [items, setItems] = useState(['Apple', 'Banana', 'Orange', 'Grapes']);

  return (
    <div>
      <h1>My Fruit List</h1>
      <ListView items={items} />
    </div>
  );
};

export default App;