# do the probabilistic model update
import math
import numpy as np

k_U = 1

def get_updated_ion_channels(U: list, dt: float, ion_channels: list, x:list):
    """update the states of ion channels (0=close, 1=open)

    Args:
        U (list): the concentration list at time t 
        dt (float): delta t
        ion_channels (list): the indices of every ion channels (assume in increasing order)
        x (list): the indices of every concentration estimation point (assume in increasing order)
    """
    indices = find_interval_indices(ion_channels, x)
    con_ion = concentration_at_ion_channels(U, indices, ion_channels, x)
    ion_states = []
    for i in range(len(ion_channels)):
        k = estimate_k_close(con_ion[i]) if con_ion[i] == 0 else estimate_k_open(con_ion[i])
        threshold = 1 - math.exp(-k*dt)
        sample = np.random.uniform()
        if (sample<threshold):
            ion_states.append(0 if ion_channels[i] == 1 else 1)
        else:
            ion_states.append(1 if ion_channels[i] == 1 else 0)
    return ion_states
    
def find_interval_indices(list1, list2):
    indices = []
    j = 0
    for a in list1:
        while j < len(list2) - 1 and not (list2[j] <= a <= list2[j+1]):
            j += 1
        if j < len(list2) - 1:
            indices.append((j, j+1))
    return indices


def concentration_at_ion_channels(U:list, indices: list, ion_channels: list, x: list):
    concentration = []
    for index, (i1, i2) in enumerate(indices):
        con1 = U[i1]
        con2 = U[i2]
        ion_pos = ion_channels[index]
        l_end = x[i1]
        h_end = x[i2]
        con = round((con1*(h_end-ion_pos)+con2*(ion_pos-l_end))/(h_end-l_end), 2)
        concentration.append(con)
    return concentration
        
def estimate_k_close(u: float):
    # lower u -> higher k -> higher chance of open
    result = 0
    if (k_U == 1):
        result = u
    elif(k_U == 2):
        result = 0.5^u
    elif(k_U == 3):
        result = 1/u
    elif(k_U == 4):
        result = math.log(u,0.5)
    elif(k_U == 5):
        result = 0.5 if u<0.3 else 0.1
    
    return result

def estimate_k_open(u: float):
    # higher u -> higher k -> higher chance of close
    result = 0
    if (k_U == 1):
        result = u
    elif(k_U == 2):
        result = 2^u
    elif(k_U == 3):
        result = u^2
    elif(k_U == 4):
        result = math.log(u,2)
    elif(k_U == 5):
        result = 0.5 if u>0.3 else 0.1
    
    return result