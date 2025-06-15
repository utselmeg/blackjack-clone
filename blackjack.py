# Blackjack

import random

in_play = True
score = 1
outcome = ""

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

def deal():
    global score, outcome, in_play, deck, player_hand, dealer_hand
    if in_play == True:
        score -= 1    
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    deck.shuffle()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())  
    in_play = True

def hit():
    global dealer_hand, player_hand, in_play, score, outcome
    if in_play == True:
    # if the hand is in play, hit the player
        if player_hand.get_value() <= 21:
            player_hand.add_card(deck.deal_card())
    # if busted, assign a message to outcome, update in_play and score
            if player_hand.get_value() > 21:
                outcome = "You busted! Dealer wins!"
                score -= 1
                in_play = False

def stand():
    global player_hand, dealer_hand, score, in_play, outcome
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play == True:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
    if dealer_hand.get_value() > 21:
        outcome = "Dealer busted! You win!"
        score += 1 
    elif player_hand.get_value() > dealer_hand.get_value():
        outcome = "You win!"
        score += 1
    elif player_hand.get_value() <= dealer_hand.get_value():
        outcome = "Dealer wins!"
        score -= 1
    in_play = False   

deal()
