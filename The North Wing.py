# Andrew Biggs
# February 20, 2022

import time

# Nested Dictionary maps all rooms and their directional relationships.
# Special rooms: Lord's Court (START), Dungeon (END), Wizard's Chamber (Teleport)
room_moves = {
	"Lord's Court": {'N': "Southeast Courtyard"},
	"Southeast Courtyard": {'N': "Northeast Courtyard", 'W': "Southwest Courtyard"},
	"Northeast Courtyard": {'S': "Southeast Courtyard", 'W': "Northwest Courtyard", 'E': "Tower 1"},
	"Northwest Courtyard": {'N': "North Wing Anteroom", 'S': "Southwest Courtyard", 'E': "Northeast Courtyard"},
	"Southwest Courtyard": {'N': "Northwest Courtyard", 'W': "Dungeon Anteroom", 'E': "Southeast Courtyard"},
	"Tower 1": {'N': "Tower 2", 'W': "Northeast Courtyard"},
	"Tower 2": {'N': "Tower 3", 'S': "Tower 1"},
	"Tower 3": {'N': "Aerie", 'S': "Tower 2"},
	"Aerie": {'S': "Tower 3"},
	"North Wing Anteroom":
		{'N': "North Wing Corridor", 'S': "Northwest Courtyard", 'W': "West Antechamber", 'E': "East Antechamber"},
	"North Wing Corridor":
		{'N': "Wizard's Chamber", 'S': "North Wing Anteroom", 'W': "West Apartment", 'E': "East Apartment"},
	"West Antechamber": {'N': "West Apartment", 'E': "North Wing Anteroom"},
	"East Antechamber": {'N': "East Apartment", 'W': "North Wing Anteroom"},
	"West Apartment": {'S': "West Antechamber", 'E': "North Wing Corridor"},
	"East Apartment": {'S': "East Antechamber", 'W': "North Wing Corridor"},
	"Wizard's Chamber": {'S': "North Wing Corridor"},
	"Dungeon Anteroom": {'S': "Dungeon", 'E': "Southwest Courtyard"}
}
# Dictionary maps all pickup items to their rooms.
inv_items = {
	'Southeast Courtyard': 'Tower Key', 'Southwest Courtyard': 'Coin Purse',
	'Northeast Courtyard': 'Dungeon Key', 'Northwest Courtyard': 'Flint',
	'Tower 1': 'Copper Coin', 'Tower 2': 'Silver Coin',
	'Tower 3': 'Steel Coin', 'Aerie': 'Glass Coin',
	'Dungeon Anteroom': 'Dragon Scale'
}
# Dictionary maps all statuses of items and environment triggers
env_values = {
	# Environmental toggles (-1 or -2)
	"West Antechamber": -1, "East Antechamber": -1, "West Apartment": -1, "East Apartment": -1,
	"North Wing Anteroom": -1, "North Wing Corridor": -1,
	# Pickup item statuses (1 for picked up, 0 for still there)
	"Southeast Courtyard": 0, "Northeast Courtyard": 0, "Southwest Courtyard": 0, "Northwest Courtyard": 0,
	"Tower 1": 0, "Tower 2": 0, "Tower 3": 0, "Aerie": 0, "Dungeon Anteroom": 0, "Wizard's Chamber": 0,
	# Environmental trigger statuses (7 for activated, 3 for inactive)
	"North Wing Locked Door": 3, "Coin Purse": 3, "Game Over": 3,
	# Start and end rooms
	"Lord's Court": "Lord's Court", "Dungeon": "Dungeon"
}

pl_inventory = []  # Items collected are appended to this list
pl_location = ""  # Holds the name of the current room
user_in = None  # Placeholder for user input


def raw_input():
	"""Prints '> ' to console and accepts user input, returns user input as a string."""
	player_in = input('> ')
	return player_in


def view_inventory():
	"""Prints full inventory, one object per line"""
	if len(pl_inventory) > 0:
		for i in range(len(pl_inventory)):
			print(pl_inventory[i])
	else:
		print('Inventory is empty!')


def item_check(item):  # Returns True if item is in inventory, False if not
	if item in pl_inventory:
		return True
	else:
		return False


def game_intro():
	"""This function marks the beginning of the game (input and output) in the program."""
	global pl_location
	pl_location = "Lord's Court"
	print("You stand before the Lord and his inner circle. All wear black, hooded robes.")
	time.sleep(1.5)
	print("One of the hooded figures standing beside the throne speaks.")
	time.sleep(1.5)
	print("'Where the wind blows from every direction at once, fires clear the way.'")
	time.sleep(2)
	print("'That's all the Wizard ever left me to find him in a time of need,' says the Lord.")
	time.sleep(1.5)
	print("'But I have no idea what it means. To make matters worse...'")
	time.sleep(1.5)
	print("'It's only a matter of time before that dragon melts his way out of the Dungeon.'")
	time.sleep(1.5)
	print("'If you can help us, a great reward awaits you. I give you free roam of my fortress.'")
	print("'Take this with you.'")
	time.sleep(1.5)
	print("Clue added to inventory.")


