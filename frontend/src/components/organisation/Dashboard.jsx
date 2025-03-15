import React from "react";
import { useNavigate } from "react-router-dom";
import "../../styles/Dashboard.css";

const CharityDashboard = () => {
  const navigate = useNavigate();
  const user = JSON.parse(localStorage.getItem("user")); // Fetch user data

  return (
    <div className="dashboard-container">
      <h1>Welcome, {user?.first_name}!</h1>
      <p>Manage your organization, events, and volunteers easily.</p>

      {/* Charity Information Section */}
      <div className="charity-info">
        <h2>
          {user?.first_name} {user?.last_name} - {user?.role}
        </h2>
        <p>
          <strong>Email:</strong> {user?.email}
        </p>
        <p>
          <strong>Phone:</strong> {user?.phone_number}
        </p>
        <p>
          <strong>Location:</strong> {user?.location}
        </p>

        <div className="social-links">
          {user?.social_media_linkedin && (
            <a href={user.social_media_linkedin} target="_blank">
              LinkedIn
            </a>
          )}
          {user?.social_media_twitter && (
            <a href={user.social_media_twitter} target="_blank">
              Twitter
            </a>
          )}
          {user?.social_media_facebook && (
            <a href={user.social_media_facebook} target="_blank">
              Facebook
            </a>
          )}
          {user?.social_media_instagram && (
            <a href={user.social_media_instagram} target="_blank">
              Instagram
            </a>
          )}
        </div>
      </div>

      {/* Dashboard Navigation Cards */}
      <div className="dashboard-grid">
        <div
          className="dashboard-card"
          onClick={() => navigate("/organisation/create-event")}
        >
          <h3>Create Event</h3>
          <p>Plan and organize new charity events.</p>
        </div>

        <div
          className="dashboard-card"
          onClick={() => navigate("/organisation/volunteerList")}
        >
          <h3>Manage Volunteers</h3>
          <p>View and manage volunteer applications.</p>
        </div>

        <div
          className="dashboard-card"
          onClick={() => navigate("/organisation/profil")}
        >
          <h3>Profile</h3>
          <p>Update your charity organization details.</p>
        </div>
      </div>
    </div>
  );
};

export default CharityDashboard;
