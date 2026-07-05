import numpy as np

G = 6.67 * 10 ** -11

def orbital_velocity(mass_of_planet, radius_of_planet, orbital_altitude):
    speed = np.sqrt((G * mass_of_planet) / (radius_of_planet + orbital_altitude))
    return (speed)

def orbital_period(mass_of_planet, radius_of_planet, orbital_altitude):
    period = (2 * np.pi * (radius_of_planet + orbital_altitude)) / orbital_velocity(mass_of_planet, radius_of_planet, orbital_altitude)
    return (period)

def escape_velocity(mass_of_planet, radius_of_planet, orbital_altitude):
    escape_speed = np.sqrt(2) * orbital_velocity(mass_of_planet, radius_of_planet, orbital_altitude)
    return (escape_speed)
