def return_numbers():
	f = open('numbers.txt', 'r')
	line = f.read().split(',')
	for i in line:
		print(i)

if __name__ == '__main__':
	return_numbers()
