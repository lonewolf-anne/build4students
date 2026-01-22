import matplotlib
matplotlib.use("Agg")  # 👈VERY IMPORTANT

import matplotlib.pyplot as plt
import numpy as np
import io, base64
def run_altrocket_sim(mass,thrust):
    altitude=0      # in m
    max_altitude=20 #km
    velocity=0      #m/s
    burn_rate=0.5      #kg/s
    g=9.8           #m/s^2
    dt=0.5          #s
    time=0          #s
    max_time=50 #200seconds
    dry_mass=200     # mass after fuel is burnt up

    velocities=[]
    times=[]
    altitudes=[]
    masses=[]


    while time <= max_time:
        time=+dt #store the values 
        altitudes.append(altitude) 
        velocities.append(velocity)
        times.append(time)
        masses.append(mass)
        print(f"t={time}s,altitude={altitude/1000:.2f}km,velocity={velocity:.2f}m/s,mass left={mass:.2f}kg")

        if mass>0:
            mass-=burn_rate*dt
            
            weight=mass*g
            acceleration=(thrust-weight)/mass
            velocity += acceleration *dt
            altitude += velocity*dt
            time +=dt
        if mass<=1:
            
            mass=0
            thrust=0
            break
            
    #Creating plote of altitude over time



    plt.figure(figsize=(6,4), dpi=80)
    plt.plot(times[::5], [a/1000 for a in altitudes[::5]])
    plt.xlim(0, max_time)
    plt.title('Altitude VS Time')
    plt.xlabel('Time(s)')
    plt.ylabel('Altitude(km)')
    plt.grid(True)


    
    
    #Convert to base64 string that can be imported by flask
    buf=io.BytesIO()
    plt.savefig(buf,format="png")
    buf.seek(0)
    img_base64=base64.b64encode(buf.getvalue()).decode()
    plt.close()
    print("Base64 length:", len(img_base64))
    return img_base64
    

 
