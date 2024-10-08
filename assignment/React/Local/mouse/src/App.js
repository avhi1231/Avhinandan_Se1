import React, { useState, useEffect } from "react";
import './App.css';  // Optional: For styling

function App() {
  // State to store the mouse position
  const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 });

  // useEffect to update the mouse position when the mouse moves
  useEffect(() => {
    const handleMouseMove = (event) => {
      setMousePosition({
        x: event.clientX,
        y: event.clientY,
      });
    };

    // Add event listener to track mouse movement
    window.addEventListener("mousemove", handleMouseMove);

    // Cleanup event listener when the component unmounts
    return () => {
      window.removeEventListener("mousemove", handleMouseMove);
    };
  }, []);

  return (
    <div className="App">
      <h2>Move the Circle with Your Mouse!</h2>
      
      {/* Circle element that moves with mouse */}
      <div
        className="circle"
        style={{
          left: mousePosition.x - 50,  // Adjust the x-coordinate of the circle
          top: mousePosition.y - 50,   // Adjust the y-coordinate of the circle
          position: "absolute",        // Position absolute to follow the cursor
        }}
      ></div>
    </div>
  );
}

export default App;
