from flask import Flask, request, jsonify
from flask_cors import CORS
from simulation.altrocket import run_altrocket_sim
from simulation.driver_reac import run_driver_sim
import matplotlib
import matplotlib.pyplot as plt
import os

matplotlib.use("Agg")  # allows plotting without display

app = Flask(__name__)
CORS(app)  # handles all CORS automatically
if not os.path.exists("static"):
    os.makedirs("static")

@app.route('/api/rocket', methods=["POST"])
def rocket_api():
    data = request.get_json()
    mass = float(data.get("mass", 100))
    thrust = float(data.get("thrust", 5000))
    
    result = run_altrocket_sim(mass, thrust)
    times, altitudes = result["times"], result["altitudes"]

    plt.figure()
    plt.plot(times, altitudes)
    plt.xlabel("Time(s)")
    plt.ylabel("Altitude(m)")
    plt.title("Rocket Altitude vs Time")
    plt.grid(True)
    plot_path = os.path.join("static", "rocket_plot.png")
    plt.savefig(plot_path)
    plt.close()

    return jsonify({"plot_url": "http://localhost:5000/static/rocket_plot.png"})


@app.route('/api/driver', methods=["POST"])
def driver_reaction_api():
    data = request.get_json()
    medium = data.get("medium", "eye")
    max_velocity = float(data.get("max_velocity", 30))

    velocities = list(range(0, int(max_velocity)+1, 5))
    reaction_distances = []

    for v in velocities:
        result = run_driver_sim(v, medium)
        reaction_distances.append(result["reaction_distance"])

    plt.figure()
    plt.plot(velocities, reaction_distances, marker='o')
    plt.xlabel("Velocity (m/s)")
    plt.ylabel("Reaction Distance (m)")
    plt.title(f"Reaction Distance vs Velocity ({medium.capitalize()})")
    plt.grid(True)
    plot_path =os.path.join("static","driver_reaction_plot.png")
    plt.savefig(plot_path)
    plt.close()

    return jsonify({"plot_url": "http://localhost:5000/static/driver_reaction_plot.png"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
