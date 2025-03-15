import React, { useState } from "react";
import "../../styles/VolunteerList.css";

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

const VolunteerList = () => {
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

  return (
    <div>
      <h2>Volunteer Management</h2>
      <table className="volunteer-table">
        <thead>
          <tr>
            <th>
              <input
                type="checkbox"
                checked={selected.length === volunteers.length}
                onChange={handleSelectAll}
              />
            </th>
            <th>Name</th>
            <th>Role</th>
            <th>Distance</th>
            <th>Contact</th>
            <th>Status</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {volunteers.map((v) => (
            <tr
              key={v.id}
              className={
                v.status === "Accepted"
                  ? "accepted"
                  : v.status === "Refused"
                  ? "refused"
                  : ""
              }
            >
              <td>
                <input
                  type="checkbox"
                  checked={selected.includes(v.id)}
                  onChange={() => handleSelect(v.id)}
                />
              </td>
              <td>{v.name}</td>
              <td>{v.role}</td>
              <td>{v.distance}</td>
              <td>{v.contact}</td>
              <td className={`status ${v.status.toLowerCase()}`}>{v.status}</td>
              <td>
                {v.status === "Pending" && (
                  <>
                    <button
                      className="accept-btn"
                      onClick={() => handleAccept(v.id)}
                    >
                      Accept
                    </button>
                    <button
                      className="refuse-btn"
                      onClick={() => handleRefuse(v.id)}
                    >
                      Refuse
                    </button>
                  </>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      <div className="bulk-actions">
        <button
          className="accept-all-btn"
          onClick={handleAcceptAll}
          disabled={selected.length === 0}
        >
          Accept Selected
        </button>
        <button
          className="refuse-all-btn"
          onClick={handleRefuseAll}
          disabled={selected.length === 0}
        >
          Refuse Selected
        </button>
      </div>
    </div>
  );
};

export default VolunteerList;
