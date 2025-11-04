import React from "react";

function VitalsCard(props) {
  const { title, value, unit, color } = props;

  return (
    <div style={{
      backgroundColor: "#f9f9f9",
      borderLeft: `6px solid ${color}`,
      borderRadius: "8px",
      padding: "20px",
      margin: "20px auto",
      width: "300px",
      boxShadow: "0px 2px 8px rgba(0,0,0,0.1)",
      textAlign: "center"
    }}>
      <h3>{title}</h3>
      <h1 style={{ color: color, fontSize: "40px" }}>
        {value} {unit}
      </h1>
    </div>
  );
}

export default VitalsCard;
