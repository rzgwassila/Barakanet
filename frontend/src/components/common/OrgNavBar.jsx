import React from "react";
import { Link, useLocation } from "react-router-dom";
import "../../styles/Navbar.css"; // Use the same style as the volunteer navbar

const OrganizationNavbar = () => {
  const location = useLocation();

  return (
    <nav className="navbar">
      <ul className="nav-links">
        <li
          className={
            location.pathname === "/organization/dashboard" ? "active" : ""
          }
        >
          <Link to="/organization/dashboard">Dashboard</Link>
          <span className="underline"></span>
        </li>
        <li
          className={
            location.pathname === "/organization/create-event" ? "active" : ""
          }
        >
          <Link to="/organization/create-event">Create Event</Link>
          <span className="underline"></span>
        </li>
        <li
          className={
            location.pathname === "/organization/profile" ? "active" : ""
          }
        >
          <Link to="/organization/profile">Profile</Link>
          <span className="underline"></span>
        </li>
      </ul>
    </nav>
  );
};

export default OrganizationNavbar;
