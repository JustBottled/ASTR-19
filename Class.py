class favAnimal():
	
	def print(self):
		print(f"My favorite animal is a {self.name}")
		print(f"Length of arms = {self.arms_length}")
		print(f"Length of legs = {self.legs_length}")
		print(f"Number of eyes = {self.num_eyes}")
		if self.have_tail:
			print(f"It has a tail.")
		else:
			print(f"It does not have a tail.")
		if self.is_furry:
			print("It is furry.")
		else:
			print(f"It is not furry.")

	def __init__(self, n="cat", aLength=0.0, lLength=11.0, eNums=2, t=True, f=True):
		self.name			= n
		self.arms_length	= aLength
		self.legs_length	= lLength
		self.num_eyes		= eNums
		self.have_tail		= t
		self.is_furry		= f

def main():
	fav_Animal = favAnimal()
	fav_Animal.print()

if __name__ == '__main__':
	main()