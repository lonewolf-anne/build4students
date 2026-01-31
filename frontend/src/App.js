import {useState} from "react";
import Controls from "./components/Controls";
import Plots from "./components/Plots";
import Notes from "./components/Notes";
import "./App.css";
console.log(Controls, Plots, Notes);


function App() {
  const [mass, setMass] = useState(100);
  const [thrust, setThrust] = useState(5000);
  const [plotUrl, setPlotUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [thoughts, setThoughts] = useState("");
  const handleSubmit = async (e) => {
    e.preventDefault();


    setLoading(true);

    const response = await fetch("http://localhost:5000/api/rocket", {
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
      <h2>Rocket simulation</h2>

      <div className="dashboard">
        <div className="panel">
          
          <Controls
            mass={mass}
            setMass={setMass}
            thrust={thrust}
            setThrust={setThrust}
            onSubmit={handleSubmit}
          />
        </div>

        <div className="panel">
          {loading && <p id="loading">Generating graph...</p>}
          {plotUrl && (
            <img
              src={`${plotUrl}?t=${Date.now()}`}
              alt="Rocket Plot"
            />
          )}
        </div>
      </div>

      <div className="panel thoughts">
        <label>Your Thoughts:</label>
        <textarea
          value={thoughts}
          onChange={(e) => setThoughts(e.target.value)}
          placeholder="Write your thoughts here..."
          rows="4"
        />
      </div>
    </div>
  );
}

export default App;
