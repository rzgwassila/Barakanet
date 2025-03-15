import React, { useEffect, useState } from "react";
import axios from "axios";
import "../../styles/HeroSection.css";
import { BiSearch } from "react-icons/bi";

const defaultImage = "/images/default-charity.jpg"; // Default charity image (store this in public/images)

const HeroSection = () => {
  const [charities, setCharities] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");

  useEffect(() => {
    // Fetch charities from the backend
    axios
      .get("http://localhost:8000/api/charities/")
      .then((response) => {
        setCharities(response.data);
      })
      .catch((error) => {
        console.error("Error fetching charities:", error);
      });
  }, []);

  // Filter charities based on search input
  const filteredCharities = charities.filter((charity) =>
    charity.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="hero">
      <div className="overlay">
        <h1 className="hero-title">BarakaNet</h1>
        <p className="hero-subtitle">
          Find volunteer opportunities near you and help those in need
        </p>
        <div className="search-box">
          <input
            type="text"
            placeholder="بحث عن الفرع"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
          <button>
            <BiSearch />
          </button>
        </div>

        {/* Display list of charities */}
        <div className="charity-list">
          {filteredCharities.length > 0 ? (
            filteredCharities.map((charity) => (
              <div key={charity.id} className="charity-card">
                <img
                  src={
                    charity.image
                      ? `http://localhost:8000${charity.image}`
                      : defaultImage
                  }
                  alt={charity.name}
                  className="charity-image"
                />
                <h3>{charity.name}</h3>
                <p>{charity.description}</p>
              </div>
            ))
          ) : (
            <p className="no-charities">No charities found.</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default HeroSection;
