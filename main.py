import dearpygui.dearpygui as dpg
import json
import os

# Config Loading
cfgpath = "cfgV2.json"
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
        ],
        "pointsrequired": 2,
        "maxpointsrequired": 3,
        "minpointsrequired": 0
}
def LoadCfg(abc): # Loads the config, either default or .json
    global cfgdata
    if os.path.exists(cfgpath):
        with open(cfgpath, "r") as f:
           cfgdata = json.load(f)
    else:
        with open(cfgpath, "w") as f:
           json.dump(default_cfg, f, indent=4)
        print("Deleted cfg.json file detected, Please Configure It If It Is Outdated!")
        cfgdata = default_cfg
    if abc == "SetLoad":
        dpg.set_value("Points", cfgdata["pointsrequired"])
        LoadWindows(True)
LoadCfg(0)
def SaveCfg():
    cfgdata["pointsrequired"] = dpg.get_value("Points")
    with open(cfgpath, "w") as f:
        json.dump(cfgdata, f, indent=4)

# Suspect Finder
traittbl = {}
global temptbl
temptbl = {}
pointstbl = {}

def FindSuspect():
    global finalsuspects
    finalsuspects = None
    suspecttbl = {}
    for v in cfgdata["suspects"]:
        pointstbl[v["Name"]] = 0

    for plr in cfgdata["suspects"]:
        for trait in plr["Traits"]:
            if trait in traittbl:
                pointstbl[plr["Name"]] += 1
    for nome, points in pointstbl.items():
        if points not in suspecttbl:
            suspecttbl[points] = []
        if pointstbl[nome] >= cfgdata["pointsrequired"]:
            suspecttbl[points].append(nome)
    for i in range(cfgdata["maxpointsrequired"], 0, -1):
        if i in suspecttbl:
            for sussy in suspecttbl[i]:
                if i == cfgdata["maxpointsrequired"]:
                    finalsuspects = sussy
                print(f"{sussy} level {i}")

    dpg.set_value("Suspect", f"The Suspect Is: {finalsuspects}")


# GUI Generation
dpg.create_context()
with dpg.window(tag="CfgWindow", pos=[396, 0], autosize=True, label="Config"):
    pass
with dpg.window(tag="Primary Window"):
    pass

def OpenCfg():
    dpg.show_item("CfgWindow")

def traitalert(CallTrait):
    global temptbl
    if dpg.get_value(CallTrait) == True:
        traittbl[CallTrait] = True
    else:
        if CallTrait in traittbl:
            traittbl.pop(CallTrait)
    if temptbl != traittbl:
        FindSuspect()
        temptbl = traittbl.copy()

def LoadWindows(Destroy):
    if Destroy:
        dpg.delete_item("CfgWindow", children_only=True)
        dpg.delete_item("Primary Window", children_only=True)

    dpg.push_container_stack("CfgWindow")
    dpg.add_button(tag="SetLoad",label="Reload Config From File", callback=LoadCfg)
    dpg.add_button(label="Save Config To File", callback=SaveCfg)
    dpg.add_slider_int(tag="Points", label="Points Required To Show",
                        max_value=cfgdata["maxpointsrequired"], min_value=cfgdata["minpointsrequired"])
    dpg.set_value("Points", cfgdata["pointsrequired"])
    dpg.pop_container_stack()

    dpg.push_container_stack("Primary Window")
    dpg.add_button(label="Open Config", callback=OpenCfg)
    dpg.add_text("The Suspect Is: None", tag="Suspect")
    for obj in cfgdata["alltraits"]: # Creates A Checkbox For Each Trait
        dpg.add_checkbox(label=obj, tag=obj, callback=traitalert)
    dpg.pop_container_stack()
    dpg.set_primary_window("Primary Window", True)
LoadWindows(False)
dpg.create_viewport(title='Armless Detective Suspect Finder', width=800, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()