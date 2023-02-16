class HotBeverage:
	def __init__(self,  name = '', price = 0):
		self.price = price
		self.name = name
	def description(self):
		return "Just some hot water in a cup."
	def __str__(self):
		return 'nome : %s\nprice : %s\ndescription : %s' % (self.name,self.price, self.description())

class Coffee(HotBeverage):
	def __init__():
		pass

	def description(self):
		return  "A coffee, to stay awake."

class Tea(HotBeverage):
	def __init__():
		pass

	def description(self):
		return  "Just some hot water in a cup."

class Chocolate(HotBeverage):
	def __init__():
		pass

	def description(self):
		return  "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
	def __init__():
		pass

	def description(self):
		return   "Un po' di Italia nella sua tazza!"

if __name__=='__main__':

	print(HotBeverage('hot beverage', '0.30'))
	print(Coffee("Caffee", '0.40'))
	print(Tea("tea", '0.30'))
	print(Chocolate("chocolate", '0.50'))
	print(Cappuccino("cappuccino", '0.45'))