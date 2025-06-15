import tkinter as tk
from PIL import Image, ImageTk

CARD_WIDTH, CARD_HEIGHT = 72, 96
CARD_COLUMNS = 13
SUIT_ORDER = ['C', 'S', 'H', 'D']
RANK_ORDER = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

sprite_sheet = Image.open("cards_jfitz.png")
card_back_image = Image.open("card_jfitz_back.png").crop((0, 0, CARD_WIDTH, CARD_HEIGHT))

def get_card_image(suit, rank):
    """Function to get a card image"""
    col = RANK_ORDER.index(rank)
    row = SUIT_ORDER.index(suit)
    left = col * CARD_WIDTH
    top = row * CARD_HEIGHT
    card = sprite_sheet.crop((left, top, left + CARD_WIDTH, top + CARD_HEIGHT))
    return ImageTk.PhotoImage(card)

root = tk.Tk()
root.title("Blackjack")
canvas = tk.Canvas(root, width=600, height=400, bg="green")
canvas.pack()

# test
test_card = get_card_image('S', 'A')
canvas.create_image(100, 100, image=test_card, anchor='nw')

def deal():
    print("deal button")
deal_button = tk.Button(root, text="Deal", command=deal, font=("Helvetica", 14))
deal_button.pack(pady=10)

root.mainloop()
