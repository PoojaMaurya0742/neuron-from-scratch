import math


def sigmoid(z):
    """Calculate the sigmoid activation."""
    return 1 / (1 + math.exp(-z))


def neuron(inputs, weights, bias):
    """Calculate the output of a single artificial neuron."""

    if len(inputs) != len(weights):
        raise ValueError("Inputs and weights must have the same length.")

    weighted_sum = 0

    # Calculate weighted sum
    for x, w in zip(inputs, weights):
        weighted_sum += x * w

    # Add bias
    z = weighted_sum + bias

    # Apply activation function
    output = sigmoid(z)

    return weighted_sum, z, output


def main():
    # Define inputs, weights, and bias
    inputs = [2, 4]
    weights = [0.5, 0.25]
    bias = 1

    # Calculate neuron output
    weighted_sum, z, output = neuron(inputs, weights, bias)

    # Display results
    print("=== Neuron From Scratch ===")
    print("Inputs:", inputs)
    print("Weights:", weights)
    print("Bias:", bias)
    print("Weighted Sum:", weighted_sum)
    print("Value after adding Bias (z):", z)
    print("Sigmoid Output:", output)


if __name__ == "__main__":
    main()