# Neural Networks - Roadmap

# 1. Motivation
**Inductive bias**
- Simplistic inductive bias limits us, e.g., Linear regression assumes linearly separable data.
- Complex human tasks like image recognition, movie recommendation, or graph-based social recommendation demand richer, non-linear inductive biases.
- Designing ML algorithms that incorporate these inductive biases manually is hard—and often task-specific.

**Feature engineering**
- Traditional ML models rely heavily on feature engineering.
- Feature engineering is the be-all-end-all in traditional ML.
- Two features combined in a specific way can be more informative than either alone.
- Traditional ML won’t do that automatically. We manually create all features. Every. Single. One.

**Curse of Dimensionality**
- As the number of features (dimensions) grows, data becomes sparse.
- Distance metrics (like Euclidean distance) lose meaning—everything looks equally far.
- Traditional ML models often fail because they rely heavily on these distance-based measures.

**Suggested resource:**
- [Blog: How do neural networks differ from traditional machine learning algorithms?](https://www.linkedin.com/advice/0/how-do-neural-networks-differ-from-traditional-aervc#:~:text=Machine%20Learning%20normally%20requires%20a,the%20weights%20at%20the%20layers.)


# 2. What is a Neural Network?
- A universal function approximator (Cybenko's Theorem). In simple terms, it can approximate ANY function.
- Designed to learn *representations*—features that are useful for a given task

## 2.1 How does it address the gaps highlighted in the motivation?
**Inductive bias and feature engineering**
- Learns complex feature combinations *automatically*
- Optimizes these features to perform well on a defined loss function
- Also learns the functions that *use* those features—joint feature & function learning
- In short: it learns *what to learn* and *how to use it*
- Magic? No. Gradient descent!

**Curse of dimensionality**
- Neural networks help by learning *low-dimensional representations* (embeddings) where structure is easier to find.
- Deep learning fights the curse of dimensionality by learning *the right features*, not relying on raw input space.

## 2.2 Notation
- **Neuron**: A function that transforms input to output, often non-linear
- **Weight**: Parameters learned during training
- **Activation**: The non-linearity (ReLU, Sigmoid, etc.)
- **Layer**: A collection of neurons working in parallel


## 2.3 What does a neural network learn?
- Think of it as learning *weighted, piecewise linear functions* (if using ReLU)
- Neurons activate selectively—like switches turning on for specific patterns
- Deep layers learn abstract, high-level representations

**Suggested resources**
- [Lecture: ML Lecture 35 - Cornell CS4780](https://youtu.be/kPXxbmBsFxs?si=RZw7u--3RO7OLO8E)
- [(Intuition) Blog/Video: Neural Networks - 3Blue1Brown](https://www.3blue1brown.com/topics/neural-networks)
- [(Optional) Book: "Neural Networks and Deep Learning" – Michael Nielsen (online book)](http://neuralnetworksanddeeplearning.com/)

# 3 Training a Neural Network
- Loss function (quantifies "how wrong") & gradient descent (how we get less wrong)
- Compared to linear regression:
    - No longer learning a simple function, but *layers* of nested functions
    - Many local minima, non-convexity
    - No closed-form solution

**Suggested resources:**
- [Lecture: ML Lecture 36 - Cornell CS4780](https://youtu.be/zmu9wR2c7Z4?si=0wgALoNJ4WmdqXen)

## 3.1 Working with an amalgamation of functions
- **Forward propagation**: compute outputs from inputs
- **Backward propagation**: compute gradients from the loss
- **Re-using computation**: dynamic programming meets chain rule

**Suggested resources:**
- [Blog: A Step by Step Backpropagation Example](https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/)
- [Practice: Derivative of the Softmax Function and the Categorical Cross-Entropy Loss](https://medium.com/data-science/derivative-of-the-softmax-function-and-the-categorical-cross-entropy-loss-ffceefc081d1)

## 3.1* Computational Graphs (Optional)
- Libraries like PyTorch and TensorFlow create a "computational graph" during forward pass.
- During backpropagation, the graph is used to compute gradients automatically.

## 3.2 Optimizers: Handling local minima and convergence
- **Momentum**: Add velocity to updates
- **RMSProp**: Adaptive learning rate
- **Adam**: Combines momentum + RMSProp (most commonly used)

**Suggested resources:**
- [YouTube: Momentun - Learn with Jay](https://youtu.be/Vce8w1sy0e8?si=6mjlo0-MYLKIhQfy)
- [YouTube: RMSprop - Learn with Jay](https://youtu.be/ajI_HTyaCu8?si=rSK4DmUNLxS2Zw8s)
- [YouTube: Adam - Learn with Jay](https://youtu.be/tuU59-G1PgU?si=g0fRAt-GSG5QGtQf)


## 3.3 Training Stabilizers & Regularization

### Batch Normalization
- Normalizes layer inputs across the batch to stabilize learning
- Helps gradients flow better by reducing internal covariate shift
- Acts like a regularizer in practice
- Often makes training faster and more robust to hyperparameter choices

**Suggested resources:**
- [Research paper: “Batch Normalization: Accelerating Deep Network Training”](https://arxiv.org/abs/1502.03167)

### Dropout
- Randomly “drops” neurons during training (sets them to 0)
- Prevents neurons from co-adapting too much
- Forces network to develop redundant representations = better generalization
- At test time, the full network is used (with scaled activations)

**Suggested resources:**
- [Sections 1 and 2: Research paper: “Dropout: A Simple Way to Prevent Neural Networks from Overfitting”](https://jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf)

### (Optional) Learning Rate Scheduling
- Adjust the learning rate over time, rather than keeping it constant
- Early in training, a higher learning rate helps the model explore the loss landscape quickly, making large updates that speed up convergence and help escape shallow local minima.
- Later in training, a lower learning rate allows the model to fine-tune around a good minimum, making small, careful updates that reduce the risk of overshooting or bouncing around the minimum.
- Gradually decaying the learning rate balances exploration and exploitation: first moving fast to find promising regions, then moving slow to precisely settle into an optimum.
- Popular methods: step decay, cosine annealing, cyclic learning rates.


# 4. What's Next?
- **CNNs**: Neural networks for images and spatial data.
- **RNNs**: Sequence models for text, speech, and time series.
- **Transformers**: Attention-based models (now dominant in NLP and beyond).
- **GNNs**: Graph neural networks for structured and relational data.
- **Reinforcement Learning**: Learning by interacting with an environment to maximize reward
- **TaBERT, TAPAS, TURL**: For tabular data.

Neural networks are a *foundation*—what you build next is up to you!


# 5. How to code up Neural Networks?
PyTorch (TensorFlow? Hard pass!)
- Widely used for research and production due to its ease of use and integration with Python.
- Working with PyTorch tensors is pretty much identical to working with NumPy arrays.
- PyTorch maintains a computaion graph. Remember section 3.1*?

**Suggested resources:**
- [YouTube: PyTorch Beginner Series](https://youtube.com/playlist?list=PL_lsbAsL_o2CTlGHgMxNrKhzP97BaG9ZN&si=gt2XRjlRtpafFWs0)
- [Official Documentation: Learn the Basics](https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html)
- [Book: Deep Learning with PyTorch by Eli Stevens, Luca Antiga, and Thomas Viehmann](https://g.co/kgs/bEqgfT9)
    - Written by PyTorch’s creator and key contributors
