# North Wing
# An interactive text game

import time

# Declaring variables

Current_room = str
SW_window, NW_window, SE_window, NE_window = 0, 0, 0, 0
S_torch, N_torch = 0, 0
Action = str
Door_choice = 0
Game_Over = 0

# Introduction to game
enter_North_Wing = input("Enter the North Wing? Y / N")
if enter_North_Wing == 'Y':
	Current_room = 'S_corr'
	time.sleep(2)
else:
	quit()

# doorchoice: functions that will be repeated, to move from one room to another in the North Wing
# function will be called depending on which room player currently occupies
def doorchoice_S_corr():
	print("Which door do you want to go through? N / S / E / W")
	global Current_room
	global Door_choice
	action = input()
	if action == 'S':
		print("If you leave now, your progress will be lost. Leave the North Wing? Y / N")
		action = input()
		if action == 'Y':
			Door_choice = 1
			quit()

	elif action == 'N':
		print("You proceed through the door at the North end of the corridor.")
		Current_room = 'N_corr'
		Door_choice = 1
	elif action == 'W':
		print("You proceed through the door to the West.")
		Current_room = 'SW_room'
		Door_choice = 1
	elif action == 'E':
		print("You proceed through the door to the East.")
		Current_room = 'SE_room'
		Door_choice = 1


def doorchoice_SW_room():
	print("Which door do you want to go through: North or East? N / E")
	global Current_room
	global Door_choice
	action = input()
	if action == 'E':
		print("You proceed through the door to the East.")
		Current_room = 'S_corr'
		Door_choice = 1
	elif action == 'N':
		print("You proceed through the door to the North.")
		Current_room = 'NW_room'
		Door_choice = 1


def doorchoice_NW_room():
	print("Which door do you want to go through: North, South, or East? N / S / E")
	global Current_room
	global Door_choice
	action = input()
	if action == 'E':
		print("You proceed through the door to the East.")
		Current_room = 'N_corr'
		Door_choice = 1
	elif action == 'N':
		print("You try to proceed through the door to the North, but find a brick wall behind it.")
		Door_choice = 0
		time.sleep(2)
	elif action == 'S':
		print("You proceed through the door to the South.")
		Current_room = 'SW_room'
		Door_choice = 1


def doorchoice_N_corr():
	print("Which door do you want to go through? N / S / E / W")
	global Current_room
	global Door_choice
	action = input()
	if action == 'N' and Game_Over == 1:
		print('You pull the door open and walk through the threshold at the North end of the corridor.')
		Current_room = 'N_room'
		Door_choice = 1
	elif action == 'N':
		print('You pull on the handle but the door is locked tight.')
	elif action == 'S':
		print('You proceed through the door to the South, into another corridor.')
		Current_room = 'S_corr'
		Door_choice = 1
	elif action == 'E':
		print('You proceed through the door into the room to the East.')
		Current_room = 'NE_room'
		Door_choice = 1
	elif action == 'W':
		print('You proceed through the door into the room to the West.')
		Current_room = 'NW_room'
		Door_choice = 1


def doorchoice_NE_room():
	print("Which door do you want to go through: North, South, or West? N / S / W")
	global Current_room
	global Door_choice
	action = input()
	if action == 'N':
		print("You try to proceed through the door to the North, but find a brick wall behind it.")
		Door_choice = 0
		time.sleep(2)
	elif action == 'S':
		print('You proceed into the room to the South.')
		Current_room = 'SE_room'
		Door_choice = 1
	elif action == 'W':
		print('You proceed into the corridor to the West.')
		Current_room = 'N_corr'
		Door_choice = 1


def doorchoice_SE_room():
	print('Which door do you want to go through? N / W')
	global Current_room
	global Door_choice
	action = input()
	if action == 'N':
		print('You proceed through the door into the room to the North.')
		Current_room = 'NE_room'
		Door_choice = 1
	elif action == 'W':
		print('You proceed through the door to the West.')
		Current_room = 'S_corr'
		Door_choice = 1


# functions to be called when player enters a room or corridor
def S_corr():
	global Door_choice
	global S_torch
	global Action
	Door_choice = 0
	Action = ''
	print("You stand in a corridor. Doors are to the West, North, East, and South and a torch sits in the middle of the"
	      " corridor.")
	if S_torch == 0:
		print("The torch is unlit. Light the torch? Y / N")
		Action = input()
		if Action == 'Y':
			S_torch = 1
			print("The torch illuminates the room.")
		else:
			print("The corridor remains dark.")
	elif S_torch == 1:
		print("The torch is lit. Extinguish the flame? Y / N")
		Action = input()
		if Action == 'Y':
			S_torch = 0
			print("You snuff the flame and the room sinks into darkness.")
		else:
			print("The fire continues to illuminate the room.")
	while Door_choice == 0:
		doorchoice_S_corr()


def SW_room():
	global Door_choice
	global SW_window
	global Action
	Door_choice = 0
	Action = ''
	print('You stand in a room.')
	print("There are doors on both the North and East walls and a window on the West wall.")
	if SW_window == 0:
		print("The window is closed. Do you want to open it? Y / N")
		Action = input()
		if Action == 'Y':
			SW_window = 1
			print("You open the window.")
		else:
			print("You leave the window closed.")
	elif SW_window == 1:
		print("The window is open. Close it? Y / N")
		Action = input()
		if Action == 'Y':
			SW_window = 0
			print("You shut the window.")
		else:
			print("The window remains open.")
	while Door_choice == 0:
		doorchoice_SW_room()


