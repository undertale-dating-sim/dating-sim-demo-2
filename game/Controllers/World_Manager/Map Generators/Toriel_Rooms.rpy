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
            self.desc = "* The entrance to Toriel's house splits off in three directions.  A wide, nondescript staircase leads down into some kind of basement."
            self.bg = "background toriel_house_staircase"

    class th_basement_door(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Basement Door"
            self.x = 5
            self.y = 1
            self.lockeast = True
            self.lockwest = True
            self.desc = "* A large, ornate door stands before you.  It feels cold and impersonal."
            


    class th_corridor(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Corridor"
            self.x = 6
            self.y = 0
            self.desc = "* The otherwise boring hallway is spruced up with potted plant life everywhere you look.  There's a mirror at the end of the hall. It lookslike it could use a cleaning, as there are fingerprints smudging the reflective surface."
            self.bg = "background toriel_house_corridor"
            self.locknorth = False
            self.events['toriel_house_corridor'] = Event("toriel_house_corridor",True)
            self.plant_watered_times = 0
            self.day_watered = 0

    class th_kitchen(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Kitchen"
            self.x = 4
            self.y = 1
            self.lockeast = True
            self.desc = "* There's a freshly cooked pie on the counter, and it appears that someone has already taste-tested it.  There are no knives in any of the drawers... but then how did the taste-tester cut the pie?"
            self.bg = "background toriel_house_kitchen"

    class th_living_room(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Living Room"
            self.x = 4
            self.y = 0
            self.desc = "* The living room is always cozy and warm, probably because the fire in the fireplace never seems to dim.  There are old-looking pictures on the walls of people you don't recognize."
            self.bg = "background toriel_house_livingroom"

    class th_frisk_room(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Frisk's Room"
            self.x = 6
            self.y = 1
            self.desc = "* The bed is made, the papers on the desk are neatly stacked, and the many miscellaneous items on the shelves are straight and facing forward.  Whoever lives in the room must like to keep it tidy."
            self.bg = "background toriel_house_frisk_room"
            self.locked = True

    class th_your_room(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Your Room"
            self.x = 6
            self.y = 1
            self.desc = "* There's a couple of moving boxes in the corner which are covered in a fine layer of dust.  It seems like someone made an attempt to make the room look more homely, but you still get the sense that it's been left empty for a long time."
            self.bg = "background toriel_house_your_room"
            self.locked = True
            self.events['th_your_room'] = Event("th_your_room",True)

    class th_toriel_room(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Toriel's Room"
            self.x = 6
            self.y = 1
            self.desc = "* Looks like a pretty normal master bedroom... except for the bucket of snails in the corner."
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
    $ renpy.show(world.current_area.current_room.bg)
    call player_waking_up from _call_player_waking_up
    return



label th_your_room:
    call show_buttons from _call_show_buttons_12
    pause
    menu:
        "Sleep":
            return
        "Not Tired":
            return
    return

label toriel_house_corridor:
    call show_buttons from _call_show_buttons_13
    pause
    while True:
        menu:
            "There are three doors here."
            "Golden flower":
                call golden_flower_event
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