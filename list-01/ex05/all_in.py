import sys

def more_arg():
	if len(sys.argv) != 2:
		sys.exit()
	states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
	}
	capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
	}

	dic_cities = {}
	list_capital_cities = capital_cities.keys()
	list_capital_cities = list(list_capital_cities)
	list_state = states.keys()
	list_state = list(list_state)
	value = 0
	for i in list_capital_cities:
		dic_cities[capital_cities[i]] = list_state[value]
		value += 1

	str_arg = [i.strip().title() for i in sys.argv[1].split(',')]
	str_arg = list(filter(None, str_arg))
	new_arg = []
	for value in str_arg:
		new_var = ""
		for splited in list(filter(None, value.split(' '))):
			new_var += splited + ' '
		new_arg += [new_var.strip()]
	
	for value in new_arg:
		state = states.get(value)
		cities = capital_cities.get(state)
		if cities:
			print(cities, "is the capital of", value)
		else:
			value_key = False
			for key in dic_cities:
				if value == key:
					value_key = True
			if value_key:
				print(value, "is the capital of", dic_cities[value])
			else:
				print(value, "is neither a capital city nor a state")

if __name__ == '__main__':
	more_arg()
