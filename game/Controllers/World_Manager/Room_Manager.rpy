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