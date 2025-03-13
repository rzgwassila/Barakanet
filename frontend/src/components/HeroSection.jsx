import React from "react";
import "../styles/HeroSection.css";
import { BiSearch } from "react-icons/bi";

const HeroSection = () => {
  return (
    <div className="hero">
      <div className="overlay">
        <h1 className="hero-title">BarakaNet</h1>
        <p className="hero-subtitle">
          Find volunteer opportunities near you and help those in need
        </p>
        <div className="search-box">
          <input type="text" placeholder="بحث عن الفرع" />
          <button>
            {" "}
            <BiSearch />{" "}
          </button>
        </div>
      </div>
    </div>
  );
};

export default HeroSection;
