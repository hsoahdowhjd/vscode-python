import time
def count_down_timer(seconds):
    while seconds>0:
        minits=int(seconds/60)
        sec=int(seconds%60)
        timer=f'{minits}:{sec}'
        print(timer)
        seconds-=1
    print("time up")
seconds=int(input("how many seconds: "))
count_down_timer(seconds)