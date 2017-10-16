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

    #sends a monster to the dead room.   handy for getting them out of a room quickly
    def banish(monster):
        world.get_monster(monster).move_to_room("Dead Room")

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
            #self.maxTime = 1440
            self.current_timezone = "Morning"
            self.day = 0
            self.timezones = ["Morning","Day","Afternoon","Evening","Night"]
            self.days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
            self.generate_ruins()
            self.areas["Toriel_House"] = Toriel_House()
            self.message = ""
            self.timezone_action_count = 0

        def get_current_timezone(self):

            return self.current_timezone

        #this function should be called at the beginning of every day.
        #it will update all of the areas for whatever we need.
        def start_the_day(self):
            #seed the random monsters
            # day 0 is the tutorial
            #renpy.say(None,"Updating the Day : Random monsters and events. Resetting Gift counts")
            if self.day > 0:
                #renpy.say(None,"Current action count is %s/10" % self.timezone_action_count)
                if self.timezone_action_count >= 10:
                    self.timezone_action_count = 0
                    self.next_timezone()
                self.seed_random_monsters()
                self.seed_random_events()
            
            #reset the gift counts
            for an,a in self.areas.iteritems():
                for rn,r in a.rooms.iteritems():
                    for m in r.monsters:
                        m.given_today_count = 0

            return

        #gets the current timezone and the day of the week
        #if set to update the day, cycles through each area,room, monster
        #each monster will move to their given room for their schedule.
        #if there is a special event, that will be done as well
        def update_world(self):
            # renpy.say(None,"Updating the World : Main Monster Schedules/Events")
            timezone = self.get_current_timezone()
            day_of_week = self.get_current_day()


            for an,a in self.areas.items():
                room_list = list(a.rooms.items())
                for rn,r in room_list:
                    #if(len(r.monsters) > 0):
                    # renpy.say(None,"%s in %s" % (len(r.monsters),r.name))
                    monster_list = list(r.monsters)
                    for m in monster_list:
                        # renpy.say(None,"Found %s in %s" % (m.name,r.name))
                        if m.schedule:
                            if timezone in m.schedule[day_of_week]:
                                for x,t in m.schedule[day_of_week][timezone].items():    
                                    # (None,"Schedule : %s goes to %s at %s on %s" % (m.name,x,timezone,day_of_week))
                                    m.move_to_room(x)
                            else:
                                # renpy.say(None,"Found %s in %s" % (m.name,r.name))
                                # renpy.say(None,"Schedule : %s has no room for %s on %s. Default is %s" % (m.name,timezone,day_of_week,m.default_room))
                                m.move_to_room(m.default_room)
                        m.handle_special_events()

            return

        def get_current_day(self):
            return self.days[self.day % 7]

        #this function will seed all of the random monsters to the various rooms they can be in.
        #rooms with events already in them should be ignored.
        def seed_random_monsters(self):
            # renpy.say(None,"Setting up the random monsters")
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
            # renpy.say(None,"Seeding Random Events")
            for an,a in self.areas.iteritems():
                # renpy.say(None,"Checking %s" % a.name)
                 # #first we get a list of all the rooms in the area
                room_list = list(a.rooms)

                # #now we remove every room that has an event, or another monster in it
                for r in a.rooms:
                    if len(a.rooms[r].monsters) > 0 or len(a.rooms[r].events) > 0:
                        room_list.remove(r)
                        
                # renpy.say(None,"Getting Random Event")
                re = a.get_random_event()
                
                if re:
                    # renpy.say(None,"Got %s" % re.label)
                    rr = renpy.random.choice(room_list)
                    a.rooms[rr].set_event(re.label,False)
                    # renpy.say(None,"Added it to %s" % a.rooms[rr].name)
                    # a.rooms[rr].events[re.label] = re
                   

        def get_current_time(self):

            if self.current_timezone == 'Morning':
                return "8:00"
            if self.current_timezone == 'Day':
                return "12:00"
            if self.current_timezone == 'Afternoon':
                return "4:00"
            if self.current_timezone == 'Evening':
                return "8:00"
            if self.current_timezone == 'Night':
                return "0:00"

        def next_timezone(self):
            # renpy.say(None,"Getting Next Time Zone")
            if self.current_timezone == "Night":
                self.current_timezone = "Morning"
            else:
                self.current_timezone = self.timezones[self.timezones.index(self.current_timezone)+1]
            self.update_world()

        #sets the current time
        def set_current_time(self,timezone,go_to_next_day = False):

            if timezone not in self.timezones:
                renpy.notify("Timezone not found.")
                return

            if go_to_next_day:
                self.day += 1


            self.current_timezone = timezone


            self.update_world()

        def move_to_room(self,name,loop=True,transition="fade"):
            for area_name,area in self.areas.iteritems():
                for room_name,room in area.rooms.iteritems():
                    if room.name == name:
                        self.current_area = area
                        self.current_area.current_room = room
                        if self.timezone_action_count >= 10:
                            self.timezone_action_count = 0
                            self.next_timezone()
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

            renpy.notify("Could not find "+name)
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
            rooms_explored = 1




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
        with Fade(.5,0,.5)

    #if ADMIN_ROOM_DESC:
    if not world.current_area.current_room.visited and world.current_area.current_room.desc and world.day > 0:
        python:
            for line in world.current_area.current_room.desc:
                renpy.say(None,line)
    $ player.current_room = world.current_area.current_room.name
    $ blook_room = world.get_monster('Napstablook').current_room.name
    #"[blook_room]"


    python:
        
        unexplored_rooms = False
        ruinscounter = 0
        curr_area = current_area()
        for room_name,room in curr_area.rooms.iteritems():              # For a room in the current area,
            if not world.current_area.rooms[room.name].visited:         # Check if it has not been visited.
                world.current_area.current_room.visited = True          # If so, mark as visited.
                if world.current_area.rooms[room.name].ignore:          # Check if it counts for exploration/game completion
                    pass
                else:
                    unexplored_rooms = True                             # If there's still more rooms to be explored, flag area as not fully explored.
                    #ruinscounter += 1 ##### FOR TESTING #####
            else:
                pass
                    
        if unexplored_rooms is True:                                    # If all rooms have been explored, nothing will have triggered the unexplored_rooms flag.
        #if ruinscounter < 14:
            pass
        else:
            world.current_area.explored = True                          # This means that the player has 100% completed exploration.

    $ temp_event = world.current_area.current_room.get_event()

    while temp_event:
        #$ renpy.say(None,temp_event.label)
        $ temp_event.call_event()
        $ temp_event = world.current_area.current_room.get_event()
    
    if loop:
        while True:
            call show_buttons
            pause
    return








