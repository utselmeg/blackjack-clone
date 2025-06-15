import tkinter as tk
from PIL import Image, ImageTk
from blackjack import BlackjackGame

CARD_WIDTH, CARD_HEIGHT = 72, 96
CARD_COLUMNS = 13
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}
sprite_sheet = Image.open("cards_jfitz.png")
card_back = Image.open("card_jfitz_back.png").crop((0, 0, CARD_WIDTH, CARD_HEIGHT))

def get_card_image(card):
    """Function to get a card image"""
    suit = card.get_suit()
    rank = card.get_rank()
    col = RANKS.index(rank)
    row = SUITS.index(suit)
    left = col * CARD_WIDTH
    top = row * CARD_HEIGHT
    cropped = sprite_sheet.crop((left, top, left + CARD_WIDTH, top + CARD_HEIGHT))
    return ImageTk.PhotoImage(cropped)

game = BlackjackGame()
root = tk.Tk()
root.title("Blackjack")
canvas = tk.Canvas(root, width=800, height=600, bg="green")
canvas.pack()

# drawn cards
image_refs = []
def redraw():
    canvas.delete("all")
    image_refs.clear()
    state = game.get_game_state()
    canvas.create_text(400, 30, text=f"Score: {state['score']}", fill="white", font=("Helvetica", 16))
    canvas.create_text(400, 60, text=state['outcome'], fill="yellow", font=("Helvetica", 16))

    # dealer cards
    canvas.create_text(100, 100, text="Dealer", fill="white", anchor="nw", font=("Helvetica", 14))
    for i, card in enumerate(state['dealer_cards']):
        if i == 1 and state['in_play']:
            img = ImageTk.PhotoImage(card_back)
        else:
            img = get_card_image(card)
        image_refs.append(img)
        canvas.create_image(100 + i * (CARD_WIDTH + 10), 130, image=img, anchor='nw')

    # player cards
    canvas.create_text(100, 270, text="Player", fill="white", anchor="nw", font=("Helvetica", 14))
    for i, card in enumerate(state['player_cards']):
        img = get_card_image(card)
        image_refs.append(img)
        canvas.create_image(100 + i * (CARD_WIDTH + 10), 300, image=img, anchor='nw')

# button handlers
def deal():
    # print("deal button")
    game.deal()
    redraw()

def hit():
    # print("hit")
    game.hit()
    redraw()

def stand():
    # print("stand")
    game.stand()
    redraw()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)
tk.Button(button_frame, text="Deal", command=deal, font=("Helvetica", 14)).pack(side='left', padx=10)
tk.Button(button_frame, text="Hit", command=hit, font=("Helvetica", 14)).pack(side='left', padx=10)
tk.Button(button_frame, text="Stand", command=stand, font=("Helvetica", 14)).pack(side='left', padx=10)

root.mainloop()
