init -10 python:
    
    class Monster():

        def __init__(self,name="bob"):
            self.name = name
            self.specialEvents = []
            self.schedule = {}
            self.currentRoom = None
            self.default_event = Event('default_event',self)
            self.FP_events = {}
            self.FP = False
            self.visited = False
            self.dialogue_toggle = False
            
        def move_to_room(self,room):
            for a in world.areas:
                for r in a.rooms:
                    if r.name == room:
                        #we found the room, so move them there
                        if self.currentRoom:
                            self.currentRoom.monsters.remove(self)
                        self.currentRoom = r
                        self.currentRoom.monsters.append(self)
                        return

            renpy.notify("Can't find room "+room)


        #will need to add math about the FP
        def get_current_event(self):
            timezone = world.get_current_timezone()
            if timezone in self.schedule:
                for x,t in self.schedule[timezone].iteritems():
                    return t
            return self.default_event
