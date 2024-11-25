import React, { useState, useEffect } from "react";
import { db } from "../firebase";
import {
  collection,
  addDoc,
  getDocs,
  deleteDoc,
  doc,
  updateDoc,
} from "firebase/firestore";

const CRUD = () => {
  const [tasks, setTasks] = useState([]);
  const [task, setTask] = useState("");
  const [editingId, setEditingId] = useState(null);

  const tasksCollection = collection(db, "tasks");

  const fetchTasks = async () => {
    const snapshot = await getDocs(tasksCollection);
    const taskList = snapshot.docs.map((doc) => ({ ...doc.data(), id: doc.id }));
    setTasks(taskList);
  };

  const handleAddTask = async (e) => {
    e.preventDefault();
    if (editingId) {
      const taskDoc = doc(db, "tasks", editingId);
      await updateDoc(taskDoc, { name: task });
      setEditingId(null);
    } else {
      await addDoc(tasksCollection, { name: task });
    }
    setTask("");
    fetchTasks();
  };

  const handleDeleteTask = async (id) => {
    const taskDoc = doc(db, "tasks", id);
    await deleteDoc(taskDoc);
    fetchTasks();
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  return (
    <div>
      <h2>Tasks</h2>
      <form onSubmit={handleAddTask}>
        <input
          type="text"
          placeholder="Task"
          value={task}
          onChange={(e) => setTask(e.target.value)}
        />
        <button type="submit">{editingId ? "Update" : "Add"}</button>
      </form>
      <ul>
        {tasks.map((t) => (
          <li key={t.id}>
            {t.name}
            <button onClick={() => handleDeleteTask(t.id)}>Delete</button>
            <button onClick={() => setEditingId(t.id) || setTask(t.name)}>Edit</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CRUD;
