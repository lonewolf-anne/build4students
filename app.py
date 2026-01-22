from flask import Flask, render_template, request
from simulation.altrocket import run_altrocket_sim

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    
    if request.method == "POST":
        mass = float(request.form.get("mass"))
        thrust = float(request.form.get("thrust"))
        print("recieved mass:",mass)
        print("received thrust:",thrust)
    else:
        mass = 100
        thrust = 5000
    
    plot_url = "data:image/png;base64," + run_altrocket_sim(mass, thrust)
    return render_template("rocket.html", plot_url=plot_url)
if __name__ == "__main__":
    app.run(debug=True)

