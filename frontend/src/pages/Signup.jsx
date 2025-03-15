import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "../styles/Auth.css";

const Signup = () => {
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
    confirmPassword: "",
    first_name: "",
    last_name: "",
    role: "volunteer",
    location: "",
    phone_number: "",
    social_media_linkedin: "",
    social_media_twitter: "",
    social_media_facebook: "",
    social_media_instagram: "",
  });

  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSignup = async (e) => {
    e.preventDefault();

    if (formData.password !== formData.confirmPassword) {
      setError("Passwords do not match.");
      return;
    }

    try {
      const response = await axios.post(
        "http://localhost:8000/api/register/",
        formData
      );

      localStorage.setItem("token", response.data.token);
      localStorage.setItem("user", JSON.stringify(response.data.user));

      alert("Signup successful! Redirecting...");
      console.log(response);

      if (response.data.user.role === "volunteer") {
        navigate("/");
      } else if (response.data.user.role === "charity") {
        navigate("/charity-dashboard");
      }
    } catch (err) {
      setError("Signup failed. Please check your details.");
    }
  };

  return (
    <div className="auth-container">
      <div className="auth-box">
        <div className="auth-left">
          <h1 className="auth-title">
            Join <span className="highlight">BarakaNet!</span>
          </h1>
          <p className="auth-subtitle">Create your account</p>

          <form onSubmit={handleSignup}>
            {/* Username & Email */}
            <div className="input-row">
              <div className="input-group">
                <label>Username</label>
                <input
                  type="text"
                  name="username"
                  placeholder="Username"
                  value={formData.username}
                  onChange={handleChange}
                  required
                />
              </div>
              <div className="input-group">
                <label>Email</label>
                <input
                  type="email"
                  name="email"
                  placeholder="Email"
                  value={formData.email}
                  onChange={handleChange}
                  required
                />
              </div>
            </div>

            {/* Passwords */}
            <div className="input-row">
              <div className="input-group">
                <label>Password</label>
                <input
                  type="password"
                  name="password"
                  placeholder="*************"
                  value={formData.password}
                  onChange={handleChange}
                  required
                />
              </div>
              <div className="input-group">
                <label>Confirm Password</label>
                <input
                  type="password"
                  name="confirmPassword"
                  placeholder="*************"
                  value={formData.confirmPassword}
                  onChange={handleChange}
                  required
                />
              </div>
            </div>

            {/* First Name & Last Name */}
            <div className="input-row">
              <div className="input-group">
                <label>First Name</label>
                <input
                  type="text"
                  name="first_name"
                  placeholder="First Name"
                  value={formData.first_name}
                  onChange={handleChange}
                  required
                />
              </div>
              <div className="input-group">
                <label>Last Name</label>
                <input
                  type="text"
                  name="last_name"
                  placeholder="Last Name"
                  value={formData.last_name}
                  onChange={handleChange}
                  required
                />
              </div>
            </div>

            {/* Role Selection */}
            <div className="input-group">
              <label>Select Role</label>
              <select
                name="role"
                value={formData.role}
                onChange={handleChange}
                required
              >
                <option value="volunteer">Volunteer</option>
                <option value="charity">Charity</option>
              </select>
            </div>

            {/* Location & Phone Number */}
            <div className="input-row">
              <div className="input-group">
                <label>Location</label>
                <input
                  type="text"
                  name="location"
                  placeholder="Location"
                  value={formData.location}
                  onChange={handleChange}
                  required
                />
              </div>
              <div className="input-group">
                <label>Phone Number</label>
                <input
                  type="text"
                  name="phone_number"
                  placeholder="Phone Number"
                  value={formData.phone_number}
                  onChange={handleChange}
                  required
                />
              </div>
            </div>

            {/* Social Media Links */}
            <div className="input-row">
              <div className="input-group">
                <label>LinkedIn</label>
                <input
                  type="text"
                  name="social_media_linkedin"
                  placeholder="LinkedIn Profile"
                  value={formData.social_media_linkedin}
                  onChange={handleChange}
                />
              </div>
              <div className="input-group">
                <label>Twitter</label>
                <input
                  type="text"
                  name="social_media_twitter"
                  placeholder="Twitter Profile"
                  value={formData.social_media_twitter}
                  onChange={handleChange}
                />
              </div>
            </div>

            <div className="input-row">
              <div className="input-group">
                <label>Facebook</label>
                <input
                  type="text"
                  name="social_media_facebook"
                  placeholder="Facebook Profile"
                  value={formData.social_media_facebook}
                  onChange={handleChange}
                />
              </div>
              <div className="input-group">
                <label>Instagram</label>
                <input
                  type="text"
                  name="social_media_instagram"
                  placeholder="Instagram Profile"
                  value={formData.social_media_instagram}
                  onChange={handleChange}
                />
              </div>
            </div>

            {error && <p className="error">{error}</p>}

            <div className="button-group">
              <button type="submit" className="signup-btn">
                Sign Up
              </button>
              <button
                type="button"
                className="login-btn"
                onClick={() => navigate("/login")}
              >
                Login
              </button>
            </div>
          </form>
        </div>

        <div className="auth-right">
          <img src="/images/auth.png" alt="Cyclist" className="auth-image" />
        </div>
      </div>
    </div>
  );
};

export default Signup;
