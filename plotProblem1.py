import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    fname_part1 = 'problem_1_1_data.txt'
    data_to_plot = np.loadtxt(fname_part1,
                              delimiter=',',
                              skiprows=2)
    print("Data to plot:")
    print(data_to_plot)
    
    print('\n')
    
    print("Generating problem 1 part 1 graph...")
    print('\n')
    
    print("Please close graph 1 to see graph 2")
    print('\n')
    
    plt.savefig('problem1_1_data.png')
    
    plt.plot(data_to_plot)
    plt.show()

    plt.clf()
    
    fname_part2 = 'problem1_2_data.txt'
    data2plot = np.loadtxt(fname_part2,
                            delimiter = ',',
                            skiprows = 1)
    
    print("Forward and central differences errors: ")
    print(data2plot)
    print('\n')
    
    print("Generating problem 1 part 2 graph...")
    
    plt.savefig('problem1_2_data.png')
    
    plt.plot(data2plot)
    
    plt.xscale('log')
    plt.yscale('log')
    
    plt.show()
