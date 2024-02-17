# the actual computational model 
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

D = 1  # Diffusion coefficient
U0 = 1  # Initial calcium concentration
Vp = 1  # Rate at which calcium is removed
J = 1  # Rate of change of calcium concentration per open channel
N = 10  # Number of ion channels
ion_channel_positions = np.linspace(0, 1, N)  # Positions of ion channels

# Define the initial condition for U
U_initial = np.full((N,), U0)  

def psi(t, U):
    return np.ones_like(U)

ion_channel_indices = np.round(ion_channel_positions * (len(U_initial) - 1)).astype(int)

# The PDE to be solved
def calcium_sparks(t, U):
    dUdt = np.zeros_like(U)
    for i in range(1, len(U) - 1):
        dUdt[i] = D * (U[i-1] - 2*U[i] + U[i+1])
    dUdt -= Vp * (U - U0) 
    for i in ion_channel_indices:
        dUdt[i] += J * psi(t, U[i])
    return dUdt

t_span = (0, 10)  
t_eval = np.linspace(t_span[0], t_span[1], 100)  

solution = solve_ivp(calcium_sparks, t_span, U_initial, t_eval=t_eval, method='RK45')

if solution.success:
    print("The integration was successful!")
else:
    print("The integration failed.")

for i in range(N):
    plt.plot(solution.t, solution.y[i], label=f'Ion channel {i+1}')

plt.xlabel('Time')
plt.ylabel('Calcium Concentration')
plt.title('Calcium Concentration Over Time')
plt.legend()
plt.show()
