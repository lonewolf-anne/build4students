from flask import Flask, request, jsonify
from flask_cors import CORS
from simulation.altrocket import run_altrocket_sim


import matplotlib
matplotlib.use("Agg") #allows plotting without dis

import matplotlib.pyplot as plt
import os
app = Flask(__name__)
CORS(app)

@app.route('/api/rocket', methods=["POST"])
def rocket_api():
    data = request.get_json()
    mass = float(data.get("mass", 100))
    thrust = float(data.get("thrust", 5000))
    
    result = run_altrocket_sim(mass,thrust) #run sim
    times=result["times"]
    altitudes=result["altitudes"]
    if not os.path.exists("static"):
        os.makedirs("static")
 #create plot
    plt.figure()
    plt.plot(times,altitudes)
    plt.xlabel("Time(s)")
    plt.ylabel("Altitude(m)")
    plt.title("Rocket Altitude vs Time")
    plt.grid(True)
    
    #save plot in a static folder
    plot_path=os.path.join("static","rocket_plot.png")
    plt.savefig(plot_path)
    plt.close()
    
    
    return jsonify({
        "plot_url":" http://localhost:5000/static/rocket_plot.png"
        })
    

@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
    return response
if __name__ == "__main__":
    app.run(debug=True)
 
    