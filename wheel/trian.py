class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_per_fig(self):
        return 2 * (self.a + self.b + self.c)