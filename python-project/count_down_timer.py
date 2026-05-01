import time

total_seconds = int(input("Enter time in seconds: "))

while total_seconds > 0:
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"{hours:02}:{minutes:02}:{seconds:02}", end="\r")

    time.sleep(1)
    total_seconds -= 1

print("\n⏰ Time's up!")