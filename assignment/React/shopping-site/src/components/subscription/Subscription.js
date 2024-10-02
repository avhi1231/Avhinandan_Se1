import React from 'react';
import './Subscriptions.css'; // Link to your CSS file for styling
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faEnvelope, faChevronRight, faChevronLeft } from '@fortawesome/free-solid-svg-icons';

const Subscription = () => {
  return (
    <section className="subscription-section">
      <div className="subscription-container">
        <div className="subscription-text">
          <h1>Don’t miss amazing grocery deals</h1>
          <p>Sign up for the daily newsletter</p>

          <div className="subscription-form">
            <div className="input-container">
              <FontAwesomeIcon icon={faEnvelope} className="envelope-icon" />
              <input type="email" placeholder="Your email address" />
            </div>
            <button className="subscribe-btn">Subscribe</button>
          </div>
        </div>
        <div className="subscription-image">
          {/* Image Placeholder */}
          <img src="https://via.placeholder.com/350" alt="Groceries" />
        </div>
      </div>
    </section>
  );
};

export default Subscription;
