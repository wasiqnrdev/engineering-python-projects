import numpy as np
import matplotlib.pyplot as plt
import trajectory

Planets = dict(Earth=9.81, Mars=3.72, Jupiter=24.79, Moon=1.625)

planet = input("""Choose a celestial object:
          
Earth
Mars 
Jupiter
Moon 

Choice: """)

while planet not in Planets:
    print(" ")
    print('Invalid planet, try again with proper upper and lower cases')
    print(" ")
    planet = input("""Choose a celestial object:
          
Earth
Mars 
Jupiter
Moon 

Choice: """)
    print(" ")

G = Planets[planet]
print(" ")
u = float(input("Enter the initial velocity: "))
theta = float(input("Enter the launch angle in degrees: "))



TimeOfFlight = trajectory.time_of_flight(u, theta, G)
MaximumHeight = trajectory.maximum_height(u, theta, G)
HorizontalRange = trajectory.range(u, theta, G)

theta = np.radians(theta)

t = np.linspace(0, TimeOfFlight, 500)

x = u * np.cos(theta) * t
y = u * np.sin(theta) * t - 0.5 * G * t**2

print(" ")
print(f"Time of Flight is {round(TimeOfFlight, 2)}s")
print(" ")
print(f"Maximum Height Reached is {round(MaximumHeight, 2)}m")
print(" ")
print(f"The Horizontal Distance Traveled is {round(HorizontalRange, 2)}m")
print(" ")

plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.title(f"Trajectory of Object on {planet}")
plt.grid(True)
plt.axis("equal")

plt.plot(x, y)

plt.savefig("trajectory.png", dpi=300)
plt.show()

