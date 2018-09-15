while True:
	print("Welcome to Simple calculator")
	print("Your options are: add (a), subtract (sub), multiply (mult), divide (div), quit (q)")
	user = raw_input(":")
	
	if user	== "q":
		break
	
	elif user == "add":
		num1 = float(raw_input("Enter any number: "))
		num2 = float(raw_input("Enter another number: "))
		result = str(num1 + num2)

		print("The answer is: " + result)
		print("Congrats")

	elif user == "subtract":
		num1 = float(raw_input("Enter any number: "))
		num2 = float(raw_input("Enter another number: "))
		result = str(num1 - num2)

		print("The answer is: " + result)
		print("Congrats")

	elif user == "divide":
		num1 = float(raw_input("Enter any number: "))
		num2 = float(raw_input("Enter another number: "))
		result = str(num1 / num2)

		print("The answer is: " + result)
		print("Congrats")

	elif user == "multiply":
		num1 = float(raw_input("Enter any number: "))
		num2 = float(raw_input("Enter another number: "))
		result = str(num1 * num2)

		print("The answer is: " + result)
		print("Congrats")

	#end here 