init -10 python:
    
    class Monster():

        def __init__(self,name="bob"):
            self.name = name
            self.specialEvents = []
            self.specialEvents.append(Event('test_label'))
            self.schedule = {}
            self.currentRoom = None
            
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

        def get_current_event(self):
            timezone = world.get_current_timezone()
            if timezone in self.schedule:
                for x,t in self.schedule[timezone].iteritems():
                    return t[x]
            return False



    class Area():

        def __init__(self,name):
            self.rooms = []
            self.currentRoom = False
            self.name = name
            #self.random_scenes = ['papyrus_random','sans_random','toriel_random','flowey_random']
        
        def add_room(self,room):
            self.rooms.append(room)

        def move_to_room(self,name):
            for r in self.rooms:
                if r.name == name:
                    self.currentRoom = r
                    break

        def move_dir(self,direction):
            dirx = self.currentRoom.x
            diry = self.currentRoom.y

            if direction == 'north':
                diry += 1
            if direction == 'east':
                dirx += 1
            if direction == 'south':
                diry -= 1
            if direction == 'west':
                dirx -= 1

            for room in self.rooms:
                if not room.locked:
                    if room.x == dirx and room.y == diry:

                        if room.visited:
                            player.time += 50
                            player.stamina -= 1
                        else:
                            player.time += 100
                            player.stamina -= 5

                        self.currentRoom = room
                        renpy.jump("load_room")


        def cr_get_neighbors(self):
            dirs = []

            for r in self.rooms:
                if r.x == self.currentRoom.x and r.y == self.currentRoom.y+1 and not r.locked and not r.locksouth:
                    dirs.append('north')
                    continue
                if r.x == self.currentRoom.x and r.y == self.currentRoom.y-1 and not r.locked and not r.locknorth:
                    dirs.append('south')
                    continue
                if r.x == self.currentRoom.x+1 and r.y == self.currentRoom.y and not r.locked and not r.lockwest:
                    dirs.append('east')
                    continue
                if r.x == self.currentRoom.x-1 and r.y == self.currentRoom.y and not r.locked and not r.lockeast:
                    dirs.append('west')

            return dirs

        def get_random_scene(self):
            
            s = False
            if len(self.random_scenes) > 0:
                if renpy.random.randint(0,100) < 101:
                    s = self.random_scenes[renpy.random.randint(0,len(self.random_scenes)-1)]
                        #remove so it doesn't happen again
                    self.random_scenes.remove(s)
                    if len(self.random_scenes) == 0 and wilson_locked:
                        renpy.call_in_new_context("wilson_unlock")
                    return s
            
            return s

    class Room():
        def __init__(self,name = 'default', x = 0, y=0 , desc = 'default',locked = False, bg = 'nothing'):
            self.name = name
            self.x = x
            self.y = y
            self.desc = desc
            self.visited = False
            #place holder to stop people from moving into the room.
            self.locked = locked
            self.bg = bg

            #stop people from leaving room in wrong direction
            self.locksouth = False
            self.locknorth = False
            self.lockeast = False
            self.lockwest = False
            self.events = []
            self.monsters = []


        #First check to see if the room itself has an event to do
        #Then check to see if the room has a monster event to do
        def has_event(self):

            for e in self.events:
                if e.completed == False:
                    return e
            for m in self.monsters:
                for e in m.specialEvents:
                    if e.completed == False:
                        return e

                if m.get_current_event():
                    return m.get_current_event()

            return False

        def add_monster(self,Monster):
            Monster.currentRoom = self
            self.monsters.append(Monster)

        def remove_monster(self,Monster):
            self.monsters.remove(Monster)


    class Event():
        def __init__(self,label = "flowey_hangout"):
            self.completed = False
            self.label = label
            self.owner = False


        def call_event(self):
            renpy.call_in_new_context(self.label)
            self.completed = True

    class World():

    
        def __init__(self):
            self.name = "Underground"
            self.areas = []
            self.currentArea = False
            self.maxTime = 1440
            self.currentTime = 0
            self.day = 1
            self.timeZones = {"Night":0,"Morning":480,"Day":720,"Afternoon":960,"Evening":1200}
            self.generate_ruins()

        def get_current_timezone(self):
            
            timezone = "Night"
            for t,z in self.timeZones.iteritems():
                if self.currentTime > z and self.timeZones[timezone] <= z:
                    timezone = t

            return timezone

        def update_world(self):

            timezone = self.get_current_timezone()
            renpy.notify(timezone)
            for a in self.areas:
                for r in a.rooms:
                    for m in r.monsters:
                        if timezone in m.schedule:
                            for x,t in m.schedule[timezone].iteritems():
                                m.move_to_room(x)



            return

        #sets the current time
        def set_current_time(self,time,update_day = False):

            if time > 1440 or time < 0:
                renpy.notify("Time too high or negative for set_current_time.")
                return

            if update_day:
                if self.currentTime > time:
                    self.day += 1

            self.currenttime = time


            self.update_world()


        #Adds minutes to the current time
        #Updates current day if time goes over
        def update_current_time(self,amount):

            #check to see if we added more than one day

            new_time = self.currentTime + amount

            if new_time > self.maxTime:
                day += 1
                new_time -= self.maxTime

            self.currentTime = new_time
            self.update_world()

        def add_monster(self,monster):
            if isinstance(monster,Monster):
                self.monsters.append()
            else:
                renpy.notify("Illegal Type: not a Monster")

        def add_area(self,area):
            if isinstance(area,Area):
                self.areas.append(area)
            else:
                renpy.notify("Illegal Type: not an Area")

        def generate_ruins(self):
            self.add_area(Area("The Ruins"))
            self.currentArea = self.areas[0]
            self.currentArea.add_room(ruins_caveroom())
            self.currentArea.add_room(ruins_grassroom())
            self.currentArea.add_room(ruins_ruinsentrance())
            self.currentArea.add_room(ruins_tunnels())
            self.currentArea.add_room(ruins_dummyroom())
            self.currentArea.add_room(ruins_froggitleaves())
            self.currentArea.add_room(ruins_sassyrock())
            self.currentArea.add_room(ruins_blookyroom())
            self.currentArea.add_room(ruins_spiderbakery())
            self.currentArea.add_room(ruins_snailhuntingroom())
            self.currentArea.add_room(ruins_tunneldivide())
            self.currentArea.add_room(ruins_overlook())
            self.currentArea.add_room(ruins_blacktreeroom())
            self.currentArea.currentRoom = self.currentArea.rooms[0]



