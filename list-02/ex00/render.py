import sys, os, re

def myCV():
	if len(sys.argv) != 2:
		print("Error")
		sys.exit()
	if not (os.path.exists('myCV.template')):
		print("The file does not exist")
		exit()
	list_var = open("settings.py", 'r').read().split('\n')
	dic = {}
	for word in list_var:
		dic[word.split('=')[0].strip()] = word.split('=')[1].strip().replace('"', '')
	
	html = open('myCV.template', 'r').read()
	file_html = open('myCV.html', 'w')
	file_html.write(html.format(**dic))

if __name__ == '__main__':
	myCV()