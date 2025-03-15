import React, { useState } from "react";
import "../styles/Auth.css";
import axios from "axios";

const Signup = () => {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
    confirmPassword: "",
    role: "volunteer",
    phoneNumber: "",
    location: "",
  });

  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  // Handle input changes
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);

    if (formData.password !== formData.confirmPassword) {
      setError("Passwords do not match!");
      return;
    }

    setLoading(true);

    const userData = {
      email: formData.email,
      password: formData.password,
      phone_number: formData.phoneNumber,
      role: formData.role,
      location: {
        address: formData.location,
      },
    };

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/api/signup/",
        userData
      );
      alert("Signup successful! You can now log in.");
    } catch (error) {
      setError(
        error.response?.data?.message || "Signup failed. Please try again."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-container">
      <div className="auth-box">
        <div className="auth-left">
          <h1 className="auth-title">
            Welcome to <span className="highlight">BarakaNet!</span>
          </h1>
          <p className="auth-subtitle">Create your account to get started.</p>

          {error && <p className="error-message">{error}</p>}

          <form onSubmit={handleSubmit}>
            <div className="input-group">
              <label>Email Address</label>
              <input
                type="email"
                name="email"
                placeholder="hakeem@digital.com"
                required
                value={formData.email}
                onChange={handleChange}
              />
            </div>

            <div className="input-group">
              <label>Password</label>
              <input
                type="password"
                name="password"
                placeholder="*************"
                required
                value={formData.password}
                onChange={handleChange}
              />
            </div>

            <div className="input-group">
              <label>Confirm Password</label>
              <input
                type="password"
                name="confirmPassword"
                placeholder="*************"
                required
                value={formData.confirmPassword}
                onChange={handleChange}
              />
            </div>

            <div className="input-group">
              <label>Role</label>
              <select name="role" value={formData.role} onChange={handleChange}>
                <option value="volunteer">Volunteer</option>
                <option value="donor">Donor</option>
              </select>
            </div>

            <div className="input-group">
              <label>Phone number</label>
              <input
                type="text"
                name="phoneNumber"
                placeholder="0123456789"
                required
                value={formData.phoneNumber}
                onChange={handleChange}
              />
            </div>

            <div className="input-group">
              <label>Location</label>
              <input
                type="text"
                name="location"
                placeholder="Algiers"
                required
                value={formData.location}
                onChange={handleChange}
              />
            </div>

            <div className="remember-forgot">
              <label>
                <input type="checkbox" /> Remember Me
              </label>
              <a href="#">Forgot Password?</a>
            </div>

            <div className="button-group">
              <button type="submit" className="signup-btn" disabled={loading}>
                {loading ? "Signing up..." : "Sign Up"}
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
