import random

def attack():
    attack_number = random.randint(1,1000)
    return attack_number

def attack_names():
    rand_names = random.randint(1,15)
    if rand_names == 1:
        names = "wolloped"
    if rand_names == 2:
        names = "grabbed a dirty dagger and stabbed"
    if rand_names == 3:
        names = "kicked"
    if rand_names == 4:
        names = "punched"
    if rand_names == 5:
        names = "bit"
    if rand_names == 6:
        names = "stomped on"
    if rand_names == 7:
        names = "threw a rock at"
    if rand_names == 8:
        names = "headbutted"
    if rand_names == 9:
        names = "belly flopped"
    if rand_names == 10:
        names = "made fun of"
    if rand_names == 11:
        names = "coughed and passed a disease to"
    if rand_names == 12:
        names = "threw 35 bricks at"
    if rand_names == 13:
        names = "threw a slipper at"
    if rand_names == 14:
        names = "licked"
    if rand_names == 15:
        names = "screamed really loudly at"
    return names

def run():
    user_hp = 1000
    opponent_hp = 1000
    while user_hp or oppenent_hp > 0:
        print("------------------------------------------------")
        print("Your HP: {}\n"
              "Python's HP: {}".format(user_hp, opponent_hp))
        print("------------------------------------------------")
        user_choice = input("Input any key to attack! ")
        user_attack = attack()
        attack_name = attack_names()
        print("------------------------------------------------")
        print("You {} Python and did {} damage!".format(attack_name, user_attack))
        opponent_hp = opponent_hp - user_attack
        if opponent_hp <= 0:
            print("------------------------------------------------")
            print("You won the battle and defeated Python!")
            print("------------------------------------------------")
            break
        else:
            pass
        print("------------------------------------------------")
        input("Input any key to prepare for Python's attack! ")
        print("------------------------------------------------")
        opponent_attack = attack()
        attack_name = attack_names()
        print("Python {} you and did {} damage!".format(attack_name, opponent_attack))
        user_hp = user_hp - opponent_attack
        if user_hp <= 0:
            print("------------------------------------------------")
            print("You died.")
            print("------------------------------------------------")
            break
        else:
            pass
        print("------------------------------------------------")
        input("Input any key to see yours and Python's HP for this turn! ")
        print("------------------------------------------------")
        print("Your HP: {}\n"
              "Python's HP: {}".format(user_hp, opponent_hp))
        print("------------------------------------------------")
        if user_hp > opponent_hp:
            print("You did the most damage this turn!")
        elif user_hp < opponent_hp:
            print("Python did the most damage this turn!")
        else:
            print("It's a draw this round!")
        print("------------------------------------------------")
        continuing = input("Would you like to continue the battle? (y/n):  ")
        print("------------------------------------------------")
        if continuing.lower() != 'y':
            print("You ran away!")
            print("------------------------------------------------")
            break

print("A mighty Python appeared! You must defeat it!")
run()

while True:
    play_again = input("Would you like to play again? (y/n): ")
    if play_again.lower() == 'y':
        run()
    else:
        print("------------------------------------------------")
        print("Thanks for playing!")
        print("------------------------------------------------")
        break