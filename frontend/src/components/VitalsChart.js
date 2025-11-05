import React from "react";
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer
} from "recharts";

function VitalsChart({ data }) {
  return (
    <div style={{ margin: "30px auto", width: "90%", background: "#fff", padding: "20px", borderRadius: "10px", boxShadow: "0 2px 8px rgba(0,0,0,0.1)" }}>
      <h3 style={{ textAlign: "center", marginBottom: "20px" }}>📈 Live Vitals Graph</h3>
      <ResponsiveContainer width="100%" height={350}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="time" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="heartRate" stroke="#E63946" strokeWidth={2} dot={false} name="Heart Rate (bpm)" />
          <Line type="monotone" dataKey="temperature" stroke="#457B9D" strokeWidth={2} dot={false} name="Temp (°C)" />
          <Line type="monotone" dataKey="movement" stroke="#2A9D8F" strokeWidth={2} dot={false} name="Movement (g)" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

export default VitalsChart;
