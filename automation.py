import win32api
import win32con
import time
import random
from constants import VK_CODE as vk
def char_to_hex(c):
    return ord(c)

def type_write(string):
    for letter in string:
        if letter == "@":
            ctrlv()
        elif ord(letter) >= ord('A') and ord(letter) <= ord('Z'):
            win32api.keybd_event(vk['shift'], 0, 0, 0)
            letter = letter.lower()
            win32api.keybd_event(vk[letter], 0, 0, 0)
            interval = 9 + random.randint(0, 5)
            time.sleep(interval/100)
            win32api.keybd_event(vk[letter], 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(0.05)
            win32api.keybd_event(vk['shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            
        else:
            
            win32api.keybd_event(vk[letter], 0, 0, 0)
            interval = 9 + random.randint(0, 5)
            time.sleep(interval/100)
            win32api.keybd_event(vk[letter], 0, win32con.KEYEVENTF_KEYUP, 0)

def ctrlv():
    VK_CONTROL = 0x11
    VK_V = 0x56

    # Simulate pressing and releasing the CTRL key
    win32api.keybd_event(VK_CONTROL, 0, 0, 0)  # Press CTRL key
    # Simulate pressing and releasing the V key
    win32api.keybd_event(VK_V, 0, 0, 0)  # Press V key
    # Release V key
    win32api.keybd_event(VK_V, 0, win32con.KEYEVENTF_KEYUP, 0)
    # Release CTRL key
    win32api.keybd_event(VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)

SIGN_UP_X_MIN = 1753
SIGN_UP_X_MAX = 1785
SIGN_UP_Y_MIN = 173
SIGN_UP_Y_MAX = 178
dwFlags = win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP
user = "DarkDomainZoomGirl"
password = "Shifra123@"
email = "r0h5g1nffd@txcct.com"

lines = list()

with open("coordinates.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

lines.reverse()

while lines:
    line = lines.pop()
    x, y = int(line.split()[0]), int(line.split()[1])
    win32api.SetCursorPos((x, y))
    time.sleep(0.01)

win32api.mouse_event(dwFlags, x, y, 0, 0)

lines = list()
with open("coord_2.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

lines.reverse()
while lines:
    line = lines.pop()
    x, y = int(line.split()[0]), int(line.split()[1])
    win32api.SetCursorPos((x, y))
    time.sleep(0.01)

win32api.mouse_event(dwFlags, x, y, 0, 0)

type_write(email)

lines = list()
with open("coord_3.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

lines.reverse()
while lines:
    line = lines.pop()
    x, y = int(line.split()[0]), int(line.split()[1])
    win32api.SetCursorPos((x, y))
    time.sleep(0.01)


win32api.mouse_event(dwFlags, x, y, 0, 0)

lines = list()
with open("coord_4.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

lines.reverse()
while lines:
    line = lines.pop()
    x, y = int(line.split()[0]), int(line.split()[1])
    win32api.SetCursorPos((x, y))
    time.sleep(0.01)

win32api.mouse_event(dwFlags, x, y, 0, 0)
type_write(user)

lines = list()
with open("coord_5.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

lines.reverse()
while lines:
    line = lines.pop()
    x, y = int(line.split()[0]), int(line.split()[1])
    win32api.SetCursorPos((x, y))
    time.sleep(0.01)

win32api.mouse_event(dwFlags, x, y, 0, 0)
type_write(password)

lines = list()
with open("coord_6.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

lines.reverse()
while lines:
    line = lines.pop()
    x, y = int(line.split()[0]), int(line.split()[1])
    win32api.SetCursorPos((x, y))
    time.sleep(0.01)

win32api.mouse_event(dwFlags, x, y, 0, 0)
time.sleep(0.1)

lines = list()
with open("coord_7.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

lines.reverse()
while lines:
    line = lines.pop()
    x, y = int(line.split()[0]), int(line.split()[1])
    win32api.SetCursorPos((x, y))
    time.sleep(0.01)

win32api.mouse_event(dwFlags, x, y, 0, 0)
time.sleep(0.1)


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

win32api.mouse_event(dwFlags, x, y, 0, 0)
time.sleep(0.5)

lines = list()
with open("coord_9.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

lines.reverse()
while lines:
    line = lines.pop()
    x, y = int(line.split()[0]), int(line.split()[1])
    win32api.SetCursorPos((x, y))
    time.sleep(0.01)

win32api.mouse_event(dwFlags, x, y, 0, 0)
