# importing packages
#import matplotlib.pyplot as plt
import random
import pandas as pd
from concurrent.futures import ProcessPoolExecutor
#from matplotlib.backends.backend_pdf import PdfPages


def randowo() -> int:
    return random.randint(300, 307)

def rollHandle(drop1: float, drop2: float, scores: int, cap: int) -> bool:
    roll = random.random()
    if scores >= 231599:
        return True
    else:
        if scores < cap:
            if (roll < drop1):
                return True
            else:
                return False
        if scores >= cap:
            if (roll < drop2):
                return True
            else:
                return False

def tmoe617Simulator(toggleScore: int) -> int:
    #initializing basic variables
    score = 0 #saves score in the current meter
    handles = 0 #total number of handles
    runs = 0 #total number of runs completed, kills loop at 100k
    addScore = (36 * score) / (231599) #the weight increase from meter
    droprate = ((18 + addScore) * (1 + (5735 / (13895 + addScore)))) / (13895 + addScore) #handle droprate with meter
    droprateOff = (18 * (1 + (5735 / 13895))) / 13895 #handle droprate without meter
    while (runs < 100000): #simulates 100,000 runs with toggleScore
        roll = rollHandle(droprate, droprateOff, score, toggleScore) #first handle roll
        kismetRoll = rollHandle(droprate, droprateOff, score, toggleScore) #kismetted handle roll, only calls if kismet is called
        #---------------------------------------------------------------------------------------------------------------------------------------
        if roll: #if a handle was rolled
            handles +=1 #increase handle counter
            if score >= toggleScore: #if the score is higher than the score at which meter is toggled (meter is off)
                if score >= 231599: #resets score if its also higher than meter itself (it was a meter handle which we toggled back on for)
                    score = randowo() #resets score
                else: #if it was not higher than the meter itself (not a meter handle AND meter is off)
                    score += randowo() #increases score
            if score < toggleScore: #if the score is LOWER than the score at which meter is toggled (meter is on)
                score = randowo() #resets score
        #---------------------------------------------------------------------------------------------------------------------------------------
        if not roll: #if a handle was NOT rolled, roll again with kismet
            if kismetRoll: #if kismet roll drops handle
                handles += 1 #increae handle counter
                if score >= toggleScore: #if meter is off (it cannot be above meter here)
                    score += randowo() #increase score
                if score < toggleScore: #if meter is on
                    score = randowo() #reset score
            if not kismetRoll: #if kismet still doesnt give handle
                score += randowo() #increase score
        runs +=1 #increase run counter
    return handles #return the number of handles

def callTmoe617Simulator(toggleScores: list) -> list:
    handlesList = []
    for toggleScore in toggleScores:
        handlesList.append(tmoe617Simulator(toggleScore))
    return handlesList

def main():
    num_simulations = 20
    toggle_scores = [1000 * i for i in range(231)]

    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(callTmoe617Simulator, toggle_scores) for _ in range(num_simulations)]
        handlesTensor = [future.result() for future in futures]

    dif = pd.DataFrame(handlesTensor).transpose()
    dif.columns = [f"Trial {i+1}" for i in range(num_simulations)]
    with pd.ExcelWriter('Data for 20 Handle Trials.xlsx') as writer:
        dif.to_excel(writer)

if __name__ == "__main__":
    main()