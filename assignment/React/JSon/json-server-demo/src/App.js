import React, { useState } from "react";
import UserList from "./components/UserList";
import UserForm from "./components/UserForm";

const App = () => {
  const [editingUser, setEditingUser] = useState(null);

  const fetchUsers = () => {
    // Trigger fetch in UserList
  };

  const handleEdit = (user) => {
    setEditingUser(user);
  };

  const clearEditing = () => {
    setEditingUser(null);
  };

  return (
    <div>
      <h1>User Management</h1>
      <UserForm
        fetchUsers={fetchUsers}
        editingUser={editingUser}
        clearEditing={clearEditing}
      />
      <UserList onEdit={handleEdit} />
    </div>
  );
};

export default App;
