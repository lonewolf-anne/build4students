import numpy as np

def run_altrocket_sim(mass, thrust):
    altitude = 0
    velocity = 0
    burn_rate = 0.5
    g = 9.8
    dt = 0.1 
    time = 0
    max_time = 50
    den_air=1.225 #kg/m^3=density of air at sea level
    drag_coef=0.75 # for a selender rocket
    ref_area=3 #m^2
    

    times = []
    altitudes = []

    for i in range(int(max_time / dt)):
        times.append(time)
        altitudes.append(altitude)

        if mass > 1:
            mass -= burn_rate * dt
            current_thrust=thrust
        else:
            current_thrust=0 #engine off
            
        weight = mass * g
            
        drag= 0.5*den_air*drag_coef*ref_area*velocity**2
        drag_force=np.sign(velocity)*drag
        net_force=thrust-weight-drag_force
            
        acceleration = (net_force) / mass
        velocity += acceleration * dt
        altitude += velocity * dt
        time += dt

        if mass <= 1:
            break

    return {
        "times": times,
        "altitudes": altitudes
    }
