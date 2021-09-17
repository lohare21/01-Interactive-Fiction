#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "6DAD02A6-38B3-4BA2-A65A-E917D43936B9",
  "name": "Interactive Story 2",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631819306835,
  "passages": [
    {
      "name": "White Room",
      "tags": "",
      "id": "1",
      "text": "You awaken in a a large white room, with four doors on each wall. Each door is a various color. You are not sure how you got there, but you sure need to get out. \n\n[[Red Door]]\n[[Orange Door]]\n[[Yellow Door]]\n[[Green Door]]",
      "links": [
        {
          "linkText": "Red Door",
          "passageName": "Red Door",
          "original": "[[Red Door]]"
        },
        {
          "linkText": "Orange Door",
          "passageName": "Orange Door",
          "original": "[[Orange Door]]"
        },
        {
          "linkText": "Yellow Door",
          "passageName": "Yellow Door",
          "original": "[[Yellow Door]]"
        },
        {
          "linkText": "Green Door",
          "passageName": "Green Door",
          "original": "[[Green Door]]"
        }
      ],
      "hooks": [],
      "cleanText": "You awaken in a a large white room, with four doors on each wall. Each door is a various color. You are not sure how you got there, but you sure need to get out."
    },
    {
      "name": "Red Door",
      "tags": "",
      "id": "2",
      "text": "The Red Door seems slightly odd as if it is warping towards you. One of the hinges is missing and is sitting slightly at an angle. \n\n[[Red Room]]\n[[White Room]]",
      "links": [
        {
          "linkText": "Red Room",
          "passageName": "Red Room",
          "original": "[[Red Room]]"
        },
        {
          "linkText": "White Room",
          "passageName": "White Room",
          "original": "[[White Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "The Red Door seems slightly odd as if it is warping towards you. One of the hinges is missing and is sitting slightly at an angle."
    },
    {
      "name": "Orange Door",
      "tags": "",
      "id": "3",
      "text": "The Orange Door has a small peep hole in the top center of the door. You feel as if you are being watched. \n\n[[Orange Room]]\n[[Peep Hole]]\n[[White Room]]",
      "links": [
        {
          "linkText": "Orange Room",
          "passageName": "Orange Room",
          "original": "[[Orange Room]]"
        },
        {
          "linkText": "Peep Hole",
          "passageName": "Peep Hole",
          "original": "[[Peep Hole]]"
        },
        {
          "linkText": "White Room",
          "passageName": "White Room",
          "original": "[[White Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "The Orange Door has a small peep hole in the top center of the door. You feel as if you are being watched."
    },
    {
      "name": "Yellow Door",
      "tags": "",
      "id": "4",
      "text": "The Yellow Door is a warm yellow. It seems inviting.\n\n[[Yellow Room]]\n[[White Room]]",
      "links": [
        {
          "linkText": "Yellow Room",
          "passageName": "Yellow Room",
          "original": "[[Yellow Room]]"
        },
        {
          "linkText": "White Room",
          "passageName": "White Room",
          "original": "[[White Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "The Yellow Door is a warm yellow. It seems inviting."
    },
    {
      "name": "Green Door",
      "tags": "",
      "id": "5",
      "text": "The green door seems the most normal out of all of them. There is nothing special about the green door, but there is still something not right about the norality of the door.\n\n[[Green Room]]\n[[White Room]]",
      "links": [
        {
          "linkText": "Green Room",
          "passageName": "Green Room",
          "original": "[[Green Room]]"
        },
        {
          "linkText": "White Room",
          "passageName": "White Room",
          "original": "[[White Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "The green door seems the most normal out of all of them. There is nothing special about the green door, but there is still something not right about the norality of the door."
    },
    {
      "name": "Red Room",
      "tags": "",
      "id": "6",
      "text": "Walking in, you hear the door shut behind you. You try the handle and it is locked. You are now trapped inside. You end up starving to death. \n\nHungry? Game Over",
      "links": [],
      "hooks": [],
      "cleanText": "Walking in, you hear the door shut behind you. You try the handle and it is locked. You are now trapped inside. You end up starving to death. \n\nHungry? Game Over"
    },
    {
      "name": "Orange Room",
      "tags": "",
      "id": "7",
      "text": "Stepping into the Orange Room, You find that it leads to two additional doors. One of them has to be the way out. \n\n[[Blue Door]]\n[[Purple Door]]",
      "links": [
        {
          "linkText": "Blue Door",
          "passageName": "Blue Door",
          "original": "[[Blue Door]]"
        },
        {
          "linkText": "Purple Door",
          "passageName": "Purple Door",
          "original": "[[Purple Door]]"
        }
      ],
      "hooks": [],
      "cleanText": "Stepping into the Orange Room, You find that it leads to two additional doors. One of them has to be the way out."
    },
    {
      "name": "Peep Hole",
      "tags": "",
      "id": "8",
      "text": "You decide to look through the peep hole. Inside you see a person looking straight back at you. This scared you to the point where you had a heart attack. \n\nI guess you didn't have the heart to go in. Game Over",
      "links": [],
      "hooks": [],
      "cleanText": "You decide to look through the peep hole. Inside you see a person looking straight back at you. This scared you to the point where you had a heart attack. \n\nI guess you didn't have the heart to go in. Game Over"
    },
    {
      "name": "Yellow Room",
      "tags": "",
      "id": "9",
      "text": "Once you enter, You find the floor is covered in water. You trigger a trip roap and a plugged in toaster falls into the water. You die from electrocution.\n\nThat was pretty shocking! Game Over",
      "links": [],
      "hooks": [],
      "cleanText": "Once you enter, You find the floor is covered in water. You trigger a trip roap and a plugged in toaster falls into the water. You die from electrocution.\n\nThat was pretty shocking! Game Over"
    },
    {
      "name": "Green Room",
      "tags": "",
      "id": "10",
      "text": "Once you enter the green room, you notice you begin to feel extremly tired. Turns out the room was filled with poisonous gas. \n\nAt least it didn't explode. Game Over",
      "links": [],
      "hooks": [],
      "cleanText": "Once you enter the green room, you notice you begin to feel extremly tired. Turns out the room was filled with poisonous gas. \n\nAt least it didn't explode. Game Over"
    },
    {
      "name": "Blue Door",
      "tags": "",
      "id": "11",
      "text": "This door smells of the Sea and Salt. You hear waves crashing behind the door. \n\n[[Blue Room]]",
      "links": [
        {
          "linkText": "Blue Room",
          "passageName": "Blue Room",
          "original": "[[Blue Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "This door smells of the Sea and Salt. You hear waves crashing behind the door."
    },
    {
      "name": "Purple Door",
      "tags": "",
      "id": "12",
      "text": "On the wood trim of the door, there are tiny images of Dragons all around. That isn't alarming...\n\n[[Orange Room]] \n[[Purple Room]]",
      "links": [
        {
          "linkText": "Orange Room",
          "passageName": "Orange Room",
          "original": "[[Orange Room]]"
        },
        {
          "linkText": "Purple Room",
          "passageName": "Purple Room",
          "original": "[[Purple Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "On the wood trim of the door, there are tiny images of Dragons all around. That isn't alarming..."
    },
    {
      "name": "Purple Room",
      "tags": "",
      "id": "13",
      "text": "Infront of you is a single black door. This has to be the way out.\n\n[[Black door]]",
      "links": [
        {
          "linkText": "Black door",
          "passageName": "Black door",
          "original": "[[Black door]]"
        }
      ],
      "hooks": [],
      "cleanText": "Infront of you is a single black door. This has to be the way out."
    },
    {
      "name": "Black door",
      "tags": "",
      "id": "14",
      "text": "This is it, the last door. Open it to find out what is on the other side. \n\n[[Open -> Outside]]",
      "links": [
        {
          "linkText": "Open",
          "passageName": "Outside",
          "original": "[[Open -> Outside]]"
        }
      ],
      "hooks": [],
      "cleanText": "This is it, the last door. Open it to find out what is on the other side."
    },
    {
      "name": "Outside",
      "tags": "",
      "id": "15",
      "text": "You finally did, you made it outside. Congrats. You win.",
      "links": [],
      "hooks": [],
      "cleanText": "You finally did, you made it outside. Congrats. You win."
    },
    {
      "name": "Blue Room",
      "tags": "",
      "id": "16",
      "text": "Once inside, you are standin in a large pool. However, you are not alone. In the water there are five sharks hungry and looking for a meal. Luckily you happened to stop by. \n\nFish Bait. Game Over",
      "links": [],
      "hooks": [],
      "cleanText": "Once inside, you are standin in a large pool. However, you are not alone. In the water there are five sharks hungry and looking for a meal. Luckily you happened to stop by. \n\nFish Bait. Game Over"
    }
  ]
}
#-----------------------------------------------------------------
import time
print("You awaken in a Large white room with multiple doors in front of you. Each door is distinctly different from each other in color. There is only one exit to each area, so be careful of the door you choose.")
print("Good Luck!")
time.sleep(3)
print("")
# ----------------------------------------------------------------
def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}
# ----------------------------------------------------------------

def render(current_location, score, moves):
	if "name" in current_location and "cleanText" in current_location:
		print("Moves: " + str(moves) + ", Score: " + str(score))
		print("You are at the " + str(current_location["name"]))
		print(current_location["cleanText"] + "\n")

def get_input():
	response = input("What do you want to do? ")
	response = response.upper().strip()
	return response

def update(current_location, location_label, response):
	if response == "":
		return location_label
	if "links" in current_location:
		for link in current_location["links"]:
			if link["linkText"].upper() == response:
				return link["passageName"]
	print("I don't understand what you are trying to do. Try again.")
	return location_label


# ----------------------------------------------------------------

location_label = "White Room"
current_location = {}
response = ""
score = 0
moves = 0

while True:
	if response == "QUIT":
		break
	moves += 1
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	if "score" in current_location:
		score = score + current_location["score"]
	render(current_location, score, moves)
	if current_location["name"] == "Exit":
		break
	response = get_input()

print("Thanks for playing!")
