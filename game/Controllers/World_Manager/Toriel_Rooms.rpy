init:
    #toriel house
    image background toriel_house_corridor = im.Scale("backgrounds/TorielsHouse/background-ruins-corridor.png",800,600)
    image background toriel_house_frisk_room = im.Scale("backgrounds/TorielsHouse/background-ruins-friskroom.png",800,600)
    image background toriel_house_kitchen = im.Scale("backgrounds/TorielsHouse/background-ruins-kitchen.png",800,600)
    image background toriel_house_livingroom = im.Scale("backgrounds/TorielsHouse/background-ruins-livingroom.png",800,600)
    image background toriel_house_staircase = im.Scale("backgrounds/TorielsHouse/background-ruins-staircase.png",800,600)
    image background toriel_house_toriel_room = im.Scale("backgrounds/TorielsHouse/background-ruins-torielroom.png",800,600)
    image background toriel_house_your_room = im.Scale("backgrounds/TorielsHouse/background-ruins-yourroom.png",800,600)
    image background toriel_house_corridor = im.Scale("backgrounds/TorielsHouse/background-ruins-corridor.png",800,600)


init python:
    
    class Toriel_House(Area):
        def __init__(self):
            Area.__init__(self,"Toriel House")
            self.add_room(th_staircase())
            self.add_room(th_corridor())
            self.add_room(th_kitchen())
            self.add_room(th_living_room())
            self.add_room(th_frisk_room())
            self.add_room(th_your_room())
            self.add_room(th_toriel_room())
            self.add_room(th_basement_door())
            self.add_room(toriel_house_to_ruins())


        def setup_breakfast_day2(self):


            return


    class th_staircase(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Staircase"
            self.x = 5
            self.y = 0
            self.desc = "This is the Stair case."
            self.bg = "background toriel_house_staircase"

    class th_basement_door(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Basement Door"
            self.x = 5
            self.y = 1
            self.lockeast = True
            self.lockwest = True
            self.desc = "This is the exit."
            


    class th_corridor(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Corridor"
            self.x = 6
            self.y = 0
            self.desc = "This is the hallway."
            self.bg = "background toriel_house_corridor"
            self.locknorth = False
            self.events['toriel_house_corridor'] = Event("toriel_house_corridor",True)

    class th_kitchen(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Kitchen"
            self.x = 4
            self.y = 1
            self.desc = "This is the kitchen."
            self.bg = "background toriel_house_kitchen"

    class th_living_room(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Living Room"
            self.x = 4
            self.y = 0
            self.desc = "This is the living room."
            self.bg = "background toriel_house_livingroom"

    class th_frisk_room(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Frisk's Room"
            self.x = 6
            self.y = 1
            self.desc = "This is Frisk's room."
            self.bg = "background toriel_house_frisk_room"
            self.locked = True

    class th_your_room(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Your Room"
            self.x = 6
            self.y = 1
            self.desc = "This is your room."
            self.bg = "background toriel_house_your_room"
            self.locked = True
            self.events['th_your_room'] = Event("th_your_room",True)

    class th_toriel_room(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Toriel's Room"
            self.x = 6
            self.y = 1
            self.desc = "This is toriel's room."
            self.bg = "background toriel_house_toriel_room"
            self.locked = True

    class toriel_house_to_ruins(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "TH Exit"
            self.x = 5
            self.y = -1
            self.desc = ""
            self.bg = ""
            self.mappable = False
            self.events["port_to_black_tree_room"] = Event("port_to_black_tree_room",True)
    
label port_to_black_tree_room:
    "The Ruins"
    $ world.move_to_room("Black Tree Room")
    
label player_sleeping_th:
    "You fall asleep in your bed."
    $ renpy.show(world.currentArea.currentRoom.bg)
    call player_waking_up from _call_player_waking_up
    return



label th_your_room:
    call show_buttons from _call_show_buttons_12
    if player.current_stamina <= 0:
        call player_waking_up from _call_player_waking_up_1
    pause
    menu:
        "Sleep" if player.current_stamina < player.max_stamina:
            call player_sleeping_th from _call_player_sleeping_th
        "Not Tired":
            return
    return

label toriel_house_corridor:
    call show_buttons from _call_show_buttons_13
    pause
    while True:
        menu:
            "There are three doors here."
            "Frisk's Room":
                if world.get_current_timezone() == "Night":
                    "The door is locked."
                else:
                    $ world.move_to_room("Frisk's Room")
            "Toriel's Room":
                if world.get_current_timezone() == "Night":
                    "The door is locked."
                else:
                    $ world.move_to_room("Toriel's Room")
            "Your Room":
                $ world.move_to_room("Your Room")
            "Exit":
                return
    return