# after computing the concentration overtime, plot it as a movie
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Define your list of lists of points (assuming each sublist represents a set of points for one frame)
points_list = [
    [[0, 0], [1, 1], [2, 2]],
    [[0, 0], [1, 1.5], [2, 2.5]],
    [[0, 0], [1, 2], [2, 3]],
    # Add more frames here as needed
]

# Define video parameters
fps = 10  # Frames per second
frame_size = (640, 480)  # Frame size

# Define video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter('graph_animation.mp4', fourcc, fps, frame_size)

# Create graphs and save frames
for points in points_list:
    plt.figure()
    plt.plot(*zip(*points), marker='o')
    plt.xlim(0, 3)  # Adjust limits as needed
    plt.ylim(0, 3)  # Adjust limits as needed
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Graph Animation')
    
    # Save the figure as an image
    plt.savefig('temp_frame.png')
    plt.close()
    
    # Read the saved image using OpenCV
    frame = cv2.imread('temp_frame.png')
    frame = cv2.resize(frame, frame_size)
    video_writer.write(frame)

# Release video writer
video_writer.release()

# Cleanup temporary file
import os
os.remove('temp_frame.png')

print("Video creation complete.")
