import random
import matplotlib.pyplot as plt

random.seed(777)

ruin = 0
goal = 100
money = 50
time = 0

time_list = [time]
money_list = [money]

while money in range(ruin + 1, goal):
    time += 1
    reward = 1
    game_res = random.choice([0, 1])
    if game_res == 1:
        money += reward
    else:
        money -= reward
    time_list.append(time)
    money_list.append(money)

print(len(money_list))
print(max(money_list))
print(min(money_list))

plt.plot(time_list, money_list)
plt.axhline(y=goal, color='g')
plt.axhline(y=ruin, color='r')
plt.show()