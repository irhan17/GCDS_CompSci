#Names: Irhan Iftikar & Toby Knoll
#Date: May 2025
#Description: CSX Assignment - Rockets
#Bonus: Animates the launch that aims to hit the goal line

#Imports libraries used in the program
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Function that converts pressure to velocity using the formula provided
def velocity(pressure):
    return 0.226*pressure + 5.2
    #return 0.173*pressure + 6.87 (2024 data group #1)
    #return 0.226*pressure + 5.2 (2025 data group B - seems more accurate)

#Function that calculates the trajectory of the rocket
def calculate_trajectory(v_i, angle, launch_position, g=10, time_points = 100):
    #Converts angle to radians for numpy purposes and calculates v_x and v_y components
    angle = np.radians(angle)
    v_x = v_i * np.cos(angle)
    v_y = v_i * np.sin(angle)
    time_of_flight = (2 * v_y) / g
    #Creates time points and calculates position at each time point using physics equations
    t = np.linspace(0, time_of_flight, time_points)
    x_m = v_x * t
    y_m = v_y * t - 0.5 * g * t**2
    #Converts meters to yards
    x_yards = x_m / 0.9144
    y_yards = y_m / 0.9144
    x_yards = launch_position - x_yards
    return x_yards, y_yards, time_of_flight

#Function that aims to hit the goal line and finds the launch angle and pressure given the input of a yard line to launch from
def goal_line(launch_position):
    #Establishes minimum and maximum values for pressure and angle
    min_pressure, max_pressure = 30, 120
    pressure_step = 1
    min_angle, max_angle = 0, 90
    angle_step = 1
    #Initializes booleans as best values and generates ranges of pressures and angles to simulate
    best_distance_to_goal = float('inf')
    optimal_pressure = None
    optimal_angle = None
    pressures = np.arange(min_pressure, max_pressure + pressure_step, pressure_step)
    angles = np.arange(min_angle, max_angle + angle_step, angle_step)
    #Tests all combinations of pressures and angles
    for pressure in pressures:
        v_i = velocity(pressure)
        for angle in angles:
            x_yards, y_yards, _ = calculate_trajectory(v_i, angle, launch_position)
            #Where the rocket hits the ground (or y=0)
            landing_position = x_yards[-1]
            distance_to_goal = abs(landing_position)
            if distance_to_goal < best_distance_to_goal:
                best_distance_to_goal = distance_to_goal
                optimal_pressure = pressure
                optimal_angle = angle
    print(f"Goal Line - Optimal angle: {optimal_angle}°, Optimal pressure: {optimal_pressure} PSI")
    return optimal_angle, optimal_pressure

#Function that finds the pressure needed to make a field goal given the input of an angle from the 30 yard line
def field_goal(angle):
    #Establishes parameters, including launch position and height and horizontal position of the goal post
    launch_position = 30 
    goal_post_position = -10 #Goal posts are 10 yards behind the goal line
    goal_post_height = 10 * 0.33333333333 #Converts 10 feet to yards
    min_pressure, max_pressure = 30, 120
    pressure_step = 0.1
    best_pressure = None
    min_height_diff = float('inf')
    #Calculates the trajectory of the rocket for each pressure value
    for pressure in np.arange(min_pressure, max_pressure, pressure_step):
        v_i = velocity(pressure)
        x_yards, y_yards, _ = calculate_trajectory(v_i, angle, launch_position)
        for i in range(len(x_yards) - 1):
            #Checks if the trajectory crosses the goal post position
            if (x_yards[i] >= goal_post_position and x_yards[i+1] <= goal_post_position) or \
               (x_yards[i] <= goal_post_position and x_yards[i+1] >= goal_post_position):
                #Finds height at the goal post position
                t = abs(x_yards[i] - goal_post_position) / abs(x_yards[i] - x_yards[i+1])
                height_at_goal = y_yards[i] * (1 - t) + y_yards[i+1] * t
                if height_at_goal >= goal_post_height:
                    #Calculates how close the rocket is to the crossbar
                    height_diff = height_at_goal - goal_post_height
                    if height_diff < min_height_diff:
                        min_height_diff = height_diff
                        best_pressure = pressure
                break
    if best_pressure:
        print(f"Field Goal - Required pressure: {best_pressure} PSI (height above crossbar: {min_height_diff:.2f} yards)")
        return best_pressure
    else:
        print("Field Goal - No suitable pressure found for this angle")
        return None

#Function that animates the trajectory of the rocket launch
def animate(v_i, angle, launch_position):
    x_yards, y_yards, time_of_flight = calculate_trajectory(v_i, angle, launch_position)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(max(0, min(x_yards) - 5), max(launch_position + 5, max(x_yards) + 5))
    ax.set_ylim(0, max(y_yards) + 5)
    ax.set_xlabel('Distance from Goal Line (yards)')
    ax.set_ylabel('Height (yards)')
    ax.grid(True)
    ax.axvline(x=0, color='r', linestyle='-', label='Goal Line')
    ax.axvline(x=launch_position, color='g', linestyle='-', label='Launch Position')
    ax.legend()
    line, = ax.plot([], [], 'bo-', lw=2, markersize=8)
    info_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

    def init():
        line.set_data([], [])
        info_text.set_text('')
        return line, info_text
    
    def animate_frame(i):
        num_points = int((i + 1) * len(x_yards) / 100)
        x_data = x_yards[:num_points]
        y_data = y_yards[:num_points]
        line.set_data(x_data, y_data)
        if len(x_data) > 0:
            current_range = launch_position - x_data[-1]
        else:
            current_range = 0
        info_text.set_text(f'Velocity: {v_i:.2f} m/s\nAngle: {angle:.1f}°\nRange: {current_range:.2f} yards')
        return line, info_text
    
    ani = FuncAnimation(fig, animate_frame, frames=100, init_func=init, 
                      interval=time_of_flight*1000/100, blit=True)
    plt.title(f'Rocket Launch (Angle: {angle}°, Velocity: {v_i:.2f} m/s)')
    plt.show()
    return ani

#Main function that runs the program by calling the functions
def main():
    #Part 1: Finds optimal angle and pressure for a launch from a given yard line
    launch_position = 35
    angle, pressure = goal_line(launch_position)
    #Part 2: Finds pressure for a launch angle from the 30 yard line for a given launch angle
    test_angle = 45
    field_goal_pressure = field_goal(test_angle)
    #Part 3: Animation of the rocket launch from the given yard line
    v_i = velocity(pressure)
    animate(v_i, angle, launch_position)

#Calls main function to run the program
if __name__ == "__main__":
    main()
