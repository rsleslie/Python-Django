def dic_order():
	d = {
	'Hendrix' : '1942',
	'Allman' : '1946',
	'King' : '1925',
	'Clapton' : '1945',
	'Johnson' : '1911',
	'Berry' : '1926',
	'Vaughan' : '1954',
	'Cooder' : '1947',
	'Page' : '1944',
	'Richards' : '1943',
	'Hammett' : '1962',
	'Cobain' : '1967',
	'Garcia' : '1942',
	'Beck' : '1944',
	'Santana' : '1947',
	'Ramone' : '1948',
	'White' : '1975',
	'Frusciante': '1970',
	'Thompson' : '1949',
	'Burton' : '1939', 
	}

	list_d = list(d.items()) 
	dic = {}
	for i in list_d:
		name = i[0]
		if name:
			name_get = dic.get(i[1])
		if name_get:
			new_name = sorted([name_get,name])
			dic[i[1]] = new_name[0] + ' ' + new_name[1]
		else:
			dic[i[1]] = i[0]
	list_dic = list(dic.items())
	list_dic = sorted(list_dic)
	new_dic = dict(list_dic)
	for value in new_dic:
		print(new_dic[value])

if __name__ == '__main__':
	dic_order()
