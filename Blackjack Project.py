

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.


import random


def twentyone():
    if sum(you_card) == 21:
        if sum(comp_card) == 21:
            final()
            print("Draw")
            aaa = False
            blackjack()
        else:
            final()
            print("You win. Blackjack.")
            aaa = False
            blackjack()
    elif sum(comp_card) == 21:
        print("Lose, opponent has Blackjack.")
        aaa = False
        blackjack()
# def show():
#     print(
#         f"   Your cards: {you_card}, current score: {sum(you_card)}\n   Computer's first card: {comp_card[0]}")


# def final():
#     print(
#         f"   Your final hand: {you_card}, final score: {sum(you_card)}\n   Computer's final hand: {comp_card}, final score: {sum(comp_card)}")


def you_bust():
    if sum(you_card) > 21:
        final()
        print("Bust. You lose.")
        aaa = False
        blackjack()


def a(cardlist):
    for card in cardlist:
        if card == 11 and sum(cardlist) > 21:
            card = 1


# print(logo)
card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# you_card = [random.choice(card), random.choice(card)]
# comp_card = [random.choice(card), random.choice(card)]


def blackjack():
    game_on = input(
        "Do you want to play a game of BlackJack? Type 'y' or 'n': ")
    you_card = [random.choice(card), random.choice(card)]
    comp_card = [random.choice(card), random.choice(card)]
    aaa = True

    def show():
        print(
            f"   Your cards: {you_card}, current score: {sum(you_card)}\n   Computer's first card: {comp_card[0]}")

    def final():
        print(
            f"   Your final hand: {you_card}, final score: {sum(you_card)}\n   Computer's final hand: {comp_card}, final score: {sum(comp_card)}")

    def twentyone():
        if sum(you_card) == 21:
            if sum(comp_card) == 21:
                final()
                print("Draw")
                aaa = False
                blackjack()
            else:
                final()
                print("You win. Blackjack.")
                aaa = False
                blackjack()
        elif sum(comp_card) == 21:
            print("Lose, opponent has Blackjack.")
            aaa = False
            blackjack()

    def you_bust():
        if sum(you_card) > 21:
            final()
            print("Bust. You lose.")
            aaa = False
            blackjack()
    if game_on == "y":
        a(you_card)
        show()
        while aaa:
            twentyone()
            another_card = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if another_card == "y":
                you_card.append(random.choice(card))
                a(you_card)
                show()
                twentyone()
                you_bust()
            else:
                if sum(comp_card) > sum(you_card):
                    final()
                    print("You lose.")
                    aaa = False
                    blackjack()
                elif sum(comp_card) < sum(you_card):
                    if sum(comp_card) >= 17:
                        final()
                        print("You win.")
                        aaa = False
                        blackjack()
                    else:
                        comp_card.append(random.choice(card))
                        a(comp_card)


blackjack()
