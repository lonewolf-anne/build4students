import React from "react";

//handles mass input
//thrust input 
//submit button

function Controls({ mass, setMass, thrust, setThrust, onSubmit }) {
  const acceleration=(thrust/mass).toFixed(2); //local acceleration

  return (
    <form onSubmit={onSubmit}>
      <label>Mass (kg):</label>
      <input
        type="number"
        value={mass}
        onChange={(e) => setMass(Number(e.target.value))}
      />
      <br /><br />

      <label>Thrust (N):</label>
      <input
        type="number"
        value={thrust}
        onChange={(e) => setThrust(Number(e.target.value))}
      />
      <br /><br />
      <p> Acceleration:{acceleration} m/s²</p>

      <button type="submit">Run Simulation</button>
    </form>
  );
}

export default Controls;
