import random

class Card:
    def __init__(self, suit, number, ):
        self.suit = suit
        self.number = number

    def show_card(self):
        print("{} of {}".format(self. number, self.suit))

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
        self.suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.card_numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.card_images = []
        self.create_deck()

    def create_deck(self):
        for suit in self.suits:
            for card in self.card_numbers:
                self.deck.append(Card(suit, card))

    def show_deck(self):
        for card in self.deck:
            card.show_card()

    def shuffle_deck(self):
        for i in range(len(self.deck)):
            rand = random.randint(0, 51)
            self.deck[i], self.deck[rand] = self.deck[rand], self.deck[i]

    def deal_card(self):
        return self.deck.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def get_dealt_card(self, deck):
        self.hand.append(deck.deal_card())

    def show_hand(self):
        for card in self.hand:
            card.show_card()

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
                self.score = scores[0], scores[1]
            elif scores[0] <= 21 and scores[1] > 21:
                self.score = scores[0]
            elif scores[0] > 21 and scores[1] > 21:
                self.score = scores[0]
        # ace conditions
        else:
            for card in self.hand:
                self.score += card.card_value()

    def show_score(self):
        try:
            if self.score[1] == 21:
                print("Black Jack! {}'s score is {}!\n".format(self.name, self.score[1]))
            else:
                print("{}'s possible scores are {} and {}!\n".format(self.name, self.score[0], self.score[1]))
                self.score = self.score[1]
        except:
            if self.score > 21:
                print("Bust :( {}'s score is {}!\n".format(self.name, self.score))
            elif self.score == 21:
                print("Black Jack! {}'s score is {}!\n".format(self.name, self.score))
            else:
                print("{}'s score is {}!\n".format(self.name, self.score))

class Dealer:
    def __init__(self):
        self.hand = []
        self.score = 0

    def deal_self_card(self, deck):
        self.hand.append(deck.deal_card())

    def show_hand(self):
        for card in self.hand:
            card.show_card()

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
                self.score = scores[0], scores[1]
            elif scores[0] <= 21 and scores[1] > 21:
                self.score = scores[0]
            elif scores[0] > 21 and scores[1] > 21:
                self.score = scores[0]
        # ace conditions
        else:
            for card in self.hand:
                self.score += card.card_value()

    def show_score(self):
        try:
            if self.score[1] >= 17:
                self.score = self.score[1]
                print("The Dealer's score is {}!\n".format(self.score[1]))
            else:
                print("The Dealer's current possible scores are {} and {}!\n".format(self.score[0], self.score[1]))
        except:
            if self.score > 21:
                print("Bust :( The Dealer's score is {}!\n".format(self.score))
            elif self.score == 21:
                print("Black Jack! The Dealer's score is {}!\n".format(self.score))
            else:
                print("The Dealer's score is {}!\n".format(self.score))

