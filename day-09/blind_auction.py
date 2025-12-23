bids = {}
next_bidder = True
highest_bidder = ""
highest_bid = 0

while next_bidder:
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║                WELCOME TO THE BLIND AUCTION                ║
    ╚════════════════════════════════════════════════════════════╝
    """)
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    next_person = input("Are there any other bidders?: Type 'yes' or 'no': ").lower()
    print("\n"*100)             # A simple way of clearing the screen for the next bidder

    if (next_person == "no"):
        next_bidder = False

    bids[name] = bid

    for bidder, bid in bids.items():
        if bid > highest_bid:
            highest_bid = bid
            highest_bidder = bidder

print(f"The winner of the bid is {highest_bidder} with a bid of ${highest_bid}.")

