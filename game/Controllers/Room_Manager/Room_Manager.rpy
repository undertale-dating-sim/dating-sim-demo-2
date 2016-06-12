init -1 python:
    wilson_locked = True
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

    class Room_Manager():
        def __init__(self):
            self.rooms = []
            #self.random_scenes = ['papyrus_random','sans_random','toriel_random','flowey_random']
        
        def add_room(self,room):
            self.rooms.append(room)

        def move_to_room(self,name):
            for r in self.rooms:
                if r.name == name:
                    self.current_room = r
                    break

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

            for room in self.rooms:
                if not room.locked:
                    if room.x == dirx and room.y == diry:

                        if room.visited:
                            player.time += 50
                            player.stamina -= 1
                        else:
                            player.time += 100
                            player.stamina -= 5

                        self.current_room = room
                        renpy.jump("load_room")


        def cr_get_neighbors(self):
            dirs = []

            for r in self.rooms:
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


    room_manager = Room_Manager()

label load_room:
    #scene background ruins_caveroom
    $ renpy.scene()
    $ room_manager.current_room.visited = True
    $ renpy.show(room_manager.current_room.bg)
    with fade
    "[room_manager.current_room.desc]"
    while True:
        pause
    return

screen show_nav_button:
    textbutton "Show Nav (E)" action [Play ("sound", "audio/sfx/click.wav"), Show("navigation_buttons"), Hide("show_nav_button")] align(.95,.1) background Frame("text-box3.png",50, 21)
    key 'e' action [Play ("sound", "audio/sfx/click.wav"), Show("navigation_buttons"), Hide("show_nav_button")]
screen navigation_buttons:
    add "#0008"
    modal True

    $dirs = room_manager.cr_get_neighbors()

    textbutton "Hide Nav (E)" action [Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button')] align(.95,.1) background Frame("text-box3.png",50, 21)
    key 'e' action [Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button')]
    if dirs.count('north') > 0:
        textbutton "north (w)" background Frame("text-box3.png",50, 21) align(0.5,0.0) action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(room_manager.move_dir,'north')]
        key 'w' action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(room_manager.move_dir,'north')]

    if dirs.count('south') > 0:
        textbutton "south (s)" background Frame("text-box3.png",50, 21) align(0.5,1.0) action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(room_manager.move_dir,'south')]
        key 's' action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(room_manager.move_dir,'south')]

    if dirs.count('east') > 0:
        textbutton "east (d)" background Frame("text-box3.png",50, 21) align(1.0,0.5)  action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(room_manager.move_dir,'east')]
        key 'd' action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(room_manager.move_dir,'east')]

    if dirs.count('west') > 0:
        textbutton "west (a)" background Frame("text-box3.png",50, 21) align(0.00,0.5) action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(room_manager.move_dir,'west')]
        key 'a' action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(room_manager.move_dir,'west')]

    text '[room_manager.current_room.name]' align(0.5,0.5)




