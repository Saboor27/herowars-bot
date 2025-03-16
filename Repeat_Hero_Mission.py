import pyautogui
import time
import os

# Give complete path of the folder where the relevant images are.
current_directory = os.getcwd()
path_imagedata = current_directory + '/Button_Images/'


# Click Button
def click_button(button_name, cnf, wait=0, wait_interval=2, max_wait=60):
    # Put Wait = 1 if needed or leave it as it is.
    if(wait == 1):
    	wait_button(button_name,cnf,wait_interval,max_wait)
    try:
        button_position = pyautogui.locateCenterOnScreen(path_imagedata + button_name,confidence=cnf)
        pyautogui.click(button_position)
        time.sleep(2)  # Wait for the action to complete
        return 1
    except TypeError:
        print("Image not found on the screen.")
        return 0


def wait_button(button_name, cnf=0.7, interval=2, max_wait=60):
    i = 0
    while (i < max_wait):
    	try:
    	    pyautogui.locateCenterOnScreen(path_imagedata+button_name, confidence=cnf)
    	    i = max_wait
    	except:
    	    time.sleep(interval)
    	    i = i + interval

def main_loop():
    a=0
    click_button('Campaign_Button.png', 0.7, wait=1)
    click_button('Move_Left_Button_C15.png', 0.501, wait=1)
    click_button('Move_Left_Button_C14.png', 0.501, wait=1)
    while (a < 3):
    	click_button('CH13_Hero_Mission_4.png', 0.7, wait=1)
    	click_button('Start_Button.png', 0.7, wait=1)
    	click_button('To_Battle_Button.png', 0.7, wait=1)
    	print(a)
    	time.sleep(45)
    	click_button('Continue_Button.png', 0.7, wait=1, wait_interval=5)
    	a = a + 1

    # Add more tasks as needed

#Determines wether running as main or modeule
if __name__ == "__main__":
    main_loop()
