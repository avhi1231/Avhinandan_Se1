// Import necessary dependencies
import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHeart, faShoppingCart, faUser, faSearch, faExchangeAlt } from '@fortawesome/free-solid-svg-icons';

const Header = () => {
  return (
    <header style={styles.headerContainer}>
      {/* Logo Section */}
      <div style={styles.logoContainer}>
        <img src="/path/to/logo.png" alt="Nest Logo" style={styles.logo} />
        <h1 style={styles.logoText}>Nest</h1>
        <p style={styles.subText}>Mart & Grocery</p>
      </div>

      {/* Search Bar Section */}
      <div style={styles.searchContainer}>
        <select style={styles.categorySelect}>
          <option>All Categories</option>
          {/* Add more categories here */}
        </select>
        <input type="text" placeholder="Search" style={styles.searchInput} />
        <button style={styles.searchButton}>
          <FontAwesomeIcon icon={faSearch} />
        </button>
      </div>

      {/* Icons Section */}
      <div style={styles.iconsContainer}>
        <div style={styles.iconWrapper}>
          <FontAwesomeIcon icon={faExchangeAlt} />
          <span style={styles.iconBadge}>0</span>
          <p>Compare</p>
        </div>
        <div style={styles.iconWrapper}>
          <FontAwesomeIcon icon={faHeart} />
          <span style={styles.iconBadge}>0</span>
          <p>Wishlist</p>
        </div>
        <div style={styles.iconWrapper}>
          <FontAwesomeIcon icon={faShoppingCart} />
          <span style={styles.iconBadge}>0</span>
          <p>Cart</p>
        </div>
        <div style={styles.iconWrapper}>
          <FontAwesomeIcon icon={faUser} />
          <p>Account</p>
        </div>
      </div>
    </header>
  );
};

// Basic styles to resemble the header in the image
const styles = {
  headerContainer: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between',
    padding: '10px 20px',
    backgroundColor: '#f8f8f8',
    borderBottom: '1px solid #ddd',
  },
  logoContainer: {
    display: 'flex',
    alignItems: 'center',
  },
  logo: {
    width: '50px',
    marginRight: '10px',
  },
  logoText: {
    margin: 0,
    fontSize: '24px',
    fontWeight: 'bold',
    color: '#28a745',
  },
  subText: {
    margin: 0,
    fontSize: '12px',
    color: '#555',
  },
  searchContainer: {
    display: 'flex',
    alignItems: 'center',
    border: '1px solid #ccc',
    borderRadius: '5px',
    padding: '5px',
    width: '40%',
  },
  categorySelect: {
    padding: '5px',
    border: 'none',
    outline: 'none',
  },
  searchInput: {
    flex: 1,
    padding: '5px',
    border: 'none',
    outline: 'none',
  },
  searchButton: {
    padding: '5px',
    border: 'none',
    backgroundColor: 'transparent',
    cursor: 'pointer',
  },
  iconsContainer: {
    display: 'flex',
    alignItems: 'center',
  },
  iconWrapper: {
    display: 'flex',
    alignItems: 'center',
    flexDirection: 'column',
    marginLeft: '20px',
    position: 'relative',
  },
  iconBadge: {
    position: 'absolute',
    top: '-5px',
    right: '-10px',
    backgroundColor: '#28a745',
    color: '#fff',
    borderRadius: '50%',
    padding: '2px 5px',
    fontSize: '10px',
  },
};

export default Header;
