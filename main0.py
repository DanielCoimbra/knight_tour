from knight import Knight as K
import time

def tour():
    beginning = time.time()
    K.All_knights.append(K(place=[1, 1]))

    while True:
# --------------------------- ENDS AT 1 WIN ------------------------------------#
        if not K.All_knights[0].board:
            K.Winners.append(K.All_knights[0])
            break

        if len(K.Winners) == 1:
            break
        K.All_knights[0].fragment_knight()
    print('congrats '+ str(K.Winners[0]+"\n"))
    for move in K.Winners[0].moves:
        print(move)
    print(f'\nelapsed time:{time.time() - beggining} seconds')


def run():
    k = K(place=[1,1])
    k.fragment_knight()


tour()
