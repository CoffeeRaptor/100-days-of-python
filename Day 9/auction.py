print("""
                __________
               |          |
               |  AUCTION |
               |__________|
                     ||
                    (||)
                   ( || )
                   / || \\
                 _/  ||  \\_
                /    ||    \\
               /     ||     \\
              |______||______|
                   _/  \\_
                  |      |
                  |      |
                  |      |
                  |______|
                 /________\\
""")

bidding = True
bidders = {}

while bidding:
    name = input("What's your name?\n")

    while True:
        try:
            price = int(input("What's your bidding price?\n"))
            break
        except ValueError:
            print("Please enter a valid number for your bid.")

    bidders[name] = price
    print("Current bids:", bidders)

    while True:
        continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
        if continue_bidding == "yes":
            bidding = True
            break
        elif continue_bidding == "no":
            bidding = False
            break
        else:
            print("Invalid input. Only type 'yes' or 'no'.")

def bid_winner_calculate(bidders):
    highest_bidder = ""
    highest_bid = 0

    for bidder, bid in bidders.items():
        if bid > highest_bid:
            highest_bid = bid
            highest_bidder = bidder

    print(f"\nThe highest bidder is {highest_bidder} with a bid of ${highest_bid}.")

bid_winner_calculate(bidders)