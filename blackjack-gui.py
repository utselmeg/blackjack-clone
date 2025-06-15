import random
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

# drawn cards
card_refs = []
def draw_random_card():
    suit = random.choice(SUIT_ORDER)
    rank = random.choice(RANK_ORDER)
    return get_card_image(suit, rank)

def deal():
    # print("deal button")
    canvas.delete("all")
    card_refs.clear()
    canvas.create_text(400, 50, text="deal button", font=("Helvetica", 20), fill="white")
    for i in range(2):
        card_img = draw_random_card()
        card_refs.append(card_img)
        canvas.create_image(100 + i * (CARD_WIDTH + 10), 150, image=card_img, anchor='nw')

def hit():
    # print("hit")
    card_img = draw_random_card()
    card_refs.append(card_img)
    canvas.create_image(100 + len(card_refs) * (CARD_WIDTH + 10), 150, image=card_img, anchor='nw')

def stand():
    # print("stand")
    canvas.create_text(400, 300, text="stand button", font=("Helvetica", 16), fill="yellow")

button_frame = tk.Frame(root)
button_frame.pack(pady=10)
tk.Button(button_frame, text="Deal", command=deal, font=("Helvetica", 14)).pack(side='left', padx=10)
tk.Button(button_frame, text="Hit", command=hit, font=("Helvetica", 14)).pack(side='left', padx=10)
tk.Button(button_frame, text="Stand", command=stand, font=("Helvetica", 14)).pack(side='left', padx=10)

root.mainloop()
