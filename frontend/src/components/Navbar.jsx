import React from "react";
import "../styles/Navbar.css";
import { Link } from "react-router-dom";
import { FaGift, FaHeart } from "react-icons/fa";

const Navbar = () => {
  return (
    <nav className="navbar">
      <ul className="nav-links">
        <li className="active">
          <a href="#">Home</a>
          <span className="underline"></span>
        </li>
        <li>
          <a href="#">Restaurants</a>
        </li>
        <li>
          <a href="#">
            <FaGift /> Donations
          </a>
        </li>
        <li>
          <a href="#">
            <FaHeart /> Favorites
          </a>
        </li>
      </ul>
      <div className="nav-buttons">
        <Link to="/login" className="login-btn-1">
          Login
        </Link>
        <Link to="/signup" className="signup-btn-1">
          Sign up
        </Link>
      </div>
    </nav>
  );
};

export default Navbar;
