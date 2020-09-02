from random import randint; from threading import Timer; from time import sleep
def x(): globals().update(a=0); print('\nCat left you...')
a = 1
while a:
    if randint(0,1):
        sleep(randint(1,3))
        t = Timer(0.5, x); t.start()
        input('cat angry, pet it with <Enter>')
        t.cancel()