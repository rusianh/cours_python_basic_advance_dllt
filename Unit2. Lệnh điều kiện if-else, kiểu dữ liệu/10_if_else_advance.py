age = 18

is_con_nit = False 
if age < 10:
	is_con_nit = True

if is_con_nit:
	print("con nit")
elif age == 18:
	print("18 tuoi tre trau")
elif age < 18:
	print("tre trau")
	if age >= 15 and age <= 17:
		print("sieu tre trau")
else:
	print("nguoi lon")