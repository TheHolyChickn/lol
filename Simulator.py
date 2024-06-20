# importing packages
import matplotlib.pyplot as plt
import random
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages

def randowo() -> int:
    return random.randrange(300, 307, 1)

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

def tmoe617Simulator(toggleScore: int, xlist: list, ylist: list) -> int:
    xx = []
    yy = []
    score = 0
    handles = 0
    addScore = (36 * score) / (231599)
    runs = 0
    droprate = ((18 + addScore) * (1 + (5735 / (13895 + addScore)))) / (13895 + addScore)
    droprateOff = (18 * (1 + (5735 / 13895))) / 13895
    while (runs < 100000):
        roll = rollHandle(droprate, droprateOff, score, toggleScore)
        if roll:
            handles +=1
            xx.append(score)
            yy.append(toggleScore)
            if score >= toggleScore:
                if score >= 231599:
                    score = randowo()
                else:
                    score += randowo()
            if score < toggleScore:
                score = randowo()
        if not roll:
            score += randowo()
        runs +=1
    xlist.append(xx)
    ylist.append(yy)
    return handles

def callTmoe617Simulator(xlist: list, ylist: list, handlesList: list):
    for i in range(0,231):
        r = 1000*i
        handlesList.append(tmoe617Simulator(r, xlist, ylist))
'''
def averageHandleScore(averages: list, xlist: list):
    for i in range(0,len(xlist)):
        avg = 0
        for j in range(0,len(xlist[i])):
            avg += xlist[i][j]
        averages.append(avg/len(xlist[i]))
'''

x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []
x8 = []
x9 = []
x10 = []
x11 = []
x12 = []
x13 = []
x14 = []
x15 = []
x16 = []
x17 = []
x18 = []
x19 = []
x20 = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
y7 = []
y8 = []
y9 = []
y10 = []
y11 = []
y12 = []
y13 = []
y14 = []
y15 = []
y16 = []
y17 = []
y18 = []
y19 = []
y20 = []
handles1 = []
handles2 = []
handles3 = []
handles4 = []
handles5 = []
handles6 = []
handles7 = []
handles8 = []
handles9 = []
handles10 = []
handles11 = []
handles12= []
handles13 = []
handles14 = []
handles15 = []
handles16 = []
handles17 = []
handles18 = []
handles19 = []
handles20 = []
xTensor = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20]
yTensor = [y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20]
handlesTensor = [handles1,handles2,handles3,handles4,handles5,handles6,handles7,handles8,handles9,handles10,handles11,handles12,handles13,handles14,handles15,handles16,handles17,handles18,handles19,handles20]
for i in range(0,20):
    callTmoe617Simulator(xTensor[i],yTensor[i],handlesTensor[i])

'''
averages1 = []
averages2 = []
averages3 = []
averages4 = []
averages5 = []
averages6 = []
averages7 = []
averages8 = []
averages9 = []
averages10 = []
averages11= []
averages12 = []
averages13 = []
averages14 = []
averages15 = []
averages16 = []
averages17 = []
averages18 = []
averages19 = []
averages20 = []
averagesTensor = [averages1, averages2, averages3, averages4, averages5, averages6, averages7, averages8, averages9, averages10, averages11, averages12, averages13, averages14, averages15, averages16, averages17, averages18, averages19, averages20]
for i in range(0,19):
    averageHandleScore(averagesTensor[i], xTensor[i])
'''
dif = pd.DataFrame({
    "Trial 1": handles1,    
    "Trial 2": handles2,
    "Trial 3": handles3,
    "Trial 4": handles4,
    "Trial 5": handles5,
    "Trial 6": handles6,
    "Trial 7": handles7,
    "Trial 8": handles8,
    "Trial 9": handles9,
    "Trial 10": handles10,
    "Trial 11": handles11,
    "Trial 12": handles12,
    "Trial 13": handles13,
    "Trial 14": handles14,
    "Trial 15": handles15,
    "Trial 16": handles16,
    "Trial 17": handles17,
    "Trial 18": handles18,
    "Trial 19": handles19,
    "Trial 20": handles20
})
with pd.ExcelWriter('Data for 20 Handle Trials.xlsx') as writer:
    dif.to_excel(writer)

''',
    "Average Score 1": averages1,
    "Average Score 2": averages2,
    "Average Score 3": averages3,
    "Average Score 4": averages4,
    "Average Score 5": averages5,
    "Average Score 6": averages6,
    "Average Score 7": averages7,
    "Average Score 8": averages8,
    "Average Score 9": averages9,
    "Average Score 10": averages10,
    "Average Score 11": averages11,
    "Average Score 12": averages12,
    "Average Score 13": averages13,
    "Average Score 14": averages14,
    "Average Score 15": averages15,
    "Average Score 16": averages16,
    "Average Score 17": averages17,
    "Average Score 18": averages18,
    "Average Score 19": averages19,
    "Average Score 20": averages20
    '''

''' #create graph
for i in range(0,len(x)-1):
    plt.scatter(x[i],y[i])
plt.xlabel('Score Handle Dropped at')
plt.ylabel('Score Meter Disabled at')
plt.title('Simulation owo')
plt.show()
'''