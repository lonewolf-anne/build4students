import {useState} from "react"
const API_BASE = "https://build4students-backend.onrender.com";

//import "./App.css";
function DriverDashboard() {
    const[velocity,setVelocity]=useState("");
    const[plotUrl,setPlotUrl]=useState("");
    const[loading,setLoading]=useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true); // prevent refresh after each submit

        const response = await fetch(`${API_BASE}/api/driver`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ 
                medium: "eye",  //hardcoded for now, can add dropdown later
                max_velocity: velocity }),
        });
        const data = await response.json();
        setPlotUrl(data.plot_url);
        setLoading(false);
    };
    return(
        <div className="dashboard">
            <div className="panel">
                <form onSubmit={handleSubmit}>
                    <label>Vehicle Velocity (m/s):</label>
                    <input 
                    type="number"
                     value={velocity} 
                     onChange={(e) => setVelocity(Number(e.target.value))} 
                     /> 
                     <br /><br />
                        <button type="submit">Run Driver Simulation</button>
                         </form> 
                         </div> 
                         <div className="panel">
                             {loading && <p id="loading">Generating graph...</p>}
                             {plotUrl && ( <img src={`${plotUrl}?t=${Date.now()}`} alt="Driver Plot" /> )} 
                             </div> 
                            </div> 
                            ); 
                        }
export default DriverDashboard;
              