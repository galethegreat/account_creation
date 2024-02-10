import time
import pyautogui as pg

print("Waiting 3 seconds")
time.sleep(3)
print("recording")

with open("coord_9.txt", "a") as file:
    while True:
        time.sleep(0.01)
        current_x, current_y = pg.position()
        file.write(f"{current_x} {current_y}\n")
        file.flush()
