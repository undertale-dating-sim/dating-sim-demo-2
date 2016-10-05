init -10 python:
    class Room():
        def __init__(self,name = 'default', x = 0, y=0 , desc = 'default',locked = False, bg = "background deadroom"):
            self.name = name
            self.x = x
            self.y = y
            self.desc = desc
            self.visited = False
            #place holder to stop people from moving into the room.
            self.locked = locked
            self.bg = bg
            self.mappable = True

            #stop people from leaving room in wrong direction
            self.locksouth = False
            self.locknorth = False
            self.lockeast = False
            self.lockwest = False
            self.events = {}
            self.monsters = []
            self.current_monster = False



        def add_event(self,event,permanent):
            if renpy.has_label(event):
                self.events[event] = Event(event,permanent)
            else:
                renpy.notify("Can't find label [event]")

        #First check to see if the room itself has an event to do
        #Then check to see if the room has a monster event to do
        def get_event(self):

            for event_name,event in self.events.iteritems():
                if event.completed == False or event.permanent:
                    return event
            if len(self.monsters) > 1:
                return Event('multiple_monster',True)
            for m in self.monsters:

                if m.get_current_event():
                    if m.get_current_event().completed == False:
                        self.current_monster = m
                        return m.get_current_event()

            return False

        def add_monster(self,Monster):
            Monster.currentRoom = self
            self.monsters.append(Monster)

        def remove_monster(self,Monster):
            self.monsters.remove(Monster)

screen multiple_monster_click_screen:
    $ count = 1

    $ width = (1.0/(len(world.currentArea.currentRoom.monsters)))
    for monster in world.currentArea.currentRoom.monsters:
        $ x = count * width
        mousearea:
            area ((count-1)* width, .4, width, .6)
            hovered [SetVariable('talking',monster.name),Notify(monster.name)]

        $ count+= 1

        #unhovered SetVariable('talking',False)
    # mousearea:
    #     area (.33, 0, .33, 1.0)
    #     hovered [SetVariable('talking',world.currentArea.currentRoom.monsters[1].name),Notify(world.currentArea.currentRoom.monsters[1].name)]
    #     #unhovered SetVariable('talking',False)

    # mousearea:
    #     area (.66, 0, .33, 1.0)
    #     hovered [SetVariable('talking',world.currentArea.currentRoom.monsters[2].name),Notify(world.currentArea.currentRoom.monsters[2].name)]
    #     #unhovered SetVariable('talking',False)


    #     #hovered Show("buttons", transition=dissolve)
    #     #unhovered Hide("buttons", transition=dissolve)

label multiple_monster:
    
    #show the background
    call show_buttons
    show screen multiple_monster_click_screen
    python:
        renpy.scene()
        if world.currentArea.currentRoom.bg:
            renpy.show(world.currentArea.currentRoom.bg)
    #for each monster, we need to figure out where to put them
    while True:
        python:
            count = 1
            
            for monster in world.currentArea.currentRoom.monsters:
                width = (1.0/(len(world.currentArea.currentRoom.monsters)+1))
                x = count * width
                
                if monster.name != talking:
                    renpy.show(monster.default_sprite,[Position(xpos = x, xanchor = 'center')])


                count += 1  
        if talking:
            pause
        else:
            pause 1.0
        if talking:
            call expression world.get_monster(talking).default_event.label pass(world.get_monster(talking),False)
 
    return