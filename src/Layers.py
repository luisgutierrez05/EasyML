import Activations
import numpy as np

class Input_Layer:
    def __init__(self, shape, name = None):
        self.shape = shape
        if name is None:
            self.name = self.__repr__()
        else:
            self.name = name
    
    def __repr__(self):
        return f"Input Layer({self.shape})"

class Dense:
    def __init__(self, unit_num, activation = Activations.Relu, name = "Dense"):
        self.unit_num = unit_num
        self.activation = activation
        if name is None:
            self.name = self.__repr__()
        else:
            self.name = name

    def __repr__(self):
        return f"Dense({self.unit_num})"

    def build(self, input_shape):
        self.w = np.random.randn(input_shape, self.unit_num)
        self.b = np.random.randn(self.unit_num)

    def forward(self, prev_layer):
        return self.activation.forward(prev_layer @ self.w + self.b)

    def backwards(self, lr, prev_grad):
        pass