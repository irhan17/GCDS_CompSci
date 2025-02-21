#Name: Irhan Iftikar
#Date: February 2025
#Description: CSX Springs Assignment - visualizing spring graphs using Python
#Sources: Several internet sources for syntax (w3schools, Stack Overflow, etc.)

#Imports matplotlib libraries to be used to graph data
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Function that initializes the data values and creates the datapoints
def create_data():
    data = []
    dt = 0.02
    k = 5
    mass = 2
    v_i = 3
    v_i_pos = 0
    time = 0
    a_y = 0
    iterations = 400
    data.append([time, a_y, v_i, v_i_pos])
    
    #Gathers all the datapoints for the number of iterations chosen, and calculates them using physics formulas
    for i in range(iterations):
        time = time + dt
        a_y = (-1)* k * v_i_pos / mass
        v_i = v_i + a_y * dt
        v_i_pos = v_i_pos + v_i * dt + 0.5 * a_y * dt ** 2
        data.append([time, a_y, v_i, v_i_pos])
    return data

#Function that plots and animates the data on a graph using matplotlib
def plot(data):
    x_vals = []
    y_vals = []

    #Function that animates the graph, taking data from the proper index in the data list
    def animate(i):
        x_vals.append(data[i][0])  
        y_vals.append(data[i][3])
        line.set_data(x_vals, y_vals)
        return line,

    #Graphs the data points using matplotlib
    fig, ax = plt.subplots()
    line, = ax.plot([], [], label='Position vs Time')
    #Sets x and y axes boundary conditions
    ax.set_xlim(0, max(row[0] for row in data))
    ax.set_ylim(min(row[3] for row in data) - 1, max(row[3] for row in data) + 1)
    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Position (meters)")
    ax.set_title("Position vs Time - Irhan Iftikar")
    ax.grid(True)

    #Calls FuncAnimation library to animate the graph
    animate = FuncAnimation(fig, animate, frames=len(data), blit=True, interval=5, repeat=False)
    plt.show()

#Main function that executes the program
def main():
    data = create_data()
    plot(data)

if __name__ == "__main__":
    main()