import time
import random

rltList = ['Loading...', 'Hold Up...', 'Getting the ammo...', 'Putting down inconveniences...', '( -_•)▄︻テحكـ━一...', 'gun  ̸̇̎/̸̄̿̅̎̎̅͆ ͆͆͆͆̔̿͞ ͆̅̿̄͞ ̿ ̄̇̿̚ ̎ ̎͆ ...', ':)...', 'BIG CHUNGUS...', 'Beans...', 'The heavy is dead (˚0˚)...', 'G was here...']

def randomLoadingText(amount, minTime, maxTime, console):
    for i in range(amount):
        time.sleep(random.randint(minTime, maxTime))
        yield random.choice(rltList)

for message in randomLoadingText(7, 1, 4, 'pc'): #test
    print(message)  

