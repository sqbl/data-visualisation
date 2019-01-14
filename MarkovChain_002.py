# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 14:02:21 2019

@author: sqbl
"""

import numpy as np
import matplotlib.pyplot as plt
import json

# Running beta version of the code. Transition probability matrix is supplyed 
# by user as both np.matrix and np.asarray:

#=========   Building prob matrix for test:     ===============================
P = np.matrix([[0.999587, 1.53664E-06, 1.63585E-05, 0.000237938, 0.000157167, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0.999588537, 0, 0, 0, 1.63585E-05, 0.000237938, 0.000157167, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0.999603359, 0, 0, 1.53664E-06, 0, 0, 0.000237938, 0.000157167, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0.999824938, 0, 0, 1.53664E-06, 0, 1.63585E-05, 0, 0.000157167, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0.999744167, 0, 0, 1.53664E-06, 0, 1.63585E-05, 0.000237938, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0.999604895, 0, 0, 0, 0, 0, 0.000237938, 0.000157167, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0.999826474, 0, 0, 0, 0, 1.63585E-05, 0, 0.000157167, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0.999745704, 0, 0, 0, 0, 1.63585E-05, 0.000237938, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0.999841296, 0, 0, 1.53664E-06, 0, 0, 0.000157167, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0.999760526, 0, 0, 1.53664E-06, 0, 0.000237938, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.999982105, 0, 0, 1.53664E-06, 1.63585E-05, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.999842833, 0, 0, 0, 0.000157167],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.999762062, 0, 0, 0.000237938],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.999983641, 0, 1.63585E-05],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.999998463, 1.53664E-06],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])
    
v = np.matrix([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

#========   Building as np.asarray:   =========================================

P_array = np.asarray([[0.999587, 1.53664E-06, 1.63585E-05, 0.000237938, 0.000157167, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0.999588537, 0, 0, 0, 1.63585E-05, 0.000237938, 0.000157167, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0.999603359, 0, 0, 1.53664E-06, 0, 0, 0.000237938, 0.000157167, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0.999824938, 0, 0, 1.53664E-06, 0, 1.63585E-05, 0, 0.000157167, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0.999744167, 0, 0, 1.53664E-06, 0, 1.63585E-05, 0.000237938, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0.999604895, 0, 0, 0, 0, 0, 0.000237938, 0.000157167, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0.999826474, 0, 0, 0, 0, 1.63585E-05, 0, 0.000157167, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0.999745704, 0, 0, 0, 0, 1.63585E-05, 0.000237938, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0.999841296, 0, 0, 1.53664E-06, 0, 0, 0.000157167, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0.999760526, 0, 0, 1.53664E-06, 0, 0.000237938, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.999982105, 0, 0, 1.53664E-06, 1.63585E-05, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.999842833, 0, 0, 0, 0.000157167],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.999762062, 0, 0, 0.000237938],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.999983641, 0, 1.63585E-05],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.999998463, 1.53664E-06],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])
    
v_array = np.asarray([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])


#==============================================================================
#============ Plotting the data as "conversion" as func of steps: ==============
#==============================================================================


def conversion_plotter(P,v,t):
    '''
    A function to plot the "conversion" between the states in the transition 
    probability matrix.
    Input:
        P: Transition probability matrix (rows sum to 1) as np.matrix
        v: Starting vector of system as np.matrix
        t: number of steps in simulation
    
    Could be used as: 
    
    _ = conversion_plotter(P,v,40000)
    
    '''
    # Get the data
    plot_data = []
    for step in range(t):
        result = v * P**step
        plot_data.append(np.array(result).flatten())
    
    # Convert the data format
    plot_data = np.array(plot_data)
    
    # Create the plot
    plt.figure(1)
    plt.xlabel('Steps')
    plt.ylabel('Probability')
    lines = []
    for i, shape in zip(range(15), ['b', '2', '3', 'g', 'r', '1','k','2','3','4','c','2','2','3','m','m']):
        line, = plt.plot(plot_data[:, i], shape, label="S%i" % (i+1))
        lines.append(line)
    #plt.legend(handles=lines, loc=1)
    plt.show()

#==============================================================================
#============ Making a random walk in the transition prob matrix ==============
#==============================================================================

def randomwalk(n, P, v, t):
    '''
    n=number of walks to simulate
    P=probability matrix as np.asarray
    v=starting vektor as np.asarray
    t=number of steps for each walk 
    
    Could be used as:
        
    walk = randomwalk(10,P_array,v_array,40000)
    
    '''
    result=[]
    for _ in range(n):
        steps_at_loc = 0
        present_loc = 0 #v.argmax()
        innerlist = []
        for i in range(t):
            new_loc = np.random.choice([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],p=list(P[present_loc])) #p=[0.993, 0.004, 0.003, 0.])
            #print(new_loc)
            if new_loc == present_loc:
                steps_at_loc += 1
            elif i == t:
                innerlist.append(present_loc)
                innerlist.append(steps_at_loc)
                print('i=t')
            elif new_loc != present_loc:
                innerlist.append(present_loc)
                innerlist.append(steps_at_loc)
                present_loc = new_loc
                steps_at_loc = 0
        innerlist.append(present_loc)
        innerlist.append(steps_at_loc)
        #if len(innerlist) == 2:
            #innerlist.append(present_loc)
            #innerlist.append(0)
            #innerlist.append(present_loc)
            #innerlist.append(0)
        #elif len(innerlist) == 4:
            #innerlist.append(present_loc)
            #innerlist.append(1199)
        #else:
            #print('hejsa')
        result.append(innerlist)
    return result

#==============================================================================
#============ Function for changing between different number of steps==========
#==============================================================================
'''

Still does not work:
    
def timechanger(data, new_time, old_time):
    new_list = []
    for i in range(len(data)):
        for n in range(len(data[i])):
            
            if n%2 == 0:
                new_list[i][n] = data[i][n]
            else:
                new_list[i][n] = data[i][data[i][n]*(new_time/old_time)]
    return new_list
'''

#==============================================================================
#============ Function for saving as json   ===================================
#==============================================================================

def filesaver(data,filename):
    '''
    Could be used as:
        
    filesaver(walk,'data.txt')
    
    '''
    with open(str(filename), 'w') as outfile:  
        json.dump(data, outfile)

