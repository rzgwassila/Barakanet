import React, { useState } from "react";
import OrganisationNavBar from "./OrgNavbar";
import "../../styles/ManageVolunteers.css";

const initialVolunteers = [
  {
    id: 1,
    name: "Ali Ben Omar",
    role: "volunteer",
    distance: "500m",
    contact: "0123456789",
    status: "Pending",
  },
  {
    id: 2,
    name: "Fatima Zahra Bouazza",
    role: "washer",
    distance: "10km",
    contact: "0123456789",
    status: "Pending",
  },
  {
    id: 3,
    name: "Youssef Kassimi",
    role: "volunteer",
    distance: "3km",
    contact: "0123456789",
    status: "Pending",
  },
  {
    id: 4,
    name: "Amina Tayebi",
    role: "food",
    distance: "5km",
    contact: "0123456789",
    status: "Pending",
  },
  {
    id: 5,
    name: "Nadia Meziani",
    role: "service",
    distance: "2km",
    contact: "0123456789",
    status: "Pending",
  },
  {
    id: 6,
    name: "Karim Belkacem",
    role: "service",
    distance: "6km",
    contact: "0123456789",
    status: "Pending",
  },
];

const ManageVolunteers = () => {
  const [volunteers, setVolunteers] = useState(initialVolunteers);
  const [selected, setSelected] = useState([]);

  const handleAccept = (id) => {
    setVolunteers(
      volunteers.map((v) => (v.id === id ? { ...v, status: "Accepted" } : v))
    );
  };

  const handleRefuse = (id) => {
    setVolunteers(
      volunteers.map((v) => (v.id === id ? { ...v, status: "Refused" } : v))
    );
  };

  const handleSelectAll = () => {
    setSelected(
      selected.length === volunteers.length ? [] : volunteers.map((v) => v.id)
    );
  };

  const handleSelect = (id) => {
    setSelected(
      selected.includes(id)
        ? selected.filter((s) => s !== id)
        : [...selected, id]
    );
  };

  const handleAcceptAll = () => {
    setVolunteers(
      volunteers.map((v) =>
        selected.includes(v.id) ? { ...v, status: "Accepted" } : v
      )
    );
    setSelected([]);
  };

  const handleRefuseAll = () => {
    setVolunteers(
      volunteers.map((v) =>
        selected.includes(v.id) ? { ...v, status: "Refused" } : v
      )
    );
    setSelected([]);
  };
  console.log("manage is rendering"); // ✅ Debugging log

  return (
    <div>
      <OrganisationNavBar />
    </div>
  );
};

export default ManageVolunteers;
