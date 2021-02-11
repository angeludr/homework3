import numpy as np
import os

sin = np.sin
cos = np.cos
pi = np.pi

def f(x):
    """function to test in our derivative
    program"""
    return 1 * sin(2*pi * (0.02) * x)

def analytic_deriv_f(x):
    """the analytical derivative of (1 m)*sin(2*pi*(0.02)*t)"""
    return 2*pi * 0.02 * cos(2*pi * 0.02 * x)

def forward_difference(x, h, func=None):
    """Computes the numerical derivative
    of an arbitrary function using the forward
    difference method.
    x: points at which the evaluate the func
    h: stepsize to compute the secant
    func: a valid python function"""
    numerator = func(x+h)-func(x)
    denominator = h
    return numerator/denominator
    
def central_difference(x, h, func=None):
    """Computes the numerical derivative
    of an arbitrary function using the central
    difference method.
    x: point at which to evaluate the func
    h: stepsize to compute the secant
    func: a valid python function"""
    numerator = func(x+h) - func(x-h)
    denominator = (2 * h)
    return numerator/denominator

if __name__ == "__main__":
    path_to_data = "sensor_position_data.txt"
    oscillator_data = np.loadtxt(path_to_data, skiprows=1, delimiter=',')
    #pulls out the first column (remember things start at 0 in python)
    oscillator_time = oscillator_data[:,0]
    oscillator_pos  = oscillator_data[:,1]
    
    #Open list to append output data
    output_data = []
    
    h = 0.01
    
    # Loop through an array from 1 to 100 in 0.01 steps
    for x_val in np.arange(1, 100, h):
        
        analyticdiff = analytic_deriv_f(x_val)
        fwdiff = forward_difference(x_val, h, f)
        centraldiff = central_difference(x_val, h, f)
        
        data = (x_val, analyticdiff, \
                fwdiff, centraldiff)
                
        output_data.append(data)

    np.savetxt('problem2_data.txt',
                np.array(output_data),
                delimiter = ',',
                header = ("function: 1 * sin(2*pi * (0.02) * x)\n"+
                "x, analytic_deriv(x), fw_diff(x), central_diff(x)"),
                fmt = '%.05f')
                
    print("Saved data to: ", 'problem2_data.txt' + '\n\n')
    
    os.system('python plotProblem2.py')
                
    # My graphs came out exactly the same so that hinders me on knowing if the analytical derivative match the computational derivative.
