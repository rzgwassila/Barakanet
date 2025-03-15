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
            location.pathname === "/organisation/dashboard" ? "active" : ""
          }
        >
          <Link to="/organisation/dashboard">Dashboard</Link>
          <span className="underline"></span>
        </li>

        <li
          className={
            location.pathname === "/organisation/create-event" ? "active" : ""
          }
        >
          <Link to="/organisation/create-event">Create Event</Link>
          <span className="underline"></span>
        </li>

        <li
          className={
            location.pathname === "/organisation/profil" ? "active" : ""
          }
        >
          <Link to="/organisation/profil">Profile</Link>
          <span className="underline"></span>
        </li>

        <li
          className={
            location.pathname === "/organisation/volunteerList" ? "active" : ""
          }
        >
          <Link to="/organisation/volunteerList">Manage Volunteers</Link>
          <span className="underline"></span>
        </li>
      </ul>
    </nav>
  );
};

export default OrganizationNavbar;
