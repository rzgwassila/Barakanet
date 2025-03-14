import React from "react";
import { NavLink } from "react-router-dom"; // Use NavLink instead of Link
import "../../styles/Navbar.css"; // Make sure to update the filename if needed
import { FaUtensils, FaHandHoldingHeart, FaRegHeart } from "react-icons/fa";

const Navbar = () => {
  return (
    <nav className="navbar">
      <ul className="nav-links">
        <li>
          <NavLink to="/" className="nav-link" activeClassName="active-link">
            Home
          </NavLink>
        </li>
        <li>
          <NavLink
            to="/restaurants"
            className="nav-link"
            activeClassName="active"
          >
            Restaurants
          </NavLink>
        </li>
      </ul>
      <div className="nav-buttons">
        <NavLink to="/login" className="login-btn-1">
          Login
        </NavLink>
        <NavLink to="/signup" className="signup-btn-1" activeClassName="active">
          Sign Up
        </NavLink>
      </div>
    </nav>
  );
};

export default Navbar;
