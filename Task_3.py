import random

for i in range(5):
    x = random.choice([i for i in range(-9,9) if i not in [0]])
    y = random.choice([i for i in range(-9,9) if i not in [0]])
    print(f"x = {x}, y = {y}")
    if ((x > 0) and (y > 0)):
        print(1)
    elif ((x > 0) and (y < 0)):
        print(4)
    elif ((x < 0) and (y > 0)):
        print(2)
    else:
        print(3)