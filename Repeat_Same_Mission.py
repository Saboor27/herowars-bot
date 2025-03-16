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

# Wait for the button to appear
def wait_button(button_name, cnf=0.7, interval=2, max_wait=60):
    i = 0
    while (i < max_wait):
    	try:
    	    pyautogui.locateCenterOnScreen(path_imagedata + button_name, confidence=cnf)
    	    i = max_wait
    	except:
    	    time.sleep(interval)
    	    i = i + interval

# Get the location of the button on screen
def get_coordinates(button_name, cnf):
    c_x, c_y = pyautogui.center( pyautogui.locateOnScreen(path_imagedata + button_name, confidence=cnf) )
    return (c_x, c_y)

# Find the button wether it is on the screen
def find_button(b_name,cnf):
    try:
    	pyautogui.locateCenterOnScreen(path_imagedata+b_name,confidence=cnf)
    	return 1
    except:
        return 0

# Move to the chapter where required mission is.
def mov_to_ch():
    click_button('Campaign_Button.png', 0.7,wait=1)
    time.sleep(2)
    c_x, c_y = get_coordinates('Move_Left_Button_C15.png', 0.46)
    for i in range(7):
    	pyautogui.click(x=c_x, y=c_y)
    	time.sleep(3)

def main_loop(max_rep=124):
    a = 0
    mov_to_ch()
    while (a < max_rep):
        if (not find_button('Ch8_AntharacitePalace_Mission.png', 0.7)):
            if find_button('Continue_Button.png', 0.7):
                click_button('Continue_Button.png', 0.7, wait=1)
        click_button('Ch8_AntharacitePalace_Mission.png', 0.7, wait=1)
        click_button('Start_Button.png', 0.7, wait=1)
        click_button('To_Battle_Button.png', 0.7, wait=1)
        time.sleep(10)
        click_button('Continue_Button.png', 0.7, wait=1, wait_interval=5, max_wait=120)
        a = a + 1
        # After 50 iterartions of the mission reload game. You can delete next 10 lines if you don't want to reload the game.
        if (a%50) == 0:    
            pyautogui.press('F5') 
            time.sleep(60)
            pyautogui.press('esc')
            pyautogui.press('esc')
            pyautogui.press('esc')
            if(find_button('Cross_Button_1.png',0.7)):
                click_button('Cross_Button_1.png', 0.7)
                time.sleep(1)
            mov_to_ch()
        print(a)
    # Add more tasks as needed

# Determines wether running as main or module
if __name__ == "__main__":
    reps = int(input("No of times the mission shall be repeated:  "))
    time.sleep(4)
    main_loop(reps)
