import React from "react";
import { Routes, Route } from "react-router-dom";
import "leaflet/dist/leaflet.css";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import RestaurantFiltre from "./components/RestaurantFiltre";
const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/restaurants" element={<RestaurantFiltre />} />{" "}
      <Route path="/login" element={<Login />} />
      <Route path="/signup" element={<Signup />} />
    </Routes>
  );
};

export default App;
