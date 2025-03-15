import React, { useState } from "react";
import "../../styles/CreateEvent.css";

const CreateEvent = () => {
  const [eventData, setEventData] = useState({
    eventName: "",
    description: "",
    date: "",
    place: "",
    requirements: "",
    phoneNumber: "",
    file: null,
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setEventData({ ...eventData, [name]: value });
  };

  const handleFileChange = (e) => {
    setEventData({ ...eventData, file: e.target.files[0] });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Event Data:", eventData);
  };

  return (
    <div className="event-container">
      <div className="upload-section">
        <h3>Upload</h3>
        <div className="upload-box">
          <input type="file" onChange={handleFileChange} />
          <p>
            Drag & drop files or <span className="browse">Browse</span>
          </p>
        </div>
        <label>Event Name</label>
        <input
          type="text"
          name="eventName"
          value={eventData.eventName}
          onChange={handleChange}
        />
        <label>Event Informations</label>
        <input
          type="text"
          name="file"
          value={eventData.file ? eventData.file.name : ""}
          readOnly
        />
        <button className="cancel-btn">CANCEL</button>
      </div>

      <div className="event-details">
        <label>Description</label>
        <input
          type="text"
          name="description"
          value={eventData.description}
          onChange={handleChange}
        />
        <label>Date of Event</label>
        <input
          type="date"
          name="date"
          value={eventData.date}
          onChange={handleChange}
        />
        <label>Place</label>
        <input
          type="text"
          name="place"
          value={eventData.place}
          onChange={handleChange}
        />
        <label>Requirements</label>
        <input
          type="text"
          name="requirements"
          value={eventData.requirements}
          onChange={handleChange}
        />
        <label>Phone Number</label>
        <input
          type="text"
          name="phoneNumber"
          value={eventData.phoneNumber}
          onChange={handleChange}
        />
        <button className="upload-btn" onClick={handleSubmit}>
          UPLOAD EVENT
        </button>
      </div>
    </div>
  );
};

export default CreateEvent;
