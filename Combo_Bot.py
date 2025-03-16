# import libraries
import pyautogui
import time

# import the other bots created
import Repeat_Hero_Mission as RHM
import Repeat_Same_Mission as RPM




def main_loop():
    RHM.main_loop()
    RPM.wait_button('Continue_Button.png',0.7,interval=5)
    RPM.click_button('Continue_Button.png',0.7)
    pyautogui.press('esc')
    RPM.main_loop()



# Determines wether running as main or module
if __name__ == "__main__":
    main_loop()
