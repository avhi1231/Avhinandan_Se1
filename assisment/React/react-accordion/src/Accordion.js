import React, { useState } from "react";
import "./App.css";

const Accordion = ({ data }) => {
  const [activeIndex, setActiveIndex] = useState(null);

  const toggleAccordion = (index) => {
    setActiveIndex(activeIndex === index ? null : index);
  };

  return (
    <div className="accordion">
      {data.map((item, index) => (
        <div key={index} className="accordion-item">
          <div
            className="accordion-header"
            onClick={() => toggleAccordion(index)}
          >
            <h3>{item.title}</h3>
          </div>
          <div
            className="accordion-body"
            style={{
              display: activeIndex === index ? "block" : "none",
            }}
          >
            <p>{item.content}</p>
          </div>
        </div>
      ))}
    </div>
  );
};

export default Accordion;
