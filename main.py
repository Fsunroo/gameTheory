import matplotlib.pyplot as plt
MAX = 10
CHOICE_RANGE = [i for i in range(MAX)]


def Win(STATE):
    my_choice, op_choice = STATE
    if my_choice + op_choice <= 10:
        return my_choice
    else:
        return 0


All_Stats = []
for me in CHOICE_RANGE:
    result = 0
    for op in CHOICE_RANGE:
        result += Win((me, op))


All_Stats.append(result)
plt.plot(All_Stats)


All_Stats.index(max(All_Stats))
