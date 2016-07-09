init:
#flowerbed
    image background ruins_caveroom = "backgrounds/Ruins/background-ruins-flowerpatch.jpg"
    image background ruins_floweyroom = "backgrounds/Ruins/background-ruins-floweyroom.jpg"

#the ruins
    image background ruins_outside_house = "backgrounds/Ruins/background-ruins-blacktree.png"
    image background ruins_froggit_room = "backgrounds/Ruins/background-ruins-froggitroom.png"
    image background ruins_first_entrance = "backgrounds/Ruins/background-ruins-firstentrance.jpg"
    image background ruins_toy_knife_room = "backgrounds/Ruins/background-ruins-toykniferoom.jpg"
    image background ruins_spider_bakery = "backgrounds/Ruins/background-ruins-spiderbakery.jpg"
    image background ruins_sassyrock_room = "backgrounds/Ruins/background-ruins-sassyrock.png"
    image background ruins_blooky_room = "backgrounds/Ruins/background-ruins-blookyroom.png"


init -1 python:
    
    random_rooms = []
    class ruins_caveroom(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Cave Room"
            self.x = 10
            self.y = 0
            self.desc = "The large cavern you are in is lit by the light coming from far above, shining into the corners of the cave and illuminating the path of flowers that broke your fall. There is one exit from the cavern, a large, ornate doorway leading to another cave."
            self.bg = "background ruins_caveroom"

    class ruins_grassroom(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Grass Room"
            self.x = 9
            self.y = 0
            self.desc = "Littering the edges of the much smaller cave are mounds of trash, a few pieces sparkling in the sparse light filtering through a crack in the ceiling. The scattered sunshine feeds a small mound of grass in the center of the cave and illuminates one exit from the cavern… though the other exit seems to be covered by a curtain of vines."
            self.bg = "background ruins_floweyroom"

    class ruins_ruinsentrance(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Ruins Entrance"
            self.x = 9
            self.y = 1
            self.desc = "The long stone hallway’s floor is covered in red leaves, gathered in drifts in corners or scattered across the path that leads to a set of curving staircases. The stairs climb up to a landing that supports a large, ivy covered building, its entrance yawning darkly and flanked by two high windows."
            self.bg = "background ruins_first_entrance"

    class ruins_tunnels(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Tunnels"
            self.x = 9
            self.y = 2
            self.desc = "The tunnels criss-crossing through the various rooms you pass through are riddled with what appear to be disabled traps and puzzles."
            self.bg = "background ruins_caveroom"


    class ruins_dummyroom(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Dummy Room"
            self.x = 9
            self.y = 3
            self.desc = "The small, curved room has a much lower ceiling than the caves before it, and houses a training dummy, set up beside the arched doorway leading on to further rooms, as well as a ghost that seems to be speaking to the dummy. The dummy looks friendly, a smile sewn into its burlap face, but the ghost looks almost… scared."
            self.bg = "background ruins_caveroom"

    class ruins_froggitleaves(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Froggit Room"
            self.x = 10
            self.y = 3
            self.desc = "The bricked hall’s path zig-zags its way around several large piles of red leaves, passing walls hung with several flourishing ivy plants to lead out the exit at the far end of the room. There is a waist high frog reclining in one of the corners of the room, looking worried."
            self.bg = "background ruins_froggit_room"
  
    class ruins_sassyrock(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Sassy Rock Room"
            self.x = 11
            self.y = 3
            self.desc = "The room before you is long and filled with odd items. There is a sign hanging on the wall closest to you, three grey rocks set on top of strange square pads on the ground, and a moat crossing the opposite side of the hall, a short bridge extended across the still water. There is an exit across the bridge."
            self.bg = "background ruins_sassyrock_room"

    class ruins_blookyroom(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Blooky Room"
            self.x = 12
            self.y = 3
            self.desc = "The room is average sized and divided by a wall halfway through, separating the side of the room you are on from two exits on the other side. There is a narrow opening in the wall, it’s floor spread with a scattering of red leaves."
            self.bg = "background ruins_blooky_room"

    class ruins_spiderbakery(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Spider Bakery"
            self.x = 13
            self.y = 3
            self.desc = "The small room feels and smells homey, despite being covered ceiling to floor with cobwebs; there is a permeating scent of baked goods coming from somewhere within. A sign has been erected in front of two of the densest clusters of webbing. The only way out is how you came in."
            self.bg = "background ruins_spider_bakery"
            self.locknorth = True
    class ruins_snailhuntingroom(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Snail Hunter"
            self.x = 10
            self.y = 4
            self.desc = "The small, brightly lit room sports a large bed of vegetation, fruit and vegetable bearing plants interspersed with various breeds of flower. A crack in the roof of the cave allows beams of sunlight from the surface to penetrate to the floor, encouraging the growth of the plants. You can see the spiraled shells of snails moving about the vegetation. The only way out is how you came in."
            self.bg = "background ruins_caveroom"

    class ruins_tunneldivide(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Tunnel Divide"
            self.x = 12
            self.y = 4
            self.desc = "The tunnel here splits into two, one offshoot leading north and the other east."
            self.bg = "background ruins_caveroom"

    class ruins_overlook(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Overlook"
            self.x = 13
            self.y = 4
            self.desc = "The balcony in this three walled room looks out over a vast, seemingly abandoned city, empty house windows staring back at you. There is a child sitting quietly in the corner, looking at the plastic knife they holding blankly. They don’t appear to have noticed you. The only way out is how you came in."
            self.bg = "background ruins_toy_knife_room"
            self.locksouth = True

    class ruins_blacktreeroom(Room):
        def __init__(self):
            Room.__init__(self)
            self.name = "Black Tree Room"
            self.x = 12
            self.y = 5
            self.desc = "The long room houses a large, majestic looking, black barked tree, it’s boughs bare but surrounded by large quantities of red leaves. The room itself is dusted with drifts of the same leaves, filling the corners and layering the front of the quaint little house at the opposite end of the room. The house looks warm and inviting."
            self.bg = "background ruins_outside_house"


    
   


    

    
