import random


def game(n: int):
    doors = [1, 2, 3]

    # randomly assign the prize behind door 1,2, or 3
    prize = random.randint(1, 4)

    # contestants random choice
    contestant_guess = random.randint(1, 4)

    goat_doors = [door for door in doors if door != prize]

    # host reveals a goat door
    possible_reveal_doors = [door for door in goat_doors if door != contestant_guess]
    if len(possible_reveal_doors) == 2:
        reveal_door = random.choice(possible_reveal_doors)
    else:
        reveal_door = possible_reveal_doors[0]

    # Define the door that the contest would switch to
    switch_door = [door for door in doors if door != contestant_guess and door != reveal_door][0]
    # determine if the player switched the door and if he won
    player_switched = switch_door != contestant_guess
    player_won = prize == switch_door

    return {"game_number": n, "player_switched": player_switched, "player_won": player_won}
