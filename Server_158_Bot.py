import pyautogui
import time

# import other bots created
import Dungeon_Clear_Bot as DCB
import Tower_Clear_Bot as TCB
import Repeat_Hero_Mission as RHM
import Repeat_Same_Mission as RPM


def main_loop():
    TCB.main_loop() # Tower Clearing bot
    time.sleep(3)
    pyautogui.press('esc')
    pyautogui.press('esc')
    DCB.main_loop()  # Dungeon Clearing Bot
    time.sleep(3)
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.press('esc')
    RHM.main_loop()  # Hero Mission Clearing Bot
    time.sleep(3)
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(1)
    RPM.main_loop() # Repeating same mission several times
    time.sleep(3)
    pyautogui.press('esc')
    pyautogui.press('esc')




if __name__ == "__main__":
    main_loop()
