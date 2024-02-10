import win32api
import win32con
import time
import random
lines = list()
with open("coord_8.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

lines.reverse()
while lines:
    line = lines.pop()
    x, y = int(line.split()[0]), int(line.split()[1])
    win32api.SetCursorPos((x, y))
    time.sleep(0.01)