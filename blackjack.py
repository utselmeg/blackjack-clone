# Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

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
    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)


class Hand:
    def __init__(self):
        self.cards = [] 
    def __str__(self):
        s = ""
        for i in self.cards:
            s += str(i) + " "
#        return "Hand contains " + s
        return ""   
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
    def draw(self, canvas, pos):
        for c in self.cards:
            pos[0] = pos[0] + 80
            c.draw(canvas, pos)
                    
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
     
def draw(canvas):
    canvas.draw_text("Blackjack", [175, 50], 50, "Red")
    canvas.draw_text("Dealer's hand", [50, 200], 25, "White")
    canvas.draw_text("Player's hand", [50, 380], 25, "White")
    canvas.draw_text(outcome, [230, 160], 20, "Red")
    canvas.draw_text("Score: " + str(score), [450, 370], 25, "Red")
    if in_play == True:
        canvas.draw_text("Will you hit or stand?", [120, 130], 35, "White")
    else:
        canvas.draw_text("Game over! New deal?", [120, 130], 35, "White")
    player_hand.draw(canvas, [-40, 400])
    dealer_hand.draw(canvas, [-38, 220])
    if in_play == True:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (78, 268), (70, 94))

frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

deal()
frame.start()
