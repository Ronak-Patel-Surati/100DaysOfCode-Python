# a simple count down program
import time

time_set_by_user = int(input("Enter the time in seconds: "))

for x in range(time_set_by_user, 0, -1):
    seconds = x % 60
    minutes = (x // 60) % 60
    hours = x // 3600
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's Up!")
