# 🧠 Neuron From Scratch

A simple implementation of a **single artificial neuron from scratch using Python**, without using PyTorch, TensorFlow, NumPy, or any machine learning library.

The purpose of this project is to understand the basic mathematical operations behind an artificial neuron.

---

## 🎯 Objective

The neuron takes input values, applies corresponding weights, adds a bias, passes the result through an activation function, and produces an output.

### Flow

```text
Input
  ↓
Weights
  ↓
Weighted Sum
  ↓
+ Bias
  ↓
Activation Function
  ↓
Output
```

---

## 🧠 How It Works

### 1. Inputs

Inputs are the values provided to the neuron.

```python
inputs = [2, 4]
```

### 2. Weights

Each input has a corresponding weight that determines how much it contributes to the calculation.

```python
weights = [0.5, 0.25]
```

### 3. Weighted Sum

Each input is multiplied by its corresponding weight, and all the products are added together.

The formula is:

Weighted Sum += input(x) * weights(w)


For this example:

(2 * 0.5) + (4 * 0.25)

= 1 + 1

= 2

### 4. Bias

The bias is added to the weighted sum.

z = Weighted Sum + Bias

Here:

z = 2 + 1 = 3


The value `z` is then passed to the activation function.

### 5. Activation Function

This implementation uses the **Sigmoid activation function**.


Sigmoid(z) = 1/1 + e^(-z)

For:

z = 3

the output is approximately:0.9526

The sigmoid function produces an output between **0 and 1**.

---

## 🧮 Complete Example

### Given

```text
Inputs  = [2, 4]
Weights = [0.5, 0.25]
Bias    = 1
```

### Calculation

```text
Weighted Sum
= (2 × 0.5) + (4 × 0.25)
= 1 + 1
= 2

Add Bias
= 2 + 1
= 3

Sigmoid
= 1 / (1 + e^-3)
≈ 0.9526
```

### Final Output

```text
0.9525741268224334
```

---

## 💻 Implementation

The neuron is implemented using:

* Python functions
* `for` loop
* `zip()` to pair inputs with their corresponding weights
* Python's built-in `math` module for the exponential calculation

No machine learning frameworks or libraries are used.

---

## 🛠️ Technologies Used

* **Python**
* **Python Standard Library (`math`)**

### Libraries Not Used

* ❌ NumPy
* ❌ Pandas
* ❌ TensorFlow
* ❌ PyTorch
* ❌ Scikit-learn

---

## ▶️ How to Run

Make sure Python is installed.

Run the following command:

```bash
python neuron_from_scratch.py
```

### Expected Output

```text
=== Neuron From Scratch ===
Inputs: [2, 4]
Weights: [0.5, 0.25]
Bias: 1
Weighted Sum: 2.0
Value after adding Bias (z): 3.0
Sigmoid Output: 0.9525741268224334
```

---

## 📚 Key Concepts Learned

Through this implementation, the following concepts were explored:

* Artificial neurons
* Inputs and weights
* Weighted sum
* Bias
* Activation functions
* Sigmoid function
* Basic neural-network computation
* Implementing ML concepts without frameworks

---

## 👩‍💻 Author

**Pooja Maurya**

Built as part of an **AI Engineer Internship — Assignment #1**.
