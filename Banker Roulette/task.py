import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#1 option
print(random.choice(friends))

#2 option
randomIndex = random.randint(0,4)
print(friends[randomIndex])