def my_var():
	lis_var = [(42 , '42') , ('42', '42'), ('quarante-deux','quarante-deux'), (42.0, '42.0'), (True, 'True'), ([42], '[42]'), ({42 : 42}, '{42 : 42}'), ((42,), '(42,)'),({42}, '{42}')]	
	for value in lis_var:
		print(value[1],"has a type", type(value[0]))
		
if __name__ == '__main__':
	my_var()