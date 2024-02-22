import numpy as np
import math
from scipy.integrate import solve_ivp

# Constants and initial conditions for PDE
D = 1  # Diffusion coefficient
U0 = 1  # Initial calcium concentration
Vp = 1  # Rate at which calcium is removed
J = 1  # Rate of change of calcium concentration per open channel
N = 10  # Number of ion channels
ion_channel_positions = np.linspace(0, 1, N)  # Positions of ion channels
U_initial = np.full((N,), U0)  # Initial condition for U

# Probabilistic model functions (as provided)
# ...

# Define the ion channel indices based on their positions
ion_channel_indices = np.round(ion_channel_positions * (len(U_initial) - 1)).astype(int)

# The PDE to be solved
def calcium_sparks(t, U):
    # Update ion channel states using the probabilistic model
    ion_states = get_updated_ion_channels(U, t, ion_channel_indices, np.arange(N))
    # Calculate the PDE based on the updated ion channel states
    dUdt = np.zeros_like(U)
    for i in range(1, N - 1):
        dUdt[i] = D * (U[i-1] - 2*U[i] + U[i+1])
    dUdt -= Vp * (U - U0)
    for i, state in zip(ion_channel_indices, ion_states):
        dUdt[i] += J * state
    return dUdt

# Solve the PDE
t_span = (0, 10)
t_eval = np.linspace(t_span[0], t_span[1], 200)
solution = solve_ivp(calcium_sparks, t_span, U_initial, t_eval=t_eval, method='RK45')

# Check if the solution was successful
if not solution.success:
    raise Exception("The integration failed.")

# Prepare to store the data points for video generation
data_storage = []
iteration_step = 5  # Store data every 5 iterations

# Store the data points
for j in range(0, len(solution.t), iteration_step):
    frame_data = []
    for i in range(N):
        frame_data.append((solution.t[j], solution.y[i, j]))
    data_storage.append(frame_data)

# The 'data_storage' variable now holds the list of points for each frame.
# It can be used for generating the video as shown in the provided video generation code.
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

# Assuming data_storage has been populated as per the previous code

# Define video parameters
fps = 10  # Frames per second
frame_size = (640, 480)  # Frame size

# Define the path for the output video file
video_file_path = 'graph_animation.mp4'

# Define video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(video_file_path, fourcc, fps, frame_size)

# Create graphs and save frames
for frame_data in data_storage:
    plt.figure(figsize=(frame_size[0] / 100, frame_size[1] / 100), dpi=100)
    for i in range(N):
        plt.plot(*zip(*[frame_data[i]]), marker='o', label=f'Ion channel {i+1}')
    plt.xlim(0, t_span[1])
    plt.ylim(0, max(U_initial) + 1)  # Assuming the concentrations don't exceed initial concentration by much
    plt.xlabel('Time')
    plt.ylabel('Calcium Concentration')
    plt.title('Calcium Concentration Over Time')
    plt.legend()

    # Save the figure as an image in memory
    plt.savefig('temp_frame.png')
    plt.close()

    # Read the saved image using OpenCV
    frame = cv2.imread('temp_frame.png')
    frame = cv2.resize(frame, frame_size)
    video_writer.write(frame)

# Release video writer
video_writer.release()

# Cleanup temporary file
os.remove('temp_frame.png')

print("Video creation complete.")

