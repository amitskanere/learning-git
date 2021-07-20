import random
#print random values
print("five random numbers:")
for i in range(1,6):
    print(random.randint(1,10))

#print members from random list
members = ["amit", "chetan", "kanal","ashish"]
leader=random.choice(members)
print("\n"+leader)

#dice program
class Dice():
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first,second


dice=Dice()
print("your dice roll result is ")
print(dice.roll())
