import numpy as np
import matplotlib.pyplot as plt

from my_python_package.operators import (
        launch_angle_range
        )
def main():

    # Question 3
    x_max = [((1-(0.04))*0.001), ((1-(0.04))*0.1), ((1-(0.04))*0.2), ((1-(0.04))*0.3), ((1-(0.04))*0.4), ((1-(0.04))*0.5), ((1-(0.04))*0.6), ((1-(0.04))*0.7), ((1-(0.04))*0.8), ((1-(0.04))*0.9), ((1-(0.04))*1)]
    x_min = [((1+(0.04))*0.001), ((1+(0.04))*0.1), ((1+(0.04))*0.2), ((1+(0.04))*0.3), ((1+(0.04))*0.4), ((1+(0.04))*0.5), ((1+(0.04))*0.6), ((1+(0.04))*0.7), ((1+(0.04))*0.8), ((1+(0.04))*0.9), ((1+(0.04))*1)]
    y_min = [(launch_angle_range(2.0, 0.001, 0.04)[0]), (launch_angle_range(2.0, 0.1, 0.04)[0]), (launch_angle_range(2.0, 0.2, 0.04)[0]), (launch_angle_range(2.0, 0.3, 0.04)[0]), (launch_angle_range(2.0, 0.4, 0.04)[0]), (launch_angle_range(2.0, 0.5, 0.04)[0]), (launch_angle_range(2.0, 0.6, 0.04)[0]), (launch_angle_range(2.0, 0.7, 0.04)[0]), (launch_angle_range(2.0, 0.8, 0.04)[0]), (launch_angle_range(2.0, 0.9, 0.04)[0]), (launch_angle_range(2.0, 1, 0.04)[0])]
    y_max = [(launch_angle_range(2.0, 0.001, 0.04)[1]), (launch_angle_range(2.0, 0.1, 0.04)[1]), (launch_angle_range(2.0, 0.2, 0.04)[1]), (launch_angle_range(2.0, 0.3, 0.04)[1]), (launch_angle_range(2.0, 0.4, 0.04)[1]), (launch_angle_range(2.0, 0.5, 0.04)[1]), (launch_angle_range(2.0, 0.6, 0.04)[1]), (launch_angle_range(2.0, 0.7, 0.04)[1]), (launch_angle_range(2.0, 0.8, 0.04)[1]), (launch_angle_range(2.0, 0.9, 0.04)[1]), (launch_angle_range(2.0, 1, 0.04)[1])]
    
    plt.plot(x_min, y_min, '--b',label='min')
    plt.plot(x_max, y_max, ':r',label='max')
    plt.legend()
    plt.title("Figure 1: Minimum and Maximum Lanuch Angles over a range of Alpha values with Tolerance for Maximum Altitude being 0.04")
    plt.xlabel("Launch Angles (Radians)")
    plt.ylabel("Alpha")
    plt.savefig('/Users/matth/OneDrive/Desktop/GOPHLAB1/goph419-f2024-lab01-stMD/figures/Launch_Angles_over_Alpha.png', bbox_inches="tight")
    plt.show()

    # Question 4
    x_max = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4]
    x_min = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4]
    y_min = [(launch_angle_range(1.0, 0.25, 0.04)[0]), (launch_angle_range(1.2, 0.25, 0.04)[0]), (launch_angle_range(1.4, 0.25, 0.04)[0]), (launch_angle_range(1.6, 0.25, 0.04)[0]), (launch_angle_range(1.8, 0.25, 0.04)[0]), (launch_angle_range(2.0, 0.25, 0.04)[0]), (launch_angle_range(2.2, 0.25, 0.04)[0]), (launch_angle_range(2.4, 0.25, 0.04)[0])]
    y_max = [(launch_angle_range(1.0, 0.25, 0.04)[1]), (launch_angle_range(1.2, 0.25, 0.04)[1]), (launch_angle_range(1.4, 0.25, 0.04)[1]), (launch_angle_range(1.6, 0.25, 0.04)[1]), (launch_angle_range(1.8, 0.25, 0.04)[1]), (launch_angle_range(2.0, 0.25, 0.04)[1]), (launch_angle_range(2.2, 0.25, 0.04)[1]), (launch_angle_range(2.4, 0.25, 0.04)[1])]
    plt.plot(x_max, y_max, ':r', label='max')
    plt.plot(x_min, y_min, '--b',label='min')
    plt.legend()
    plt.title("Minimum and Maximum Launch Angles for a range of the Ratio Velocity")
    plt.xlabel("Ratio of Escape Velocity to Terminal Velocity")
    plt.ylabel("Launch Angles (Radians)")
    plt.savefig('/Users/matth/OneDrive/Desktop/GOPHLAB1/goph419-f2024-lab01-stMD/figures/Launch_Angles_over_Ratio_Velocity.png',bbox_inches="tight")
    plt.show()
    
if __name__ == '__main__':
    main()