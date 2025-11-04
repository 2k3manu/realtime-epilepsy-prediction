import Navbar from "./components/Navbar";
import VitalsCard from "./components/VitalsCard";

function App() {
  return (
    <div>
      <Navbar />
      <div style={{ textAlign: "center", marginTop: "30px" }}>
        <h2>Patient Live Vitals</h2>
      </div>

      <div style={{
        display: "flex",
        justifyContent: "center",
        flexWrap: "wrap"
      }}>
        <VitalsCard title="Heart Rate" value={82} unit="bpm" color="#E63946" />
        <VitalsCard title="Body Temp" value={36.7} unit="°C" color="#457B9D" />
        <VitalsCard title="Movement" value={1.2} unit="g" color="#2A9D8F" />
      </div>
    </div>
  );
}

export default App;
