import numpy as np


# Define the objective function
def objective_function(x):
    return x[0] ** 2 + x[1] ** 2


# Set the parameters
num_iter = 50  # max number of iterations
num_agents = 10  # number of agents (individuals)
dim = 2  # problem dimension (number of decision variables)
G0 = 100  # the gravitational constant
alpha = 20  # the power of distance function
lower_bound = -5  # the lower bound of decision variables
upper_bound = 5  # the upper bound of decision variables

# Initialize the agents (individuals)
agents_pos = lower_bound + (upper_bound - lower_bound) * np.random.rand(num_agents, dim)
agents_fitness = np.zeros(num_agents)

# Main loop
for i in range(num_iter):
    # Evaluate the fitness of each agent
    for j in range(num_agents):
        agents_fitness[j] = objective_function(agents_pos[j])

    # Find the best agent (individual)
    best_agent_idx = np.argmin(agents_fitness)
    best_agent_pos = agents_pos[best_agent_idx]

    # Calculate the distance between each agent and the best agent
    distance = np.zeros(num_agents)
    for j in range(num_agents):
        distance[j] = np.linalg.norm(best_agent_pos - agents_pos[j])

    # Calculate the gravitational constant for each agent
    G = G0 / (1 + alpha * distance) ** 2

    # Calculate the gravitational force acting on each agent
    force = np.zeros((num_agents, dim))
    for j in range(num_agents):
        for k in range(dim):
            force[j, k] = G[j] * (best_agent_pos[k] - agents_pos[j, k])

    # Calculate the new position for each agent
    for j in range(num_agents):
        agents_pos[j] = agents_pos[j] + force[j]

        # Check the bounds of the decision variables
        agents_pos[j] = np.maximum(lower_bound, agents_pos[j])
        agents_pos[j] = np.minimum(upper_bound, agents_pos[j])

    # Print the results
    print("Iteration", i + 1, ": Best fitness =", agents_fitness[best_agent_idx], "Best position =", best_agent_pos)
print(agents_pos)