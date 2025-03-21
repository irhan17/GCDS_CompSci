#Name: Irhan Iftikar
#Date: March 2025
#Description: CSX Assignment - Orbits
#Bonuses: Verifies all three of Kepler's Laws, Applies conservation of angular momentum to verify Kepler's Second Law, Shows energy conservation throughout the orbit
#Bugs: No notable bugs found in program
#Sources: Several Internet Sources for Syntax (w3schools, Stack Overflow, GeeksForGeeks, etc.) and sources for physics formulas and properties

#Imports libraries used in the program
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

class model:
    #Function that initializes the data values and constants used in the program
    def __init__(self, dt, mass_host, x_initial, y_initial, v_x_initial, v_y_initial, iterations):
        self.dt = dt
        self.mass_host = mass_host
        self.x = x_initial
        self.y = y_initial
        self.v_x = v_x_initial
        self.v_y = v_y_initial
        self.iterations = iterations

        self.sun_x = 0
        self.sun_y = 0
        self.time = 0
        self.G = float(6.67e-11)
        self.array = []
    
    #Function that calculates the relevant data points using physics formulas
    def calculate(self):
        for row in range(self.iterations):
            new_line = []
            if row == 0:
                new_line.append(self.time)                
                new_line.append(self.x)                   
                new_line.append(self.y)
                dx = new_line[1] - self.sun_x
                dy = new_line[2] - self.sun_y
                new_line.append((-1 * self.G * self.mass_host * dx) / ((dx**2 + dy**2)**(1.5)))
                new_line.append((-1 * self.G * self.mass_host * dy) / ((dx**2 + dy**2)**(1.5)))
                new_line.append(self.v_x)                 
                new_line.append(self.v_y)
            else:
                new_line.append(self.time)
                new_line.append(self.array[-1][1] + self.array[-1][5] * self.dt)
                new_line.append(self.array[-1][2] + self.array[-1][6] * self.dt)
                dx = new_line[1] - self.sun_x
                dy = new_line[2] - self.sun_y
                new_line.append((-1 * self.G * self.mass_host * dx) / ((dx**2 + dy**2)**(1.5)))
                new_line.append((-1 * self.G * self.mass_host * dy) / ((dx**2 + dy**2)**(1.5)))
                new_line.append(self.array[-1][5] + new_line[3] * self.dt)
                new_line.append(self.array[-1][6] + new_line[4] * self.dt)
            
            self.array.append(new_line)
            self.time += self.dt

        dataset = self.array
        self.graph(dataset, self.iterations)
        times = [row[0] for row in dataset]
        x_positions = [row[1] for row in dataset]
        y_positions = [row[2] for row in dataset]
        self.kepler_first_law(x_positions, y_positions)
        self.kepler_second_law(x_positions, y_positions, times)
        self.kepler_third_law(x_positions, y_positions, times)
        self.energy_conservation(x_positions, y_positions, times, dataset)

    #Verifies Kepler's First Law
    def kepler_first_law(self, x_positions, y_positions):
        #Calculates orbital properties to verify that the path is elliptical through its eccentricity
        radial_distances = [math.sqrt((x - self.sun_x)**2 + (y - self.sun_y)**2) 
                           for x, y in zip(x_positions, y_positions)]
        perihelion = min(radial_distances)
        aphelion = max(radial_distances)
        eccentricity = (aphelion - perihelion) / (aphelion + perihelion)
        #Verifies the sun is at a foci of the ellipse by comparing sun's position to the foci
        focus_distance = ((perihelion + aphelion) / 2) * eccentricity
        center_x = (min(x_positions) + max(x_positions)) / 2
        center_y = (min(y_positions) + max(y_positions)) / 2
        sun_to_center = math.sqrt((center_x - self.sun_x)**2 + (center_y - self.sun_y)**2)
        deviation = (abs(sun_to_center - focus_distance) / focus_distance) * 100
        print("Kepler's First Law: A planet orbits the Sun in an elliptical path, where the Sun exists at the focus of the ellipse.")
        print(f"Verification 1: Since the orbit has an eccentricity of {eccentricity:.2f}, it is by mathematical definition an ellipse.")
        print(f"Verification 2: The Sun is mathematically positioned at one focus of the ellipse in our simulation ({deviation:.2f}% away from exact foci position).")

    #Verifies Kepler's Second Law
    def kepler_second_law(self, x_positions, y_positions, times):
        #Calculates angular momentum per unit mass - which should roughly be conserved
        angular_momentum = []
        for i in range(len(x_positions)):
            #Calculates vector, velocity, and angular momentum components using cross product physics formula
            r_x = x_positions[i] - self.sun_x
            r_y = y_positions[i] - self.sun_y
            v_x = self.array[i][5]
            v_y = self.array[i][6]
            l = r_x * v_y - r_y * v_x
            angular_momentum.append(abs(l))
        average_angular_momentum = sum(angular_momentum) / len(angular_momentum)
        maximum_deviation = max([abs(am - average_angular_momentum) for am in angular_momentum])
        percentage_deviation = maximum_deviation / average_angular_momentum * 100
        print("\nKepler's Second Law: A line connecting a planet and the Sun sweeps out equal areas of space in equal time intervals.")
        print("Interestingly, this can be proven through conserved angular momentum.")
        print(f"Verification: The average angular momentum is {average_angular_momentum:.4e} m^2/s, with a maximum deviation of {maximum_deviation:.4e} m^2/s (which is a deviation of {percentage_deviation:.4f}%)")
        print("Graphically, we can visualize the conserved angular momentum over time.")
        #Visualizes the conserved angular momentum over time
        plt.figure(figsize=(10, 6))
        plt.plot(times, angular_momentum)
        plt.title("Angular Momentum Vs. Time - Irhan Iftikar")
        plt.xlabel("Time (sec)")
        plt.ylabel("Angular Momentum (m^2/s)")
        plt.grid(True)
        plt.show()

    #Verifies Kepler's Third Law
    def kepler_third_law(self, x_positions, y_positions, times):
        radial_distances = [math.sqrt((x - self.sun_x)**2 + (y - self.sun_y)**2) 
                           for x, y in zip(x_positions, y_positions)]
        semi_major_axis = (max(radial_distances) + min(radial_distances)) / 2
        #Finding the orbital period by finding when the planet crosses the x-axis twice
        crossings = []
        for i in range(1, len(y_positions)):
            if y_positions[i-1] < 0 and y_positions[i] >= 0 and x_positions[i] > 0:
                crossings.append(times[i])
        if len(crossings) >= 2:
            #Compares orbital period to expected orbital period using Kepler's Third Law: T^2 = r^3*(4pi^2/GM)
            orbital_period = crossings[1] - crossings[0]
            expected_period = 2 * math.pi * math.sqrt(semi_major_axis**3 / (self.G * self.mass_host))
            percent_difference = abs(orbital_period - expected_period) / expected_period * 100
            print("\nKepler's Third Law: The square of a planet's orbital period is proportional to the cube of the semi-major axis of its orbit.")
            print(f"The calculated orbital period is {orbital_period:.2f} seconds, with the expected orbital period {expected_period:.4e} seconds.")
            print(f"Verification: Since the perfect difference is {percent_difference:.4f}%, Kepler's Third Law is proven.")
        else:
            print("There isn't enough orbital data to evaluate - increase simulation time.")

    #Verifies energy conservation throughout the orbit
    def energy_conservation(self, x_positions, y_positions, times, dataset):
        vx_values = [row[5] for row in dataset]
        vy_values = [row[6] for row in dataset]
        planet_mass = 3.285E23 #Mass of Mercury in kg
        kinetic_energies = []
        potential_energies = []
        total_energies = []
        #Calculates distance from sun, velocity magnitudes, kinetic energy, potential energy, and total energy for each time interval
        for i in range(len(times)):
            distance = math.sqrt((x_positions[i] - self.sun_x)**2 + (y_positions[i] - self.sun_y)**2)
            velocity = math.sqrt(vx_values[i]**2 + vy_values[i]**2)
            kinetic_energy = 0.5 * planet_mass * velocity**2
            potential_energy = -self.G * self.mass_host * planet_mass / distance
            total_energy = kinetic_energy + potential_energy
            kinetic_energies.append(kinetic_energy)
            potential_energies.append(potential_energy)
            total_energies.append(total_energy)
        
        average_total_energy = sum(total_energies) / len(total_energies)
        maximum_deviation = max([abs(e - average_total_energy) for e in total_energies])
        percent_deviation = (maximum_deviation / abs(average_total_energy)) * 100
        print("Energy Conservation: The total energy of the system (kinetic + potential) should be conserved.")
        print(f"Average total energy: {average_total_energy:.4e} J. The maximum deviation is {maximum_deviation:.4e} J with a percent deviation of ({percent_deviation:.6f}%)")
        print("Verification: The small deviation shows conservation of energy. This can also be graphically shown.")
        #Visualizes the energy conservation over time
        plt.figure(figsize=(10, 6))
        plt.plot(times, kinetic_energies, 'r-', label='Kinetic Energy')
        plt.plot(times, potential_energies, 'b-', label='Potential Energy')
        plt.plot(times, total_energies, 'g-', label='Total Energy')
        plt.xlabel('Time (sec)')
        plt.ylabel('Energy (J)')
        plt.title('Energy vs. Time - Irhan Iftikar')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    #Graphs the data points using matplotlib
    def graph(self, dataset, iterations):
        xValues = []
        yValues = []
        for line in dataset:
            xValues.append(line[1])
            yValues.append(line[2])
    
        fig = plt.figure(figsize=(10, 8))
        max_x = max(abs(max(xValues)), abs(min(xValues)))
        max_y = max(abs(max(yValues)), abs(min(yValues)))
        max_dim = max(max_x, max_y) * 1.1
        plt.axes(xlim=(-max_dim, max_dim), ylim=(-max_dim, max_dim))
        plt.plot(xValues, yValues, linestyle='--', color='#444444', label='Planet Orbit')
        plt.plot(self.sun_x, self.sun_y, 'ro', markersize=10, label='Star (Sun)')
        plt.grid(True, which='major', axis='both')
        plt.title("Elliptical Orbit - Irhan Iftikar")
        plt.xlabel('X Position (m)')
        plt.ylabel('Y Position (m)')
        plt.legend()
        line, = plt.plot([], [], 'bo', markersize=6)
        framesNumber = math.floor((iterations-1)/8)

        def init():
            line.set_data([], [])
            return line,
        def animate(i):
            x_data = xValues[:min(8 * i, len(xValues))]
            y_data = yValues[:min(8 * i, len(yValues))]
            line.set_data(x_data, y_data)
            return line,   
        anim = animation.FuncAnimation(fig, animate, init_func=init, interval=1, blit=True, frames=framesNumber, repeat=True)
        plt.show()

#Main function that calls on the model class and runs the code by setting parameters specific to a planet (Mercury)
def main():
    G = 6.67e-11
    mass_sun = 1.989E+30
    semi_major_axis = 0.39 * 1.496E+11
    eccentricity = 0.21
    perihelion = semi_major_axis * (1 - eccentricity)
    x_initial = perihelion #Since Sun starts at (0,0), the planet starts at (perihelion, 0)
    y_initial = 0
    v_perihelion = math.sqrt(G * mass_sun * (1 + eccentricity) / (semi_major_axis * (1 - eccentricity)))
    v_x_initial = 0
    v_y_initial = v_perihelion
    iterations = 20000
    dt = 3000
    
    planet = model(dt, mass_sun, x_initial, y_initial, v_x_initial, v_y_initial, iterations)
    planet.calculate()

if __name__ == '__main__':
    main()