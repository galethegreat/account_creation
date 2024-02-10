import win32api
import win32con
import ctypes
import time
# Define the INPUT structure
class INPUT(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_ulong),
        ("ki", ctypes.POINTER(win32con.KEYBDINPUT))
    ]

# Define the KEYBDINPUT structure
class KEYBDINPUT(ctypes.Structure):
    _fields_ = [
        ("wVk", ctypes.c_ushort),
        ("wScan", ctypes.c_ushort),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))
    ]

# Define the key event constants
KEYEVENTF_KEYDOWN = 0x0000
KEYEVENTF_KEYUP = 0x0002

# Define a function to simulate keyboard input using SendInput
def send_input(keys):
    inputs = []
    for key in keys:
        ki = win32con.KEYBDINPUT(key, 0, KEYEVENTF_KEYDOWN, 0, None)
        inputs.append(INPUT(win32con.INPUT_KEYBOARD, ctypes.pointer(ki)))
        ki = win32con.KEYBDINPUT(key, 0, KEYEVENTF_KEYUP, 0, None)
        inputs.append(INPUT(win32con.INPUT_KEYBOARD, ctypes.pointer(ki)))
    win32api.SendInput(len(inputs), (INPUT * len(inputs))(*inputs))

# Example usage:
time.sleep(2)
send_input([ord('A'), ord('B'), ord('C')])