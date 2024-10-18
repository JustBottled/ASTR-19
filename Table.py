import numpy as np

def table():

    x_elements = np.linspace(0, 2*np.pi, 1000)
    for x in x_elements:
        print(x, np.sin(x))
    
def main():
    table()

if __name__ == "__main__":
    main()