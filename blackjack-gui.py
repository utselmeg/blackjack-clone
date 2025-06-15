import tkinter as tk
from PIL import Image, ImageTk
from blackjack import BlackjackGame, Card

CARD_WIDTH, CARD_HEIGHT = 72, 96
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

class BlackjackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack")

        self.canvas = tk.Canvas(root, width=800, height=600, bg="green")
        self.canvas.pack()

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)
        tk.Button(self.button_frame, text="Deal", command=self.on_deal, font=("Helvetica", 14)).pack(side="left", padx=10)
        tk.Button(self.button_frame, text="Hit", command=self.on_hit, font=("Helvetica", 14)).pack(side="left", padx=10)
        tk.Button(self.button_frame, text="Stand", command=self.on_stand, font=("Helvetica", 14)).pack(side="left", padx=10)

        self.sprite_sheet = Image.open("cards_jfitz.png")
        self.card_back = Image.open("card_jfitz_back.png").crop((0, 0, CARD_WIDTH, CARD_HEIGHT))
        self.image_refs = []

        self.game = BlackjackGame()
        self.game.deal()
        self.redraw()

    def get_card_image(self, card: Card):
        """Function to get a card image"""
        suit = card.get_suit()
        rank = card.get_rank()
        col = RANKS.index(rank)
        row = SUITS.index(suit)
        left = col * CARD_WIDTH
        top = row * CARD_HEIGHT
        cropped = self.sprite_sheet.crop((left, top, left + CARD_WIDTH, top + CARD_HEIGHT))
        return ImageTk.PhotoImage(cropped)

    def redraw(self):
        self.canvas.delete("all")
        self.image_refs.clear()
        state = self.game.get_game_state()

        self.canvas.create_text(400, 30, text=f"Score: {state['score']}", fill="white", font=("Helvetica", 16))
        self.canvas.create_text(400, 60, text=state['outcome'], fill="yellow", font=("Helvetica", 16))

        self.canvas.create_text(100, 100, text="Dealer", fill="white", anchor="nw", font=("Helvetica", 14))
        for i, card in enumerate(state['dealer_cards']):
            if i == 1 and state['in_play']:
                img = ImageTk.PhotoImage(self.card_back)
            else:
                img = self.get_card_image(card)
            self.image_refs.append(img)
            self.canvas.create_image(100 + i * (CARD_WIDTH + 10), 130, image=img, anchor='nw')

        self.canvas.create_text(100, 270, text="Player", fill="white", anchor="nw", font=("Helvetica", 14))
        for i, card in enumerate(state['player_cards']):
            img = self.get_card_image(card)
            self.image_refs.append(img)
            self.canvas.create_image(100 + i * (CARD_WIDTH + 10), 300, image=img, anchor='nw')

    def on_deal(self):
        self.game.deal()
        self.redraw()

    def on_hit(self):
        self.game.hit()
        self.redraw()

    def on_stand(self):
        self.game.stand()
        self.redraw()

if __name__ == "__main__":
    root = tk.Tk()
    app = BlackjackGUI(root)
    root.mainloop()
