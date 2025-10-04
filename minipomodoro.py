from math import floor
from time import sleep


def pomo(
    duration: float, label: str
):  # main function takes in a duration in minutes and a labal
    timeElapsed: int = (
        0  # assuming second precision is good enough for this simple of a task
    )
    while timeElapsed < (duration * 60):
        sleep(1)
        timeElapsed += 1
        if timeElapsed >= 60:
            timeMin = floor(timeElapsed / 60)  # 60 seconds/60 = 1 min
            remTime = (
                timeElapsed % 60
            )  # the remaining time in seconds is the remainder of the division of seconds/60
            print(f"\relapsed time: {timeMin}m, {remTime}s      ", end="", flush=True)
        else:
            print(f"\relapsed time: {timeElapsed}s", end="", flush=True)
    print(f"\nyour {label} is finished!")


timeWork: float = float(input("how many minutes should a work session take?: "))
timeBreak: float = float(input("how many minutes should a break last?: "))
sessions: int = int(input("how many sessions do you want?: "))

for i in range(sessions):
    print(f"cycle {i + 1}")
    pomo(timeWork, "work session")
    if i < sessions - 1:
        pomo(
            timeBreak, "break"
        )  # makes it so you dont have a break after the final cycle
print("all cycles complete!")
