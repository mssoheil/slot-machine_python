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

def validateBetAmount(bet: str):
	isValidNumber = validateNumeric(bet, f"Bet should be between {MIN_BET}-{MAX_BET}", MIN_BET, MAX_BET)

	if not isValidNumber:
		return False
	
	return True
	

def validateNumberOfLines(numberOfLines: str):
	isValidNumber = validateNumeric(numberOfLines, f"Number of lines should be between {MIN_LINES}-{MAX_LINES}", MIN_LINES, MAX_LINES)

	if not isValidNumber:
		return False
	
	numberOfLines = int(numberOfLines)

	return True

def deposit():
	while True:
		amount = input("Enter your deposit amount? $")

		isAmountValid = validateDepositAmount(amount)

		if not isAmountValid:
			continue

		break

	return int(amount)

def getNumberOfLines():
	while True:
		numberOfLines = input(f"Enter the number of lines you want to bet on ({MIN_LINES}-{MAX_LINES})? ")

		isNumberOfLineValid = validateNumberOfLines(numberOfLines)

		if not isNumberOfLineValid:
			continue

		break

	return int(numberOfLines)

def getBet():
	while True:
		betAmount = input(f"Enter the amount you want to bet on each line ({MIN_BET}-{MAX_BET})? ")

		isBetAmountValid = validateBetAmount(betAmount)

		if not isBetAmountValid:
			continue

		break

	return int(betAmount)


def main():
	balance = deposit()
	lines = getNumberOfLines()
	bet = getBet()

	totalBet = bet * lines

	print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${totalBet}")

if __name__ == "__main__":
	main()




