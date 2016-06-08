init -1 python:
    
    random_rooms = []
    class th_staircase(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Staircase"
            self.x = 100
            self.y = 100
            self.desc = "Welcome to the prototype. Find your favorite character hiding in the house! (We are testing random events)"
            self.scene = "toriel_house_staircase"
            self.bg = "backgrounds/background-ruins-staircase.png"

    class th_corridor(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Corridor"
            self.x = 101
            self.y = 100
            self.desc = "This is the hallway."
            self.scene = "toriel_house_corridor"

    class th_kitchen(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Kitchen"
            self.x = 99
            self.y = 101
            self.desc = "This is the kitchen."
            self.scene = "toriel_house_kitchen"

    class th_living_room(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Living Room"
            self.x = 99
            self.y = 100
            self.desc = "This is the living room."
            self.scene = "toriel_house_living_room"

    class th_frisk_room(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Frisk's Room"
            self.x = 101
            self.y = 101
            self.desc = "This is Frisk's room."
            self.scene = "toriel_house_frisk_room"
            self.locked = True

    class th_your_room(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Your Room"
            self.x = 101
            self.y = 101
            self.desc = "This is your room."
            self.scene = "toriel_house_your_room"
            self.locked = True

    class th_toriel_room(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Toriel's Room"
            self.x = 101
            self.y = 101
            self.desc = "This is toriel's room."
            self.scene = "toriel_house_toriel_room"
            self.locked = True
    
    room_manager.add_room(th_staircase())
    room_manager.add_room(th_kitchen())
    room_manager.add_room(th_living_room())
    room_manager.add_room(th_corridor())
    room_manager.add_room(th_your_room())
    room_manager.add_room(th_frisk_room())
    room_manager.add_room(th_toriel_room())
    
    room_manager.current_room = room_manager.rooms[0]
    
label toriel_house_corridor:
    scene background toriel_house_corridor
    while True:
        menu:
            "There are three doors here."
            "Frisk's Room":
                jump toriel_house_frisk_room
            "Toriel's Room":
                jump toriel_house_toriel_room
            "This one has a paw on it. You hear typing.":
                if wilson_locked:
                    "The door knob won't turn.  Surely there is some objective to this?"
                else:
                    jump toriel_house_your_room
    return


label toriel_house_kitchen:
    scene background toriel_house_kitchen
    with fade
    if random_rooms.count(room_manager.current_room.name) == 0:
        $ random_rooms.append(room_manager.current_room.name)
        $ chance = room_manager.get_random_scene()
        if chance:
            $ renpy.call_in_new_context(chance)
        "[room_manager.current_room.desc]"
    return
    
label toriel_house_living_room:
    scene background toriel_house_livingroom
    with fade
    if random_rooms.count(room_manager.current_room.name) == 0:
        $ random_rooms.append(room_manager.current_room.name)
        $ chance = room_manager.get_random_scene()
        if chance:
            $ renpy.call_in_new_context(chance)
    while True:
        "[room_manager.current_room.desc]"
    return
    
label toriel_house_staircase :
    scene background toriel_house_staircase
    with fade
    "[room_manager.current_room.desc]"
    call screen test_screen
    return
    
label toriel_house_toriel_room:
    $ room_manager.move_to_room("Toriel's Room") 
    scene background toriel_house_toriel_room
    with fade
    if random_rooms.count(room_manager.current_room.name) == 0:
        $ random_rooms.append(room_manager.current_room.name)
        $ chance = room_manager.get_random_scene()
        if chance:
            $ renpy.call_in_new_context(chance)

    while True:
        "[room_manager.current_room.desc]"
    return
    
label toriel_house_your_room:
    $ room_manager.move_to_room("Your Room") 
    scene background toriel_house_your_room
    with fade
    $ renpy.call_in_new_context("wilson_label")
    jump the_end


label toriel_house_frisk_room:
    $ room_manager.move_to_room("Frisk's Room") 
    scene background toriel_house_frisk_room
    with fade
    if random_rooms.count(room_manager.current_room.name) == 0:
        $ random_rooms.append(room_manager.current_room.name)
        $ chance = room_manager.get_random_scene()
        if chance:
            $ renpy.call_in_new_context(chance)
    while True:
        "[room_manager.current_room.desc]"
    return
    


label toriel_random:
    show toriel placeholder
    with moveinbottom
    toriel "BOO"
    toriel "This is a random scene!"
    toriel "Ewe never know where they are!"
    hide toriel ph
    with moveoutbottom
    return

label flowey_random:
    show flowey placeholder
    with moveinbottom
    flowey "HOWDY"
    flowey "We are hidden at random in the house."
    flowey "Sometimes we might even be in a room you've been in!"
    flowey "Watching...."
    hide flowey ph
    with moveoutbottom
    return

label papyrus_random:
    show papyrus surprised
    with moveinbottom
    papyrus "....."
    hide papyrus surprised
    show papyrus suspicious
    papyrus "Spaghetti?"
    hide papyrus suspicious
    with moveoutbottom
    return

label sans_random:
    show sans normal
    with moveinbottom
    sans "Brah"
    hide sans normal
    show sans medium at Position(xpos=0.5, ypos=1.5)
    sans "Help"
    hide sans medium
    show sans large at Position (xpos=0.5, ypos=3.5)
    with hpunch
    sans "Me."
    hide sans large
    
    return

label wilson_label:
    
    show wilson down at Position(xpos=0.7,ypos=0.75)
    show papyrus disgust at right
    stop music
    play music 'audio/Nyeh_Heh_Heh.MP3'
    wilson "So if sphaghetti==1 then pap needs to go. yeah that will work."
    play sound "audio/typing.wav"
    wilson "<type type type type>"
    hide papyrus disgust
    with dissolve
    show papyrus bigsmile at right
    with dissolve
    papyrus "Hello Wilson!"
    papyrus "You are my best fend! We should go on date with spaghetti! Like papyrus would!"
    wilson "Fend?!?! <growl> That's not right...."
    play sound "audio/typing.wav"
    wilson "<type type type>"
    stop sound
    wilson "{cps=1}...{/cps}"
    hide wilson down
    stop music
    show wilson up at Position(xpos=0.7,ypos=0.75)
    wilson "......"
    wilson "how {cps=2}long have you"
    hide papyrus bigsmile
    hide wilson down
    show wilson large
    with vpunch
    wilson "{size=+20}OMG GET OUT!!!!!!"

    hide wilson down
    return
label wilson_unlock:
    "You hear a click from across the hallway. Is there someone else here?"
    $ wilson_locked = False
    
    return