import pyautogui
import time
import os


current_directory = os.getcwd()
path_imagedata = current_directory + '/Button_Images/'


def click_button(button_name, cnf, wait=0, wait_interval=2, max_wait=60):
    # Put Wait = 1 if needed or leave it as it is.
    if(wait == 1):
    	wait_button(button_name,cnf,wait_interval,max_wait)
    try:
        button_position = pyautogui.locateCenterOnScreen(path_imagedata+button_name,confidence=cnf)
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

def main_loop(dv_crd_tr=0):
    a = 0
    i = 0
    click_button('Daily_Quests_Button.png',0.6,wait=1)
    time.sleep(1)
    c_x, c_y = pyautogui.center( pyautogui.locateOnScreen(path_imagedata+'GoFor_Button.png',confidence=0.7) )
    while ((not(find_button('Guild_Dungeon_DQ_button.png',0.7))) and (i < 10)):
    	pyautogui.scroll(clicks=-1,x=c_x,y=c_y)
    	i= i + 1
    time.sleep(1)
    c_x, c_y = pyautogui.center( pyautogui.locateOnScreen(path_imagedata+'Guild_Dungeon_DQ_button.png',confidence=0.7) )
    pyautogui.click(x=c_x+440,y=c_y+17)
    time.sleep(4)

    #Checking For Devinition Card Usage
    if (dv_crd_tr == 1):
        click_button('Dungeon_Divination_Card_Button.png',0.7,wait=1)
        while(find_button('Dungeon_Divination_Card_Claim_Button.png',0.7)):
            click_button('Dungeon_Divination_Card_Claim_Button.png',0.7,wait=1)
            time.sleep(2)
        pyautogui.press('esc')
    dv_crd_us = 0
    
    while (a < 20):
        print(a)
        click_button('Dungeon_To_Battle.png',0.7,wait=1)
        time.sleep(2)
        if (dv_crd_tr == 1) and (dv_crd_us < 15):
            if(find_button('Attack.png', 0.7)):
                click_button('Attack.png', 0.7)
            click_button('Accept_this_Fate_Button.png', 0.7, wait=1)
            dv_crd_us = dv_crd_us + 1
        else:
            click_button('Attack.png', 0.7, wait=1, wait_interval=1)
            click_button('To_Battle_Button.png', 0.7, wait=1, wait_interval=1)
            click_button('Auto_Button_Unclicked_Dungeon.png', 0.5, wait=1, wait_interval=1)
            time.sleep(5)
            click_button('OK_Button.png', 0.7, wait=1, wait_interval=5)
        if (find_button('Activate_Dungeon_Button.png', 0.6)):
            click_button('Activate_Dungeon_Button.png', 0.6, wait=1)
            click_button('Collect_Dungeon_Button.png', 0.5, wait=1)

        a = a + 1


#Determines wether running as main or module
if __name__ == "__main__":
    a = bool(input("Please Enter 1 if you want to use divinition card: "))
    time.sleep(2)
    main_loop(a)
