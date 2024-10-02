import React, { useState } from 'react';
import './Navbars.css'; // Import a CSS file for styling
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHeadset, faBars } from '@fortawesome/free-solid-svg-icons';

const Navbar = () => {
  const [isDropdownOpen, setDropdownOpen] = useState(false);

  const toggleDropdown = () => {
    setDropdownOpen(!isDropdownOpen);
  };

  return (
    <nav className="navbar">
      <div className="navbar-left">
        {/* Browse All Categories */}
        <div className="dropdown">
          <button className="dropdown-btn" onClick={toggleDropdown}>
            <FontAwesomeIcon icon={faBars} /> Browse All Categories
          </button>
          {isDropdownOpen && (
            <ul className="dropdown-menu">
              <li>Category 1</li>
              <li>Category 2</li>
              <li>Category 3</li>
              <li>Category 4</li>
            </ul>
          )}
        </div>

        {/* Navbar Links */}
        <div className="nav-links">
          <a href="#hot-deals">Hot Deals</a>
          <a href="#home">Home</a>
          <a href="#about">About</a>
          <a href="#shop">Shop</a>
          <a href="#vendors">Vendors</a>
          <a href="#mega-menu">Mega Menu</a>
          <a href="#blog">Blog</a>
          <a href="#pages">Pages</a>
          <a href="#contact">Contact</a>
        </div>
      </div>

      {/* Support Center */}
      <div className="navbar-right">
        <span className="support-icon">
          <FontAwesomeIcon icon={faHeadset} /> 1900 - 888
        </span>
        <small className="support-text">24/7 Support Center</small>
      </div>
    </nav>
  );
};

export default Navbar;
