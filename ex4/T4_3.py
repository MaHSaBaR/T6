try:
    names = input('').split(' ')
    player1 = names[0]
    player2 = names[1]
    try:
        health = input().split(' ')
        health1 = int(health[0])
        health2 = int(health[1])
        try:
            damage = input().split(' ')
            A = int(damage[0])
            B = int(damage[1])
            C = int(damage[2])
            try:
                round1 = input('').split(' ')
                round2 = input('').split(' ')
                round3 = input('').split(' ')

                dict = {'A': A, 'B': B, 'C':C}

                Health1 = health1 - dict[round1[1]] - dict[round2[1]] - dict[round3[1]]
                Health2 = health2 - dict[round1[0]] - dict[round2[0]] - dict[round3[0]]


                s1 = 0
                s2 = 0
                if dict[round1[1]] > dict[round1[0]]:
                    s2 += 1
                elif dict[round1[1]] < dict[round1[0]]:
                    s1 += 1
                if dict[round2[1]] > dict[round2[0]]:
                    s2 += 1
                elif dict[round2[1]] < dict[round2[0]]:
                    s1 += 1
                if dict[round3[1]] > dict[round3[0]]:
                    s2 += 1
                elif dict[round3[1]] < dict[round3[0]]:
                    s1 += 1


                print(f'{player1} -> Score: {s1}, Health: {Health1}')
                print(f'{player2} -> Score: {s2}, Health: {Health2}')


            except:
                print('Invalid Command.')
        except:
            print('Invalid Command.')
    except:
        print('Invalid Command.')
except:
    print('Invalid Command.')

finally:
    with open('result.txt','w') as f:
        f.write('{} -> Score: {}, Health: {}'.format(player1,s1,Health1))
        f.write('\n{} -> Score: {}, Health: {}'.format(player2,s2,Health2))
       
    f.close()


    import pandas as pd
    import matplotlib.pyplot as plt
    data = {'players' : [player1,player2], 'scores':[s1,s2]}
    df = pd.DataFrame(data)
    df.plot(kind= 'bar', x= 'players', y= 'scores')
    plt.show()

        




