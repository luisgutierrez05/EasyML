class Relu:
    def forward(x):
        return max(0, x)
    def backwards(x):
        if x > 0:
            return 1
        return 0