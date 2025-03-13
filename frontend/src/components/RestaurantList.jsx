import React from "react";
import "../styles/RestaurantList.css"; // Ensure styles are added

const restaurants = [
  {
    id: 1,
    name: "Restaurant Ihssan",
    location: "Algiers | Bab El oued",
    rating: 4.5,
    participants: 1897,
    img: "../public/images/card.png",
  },
  {
    id: 2,
    name: "Restaurant Ahmed",
    location: "Algiers | Bab El oued",
    rating: 4.7,
    participants: 1897,
    img: "../public/images/card.png",
  },
  {
    id: 3,
    name: "Restaurant Rahma",
    location: "Algiers | Bab El oued",
    rating: 4.6,
    participants: 1897,
    img: "../public/images/card.png",
  },
  {
    id: 4,
    name: "Restaurant Yasser",
    location: "Algiers | Bab El oued",
    rating: 4.3,
    participants: 1897,
    img: "../public/images/card.png",
  },
  {
    id: 5,
    name: "Restaurant Family",
    location: "Algiers | Bab El oued",
    rating: 4.2,
    participants: 1897,
    img: "../public/images/card.png",
  },
  {
    id: 6,
    name: "Restaurant The City",
    location: "Algiers | Bab El oued",
    rating: 4.1,
    participants: 1897,
    img: "../public/images/card.png",
  },
];

const RestaurantList = () => {
  return (
    <div className="restaurant-container">
      <div className="header">
        <p>
          Found <span className="highlight">376 results</span> in 54 seconds
        </p>
        <div className="filters">
          <select>
            <option>Rating: Low to High</option>
            <option>Rating: High to Low</option>
          </select>
          <select>
            <option>Results: 1 - 5</option>
            <option>Results: 6 - 10</option>
          </select>
        </div>
      </div>

      <div className="restaurant-grid">
        {restaurants.map((restaurant) => (
          <div key={restaurant.id} className="restaurant-card">
            <img src={`/images/${restaurant.img}`} alt={restaurant.name} />
            <h3>{restaurant.name}</h3>
            <p>{restaurant.location}</p>
            <p>
              ⭐ {restaurant.rating} ({restaurant.participants} participants)
            </p>
            <button className="volunteer-btn">Volunteer</button>
          </div>
        ))}
      </div>

      <div className="pagination">
        <button>◀</button>
        <button className="active">01</button>
        <button>02</button>
        <button>03</button>
        <button>...</button>
        <button>08</button>
        <button>▶</button>
      </div>
    </div>
  );
};

export default RestaurantList;
