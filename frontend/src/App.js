

import {useState} from "react";
import Controls from "./components/Controls";
import Plots from "./components/Plots";
import Notes from "./components/Notes";
import DriverDashboard from "./components/DriverDashboard";
import RocketDashboard from "./components/RocketDashboard";
import "./App.css";
const API_BASE = "https://build4students-backend.onrender.com";

console.log(Controls, Plots, Notes);


function App() {
  const [mass, setMass] = useState(100);
  const [thrust, setThrust] = useState(5000);
  const [plotUrl, setPlotUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [mode,setMode] = useState("home");  //Mode rocket or driver default rocket

  const handleRocketSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    
    

    const response = await fetch(`${API_BASE}/api/rocket`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ mass, thrust }),
    });

    const data = await response.json();
    setPlotUrl(data.plot_url);
    setLoading(false);
  };

  return (
    <div className="App">
      <h2>Physics Simulations</h2>

      {mode==="home" &&(
      <div className="home">
        <h1>Welcome to Physics Simulations </h1>
        <p>Explore the physics of rockets and driver reactions through interactive simulations. Use the tabs above to switch between different simulations and visualize the results. Adjust parameters, run simulations, and gain insights into the fascinating world of physics!</p>
        <div className="home-buttons">
          <button onClick={()=>setMode("rocket")}>Try Rocket Simulation</button>
          <button onClick={()=>setMode("driver")}>Try Driver Simulation</button>
        </div>
      </div>
      )}
        {/*switch to rocket simulation */}
      <div className="tabs">
        <button onClick={()=>setMode("rocket")}>
          Rocket Simualtion 
        </button> 

        {/*switch to driver simulation */}
        <button onClick={()=>setMode("driver")}>
          Driver Reaction
        </button>
      </div>
        {mode==="rocket" && (

          <RocketDashboard
          mass={mass}
          setMass={setMass}
          thrust={thrust}
          setThrust={setThrust}
          plotUrl={plotUrl}
          loading={loading}
          onSubmit={handleRocketSubmit}
        />
        )}

          {mode==="driver" && 
          <DriverDashboard />}
          </div>
        );
      }
          

export default App;
