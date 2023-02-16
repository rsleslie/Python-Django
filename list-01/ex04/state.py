import sys

def capital_city():
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
	for i in list_capital_cities:
		dic_cities[capital_cities[i]] = i

	dic_states = {}
	list_states = states.keys()
	list_states = list(list_states)
	for i in list_states:
		dic_states[states[i]] = i
	

	if sys.argv[1]:
		cities = dic_cities.get(sys.argv[1])
		state = dic_states.get(cities)
		if state:
			print(state)
		else:
			print("Unknown capital city")
	else:
		exit()

if __name__ == '__main__':
	capital_city()
