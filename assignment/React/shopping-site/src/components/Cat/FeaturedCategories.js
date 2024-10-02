import React from 'react';
import './FeaturedCategorie.css';

const categories = [
  { name: 'Cake & Milk', items: 26, image: 'https://via.placeholder.com/100' },
  { name: 'Organic Kiwi', items: 28, image: 'https://via.placeholder.com/100' },
  { name: 'Peach', items: 26, image: 'https://via.placeholder.com/100' },
  { name: 'Red Apple', items: 26, image: 'https://via.placeholder.com/100' },
  { name: 'Snack', items: 26, image: 'https://via.placeholder.com/100' },
  { name: 'Vegetables', items: 26, image: 'https://via.placeholder.com/100' },
  { name: 'Strawberry', items: 26, image: 'https://via.placeholder.com/100' },
  { name: 'Black plum', items: 26, image: 'https://via.placeholder.com/100' },
  { name: 'Custard apple', items: 26, image: 'https://via.placeholder.com/100' },
  { name: 'Coffee & Tea', items: 26, image: 'https://via.placeholder.com/100' }
];

const FeaturedCategories = () => {
  return (
    <section className="featured-categories-section">
      <h2>Featured Categories</h2>

      {/* Category Cards */}
      <div className="categories-container">
        {categories.map((category, index) => (
          <div key={index} className="category-card">
            <img src={category.image} alt={category.name} />
            <h3>{category.name}</h3>
            <p>{category.items} items</p>
          </div>
        ))}
      </div>

      {/* Promotional Banners */}
      <div className="promotional-banners">
        <div className="banner">
          <h3>Everyday Fresh & Clean with Our Products</h3>
          <button className="shop-now-btn">Shop Now</button>
        </div>
        <div className="banner">
          <h3>Make your Breakfast Healthy and Easy</h3>
          <button className="shop-now-btn">Shop Now</button>
        </div>
        <div className="banner">
          <h3>The best Organic Products Online</h3>
          <button className="shop-now-btn">Shop Now</button>
        </div>
      </div>
    </section>
  );
};

export default FeaturedCategories;
