import deck
import player


def print_players(show_first_banker_card=False):
    print("------------")
    print("PLAYER1:")
    player1.show_cards()
    print("\nBANKER:")
    dealer.show_cards(show_first_banker_card)
    print("------------")

def evaluate_game():
    print("\nVÝSLEDEK HRY")
    print_players(True)
    player1_result = player1.evaluate_player()
    dealer_result = dealer.evaluate_player()
    print(f"PLAYER 1 SCORE: {player1.points}")
    print(f"DEALER SCORE: {dealer.points}")
    if player1_result and not dealer_result:
        print("VYHRAL PLAYER 1!!!")
        player1.budget += 2 * player1.bet
    elif dealer_result and not player1_result:
        print("PLAYER 1 PROHRAL!!!")
    elif player1.points == dealer.points:
        print("DRAW!!!")
        player1.budget += player1.bet
    elif 21 >= player1.points > dealer.points and player1_result:
        print("VYHRAL PLAYER 1!!!")
        player1.budget += 2*player1.bet
    elif 21 >= dealer.points > player1.points and dealer_result:
        print("PLAYER 1 PROHRAL!!!")
    else:
        print("STALA SE NEJAKA BLBOST")
    player1.reset_player()
    dealer.reset_player()

def evaluate_session():
    print("-------------------------------------------")
    print(f"Roll hráče 1 je {player1.budget}")


player1 = player.Player(True)
dealer = player.Player(False)

while True:
    new_deck = deck.Deck()

    player1.place_bet()

    player1.receive_card(new_deck.get_random_card())
    player1.receive_card(new_deck.get_random_card())

    dealer.receive_card(new_deck.get_random_card())
    dealer.receive_card(new_deck.get_random_card())

    print_players()

    while True:
        if player1.stand_or_hit():
            player1.receive_card(new_deck.get_random_card())
            if not player1.evaluate_player():
                break
            if dealer.points < 17:
                dealer.receive_card(new_deck.get_random_card())
                if not dealer.evaluate_player():
                    break
            print_players()
        else:
            while dealer.points < 17:
                dealer.receive_card(new_deck.get_random_card())
                dealer.evaluate_player()
            break

    evaluate_game()

    if input("\nChcete hrát znovu (ano/ne)? ")!="ano":
        break

evaluate_session()