def NW_room():
	global Door_choice
	global NW_window
	global Action
	Door_choice = 0
	Action = ''
	print('You stand in a room.')
	print("There are doors on the North, South, and East walls and a window on the West wall.")
	if NW_window == 0:
		print("The window is closed. Do you want to open it? Y / N")
		Action = input()
		if Action == 'Y':
			NW_window = 1
			print("You open the window.")
		else:
			print("You leave the window closed.")
	elif NW_window == 1:
		print("The window is open. Close it? Y / N")
		Action = input()
		if Action == 'Y':
			NW_window = 0
			print("You shut the window.")
		else:
			print("The window remains open.")

	while Door_choice == 0:
		doorchoice_NW_room()


def N_corr():
	global Door_choice
	global N_torch
	global Action
	global NE_window
	global NW_window
	global SE_window
	global SW_window
	global S_torch
	global Game_Over
	Door_choice = 0
	Action = ''
	print("You stand in a corridor. Doors are to the West, North, East, and South and a torch sits in the middle of the"
	      " corridor.")
	if N_torch == 0:
		print("The torch is unlit. Light the torch? Y / N")
		Action = input()
		if Action == 'Y':
			N_torch = 1
			print("The torch illuminates the room.")
		else:
			print("The corridor remains dark.")
	elif N_torch == 1:
		print("The torch is lit. Extinguish the flame? Y / N")
		Action = input()
		if Action == 'Y':
			N_torch = 0
			print("You snuff the flame and the room sinks into darkness.")
		else:
			print("The fire continues to illuminate the room.")
	if N_torch == 1 and S_torch == 1 and SW_window == 1 and SE_window == 1 and NE_window == 1 and NW_window == 1:
		print("You hear latches moving in the door on the North wall.")
		Game_Over = 1
	elif N_torch == 1 and S_torch == 0 and SW_window == 1 and SE_window == 1 and NE_window == 1 and NW_window == 1:
		print("You feel drawn to the South.")
	elif N_torch == 1:
		N_torch, S_torch, NW_window, NE_window, SW_window, SE_window = 0, 0, 0, 0, 0, 0
		print("You feel a gust of wind and hear slamming sounds coming from every direction, then silence.")

	while Door_choice == 0:
		doorchoice_N_corr()


def SE_room():
	global Door_choice
	global SE_window
	global Action
	Door_choice = 0
	Action = ''
	print('You stand in a room.')
	print("There are doors on both the North and West walls and a window on the East wall.")
	if SE_window == 0:
		print("The window is closed. Do you want to open it? Y / N")
		Action = input()
		if Action == 'Y':
			SE_window = 1
			print("You open the window.")
		else:
			print("You leave the window closed.")
	elif SE_window == 1:
		print("The window is open. Close it? Y / N")
		Action = input()
		if Action == 'Y':
			SE_window = 0
			print("You shut the window.")
		else:
			print("The window remains open.")
	while Door_choice == 0:
		doorchoice_SE_room()


def NE_room():
	global Door_choice
	global NE_window
	global Action
	Door_choice = 0
	Action = ''
	print("There are doors on the North, South, and West walls and a window on the East wall.")
	if NE_window == 0:
		print("The window is closed. Do you want to open it? Y / N")
		Action = input()
		if Action == 'Y':
			NE_window = 1
			print("You open the window.")
		else:
			print("You leave the window closed.")
	elif NE_window == 1:
		print("The window is open. Close it? Y / N")
		Action = input()
		if Action == 'Y':
			NE_window = 0
			print("You shut the window.")
		else:
			print("The window remains open.")

	while Door_choice == 0:
		doorchoice_NE_room()


def N_room():
	print('The room is filled with antique furniture.')
	time.sleep(2)
	print('There are small statuettes on the hutches and tables, hand-carved from wood, jade, or marble.')
	time.sleep(2)
	print('You pick up one of the small objects and inspect the fine, ancient paint on the figure.')
	time.sleep(2)
	print('Your attention is drawn to the North wall of the room, where what appears to be an altar stands.')
	time.sleep(2)
	print('You approach the altar and find an immaculate mirror, an ornate sword and unburnt black candle in front.')
	time.sleep(5)
	print("""
                 />
                /<
               /<
     |/_______{o}----------------------------------------------------------_
    [///////////{*}:::<=============================================-       >
     |/~~~~~~~{o}----------------------------------------------------------~
               \<
                \<
                 \>
    """)
	time.sleep(6.7)
	print("""       
         (
        /)
       {_}
      .-;-.
     |'-=-'|
     |     |
     |     |
     |     |
     |     |
     '.___.'""")
	time.sleep(3)
	print('Thanks for playing North Wing!')
	time.sleep(3)
	print('Closing app. . .')
	time.sleep(7)

while Current_room != 'N_room':
	if Current_room == 'N_corr':
		N_corr()
	elif Current_room == 'S_corr':
		S_corr()
	elif Current_room == 'NE_room':
		NE_room()
	elif Current_room == 'NW_room':
		NW_room()
	elif Current_room == 'SE_room':
		SE_room()
	elif Current_room == 'SW_room':
		SW_room()
if Current_room == 'N_room':
	N_room()
