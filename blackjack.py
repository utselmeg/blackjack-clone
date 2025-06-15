"""
Blackjack clone game
"""

import random

SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank


class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        s = ""
        for i in self.cards:
            s += str(i) + " "
        return "Hand contains " + s
        # return ""

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        hand_value = 0
        ace = False
        for c in self.cards:
            hand_value += VALUES[c.get_rank()]
            if c.get_rank == 'A':
                ace = True
        if ace == True and (hand_value + 10) <= 21:
            hand_value += 10
        return hand_value

    def get_cards(self):
        return self.cards


class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit ,rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def __str__(self):
        s = ""
        for i in self.cards:
            s += str(i) + " "
        return "Deck contains " + s


class BlackjackGame:
    def __init__(self):
        self.deck = None
        self.player_hand = None
        self.dealer_hand = None
        self.in_play = False
        self.score = 0
        self.outcome = ""

    def deal(self):
        if self.in_play:
            self.score -= 1  # player loses if they abandon round

        self.deck = Deck()
        self.deck.shuffle()

        self.player_hand = Hand()
        self.dealer_hand = Hand()

        self.player_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())

        self.in_play = True
        self.outcome = "Hit or Stand?"

    def hit(self):
        if not self.in_play:
            return

        self.player_hand.add_card(self.deck.deal_card())

        if self.player_hand.get_value() > 21:
            self.in_play = False
            self.outcome = "You have busted!"
            self.score -= 1

    def stand(self):
        if not self.in_play:
            return

        # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
        while self.dealer_hand.get_value() < 17:
            self.dealer_hand.add_card(self.deck.deal_card())

        # TODO: replace with variables
        # player_val = self.player_hand.get_value()
        # dealer_val = self.dealer_hand.get_value()

        if self.dealer_hand.get_value() > 21:
            self.outcome = "Dealer busted! You win!"
            self.score += 1
        elif self.player_hand.get_value() > self.dealer_hand.get_value():
            self.outcome = "You win!"
            self.score += 1
        elif self.player_hand.get_value() < self.dealer_hand.get_value():
            self.outcome = "Dealer wins!"
            self.score -= 1
        else:
            self.outcome = "It's a tie."
        self.in_play = False

    def get_game_state(self):
        return {
            "player_cards": self.player_hand.get_cards(),
            "dealer_cards": self.dealer_hand.get_cards(),
            "in_play": self.in_play,
            "score": self.score,
            "outcome": self.outcome
        }
