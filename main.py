import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLUMNS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_wins(columns, lines, bet, values):
    wins = 0
    win_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol_to_check != symbol:
                break

        else:
            wins += values[symbol]*bet
            win_lines.append(line+1)

    return wins, win_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("How much do you want to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Deposit amount must be greater than 0.")
                continue
        else:
            print("Please enter the amount you wish to deposit.")
            continue

    return amount


def get_no_of_lines():
    while True:
        lines = input(f"Enter the no of lines to bet on (1-{str(MAX_LINES)})?: ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid no of lines to bet on.")
        else:
            print("Please enter the no of lines.")

    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Deposit amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter the amount you wish to bet.")

    return amount


def game_spin(balance):
    lines = get_no_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not enough balance to bet! Your current balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Your total bet is ${total_bet}")

    slots = get_slot_machine_spin(rows=ROWS, cols=COLUMNS, symbols=symbol_count)
    print_slot_machine(slots)
    win, win_line = check_wins(slots, lines, bet, symbol_values)
    print(f"You have won ${win}.")
    print("You won on lines:", *win_line)
    return win - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}.")
        spin = input("Press enter to play (q to quit):")
        if spin == "q":
            break
        balance += game_spin(balance)

    print(f"You won a total of ${balance}")


if __name__ == "__main__":
    main()
