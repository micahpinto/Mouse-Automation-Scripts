import pyautogui          # Import mouse automation library
import time               # Import time library for delays

pyautogui.FAILSAFE = True # Enable failsafe mode (move mouse to corner to stop)

time.sleep(5)             # Wait 5 seconds before starting

pyautogui.moveTo(646, 55, duration=0.01)  # Move cursor to x=646, y=55
pyautogui.click()                         # Click the mouse

time.sleep(0.3)           # Wait 0.3 seconds

# Move mouse to main interaction area
pyautogui.moveTo(794, 738, duration=0.01) 

# Loop 10,000 times
for i in range(10000):
    pyautogui.click()     # Click at current position
    time.sleep(14.5)      # Wait 14.5 seconds before next click

# Final click to close or finish
pyautogui.moveTo(905, 738, duration=0.01) 
pyautogui.click()         # Final click
