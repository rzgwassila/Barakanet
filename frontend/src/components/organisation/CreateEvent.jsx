import React, { useState } from "react";
import axios from "axios";
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

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("event_name", eventData.eventName);
    formData.append("description", eventData.description);
    formData.append("date", eventData.date);
    formData.append("place", eventData.place);
    formData.append("requirements", eventData.requirements);
    formData.append("phone_number", eventData.phoneNumber);
    if (eventData.file) {
      formData.append("file", eventData.file);
    }

    try {
      const response = await axios.post(
        "http://localhost:8000/api/events/create/",
        formData,
        {
          headers: { "Content-Type": "multipart/form-data" },
        }
      );

      console.log("Event Created:", response.data);
      alert("Event successfully created!");

      // Reset form after submission
      setEventData({
        eventName: "",
        description: "",
        date: "",
        place: "",
        requirements: "",
        phoneNumber: "",
        file: null,
      });
    } catch (error) {
      console.error(
        "Error creating event:",
        error.response?.data || error.message
      );
      alert("Error creating event. Please try again.");
    }
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
        <button className="cancel-btn" type="reset">
          CANCEL
        </button>
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
