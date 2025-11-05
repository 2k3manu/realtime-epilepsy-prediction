import React from "react";

function AlertCard({ message, level }) {
  const colors = {
    high: "#E63946",    // red
    medium: "#F4A261",  // orange
    normal: "#2A9D8F"   // green
  };

  return (
    <div style={{
      backgroundColor: colors[level],
      color: "white",
      padding: "15px",
      borderRadius: "8px",
      margin: "10px auto",
      width: "60%",
      textAlign: "center",
      fontWeight: "bold",
      boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
    }}>
      {message}
    </div>
  );
}

export default AlertCard;
