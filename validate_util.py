
def validateNumeric(number: str, errorText: str, min: int, max: int):
	# isNumeric if float should be allowed
	if not number.isdigit():
			print("Please enter a valid number")
			return False

	number = int(number)
	
	if number < min or number > max:
			print(errorText)
			return False
	
	return True