def north_wing_lock():
	if env_values["West Antechamber"] == -2 and env_values["West Apartment"] == -2:
		if env_values["East Antechamber"] == -2 and env_values["East Apartment"] == -2:
			if env_values["North Wing Anteroom"] == -2 and env_values["North Wing Corridor"] == -2:
				env_values["North Wing Locked Door"] = 7
		else:
			if env_values["North Wing Anteroom"] == -2 or env_values["North Wing Corridor"] == -2:
				env_values["West Antechamber"] = -1
				env_values["East Antechamber"] = -1
				env_values["East Apartment"] = -1
				env_values["West Apartment"] = -1
				env_values["North Wing Anteroom"] = -1
				env_values["North Wing Corridor"] = -1
				print("You hear a loud *whooshing* sound then a *crunch* from every direction. The room goes dark.")
	else:
		if env_values["North Wing Anteroom"] == -2 or env_values["North Wing Corridor"] == -2:
			env_values["West Antechamber"] = -1
			env_values["East Antechamber"] = -1
			env_values["East Apartment"] = -1
			env_values["West Apartment"] = -1
			env_values["North Wing Anteroom"] = -1
			env_values["North Wing Corridor"] = -1
			print("You hear a loud *whooshing* sound then a *slam* from every direction. The room goes dark.")


def dragon_encounter():
	"""This function determines whether the player has collected every item;
	if yes, then the boss battle sequence ensues. Multiple game endings, depending on player input.
	If not all items have been collected, game ends with dragon defeating the player.
	"""
	global env_values
	print('You step into the darkness of the dungeon. Teeth and eyes reflect glints of light from the anteroom.')
	time.sleep(1)
	if 'Sword' not in pl_inventory or 'Glass Coin' not in pl_inventory or 'Copper Coin' not in pl_inventory or \
		'Silver Coin' not in pl_inventory or 'Steel Coin' not in pl_inventory:
		if 'Dragon Scale' in pl_inventory:
			print("'I smell a dragon but I see no treasure!' The Dragon shouts, and a fireball consumes you.")
		else:
			print("'You smell of my enemies!' The Dragon shouts before impaling you on one of his fangs.")
		env_values['Game Over'] = 7
	elif 'Dragon Scale' in pl_inventory:
		print("'Ah, I can't see you,' says the Dragon quietly. 'But I can smell you. Show me your face.'")
		time.sleep(1)
		print("You pull out the candle and the dragon breathes a miniscule fireball that catches on the wick.")
		time.sleep(1)
		print("'You solved my riddle,' the beast breathes through its cavernous nostrils.")
		time.sleep(1)
		print("'Now join me,' the creature growls. 'This kingdom was mine long before that petty Lord was here.'")
		time.sleep(1)
		print("The Dragon cranes his neck and turns his fist-sized eyeball toward you.")
		time.sleep(1)
		print("Ally with the Dragon? Y / N")
		reply = raw_input().upper()
		if reply == 'Y':
			print("You nod and drop your sword on the ground at its feet.")
			time.sleep(1.5)
			print("'Fool!' The Dragon cackles.")
			time.sleep(1)
			print("'Now, perish!'")
			time.sleep(.5)
			print("You reach for the only thing you have that resembles a weapon and pull the mirror out.")
			time.sleep(1)
			print("The Dragon sees his reflection in the mirror and gasps.")
			time.sleep(1)
			print("A steady stream of smoke begins to ascend from his nostrils. The creature begins to shrink in size.")
			time.sleep(1)
			print("A moment later, a Wizard slumps on the ground where the Dragon stood.")
			time.sleep(1)
			print("The guards rush in and take the Wizard. The Lord approaches you.")
			time.sleep(1)
			print("Thank you, adventurer! Our fief is saved!")
		else:
			print("You lunge and decapitate the Dragon with your sword!")
			time.sleep(2)
			print("The Dragon's body shrinks into a pile of clothes resembling sigils you saw in the Wizard's Chamber.")
			time.sleep(1)
			print("The guards rush in and take the clothes. The Lord approaches you.")
			time.sleep(1)
			print("Thank you, adventurer! Our fief is saved!")
	env_values['Game Over'] = 7


