label default_event:
    "You shouldn't see this.  Its the default. Tell Wilson."
    return
init -10 python:
    import random

    #CONVENIENCE FUNCTIONS
    # returns the current room.
    def current_room():
        return world.current_area.current_room

    #returns the current area
    def current_area():
        return world.current_area

    # Accepts a string of a room name and parses the world for that room.
    def get_room(name):
        return world.get_room(name)

    #moves the player to a room. Accepts the room name and a type of transition.
    def move_to_room(room,loop=True,transition="fade"):
        world.move_to_room(room,loop,transition)

    #brings a monster to the current room. monster == monster.name
    def summon(monster):
        world.get_monster(monster).move_to_room(current_room().name)
        reload_room()

    #sends a monster to the dead room.   handy for getting them out of a room quickly
    def banish(monster):
        world.get_monster(monster).move_to_room("Dead Room")
        reload_room()

    #runs all of the updates for the world
    def update():
        world.update_day()

    #Returns a monster by name
    def get_monster(monster):
        return world.get_monster(monster)

    #Locks the room to stop the player from getting in. True or False
    def set_lock_room(name,lock):
        if get_room(name):
            get_room(name).locked = lock
            return True
        else:
            renpy.notify(str(name) + " not found.")
            return False

    #this will set an event for the monster. It will activate when you first talk to them.
    def give_monster_event(monster_name,label_name):
        world.get_monster(monster_name).set_special_event(label_name)
        return

    #takes an item class    example : pickup_item(Heart_Locket())
    #these can be found in the various item files in the inventory folder
    def pickup_item(item):
        if isinstance(item,Item):
            if inventory.has_space():
                inventory.add(item)
                return True
            else:
                renpy.notify("No space.")
                return False
        else:
            renpy.notify("Not a valid item.")
            return False
    
    def reload_room():
        renpy.call("load_room")

    ##Getting tired of the convoluted way to call the monsters
    def get_flowey():
        return get_monster("Flowey")
    def get_toriel():
        return get_monster("Toriel")
    def get_frisk():
        return get_monster("Frisk")
    def get_napstablook():
        return get_monster("Napstablook")

    class World():
    
        def __init__(self):
            self.name = "Underground"
            self.areas = {}
            self.current_area = False
            self.maxTime = 1440
            self.currentTime = 700
            self.day = 1
            self.timeZones = {"Night":0,"Morning":480,"Day":720,"Afternoon":960,"Evening":1200}
            self.days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
            self.generate_ruins()
            self.areas["Toriel_House"] = Toriel_House()
            self.message = ""

        def get_current_timezone(self):
            
            timezone = "Night"
            for t,z in self.timeZones.iteritems():
                if self.currentTime >= z and self.timeZones[timezone] < z:
                    timezone = t

            return timezone

        #this function should be called at the beginning of every day.
        #it will update all of the areas for whatever we need.
        def update_day(self):
            #seed the random monsters
            # day 0 is the tutorial

            #if self.day > 0:
                #self.seed_random_monsters()
                #self.seed_random_events()
            
            #reset the gift counts
            for an,a in self.areas.iteritems():
                for rn,r in a.rooms.iteritems():
                    for m in r.monsters:
                        m.given_today_count = 0

            return

        def get_current_day(self):
            return self.days[self.day % 7]

        #this function will seed all of the random monsters to the various rooms they can be in.
        #rooms with events already in them should be ignored.
        def seed_random_monsters(self):
            for an,a in self.areas.iteritems():


                # #first we get a list of all the rooms in the area
                room_list = list(a.rooms)

                # #now we remove every room that has an event, or another monster in it
                for r in a.rooms:
                    if len(a.rooms[r].monsters) > 0 or len(a.rooms[r].events) > 0:
                        room_list.remove(r)
                        
                # #now we seed the monsters into random rooms in the list, removing each room as we do it.
                # #we will do this until we run out of rooms
                random.shuffle(a.random_monsters)
                random.shuffle(room_list)
                for m in a.random_monsters:
                    if len(room_list) > 0:
                        m.move_to_room(room_list[0])
                        room_list.remove(room_list[0])

        def seed_random_events(self):
            for an,a in self.areas.iteritems():
                 # #first we get a list of all the rooms in the area
                room_list = list(a.rooms)

                # #now we remove every room that has an event, or another monster in it
                for r in a.rooms:
                    if len(a.rooms[r].monsters) > 0 or len(a.rooms[r].events) > 0:
                        room_list.remove(r)
                        
                # #we will do this until we run out of rooms
                re = a.get_random_event()
                if re:
                    rr = renpy.random.choice(room_list)
                    a.rooms[rr].events[re.label] = re
                   
        #gets the current timezone and the day of the week
        #if set to update the day, cycles through each area,room, monster
        #each monster will move to their given room for their schedule.
        #if there is a special event, that will be done as well
        def update_world(self,update_day = False):

            timezone = self.get_current_timezone()
            day_of_week = self.get_current_day()

            if update_day:
                for an,a in self.areas.iteritems():
                    for rn,r in a.rooms.iteritems():
                        for m in r.monsters:
                            if m.schedule:

                                if timezone in m.schedule[day_of_week]:
                                    for x,t in m.schedule[day_of_week][timezone].iteritems():
                                        m.move_to_room(x)
                                else:
                                    m.move_to_room(m.default_room)

                            m.handle_special_events()

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

        def move_to_room(self,name,loop=True,transition="fade"):
            for area_name,area in self.areas.iteritems():
                for room_name,room in area.rooms.iteritems():
                    if room.name == name:
                        self.current_area = area
                        self.current_area.current_room = room
                        renpy.call("load_room",loop,transition)
                        return True
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
            self.current_area = self.areas["The Ruins"]
            self.current_area.current_room = self.current_area.rooms["Grass Room"]




label test_label:
    "Awesome, it worked."
    return



#This is the label that handles the loading
#shows the current background, if the room hasn't been visited shows the description, sets visited to True, then Pauses to allow player to do things
label load_room(loop=True,transition="fade"):
    
    call hide_buttons from _call_hide_buttons

    python:
        cell_convo_count = 0
        renpy.scene()
        if world.current_area.current_room.bg:
            renpy.show(world.current_area.current_room.bg)

    if transition == "fade":
        with Fade(.5,0,.5)
    else:
        $ renpy.notify(str(transition) + " not a valid option for transition")

    #if ADMIN_ROOM_DESC:
    if not world.current_area.current_room.visited and world.current_area.current_room.desc and world.day > 0:
        "[world.current_area.current_room.desc]"
    $ world.current_area.current_room.visited = True


    $ temp_event = world.current_area.current_room.get_event()

    while temp_event:
        $ temp_event.call_event()
        $ temp_event = world.current_area.current_room.get_event()
    
    if loop:
        while True:
            call show_buttons
            pause
    return








