import pyautogui
import time

# Wait 5 seconds for user to prepare and move mouse to desired location
time.sleep(5)

# Print the current mouse cursor position (x, y coordinates)
print(pyautogui.position())
