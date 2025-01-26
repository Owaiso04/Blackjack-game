import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]


def deal_card():
    """Returns a random card from the deck."""
    return random.choice(cards)


def calculate_score(hand):
    """Calculates the score of a hand."""
    if sum(hand) == 21 and len(hand) == 2:
        return 0  # Blackjack
    if 11 in hand and sum(hand) > 21:
        hand[hand.index(11)] = 1
    return sum(hand)


def compare_scores(player_score, computer_score):
    if player_score > 21:
        return "You went over.. You lose!"
    elif computer_score > 21:
        return "Computer went over.. You win!"
    elif player_score == computer_score:
        return "That was a draw!"
    elif player_score == 0:
        return "Congratulations.. You got a Blackjack, You win!"
    elif computer_score == 0:
        return "Computer got a Blackjack, You lose!"
    elif player_score > computer_score:
        return "Congratulations.. You win!"
    else:
        return "You lose!"


def play_game():
    print(logo)
    player_hand = [deal_card(), deal_card()]
    computer_hand = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card: {computer_hand[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True

        else:
            another_card = input(
                "Type 'y' to get another card, type 'n' to pass: "
            ).lower()
            if another_card == "y":
                player_hand.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
    print(compare_scores(player_score, computer_score))


while (
    input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y"
):
    play_game()
