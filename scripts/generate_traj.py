import numpy as np

def generate_trajectory(ax, ax_new, beta, alpha, steps):
    # Example function to generate a trajectory using DMP parameters
    trajectory = []
    for t in range(steps):
        x = np.sin(ax * t / steps) * np.exp(-beta * t / steps)  # Example calculation
        y = np.cos(ax_new * t / steps) * np.exp(-alpha * t / steps)  # Example calculation
        trajectory.append((x, y))
    return trajectory

best_params = (5.822907575701987, 8.614542308990474, 12.876585280801248, 20.977074359273495) # You have to add your best parameters after running DMP
trajectory = generate_trajectory(*best_params, steps=100)

