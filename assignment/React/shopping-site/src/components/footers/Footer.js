import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPhone, faEnvelope, faMapMarkerAlt, faClock } from '@fortawesome/free-solid-svg-icons';
import { faFacebook, faTwitter, faInstagram, faPinterest } from '@fortawesome/free-brands-svg-icons';

const Footer = () => {
  return (
    <footer style={styles.footerContainer}>
      {/* Logo and Company Info */}
      <div style={styles.footerSection}>
        <img src="/path/to/logo.png" alt="Nest Logo" style={styles.logo} />
        <p>Awesome grocery store website template</p>
        <p><FontAwesomeIcon icon={faMapMarkerAlt} /> Address: 5171 W Campbell Ave, Kent, Utah, 53127, United States</p>
        <p><FontAwesomeIcon icon={faPhone} /> Call Us: (+91) - 540-025-124553</p>
        <p><FontAwesomeIcon icon={faEnvelope} /> Email: sale@Nest.com</p>
        <p><FontAwesomeIcon icon={faClock} /> Hours: 10:00 - 18:00, Mon - Sat</p>
      </div>

      {/* Company Links */}
      <div style={styles.footerSection}>
        <h4>Company</h4>
        <ul style={styles.linkList}>
          <li>About Us</li>
          <li>Delivery Information</li>
          <li>Privacy Policy</li>
          <li>Terms & Conditions</li>
          <li>Contact Us</li>
          <li>Support Center</li>
          <li>Careers</li>
        </ul>
      </div>

      {/* Account Links */}
      <div style={styles.footerSection}>
        <h4>Account</h4>
        <ul style={styles.linkList}>
          <li>Sign In</li>
          <li>View Cart</li>
          <li>My Wishlist</li>
          <li>Track My Order</li>
          <li>Help Ticket</li>
          <li>Shipping Details</li>
          <li>Compare Products</li>
        </ul>
      </div>

      {/* Corporate Links */}
      <div style={styles.footerSection}>
        <h4>Corporate</h4>
        <ul style={styles.linkList}>
          <li>Become a Vendor</li>
          <li>Affiliate Program</li>
          <li>Farm Business</li>
          <li>Farm Careers</li>
          <li>Our Suppliers</li>
          <li>Accessibility</li>
          <li>Promotions</li>
        </ul>
      </div>

      {/* Popular Links */}
      <div style={styles.footerSection}>
        <h4>Popular</h4>
        <ul style={styles.linkList}>
          <li>Milk & Flavoured Milk</li>
          <li>Butter and Margarine</li>
          <li>Eggs Substitutes</li>
          <li>Marmalades</li>
          <li>Sour Cream and Dips</li>
          <li>Tea & Kombucha</li>
          <li>Cheese</li>
        </ul>
      </div>

      {/* Install App Section */}
      <div style={styles.footerSection}>
        <h4>Install App</h4>
        <p>From App Store or Google Play</p>
        <div>
          <img src="/path/to/appstore.png" alt="App Store" style={styles.appStoreImage} />
          <img src="/path/to/googleplay.png" alt="Google Play" style={styles.appStoreImage} />
        </div>
        <p>Secured Payment Gateways</p>
        <div style={styles.paymentLogos}>
          <img src="/path/to/visa.png" alt="Visa" />
          <img src="/path/to/mastercard.png" alt="MasterCard" />
          <img src="/path/to/maestro.png" alt="Maestro" />
          <img src="/path/to/paypal.png" alt="Paypal" />
        </div>
      </div>

      {/* Bottom Footer with Contact and Social Media */}
      <div style={styles.footerBottom}>
        <p>© 2024, Nest - HTML Ecommerce Template. All rights reserved.</p>
        <div style={styles.contactInfo}>
          <p><FontAwesomeIcon icon={faPhone} /> 1900 - 6666 (Working 8:00 - 22:00)</p>
          <p><FontAwesomeIcon icon={faPhone} /> 1900 - 8888 (24/7 Support Center)</p>
        </div>
        <div style={styles.socialMedia}>
          <p>Follow Us</p>
          <div>
            {/* Add your social media icons here */}
            <FontAwesomeIcon icon={faFacebook} />
            <FontAwesomeIcon icon={faTwitter} />
            <FontAwesomeIcon icon={faInstagram} />
            <FontAwesomeIcon icon={faPinterest} />
          </div>
        </div>
      </div>
    </footer>
  );
};

// Basic styles to replicate the footer
const styles = {
  footerContainer: {
    display: 'grid',
    gridTemplateColumns: 'repeat(6, 1fr)',
    gap: '20px',
    backgroundColor: '#f8f8f8',
    padding: '40px',
    borderTop: '1px solid #ddd',
  },
  footerSection: {
    display: 'flex',
    flexDirection: 'column',
    fontSize: '14px',
    color: '#333',
  },
  logo: {
    width: '80px',
    marginBottom: '10px',
  },
  linkList: {
    listStyleType: 'none',
    padding: 0,
    lineHeight: '1.8',
  },
  appStoreImage: {
    width: '120px',
    margin: '10px 0',
  },
  paymentLogos: {
    display: 'flex',
    gap: '10px',
  },
  footerBottom: {
    gridColumn: '1 / -1',
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: '20px 0',
    borderTop: '1px solid #ddd',
    fontSize: '14px',
    color: '#777',
  },
  contactInfo: {
    display: 'flex',
    gap: '30px',
  },
  socialMedia: {
    display: 'flex',
    gap: '10px',
    alignItems: 'center',
  },
};

export default Footer;