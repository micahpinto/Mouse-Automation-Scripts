# Mouse-Automation-Scripts
Automate repetitive clicking tasks so you don't have to click manually over and over.

This file contains Python scripts that automate repetitive mouse clicks for testing memory chip efficiency. When a memory chip is programmed and tested multiple times (1,000 cycles, 7,000 cycles, 10,000 cycles), manual clicking becomes impractical due to the time required. These scripts eliminate manual user interaction by automating the entire testing process.

Why Automate Memory Chip Testing?
The Problem: Manual Testing is Impractical

When testing memory chip efficiency, you need to run multiple program cycles:

Example Timeline:
```
Test Scenario: 1,000 cycles with 20 minutes per cycle

1,000 cycles × 20 minutes = 20,000 minutes
                          = 333 hours
                          = 14 days (non-stop)

Manual clicking for 14 days is impossible!
```
**The Solution: Automation**

Instead of clicking manually for weeks/months, automate it:
- Run continuously unattended
- Complete in days instead of weeks of manual work
- Run overnight and weekends
- Eliminate human error from repetitive clicking
- Test multiple scenarios simultaneously
- Collect data automatically

**Scripts Included**
1. mouse_cordinates.py — Find Button Coordinates

What it does: Identifies the exact pixel location of buttons in the testing interface.

Why you need it: The automation script needs to know exactly where to click (Verify button, Next button, close,etc.).

2. automate_mouse_program_cycle.py — Automate Test Cycles

What it does: Automatically clicks buttons at timed intervals to complete all program cycles without manual intervention.

Why you need it: Eliminates the need to manually click for days/weeks/months.

**An interesting application of this would be -  Game Farming Automation**
Repeatedly performing the same action in a game to collect resources, currency, or rewards automatically.
Instead of clicking manually hundreds or thousands of times, automation does it for you.
All you need to do this:
1.Change the loop count — for i in range(10000): to however many times you want to farm (e.g., for i in range(5000): for 5,000 harvests)
2.Change the wait time — time.sleep(1200) to match your game's cycle time in seconds (e.g., time.sleep(15) if each harvest takes 15 seconds, or time.sleep(1800) if it takes 30 minutes)
That's it! Everything else stays the same — the script will automatically farm for you :)
