import React from "react";

function AlertCard({ message, level }) {
  const colors = {
    low: "#4CAF50",
    medium: "#FFB74D",
    high: "#E53935"
  };

  const bgColor = colors[level] || "#999";

  return (
    <div
      style={{
        background: bgColor,
        padding: "15px",
        borderRadius: "8px",
        color: "white",
        fontWeight: "bold",
        textAlign: "center",
        width: "60%",
        margin: "20px auto",
        boxShadow: "0 2px 6px rgba(0,0,0,0.15)"
      }}
    >
      {message}
    </div>
  );
}

export default AlertCard;

