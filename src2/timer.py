import time

seconds = 5
print(f"Countdown from {seconds} seconds")
for i in range(seconds, 0, -1):
    print(i)
    time.sleep(1)
print("Time's up!")
