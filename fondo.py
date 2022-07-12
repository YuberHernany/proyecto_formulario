# we define class Cuadratica
import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
plt.style.use("dark_background")
x = sy.symbols('x')


class Cuadratica:
    def __init__(self, a, b, c):
        """a, b, c are floats, with a different from zero"""
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        return f"{self.a}x^2+{self.b}x+{self.c}"
    def discriminat(self):
        return self.b **2 - 4 * self.a * self.c
    def hasRealSols(self):
        return self.discriminat() >= 0
    def hasComplexSols(self):
        return not self.hasRealSols()
    def roots(self):
        if self.a != 0:
            if self.hasRealSols():
                x1 = (-self.b + np.sqrt(self.discriminat()))/(2*self.a)
                x2 = (-self.b - np.sqrt(self.discriminat()))/(2*self.a)
            elif self.hasComplexSols():
                x1 = (-self.b + 1j * np.sqrt(-self.discriminat()))/(2*self.a)
                x2 = (-self.b - 1j * np.sqrt(-self.discriminat()))/(2*self.a)
        return x1, x2
    def domainNearExtreme(self):
        if self.hasRealSols():
            x1, x2 = self.roots()
            dom = np.linspace(x2-1, x1+1)
        elif self.hasComplexSols():
            x1, _ = self.roots()
            dom = np.linspace(x1.real-4, x1.real+4)
        return dom
    def draw(self, **kwargs):
        ax = plt.gca()
        dom = self.domainNearExtreme()
        codom = self.a * (dom ** 2) + self.b * dom + self.c
        ax.plot(dom, codom, **kwargs)



if __name__ == "__main__":


    # c1 = Cuadratica(1,5,6)
    # c2 = Cuadratica(1,1,1)
    # fig, ax = plt.subplots()
    # c2.draw(color='yellow', linewidth=20)
    # plt.show()
    pass