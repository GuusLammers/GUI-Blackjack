import random
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk


class Card:
    def __init__(self, suit, number, image):
        self.suit = suit
        self.number = number
        self.value = self.card_value()
        self.image = image

    # set card value
    def card_value(self):
        if self.number == "A":
            return 1, 11
        elif self.number == "2":
            return 2
        elif self.number == "3":
            return 3
        elif self.number == "4":
            return 4
        elif self.number == "5":
            return 5
        elif self.number == "6":
            return 6
        elif self.number == "7":
            return 7
        elif self.number == "8":
            return 8
        elif self.number == "9":
            return 9
        elif self.number == "10" or self.number == "J" or self.number == "Q" or self.number == "K":
            return 10


class Deck:
    def __init__(self):
        self.deck = []
        self.suits = ["H", "D", "S", "C"]
        self.card_numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.card_image_names = [["2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AH"],
                                 ["2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AD"],
                                 ["2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AS"],
                                 ["2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AC"]]
        self.directory = "C:/Users/guusl/Documents/Guus/Coding Projects/Black Jack GUI/CardImages/"
        self.create_deck()

    # create deck
    def create_deck(self):
        for suit, image_suit in zip(self.suits, self.card_image_names):
            for card, image in zip(self.card_numbers, image_suit):
                self.deck.append(
                    Card(suit, card, Image.open(self.directory + image + ".png").resize((100, 125), Image.ANTIALIAS)))

    def shuffle_deck(self):
        for i in range(len(self.deck)):
            rand = random.randint(0, 51)
            self.deck[i], self.deck[rand] = self.deck[rand], self.deck[i]

    def deal_card(self):
        return self.deck.pop()


class Player:
    def __init__(self):
        self.hand = []
        self.score = 0

    def get_dealt_card(self, deck):
        self.hand.append(deck.deal_card())

    def check_blackjack(self):
        if self.hand[0].number == "A" and self.hand[1].card_value() == 10 or self.hand[1].number == "A" and self.hand[0].card_value() == 10:
            self.score = 21
            return True

    def compute_score(self):
        self.score = 0
        # ace conditions
        ace_count = 0
        for card in self.hand:
            if card.number == "A":
                ace_count = ace_count + 1
        if ace_count != 0:
            scores = [0] * 2
            if ace_count == 1:
                scores[0], scores[1] = 1, 11
            elif ace_count == 2:
                scores[0], scores[1] = 2, 12
            elif ace_count == 3:
                scores[0], scores[1] = 3, 13
            elif ace_count == 4:
                scores[0], scores[1] = 4, 14
            for card in self.hand:
                if card.number == "A":
                    continue
                else:
                    scores[0], scores[1] = scores[0] + card.card_value(), scores[1] + card.card_value()
            if scores[0] <= 21 and scores[1] <= 21:
                self.score = scores[1]
            elif scores[0] <= 21 and scores[1] > 21:
                self.score = scores[0]
            elif scores[0] > 21 and scores[1] > 21:
                self.score = scores[0]
        # ace conditions
        else:
            for card in self.hand:
                self.score += card.card_value()


class Dealer:
    def __init__(self):
        self.hand = []
        self.score = 0

    def deal_self_card(self, deck):
        self.hand.append(deck.deal_card())

    def check_blackjack(self):
        if self.hand[0].number == "A" and self.hand[1].card_value() == 10 or self.hand[1].number == "A" and self.hand[0].card_value() == 10:
            self.score = 21
            return True

    def compute_score(self):
        self.score = 0
        # ace conditions
        ace_count = 0
        for card in self.hand:
            if card.number == "A":
                ace_count = ace_count + 1
        if ace_count != 0:
            scores = [0] * 2
            if ace_count == 1:
                scores[0], scores[1] = 1, 11
            elif ace_count == 2:
                scores[0], scores[1] = 2, 12
            elif ace_count == 3:
                scores[0], scores[1] = 3, 13
            elif ace_count == 4:
                scores[0], scores[1] = 4, 14
            for card in self.hand:
                if card.number == "A":
                    continue
                else:
                    scores[0], scores[1] = scores[0] + card.card_value(), scores[1] + card.card_value()
            if scores[0] <= 21 and scores[1] <= 21:
                self.score = scores[1]
            elif scores[0] <= 21 and scores[1] > 21:
                self.score = scores[0]
            elif scores[0] > 21 and scores[1] > 21:
                self.score = scores[0]
        # ace conditions
        else:
            for card in self.hand:
                self.score += card.card_value()


