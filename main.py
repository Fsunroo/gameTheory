import matplotlib.pyplot as plt
MAX = 100
CHOICE_RANGE = [i for i in range(MAX)]


def Win(STATE):
    STATE = list(STATE)
    mean = sum(STATE) / len(STATE)
    delta = list(map(lambda x: abs(x-(mean/3)), STATE))

    if min(delta) == delta[0]:
        return 100 / (len(delta)-len(set(delta))+1)
    else:
        return 0


All_Stats = []
for me in CHOICE_RANGE:
    result = 0
    for op1 in CHOICE_RANGE:
        for op2 in CHOICE_RANGE:
            result += Win((me, op1, op2))
    All_Stats.append(result)



All_Stats.append(result)
plt.plot(All_Stats)
plt.show()

print(All_Stats.index(max(All_Stats)))
