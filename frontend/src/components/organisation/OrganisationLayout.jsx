import React from "react";
import { Outlet } from "react-router-dom";
import OrganisationNavBar from "./OrgNavbar";

const OrganisationLayout = () => {
  return (
    <div>
      <OrganisationNavBar />

      <div style={{ padding: "20px" }}>
        <Outlet />
      </div>
    </div>
  );
};

export default OrganisationLayout;
