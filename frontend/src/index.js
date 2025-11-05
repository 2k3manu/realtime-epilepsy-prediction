import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";

// Removed StrictMode to avoid double-rendering of alerts
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
