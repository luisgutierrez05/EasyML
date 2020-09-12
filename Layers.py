import Activations
import numpy as np

class Dense:
    def __init__(self, units, input_shape = None, name = None):
        self.units = units
        self.name = name
        if input_shape is not None:
            self.input_shape = input_shape
    def build(self, input_shape):
        if input_shape is None:
            self.input_shape = input_shape
        else:
            raise ValueError("The input shape for the layer")