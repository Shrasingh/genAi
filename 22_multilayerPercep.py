# limitation of perceptron vs advantage of multilayer perceptron
# only linearly separable data, can learn complex , non-linear functions making it suitable for a wider range of problems.
# single layer, multiple layers to extract complex features at different levels of abstraction
# limited capacity, adjustable model capacity
# prone to underfitting, better fit for complex data
# no or one hidden layer, hidden layers for better representation
# Architecture - perceptron - composed of a single layer of neurons
#                only includes an input layer and an op layer
#                lacks hidden layers
# multi layer p :-  composed of multiple layers of neurons  
#                  includes an input layer, hidden layers, and an op layer      
#                  can have one or more hidden layers
#                  allows for more complex representations


#Functionalities
# input layer - data input
# hidden layer - model training adjusting weight
# output layer op 

#Activation F - add non linearity

#  Forward Propagation:
# What: The input flows forward through the network to produce an output.

# How:
#  Input → Weighted sum → Activation → Output (layer by layer)

# ✅ Used to predict and calculate loss

# 🔹 Backward Propagation:
# What: The error (loss) flows backward to update weights.

# How:
# Compute gradients using chain rule → Update weights using gradient descent

# ✅ Used to train the model (learn from mistakes)

# 🔁 Summary:
# Forward = Predict

# Backward = Learn (update weights)
# 
# 