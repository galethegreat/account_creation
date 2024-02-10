import win32api
import win32con

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