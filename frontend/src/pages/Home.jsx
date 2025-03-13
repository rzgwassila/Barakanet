import React from "react";
import Navbar from "../components/Navbar";
import HeroSection from "../components/HeroSection";
import RestaurantList from "../components/RestaurantList";

const Home = () => {
  return (
    <>
      <Navbar />
      <HeroSection />
      <RestaurantList />
    </>
  );
};

export default Home;
