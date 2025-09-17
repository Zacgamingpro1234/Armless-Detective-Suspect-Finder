import json
import os

cfgpath = "cfg.json"
default_cfg = { # The default config to be used if not config file is found
        "suspects": [
            {"Name": "Charles", "Traits": ["Sheds hair oftenly", "Writes in their diary", "Likes to clean"]},
            {"Name": "Nancy", "Traits": ["Has no Robux", "Writes in their diary", "Likes to clean"]},
            {"Name": "Oliver", "Traits": ["Has no Robux", "Writes in their diary", "Cold-blooded"]},
            {"Name": "Clara", "Traits": ["Bad at hiding their fingerprints", "Cold-blooded", "Has no Robux"]},
            {"Name": "Sophia", "Traits": ["Eats lots of food", "Sheds hair oftenly", "Bad at hiding their fingerprints"]},
            {"Name": "Trey", "Traits": ["Eats lots of food", "Cold-blooded", "Has no Robux"]},
            {"Name": "Junior", "Traits": ["Sheds hair oftenly", "Cold-blooded", "Has no Robux"]},
            {"Name": "Buck", "Traits": ["Writes in their diary", "Eats lots of food", "Bad at hiding their fingerprints"]},
            {"Name": "Donald", "Traits": ["Likes to clean", "Eats lots of food", "Bad at hiding their fingerprints"]},
            {"Name": "Susan", "Traits": ["Sheds hair oftenly", "Bad at hiding their fingerprints", "Cold-blooded"]},
            {"Name": "Betty", "Traits": ["Likes to clean", "Sheds hair oftenly", "Has no Robux"]},
            {"Name": "Thomas", "Traits": ["Likes to clean", "Eats lots of food", "Cold-blooded"]},
            {"Name": "David", "Traits": ["Likes to clean", "Sheds hair oftenly", "Cold-blooded"]},
            {"Name": "Linda", "Traits": ["Writes in their diary", "Bad at hiding their fingerprints", "Cold-blooded"]},
            {"Name": "Mary", "Traits": ["Writes in their diary", "Eats lots of food", "Cold-blooded"]},
            {"Name": "James", "Traits": ["Writes in their diary", "Sheds hair oftenly", "Cold-blooded"]},
            {"Name": "Matthew", "Traits": ["Writes in their diary", "Sheds hair oftenly", "Has no Robux"]},
            {"Name": "Kyle", "Traits": ["Eats lots of food", "Bad at hiding their fingerprints", "Cold-blooded"]},
            {"Name": "Herbert", "Traits": ["Likes to clean", "Sheds hair oftenly", "Bad at hiding their fingerprints"]},
            {"Name": "Rebecca", "Traits": ["Writes in their diary", "Bad at hiding their fingerprints", "Has no Robux"]},
            {"Name": "Sara", "Traits": ["Likes to clean", "Bad at hiding their fingerprints", "Has no Robux"]},
            {"Name": "Bob", "Traits": ["Likes to clean", "Eats lots of food", "Has no Robux"]},
            {"Name": "Jimbo", "Traits": ["Writes in their diary", "Eats lots of food", "Has no Robux"]},
            {"Name": "William", "Traits": ["Likes to clean", "Eats lots of food", "Sheds hair oftenly"]},
        ],

        "alltraits": [
            "Sheds hair oftenly", "Writes in their diary", "Likes to clean", "Has no Robux",
            "Cold-blooded", "Bad at hiding their fingerprints", "Eats lots of food"
        ]              
}

def LoadCfg(): # Loads the config, either default or .json
    if os.path.exists(cfgpath):
        with open(cfgpath, "r") as f:
           return json.load(f)
    else:
        with open(cfgpath, "w") as f:
           json.dump(default_cfg, f, indent=4)
    print("Deleted cfg.json file detected, Please Configure It If It Is Outdated!")
    return default_cfg

def FindClues(): # Gets all clues
    traitable = cfgdata["alltraits"]
    clues = {}
    for trait in traitable:
       print("Suspect, " + trait)
       ipt = input()
       if ipt == "y":
        clues[trait] = True    
    return clues

def FindSuspect(clues: dict): # Find the suspect with the given clues
   suspect = []
   suspects = cfgdata["suspects"]
   for plrindex, person in enumerate(suspects):
      istraited = [False, False, False]
      for index, plrtrait in enumerate(person["Traits"]): # A list of the plrs traits
         for clue in clues: # A list of the found clues
            if clue == plrtrait:
               istraited[index] = True
         if istraited[index] == False:
             break
      if istraited[0] and istraited[1] and istraited[2]:
         suspect.append([plrindex ,person["Name"]])
   return suspect

def start():
   global cfgdata
   cfgdata = LoadCfg()
   clues = FindClues()
   suspectable = FindSuspect(clues)
   if len(suspectable) == 0:
      print("No Suspect Found, Or Too Little Clues Given")
   for suspect in suspectable:
      print(f"And the suspect is: No°{suspect[0]+1} {suspect[1]}")

start()
while True:
   print("")
   print("Again?")
   again = input()
   if again == "y":
         start()
   else:
    break