#Name: Irhan Iftikar
#Date: April 2025
#Description: CSX Assignment - Orbits
#Bonus: This is a bonus program that models the solar system of the four closest planets to the Sun
#Bugs: No notable bugs found in program
#Sources: Several internet sources for syntax (w3schools, Stack Overflow, GeeksForGeeks, etc.) and sources for physics formulas

#Imports libraries used in the program
import matplotlib.pyplot as plt
import math

#Class that defines the properties of each planet in the solar system
class Planet:
    #Function that initializes the data values and constants used in the program
    def __init__(self, name, mass, semi_major_axis, eccentricity, color):
        self.name = name
        self.mass = mass
        self.semi_major_axis = semi_major_axis
        self.eccentricity = eccentricity
        self.color = color
        self.G = 6.67e-11
        self.sun_mass = 1.989E+30
        #Establishes the initial conditions of the planet's orbit
        self.perihelion = self.semi_major_axis * (1 - self.eccentricity)
        self.x_initial = self.perihelion
        self.y_initial = 0
        self.v_perihelion = math.sqrt(self.G * self.sun_mass * (1 + self.eccentricity) / (self.semi_major_axis * (1 - self.eccentricity)))
        self.v_x_initial = 0
        self.v_y_initial = self.v_perihelion
        self.x_positions = []
        self.y_positions = []
        self.times = []

#Class that defines the properties of the solar system as a whole
class SolarSystem:
    #Function that initializes the data values and constants used in the program
    def __init__(self, dt, iterations):
        self.dt = dt
        self.iterations = iterations
        self.G = 6.67e-11
        self.sun_x = 0
        self.sun_y = 0
        self.sun_mass = 1.989E+30
        self.bodies = []
        planets_data = [("Mercury", 3.285E23, 0.583E+11, 0.21, 'gray'), ("Venus", 4.867E24, 1.077E+11, 0.007, 'orange'),
                        ("Earth", 5.97E24, 1.496E+11, 0.017, 'blue'), ("Mars", 6.39E23, 2.274E+11, 0.093, 'red')]
        for name, mass, semi_major_axis, eccentricity, color in planets_data:
            body = Planet(name, mass, semi_major_axis, eccentricity, color)
            self.bodies.append(body)
    
    #Simulates the orbital motion of each planet
    def simulate_orbit(self):
        for body in self.bodies:
            body.x_positions = [body.x_initial]
            body.y_positions = [body.y_initial]
            body.times = [0]
            x = body.x_initial
            y = body.y_initial
            vx = body.v_x_initial
            vy = body.v_y_initial
            time = 0
            #Calculates the relevant data points using physics formulas
            for row in range(self.iterations):
                dx = x - self.sun_x
                dy = y - self.sun_y
                ax = (-1 * self.G * self.sun_mass * dx) / ((dx**2 + dy**2)**(1.5))
                ay = (-1 * self.G * self.sun_mass * dy) / ((dx**2 + dy**2)**(1.5))
                vx += ax * self.dt
                vy += ay * self.dt
                x += vx * self.dt
                y += vy * self.dt
                body.x_positions.append(x)
                body.y_positions.append(y)
                time += self.dt
                body.times.append(time)
    
    #Plots the orbits of the planets in the solar system using matplotlib
    def plot_orbits(self):
        plt.figure(figsize=(12, 12))
        plt.plot(0, 0, 'yo', markersize=15, label='Sun')
        for body in self.bodies:
            plt.plot(body.x_positions, body.y_positions, linestyle='--', color=body.color, label=body.name)
        plt.title("Solar System Orbit (first 4 planets) - Irhan Iftikar")
        plt.xlabel("X-Position (meters)")
        plt.ylabel("Y-Position (meters)")
        plt.axis('equal')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

#Main function that runs the simulation and plots the orbits of the planets
def main():
    iterations = 20000
    dt = 3000
    solar_system = SolarSystem(dt, iterations)
    solar_system.simulate_orbit()
    solar_system.plot_orbits()

if __name__ == '__main__':
    main()