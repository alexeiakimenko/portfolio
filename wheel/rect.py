class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_per_fig(self):
        return 2 * (self.w + self.h)


__author__ = 'Alex'
print(f'Module {__name__} (author: {__author__})')
