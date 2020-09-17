class MeanSquaredError:
    def forward(self, y, yhat):
        return np.array((y - yhat) ** 2)
    def backward(self, y, yhat):
        return np.array(-2 * (y - yhat))