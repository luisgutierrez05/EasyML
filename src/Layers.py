import unittest
import Activations
import numpy as np

class Input_Layer:
    def __init__(self, shape):
        self.shape = shape
    
    def __repr__(self):
        return f"Input Layer({self.shape})"

class Dense:
    def __init__(self, unit_num, input_shape = None, activation = Activations.Relu, name = "Dense"):
        self.unit_num = unit_num
        self.name = name
        self.activation = activation
        self.input_shape = input_shape

    def __repr__(self):
        return f"Dense({self.unit_num})"

    def build(self, input_shape):
        self.w = np.random.randn(input_shape, self.unit_num)
        self.b = np.random.randn(self.unit_num)

    def forward(self, inputs):
        pass