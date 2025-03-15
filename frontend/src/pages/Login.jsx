import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "../styles/Auth.css";

const Login = () => {
  const [usernameOrEmail, setUsernameOrEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post("http://localhost:8000/api/login/", {
        username: usernameOrEmail, // Accepts username or email
        password,
      });

      // Store token and user details
      localStorage.setItem("token", response.data.token);
      localStorage.setItem("user", JSON.stringify(response.data.user));

      alert("Login successful!");
      console.log(response);

      // Redirect based on user role
      if (response.data.user.role === "volunteer") {
        navigate("/volunteer-dashboard");
      } else if (response.data.user.role === "charity") {
        navigate("/charity-dashboard");
      } else {
        navigate("/dashboard");
      }
    } catch (err) {
      setError("Invalid credentials. Please try again.");
    }
  };

  return (
    <div className="auth-container">
      <div className="auth-box">
        <div className="auth-left">
          <h1 className="auth-title">
            Welcome to <span className="highlight">BarakaNet!</span>
          </h1>
          <p className="auth-subtitle">Login to your account</p>

          <form onSubmit={handleLogin}>
            <div className="input-group">
              <label>Username or Email</label>
              <input
                type="text"
                placeholder="Enter your username or email"
                value={usernameOrEmail}
                onChange={(e) => setUsernameOrEmail(e.target.value)}
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
            {error && <p className="error">{error}</p>}
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
