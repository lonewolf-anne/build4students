
import numpy as np
import math

def run_driver_sim(velocity,medium):
    #print('This is a reaction and responce test done to  calculate the average responce time of a driver')
    medium=medium.lower()
    rate_dictionary={'eye':0.25,'ear':0.17,'touch':0.15}

    if medium not in rate_dictionary:
        return {"error":'Invalid input. Please try again.'}
    rate_reaction=rate_dictionary[medium]   #seconds . This is the average reaction rate of a human beign by vision
    deceleration=7   #m/s^2   # This the deceleration for dry roads 

    reaction_dis=round(velocity*rate_reaction,3)  #distance moved before brakes are applied.
    braking_dis=round(math.sqrt(velocity)/(2*deceleration),3)
    return {
            "medium":medium,
            "reaction_time":rate_reaction,
            "reaction_distance":reaction_dis,
            "braking_distance":braking_dis
        }
   