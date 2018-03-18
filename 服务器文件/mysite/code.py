import random
def randomcode():
    a = random.randint(100,999)
    a = str(a)+chr(random.randint(97,112))
    return a