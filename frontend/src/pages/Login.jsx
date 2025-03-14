import React, { useState } from "react";
import { useNavigate } from "react-router-dom"; // Redirect after login
import axios from "axios"; // API requests
import "../styles/Auth.css";

const Login = () => {
  const [email, setEmail] = useState(""); // Store email
  const [password, setPassword] = useState(""); // Store password
  const [error, setError] = useState(""); // Store error messages
  const navigate = useNavigate(); // For redirection

  const handleLogin = async (e) => {
    e.preventDefault(); // Prevent page refresh

    try {
      const response = await axios.post("http://localhost:8000/api/login/", {
        email,
        password,
      });

      // If login is successful, save token & redirect
      localStorage.setItem("token", response.data.token);
      alert("Login successful!");
      navigate("/dashboard"); // Redirect user to dashboard
    } catch (err) {
      setError("Invalid email or password. Please try again.");
    }
  };

  return (
    <div className="auth-container">
      <div className="auth-box">
        <div className="auth-left">
          <h1 className="auth-title">
            Welcome to <span className="highlight">BarakaNet!</span>
          </h1>
          <p className="auth-subtitle">
            Welcome back! Please login to your account.
          </p>

          <form onSubmit={handleLogin}>
            <div className="input-group">
              <label>Email Address</label>
              <input
                type="email"
                placeholder="hakeem@digital.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>
            <div className="input-group">
              <label>Password</label>
              <input
                type="password"
                placeholder="*************"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>
            {error && <p className="error">{error}</p>}{" "}
            {/* Show error message */}
            <div className="remember-forgot">
              <label>
                <input type="checkbox" /> Remember Me
              </label>
              <a href="#">Forgot Password?</a>
            </div>
            <div className="button-group">
              <button type="submit" className="login-btn">
                Login
              </button>
              <button
                type="button"
                className="signup-btn"
                onClick={() => navigate("/signup")}
              >
                Sign Up
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

export default Login;
