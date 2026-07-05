import physics as phy
from constants import planet_masses, planet_radii
import plot
import matplotlib.pyplot as plt

planet = input(
"""Choose a celestial body:
1. Earth
2. Moon
3. Mars
4. Jupiter

Enter your choice: """)

mass = planet_masses[planet]
radius = planet_radii[planet]

altitude = int(input('Enter orbital altitude (km): '))
altitude = altitude * 1000

print("""
Results
--------""")

print(f"""The orbital velocity is {round(phy.orbital_velocity(mass, radius, altitude) / 1000, 2)} km/s """)
print(f'The orbital period is {round(phy.orbital_period(mass, radius, altitude) / 60, 2)} minutes')
print(f'The escape velocity of the object is {round(phy.escape_velocity(mass, radius, altitude) / 1000, 2)} km/s')

plot.plot_orbit(radius, altitude / 1000, planet)