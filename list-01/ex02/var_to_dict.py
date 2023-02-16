def my_dic():
	d = [
	('Hendrix' , '1942'),
	('Allman' , '1946'),
	('King' , '1925'),
	('Clapton' , '1945'),
	('Johnson' , '1911'),
	('Berry' , '1926'),
	('Vaughan' , '1954'),
	('Cooder' , '1947'),
	('Page' , '1944'),
	('Richards' , '1943'),
	('Hammett' , '1962'),
	('Cobain' , '1967'),
	('Garcia' , '1942'),
	('Beck' , '1944'),
	('Santana' , '1947'),
	('Ramone' , '1948'),
	('White' , '1975'),
	('Frusciante', '1970'),
	('Thompson' , '1949'),
	('Burton' , '1939')
	]

	dic = {}
	for i in d:
		name = i[0]
		if name:
			name_get = dic.get(i[1])
		if name_get:
			dic[i[1]] = name_get + ' ' + name
		else:
			dic[i[1]] = i[0]
	for item in dic:
		print(item, ":", dic[item])

if __name__ == '__main__':
	my_dic()		