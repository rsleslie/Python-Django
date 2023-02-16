import random 
from beverages import * 

class CoffeeMachine:
	def __init__(self):
		self.drinks = 0

	class EmptyCup(HotBeverage):
		def __init__(self):
			self.name = "empty cup"
			self.price = '0.90'
		def description(self):
			return "An empty cup?! Gimme my money back!"
	
	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__(self,"This coffee machine has to be repaired.")

	def repair(self):
		self.drinks = 0
	
	def serve(self, list_method):
		if self.drinks < 10:
			self.drinks += 1
			return random.choice([list_method, self.EmptyCup()])
		else:
			raise self.BrokenMachineException() 

if __name__=='__main__':
	
	
	value = CoffeeMachine()

	list_method = [Coffee(), Cappuccino(), Tea(), Chocolate()]
	for i in range(22):
		try:
			print(value.serve(random.choice(list_method)))
		except:
			value.repair()