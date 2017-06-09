init:
#flowerbed
    image background ruins_caveroom = im.Scale("backgrounds/Ruins/background-ruins-flowerpatch.jpg",800,600)
    image background ruins_floweyroom = im.Scale("backgrounds/Ruins/background-ruins-floweyroom.jpg",800,600)

#the ruins
    image background ruins_outside_house = im.Scale("backgrounds/Ruins/background-ruins-blacktree.png",800,600)
    image background ruins_froggit_room = im.Scale("backgrounds/Ruins/background-ruins-froggitroom.jpg",800,600)
    image background ruins_first_entrance = im.Scale("backgrounds/Ruins/background-ruins-firstentrance.jpg",800,600)
    image background ruins_toy_knife_room = im.Scale("backgrounds/Ruins/background-ruins-toykniferoom.jpg",800,600)
    image background ruins_spider_bakery = im.Scale("backgrounds/Ruins/background-ruins-spiderbakery.jpg",800,600)
    image background ruins_sassyrock_room = im.Scale("backgrounds/Ruins/background-ruins-sassyrock.jpg",800,600)
    image background ruins_blooky_room = im.Scale("backgrounds/Ruins/background-ruins-blookyroom.jpg",800,600)
    image background ruins_dummy_room = im.Scale("backgrounds/Ruins/background-ruins-dummyroom.jpg",800,600)
    image background ruins_hallway = im.Scale("backgrounds/Ruins/background-ruins-hallway.jpg",800,600)
    image background ruins_monstercandy_room = im.Scale("backgrounds/Ruins/Monster-Candy-Room-Sketch.jpg",800,600)
    image background ruins_snailhunting_room = im.Scale("backgrounds/Ruins/Secret-Garden-Final.jpg",800,600)
    image background deadroom = im.Scale("backgrounds/gaster.png",800,600)

