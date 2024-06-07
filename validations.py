

MIN_BET = 1
MAX_BET = 100

MAX_LINES = 3
MIN_LINES = 1

MIN_DEPOSIT_AMOUNT = 1
MAX_DEPOSIT_AMOUNT = 1000000

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


def validateDepositAmount(amount: str):
	isValidNumber = validateNumeric(amount, f"Amount should be between {MIN_DEPOSIT_AMOUNT}-{MAX_DEPOSIT_AMOUNT}", MIN_DEPOSIT_AMOUNT, MAX_DEPOSIT_AMOUNT)

	if not isValidNumber:
		return False
	
	return True

def validateBetAmount(bet: str, balance: int, lines: int):
	isValidNumber = validateNumeric(bet, f"Bet should be between {MIN_BET}-{MAX_BET}", MIN_BET, MAX_BET)

	if not isValidNumber:
		return False
	
	totalBet = int(bet) * lines

	if totalBet > balance:
		print(f"You do not have enough to bet that amount,Your total bet is ${totalBet} Your current balance is: ${balance}")
		return False

	
	return True
	

def validateNumberOfLines(numberOfLines: str):
	isValidNumber = validateNumeric(numberOfLines, f"Number of lines should be between {MIN_LINES}-{MAX_LINES}", MIN_LINES, MAX_LINES)

	if not isValidNumber:
		return False
	
	numberOfLines = int(numberOfLines)

	return True