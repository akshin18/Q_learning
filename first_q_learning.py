
import numpy as np
import random
import	pygame







'''

	0	0	0	0	0

	x	x	x	x	0

	0	0	0	0	0

	0	0	0	0	x

	0	0	0	0	W



'''
long = 5
actions_count = 4
Q = np.zeros((long**2 ,actions_count))
state =0
can = []
epsilon = 0.3
G = 0.85
steps = [0]
c = -1

for i in range(2000):
    for i in range(actions_count):  # выявляем возможные действия для текущего состояния
        if i == 0:
            if state - long >= 0:
                can.append([state, i])
        if i == 1:
            if state % long != 4:
                can.append([state, i])
        if i == 2:
            if state + long < long ** 2:
                can.append([state, i])
        if i == 3:
            if state % long != 0:
                can.append([state, i])

    # rand = random.random()
    # if epsilon < rand:
    # 	for i in can:
    # 		predict = max(can)
    # if epsilon > rand:
    predict = random.choice(can)

    if predict[1] == 0:
        state -= 5
    if predict[1] == 1:
        state += 1
    if predict[1] == 2:
        state += 5
    if predict[1] == 3:
        state -= 1

    if state == 24:
        R = 200
    # print("Пиздец бочек потик")
    elif state == 5:
        R = -100
    elif state == 6:
        R = -100
    elif state == 7:
        R = -100
    elif state == 8:
        R = -100
    elif state == 19:
        R = -100
    elif state == 18:
        R = -100
    elif state == 17:
        R = -100
    else:
        R = 0

    # print(predict)
    # print(state)
    # print(R)
    # print(Q[predict[1]])

    Q[predict[0], predict[1]] += 0.01 * (R + (G * (np.max(Q[state]) - Q[predict[0], predict[1]])))
    can = []

for zi, i in enumerate(Q):
    print(zi, i)

# for zi,i in enumerate(Q):
# 	if zi% 5 == 0:
# 		print('\n',end='\n')


# 	print(i,end='\t\t\t')
# print()	


state = 0

for i in range(14):
    for i in range(actions_count):  # выявляем возможные действия для текущего состояния
        if i == 0:
            if state - long >= 0:
                can.append([state, i, Q[state, i]])
        if i == 1:
            if state % long != 4:
                can.append([state, i, Q[state, i]])
        if i == 2:
            if state + long < long ** 2:
                can.append([state, i, Q[state, i]])
        if i == 3:
            if state % long != 0:
                can.append([state, i, Q[state, i]])
    predict = max([i[2] for i in can])
    # print(can)
    # print(predict)
    for i in can:
        if predict == i[2]:
            a = [i[0], i[1]]
            break
    # print(a)

    if a[1] == 0:
        state -= 5
    if a[1] == 1:
        state += 1
    if a[1] == 2:
        state += 5
    if a[1] == 3:
        state -= 1
    can = []
    steps.append(state)
    print(state, end=" -> ")
steps.append(29)
steps = iter(steps)

RES = WEIGHT, HEIGHT = (300, 300)
TILE = 50
FPS = 2
x, y = 0, 0

pygame.init()
sc = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

while True:
    sc.fill(pygame.Color('darkslategray'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.draw.rect(sc, pygame.Color('green'), (WEIGHT - TILE, HEIGHT - TILE, TILE, TILE))
    [pygame.draw.rect(sc, pygame.Color('red'), (TILE * i, 1 * TILE, TILE, TILE)) for i in range(5)]
    [pygame.draw.rect(sc, pygame.Color('red'), (WEIGHT - TILE*i, HEIGHT - TILE * 3, TILE, TILE)) for i in range(4)]
    # [pygame.draw.rect(sc, pygame.Color('red'), (WEIGHT-TILE-TILE * i, 11 * TILE, TILE, TILE)) for i in range(0,3)]

    try:
        b = next(steps)
        print(b - c)
        if b - c == 1:
            x += TILE
        elif b - c == 5:
            y += TILE
        elif b - c == -1:
            x -= TILE
        elif b - c == -5:
            y -= TILE
        else:
            pass
        c = b
    except Exception as e:
        pass

    pygame.draw.rect(sc, pygame.Color('black'), (x, y, TILE, TILE))
    [pygame.draw.line(sc, pygame.Color('gold'), (i * TILE, 0), (i * TILE, HEIGHT), 3) for i in range(HEIGHT // TILE)]
    [pygame.draw.line(sc, pygame.Color('gold'), (0, i * TILE), (WEIGHT, i * TILE), 3) for i in range(WEIGHT // TILE)]

    pygame.display.flip()
    clock.tick(FPS)