class GUI:
    def __init__(self):
        self.card_deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.main_frame = Frame(bg="blue")
        self.images = {}
        self.card_back_image = ImageTk.PhotoImage(
            Image.open(self.card_deck.directory + "YB.png").resize((100, 125), Image.ANTIALIAS))
        self.open_images()
        self.myFont = font.Font(family='Helvetica', size=40, weight='bold')

        # main frame
        table = Frame(self.main_frame, bg="#32a852")
        table.place(relx=0, rely=0, relwidth=1, relheight=1)

# -------------------------------------------------home screen----------------------------------------------------------

        # home screen labels
        self.main_label = Label(table, text="Welcome to Casino BlackJack", bg="#32a852", fg="#fdcd44", font=self.myFont)
        self.main_label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.3)

        # home screen buttons
        self.button_play = Button(table, text="Play", bg="#fdcd44", command=self.menu_to_table)
        self.button_exit = Button(table, text="Exit", bg="#fdcd44", command=root.destroy)
        self.button_play.place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.2)
        self.button_exit.place(relx=0.45, rely=0.65, relwidth=0.1, relheight=0.1)

# -------------------------------------------------home screen----------------------------------------------------------

# ----------------------------------------------------table-------------------------------------------------------------

        # labels for player and dealer
        self.dealer_label = Label(table, text="Dealer's Hand", bg="#32a852", fg="#fdcd44", font=self.myFont)
        self.player_label = Label(table, text="Player's Hand", bg="#32a852", fg="#fdcd44", font=self.myFont)

        # table buttons
        self.main_menu = Button(table, text="Main Menu", bg="#fdcd44", command=self.table_to_menu)
        self.start = Button(table, text="Deal", bg="#fdcd44", command=self.deal_first_2)

        self.card_deck.shuffle_deck()

        # player card labels
        self.pcard1_label = Label(table)
        self.pcard2_label = Label(table)
        self.pcard3_label = Label(table)
        self.pcard4_label = Label(table)
        self.pcard5_label = Label(table)

        # dealer card labels
        self.dcard1_label = Label(table)
        self.dcard2_label = Label(table)
        self.dcard3_label = Label(table)
        self.dcard4_label = Label(table)
        self.dcard5_label = Label(table)

        # blackjack labels
        self.player_bj_label = Label(table, text="BlackJack", bg="#32a852", fg="#850000", font=self.myFont)
        self.dealer_bj_label = Label(table, text="BlackJack", bg="#32a852", fg="#850000", font=self.myFont)

        # winner label
        self.player_wins_label = Label(table, text="Player Wins", bg="#32a852", fg="#850000", font=self.myFont)
        self.dealer_wins_label = Label(table, text="Dealer Wins", bg="#32a852", fg="#850000", font=self.myFont)
        self.tie_label = Label(table, text="Tie", bg="#32a852", fg="#850000", font=self.myFont)
        self.bust_label = Label(table, text="Bust", bg="#32a852", fg="#850000", font=self.myFont)

        # hit or don't hit button
        self.hit_button = Button(table, text="Hit", bg="#fdcd44", command=self.hit)
        self.stand_button = Button(table, text="Stand", bg="#fdcd44", command=self.stand)

        # game over buttons
        self.play_again_button = Button(table, text="Play Again", bg="#fdcd44", command=self.play_again)

