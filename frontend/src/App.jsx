import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "leaflet/dist/leaflet.css";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import RestaurantFiltre from "./components/volunteer/RestaurantFiltre";

// Import Organisation Pages
import Dashboard from "./components/organisation/OrganizationDashboard";
import ManageVolunteers from "./components/organisation/ManageVolunteers";
import OrganisationLayout from "./components/organisation/OrganisationLayout";
import Profil from "./components/organisation/Profil";
import CreateEvent from "./components/organisation/CreateEvent";
import VolunteerList from "./components/organisation/VolunteersList";
const App = () => {
  console.log("App.js is rendering"); // ✅ Debugging log

  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/restaurants" element={<RestaurantFiltre />} />
      <Route path="/login" element={<Login />} />
      <Route path="/signup" element={<Signup />} />

      {/* Organisation Routes with Layout */}
      <Route path="/organisation/*" element={<OrganisationLayout />}>
        <Route path="dashboard" element={<Dashboard />} />
        <Route path="profil" element={<Profil />} />
        <Route path="create-event" element={<CreateEvent />} />
        <Route path="volunteers" element={<ManageVolunteers />} />
        <Route path="volunteerList" element={<VolunteerList />} />
      </Route>
    </Routes>
  );
};

export default App;
