from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from simulation.altrocket import run_altrocket_sim
from simulation.driver_reac import run_driver_sim
import matplotlib
import matplotlib.pyplot as plt
import os
import time

# Use Agg backend for headless plotting
matplotlib.use("Agg")

# Initialize Flask app and allow CORS
app = Flask(__name__, static_folder="static")
CORS(app)

# Ensure static folder exists
if not os.path.exists("static"):
    os.makedirs("static")

# Route to serve static files (images)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

# Rocket simulation endpoint
@app.route('/api/rocket', methods=["POST"])
def rocket_api():
    data = request.get_json()
    mass = float(data.get("mass", 100))
    thrust = float(data.get("thrust", 5000))
    
    # Run simulation
    result = run_altrocket_sim(mass, thrust)
    times, altitudes = result["times"], result["altitudes"]

    # Generate unique filename
    filename = f"rocket_plot_{int(time.time())}.png"
    #plot_path = os.path.join(app.static_folder, filename)
    timestamp=int(time.time())
    filename=f"rocket_plot_{timestamp}.png"
    plot_path = os.path.join(app.static_folder, filename)
    plt.savefig(plot_path)
    # Plot and save
    plt.figure()
    plt.plot(times, altitudes)
    plt.xlabel("Time (s)")
    plt.ylabel("Altitude (m)")
    plt.title("Rocket Altitude vs Time")
    plt.grid(True)
    plt.savefig(plot_path)
    plt.close()

    # Return full Render URL
    backend_url ="https://build4students-backend.onrender.com"  # <-- Replace with your actual Render backend URL
    return jsonify({"plot_url": f"{backend_url}/static/{filename}"})

# Driver simulation endpoint
@app.route('/api/driver', methods=["POST"])
def driver_reaction_api():
    data = request.get_json()
    medium = data.get("medium", "eye").lower()
    max_velocity = float(data.get("max_velocity", 30))

    velocities = list(range(0, int(max_velocity)+1, 5))
    reaction_distances = []

    for v in velocities:
        result = run_driver_sim(v, medium)
        reaction_distances.append(result["reaction_distance"])

    # Generate unique filename
    filename = f"driver_plot_{int(time.time())}.png"
    plot_path = os.path.join(app.static_folder, filename)

    # Plot and save
    plt.figure()
    plt.plot(velocities, reaction_distances, marker='o')
    plt.xlabel("Velocity (m/s)")
    plt.ylabel("Reaction Distance (m)")
    plt.title(f"Reaction Distance vs Velocity ({medium.capitalize()})")
    plt.grid(True)
    plt.savefig(plot_path)
    plt.close()

    # Return full Render URL
    backend_url ="https://build4students-backend.onrender.com"  # <-- Replace with your actual Render backend URL
    return jsonify({"plot_url": f"{backend_url}/static/{filename}"})

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
