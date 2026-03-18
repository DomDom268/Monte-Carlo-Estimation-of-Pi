import streamlit as st
import random
import matplotlib.pyplot as plt
import numpy as np
import math 

st.title("Monte Carlo Estimation of π")

def estimate_pi(numPoints):
    
    points = np.random.rand(numPoints,2)
    distances = np.sum(points**2,axis = 1)
    inCircle = np.sum(distances <= 1 )
    
    return round(4 * (inCircle/numPoints),10)

# def visualizeError(x,y,xlabel,ylabel,title):
#     plt.figure(figsize=(8, 6))
#     plt.gca().invert_yaxis()
#     plt.scatter(x, y, color='blue', s=5)
#     plt.xlabel(xlabel)
#     plt.ylabel(ylabel)
#     plt.title(title)
#     plt.tight_layout()
#     plt.show()

def error(pi):
    return abs(round(np.pi-pi,4))

def visualize_pi(n_points,pi):
    points = np.random.rand(n_points, 2)
    inside = np.sum(points**2, axis=1) <= 1
    
    #plt.figure(figsize=(6, 6))
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Plot points inside the circle in blue, outside in red
    ax.scatter(points[inside, 0], points[inside, 1], color='dodgerblue', s=5, label='Inside')
    ax.scatter(points[~inside, 0], points[~inside, 1], color='tomato', s=5, label='Outside')
    
    # Add a visual boundary for the quarter-circle
    circle = plt.Circle((0, 0), 1, color='black', fill=False, linewidth=2)
    ax.gca().add_patch(circle)
    
    ax.xlim(0, 1)
    ax.ylim(0, 1)
    ax.legend()
    ax.title(f"$\\pi$ ({pi}) Estimation with {n_points} points")
    return fig

points = [10,100,1000,10000,100000]
selected_points = st.radio(
    "Select number of poitns generated",
    points,
    horizontal=True
)

if st.button("Run Simulation"):
    estimate = estimate_pi(selected_points)
    err = error(estimate)

    st.subheader(f"Estimated π: {round(estimate, 6)}")
    st.write(f"Error: {round(err, 6)}")

    fig = visualize_pi(selected_points,estimate)
    st.pyplot(fig)



# errors = []
# for point in points:
#     estimate = estimate_pi(point)
#     sim_error = error(estimate)
#     errors.append(sim_error)
#     print(f"With {point} points generated, the estimate of pi is {estimate} with a {sim_error} error")
#     visualize_pi(point,estimate)

