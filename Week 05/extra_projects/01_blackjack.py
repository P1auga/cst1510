"""Blackjack - the object-oriented version."""

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


class Hand:
    """One player's cards, with the rules that apply to them."""

    def __init__(self):
        """Start with no cards."""
        self.cards = []

    def add_card(self):
        """Deal one card and append it to the hand."""
        self.cards.append(random.choice(cards))

    def score(self):
        """Return the total, with an ace dropping 11 -> 1 to avoid busting."""
        total = sum(self.cards)

        while total > 21 and 11 in self.cards:
            # Downgrade one ace and recheck - a hand can hold two.
            self.cards[self.cards.index(11)] = 1
            total = sum(self.cards)

        return total

    def blackjack(self):
        """Return True for two cards totalling 21."""
        return len(self.cards) == 2 and self.score() == 21


def compare(user_hand, computer_hand):
    """Return the result of the round as a sentence."""
    if user_hand.blackjack():
        return "You have blackjack. You win."
    if computer_hand.blackjack():
        return "The computer has blackjack. You lose."

    user_score = user_hand.score()
    computer_score = computer_hand.score()

    if user_score > 21:
        return "You went over. You lose."
    if computer_score > 21:
        return "The computer went over. You win."
    if user_score == computer_score:
        return "Draw."
    if user_score > computer_score:
        return "You win."
    return "You lose."


def play():
    """Play one round of blackjack."""
    user_hand = Hand()
    computer_hand = Hand()

    for _ in range(2):
        user_hand.add_card()
        computer_hand.add_card()

    playing = True

    while playing:
        print(f"Your cards: {user_hand.cards}, score {user_hand.score()}")
        print(f"Computer's first card: {computer_hand.cards[0]}")

        if user_hand.score() > 21 or user_hand.blackjack():
            playing = False
            continue

        if input("Type 'y' to draw another card, 'n' to pass: ").strip().lower() != "y":
            playing = False

    while computer_hand.score() < 17:
        computer_hand.add_card()

    print(f"\nYour final hand: {user_hand.cards}, score {user_hand.score()}")
    print(f"Computer's final hand: {computer_hand.cards}, score {computer_hand.score()}")
    print(compare(user_hand, computer_hand))


play()