# ----------------------------------------------------table-------------------------------------------------------------

    # opens all images and stores them in a dictionary where the key is the cards value followed by its suit ex(2H, 10S)
    def open_images(self):
        for card in self.card_deck.deck:
            self.images[card.number + card.suit] = (ImageTk.PhotoImage(card.image))
        self.images["B"] = self.card_back_image

    # loads the table after play is clicked
    def menu_to_table(self):
        # forget main menu widgets
        self.button_play.place_forget()
        self.button_exit.place_forget()
        self.main_label.place_forget()

        # place table widgets
        self.dealer_label.place(relx=0.3, rely=0.05, relwidth=0.4, relheight=0.1)
        self.player_label.place(relx=0.3, rely=0.85, relwidth=0.4, relheight=0.1)
        self.main_menu.place(relx=0.05, rely=0.9, relwidth=0.05, relheight=0.05)
        self.start.place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.2)

    # loads the menu after Main Menu is clicked
    def table_to_menu(self):
        # forget table widgets
        self.dealer_label.place_forget()
        self.player_label.place_forget()
        self.main_menu.place_forget()
        self.start.place_forget()
        self.pcard1_label.place_forget()
        self.pcard2_label.place_forget()
        self.pcard3_label.place_forget()
        self.pcard4_label.place_forget()
        self.pcard5_label.place_forget()
        self.dcard1_label.place_forget()
        self.dcard2_label.place_forget()
        self.dcard3_label.place_forget()
        self.dcard4_label.place_forget()
        self.dcard5_label.place_forget()
        self.player_bj_label.place_forget()
        self.dealer_bj_label.place_forget()
        self.player_wins_label.place_forget()
        self.dealer_wins_label.place_forget()
        self.tie_label.place_forget()
        self.bust_label.place_forget()
        self.hit_button.place_forget()
        self.stand_button.place_forget()
        self.play_again_button.place_forget()

        # place menu widgets
        self.main_label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.3)
        self.button_play.place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.2)
        self.button_exit.place(relx=0.45, rely=0.65, relwidth=0.1, relheight=0.1)

        # reset deck, player, and dealer
        self.card_deck = Deck()
        self.card_deck.shuffle_deck()
        self.player = Player()
        self.dealer = Dealer()

    # deal first two cards and place them on table
    def deal_first_2(self):
        # forget deal button
        self.start.place_forget()

        # deal player first card
        self.player.get_dealt_card(self.card_deck)
        self.pcard1_label.config(image=self.images[self.player.hand[0].number + self.player.hand[0].suit])
        self.pcard1_label.place(relx=0.42, rely=0.65, relwidth=0.065, relheight=0.165)

        # deal dealer first card
        self.dealer.deal_self_card(self.card_deck)
        self.dcard1_label.config(image=self.images[self.dealer.hand[0].number + self.dealer.hand[0].suit])
        self.dcard1_label.place(relx=0.42, rely=0.2, relwidth=0.065, relheight=0.165)

        # deal player second card
        self.player.get_dealt_card(self.card_deck)
        self.pcard2_label.config(image=self.images[self.player.hand[1].number + self.player.hand[1].suit])
        self.pcard2_label.place(relx=0.52, rely=0.65, relwidth=0.065, relheight=0.165)

        # deal dealer second card face down
        self.dealer.deal_self_card(self.card_deck)
        self.dcard2_label.config(image=self.images["B"])
        self.dcard2_label.place(relx=0.52, rely=0.2, relwidth=0.065, relheight=0.165)

        # check blackjack player and dealer
        if self.player.check_blackjack():
            if self.dealer.check_blackjack():
                self.dcard2_label.config(image=self.images[self.dealer.hand[1].number + self.dealer.hand[1].suit])
                self.tie_label.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.2)
                self.play_again_button.place(relx=0.7, rely=0.45, relwidth=0.1, relheight=0.1)
                # blackjack labels
                self.player_bj_label.place(relx=0.725, rely=0.7, relwidth=0.175, relheight=0.1)
                self.dealer_bj_label.place(relx=0.3725, rely=0.23, relwidth=0.175, relheight=0.1)

            else:
                self.dcard2_label.config(image=self.images[self.dealer.hand[1].number + self.dealer.hand[1].suit])
                self.player_wins_label.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.2)
                self.play_again_button.place(relx=0.7, rely=0.45, relwidth=0.1, relheight=0.1)
                # blackjack labels
                self.player_bj_label.place(relx=0.725, rely=0.7, relwidth=0.175, relheight=0.1)
        else:
            self.hit_button.place(relx=0.35, rely=0.45, relwidth=0.1, relheight=0.1)
            self.stand_button.place(relx=0.55, rely=0.45, relwidth=0.1, relheight=0.1)

    # hit
    def hit(self):
        self.player.get_dealt_card(self.card_deck)

        # display new card
        if len(self.player.hand) == 3:
            # forget current player card widgets
            self.pcard1_label.place_forget()
            self.pcard2_label.place_forget()
            # configure pcard3
            self.pcard3_label.config(image=self.images[self.player.hand[2].number + self.player.hand[2].suit])
            # place player card widgets
            self.pcard1_label.place(relx=0.3775, rely=0.65, relwidth=0.065, relheight=0.165)
            self.pcard2_label.place(relx=0.4675, rely=0.65, relwidth=0.065, relheight=0.165)
            self.pcard3_label.place(relx=0.5575, rely=0.65, relwidth=0.065, relheight=0.165)
            # compute players score
            self.player.compute_score()
            # check if player busted
            if self.player.score > 21:
                # forget buttons
                self.hit_button.place_forget()
                self.stand_button.place_forget()
                # display winner
                self.dcard2_label.config(image=self.images[self.dealer.hand[1].number + self.dealer.hand[1].suit])
                self.dealer_wins_label.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.2)
                self.bust_label.place(relx=0.725, rely=0.7, relwidth=0.1, relheight=0.1)
                self.play_again_button.place(relx=0.7, rely=0.45, relwidth=0.1, relheight=0.1)
            # checks if player has blackjack
            elif self.player.score == 21:
                # forget buttons
                self.hit_button.place_forget()
                self.stand_button.place_forget()
                # display blackjack label
                self.player_bj_label.place(relx=0.725, rely=0.7, relwidth=0.175, relheight=0.1)
                # deal dealer
                self.stand()

        elif len(self.player.hand) == 4:
            # forget current player card widgets
            self.pcard1_label.place_forget()
            self.pcard2_label.place_forget()
            self.pcard3_label.place_forget()
            # configure pcard3
            self.pcard4_label.config(image=self.images[self.player.hand[3].number + self.player.hand[3].suit])
            # place player card widgets
            self.pcard1_label.place(relx=0.3325, rely=0.65, relwidth=0.065, relheight=0.165)
            self.pcard2_label.place(relx=0.4225, rely=0.65, relwidth=0.065, relheight=0.165)
            self.pcard3_label.place(relx=0.5125, rely=0.65, relwidth=0.065, relheight=0.165)
            self.pcard4_label.place(relx=0.6025, rely=0.65, relwidth=0.065, relheight=0.165)
            # compute players score
            self.player.compute_score()
            # check if player busted
            if self.player.score > 21:
                # forget buttons
                self.hit_button.place_forget()
                self.stand_button.place_forget()
                # display winner
                self.dcard2_label.config(image=self.images[self.dealer.hand[1].number + self.dealer.hand[1].suit])
                self.dealer_wins_label.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.2)
                self.bust_label.place(relx=0.725, rely=0.7, relwidth=0.1, relheight=0.1)
                self.play_again_button.place(relx=0.7, rely=0.45, relwidth=0.1, relheight=0.1)
            # checks if player has blackjack
            elif self.player.score == 21:
                # forget buttons
                self.hit_button.place_forget()
                self.stand_button.place_forget()
                # display blackjack label
                self.player_bj_label.place(relx=0.725, rely=0.7, relwidth=0.175, relheight=0.1)
                # deal dealer
                self.stand()
        else:
            # forget current player card widgets
            self.pcard1_label.place_forget()
            self.pcard2_label.place_forget()
            self.pcard3_label.place_forget()
            self.pcard4_label.place_forget()
            # configure pcard3
            self.pcard5_label.config(image=self.images[self.player.hand[4].number + self.player.hand[4].suit])
            # place player card widgets
            self.pcard1_label.place(relx=0.2875, rely=0.65, relwidth=0.065, relheight=0.165)
            self.pcard2_label.place(relx=0.3775, rely=0.65, relwidth=0.065, relheight=0.165)
            self.pcard3_label.place(relx=0.4675, rely=0.65, relwidth=0.065, relheight=0.165)
            self.pcard4_label.place(relx=0.5575, rely=0.65, relwidth=0.065, relheight=0.165)
            self.pcard5_label.place(relx=0.6475, rely=0.65, relwidth=0.065, relheight=0.165)
            # compute players score
            self.player.compute_score()
            # check if player busted
            if self.player.score > 21:
                # forget buttons
                self.hit_button.place_forget()
                self.stand_button.place_forget()
                # display winner
                self.dcard2_label.config(image=self.images[self.dealer.hand[1].number + self.dealer.hand[1].suit])
                self.dealer_wins_label.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.2)
                self.bust_label.place(relx=0.725, rely=0.7, relwidth=0.1, relheight=0.1)
                self.play_again_button.place(relx=0.7, rely=0.45, relwidth=0.1, relheight=0.1)
            # checks if player has blackjack
            elif self.player.score == 21:
                # forget buttons
                self.hit_button.place_forget()
                self.stand_button.place_forget()
                # display blackjack label
                self.player_bj_label.place(relx=0.725, rely=0.7, relwidth=0.175, relheight=0.1)
                # deal dealer
                self.stand()

    # stand
    def stand(self):
        # remove hit and stand labels
        self.hit_button.place_forget()
        self.stand_button.place_forget()

        # dealer takes cards until score greater then 17 or bust
        while self.dealer.score < 17:
            self.dealer.deal_self_card(self.card_deck)
            self.dealer.compute_score()

        # check how many cards the dealer has and display them on the screen
        if len(self.dealer.hand) == 2:
            self.dcard2_label.config(image=self.images[self.dealer.hand[1].number + self.dealer.hand[1].suit])
        elif len(self.dealer.hand) == 3:
            # forget current dealer card widgets
            self.dcard1_label.place_forget()
            self.dcard2_label.place_forget()
            # configure dcard2 and dcard3
            self.dcard2_label.config(image=self.images[self.dealer.hand[1].number + self.dealer.hand[1].suit])
            self.dcard3_label.config(image=self.images[self.dealer.hand[2].number + self.dealer.hand[2].suit])
            # place player card widgets
            self.dcard1_label.place(relx=0.3775, rely=0.2, relwidth=0.065, relheight=0.165)
            self.dcard2_label.place(relx=0.4675, rely=0.2, relwidth=0.065, relheight=0.165)
            self.dcard3_label.place(relx=0.5575, rely=0.2, relwidth=0.065, relheight=0.165)
        elif len(self.dealer.hand) == 4:
            # forget current dealer card widgets
            self.dcard1_label.place_forget()
            self.dcard2_label.place_forget()
            # configure dcard2, dcard3 and dcard4
            self.dcard2_label.config(image=self.images[self.dealer.hand[1].number + self.dealer.hand[1].suit])
            self.dcard3_label.config(image=self.images[self.dealer.hand[2].number + self.dealer.hand[2].suit])
            self.dcard4_label.config(image=self.images[self.dealer.hand[3].number + self.dealer.hand[3].suit])
            # place dealer card widgets
            self.dcard1_label.place(relx=0.3325, rely=0.2, relwidth=0.065, relheight=0.165)
            self.dcard2_label.place(relx=0.4225, rely=0.2, relwidth=0.065, relheight=0.165)
            self.dcard3_label.place(relx=0.5125, rely=0.2, relwidth=0.065, relheight=0.165)
            self.dcard4_label.place(relx=0.6025, rely=0.2, relwidth=0.065, relheight=0.165)
        elif len(self.dealer.hand) == 5:
            # forget current player card widgets
            self.dcard1_label.place_forget()
            self.dcard2_label.place_forget()
            # configure dcard2, dcard3, dcard4, and dcard5
            self.dcard2_label.config(image=self.images[self.dealer.hand[1].number + self.dealer.hand[1].suit])
            self.dcard3_label.config(image=self.images[self.dealer.hand[2].number + self.dealer.hand[2].suit])
            self.dcard4_label.config(image=self.images[self.dealer.hand[3].number + self.dealer.hand[3].suit])
            self.dcard5_label.config(image=self.images[self.dealer.hand[4].number + self.dealer.hand[4].suit])
            # place player card widgets
            self.dcard1_label.place(relx=0.2875, rely=0.2, relwidth=0.065, relheight=0.165)
            self.dcard2_label.place(relx=0.3775, rely=0.2, relwidth=0.065, relheight=0.165)
            self.dcard3_label.place(relx=0.4675, rely=0.2, relwidth=0.065, relheight=0.165)
            self.dcard4_label.place(relx=0.5575, rely=0.2, relwidth=0.065, relheight=0.165)
            self.dcard5_label.place(relx=0.6475, rely=0.2, relwidth=0.065, relheight=0.165)

        # check if dealer busted
        if self.dealer.score > 21:
            self.player_wins_label.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.2)
            self.bust_label.place(relx=0.725, rely=0.23, relwidth=0.1, relheight=0.1)
            self.play_again_button.place(relx=0.7, rely=0.45, relwidth=0.1, relheight=0.1)
        # check black jacks
        elif self.dealer.score == 21:
            if self.player.score == 21:
                self.tie_label.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.2)
                self.play_again_button.place(relx=0.7, rely=0.45, relwidth=0.1, relheight=0.1)
                # blackjack labels
                self.dealer_bj_label.place(relx=0.725, rely=0.2, relwidth=0.175, relheight=0.1)
            else:
                self.dealer_wins_label.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.2)
                self.play_again_button.place(relx=0.7, rely=0.45, relwidth=0.1, relheight=0.1)
                # blackjack labels
                self.dealer_bj_label.place(relx=0.725, rely=0.2, relwidth=0.175, relheight=0.1)
        # dealer wins
        elif self.dealer.score > self.player.score:
            self.dealer_wins_label.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.2)
            self.play_again_button.place(relx=0.7, rely=0.45, relwidth=0.1, relheight=0.1)
        # player wins
        elif self.dealer.score < self.player.score:
            self.player_wins_label.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.2)
            self.play_again_button.place(relx=0.7, rely=0.45, relwidth=0.1, relheight=0.1)
        # tie
        else:
            self.tie_label.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.2)
            self.play_again_button.place(relx=0.7, rely=0.45, relwidth=0.1, relheight=0.1)

    # play again
    def play_again(self):
        # remove all widgets on table
        self.pcard1_label.place_forget()
        self.pcard2_label.place_forget()
        self.pcard3_label.place_forget()
        self.pcard4_label.place_forget()
        self.pcard5_label.place_forget()
        self.dcard1_label.place_forget()
        self.dcard2_label.place_forget()
        self.dcard3_label.place_forget()
        self.dcard4_label.place_forget()
        self.dcard5_label.place_forget()
        self.player_bj_label.place_forget()
        self.dealer_bj_label.place_forget()
        self.player_wins_label.place_forget()
        self.dealer_wins_label.place_forget()
        self.tie_label.place_forget()
        self.bust_label.place_forget()
        self.hit_button.place_forget()
        self.stand_button.place_forget()
        self.play_again_button.place_forget()

        # place game starting widgets
        self.start.place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.2)

        # reset card deck, player, and dealer
        self.card_deck = Deck()
        self.card_deck.shuffle_deck()
        self.player = Player()
        self.dealer = Dealer()


root = Tk()
root.geometry("1500x750")
root.title("BlackJack")
root.resizable(0, 0)
main = GUI()
main.main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
root.mainloop()
