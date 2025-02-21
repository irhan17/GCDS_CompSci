#Imports matplotlib libraries to be used to graph data
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Defines ball class that initializes the data values and creates the datapoints using the physics formulas
class ball: 
    def __init__(self, dt, k, mass, v_i, v_i_pos, startX = 0, startY = 0):
        self.Xs = [startX]
        self.Ys = [startY]

        self.dt = dt
        self.k = k
        self.mass = mass
        self.v_i = v_i
        self.v_i_pos = v_i_pos
        self.time = 0

    def calculate(self):
        a = (-1)* self.k * self.v_i_pos / self.mass
        self.v_i = self.v_i + a * self.dt
        self.v_i_pos = self.v_i_pos + self.v_i * self.dt + 0.5 * a * self.dt ** 2
        self.time = self.time + self.dt
        
        self.Xs.append(self.time)
        self.Ys.append(self.v_i_pos)

#Adds a trail to ball movement and calls an instance of the ball class with specified parameters
trail = True
object_ball = ball(dt = 0.02, k = 5, mass = 2, v_i = 3, v_i_pos = 0)

#Function that animates the graphing display
def animate(i):
    #Begins by clearing the graph to prevent overlapping of data points and calls on the ball class functions
    plt.cla()
    object_ball.calculate()

    if trail:
        plt.plot(object_ball.Xs, object_ball.Ys)
    plt.scatter(object_ball.Xs[-1], object_ball.Ys[-1], marker="o", s=100)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Position (meters)")
    plt.title("Position vs Time - Irhan Iftikar")
    plt.grid()

fig, ax = plt.subplots()
animate = FuncAnimation(fig, animate, interval = 50)
plt.show()