# Play BlackJack
input("Welcome to Casino Black Jack, to continue press 'Enter'\n")
play = True
while(play):
    deck = Deck()
    deck.shuffle_deck()
    dealer = Dealer()

    check = True
    play_or_quit = ""
    while check:
        play_or_quit = input("To play type 'P' and press 'Enter'.\n  To leave type 'L' and press 'Enter'.\n")
        if play_or_quit == "P":
            check = False
        elif play_or_quit == "L":
            check = False
        else:
            print("Invalid entry, please try again.\n")

    if play_or_quit == "P":
        player = Player(input("Please type in your name and press 'Enter'!\n"))
        input("To start the game press 'Enter'\n")

        playing = True
        while(playing):
            # deal first 2 cards
            player.get_dealt_card(deck)
            dealer.deal_self_card(deck)
            player.get_dealt_card(deck)
            dealer.deal_self_card(deck)
            # deal first 2 cards

            # show scores
            if player.check_blackjack() and dealer.check_blackjack():
                print("Black Jack: Dealer and {} Tie!\n".format(player.name))
                print("Dealers Hand:")
                dealer.show_hand()
                dealer.show_score()
                print("{}'s Hand:".format(player.name))
                player.show_hand()
                player.show_score()
                break
            elif player.check_blackjack():
                print("Black Jack: {} wins!\n".format(player.name))
                print("Dealers Hand:")
                dealer.compute_score()
                dealer.show_hand()
                dealer.show_score()
                print("{}'s Hand:".format(player.name))
                player.show_hand()
                player.show_score()
                break
            elif dealer.check_blackjack():
                print("Black Jack: Dealer wins!\n")
                print("Dealers Hand:")
                dealer.show_hand()
                dealer.show_score()
                print("{}'s Hand:".format(player.name))
                player.compute_score()
                player.show_hand()
                player.show_score()
                break
            else:
                print("Dealers Hand:")
                print(dealer.hand[0].show_card())
                print("\n{}'s Hand:".format(player.name))
                player.compute_score()
                player.show_hand()
                player.show_score()
            # show scores

            # player hit or not
            player_hitting = True
            bust = False
            while player_hitting:
                hit_or_not = input("Would you like a Hit?\n  To Hit type 'H' and press 'Enter'.\n  Type 'N' and press 'Enter' if you want to stay.\n")
                if hit_or_not != "H":
                    player_hitting = False
                else:
                    player.get_dealt_card(deck)
                    player.compute_score()
                    try:
                        if player.score > 21:
                            bust = True
                            player_hitting = False
                        else:
                            print("Dealers Hand:")
                            print(dealer.hand[0].show_card())
                            print("\n{}'s Hand:".format(player.name))
                            player.show_hand()
                            player.show_score()
                    except:
                        print("Dealers Hand:")
                        print(dealer.hand[0].show_card())
                        print("\n{}'s Hand:".format(player.name))
                        player.show_hand()
                        player.show_score()

            if bust:
                print("Bust, {} losses :(\n".format(player.name))
                print("Dealers Hand:")
                dealer.compute_score()
                dealer.show_hand()
                dealer.show_score()
                print("\n{}'s Hand:".format(player.name))
                player.show_hand()
                player.show_score()
                break
            # player hit or not

            # dealer hitting
            dealer_hitting = True
            bust = False
            while dealer_hitting:
                dealer.compute_score()
                try:
                    dealer.score = dealer.score[1]
                    if dealer.score <= 21 and dealer.score >= 17:
                        dealer_hitting = False
                    else:
                        dealer.deal_self_card(deck)
                except:
                    if dealer.score <= 21 and dealer.score >= 17:
                        dealer_hitting = False
                    elif dealer.score > 21:
                        dealer_hitting = False
                        bust = True
                    else:
                        dealer.deal_self_card(deck)

            if bust:
                print("Bust, the Dealer losses :(\n".format(player.name))
                print("Dealers Hand:")
                dealer.show_hand()
                dealer.show_score()
                print("\n{}'s Hand:".format(player.name))
                player.show_hand()
                player.show_score()
                break
            # dealer hitting

            # crown winner
            try:
                player.score = player.score[1]
            except:
                pass

            if player.score > dealer.score:
                print("{} wins!\n".format(player.name))
                print("Dealers Hand:")
                dealer.show_hand()
                dealer.show_score()
                print("\n{}'s Hand:".format(player.name))
                player.show_hand()
                player.show_score()
            elif player.score < dealer.score:
                print("The Dealer wins!\n")
                print("Dealers Hand:")
                dealer.show_hand()
                dealer.show_score()
                print("\n{}'s Hand:".format(player.name))
                player.show_hand()
                player.show_score()
            else:
                print("It's a Tie!\n")
                print("Dealers Hand:")
                dealer.show_hand()
                dealer.show_score()
                print("\n{}'s Hand:".format(player.name))
                player.show_hand()
                player.show_score()
            playing = False
            # crown winner

    else:
        print("Thanks for coming to Casino Black Jack, have a good night!")
        play = False
