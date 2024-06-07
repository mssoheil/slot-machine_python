import random
from validations import (
    MAX_BET,
    MIN_BET,
    MAX_LINES,
    MIN_LINES,
    validateBetAmount,
    validateDepositAmount,
    validateNumberOfLines,
)

ROWS = 3
COLS = 3

SYMBOL_COUNT = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

SYMBOL_VALUE = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def getAllSymbols(symbols: dict[str, int]):
    allSymbols: list[str] = []

    for symbol, symbolCount in symbols.items():
        for _ in range(symbolCount):
            allSymbols.append(symbol)

    return allSymbols

def getColumns(cols: int, rows: int, allSymbols: list[str]):
    """Creating symbols for each column of each rows of slot machine"""
    columns: list[list[str]] = []

    for _ in range(cols):
        column: list[str] = []
        currentSymbols = allSymbols[:]
        for _ in range(rows):
            value = random.choice(currentSymbols)
            currentSymbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def checkWinnings(
    columns: list[list[str]], lines: int, bet: int, values: dict[str, int]
):
    winnings = 0
    winningLines: list[int] = []
    for line in range(lines):
        # all of the row symbols should be equal to the first column of that row symbol
        symbol = columns[0][line]

        for column in columns:
            symbolToCheck = column[line]
            if symbol != symbolToCheck:
                break
        else:
            winnings += values[symbol] * bet
            winningLines.append(line + 1)

    return (winnings, winningLines)

def getSlotMachineSpin(cols: int, rows: int, symbols: dict[str, int]):
    allSymbols = getAllSymbols(symbols)

    columns = getColumns(cols, rows, allSymbols)

    return columns

def printSlotMachine(columns: list[list[str]]):
    # transposing the columns to reverse it to become rows
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):

            print(column[row], end=" | " if i != len(column) - 1 else "")

        print()

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
        numberOfLines = input(
            f"Enter the number of lines you want to bet on ({MIN_LINES}-{MAX_LINES})? "
        )

        isNumberOfLineValid = validateNumberOfLines(numberOfLines)

        if not isNumberOfLineValid:
            continue

        break

    return int(numberOfLines)

def getBet(balance: int, lines: int):
    while True:
        betAmount = input(
            f"Enter the amount you want to bet on each line ({MIN_BET}-{MAX_BET})? "
        )

        isBetAmountValid = validateBetAmount(betAmount, balance, lines)

        if not isBetAmountValid:
            continue

        break

    return int(betAmount)

def spin(balance: int):
    lines = getNumberOfLines()
    bet = getBet(balance, lines)

    totalBet = bet * lines

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${totalBet}"
    )

    slots = getSlotMachineSpin(COLS, ROWS, SYMBOL_COUNT)
    printSlotMachine(slots)

    (winnings, winningLines) = checkWinnings(slots, lines, bet, SYMBOL_VALUE)
    print(f"You won {winnings}.")
    # it's unpack|splat operator which is like spread operator of javascript
    print("You won on lines:", *winningLines)
    return winnings - totalBet

def main():
    balance = deposit()

    while True:
        print(f"Current balance is ${balance}")
        play = input("Press enter to play. (q to quit).")
        if play == "q":
            break

        balance += spin(balance)

    print(f"You left with ${balance}")


if __name__ == "__main__":
    main()
