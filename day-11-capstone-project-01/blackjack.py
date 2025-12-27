import random

def deal_card():
    """Returns a random card from the deck"""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)


def calculate_score(hand):
    """
    Calculates the score of a hand.
    Handles Ace (11 or 1).
    """
    if sum(hand) == 21 and len(hand) == 2:
        return 0  # 0 represents blackjack

    while 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return sum(hand)


def compare(player_score, dealer_score):
    """Compares player and dealer scores and returns result"""
    if player_score == dealer_score:
        return "Draw!"
    elif dealer_score == 0:
        return "Lose, dealer has Blackjack!"
    elif player_score == 0:
        return "Win with a Blackjack!"
    elif player_score > 21:
        return "You went over. You lose!"
    elif dealer_score > 21:
        return "Dealer went over. You win!"
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "You lose!"


def play_blackjack():
    print("🃏 Welcome to Blackjack 🃏")

    player_hand = []
    dealer_hand = []

    # Deal initial cards
    for _ in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

    game_over = False

    # Player's turn
    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f"\nYour cards: {player_hand}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")

        if player_score == 0 or player_score > 21:
            game_over = True
        else:
            choice = input("Type 'hit' to get another card, or 'stand' to pass: ").lower()
            if choice == "hit":
                player_hand.append(deal_card())
            else:
                game_over = True

    # Dealer's turn
    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    # Final results
    print("\n==========================")
    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
    print(compare(player_score, dealer_score))
    print("==========================\n")


# Play again
while input("Do you want to play Blackjack? (y/n): ").lower() == "y":
    play_blackjack()

print("Game over. Thanks for playing Blackjack!")
