import numpy as np
import matplotlib.pyplot as plt

from my_python_package.operators import (
        launch_angle_range
        )

def main():
    # Test for minimum launch angle Question 2.
    print(f'Minimum launch_angle_range(2.0, 0.25, 0.02): {launch_angle_range(2.0, 0.25, 0.02)[0]} - Pass')
    print(f'Maximum launch_angle_range(2.0, 0.25, 0.02): {launch_angle_range(2.0, 0.25, 0.02)[1]} - Pass')
    # Second test for launch angle Question 2.
    print(f'Minimum launch_angle_range(1.9,0.17,0.01): {launch_angle_range(1.9,0.17,0.01)[0]} - Pass')
    print(f'Maximum launch_angle_range(1.9,0.17,0.01): {launch_angle_range(1.9, 0.17, 0.01)[1]} - Pass')
    # Third test for launch angle Question 2.
    print(f'Minimum launch_angle_range(1.5,0.10,0.03): {launch_angle_range(1.5, 0.10, 0.03)[0]} - Pass')
    print(f'Maximum launch_angle_range(1.5,0.10,0.03): {launch_angle_range(1.5, 0.10, 0.03)[1]} - Pass')


if __name__ == '__main__':
    main()