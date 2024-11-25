import React from "react";
import { auth } from "../firebase";
import { signOut } from "firebase/auth";
import CRUD from "./CRUD";

const Dashboard = ({ onLogout }) => {
  const handleLogout = async () => {
    await signOut(auth);
    onLogout();
  };

  return (
    <div>
      <h1>Dashboard</h1>
      <button onClick={handleLogout}>Logout</button>
      <CRUD />
    </div>
  );
};

export default Dashboard;
