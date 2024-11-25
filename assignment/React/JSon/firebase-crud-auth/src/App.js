import React, { useState } from "react";
import Auth from "./components/Auth";
import Dashboard from "./components/Dashboard";

const App = () => {
  const [user, setUser] = useState(null);

  const handleAuthSuccess = () => {
    setUser(true);
  };

  const handleLogout = () => {
    setUser(false);
  };

  return (
    <div>
      {user ? <Dashboard onLogout={handleLogout} /> : <Auth onAuthSuccess={handleAuthSuccess} />}
    </div>
  );
};

export default App;
