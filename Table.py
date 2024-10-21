import numpy as np

def table():

    x_elements = np.linspace(0, 2*np.pi, 1000)
    sin_elements = np.sin(x_elements)
    for x in x_elements:
        print(x_elements[x], sin_elements[x])
    
def main():
    table()

if __name__ == "__main__":
    main()