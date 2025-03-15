import React, { useState } from "react";
import "../../styles/ProfileOrg.css";
const ProfilePage = () => {
  // Initial user data

  const [formData, setFormData] = useState({
    associationName: "Kafil EL yatim",
    description: "",
    yearOfCreation: "2019",
    field: "orphans",
    numMembers: "",
    email: "",
    phone: "+213 0123456789",
    wilaya: "Alger",
    city: "Blida",
    profilePicture: "image-name-goes-here.png",
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Updated Profile Data:", formData);
  };

  return (
    <div className="profile-container">
      <h3 className="last-update">Last update August 1</h3>
      <form onSubmit={handleSubmit} className="profile-form">
        <div className="form-section">
          <h4>Personal</h4>
          <label>Association Name</label>
          <input
            type="text"
            name="associationName"
            value={formData.associationName}
            onChange={handleChange}
          />

          <label>Description</label>
          <input
            type="text"
            name="description"
            placeholder="Year of creation achievements..."
            value={formData.description}
            onChange={handleChange}
          />

          <label>Year of Creation</label>
          <input
            type="number"
            name="yearOfCreation"
            value={formData.yearOfCreation}
            onChange={handleChange}
          />

          <label>Field</label>
          <select name="field" value={formData.field} onChange={handleChange}>
            <option value="orphans">Orphans</option>
            <option value="education">Education</option>
            <option value="health">Health</option>
          </select>

          <label>Number of Members</label>
          <input
            type="text"
            name="numMembers"
            placeholder="Year of creation achievements..."
            value={formData.numMembers}
            onChange={handleChange}
          />
        </div>

        <div className="form-section">
          <h4>Contact</h4>
          <label>Email</label>
          <input
            type="email"
            name="email"
            placeholder="Enter Value"
            value={formData.email}
            onChange={handleChange}
          />

          <label>Phone Number</label>
          <div className="phone-group">
            <span>+213</span>
            <input
              type="text"
              name="phone"
              value={formData.phone}
              onChange={handleChange}
            />
          </div>

          <label>Wilaya</label>
          <select name="wilaya" value={formData.wilaya} onChange={handleChange}>
            <option value="Alger">Alger</option>
            <option value="Blida">Blida</option>
            <option value="Oran">Oran</option>
          </select>

          <label>City</label>
          <select name="city" value={formData.city} onChange={handleChange}>
            <option value="Blida">Blida</option>
            <option value="Boumerdes">Boumerdes</option>
            <option value="Constantine">Constantine</option>
          </select>

          <label>Association Picture Profile</label>
          <input
            type="text"
            name="profilePicture"
            value={formData.profilePicture}
            onChange={handleChange}
          />
        </div>

        <div className="buttons">
          <button type="submit" className="save-btn">
            Save
          </button>
          <button type="button" className="cancel-btn">
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
};

export default ProfilePage;
