import time
import pyautogui

# get the time from the user
hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))
milliseconds = int(input("Enter the number of milliseconds: "))

# calculate the total time in seconds
total_time = hours * 3600 + minutes * 60 + seconds + milliseconds / 1000

# loop until the time is up
while total_time > 0:
    # calculate the time in seconds, minutes, hours, and milliseconds
    milliseconds = int((total_time % 1) * 1000)
    seconds = int(total_time % 60)
    minutes = int((total_time // 60) % 60)
    hours = int(total_time // 3600)

    # print the time
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}:{milliseconds:03d}")

    # wait for 1 millisecond
    time.sleep(0.01)

    # decrement the total time
    total_time -= 0.01

# print "Time's up!" when the countdown is finished
print("Time's up!")
pyautogui.click()