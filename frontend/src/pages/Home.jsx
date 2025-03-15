import React from "react";
import Navbar from "../components/common/Navbar";
import HeroSection from "../components/common/HeroSection";
import RestaurantList from "../components/common/RestaurantList";

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
