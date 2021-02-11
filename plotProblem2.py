import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    
    data = np.loadtxt('problem2_data.txt', delimiter =',', skiprows = 2)
    
    # Calling the appropriate columns for plotting
    analyticDeriv = data[:,1]
    
    fwdiff = data[:,2]
    
    centraldiff = data[:,3]
    
    print("Analytical derivative: ")
    print(analyticDeriv)
    print('\n')
    
    print("Forward difference: ")
    print(fwdiff)
    print('\n')
    
    print("Central difference: ")
    print(centraldiff)
    print('\n')
    
    plt.plot(analyticDeriv, label = "Analytical Derivative")
    plt.plot(fwdiff, label = "Forward Difference")
    plt.plot(centraldiff, label = "Central Difference")
    
    plt.savefig('problem2_data.png')
    
    plt.legend()
    plt.show()
    
    
