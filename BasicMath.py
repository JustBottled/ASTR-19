
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
	num1 = 2
	num2 = 6
	num3 = 7.8
	num4 = 3.7
	print(sumOf(num3, num4))
	print(diffOf(num2, num1))
	print(productOf(num3, num1))
	
if __name__ == '__main__':
	main()