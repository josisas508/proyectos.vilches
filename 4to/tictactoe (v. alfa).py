respuesta1=input("Ingrese que letra quiere usar ""\n1.	X" "\n2.	O\n")
if (respuesta1== "1"):
	print ("Has seleccionado X!\n")
	respuesta2=input("Ingrese que posicion quiere utilizar ""\n_|_|_\n_|_|_\n_|_|_\nSabiendo que va desde el numero 0 hasta el 8\n")
	if (respuesta2 == "0"):
		print ("\nX|_|_\n_|_|_\n_|_|_\n")
		
		respuesta3=input("Ingrese que posicion quiere utilizar ""\nX|_|_\n_|_|_\n_|_|_\nSabiendo que va desde el numero 0 hasta el 8\n")
		if (respuesta3 == "1"):
			print ("\nX|X|_\n_|_|_\n_|_|_\n")
		if (respuesta3 == "2"):
			print ("\nX|_|X\n_|_|_\n_|_|_\n")
		if (respuesta3 == "3"):
			print ("\nX|_|_\nX|_|_\n_|_|_\n")
		if (respuesta3 == "4"):
			print ("\nX|_|_\n_|X|_\n_|_|_\n")
		if (respuesta3 == "5"):
			print ("\nX|_|_\n_|_|X\n_|_|_\n")
		if (respuesta3 == "6"):
			print ("\nX|_|_\n_|_|_\nX|_|_\n")
		if (respuesta3 == "7"):
			print ("\nX|_|_\n_|_|_\n_|X|_\n")
		if (respuesta3 == "8"):
			print ("\nX|_|_\n_|_|_\n_|_|X\n")
		
	if (respuesta2 == "1"):
		print ("\n_|X|_\n_|_|_\n_|_|_\n")
		
		respuesta3=input("Ingrese que posicion quiere utilizar ""\n_|X|_\n_|_|_\n_|_|_\nSabiendo que va desde el numero 0 hasta el 8\n")
		if (respuesta3 == "0"):
			print ("\nX|x|_\n_|_|_\n_|_|_\n")
		if (respuesta3 == "2"):
			print ("\n_|X|X\n_|_|_\n_|_|_\n")
		if (respuesta3 == "3"):
			print ("\n_|X|_\nX|_|_\n_|_|_\n")
		if (respuesta3 == "4"):
			print ("\n_|X|_\n_|X|_\n_|_|_\n")
		if (respuesta3 == "5"):
			print ("\n_|X|_\n_|_|X\n_|_|_\n")
		if (respuesta3 == "6"):
			print ("\n_|X|_\n_|_|_\nX|_|_\n")
		if (respuesta3 == "7"):
			print ("\n_|X|_\n_|_|_\n_|X|_\n")
		if (respuesta3 == "8"):
			print ("\n_|X|_\n_|_|_\n_|_|X\n")
		
	if (respuesta2 == "2"):
		print ("\n_|_|X\n_|_|_\n_|_|_\n")
	if (respuesta2 == "3"):
		print ("\n_|_|_\nX|_|_\n_|_|_\n")
	if (respuesta2 == "4"):
		print ("\n_|_|_\n_|X|_\n_|_|_\n")
	if (respuesta2 == "5"):
		print ("\n_|_|_\n_|_|X\n_|_|_\n")
	if (respuesta2 == "6"):
		print ("\n_|_|_\n_|_|_\nX|_|_\n")
	if (respuesta2 == "7"):
		print ("\n_|_|_\n_|_|_\n_|X|_\n")
	if (respuesta2 == "8"):
		print ("\n_|_|_\n_|_|_\n_|_|X\n")
		

else:
	print ("Has seleccionado O!\n")
