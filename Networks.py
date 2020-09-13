import Layers
import numpy as np

class Model:
    def __init__(self, layers, input_shape = None):
        self.layers = layers

    def __repr__(self):
        res = """"""
        for layer in self.layers:
            res += layer.__repr__() + "\n"
        return res

    def build(self):
        for layer in layers:
            layer.build()

    def forward(self, inputs):
        pass