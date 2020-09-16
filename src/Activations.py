class Relu:
    def forward(x):
        return [max(0, y) for y in x]
    def backwards(x):
        return [1 if y > 0 else 0 for y in x]