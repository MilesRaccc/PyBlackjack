from Entities.Classes import *
import os


def clear():
    os.system("cls")


def main():
    resp = input("Wanna play a blackjack game? Y/N\n")
    if resp == "Y":
        # clear()

        while True:
            deck = Deck()
            ai_hand = AiHand(deck)
            player_set = [PlayerHand(deck)]

            if ai_hand.get_total_value() == 21:
                ai_hand.ai_open_hand()
                ai_hand.ai_console_output(player_set)
            else:
                # Player Turn
                first_player_hand = player_set[0]
                q = first_player_hand.player_turn(deck, player_set, ai_hand)

                if len(player_set) > 1:
                    second_player_hand = player_set[1]
                    q = second_player_hand.player_turn(deck, player_set, ai_hand)

                if q:
                    break

                if not all(hand.hand_lost for hand in player_set):
                    ai_hand.ai_open_hand()
                    while True:
                        ai_hand.ai_console_output(player_set)
                        if ai_hand.get_total_value() < 22 and not ai_hand.ai_win_conditions(player_set):
                            ai_hand.hit(deck)
                        else:
                            break

            resp = input("\nPlay Again? Y/N\n")
            if resp == "N":
                break


if __name__ == "__main__":
    main()
