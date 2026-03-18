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

def visualizeError(x,y,xlabel,ylabel,title):
    fig, ax = plt.subplots(figsize=(8, 6))

    ax.plot(x,y,marker = 'o') #Empirical error

    scale = y[0] * np.sqrt(x[0])
    theoretical = scale / np.sqrt(x)
    
    ax.plot(x, theoretical, linestyle='--', label="~ 1/√n (theoretical)") #Theoretical error
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    # ax.set_xscale('log')
    # ax.set_yscale('log')
    ax.set_title(title)
    ax.legend
    return fig

def error(pi):
    return abs(round(np.pi-pi,4))

def generate_convergence(max_points):
    steps = np.logspace(1, np.log10(max_points), num=10, dtype=int)
    
    errors = []
    for n in steps:
        pi_est = estimate_pi(n)
        err = abs(np.pi - pi_est)
        errors.append(err)
    
    return steps, errors
    
def visualizePi(n_points,pi):
    points = np.random.rand(n_points, 2)
    inside = np.sum(points**2, axis=1) <= 1
    
    #plt.figure(figsize=(6, 6))
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Plot points inside the circle in blue, outside in red
    ax.scatter(points[inside, 0], points[inside, 1], color='dodgerblue', s=5, label='Inside')
    ax.scatter(points[~inside, 0], points[~inside, 1], color='tomato', s=5, label='Outside')
    
    # Add a visual boundary for the quarter-circle
    circle = plt.Circle((0, 0), 1, color='black', fill=False, linewidth=2)
    ax.add_patch(circle)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.legend()
    ax.set_title(f"$\\pi$ ({pi}) Estimation with {n_points} points")
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
    steps, errors = generate_convergence(selected_points)

    st.subheader(f"Estimated π: {round(estimate, 6)}")
    st.write(f"Error: {round(err, 6)}")

    fig = visualizePi(selected_points,estimate)
    st.pyplot(fig)

    fig = visualizeError(
    steps,
    errors,
    "Number of Points",
    "Error",
    "Convergence of Monte Carlo π Estimate"
)
    st.pyplot(fig)



# errors = []
# for point in points:
#     estimate = estimate_pi(point)
#     sim_error = error(estimate)
#     errors.append(sim_error)
#     print(f"With {point} points generated, the estimate of pi is {estimate} with a {sim_error} error")
#     visualize_pi(point,estimate)

