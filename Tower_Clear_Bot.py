import pyautogui
import time
import os

# Give complete path of the folder where the relevant images are.  
current_directory = os.getcwd()
path_imagedata = current_directory + '/Tower_Clear_Data/'

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
   
def find_button(b_name,cnf):
    try:
    	pyautogui.locateCenterOnScreen(path_imagedata+b_name,confidence=cnf)
    	return 1
    except:
        return 0

def main_loop():
     a = 0
     click_button("Tower.png",0.7,wait=1)
     click_button("Tower_Inst_CLear.png",0.7,wait=1)
     click_button("Tower_Insta_CLear_Choose_Chests.png",0.7,wait=1)
     time.sleep(2)
     while a<7:
     	click_button("Tower_Chest_first.png",0.7,wait=1)
     	click_button("Open_Button.png",0.7,wait=1)
     	click_button("Proceed_Button.png",0.7,wait=1)
     	a = a + 1
     while(a<14):
     	click_button("Tower_Chest-2.png",0.7,wait=1)
     	click_button("Open_Button.png",0.7,wait=1)
     	click_button("Proceed_Button.png",0.7,wait=1)
     	a = a + 1
     click_button("Tower_Final_Chest.png",0.7,wait=1)
     click_button("Open_Button.png",0.7,wait=1)
     click_button("Cross_Button.png",0.7,wait=1)
     click_button("Tower_Points_Reward.png",0.7,wait=1)
     click_button("Tower_Collect_All_Point_reward.png",0.7,wait=1)
     click_button("Cross_Button-1.png",0.7,wait=1)
     click_button("Tower_Final_reward_1.png",0.7,wait=1)
     click_button("Exchange_Skull_Points_Reward.png",0.7,wait=1)
     
    	

# Determines wether running as main or module
# If you are running this script directly this the main.
if __name__ == "__main__":
    main_loop()
