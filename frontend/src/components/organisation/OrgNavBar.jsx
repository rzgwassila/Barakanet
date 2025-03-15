import React from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import "../../styles/Navbar.css"; // Use the same style as the volunteer navbar
import { FaSignOutAlt } from "react-icons/fa";

const OrganizationNavbar = () => {
  const location = useLocation();
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    navigate("/"); // Redirect to home after logout
  };

  return (
    <nav className="navbar">
      <ul className="nav-links">
        <li
          className={
            location.pathname === "/organisation/dashboard" ? "active" : ""
          }
        >
          <Link to="/organisation/dashboard">Dashboard</Link>
        </li>

        <li
          className={
            location.pathname === "/organisation/create-event" ? "active" : ""
          }
        >
          <Link to="/organisation/create-event">Create Event</Link>
        </li>

        <li
          className={
            location.pathname === "/organisation/profil" ? "active" : ""
          }
        >
          <Link to="/organisation/profil">Profile</Link>
        </li>

        <li
          className={
            location.pathname === "/organisation/volunteerList" ? "active" : ""
          }
        >
          <Link to="/organisation/volunteerList">Manage Volunteers</Link>
        </li>
      </ul>

      {/* Logout Button */}
      <div className="nav-buttons">
        <button className="logout-btn" onClick={handleLogout}>
          <FaSignOutAlt /> Logout
        </button>
      </div>
    </nav>
  );
};

export default OrganizationNavbar;
