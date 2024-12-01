import React from "react";
import Accordion from "./Accordion";

const App = () => {
  // Data for the accordion
  const accordionData = [
    {
      title: "Accordion 1",
      content: "This is the content of Accordion 1.",
    },
    {
      title: "Accordion 2",
      content: "This is the content of Accordion 2.",
    },
    {
      title: "Accordion 3",
      content: "This is the content of Accordion 3.",
    },
  ];

  return (
    <div className="App">
      <h1>React Accordion</h1>
      <Accordion data={accordionData} />
    </div>
  );
};

export default App;
