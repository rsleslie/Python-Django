import sys

def state():
	if len(sys.argv) != 2 :
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
	if sys.argv[1]:
		state = states.get(sys.argv[1])
		cities = capital_cities.get(state)
		if cities:
			print(cities)
		else:
			print("Unknown state")
	else:
		exit()

if __name__ == '__main__':
	state()