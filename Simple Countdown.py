from time import sleep

print("Type `-1` to stop the script.")
sec = int(input("Seconds to begin the countdown: "))

count = sec
while sec != -1:
    count -= 1
    sleep(1)
    print(f"[Countdown] - [{count}]")
    if count == 0:
        print("\n[Countdown] - Stopped!")
        print("Type `-1` to stop the script.")
        sec = int(input("Seconds to begin the countdown: "))

