import physics as phy
import numpy as np
import constants
import matplotlib.pyplot as plt

def plot_orbit(planet_radius, orbital_altitude, planet):
    orbital_radius = planet_radius + orbital_altitude
    theta = np.linspace(0, 2 * np.pi, 500)
    orbit_x = orbital_radius * np.cos(theta)
    orbit_y = orbital_radius * np.sin(theta)
    plt.plot(orbit_x, orbit_y, color='blue', label='Orbit', linewidth=2)

    display_radius = planet_radius / 4

    planet_x = display_radius * np.cos(theta)
    planet_y = display_radius * np.sin(theta)
    plt.fill(planet_x, planet_y, color='green', label='Planet')
    plt.plot(planet_x, planet_y, color='black',)
    
    plt.axis('equal')
    plt.axis('off')
    plt.legend()
    plt.title(f'{planet} Orbit')
    plt.savefig('Orbit.png')

    plt.show()