class MeanSquaredError:
    def forward(self, y, yhat):
        return (y - yhat) ** 2
    def backward(self, y, yhat):
        return -2 * (y - yhat)