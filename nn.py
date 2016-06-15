import numpy as np

class NeuralNetwork:

  def __init__(self, shape):
    self.layers = []

    for i in range(len(shape) - 1):
      self.layers.append({
        "weights": np.random.normal(0, .001, [shape[i] + 1, shape[i + 1]]),
        "a": None,
        "z": None,
        "d": None
      })

  def forward_propagate(self, input):

    for i in range(len(self.layers)):
      if i == 0:
        layer_input = input
      else:
        layer_input = self.layers[i - 1]["a"]
      self.layers[i]["z"] = np.dot(self.layers[i]["weights"].T, np.append(layer_input, 1))
      self.layers[i]["a"] = 1 / (1 + np.exp(-self.layers[i]["z"]))


  def back_propagate(self, predicted, actual):

    for i in range(len(self.layers) - 1):

      layer = len(self.layers) - 1 - i
      prev = layer - 1

      if i == 0:
        self.layers[layer]["d"] = (predicted - actual) * actual * (1 - actual)

      self.layers[prev]["d"] = np.dot(
                                 self.layers[layer]["weights"],
                                 self.layers[layer]["d"]
                               ) * self.layers[layer]["a"] * (1 - self.layers[layer]["a"]);

  def gradient(self):


  def train(self, batch):

    for x, y in batch:
      self.forward_propagate(x)
      output = self.layers[len(self.layers) - 1]["a"]
      self.back_propagate(output, y)
      d = learning_rate * self.gradient()
      for layer in range(len(d)):
        self.layers[layer]["w"] += 



x = NeuralNetwork([5, 3, 2])
x.forward_propagate([1,1,1,1,1])
x.back_propagate(x.layers[len(x.layers) - 1]["a"], np.array([1, 0]))
print x.layers