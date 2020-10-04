import random

#A trading game based on a real-life simulation used to coach new traders

starting_purse = 1000
purse = 0
purse += starting_purse
current_round = 0

marbles = []
marbles.extend(["red"]*4)
marbles.extend(["green"]*6)

#function to shuffle up marbles
def shuffle_bag():
    global marbles
    random.shuffle(marbles)
    return marbles

#function to ask for how many rounds to play
def rounds_to_play():
    while True:        
        try:
            total_rounds = int(input("How many rounds to play? (3 to 8)\n")) 
        except ValueError:
            print("This is not a valid number")
            continue
        if (total_rounds >= 3 and total_rounds < 9):
            break 
    return total_rounds

#printing the rules for the user
def print_rules():
    print("""
    Bet before each round.
    Each time a coloured marble is drawn and removed from the bag.
    If you draw a green marble, you win the amount bet.
    If you draw a red marble you lose the amount bet.
    The game will end when either rounds are up, there are no more green marbles or your purse is less than £500.
    """)

#checking purse and green and red left
def check_status():
    red = marbles.count("red")
    green = marbles.count("green")
    print(f"\nRound: {current_round}")
    print(f"Purse: £{purse}.")
    print(f"Reds: {red}, Green: {green}")

#ask user to place a bet
def ask_user_bet():
    while True:
        try: 
            round_bet = int(input("How much would you like to bet:\t"))
        except ValueError:
            print(f"This is not a valid input")
            continue
        if purse < round_bet:
            print(f"Try again, money in purse: £{purse}")
        elif round_bet < 1:
            print("Bets must be £1 or more")
        else: 
            return round_bet

#function for draw and consequences
def draw_marble(round_bet):
    global marbles, purse
    drawn_marble = marbles.pop()
    if drawn_marble == 'green':
        purse += round_bet
        print(f"Green marble drawn. You won {round_bet}!")
    elif drawn_marble == 'red':
        purse -= round_bet
        print(f"Red marble drawn. Bad luck, you lost {round_bet}!")
    return marbles, purse

#game while loop
#to check if game over (current round == totals rounds)
# or purse < 0.5 * starting purse

print_rules()
shuffle_bag()
total_rounds = rounds_to_play()

while current_round < total_rounds and (purse > (0.5 * starting_purse)) and 'green' in marbles:
    current_round += 1
    check_status()
    round_bet = ask_user_bet()
    draw_marble(round_bet)

if not(purse > (0.5 * starting_purse)):
    print(f"You lost. Your current purse is £{purse}. Less than half of starting purse (£{starting_purse})")
else:
    print(f"You won! Your current purse is {purse}")
    percentage_win = (purse / starting_purse) * 100
    print(f"Your ending percentage is: {round(percentage_win)}%")

    

