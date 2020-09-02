import random, time
from threading import Timer
def x(): globals().update(a=0); print('\nCat left you...')
a = 1
while a:
    if random.randint(0,1):
        time.sleep(random.randint(1,3))
        t = Timer(1, x)
        t.start()
        i = input('cat angry, pet it with <Enter>:')
        t.cancel()