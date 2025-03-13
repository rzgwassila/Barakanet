import React from "react";
import "../styles/Auth.css";

const Login = () => {
  return (
    <div className="auth-container">
      <div className="auth-box">
        <div className="auth-left">
          <h1 className="auth-title">
            Welcome in <span className="highlight">BarakaNet!</span>
          </h1>
          <p className="auth-subtitle">
            Welcome back! Please login to your account.
          </p>

          <form>
            <div className="input-group">
              <label>Email Address</label>
              <input type="email" placeholder="hakeem@digital.com" required />
            </div>

            <div className="input-group">
              <label>Password</label>
              <input type="password" placeholder="*************" required />
            </div>

            <div className="remember-forgot">
              <label>
                <input type="checkbox" /> Remember Me
              </label>
              <a href="#">Forgot Password?</a>
            </div>

            <div className="button-group">
              <button className="login-btn">Login</button>
              <button className="signup-btn">Sign Up</button>
            </div>
          </form>
        </div>

        <div className="auth-right">
          <img
            src="/assets/bike-image.png"
            alt="Cyclist"
            className="auth-image"
          />
        </div>
      </div>
    </div>
  );
};

export default Login;
