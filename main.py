#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "55010BC9-FE20-4B0A-B484-CF4FE84235DC",
  "name": "Interactive Story",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631460200064,
  "passages": [
    {
      "name": "White Room",
      "tags": "",
      "id": "1",
      "text": "You have awaken in a large white room. \nAround you there are five white walls with five doors all distinctly different from each other. \nThere is a: \n\n[[DOOR A -> Red Door]] \n[[DOOR B -> Orange Door]]\n[[DOOR C -> Yellow Door]]\n[[DOOR D -> Green Door]]\n[[DOOR e -> Black Door]]\n[[ Middle of Room]]",
      "links": [
        {
          "linkText": "Red Door",
          "passageName": "Red Door",
          "original": "[[DOOR A -> Red Door]]"
        },
        {
          "linkText": "Orange Door",
          "passageName": "Orange Door",
          "original": "[[DOOR B -> Orange Door]]"
        },
        {
          "linkText": "Yellow Door",
          "passageName": "Yellow Door",
          "original": "[[DOOR C -> Yellow Door]]"
        },
        {
          "linkText": "Green Door",
          "passageName": "Green Door",
          "original": "[[DOOR D -> Green Door]]"
        },
        {
          "linkText": "Black Door",
          "passageName": "Black Door",
          "original": "[[DOOR e -> Black Door]]"
        },
        {
          "linkText": "Check Room",
          "passageName": "Middle of Room",
          "original": "[[ Middle of Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "You have awaken in a large white room. \nAround you there are five white walls with five doors all distinctly different from each other."
    },
    {
      "name": " Red Door",
      "tags": "",
      "id": "2",
      "text": "The red door is a bright shimmery red. The look and smell reminds you of strawberries. \n\n[[INSIDE -> Red Room]]\n[[BACK ->White Room]] \n[[DOOR B -> Orange Door]]\n[[DOOR C -> Yellow Door]]\n[[DOOR D -> Green Door]]\n[[DOOR E -> Black Door]]\n[[ Middle of Room]]",
      "links": [
        {
          "linkText": "INSIDE",
          "passageName": "Red Room",
          "original": "[[INSIDE -> Red Room]]"
        },
        {
          "linkText": "BACK",
          "passageName": "White Room",
          "original": "[[BACK ->White Room]]"
        },
        {
          "linkText": "DOOR B",
          "passageName": "Orange Door",
          "original": "[[DOOR B -> Orange Door]]"
        },
        {
          "linkText": "DOOR C",
          "passageName": "Yellow Door",
          "original": "[[DOOR C -> Yellow Door]]"
        },
        {
          "linkText": "DOOR D",
          "passageName": "Green Door",
          "original": "[[DOOR D -> Green Door]]"
        },
        {
          "linkText": "DOOR E",
          "passageName": "Black Door",
          "original": "[[DOOR E -> Black Door]]"
        },
        {
          "linkText": "Middle of Room",
          "passageName": "Middle of Room",
          "original": "[[ Middle of Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "The red door is a bright shimmery red. The look and smell reminds you of strawberries."
    },
    {
      "name": " Orange Door",
      "tags": "",
      "id": "3",
      "text": "The orange door is covered in stickers of different oragned things, like oranges, goldfirsh, plants. You think it is a bit childish.\n\n[[DOOR A -> Red Door]]\n[[DOOR C -> Yellow Door]]\n[[DOOR D -> Green Door]]\n[[DOOR E -> Black Door]]\n[[ Middle of Room]] \n[[ORANGE ROOM -> orange room]]",
      "links": [
        {
          "linkText": "DOOR A",
          "passageName": "Red Door",
          "original": "[[DOOR A -> Red Door]]"
        },
        {
          "linkText": "DOOR C",
          "passageName": "Yellow Door",
          "original": "[[DOOR C -> Yellow Door]]"
        },
        {
          "linkText": "DOOR D",
          "passageName": "Green Door",
          "original": "[[DOOR D -> Green Door]]"
        },
        {
          "linkText": "DOOR E",
          "passageName": "Black Door",
          "original": "[[DOOR E -> Black Door]]"
        },
        {
          "linkText": "Middle of Room",
          "passageName": "Middle of Room",
          "original": "[[ Middle of Room]]"
        },
        {
          "linkText": "ORANGE ROOM",
          "passageName": "orange room",
          "original": "[[ORANGE ROOM -> orange room]]"
        }
      ],
      "hooks": [],
      "cleanText": "The orange door is covered in stickers of different oragned things, like oranges, goldfirsh, plants. You think it is a bit childish."
    },
    {
      "name": " Yellow Door",
      "tags": "",
      "id": "4",
      "text": "The yellow door is a muted mustard color. It seems like the wood is old. \n\n[[DOOR A -> Red Door]]\n[[DOOR B -> Orange Door]]\n[[DOOR D -> Green Door]]\n[[DOOR E -> Black Door]]\n[[Yellow room]]",
      "links": [
        {
          "linkText": "DOOR A",
          "passageName": "Red Door",
          "original": "[[DOOR A -> Red Door]]"
        },
        {
          "linkText": "DOOR B",
          "passageName": "Orange Door",
          "original": "[[DOOR B -> Orange Door]]"
        },
        {
          "linkText": "DOOR D",
          "passageName": "Green Door",
          "original": "[[DOOR D -> Green Door]]"
        },
        {
          "linkText": "DOOR E",
          "passageName": "Black Door",
          "original": "[[DOOR E -> Black Door]]"
        },
        {
          "linkText": "Yellow room",
          "passageName": "Yellow room",
          "original": "[[Yellow room]]"
        }
      ],
      "hooks": [],
      "cleanText": "The yellow door is a muted mustard color. It seems like the wood is old."
    },
    {
      "name": " Green Door",
      "tags": "",
      "id": "5",
      "text": "The greed door is a mint color. It heavily smells of cleaning products and soap.\n\n[[DOOR A -> Red Door]]\n[[DOOR B -> Orange Door]]\n[[DOOR C -> Yellow Door]]\n[[DOOR E -> Black Door]]\n[[Green Room]]",
      "links": [
        {
          "linkText": "DOOR A",
          "passageName": "Red Door",
          "original": "[[DOOR A -> Red Door]]"
        },
        {
          "linkText": "DOOR B",
          "passageName": "Orange Door",
          "original": "[[DOOR B -> Orange Door]]"
        },
        {
          "linkText": "DOOR C",
          "passageName": "Yellow Door",
          "original": "[[DOOR C -> Yellow Door]]"
        },
        {
          "linkText": "DOOR E",
          "passageName": "Black Door",
          "original": "[[DOOR E -> Black Door]]"
        },
        {
          "linkText": "Green Room",
          "passageName": "Green Room",
          "original": "[[Green Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "The greed door is a mint color. It heavily smells of cleaning products and soap."
    },
    {
      "name": " Black Door",
      "tags": "",
      "id": "6",
      "text": "The door is covered in five different locks. Each lock is color coded to the other doors in the room. \nGetting close to the door, you hear something moving on the other side.\n\n[[DOOR A -> Red Door]]\n[[DOOR B -> Orange Door]]\n[[DOOR C -> Yellow Door]]\n[[DOOR D -> Green Door]]\n[[OPEN -> Outside]]\n[[ Middle of Room]]",
      "links": [
        {
          "linkText": "DOOR A",
          "passageName": "Red Door",
          "original": "[[DOOR A -> Red Door]]"
        },
        {
          "linkText": "DOOR B",
          "passageName": "Orange Door",
          "original": "[[DOOR B -> Orange Door]]"
        },
        {
          "linkText": "DOOR C",
          "passageName": "Yellow Door",
          "original": "[[DOOR C -> Yellow Door]]"
        },
        {
          "linkText": "DOOR D",
          "passageName": "Green Door",
          "original": "[[DOOR D -> Green Door]]"
        },
        {
          "linkText": "OPEN",
          "passageName": "Outside",
          "original": "[[OPEN -> Outside]]"
        },
        {
          "linkText": "Middle of Room",
          "passageName": "Middle of Room",
          "original": "[[ Middle of Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "The door is covered in five different locks. Each lock is color coded to the other doors in the room. \nGetting close to the door, you hear something moving on the other side."
    },
    {
      "name": " Red Room",
      "tags": "",
      "id": "7",
      "text": "Inside the red room, you spot a bed, a table, chairs, a painting of a strawberry and on the farthest wall, there was a window that lead into a seperate room.\nOn the table there is a small plate with an apple and cheese. \n\n[[DOOR A -> Red Door]]\n[[WINDOW -> Window]]",
      "links": [
        {
          "linkText": "DOOR A",
          "passageName": "Red Door",
          "original": "[[DOOR A -> Red Door]]"
        },
        {
          "linkText": "WINDOW",
          "passageName": "Window",
          "original": "[[WINDOW -> Window]]"
        }
      ],
      "hooks": [],
      "cleanText": "Inside the red room, you spot a bed, a table, chairs, a painting of a strawberry and on the farthest wall, there was a window that lead into a seperate room.\nOn the table there is a small plate with an apple and cheese."
    },
    {
      "name": " Window",
      "tags": "",
      "id": "8",
      "text": "You pear into the window.\nLooking in you see a room completely identical to the on you are in currently. However, on the table inside the room there is a red key. \n\n[[Dangerous]]\n[[Safe]]",
      "links": [
        {
          "linkText": "Dangerous",
          "passageName": "Dangerous",
          "original": "[[Dangerous]]"
        },
        {
          "linkText": "Safe",
          "passageName": "Safe",
          "original": "[[Safe]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pear into the window.\nLooking in you see a room completely identical to the on you are in currently. However, on the table inside the room there is a red key."
    },
    {
      "name": " Adjacent Red Room",
      "tags": "",
      "id": "9",
      "text": "Inside you grab the key and head back to the previous room.\n\n[[Dangerous]]\n[[Safe]]",
      "links": [
        {
          "linkText": "Dangerous",
          "passageName": "Dangerous",
          "original": "[[Dangerous]]"
        },
        {
          "linkText": "Safe",
          "passageName": "Safe",
          "original": "[[Safe]]"
        }
      ],
      "hooks": [],
      "cleanText": "Inside you grab the key and head back to the previous room."
    },
    {
      "name": " Outside",
      "tags": "",
      "id": "10",
      "text": "You open the door and find yourself outside. You have won the game.",
      "links": [],
      "hooks": [],
      "cleanText": "You open the door and find yourself outside. You have won the game."
    },
    {
      "name": " Middle of Room",
      "tags": "",
      "id": "11",
      "text": "In the center of the room, you find a table to with a black key.\n\n[[DOOR A -> Red Door]]\n[[DOOR B -> Orange Door]]\n[[DOOR C -> Yellow Door]]\n[[DOOR D -> Green Door]]\n[[DOOR E -> Black Door]]\n[[White Room]]",
      "links": [
        {
          "linkText": "DOOR A",
          "passageName": "Red Door",
          "original": "[[DOOR A -> Red Door]]"
        },
        {
          "linkText": "DOOR B",
          "passageName": "Orange Door",
          "original": "[[DOOR B -> Orange Door]]"
        },
        {
          "linkText": "DOOR C",
          "passageName": "Yellow Door",
          "original": "[[DOOR C -> Yellow Door]]"
        },
        {
          "linkText": "DOOR D",
          "passageName": "Green Door",
          "original": "[[DOOR D -> Green Door]]"
        },
        {
          "linkText": "DOOR E",
          "passageName": "Black Door",
          "original": "[[DOOR E -> Black Door]]"
        },
        {
          "linkText": "White Room",
          "passageName": "White Room",
          "original": "[[White Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "In the center of the room, you find a table to with a black key."
    },
    {
      "name": " orange room",
      "tags": "",
      "id": "12",
      "text": "Inside, you find room filled with plants of all kind. There are mainly orange plants, but there are a few other species. \n\n[[ Orange Door]] \n[[crawl space]]",
      "links": [
        {
          "linkText": "Orange Door",
          "passageName": "Orange Door",
          "original": "[[ Orange Door]]"
        },
        {
          "linkText": "crawl space",
          "passageName": "crawl space",
          "original": "[[crawl space]]"
        }
      ],
      "hooks": [],
      "cleanText": "Inside, you find room filled with plants of all kind. There are mainly orange plants, but there are a few other species."
    },
    {
      "name": "crawl space",
      "tags": "",
      "id": "13",
      "text": "You find a small crawl space on the right side of the room. Inside there are a small pile of books with different sticky note sticking out of them. \n\n[[ orange room]]",
      "links": [
        {
          "linkText": "orange room",
          "passageName": "orange room",
          "original": "[[ orange room]]"
        }
      ],
      "hooks": [],
      "cleanText": "You find a small crawl space on the right side of the room. Inside there are a small pile of books with different sticky note sticking out of them."
    },
    {
      "name": "Yellow room",
      "tags": "",
      "id": "14",
      "text": "Inside you find a small library of books. There are a few tables with lamps. There is a computer in the center of the room. \n\n[[ Yellow Door]] \n[[Computer]]",
      "links": [
        {
          "linkText": "Yellow Door",
          "passageName": "Yellow Door",
          "original": "[[ Yellow Door]]"
        },
        {
          "linkText": "Computer",
          "passageName": "Computer",
          "original": "[[Computer]]"
        }
      ],
      "hooks": [],
      "cleanText": "Inside you find a small library of books. There are a few tables with lamps. There is a computer in the center of the room."
    },
    {
      "name": "Green Room",
      "tags": "",
      "id": "15",
      "text": "Inside is a storage closest, filled with cleaning products, mops, brooms, and a bucket. There is also a small sink on the farthest wall. \n\nThere is also a tool kit on one of the sheleves.\n\n[[ Green Door]] \n[[Chemical]]\n[[sink]]\n[[shelf]]",
      "links": [
        {
          "linkText": "Green Door",
          "passageName": "Green Door",
          "original": "[[ Green Door]]"
        },
        {
          "linkText": "Chemical",
          "passageName": "Chemical",
          "original": "[[Chemical]]"
        },
        {
          "linkText": "sink",
          "passageName": "sink",
          "original": "[[sink]]"
        },
        {
          "linkText": "shelf",
          "passageName": "shelf",
          "original": "[[shelf]]"
        }
      ],
      "hooks": [],
      "cleanText": "Inside is a storage closest, filled with cleaning products, mops, brooms, and a bucket. There is also a small sink on the farthest wall. \n\nThere is also a tool kit on one of the sheleves."
    },
    {
      "name": "Dangerous",
      "tags": "",
      "id": "16",
      "text": "When trying to get through the window, you find that you have accidentally cut yourself. The wound is pretty deep. \n\nYou end up bleeding to death. The color of your blood, matches the same color as the room.",
      "links": [],
      "hooks": [],
      "cleanText": "When trying to get through the window, you find that you have accidentally cut yourself. The wound is pretty deep. \n\nYou end up bleeding to death. The color of your blood, matches the same color as the room."
    },
    {
      "name": "Safe",
      "tags": "",
      "id": "17",
      "text": "You make it through the window safely. \n\n[[Room A.2 -> Adjacent Red Room]]\n[[ Red Room]]",
      "links": [
        {
          "linkText": "Room A.2",
          "passageName": "Adjacent Red Room",
          "original": "[[Room A.2 -> Adjacent Red Room]]"
        },
        {
          "linkText": "Red Room",
          "passageName": "Red Room",
          "original": "[[ Red Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "You make it through the window safely."
    },
    {
      "name": "Computer",
      "tags": "",
      "id": "18",
      "text": "You turn on the computer and find a log in screen. The hint states, where are you now page 41.\n\n[[Fail]]\n[[SUCESS]]",
      "links": [
        {
          "linkText": "Fail",
          "passageName": "Fail",
          "original": "[[Fail]]"
        },
        {
          "linkText": "SUCESS",
          "passageName": "SUCESS",
          "original": "[[SUCESS]]"
        }
      ],
      "hooks": [],
      "cleanText": "You turn on the computer and find a log in screen. The hint states, where are you now page 41."
    },
    {
      "name": "Fail",
      "tags": "",
      "id": "19",
      "text": "You have failed unlocking the computer. Game Over.",
      "links": [],
      "hooks": [],
      "cleanText": "You have failed unlocking the computer. Game Over."
    },
    {
      "name": "SUCESS",
      "tags": "",
      "id": "20",
      "text": "You sucessfully log into the computer.\n\n[[Lock Box]]",
      "links": [
        {
          "linkText": "Lock Box",
          "passageName": "Lock Box",
          "original": "[[Lock Box]]"
        }
      ],
      "hooks": [],
      "cleanText": "You sucessfully log into the computer."
    },
    {
      "name": "Lock Box",
      "tags": "",
      "id": "21",
      "text": "You click a button on the computer, and a switch clicks on. You see a key inside the box.\n\n[[Green Room]] \n[[ Green Door]]",
      "links": [
        {
          "linkText": "Green Room",
          "passageName": "Green Room",
          "original": "[[Green Room]]"
        },
        {
          "linkText": "Green Door",
          "passageName": "Green Door",
          "original": "[[ Green Door]]"
        }
      ],
      "hooks": [],
      "cleanText": "You click a button on the computer, and a switch clicks on. You see a key inside the box."
    },
    {
      "name": "Chemical",
      "tags": "",
      "id": "22",
      "text": "You decided to drink the chemicals on the shelf. \\\n\nYou started coughing up blood, and are slowly passing out from the pain. Game over.",
      "links": [],
      "hooks": [],
      "cleanText": "You decided to drink the chemicals on the shelf. \\\n\nYou started coughing up blood, and are slowly passing out from the pain. Game over."
    },
    {
      "name": "sink",
      "tags": "",
      "id": "23",
      "text": "You observe the sink. Inside the drain is a key. You are unable to reach it. You need a tool to grab the key.\n\n[[Green Room]] \n[[shelf]]\n[[drain]]",
      "links": [
        {
          "linkText": "Green Room",
          "passageName": "Green Room",
          "original": "[[Green Room]]"
        },
        {
          "linkText": "shelf",
          "passageName": "shelf",
          "original": "[[shelf]]"
        },
        {
          "linkText": "drain",
          "passageName": "drain",
          "original": "[[drain]]"
        }
      ],
      "hooks": [],
      "cleanText": "You observe the sink. Inside the drain is a key. You are unable to reach it. You need a tool to grab the key."
    },
    {
      "name": "shelf",
      "tags": "",
      "id": "24",
      "text": "On the shelf you see a tool kit, chemicals, and other cleaning products.\n\n[[Chemical]] \n[[sink]]",
      "links": [
        {
          "linkText": "Chemical",
          "passageName": "Chemical",
          "original": "[[Chemical]]"
        },
        {
          "linkText": "sink",
          "passageName": "sink",
          "original": "[[sink]]"
        }
      ],
      "hooks": [],
      "cleanText": "On the shelf you see a tool kit, chemicals, and other cleaning products."
    },
    {
      "name": "drain",
      "tags": "",
      "id": "25",
      "text": "You use the wrench to open up the drain and grab the key.\n\n[[Green Room]] \n[[ Green Door]]",
      "links": [
        {
          "linkText": "Green Room",
          "passageName": "Green Room",
          "original": "[[Green Room]]"
        },
        {
          "linkText": "Green Door",
          "passageName": "Green Door",
          "original": "[[ Green Door]]"
        }
      ],
      "hooks": [],
      "cleanText": "You use the wrench to open up the drain and grab the key."
    }
  ]
}
#-----------------------------------------------------------------
import time
print("You awaken in a Large white room with multiple doors in front of you. Each door is distinctly different from each other in color, texture, and style. The building has many secrets surrounding it and it is up to you to find all of them and escape.")
print("Use your imagination along with the items around you to find your way out.")
print("Good Luck!")
time.sleep(1)
print("")
# ----------------------------------------------------------------
current = "White Room"
response = ""
while True:
    if response == "quit":
        break

    current_location = {}
    for passage in world["passages"]:
      if passage["name"] == current:
        current_location = passage

    print(current_location["name"])
    print(current_location["cleanText"])
    for link in current_location["links"]:
      print(link["linkText"])

response = input("What would you like to do? ")
for link in current_location["links"]:
      if response == link["links"]:
        current = link["passageName"]
#-------------------------------------------------------------
