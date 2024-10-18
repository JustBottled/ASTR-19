def sumOf(x, y):
    return x + y

def diffOf(x, y):
    if y > x:
        return y - x
    else:
        return x - y

def productOf(x, y):
    return x * y

def main():
    num1 = 7.8
    num2 = 3.7
    num3 = 2
    num4 = 6

    x = sumOf(num1, num2)
    y = diffOf(num3, num4)
    z = productOf(num1, num3)

    print(x)
    print("type: " + str(type(x)))
    print(y)
    print("type: " + str(type(y)))
    print(z)
    print("type: " + str(type(z)))

if __name__ == '__main__':
    main()
