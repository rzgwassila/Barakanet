import React from "react";
import "../styles/Auth.css";

const Signup = () => {
  return (
    <div className="auth-container">
      <div className="auth-box">
        <div className="auth-left">
          <h1 className="auth-title">
            Welcome in <span className="highlight">BarakaNet!</span>
          </h1>
          <p className="auth-subtitle">Create your account to get started.</p>

          <form>
            <div className="input-group">
              <label>Email Address</label>
              <input type="email" placeholder="hakeem@digital.com" required />
            </div>

            <div className="input-group">
              <label>Password</label>
              <input type="password" placeholder="*************" required />
            </div>

            <div className="input-group">
              <label>Password again</label>
              <input type="password" placeholder="*************" required />
            </div>

            <div className="input-group">
              <label>Role</label>
              <select>
                <option value="volunteer">Volunteer</option>
                <option value="donor">Donor</option>
              </select>
            </div>

            <div className="input-group">
              <label>Phone number</label>
              <input type="text" placeholder="0123456789" required />
            </div>

            <div className="input-group">
              <label>Location</label>
              <input type="text" placeholder="Algiers" required />
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
            src="../../public/images/auth.png"
            alt="Cyclist"
            className="auth-image"
          />
        </div>
      </div>
    </div>
  );
};

export default Signup;