init -1 python:
    
    class TheRuins(Area):
        def __init__(self):
            Area.__init__(self,"The Ruins")
            self.random_areas = []
            self.random_monsters = [Loox(),Vegetoid(),Moldsmol(),Whimsun(),Migosp(),Froggit()]
            self.random_events = [Event("whimsun_re_start",False),Event("dummy_ruins_random_event_start",False),Event("vegetoid_ruins_re_start",False),Event("froggit_loox_ss_start",False)]
            self.add_room(ruins_caveroom())
            self.add_room(ruins_grassroom())
            self.add_room(ruins_ruinsentrance())
            self.add_room(dead_room())
            self.add_room(ruins_tunnels())
            self.add_room(ruins_dummyroom())
            self.add_room(ruins_froggitleaves())
            self.add_room(ruins_sassyrock())
            self.add_room(ruins_blookyroom())
            self.add_room(ruins_spiderbakery())
            self.add_room(ruins_snailhuntingroom())
            self.add_room(ruins_monstercandyroom())
            self.add_room(ruins_tunneldivide())
            self.add_room(ruins_overlook())
            self.add_room(ruins_blacktreeroom())
            self.add_room(ruins_to_toriel_house())
            

    class dead_room(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Dead Room"
            self.x = -666
            self.y = -666
            self.desc = "You shouldn't be here."
            self.visited = True
            self.bg = "background deadroom"
            #self.events["dead_room"] = Event("dead_room",True)
            self.mappable = False
            self.add_monster(Flowey())
            self.add_monster(Toriel())
            self.add_monster(Frisk())
            self.add_monster(Napstablook())
            
            
            
            
    class ruins_caveroom(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Cave Room"
            self.x = 10
            self.y = 0
            self.desc = "* The cavern is lit by a light from far above. It shines into the dark corners of the cave, illuminating the patch of flowers that broke your fall. A large, ornate doorway is the only exit."
            self.bg = "background ruins_caveroom"
            

            

    class ruins_grassroom(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Grass Room"
            self.x = 9
            self.y = 0
            self.desc = "* Mounds of trash litter the edges of the small cave. The sparse light which floods through a crack in the ceiling reveals a small mound of grass in the center of the cavern. There is one exit... but it seems to be covered by a curtain of vines. "
            self.bg = "background ruins_floweyroom"
           



    class ruins_ruinsentrance(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Ruins Entrance"
            self.x = 9
            self.y = 1
            self.desc = "* The floor of the stone hallway is covered in red leaves that gather in drifts in the corners and scatter across the path, leading to a set of curving staircases. The stairs climb up to a landing that supports a large, ivy-covered building. Its entrance yawns darkly and is flanked by two high windows."
            self.bg = "background ruins_first_entrance"
            


    class ruins_tunnels(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Tunnels"
            self.x = 9
            self.y = 2
            self.desc = "* The tunnels criss-crossing in and out of the various rooms that you pass through are riddled with what appear to be disabled traps and puzzles."
            self.bg = "background ruins_hallway"
           


    class ruins_dummyroom(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Dummy Room"
            self.x = 9
            self.y = 3
            self.desc = "* The small, curved room has a much lower ceiling than the caves before it. An arched doorway leads on to further rooms."
            self.bg = "background ruins_dummy_room"

    class ruins_froggitleaves(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Froggit Room"
            self.x = 10
            self.y = 3
            self.desc = "* The bricked hall zig-zags its way around several large piles of red leaves, passing walls hung with flourishing ivy plants and leading to the exit at the far end of the room."
            self.bg = "background ruins_froggit_room"
  
    class ruins_sassyrock(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Sassy Rock Room"
            self.x = 11
            self.y = 3
            self.desc = "* The room before you is long and filled with odd items. There is a sign hanging on the wall closest to you. Three grey rocks sit on top of strange square pads on the ground, and a moat crosses the opposite side of the hall. A short bridge extends across the still water. There is an exit across the bridge."
            self.bg = "background ruins_sassyrock_room"

    class ruins_blookyroom(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Blooky Room"
            self.x = 12
            self.y = 3
            self.desc = "* The room is average sized and is divided by a wall halfway through that separates the side of the room you are on from two exits on the other side. There is a narrow opening in the wall, its floor covered with a scattering of red leaves."
            self.bg = "background ruins_blooky_room"

    class ruins_spiderbakery(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Spider Bakery"
            self.x = 13
            self.y = 3
            self.desc = "* The room is small and full of cobwebs. A sign proclaims that this is the Spider Bake Sale, which is evident by the donuts and bottles of cider stuck in the webs around you."
            self.bg = "background ruins_spider_bakery"
            self.locknorth = True
            self.events["Muffet_Shop"] = Event("Muffet_Shop",True)

    class ruins_monstercandyroom(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Monster Candy Room"
            self.x = 10
            self.y = 4
            self.desc = "*A nice looking bowl of candy sits on a pillar in the center of the room.  A small note says 'Take only one.' There is a small passage in the back."
            self.bg = "background ruins_monstercandy_room"

    class ruins_snailhuntingroom(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Snail Hunting Room"
            self.x = 10
            self.y = 5
            self.desc = "* The small and brightly lit room sports a large bed of vegetation, fruit and vegetable bearing plants interspersed with various breeds of flowers. A crack in the roof of the cave allows for beams of sunlight from the surface to penetrate to the floor, encouraging the growth of the plants. You can see the spiraled shells of snails moving about the vegetation. The only way out is how you came in."
            self.bg = "background ruins_snailhunting_room"
            self.events["Random Snails"] = Event("Snail_Hunter_Random_Event",True)

    class ruins_tunneldivide(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Tunnel Divide"
            self.x = 12
            self.y = 4
            self.desc = "* A short hallway stretches before you, with paths leading off in different directions. Overgrown vines hang from the stone walls and a few, stray leaves crunch underfoot."
            self.bg = "background ruins_hallway"

    class ruins_overlook(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Overlook"
            self.x = 13
            self.y = 4
            self.desc = "* This dead-end makes for a spectacular view. Abandoned, overgrown buildings stretch before you as far as the eye can see."
            self.bg = "background ruins_toy_knife_room"
            self.locksouth = True

    class ruins_blacktreeroom(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Black Tree Room"
            self.x = 12
            self.y = 5
            self.desc = "* The long room houses a large and majestic looking, black barked tree. Its boughs are bare but surrounded by large quantities of red leaves. The room itself is dusted with drifts of the same leaves that fill the corners and layer the front of the quaint little house at the opposite end of the room. The house looks warm and inviting."
            self.bg = "background ruins_outside_house"

    class ruins_to_toriel_house(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Exit"
            self.x = 12
            self.y = 6
            self.desc = ""
            self.bg = ""
            self.mappable = False
            self.events["port_to_toriel_house"] = Event("port_to_toriel_house",True)
    
label port_to_toriel_house:
    "Toriels House"
    $ world.move_to_room("Staircase")

label dead_room:
    #show wilson scary
    #"{size=+5}{font=font/Pixelated_Wingdings.ttf}You   SHOULDN'T    BE     HERE{/font}"
    return