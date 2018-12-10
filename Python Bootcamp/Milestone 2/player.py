class Player:

    def __init__(self, human=True):
        self.human = human
        self.budget = 100
        self.bet = 0
        self.points = 0
        self.my_cards = []

    def stand_or_hit(self):
        if self.human:
            action = input("stand or hit? ")
            if action == "hit":
                return True
            else:
                return False
        else:
            return False

    def receive_card(self, card):
        self.my_cards.append(card)

    def place_bet(self):
        while True:
            if self.human:
                try:
                    print("-------------------------------------------")
                    amount = int(input("Place a bet... "))
                    if amount <= self.budget:
                        self.budget -= amount
                        self.bet = amount
                        print(f"Vsazeno {self.bet}!")
                        print(f"Zbývá {self.budget}")
                        return True
                    else:
                        print("Insufficent funds")
                        return False
                except ValueError:
                    print("Špatná sázka")

    def show_cards(self, show_first_banker_card=False):
        first_banker_card=1
        for card in self.my_cards:
            if not self.human and first_banker_card==1 and not show_first_banker_card:
                first_banker_card+=1
                print("HIDDEN CARD")
            else:
                print(card.get_card())

    def evaluate_player(self):
        self.points = 0
        aces_in_hand = []
        for card in self.my_cards:
            self.points += card.get_points()[0]
            if card.get_card()[0] == 'Ace':
                aces_in_hand.append(10)

        # připočítání aces
        for aceplus in aces_in_hand:
            if self.points+aceplus > 21:
                break
            else:
                self.points += aceplus

        if self.points > 21:
            return False
        else:
            return True

    def reset_player(self):
        self.bet = 0
        self.points = 0
        self.my_cards = []
