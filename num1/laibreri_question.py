ex_d=int(input('enter expected date='))
re_d=int(input('enter return date='))
ex_m=int(input('enter ecpected month='))
re_m=int(input('enter return month='))
ex_y=int(input('enter expected year='))
re_y=int(input('enter a return year='))
if ex_y==re_y:
	if ex_m==re_m:
		if ex_d==re_d:
			print('no fine')
		else:
			print("your free is",15*(ex_d-re_d))
	else:
		print(500*(ex_m-re_m))
else:
	print(1000*(ex_y-re_y))