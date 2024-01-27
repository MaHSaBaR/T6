import pandas as pd
import matplotlib.pyplot as plt

try:
    # Input player names
    names = input('').split(' ')
    player1, player2 = names[0], names[1]

    # Input player health
    health = input().split(' ')
    health1, health2 = int(health[0]), int(health[1])

    # Input damage values
    damage = input().split(' ')
    A, B, C = int(damage[0]), int(damage[1]), int(damage[2])

    # Input rounds
    round1, round2, round3 = input('').split(' '), input('').split(' '), input('').split(' ')

    damage_dict = {'A': A, 'B': B, 'C': C}

    # Calculate remaining health
    Health1 = health1 - damage_dict[round1[1]] - damage_dict[round2[1]] - damage_dict[round3[1]]
    Health2 = health2 - damage_dict[round1[0]] - damage_dict[round2[0]] - damage_dict[round3[0]]

    # Calculate scores
    s1 = sum(damage_dict[round1[1]] > damage_dict[round1[0]],
             damage_dict[round2[1]] > damage_dict[round2[0]],
             damage_dict[round3[1]] > damage_dict[round3[0]])

    s2 = 3 - s1

    # Print results
    print(f'{player1} -> Score: {s1}, Health: {Health1}')
    print(f'{player2} -> Score: {s2}, Health: {Health2}')

except Exception as e:
    print(f'Error: {e}')

finally:
    # Write results to a file
    with open('result.txt', 'w') as f:
        f.write('{} -> Score: {}, Health: {}'.format(player1, s1, Health1))
        f.write('\n{} -> Score: {}, Health: {}'.format(player2, s2, Health2))

    # Create a bar plot
    data = {'players': [player1, player2], 'scores': [s1, s2]}
    df = pd.DataFrame(data)
    df.plot(kind='bar', x='players', y='scores')
    plt.show()
