import matplotlib.pyplot as plt
import numpy as np
import time

G = 1

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Time taken: {elapsed_time}")
        return result
    return wrapper

class SolarSystem():
    def __init__(self, xmax, ymax, delta):
        self.bodies = []
        self.x = np.arange(-1*xmax, xmax, delta)
        self.y = np.arange(-1*ymax, ymax, delta)
        self.X, self.Y = np.meshgrid(self.x, self.y)
        self.Z_f = 0
    
    def addPlanet(self, body):
        self.bodies.append(body)

    @timeit
    def calculate_phi(self,):
        softening = 0.01

        Z_arr = []
        
        for body in self.bodies:
            m = body.mass
            x1 = body.position[0]
            y1 = body.position[1]
            Z = -G * m / np.sqrt((self.X - x1 + softening)**2 + (self.Y - y1 + softening)**2)
            Z_arr.append(Z)

        for z in Z_arr:
            self.Z_f += z

        print("Min Z_f:", np.min(self.Z_f))
        print("Max Z_f:", np.max(self.Z_f))

    def plot(self):

        lv = np.linspace(-50, 0, 100)

        plt.contour(self.X, self.Y, self.Z_f, levels=lv)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.colorbar(label='Gravitational Potential')
        plt.show()
        

class Planet():
    def __init__(self, mass, position):
        self.mass = mass
        self. position = position

    



planet1 = Planet(100, np.array([50,0]))
planet2 = Planet(10, np.array([0,0]))

system1 = SolarSystem(100,100,1)
system1.addPlanet(planet1)
system1.addPlanet(planet2)


system1.calculate_phi()
system1.plot()




