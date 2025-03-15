import React, { useState } from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css"; // Make sure Leaflet styles are imported
import "leaflet/dist/images/marker-shadow.png";
import Navbar from "../common/Navbar"; // Ensure you have a Navbar component
import "../../styles/RestaurantFiltre.css";

import L from "leaflet";

// Custom icon for the markers
const customIcon = new L.Icon({
  iconUrl: "../public/images/card.png", // Replace with your icon URL
  iconSize: [30, 40],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41],
});

const restaurantData = [
  {
    id: 1,
    name: "Restaurant Ihssan",
    lat: 36.7538,
    lon: 3.0422,
    city: "Algiers",
    rating: 4.5,
    price: "4.5K",
    image: "../public/images/card.png",
  },
  {
    id: 2,
    name: "Restaurant Ahmed",
    lat: 36.7762,
    lon: 3.06,
    city: "Bab El Oued",
    rating: 4.8,
    price: "5.2K",
    image: "../public/images/card.png",
  },
  {
    id: 3,
    name: "Restaurant Abdel",
    lat: 36.7568,
    lon: 3.0422,
    city: "El Harrach",
    rating: 4.6,
    price: "3.8K",
    image: "../public/images/card.png",
  },
];

const RestaurantFiltre = () => {
  const [cityFilter, setCityFilter] = useState("");

  const filteredRestaurants = restaurantData.filter((restaurant) =>
    cityFilter
      ? restaurant.city.toLowerCase().includes(cityFilter.toLowerCase())
      : true
  );

  return (
    <div>
      <Navbar />
      <div className="restaurant-filtre">
        <div className="filters">
          <button className="filter-button">Free Cancellation</button>
          <select
            onChange={(e) => setCityFilter(e.target.value)}
            className="filter-select"
          >
            <option value="">All Locations</option>
            <option value="Algiers">Algiers</option>
            <option value="Bab El Oued">Bab El Oued</option>
            <option value="El Harrach">El Harrach</option>
          </select>
        </div>

        <div className="content">
          {/* LEFT SIDE: Restaurant List */}
          <div className="list-container">
            <h2>Stays in Algiers</h2>
            {filteredRestaurants.map((restaurant) => (
              <div key={restaurant.id} className="restaurant-card">
                <img
                  src={restaurant.image}
                  alt={restaurant.name}
                  className="restaurant-img"
                />
                <div className="restaurant-info">
                  <h3>{restaurant.name}</h3>
                  <p>
                    {restaurant.city} - <strong>{restaurant.price}</strong>
                  </p>
                  <p>⭐ {restaurant.rating}</p>
                  <button className="volunteer-btn">Volunteer</button>
                </div>
              </div>
            ))}
          </div>

          {/* RIGHT SIDE: Map */}
          <div className="map-container">
            <MapContainer center={[36.7538, 3.0422]} zoom={12} className="map">
              <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
              />
              {filteredRestaurants.map((restaurant) => (
                <Marker
                  key={restaurant.id}
                  position={[restaurant.lat, restaurant.lon]}
                  icon={customIcon}
                >
                  <Popup>
                    <b>{restaurant.name}</b>
                    <br />
                    {restaurant.city} - {restaurant.price}
                  </Popup>
                </Marker>
              ))}
            </MapContainer>
          </div>
        </div>
      </div>
    </div>
  );
};

export default RestaurantFiltre;
