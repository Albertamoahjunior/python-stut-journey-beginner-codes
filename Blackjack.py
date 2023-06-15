import random

cards = [1,2,3,4,5,6,7,8,9,10,"A","J","Q","K"]
player = {
"player":[],
"dealer":[],
}
card_number = {
"A" : 1,
"J" : 10,
"Q" : 10,
"K" : 10,
}
play = True
selection = 0
dealer_total = 0
player_total = 0

def verdict(total):
    global dealer_total
    if total <= 21:
        if dealer_total < 17:
            selection = random.randint(1,15)
            if selection > 10:
                player["dealer"].append(cards[selection - 1])
            else:
                player["dealer"].append(selection)
            dealer_total += selection

            if dealer_total > 21:
                    dealer_total - selection
                    player["dealer"].pop(selection)

        if total > dealer_total:
            if "A" in player["dealer"]:
                dealer_total += 10
                if dealer_total > 21:
                    dealer_total - 10
            if total > dealer_total:
                return f"You win"

        elif total == dealer_total:
            return f"You draw"

        else:
            return f"You loose"
    else:
        return f"You busted you loose"

play = input("Do you want to play Black Jack? Type 'y' for yes 'n' for no: ")
if play == 'n':
    play = False

while play:
    for n in range(0,2):
        selection = random.randint(1,14)
        if selection > 10:
            player["dealer"].append(cards[selection - 1])
        else:
            player["dealer"].append(selection)

        player_selection = random.randint(1,14)
        if selection > 10:
            player["player"].append(cards[player_selection - 1])
        else:
            player["player"].append(player_selection)
    for n in player["dealer"]:
        if n == 'J' or n == 'Q' or n == 'K':
            n = 10
        elif n == 'A':
            n =1
        dealer_total += n

    for n in player["player"]:
        if n == 'J' or n == 'Q' or n == 'K':
            n = 10
        elif n == 'A':
            n = 1
        player_total += n

    choice = player["dealer"][0]
    dealer = player["dealer"]
    cards = player["player"]
    print(f"Your cards: {cards}, current score is {player_total}")
    print(f"Computer's first card {choice}")

    player_choice = input("Type 'y' to get another card, type 'n' to pass: ")
    if player_choice == 'y':
        player_selection = random.randint(1,14)
        if player_selection == 10:
            player_total += 10
            player["player"].append(player_selection)
        elif player_selection > 10:
            player["player"] += cards[player_selection - 1]
            player_total += 10
        else:
            player["player"].append(player_selection)
            player_total += player_selection
        break
    else:
        break

print(verdict(player_total))
print(f"Your cards: {cards}")
print(f"Computer's cards: {dealer} ")



