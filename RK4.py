import numpy as np 
import matplotlib.pyplot as plt 

def test(t,x):
    return np.sin(t)**2*x

def RK4(func, initial_condition, stop_time,  num_of_steps, start_time = 0):
    step_size = (stop_time - start_time)/num_of_steps
    solution = np.zeros(num_of_steps+1)
    solution[0] = initial_condition

    for t in range(num_of_steps):
        y = solution[t]
        k1 = func(t, y)
        k2 = func(t + step_size/2, y + k1/2)
        k3 = func(t + step_size/2, y + k2/2)
        k4 = func(t + step_size, y + k3)
        y = y + step_size*(k1 + 2*k2 + 2*k3 + k4)
        solution[t+1] = y
    return range(num_of_steps+1), solution

time, res = RK4(test,2,10,100)
plt.plot(time, res)
plt.show()