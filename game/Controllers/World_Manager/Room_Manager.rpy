init -10 python:
    class Room():
        def __init__(self,name = 'default', x = 0, y=0 , desc = 'default',locked = False, bg = "background deadroom"):
            self.name = name
            self.x = x
            self.y = y
            self.desc = desc
            self.visited = False
            self.ignore = False # Ignore room for the purposes of 100% exploration
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


        #this function will add an event to the rooms queue.
        def add_event(self,event,permanent,time=0):
            if renpy.has_label(event):
                self.events[event] = Event(event,permanent,time)
            else:
                renpy.notify("Can't find label [event]")

        #this function removes all events and replaces them with the given one.
        def set_event(self,event,permanent):
            if renpy.has_label(event):
                self.events = {}
                self.events[event] = Event(event,permanent)
#                renpy.say(None,"Setting Event %s in %s" % (event,self.name))
            else:
                renpy.notify("Can't find label [event]")

        #is used for the map to see if it should show events        
        def has_events(self):
            for event_name,e in self.events.iteritems():
                if e.completed == False or e.permanent:
                    return True
            return False

        #empty the room of events
        def clear_events(self):
            self.events = {}
        
        def reset_permanent_events(self):
            for event_name,event in self.events.iteritems():
                if event.permanent:
                    event.completed = False
                    
        #First check to see if the room itself has an event to do
        #Then check to see if the room has a monster event to do
        def get_event(self):

            self.current_monster = False
            has_event = False
            has_monster = False
            for event_name,event in self.events.iteritems():
                if event.completed == False:
                    has_event = event
            for m in self.monsters:

                if m.get_current_event():
                    if m.get_current_event().completed == False or m.get_current_event() == m.default_event:
                        self.current_monster = m
                        has_monster = m.get_current_event()

            if has_event and has_monster:
                return Event("multiple_monster",True,arg=has_event)
            elif has_event:
                return has_event
            elif has_monster:
                return has_monster
            else:
                return False

        def add_monster(self,Monster):
            Monster.current_room = self
            self.monsters.append(Monster)

        def remove_monster(self,Monster):
            self.monsters.remove(Monster)


label current_room_description:
    python:
        for line in world.current_area.current_room.desc:
            renpy.say(None,line)


label multiple_monster(event):
    
    call show_buttons
    menu:
        "Check the room":
            $ event.call_event()
        "Talk to Frisk " if get_frisk() in world.current_area.current_room.monsters:
            $ get_frisk().get_current_event().call_event()
            hide frisk
        "Talk to Napstablook " if get_napstablook() in world.current_area.current_room.monsters:
            $ get_napstablook().get_current_event().call_event()
            hide napstablook
        "Talk to Toriel " if get_toriel() in world.current_area.current_room.monsters:
            $ get_toriel().get_current_event().call_event()
            hide toriel
        "Talk to Flowey " if get_flowey() in world.current_area.current_room.monsters:
            $ get_flowey().get_current_event().call_event()
            hide flowey

    $ world.current_area.current_room.reset_permanent_events()
    return


