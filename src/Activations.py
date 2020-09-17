import numpy as np

class Relu:
    def forward(x):
        return np.array([max(0, y) for y in x])
    def backwards(x):
        return np.array([1 if y > 0 else 0 for y in x])

class Identity_Activation:
    def forward(x):
        return x
    def backwards(x):
        return np.ones_like(x)