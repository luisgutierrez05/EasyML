import Layers
import Losses
import Activations
import numpy as np

class Model:
    def __init__(self, layers):
        self.input_layer = layers[0]
        self.layers = layers[1:]

    def __repr__(self):
        res = """"""
        for layer in self.layers:
            res += layer.__repr__() + "\n"
        return res

    def build(self, loss = Losses.MeanSquaredError):
        self.loss = loss

        prev_layer_output = self.input_layer.shape

        for layer in self.layers:
            layer.build(prev_layer_output)
            prev_layer_output = layer.unit_num


    def forward(self, inputs):
        if inputs.shape[0] != self.input_layer.shape:
            raise ValueError("Mismatch in input dimensions to the neural net.")
        else:
            output = inputs
            for layer in self.layers:
                output = layer.forward(output)
            return output

    def backwards(self, loss_grad):
        pass