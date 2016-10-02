label default_event:
    "You shouldn't see this.  Its the default. Tell Wilson."
    return

init -10 python:
    import random

    class World():
    
        def __init__(self):
            self.name = "Underground"
            self.areas = {}
            self.currentArea = False
            self.maxTime = 1440
            self.currentTime = 700
            self.day = 1
            self.timeZones = {"Night":0,"Morning":480,"Day":720,"Afternoon":960,"Evening":1200}
            self.days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
            self.generate_ruins()
            self.areas["Toriel_House"] = Toriel_House()

        def get_current_timezone(self):
            
            timezone = "Night"
            for t,z in self.timeZones.iteritems():
                if self.currentTime >= z and self.timeZones[timezone] < z:
                    timezone = t

            return timezone

        #this function should be called at the beginning of every day.
        #it will update all of the areas for whatever we need.
        def update_day(self):
            #self.seed_random_monsters()
            return

        def get_current_day(self):
            return self.days[self.day % 7]
        #this function will seed all of the random monsters to the various rooms they can be in.
        #rooms with events already in them should be ignored.
        def seed_random_monsters(self):
            for a in self.areas:
                #we need to add each random monster to a different room

                #first we get a list of all the rooms in the area
                room_list = list(a.rooms)
                #now we remove every room that has an event, or another monster in it
                for r in room_list:
                    if len(r.monsters) > 0 or len(r.events) > 0:
                        room_list.remove(r)

                #now we seed the monsters into random rooms in the list, removing each room as we do it.
                #we will do this until we run out of rooms
                random.shuffle(a.random_monsters)
                random.shuffle(room_list)
                for m in a.random_monsters:
                    if len(room_list) > 0:
                        m.move_to_room(room_list[0].name)
                        room_list.remove(room_list[0])

            return

        def update_world(self,update_day = False):

            timezone = self.get_current_timezone()
            day = self.get_current_day()
            for an,a in self.areas.iteritems():
                for rn,r in a.rooms.iteritems():
                    for m in r.monsters:
                        if m.schedule:

                            if timezone in m.schedule[day]:
                                for x,t in m.schedule[day][timezone].iteritems():
                                    m.move_to_room(x)
                            else:
                                m.move_to_room(m.default_room)

            if update_day:
                self.update_day()

            return

        def get_current_time(self):
            seconds = self.currentTime * 60
            m, s = divmod(seconds, 60)
            h, m = divmod(m, 60)
            return "%d:%02d" % (h, m)

        #sets the current time
        def set_current_time(self,time,update_day = False):

            if time > 1440 or time < 0:
                renpy.notify("Time too high or negative for set_current_time.")
                return

            if update_day:
                self.day += 1


            self.currentTime = time


            self.update_world(update_day)


        #Adds minutes to the current time
        #Updates current day if time goes over
        def update_current_time(self,amount):

            #check to see if we added more than one day

            new_time = self.currentTime + amount
            update_day_check = False

            if new_time > self.maxTime:
                self.day += 1
                new_time -= self.maxTime
                update_day_check = True
            if new_time < 0:
                self.day -= 1
                new_time += self.maxTime
                update_day_check = True

            self.currentTime = new_time
            self.update_world(update_day_check)
            renpy.call("load_room")

        def move_to_room(self,name):
            for area_name,area in self.areas.iteritems():
                for room_name,room in area.rooms.iteritems():
                    if room.name == name:
                        self.currentArea = area
                        self.currentArea.currentRoom = room
                        renpy.jump("load_room")
                        break
            renpy.notify(name + " not found.")
        def get_room(self,name):
            for area_name,area in self.areas.iteritems():
                for room_name,room in area.rooms.iteritems():
                    if room.name == name:
                        return room
                        
            renpy.notify(name + " not found.")
            return False

        def get_monster(self,name):
            for area_name,area in self.areas.iteritems():
                for room_name,room in area.rooms.iteritems():
                    for monster in room.monsters:
                        if monster.name.lower() == name.lower():
                            return monster

            renpy.notify("Could not find "+name);
            return False

        def add_monster(self,monster):
            if isinstance(monster,Monster):
                self.monster[monster.name] = monster
            else:
                renpy.notify("Illegal Type: not a Monster")

        def add_area(self,area):
            if isinstance(area,Area):
                self.areas[area.name] = area
            else:
                renpy.notify("Illegal Type: not an Area")

        def generate_ruins(self):
            self.add_area(TheRuins())
            self.currentArea = self.areas["The Ruins"]
            self.currentArea.currentRoom = self.currentArea.rooms["Grass Room"]




label test_label:
    "Awesome, it worked."
    return



#This is the label that handles the loading
#shows the current background, if the room hasn't been visited shows the description, sets visited to True, then Pauses to allow player to do things
label load_room:
    
    call hide_buttons

    python:
        cell_convo_count = 0
        renpy.scene()
        if world.currentArea.currentRoom.bg:
            renpy.show(world.currentArea.currentRoom.bg)

    with fade
    if not world.currentArea.currentRoom.visited and world.currentArea.currentRoom.desc:
        "[world.currentArea.currentRoom.desc]"
    $ world.currentArea.currentRoom.visited = True


    $ temp_event = world.currentArea.currentRoom.get_event()

    while temp_event:
        $ temp_event.call_event()
        $ temp_event = world.currentArea.currentRoom.get_event()
    
    while True:
        call show_buttons
        pause
    return








