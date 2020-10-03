import random

#A trading game based on a real-life simulation used to coach new  traders

starting_purse = 1000
purse = 0
purse += starting_purse

marbles = []
marbles.extend(["red"]*4)
marbles.extend(["green"]*6)
# print(marbles)

red = marbles.count("red")
green = marbles.count("green")

#function to shuffle up marbles
def shuffle_bag(marbles):
    random.shuffle(marbles)
    return marbles

#function to ask for how many rounds to play
def rounds_to_play():
    while True:        
        try:
            total_rounds = int(input("How many round to play? (up to 9)\n")) 
        except ValueError:
            print("This is not a valid number")
            continue
        if (total_rounds > 0 and total_rounds < 10):
            break 
        return total_rounds

#printing the rules for the user
def print_rules():
    print("""
    Bet before each round.
    Each time a coloured marble is drawn and removed from the bag.
    If you draw a green marble, you win the amount bet.
    If you draw a red marble you lose the amount bet.
    The game will end when either rounds are up, or your purse is less than £500.
    """)

#checking purse and green and red left
def check_status():
    print(f"Purse: £{purse}.")
    print(f"Reds: {red}, Green: {green}")

#ask user to place a bet
