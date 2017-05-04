init -10 python:
    class Area():

        def __init__(self,name):
            self.rooms = {}
            self.current_room = False
            self.name = name
            self.random_areas = {}
            self.random_monsters = []
            self.random_events = []
    
        #Adds a room to the area. Needs to be an instance of Room()        
        def add_room(self,room):
            self.rooms[room.name] = room

        #Moves the player to the given room, accepts room.name
        def move_to_room(self,name):
            for r in self.rooms:
                if r.name == name:
                    self.current_room = r
                    renpy.jump("load_room")
                    break

        #Looks in the given direction to see if the player can move that way on the map, then moves them.
        def move_dir(self,direction):
            dirx = self.current_room.x
            diry = self.current_room.y

            if direction == 'north':
                diry += 1
            if direction == 'east':
                dirx += 1
            if direction == 'south':
                diry -= 1
            if direction == 'west':
                dirx -= 1

            for room_name,room in self.rooms.iteritems():
                if not room.locked:
                    if room.x == dirx and room.y == diry:

                        self.current_room = room
                        renpy.jump("load_room")

        #gets a random monster by name
        def get_random_monster(self,name):
            for x in self.random_monsters:
                if x.name == name:
                    return x

            return False

        #gets the rooms surrounding the current room
        def cr_get_neighbors(self):
            dirs = []

            for r_name,r in self.rooms.iteritems():
                if r.x == self.current_room.x and r.y == self.current_room.y+1 and not r.locked and not r.locksouth:
                    dirs.append('north')
                    continue
                if r.x == self.current_room.x and r.y == self.current_room.y-1 and not r.locked and not r.locknorth:
                    dirs.append('south')
                    continue
                if r.x == self.current_room.x+1 and r.y == self.current_room.y and not r.locked and not r.lockwest:
                    dirs.append('east')
                    continue
                if r.x == self.current_room.x-1 and r.y == self.current_room.y and not r.locked and not r.lockeast:
                    dirs.append('west')

            return dirs

        #gets a random event that hasn't been completed yet.
        def get_random_event(self):

            random_select = []
            
            for event in self.random_events:
                if not event.completed:
                    random_select.append(event)

            if len(random_select) > 0:
                return renpy.random.choice(random_select)
            else:
                return False