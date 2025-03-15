import React from "react";
import { NavLink, useNavigate } from "react-router-dom";
import "../../styles/Navbar.css";
import OrgNavBar from "../organisation/OrgNavBar"; // Import OrgNavBar
import { FaSignOutAlt } from "react-icons/fa";

const Navbar = () => {
  const navigate = useNavigate();
  const user = JSON.parse(localStorage.getItem("user")); // Get user from localStorage
  const userRole = user?.role; // Get the user role

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    navigate("/"); // Redirect to home after logout
  };

  // ✅ If user is a charity, show OrgNavBar instead
  if (userRole === "charity") {
    return <OrgNavBar handleLogout={handleLogout} />;
  }

  return (
    <nav className="navbar">
      <ul className="nav-links">
        <li>
          <NavLink to="/" className="nav-link">
            Home
          </NavLink>
        </li>
        <li>
          <NavLink to="/restaurants" className="nav-link">
            Restaurants
          </NavLink>
        </li>
      </ul>

      <div className="nav-buttons">
        {user ? (
          <div className="user-info">
            <span className="user-name">{user.username}</span>
            <button className="logout-btn" onClick={handleLogout}>
              <FaSignOutAlt />
            </button>
          </div>
        ) : (
          <>
            <NavLink to="/login" className="login-btn-1">
              Login
            </NavLink>
            <NavLink to="/signup" className="signup-btn-1">
              Sign Up
            </NavLink>
          </>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
