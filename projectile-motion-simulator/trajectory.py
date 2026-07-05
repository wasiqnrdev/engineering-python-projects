import numpy as np

def time_of_flight(Initial_Velocity, Launch_Angle, Gravitational_Acceleration):
    angle_in_radians = np.radians(Launch_Angle)
    time = (2/Gravitational_Acceleration) * Initial_Velocity * np.sin(angle_in_radians)
    return time

def maximum_height(Initial_Velocity, Launch_Angle, Gravitational_Acceleration):
    angle_in_radians = np.radians(Launch_Angle)
    height = (Initial_Velocity * np.sin(angle_in_radians))**2 / (2 * Gravitational_Acceleration)
    return height

def range(Initial_Velocity, Launch_Angle, Gravitational_Acceleration):
    angle_in_radians = np.radians(Launch_Angle)
    double_angle = angle_in_radians * 2
    h_range = (1/Gravitational_Acceleration) * (Initial_Velocity ** 2) * np.sin(double_angle)
    return h_range
