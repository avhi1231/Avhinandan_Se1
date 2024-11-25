import React, { useState } from "react";
import axios from "axios";

const UserForm = ({ fetchUsers, editingUser, clearEditing }) => {
  const [formData, setFormData] = useState(editingUser || { name: "", email: "" });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (formData.id) {
      // Update user (PUT)
      await axios.put(`http://localhost:5000/users/${formData.id}`, formData);
    } else {
      // Add new user (POST)
      await axios.post("http://localhost:5000/users", formData);
    }
    fetchUsers();
    clearEditing();
    setFormData({ name: "", email: "" });
  };

  const patchUser = async () => {
    if (formData.id) {
      // Patch user
      await axios.patch(`http://localhost:5000/users/${formData.id}`, { name: formData.name });
      fetchUsers();
      clearEditing();
    }
  };

  return (
    <div>
      <h2>{formData.id ? "Edit User" : "Add User"}</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="Name"
          value={formData.name}
          onChange={handleChange}
        />
        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
        />
        <button type="submit">{formData.id ? "Update" : "Add"}</button>
        {formData.id && <button onClick={patchUser}>Patch Name</button>}
      </form>
    </div>
  );
};

export default UserForm;
