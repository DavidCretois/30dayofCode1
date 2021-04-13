# J = Pierre, C = Pierre == Egalité
# J = Pierre, C = Papier == C gagné
# J = Pierre, C = Ciseaux == J gagné
# J = Papier, C = Pierre == J gagné
# J = Papier, C = Papier == Egalité
# J = Papier, C = Ciseaux == C gagné
# J = Ciseaux, C = Pierre == C gagné
# J = Ciseaux, C = Papier == J gagné
# J = Ciseaux, C = Ciseaux == Egalité
# LOGICAL : Eglité = 2, Perdu = 3, Gagné = 3

import ramdom
import math

def play():
    user = input("Quel est votre choix ? 'r' pour pierre, 'p' pour papier, 's' pour ciseaux\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return (0, user, computer)

    # r > s, s > p, p > r
    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)

    return "Vous avez choisis {} et l'ordinateur a choisit {}. Vous avez perdu".format(user, computer)


def is_win(player, opposent):
    if (player == 'r' and opposent == 's') or (player == 's' and opposent == 'p') or (player == 'p' and opposent == 'r'):
        return True
    return False

def play_best_of(n):
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        # Egalité
        if result == 0:
            print("Egalité ! Vous et l'ordinateur avez les mêmes choix {}. \n".formmat(user))
        #Vous avez gagné
        elif result == 1:
            player_wins += 1
            print("Vous avez choisis {} et l'ordinateur a choisit {}. Vous avez gagné\n".format(user, computer))
        else:
            computer_wins += 1
            print("Vous avez choisis {} et l'ordinateur a choisit {}. Vous avez perdu !(\n".format(user, computer))

    if player_wins > computer_wins:
        print("Tu as gagné les parts de {} parties! Quel champion !.format(n)")
    else:
        print("Malheureusement, the computer a gagné les parties {}. Tu ferais mieux la prochaine fois !".format(n))

if __name__ == '__main__':
    play_best_of(3) #2
