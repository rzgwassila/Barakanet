import React from "react";
import { useParams } from "react-router-dom";
import "../../styles/VolunteerDetails.css";

const VolunteerDetails = () => {
  const { id } = useParams(); // Get organization ID from URL (Assuming React Router is used)

  // Mock data (Replace with API call)
  const organization = {
    id,
    name: "Restaurant Ihssan",
    description: "A place that provides meals to those in need.",
    address: "Algeria | Bab Ezzouar",
    age: "25 - 35 years old",
    volunteers: "10 volunteers in need",
    image: "/images/default-charity.jpg", // Default image
    needs: [
      {
        title: "Cleaning & Maintenance",
        emoji: "🧹",
        description:
          "Keep the dining area clean, wash dishes, and manage waste disposal.",
        color: "#E5E5E5",
      },
      {
        title: "Serving Meals",
        emoji: "🍽️",
        description:
          "Serve food to people, ensuring proper hygiene and guidelines.",
        color: "#B8DFFB",
      },
      {
        title: "Food Preparation & Cooking",
        emoji: "👨‍🍳",
        description:
          "Assist in food cutting, peeling, and packaging for takeaway.",
        color: "#FAF3B3",
      },
      {
        title: "Providing Social & Support",
        emoji: "❤️",
        description:
          "Talk and inspire individuals, promoting kindness and positivity.",
        color: "#FAD9D7",
      },
      {
        title: "Managing Donations & Supplies",
        emoji: "📦",
        description: "Sort and organize food donations, track shortages.",
        color: "#C6E5B1",
      },
      {
        title: "Food Delivery & Distribution",
        emoji: "🚚",
        description: "Deliver meals to those unable to come to the restaurant.",
        color: "#F9C8C8",
      },
    ],
  };

  return (
    <div className="volunteer-container">
      {/* Charity Info Section */}
      <div className="charity-info">
        <img
          src={organization.image}
          alt={organization.name}
          className="charity-image"
        />
        <div className="charity-details">
          <h2>{organization.name}</h2>
          <p>{organization.description}</p>
          <div className="info-box">
            <p>
              <strong>📍 Address:</strong> {organization.address}
            </p>
            <p>
              <strong>🧑‍🤝‍🧑 Age Group:</strong> {organization.age}
            </p>
            <p>
              <strong>🤝 Volunteers Needed:</strong> {organization.volunteers}
            </p>
          </div>
          <div className="buttons">
            <button className="contact-btn">Contact Us</button>
            <button className="volunteer-btn">Volunteer</button>
          </div>
        </div>
      </div>

      {/* Volunteer Needs Section */}
      <h2 className="needs-title">Needs</h2>
      <div className="needs-grid">
        {organization.needs.map((need, index) => (
          <div
            key={index}
            className="need-card"
            style={{ backgroundColor: need.color }}
          >
            <h3>
              {need.title} {need.emoji}
            </h3>
            <p>{need.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default VolunteerDetails;