label test_label:
    "Awesome, it worked."
    return
#This is the label that handles the loading
#shows the current background, if the room hasn't been visited shows the description, sets visited to True, then Pauses to allow player to do things
label load_room:
    $ renpy.scene()
    
    $ renpy.show(world.currentArea.currentRoom.bg)

    with fade
    $ world.update_current_time(200)
    if not world.currentArea.currentRoom.visited:
        "[world.currentArea.currentRoom.desc]"
    $ world.currentArea.currentRoom.visited = True

    $ temp_event = world.currentArea.currentRoom.has_event()

    while temp_event:
        $ temp_event.call_event()
        $ temp_event = world.currentArea.currentRoom.has_event()
    
    while True:
        pause
    return

screen show_nav_button:
    textbutton "Show Nav (E)" action [Play ("sound", "audio/sfx/click.wav"), Show("navigation_buttons"), Hide("show_nav_button")] align(.95,.1) background Frame("UI/text-box3.png",50, 21)
    key 'e' action [Play ("sound", "audio/sfx/click.wav"), Show("navigation_buttons"), Hide("show_nav_button")]
screen navigation_buttons:
    add "#0008"
    modal True

    $dirs = world.currentArea.cr_get_neighbors()

    textbutton "Hide Nav (E)" action [Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button')] align(.95,.1) background Frame("UI/text-box3.png",50, 21)
    key 'e' action [Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button')]
    if dirs.count('north') > 0:
        textbutton "north (w)" background Frame("UI/text-box3.png",50, 21) align(0.5,0.0) action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.currentArea.move_dir,'north')]
        key 'w' action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.currentArea.move_dir,'north')]

    if dirs.count('south') > 0:
        textbutton "south (s)" background Frame("UI/text-box3.png",50, 21) align(0.5,1.0) action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.currentArea.move_dir,'south')]
        key 's' action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.currentArea.move_dir,'south')]

    if dirs.count('east') > 0:
        textbutton "east (d)" background Frame("UI/text-box3.png",50, 21) align(1.0,0.5)  action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.currentArea.move_dir,'east')]
        key 'd' action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.currentArea.move_dir,'east')]

    if dirs.count('west') > 0:
        textbutton "west (a)" background Frame("UI/text-box3.png",50, 21) align(0.00,0.5) action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.currentArea.move_dir,'west')]
        key 'a' action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.currentArea.move_dir,'west')]

    text '[world.currentArea.currentRoom.name]' align(0.5,0.5)


#until we find a way to figure out what order the files are loaded in, all the rooms have to go in here.