def action_prompts(room_name):
	"""This function prompts player for interaction with the various item types in the game."""
	global pl_inventory
	print("The current room is: {}.".format(room_name))
	time.sleep(1)
	# inventory item pickup prompts
	if env_values[room_name] == 0:
		print("Something catches your eye. You reach down and pick up {}.".format(inv_items[room_name]))
		print("Keep it? Y")
		action = raw_input()
		if action == 'Y' or action == 'y':
			if room_name == 'Tower 1' or room_name == 'Tower 2' or room_name == 'Tower 3' or room_name == 'Aerie':
				if item_check('Coin Purse'):
					pl_inventory.append(inv_items[room_name])
					env_values[room_name] = 1
					print('{} added to inventory'.format(inv_items[room_name]))
				else:
					print("You don't have anything to hold that!")
			else:
				pl_inventory.append(inv_items[room_name])
				env_values[room_name] = 1
		else:
			print('You leave the {} where you found it.'.format(inv_items[room_name]))
		time.sleep(1)
	# environmental toggles prompts
	elif env_values[room_name] == -1:
		if room_name == "North Wing Anteroom" or room_name == "North Wing Corridor":
			if "Flint" in pl_inventory:
				print("The torch isn't lit. Light the torch?")
				action = raw_input()
				if action == "Y" or action == "y":
					print("Torchlight illuminates the room.")
					env_values[room_name] = -2
					north_wing_lock()
				else:
					print("The room remains shrouded in shadows.")
			else:
				print("It's dark because the torch isn't lit.")
		elif room_name != "North Wing Anteroom" and room_name != "North Wing Corridor":
			print("The window is closed. Open the window?")
			action = raw_input()
			if action == 'Y' or action == 'y':
				print("You open the window, and an unusual summer chill blows into the room.")
				env_values[room_name] = -2
			else:
				print("You leave the window closed.")
		time.sleep(1)
	elif env_values[room_name] == -2:
		if room_name == "North Wing Anteroom" or room_name == "North Wing Corridor":
			print("The torch burns bright, lighting every corner of the room. Snuff the flame?")
			action = raw_input()
			if action == 'Y' or action == 'y':
				print("The room darkens in an instant.")
				env_values[room_name] = -1
			else:
				print("The fire continues to burn.")
		elif room_name != "North Wing Anteroom" and room_name != "North Wing Corridor":
			print("The window is open. Shut the window?")
			action = raw_input()
			if action == 'Y' or action == 'y':
				print("You close the window.")
				env_values[room_name] = -1
			else:
				print("From the open window, a light breeze continues to stir in the room.")
		time.sleep(1)
	elif env_values[room_name] == "Lord's Court":
		time.sleep(1)


def movement_prompts(room_name):
	"""This function determines output, given directional input and player's current location."""
	global pl_location
	print("Enter 'clue' to view the Wizard's cryptic message or try to exit the room by entering a direction...")
	time.sleep(.3)
	print("N / S / E / W")
	direction = raw_input().upper()
	if direction == 'N' or direction == 'S' or direction == 'E' or direction == 'W' or direction == 'CLUE':
		if direction == 'CLUE':
			print("'Where the wind blows from every direction at once, fires clear the way.'")
		elif direction in room_moves[room_name].keys():
			if room_moves[room_name][direction] == 'Tower 1':
				if item_check('Tower Key'):
					if room_name == 'Northeast Courtyard':
						print('You turn the key and enter the Tower.')
						pl_location = room_moves[room_name][direction]
						time.sleep(1)
					else:
						pl_location = room_moves[room_name][direction]
						time.sleep(1)
				else:
					print('The door is locked')
					time.sleep(.3)
			elif room_moves[room_name][direction] == 'Dungeon':
				if item_check('Dungeon Key'):
					print('You turn the key and enter the Dungeon')
					pl_location = room_moves[room_name][direction]
					dragon_encounter()
					return
				else:
					print('You feel the heat emanating from the dungeon, but the door is locked.')
					time.sleep(.3)
			elif room_moves[room_name][direction] == "Wizard's Chamber":
				if env_values['North Wing Locked Door'] == 7:
					print(
						'The door into the northernmost chamber opens on its own as you approach. You cross the threshold.')
					time.sleep(2)
					print('The room is filled with antique furniture.')
					time.sleep(2)
					print('There are small statuettes on the hutches and tables, hand-carved from wood, jade, or marble.')
					time.sleep(2)
					print('You pick up one of the small objects and inspect the fine, ancient paint on the figure.')
					time.sleep(2)
					print('Your attention is drawn to the North wall of the room, where what appears to be an altar stands.')
					time.sleep(2)
					print(
						'You approach the altar and find an immaculate mirror, an ornate sword and unburnt black candle in front.')
					time.sleep(5)
					print("""
					                 />
					                /<
					               /<
					     |/~~~~~~~{o}----------------------------------------------------------_
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
					time.sleep(6)
					print("You take the candle, mirror, and sword. The world fades to black as your consciousness slips.")
					pl_inventory.append("Sword")
					pl_inventory.append("Candle")
					pl_inventory.append("Mirror")
					pl_location = "Aerie"
					time.sleep(2)
				else:
					print('The door has no handle and is covered in an intricate lock apparatus.')
					time.sleep(.3)
				time.sleep(.3)
			else:
				print("You exit {}.".format(pl_location))
				pl_location = room_moves[room_name][direction]
				time.sleep(1)


# All seven North Wing area rooms have non-inventory items, which is part of a puzzle
# Open all four windows located in the east and west anterooms and apartments then light the torches

# Game Start
game_intro()
while env_values["Game Over"] == 3:
	action_prompts(pl_location)
	print("Inventory:{}".format(pl_inventory))
	movement_prompts(pl_location)
